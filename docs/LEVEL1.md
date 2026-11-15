# Level 1 — WiFi control (8001/8002 websocket)

**English** | [Español](LEVEL1.es.md)

Official local remote-control channel. Read-only first, keys only when you say so.
Your computer and the TV must share the same subnet.

## Probe (read-only, always safe)

```powershell
python tools/tv_info.py --host <TV_IP>
```

Prints a **sanitized** summary (model, Tizen, power, TokenAuth, developerMode…).
DUID / MAC / AP identifiers are redacted. Never publish `--raw` output.

## Dry run (no connection)

```powershell
python tools/remote.py --host <TV_IP> --dry-run
```

## Send a key (needs on-TV Allow once)

```powershell
pip install -r requirements.txt
python tools/remote.py --host <TV_IP> --port 8002 --key KEY_MENU
```

Useful keys: `KEY_HOME`, `KEY_MENU`, `KEY_UP/DOWN/LEFT/RIGHT`, `KEY_ENTER`,
`KEY_RETURN`, `KEY_HDMI1`… The first connect raises **Allow** on the TV;
the token is cached in `.tv-token.txt` (gitignored — keep it private).

## Launch an app by id

```powershell
python tools/remote.py --host <TV_IP> --port 8002 --app <APP_ID>
```

## Limits (Tizen, by design)

- No screenshots, no shell, no package lists over this channel.
- Blind key sequences are fragile: menu order differs by year/region/firmware.
- Same subnet only; cross-VLAN controllers are refused by the TV.
