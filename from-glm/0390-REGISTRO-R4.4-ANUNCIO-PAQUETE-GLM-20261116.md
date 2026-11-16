# REGISTRO — ANUNCIO DE PAQUETE RELAY R4.4 (ENTREGA PENDIENTE) — GLM 2026-11-16

GLM · 2026-11-16 (CET) · canal: relay David
Objeto: anuncio de Deepseek del paquete de relay R4.4 (`upload/R4.4-RELAY-20261116.zip`).
**El anuncio llegó; el paquete NO.** Este registro deja constancia de lo declarado,
lo verificado y lo que falta para el dictamen final.

---

## 1. Metadatos declarados en el anuncio (constancia literal)

| Artefacto | Ruta declarada | sha256 declarado | Tamaño |
|---|---|---|---|
| Paquete (zip) | `upload/R4.4-RELAY-20261116.zip` | `3465b25d1292e497bf2788ea5df8bad7fe5c43d806d334b2fabaa9280cfcb455` | 19 686 B |
| Hash del paquete | `upload/R4.4-RELAY-20261116.zip.sha256` | — | 90 B |
| Nota de transporte | `upload/README-TRANSPORTE-R4.4-20261116.txt` | `7177ad9db5f405c7fefb6207e7ef178fb62acbf91ba9999e564bc496a7c6304c` | 1 356 B |

Contenido declarado del zip (5 entradas):

1. `PROPUESTA-R4.4-MODELO-NEH-VOLUMEN-PURO-20261116.md` —
   `fe98b00dcec0ca30228898e99edb9d60893e0eafef69ab94d08ec19b6466dc81` — 293 líneas.
2. `PARA-GLM-REVISION-PROPUESTA-R4.4-20261116.md` —
   `7286f0930db2e674194e5dabb15c870b4f7d30260d3cb7bcdfa8effbb7289653` — 338 líneas.
3. `RESPUESTA-A-GLM-PRE-DICTAMEN-R4.4-20261116.md` —
   `2af5df2f6eefdbefed3896840b95c6d841078e8c3b30a78c1ce63c7d56266fd9` — 150 líneas.
4. `README-RELAY-R4.4.txt` — 53 líneas, ASCII/CRLF.
5. `SHA256SUMS` — 4 entradas, LF nativo.

Declaraciones del emisor: `sha256sum -c SHA256SUMS` interno 4/4 OK tras
extracción limpia; `.sha256` del zip coincide; tres documentos ASCII sin BOM,
CRLF completo, 293/338/150 líneas; zip con exactamente 5 entradas, sin
ficheros ocultos ni material de Android; el PRE-DICTAMEN de GLM queda fuera
del paquete («es su artefacto y ya lo tiene»); sin build, sin tests, sin
dispositivo; nada enviado, commiteado ni pusheado. Queda decisión abierta
para David: `integrateTEC` fuera de R4.8 (la respuesta recomienda descarte
documentado en R4, salvo enmienda de plan o slice posterior).

## 2. Estado de la entrega en el lado GLM

- `upload/` GLM (08:4x UTC): **solo** los dos ficheros preexistentes
  (`ionosphere-live-3d[1]`, HTML de GitHub del repo desktop, 13-11; y
  `Pasted Content_1793610592201.txt`, 02-11). **El zip NO está.**
- Búsqueda extendida (download/, scripts/, /tmp, ficheros de hoy): ningún
  `R4.4-RELAY-20261116.zip`. El anuncio viajó; el adjunto no.
- Consecuencia: **ningún hash, recuento ni contenido del paquete es
  verificable todavía**. El dictamen D1/D2/D3 + GLOBAL sigue RESERVADO
  (§5 del pre-dictamen).

## 3. Verificación independiente de las afirmaciones de repositorio (FIEL)

GLM 2026-11-16 08:44–08:45 UTC: `git fetch` + `rev-parse`/`ls-tree`, y
endpoint individual de PR vía api.github.com.

| # | Afirmación | Verificación GLM | Veredicto |
|---|---|---|---|
| 1 | Android sigue en `main` `84d4e9e` | `origin/main` = `84d4e9edf36fecd258268cc82b91ebc1819b39b9` (sin cambios desde el pre-dictamen) | **FIEL** |
| 2 | no hay rama R4.4 | 0 ramas remotas con `r4.4` | **FIEL** |
| 3 | sin PR nuevo | `pulls/48` → 404 | **FIEL** |
| 4 | untracked `work/` y `work-perf-*` preexistentes | no observable desde GLM (espacio de Deepseek); sin incidencia sobre git | n/a (fuera de alcance) |

## 4. Consistencia interna del anuncio (sin paquete, solo aritmética)

| Comprobación | Resultado |
|---|---|
| Hashes de PROPUESTA y PARA-GLM vs anuncio anterior (08:2x UTC) | **idénticos** (`fe98b00d…` 293; `7286f093…` 338) — sin reescritura entre anuncios, conforme a lo declarado («los tres documentos quedan sin reescribir») |
| Tercer documento `RESPUESTA-A-GLM-PRE-DICTAMEN…` (150 líneas) | **nuevo** — cronológicamente coherente: responde al pre-dictamen GLM depositado 08:24 UTC; implica que el pre-dictamen llegó al lado Deepseek por el relay de David |
| `.sha256` de 90 B | 64 (hex) + 2 (espacios) + 23 (`R4.4-RELAY-20261116.zip`) + 1 (LF) = **90 B exactos** ✓ |
| Zip de 19 686 B para 781+53 líneas de texto + manifiesto | plausible con compresión de texto; sin imposibilidad aritmética ✓ |
| Exclusión del pre-dictamen del paquete | correcta: es artefacto GLM, ya custodiado aquí (sha256 `47e6024b…`) ✓ |

## 5. Pendiente

1. **Relay físico del zip** (y, si se quiere, `.sha256` y
   `README-TRANSPORTE`) a `upload/` GLM — es lo único que falta.
2. A la entrega: verificar zip sha256 `3465b25d…`, listado de 5 entradas,
   extracción limpia, `SHA256SUMS` 4/4, convenciones (ASCII sin BOM, CRLF,
   LF nativo del manifiesto, 293/338/150 líneas).
3. Leer los tres documentos; cotejar los hashes del oráculo declarados
   contra las anclas blob del pre-dictamen §2 (`layerProfile.ts 4184bdb1…`,
   `densityVolume.ts 63c16fd5…`, etc.).
4. Emitir el **DICTAMEN FINAL D1/D2/D3 + GLOBAL** (formato de la nota de
   revisión), con la posición provisional del pre-dictamen §4 como punto de
   partida (D1 aceptable con 2 condiciones; D2 aceptable con corrección
   `integrateTEC`/R4.8; D3 aceptable).
5. Recordatorio de protocolo: dictamen GLM → **GO de David** → rama →
   implementación → PR. La decisión abierta de `integrateTEC` es de David.

## 6. Higiene del turno

Turno read-only: `git fetch` (android), `rev-parse`/`ls-tree`/`branch -r`,
WebFetch a api.github.com (`pulls/48`), aritmética local (Python),
inventario de `upload/`. Sin push, sin mutación de repositorios o ficheros
ajenos, sin congelación. Único artefacto nuevo: este registro.

— GLM (canal relay David), 2026-11-16 08:45 UTC
