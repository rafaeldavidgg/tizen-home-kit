# Privacidad — jamás publiques esto

[English](PRIVACY.md) | **Español**

Este repo está diseñado para ser publicable, pero el mundo de la TV está
lleno de secretos ligados a tu dispositivo. Ten esta lista a mano.

## Jamás subas ni pegues en público

- **DUID** / UDID de la TV (`uuid:…`), `id` de dispositivo, `udn`.
- **MAC WiFi**, MAC del punto de acceso, números de serie, `wifiMac`, `ssid`.
- **Tokens** de mando (`.tv-token.txt`), volcados `--raw` de la sonda.
- Certificados: `author.p12`, `distributor.p12`, contraseñas de firmado, perfiles.
- Email / contraseña de Samsung (entras en tu propio navegador y punto).
- `.wgt` firmados con tu certificado distributor (llevan tu DUID dentro).
- Capturas o fotos donde se vea algo de lo anterior.

## Convenciones de este repo

- Marcadores `<TV_IP>` / `<PC_IP>` en todas partes; nada de direcciones reales.
- `tv_info.py` censura DUID/MAC/AP por defecto; `--raw` es solo para tus ojos.
- `odd/` (bitácora con valores reales) está en gitignore y jamás se publica.
- Al reportar un bug upstream: solo modelo + versión de Tizen + mensaje sanitizado.

## Si filtraste algo

Rótalo: certificado distributor nuevo, token nuevo (borra `.tv-token.txt` y
vuelve a permitir), contraseñas nuevas. Borrar un commit no basta — rota el secreto.
