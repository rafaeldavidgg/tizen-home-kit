# Nivel 0 — Higiene con el mando (Samsung 2020, p. ej. TU7125)

[English](LEVEL0.md) | **Español**

Unos 10 minutos, solo con el mando. Nada se instala, todo es reversible.
Hazlo primero en cualquier Samsung antes de tocar WiFi o apps.

## 1. Apaga Viewing Information Services (ACR)

`Ajustes → Soporte → Términos y privacidad → Privacy Choices → Viewing Information Services OFF`

(Algunos firmwares dicen `Términos y política`. Entrada alternativa: `Home → Privacy Choices`.)

## 2. Desmarca el resto de esa pantalla

- Interest-Based Advertisements OFF
- Customization Service OFF
- Improve personalized ads OFF
- Get news and special offers OFF
- Do not track ON

Los nombres varían un poco por firmware; desmarca todo lo opcional que veas.

## 3. Resetea el ID de publicidad

`Ajustes → Todos los ajustes → General y privacidad → Términos y privacidad → Reset PSID`

## 4. Apaga el wake-up de Bixby

`Ajustes → General → Voz → Bixby Voice Settings → Voice Wake-Up OFF`

(Bixby no se puede borrar, solo su escucha por voz.)

## 5. Anota la IP de tu TV (la necesitarás en el Nivel 1)

`Ajustes → General → Red → Estado de red → Ajustes IP`

Anótala en privado como `<TV_IP>`. El PC debe estar en la **misma** WiFi
(no en una red de invitados aislada) para los Niveles 1 y 2.

## Tras actualizaciones de firmware

Revisa los pasos 1–2: se ha visto que Samsung reactiva ajustes de anuncios
después de actualizar.

## Para ir más lejos (opcional, a nivel de router)

Bloqueo DNS en el router (p. ej. NextDNS / Pi-hole / AdGuard Home con lista
HaGeZi `native.samsung`) bloquea dominios de rastreo en toda la LAN.
No confíes en un DNS manual puesto en la TV: se ha visto que no se mantiene.
