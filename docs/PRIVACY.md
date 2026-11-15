# Privacy — never publish these

**English** | [Español](PRIVACY.es.md)

This repo is designed to be public-safe, but the TV world is full of device-bound
secrets. Keep this list next to you.

## Never commit or paste anywhere public

- TV **DUID** / UDID (`uuid:…`), device `id`, `udn`.
- **WiFi MAC**, AP BSSID/MAC, serials, `wifiMac`, `ssid` of your access point.
- Remote-control **tokens** (`.tv-token.txt`), `--raw` probe dumps.
- Certificates: `author.p12`, `distributor.p12`, signing passwords, profiles.
- Samsung account email / password (you sign in in your own browser only).
- Signed `.wgt` files built with your distributor cert (they embed your DUID).
- Screenshots/photos showing any of the above.

## Conventions used in this repo

- `<TV_IP>` / `<PC_IP>` placeholders everywhere; no real LAN addresses.
- `tv_info.py` redacts DUID/MAC/AP fields by default; `--raw` is for your eyes only.
- `odd/` (work log with real values) is gitignored and never published.
- When reporting a bug upstream: model + Tizen version + sanitized message only.

## If you leaked something

Revoke/replace it: new distributor cert, new token (delete `.tv-token.txt` and
re-allow), new passwords. Removing a commit is not enough — rotate the secret.
