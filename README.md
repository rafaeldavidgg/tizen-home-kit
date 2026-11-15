# tele-samsung — UE43TU7125KXXC (2020, Tizen 5.5)

Local-first toolkit for a Samsung 7 Series 43 (TU7125, Tizen 5.5).
No ADB, no root, no launcher takeover. Three depth levels.

## Levels

- **Level 0 — Remote hygiene (done):** Viewing Information Services OFF, Interest-Based Ads OFF, Reset PSID, Bixby Wake-Up OFF. Path on 2020: Settings > Support > Terms & Privacy > Privacy Choices.
- **Level 1 — WiFi control (this repo):** read-only probe + safe remote keys over 8001/8002 websocket with token.
- **Level 2 — Own dashboard (next):** hack-tv as base (same TU7125 family, requires Tizen 5.5), TizenBrew as installer, free-my-tv as alternative. Needs Developer Mode + sdb 26101 + Samsung cert with DUID.

## Quickstart Level 1

```powershell
python tools/tv_info.py --host 192.168.1.22
pip install -r requirements.txt
python tools/remote.py --host 192.168.1.22 --dry-run
python tools/remote.py --host 192.168.1.22 --port 8002 --key KEY_MENU
```

First real connect shows Allow on the TV. Token goes to `.tv-token.txt` (gitignored).

## Privacy

Never publish `--raw` output, DUID, WiFi MAC, AP MAC, tokens or `author.p12`.
`tv_info.py` redacts them by default.

## Credits / refs

- https://github.com/GuillemCortesOvide/hack-tv (video origin, final Tizen app)
- https://github.com/simbasjungles/free-my-tv
- https://github.com/reisxd/TizenBrew
- https://github.com/Gathin23/cleanyourtv (Android-only, not usable on Tizen — inspiration + not-android hygiene guide)
