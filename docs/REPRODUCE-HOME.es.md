# Reproducir la Home v1 (TU7125 / Tizen 5.5)

[English](REPRODUCE-HOME.md) | **Español**

Recrea la Home v1 exacta: dock de 5 + bandeja de deportes de 2, resto oculto,
cabecera compacta, scroll fijo en la segunda fila, icono cuadrado y tiles
reales de DAZN / Orange. El código upstream **no** se copia aquí — lo clonas
pineado y aplicas nuestro patch.

## 0. Vista previa del resultado

- Fila 1 (dock): Netflix, Disney+, Prime Video, HBO Max, YouTube
- Fila 2 (deportes): DAZN, Orange
- Después: solo fuentes TV/HDMI (resto oculto con `showAll: false`)
- Cabecera compacta; la fila de deportes no desliza; el scroll empieza en fuentes.

## 1. Requisitos

- TV encendida, misma LAN (`<TV_IP>`), mando a mano.
- PC en la misma WiFi (`<PC_IP>`).
- Tizen Studio (vale el Web CLI) + **TV Extensions** + **Samsung Certificate
  Extension** instalados desde su Package Manager.
- `tizen` y `sdb` en el PATH, p. ej. `C:\tizen-studio\tools` y
  `C:\tizen-studio\tools\ide\bin`.
- Cuenta gratuita de desarrollador Samsung (entras en tu propio navegador;
  jamás pegues su contraseña en ningún lado).

## 2. Modo Developer + conexión

1. En la TV: `Apps` → escribe `12345` → Developer Mode **ON** → Host PC IP
   `<PC_IP>` → reinicia (arriba de Apps sale `Develop Mode`).
2. `sdb connect <TV_IP>` → `sdb devices` lista tu TV.
3. Device Manager → click derecho en la TV → **Permit to install applications**.

## 3. Certificados (una vez)

Certificate Manager → perfil nuevo **Samsung → TV** (`<YOUR_PROFILE>`):
certificado de autor (nuevo) + certificado distributor (**Public**, con el
DUID de tu TV). Guarda `author.p12` y su contraseña **fuera de cualquier
repo**, con copia de seguridad.

## 4. Clona upstream pineado + aplica nuestro patch

```powershell
git clone https://github.com/GuillemCortesOvide/hack-tv.git hack-tv-v1
cd hack-tv-v1
git checkout f52b5450d9c3bec7e935d6a395ffdad8bf9cef
git apply ..\tizen-home-kit\patches\001-v1-tu7125-home.patch
```

(Ajusta la ruta del patch a donde hayas clonado este repo.)

## 5. Configura (lo tuyo)

Copia los valores de `config/home-v1.example.js` al `launcher/config.js` del
clon (ciudad opcional para el clima; dock / sports / showAll tal cual vienen).

## 6. Compila, firma, instala

```powershell
python instalar.py
<path-to>\tizen.bat package -t wgt -s <YOUR_PROFILE> -- build\package
<path-to>\tizen.bat install -n Home.wgt -s <TV_IP>:26101 -- build\package
```

Notas:

- El `instalar.py` original llama a `tizen` a secas, que en Windows falla
  (`WinError 2`) porque es `tizen.bat`. Llamar a `tizen.bat` directamente
  para package/install (como arriba) es el workaround soportado.
- Abre **Home** desde Apps. `Return` sale; el botón **Home** del mando
  siempre va a Smart Hub (limitación de Samsung, no un bug).
- Tizen cachea el icono por id: tras cambios de icono, desinstala
  (`tizen uninstall -p HkTvHome01.Home -s <TV_IP>:26101`) o sube la versión
  en `launcher/config.xml` antes de reinstalar.

## 7. Revertir

```powershell
<path-to>\tizen.bat uninstall -p HkTvHome01.Home -s <TV_IP>:26101
```

(También vale Quitar desde el menú Apps de la TV.) Apaga el Developer Mode
**OFF** y reinicia cuando termines de iterar.
