"""WiFi remote for Samsung Tizen (8001/8002 websocket).

Read-only by default. Sending a key requires explicit --key and an
on-TV Allow prompt on first connect (token is cached locally, never committed).
"""
import argparse
import os
import sys

DEFAULT_TOKEN_FILE = os.path.join(os.path.dirname(__file__), "..", ".tv-token.txt")


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Samsung Tizen WiFi remote (safe defaults)")
    ap.add_argument("--host", required=True, help="TV IP, e.g. 192.168.1.50")
    ap.add_argument("--port", type=int, default=8002, help="8002 (wss, modern) or 8001 (ws)")
    ap.add_argument("--token-file", default=os.path.abspath(DEFAULT_TOKEN_FILE))
    ap.add_argument("--key", default=None, help="remote key to send, e.g. KEY_MENU, KEY_HOME, KEY_UP")
    ap.add_argument("--app", default=None, help="app id to launch, e.g. 3201606009684 (Spotify)")
    ap.add_argument("--dry-run", action="store_true", help="print what would be sent, do not connect")
    return ap


def main() -> int:
    args = build_parser().parse_args()
    plan = {"host": args.host, "port": args.port, "key": args.key, "app": args.app}
    if args.dry_run or (not args.key and not args.app):
        print(f"DRY-RUN plan: {plan} token_file={args.token_file}")
        if not args.key and not args.app:
            print("No action requested. Use --key KEY_MENU or --app <appId>.")
        return 0
    try:
        from samsungtvws import SamsungTVWS
    except ImportError:
        print("ERROR: samsungtvws not installed. Run: pip install -r requirements.txt", file=sys.stderr)
        return 2
    tv = SamsungTVWS(host=args.host, port=args.port, token_file=args.token_file)
    if args.key:
        print(f"Sending key {args.key} to {args.host}:{args.port} (confirm Allow on TV if first time)")
        tv.send_key(args.key)
    if args.app:
        print(f"Launching app {args.app}")
        tv.run_app(args.app)
    print(f"Token cached at {args.token_file} — keep private, never commit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
