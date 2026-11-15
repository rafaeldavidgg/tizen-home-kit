# Reproduce Home v1 (TU7125 / Tizen 5.5)

Recreates the exact v1 Home: dock of 5 + sports tray of 2, rest hidden, tightened
header, fixed second-row scroll, square icon, real DAZN / Orange tiles.
Upstream code is **not** copied here — you clone it pinned and apply our patch.

## 0. Result preview

- Row 1 (dock): Netflix, Disney+, Prime Video, HBO Max, YouTube
- Row 2 (sports): DAZN, Orange
- Then: TV / HDMI sources only (rest hidden via `showAll: false`)
- Header compact; sports row does not scroll away; scroll starts at sources.

## 1. Prerequisites

- TV on, same LAN (`<TV_IP>`), remote at hand.
- PC on the same WiFi (`<PC_IP>`).
- Tizen Studio (Web CLI is enough) + **TV Extensions** + **Samsung Certificate
  Extension** installed via its Package Manager.
- `tizen` and `sdb` on PATH, e.g. `C:\tizen-studio\tools` and
  `C:\tizen-studio\tools\ide\bin`.
- Free Samsung developer account (you sign in in your own browser; never paste
  its password anywhere).

## 2. Developer Mode + connection

1. On the TV: `Apps` → type `12345` → Developer Mode **ON** → Host PC IP `<PC_IP>`
   → restart (top of Apps shows `Develop Mode`).
2. `sdb connect <TV_IP>` → `sdb devices` lists your TV.
3. Device Manager → right-click the TV → **Permit to install applications**.

## 3. Certificates (once)

Certificate Manager → new **Samsung → TV** profile (`<YOUR_PROFILE>`):
author certificate (new) + distributor certificate (**Public**, with your TV's
DUID). Keep `author.p12` and its password **outside any repo**, backed up.

## 4. Clone upstream pinned + apply our patch

```powershell
git clone https://github.com/GuillemCortesOvide/hack-tv.git hack-tv-v1
cd hack-tv-v1
git checkout f52b5450d9c3bec7e935d6a395ffdad8bf9cef
git apply ..\tizen-home-kit\patches\001-v1-tu7125-home.patch
```

(Adjust the patch path to wherever you checked out this repo.)

## 5. Configure (yours)

Copy `config/home-v1.example.js` values into the clone's `launcher/config.js`
(city optional for weather; dock / sports / showAll as shipped).

## 6. Build, sign, install

```powershell
python instalar.py
<path-to>\tizen.bat package -t wgt -s <YOUR_PROFILE> -- build\package
<path-to>\tizen.bat install -n Home.wgt -s <TV_IP>:26101 -- build\package
```

Notes:

- The upstream `instalar.py` calls bare `tizen`, which fails on Windows
  (`WinError 2`) because it is `tizen.bat`. Calling `tizen.bat` directly for
  package/install (as above) is the supported workaround.
- Open **Home** from Apps. `Return` exits it; the remote's **Home** button
  always goes to Smart Hub (Samsung limitation, not a bug).
- Tizen caches the app icon per id: after icon changes, uninstall
  (`tizen uninstall -p HkTvHome01.Home -s <TV_IP>:26101`) or bump
  `launcher/config.xml` version before reinstalling.

## 7. Revert

```powershell
<path-to>\tizen.bat uninstall -p HkTvHome01.Home -s <TV_IP>:26101
```

(Remove via the TV's Apps menu works too.) Turn Developer Mode **OFF** and
restart when done iterating.
