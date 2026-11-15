"""Read-only TV info probe (no remote keys, no install).

Fetches GET http://<host>:8001/api/v2/ and prints a sanitized summary.
DUID, UDN, MACs and AP identifiers are redacted by default.
"""
import argparse
import json
import sys
import urllib.request

SENSITIVE_KEYS = {"id", "udn", "duid", "wifiMac", "ssid", "mac"}


def sanitize_device(payload: dict) -> dict:
    device = dict(payload.get("device", {}))
    for key in list(device.keys()):
        low = key.lower()
        if key in SENSITIVE_KEYS or low in {"duid", "udn", "wifimac", "ssid"} or "mac" in low:
            device[key] = "[redacted]"
    out = {
        "modelName": payload.get("device", {}).get("modelName"),
        "model": payload.get("device", {}).get("model"),
        "os": payload.get("device", {}).get("OS"),
        "power": payload.get("device", {}).get("PowerState"),
        "tokenAuth": payload.get("device", {}).get("TokenAuthSupport"),
        "developerMode": payload.get("device", {}).get("developerMode"),
        "network": payload.get("device", {}).get("networkType"),
        "resolution": payload.get("device", {}).get("resolution"),
        "apiVersion": payload.get("version"),
        "device_sanitized": device,
    }
    return out


def fetch(host: str, timeout: int = 8) -> dict:
    url = f"http://{host}:8001/api/v2/"
    with urllib.request.urlopen(url, timeout=timeout) as res:
        return json.loads(res.read().decode("utf-8", "replace"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Samsung Tizen read-only info probe")
    ap.add_argument("--host", required=True, help="TV IP, e.g. 192.168.1.22")
    ap.add_argument("--raw", action="store_true", help="print raw JSON (contains private IDs, do not publish)")
    args = ap.parse_args()
    try:
        data = fetch(args.host)
    except Exception as e:  # noqa: BLE001 - CLI surface
        print(f"ERROR: cannot reach TV at {args.host}:8001: {e}", file=sys.stderr)
        return 1
    if args.raw:
        print(json.dumps(data, indent=2))
    else:
        print(json.dumps(sanitize_device(data), indent=2))
        print("\nNote: DUID/MAC/AP identifiers redacted. Do not publish --raw output.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
