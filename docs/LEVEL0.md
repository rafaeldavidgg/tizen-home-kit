# Level 0 — Remote hygiene (Samsung 2020, e.g. TU7125)

**English** | [Español](LEVEL0.es.md)

About 10 minutes, remote control only. Nothing installed, everything reversible.
Do this first on any Samsung before any WiFi or app work.

## 1. Turn off Viewing Information Services (ACR)

`Settings → Support → Terms & Privacy → Privacy Choices → Viewing Information Services OFF`

(Some firmwares say `Terms & Policy`. Alternative entry: `Home → Privacy Choices`.)

## 2. Untick the rest on the same screen

- Interest-Based Advertisements OFF
- Customization Service OFF
- Improve personalized ads OFF
- Get news and special offers OFF
- Do not track ON

Menu names vary slightly by firmware; untick everything optional you find there.

## 3. Reset the ad ID

`Settings → All Settings → General & Privacy → Terms & Privacy → Reset PSID`

## 4. Bixby wake word off

`Settings → General → Voice → Bixby Voice Settings → Voice Wake-Up OFF`

(Bixby itself cannot be removed, only its wake word.)

## 5. Note your TV IP (needed for Level 1)

`Settings → General → Network → Network Status → IP Settings`

Write it down privately as `<TV_IP>`. Your computer must be on the **same** WiFi
(not an isolated guest network) for Level 1/2.

## After firmware updates

Re-check steps 1–2: Samsung has been observed re-enabling ad settings after updates.

## Going further (optional, router-level)

DNS blocking at the router (e.g. NextDNS / Pi-hole / AdGuard Home with a
HaGeZi `native.samsung` list) blocks tracking domains for the whole LAN.
Do not rely on a manual DNS set on the TV itself — it has been observed not to stick.
