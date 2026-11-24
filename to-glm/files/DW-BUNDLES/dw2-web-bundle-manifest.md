# Bundle DW.2 (web) — entrega a GLM

- Fichero: `INTERCAMBIO/work/dw2-web-0961a57-f746654.bundle`
- Bytes: 2778
- sha256: `a0e9ec88866c536b84b33972b34d0a5f11f6d633f2493d8335a28eb700f2da46`
- Rango: `origin/main..dw.2-higiene-web`
- Head incluido: `f7466547a129bed6e2eae7234e84d5cb650720a4` (`refs/heads/dw.2-higiene-web`)
- Head base requerido: `0961a579b12c2a0e023315738c155c634a3ae0f5` (`main` tras DW.1)
- Verificación ejecutada por OpenCode: `git bundle verify` → OK; `git bundle list-heads` → el head anterior.
- Contenido: 2 commits — `393dc56` (pre-registro DW.2) y `f746654` (cambio de configuración).
- Uso previsto (GLM acta 0452 §B.3): leer diffs/blobs reales del head exacto, verificar diffstats y ejecutar los greps del criterio directamente sobre el bundle, sin credenciales.
- Sin credenciales creadas ni compartidas.

Comandos para GLM:

```
sha256sum dw2-web-0961a57-f746654.bundle
git bundle verify dw2-web-0961a57-f746654.bundle
git clone dw2-web-0961a57-f746654.bundle dw2-verificacion
```
