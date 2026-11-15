# tizen-home-kit — v1 for Samsung UE43TU7125KXXC (2020, Tizen 5.5)

Personal toolkit to de-track, remote-control and re-skin a Samsung 7 Series TU7125 over Wi-Fi.
No root, no ADB, no launcher takeover (Tizen does not allow it). Three depth levels.

> Public-repo safe: every example uses placeholders like `<TV_IP>`. Real DUID, MACs,
> tokens, certificates and passwords never belong in this repo. See `docs/PRIVACY.md`.

## Levels

- **Level 0 — Remote hygiene (10 min, remote only):** turn off Viewing Information
  Services / ACR, interest-based ads, reset PSID, Bixby wake-up. See `docs/LEVEL0.md`.
- **Level 1 — WiFi control (this repo's tools):** read-only TV probe plus safe remote
  keys over the official websocket (8001/8002) with token. See `docs/LEVEL1.md`.
- **Level 2 — Own Home v1 (reproducible):** hack-tv based dashboard (same TU7125 family,
  Tizen 5.5) with dock + sports trays, rest hidden, tightened header, square icon,
  real DAZN / Orange tiles. Reproduce it exactly with `docs/REPRODUCE-HOME.md` +
  `patches/001-v1-tu7125-home.patch` (base pinned, no upstream code copied here).

## Quickstart (Level 1)

```powershell
python tools/tv_info.py --host <TV_IP>
pip install -r requirements.txt
python tools/remote.py --host <TV_IP> --dry-run
python tools/remote.py --host <TV_IP> --port 8002 --key KEY_MENU
```

First real connect shows **Allow** on the TV. The token lands in `.tv-token.txt`
(gitignored, private — never commit it).

## Repo layout

```text
tools/          Level 1: tv_info.py (read-only probe), remote.py (safe remote)
docs/           LEVEL0, LEVEL1, REPRODUCE-HOME, PRIVACY, ATTRIBUTION
patches/        v1 Home patch vs pinned upstream (apply on a fresh clone)
config/         your v1 Home values (dock, sports, showAll) as an example file
assets/         original v1 Home icon (ours, square, no transparency issues)
```

## Versions

- **v1** — this release: TU7125 2020 / Tizen 5.5 Home described above.
- Future Homes (v2, …) follow the same pattern: new patch + new config + new docs.

## Credits / refs

- Home base: https://github.com/GuillemCortesOvide/hack-tv (MIT, see `docs/ATTRIBUTION.md`)
- Alternatives: https://github.com/simbasjungles/free-my-tv · https://github.com/reisxd/TizenBrew
- Android-only inspiration (does NOT work on Tizen): https://github.com/Gathin23/cleanyourtv
