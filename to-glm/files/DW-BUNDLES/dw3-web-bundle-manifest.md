# Bundle DW.3 (web) — entrega a GLM

- Fichero: `INTERCAMBIO/work/dw3-web-118c7e9-5854e04.bundle`
- Bytes: 3791
- sha256: `53b71fcbb9fb35e5301ace24b8f056f8e569a62adf0144c605111c72cf940e01`
- Rango: `118c7e9..5854e04` (`origin/main..dw.3-solarwind-extract`)
- Head incluido: `5854e04bbfb71908baf79a05e588acd2f210e50d`
- Contenido: 2 commits — `8269705` (pre-registro DW.3) y `5854e04` (extracción de `solarWindColor`).
- Verificado por OpenCode: `git bundle verify` → "bundle is okay"; `git bundle list-heads` → el head anterior.
- Uso previsto: leer el diff real del movimiento, verificar el bloque byte-idéntico salvo `export` y ejecutar los greps de conteo propios.
- Sin credenciales.

Comandos:

```
sha256sum dw3-web-118c7e9-5854e04.bundle
git bundle verify dw3-web-118c7e9-5854e04.bundle
git clone dw3-web-118c7e9-5854e04.bundle dw3-verificacion
```
