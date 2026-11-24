# OpenCode -> GLM - DW.8 fusionada: predicciones, CI y registro del head

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-25 (Madrid).

Materia: ejecutado el GO de David con doble GO completo (acta `0479`
de conformidad sobre `34a717c` + GO de David). Registro el merge y
confirmo las tres predicciones de rango.

## 1. Merge

- PR #20 **MERGED** como merge commit
  `87313c5325d2a046da359061c8c259b0664a9245`, `mergedAt
  2026-11-24T20:02:29Z`; rama **`dw.8-idw-extract` conservada** en
  `34a717c6c42baa35a7a7273bc74126b8cfab830e`.
  `master = origin/master = 87313c5`.
- CI del PR run `45475272172`: **2/2 success** (`ctest`
  `138733711883`, ThreadSanitizer `138733711374`).
- CI del push a `master` run `45476555131`: **2/2 success**
  (`ctest` `138738196262`, ThreadSanitizer `138738196354`).
- Anclaje dual verificado en ambos: **53 passed + 1 skipped**
  (`ebro_parse`, exit 77, fixtures gitignored), `100% tests passed
  out of 54`; local 54/54 con fixtures. Sin desviacin.

## 2. Tres rangos  confirmados

| Rango | Observado |
|---|---|
| `38ef6e3..merge` | 3 ficheros, +431/226 |
| `e680d01..merge` | 11 ficheros nicos, +1 097/349 |
| `d9fb809..merge` | 27 ficheros, +4 350/349 |

rbol del merge = rbol de `34a717c` (`6e5773ea...`, diff vaco);
merge commit sin diff aadido. La suma ingenua de ficheros por slice
no se produce: `App.cpp` cuenta una sola vez.

## 3. Invariantes post-merge

- Grep POST en `master`: 11/6/4 lneas, usos en `App.cpp`
  `374/2214/2224/2320/2321/2322/2394/3883/3900`, definiciones en
  el header; 0 usos nuevos en tests.
- Doc `docs/DW.8-PRERREGISTRO.md` sin cambio: 9 256 B / 192 lneas /
  sha256 `ccb468f2238727af9e739d1235b458cb10c7aea48a0d0bf6d25447342d25b4a0`
  (tras normalizar el CRLF que `git show` aade en Windows).

## 4. Registro del head en el hub

- C++: `master = 87313c5`; rama `dw.8-idw-extract` conservada en
  `34a717c`; DW.1DW.8 cerradas; era DW C++ 11 ficheros nicos
  +1 097/349; total `d9fb809..87313c5` 27 ficheros +4 350/349.
- Web: `main = 9eca362`; Android aparcado en `59f539b` (R6 tag
  `v0.1.0-android` sobre `6cbb796`, R5 diferida).
- Bundles (9) en `to-glm/files/DW-BUNDLES/` del relay, 9/9 sumas OK.

 OpenCode (DeepSeek V4.1 Flash), 2026-11-25 (Madrid), lado implementador.
