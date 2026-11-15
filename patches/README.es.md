# parches/

[English](README.md) | **Español**

Diffs de nuestros cambios v1 de la Home contra el commit upstream pineado,
para que este repo no incluya código upstream copiado.

- `001-v1-tu7125-home.patch` — vs `GuillemCortesOvide/hack-tv@f52b545`:
  filtro de servicios/widgets + dedup por nombre, bandeja sports (`DAZN`,
  `Orange`) con matching tolerante, flag `showAll` (resto oculto), segunda
  fila sin scroll, cabecera compacta, icono cuadrado, tiles reales
  DAZN/Orange, lista de assets del instalador.
  Sin secretos dentro (auditado: sin IPs, DUIDs, MACs, tokens ni certs).

Aplicar en un clon fresco:

```powershell
git checkout f52b5450d9c3bec7e935d6a395ffdad8bf9cef
git apply <ruta-a>/001-v1-tu7125-home.patch
```
