"""Auto-launch Home v1 when the TV is already on (external workaround, no root).

Tizen does not allow replacing the launcher or native autostart, and a
powered-off TV has no 8001/8002 listening. This script runs on any always-on
box on the same LAN (PC, Raspberry Pi): it polls http://<host>:8001/api/v2/
until the TV answers, then launches the sideloaded Home via REST
POST /api/v2/applications/<app> (http 8001, no token needed, works for
dev-mode apps like HkTvHome01.Home where websocket DEEP_LINK is ignored).

The TV IP can change by DHCP: set a DHCP reservation in the router and/or
pass the current IP with --host each run.

Examples:
  python tools/auto_home.py --host <TV_IP> --dry-run
  python tools/auto_home.py --host <TV_IP> --app HkTvHome01.Home
  python tools/auto_home.py --host <TV_IP> --timeout 120 --interval 3 --settle 5
  # Raspberry Pi always-on:
  #   nohup python3 tools/auto_home.py --host <TV_IP> --timeout 600 &
"""
import argparse
import os
import sys
import time
import urllib.request

DEFAULT_TOKEN_FILE = os.path.join(os.path.dirname(__file__), "..", ".tv-token.txt")
DEFAULT_APP_ID = "HkTvHome01.Home"


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Wait for TV power-on then launch Home v1 (external autorun)")
    ap.add_argument("--host", required=True, help="TV IP, e.g. 192.168.1.50")
    ap.add_argument("--app", default=DEFAULT_APP_ID, help=f"app id to launch (default {DEFAULT_APP_ID})")
    ap.add_argument("--port", type=int, default=8001, help="REST port for launch: 8001 http (no cert warning) or 8002 https")
    ap.add_argument("--token-file", default=os.path.abspath(DEFAULT_TOKEN_FILE), help="kept for compat with remote.py; REST launch does not need it")
    ap.add_argument("--timeout", type=int, default=120, help="max seconds to wait for TV HTTP up")
    ap.add_argument("--interval", type=float, default=3.0, help="seconds between HTTP probes")
    ap.add_argument("--settle", type=float, default=5.0, help="extra seconds to wait after HTTP up before REST launch")
    ap.add_argument("--dry-run", action="store_true", help="wait for TV but do not send REST launch")
    return ap


def wait_for_tv(host: str, timeout: int, interval: float) -> bool:
    url = f"http://{host}:8001/api/v2/"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=5) as res:
                if res.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(interval)
    return False


def main() -> int:
    args = build_parser().parse_args()
    print(f"Waiting for TV at {args.host}:8001 (timeout {args.timeout}s)...")
    up = wait_for_tv(args.host, args.timeout, args.interval)
    if not up:
        print(f"ERROR: TV did not answer at {args.host}:8001 within {args.timeout}s", file=sys.stderr)
        return 1
    print(f"TV is up. Settling {args.settle}s before launch...")
    if args.settle > 0 and not args.dry_run:
        time.sleep(args.settle)
    if args.dry_run:
        print(f"DRY-RUN would POST http://{args.host}:8001/api/v2/applications/{args.app} (REST, no token needed)")
        return 0
    try:
        from samsungtvws import SamsungTVWS
    except ImportError:
        print("ERROR: samsungtvws not installed. Run: pip install -r requirements.txt", file=sys.stderr)
        return 2
    print(f"Launching app {args.app} via REST POST http://{args.host}:8001/api/v2/applications/{args.app}")
    tv = SamsungTVWS(host=args.host, port=args.port, token_file=args.token_file)
    print(tv.rest_app_run(args.app))
    print(f"Launch sent via REST. Token file {args.token_file} not needed for REST — keep private, never commit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
