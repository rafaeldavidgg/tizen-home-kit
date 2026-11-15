# Nivel 1 — Control por WiFi (websocket 8001/8002)

[English](LEVEL1.md) | **Español**

Canal oficial de mando local. Primero solo lectura, teclas solo cuando tú digas.
El PC y la TV deben estar en la misma subred.

## Sonda (solo lectura, siempre segura)

```powershell
python tools/tv_info.py --host <TV_IP>
```

Imprime un resumen **sanitizado** (modelo, Tizen, encendido, TokenAuth,
developerMode…). DUID / MAC / identificadores del punto de acceso van
censurados. Jamás publiques la salida de `--raw`.

## Simulación (sin conectar)

```powershell
python tools/remote.py --host <TV_IP> --dry-run
```

## Enviar una tecla (pide Allow en la TV una vez)

```powershell
pip install -r requirements.txt
python tools/remote.py --host <TV_IP> --port 8002 --key KEY_MENU
```

Teclas útiles: `KEY_HOME`, `KEY_MENU`, `KEY_UP/DOWN/LEFT/RIGHT`, `KEY_ENTER`,
`KEY_RETURN`, `KEY_HDMI1`… La primera conexión muestra **Allow** en la TV;
el token se guarda en `.tv-token.txt` (ignorado por git — mantenlo privado).

## Lanzar una app por id

```powershell
python tools/remote.py --host <TV_IP> --port 8002 --app <APP_ID>
```

## Límites (Tizen, por diseño)

- Sin capturas de pantalla, sin shell, sin listas de paquetes por este canal.
- Las secuencias de teclas a ciegas son frágiles: el orden de menús cambia por
  año, región y firmware.
- Solo misma subred; la TV rechaza controladores de otra VLAN.
