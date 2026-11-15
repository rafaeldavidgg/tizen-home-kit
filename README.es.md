# tizen-home-kit — v1 para Samsung UE43TU7125KXXC (2020, Tizen 5.5)

[English](README.md) | **Español**

Kit personal para limpiar el rastreo, controlar por WiFi y personalizar la home
de una Samsung 7 Series TU7125 por WiFi. Sin root, sin ADB y sin reemplazar el
launcher (Tizen no lo permite). Tres niveles de profundidad.

> Repo apto para publicar: todos los ejemplos usan marcadores como `<TV_IP>`.
> DUID, MACs, tokens, certificados y contraseñas jamás van en este repo.
> Ver `docs/PRIVACY.es.md`.

## Niveles

- **Nivel 0 — Higiene con el mando (10 min, solo mando):** apaga Viewing
  Information Services / ACR, anuncios personalizados, resetea el PSID y el
  wake-up de Bixby. Ver `docs/LEVEL0.es.md`.
- **Nivel 1 — Control por WiFi (herramientas de este repo):** sonda de solo
  lectura más teclas remotas por el websocket oficial (8001/8002) con token.
  Ver `docs/LEVEL1.es.md`.
- **Nivel 2 — Home propia v1 (reproducible):** dashboard basado en hack-tv
  (misma familia TU7125, Tizen 5.5) con dock + bandeja de deportes, resto
  oculto, cabecera compacta, icono cuadrado y tiles reales de DAZN / Orange.
  Reprodúcela exacta con `docs/REPRODUCE-HOME.es.md` +
  `patches/001-v1-tu7125-home.patch` (base pineada, sin copiar código ajeno).

## Inicio rápido (Nivel 1)

```powershell
python tools/tv_info.py --host <TV_IP>
pip install -r requirements.txt
python tools/remote.py --host <TV_IP> --dry-run
python tools/remote.py --host <TV_IP> --port 8002 --key KEY_MENU
```

La primera conexión real muestra **Allow** en la TV. El token queda en
`.tv-token.txt` (ignorado por git, privado — jamás lo subas).

## Estructura del repo

```text
tools/          Nivel 1: tv_info.py (sonda de solo lectura), remote.py (mando seguro)
docs/           LEVEL0, LEVEL1, REPRODUCE-HOME, PRIVACY, ATTRIBUTION (+ versiones .es)
patches/        patch v1 de la Home contra upstream pineado (aplicar en clon fresco)
config/         tus valores v1 de la Home (dock, sports, showAll) como ejemplo
assets/         icono v1 original de la Home (nuestro, cuadrado, sin transparencias)
```

## Versiones

- **v1** — esta release: Home TU7125 2020 / Tizen 5.5 descrita arriba.
- Futuras Homes (v2, …) siguen el mismo patrón: patch + config + docs nuevos.

## Créditos / refs

- Base de la Home: https://github.com/GuillemCortesOvide/hack-tv (MIT, ver `docs/ATTRIBUTION.es.md`)
- Alternativas: https://github.com/simbasjungles/free-my-tv · https://github.com/reisxd/TizenBrew
- Inspiración solo-Android (NO funciona en Tizen): https://github.com/Gathin23/cleanyourtv
