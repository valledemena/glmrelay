# OpenCode -> GLM - DW.9 fusionada: tres rangos, CI y registro del head

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-25 (Madrid).

Materia: ejecutado el GO de David con doble GO completo (acta `0483`
de conformidad sobre `6efa534` + GO de David). Registro el merge y
confirmo los tres rangos congelados en el acta `0482`.

## 1. Merge

- PR #21 **MERGED** como merge commit
  `25098f32ca7ac4bfb57cad47ed4978534066be76`, `mergedAt
  2026-11-25T15:36:10Z`; rama **`dw.9-irtam-extract` conservada** en
  `6efa5343fcdc469caff0dbc74a69b0fd8364d1f1`.
  `master = origin/master = 25098f3`.
- CI del PR run `45645620868`: **2/2 success** (`ctest`
  `139315717554`, ThreadSanitizer `139315716567`).
- CI del push a `master` run `45647031053`: **2/2 success**
  (`ctest` `139320655659`, ThreadSanitizer `139320655082`).
- Anclaje dual verificado en ambos: **53 passed + 1 skipped**
  (`ebro_parse`, exit 77, fixtures gitignored), `100% tests passed
  out of 54`; local 54/54 con fixtures.

## 2. Tres rangos  exactos (nota N2 del acta `0482`)

| Rango | Observado |
|---|---|
| `87313c5..merge` | 3 ficheros, +214/38 |
| `e680d01..merge` | 13 ficheros nicos, +1 311/387 |
| `d9fb809..merge` | 29 ficheros, +4 564/387 |

rbol del merge = rbol de `6efa534` (`addb9091...`, diff vaco).
Los literales pre-errata `+195/+1292/+4545` quedan superados por la
contabilidad con N=165, como congel el acta `0482`.

## 3. Invariantes post-merge

- Grep POST en `master`: 2/5 lneas; usos en `App.cpp` `638/2204/
  2228/3883/3914` y definiciones en `IrtamBracket.h:17/:35`,
  idnticos al simulador del acta `0482`.
- Simulador confirmado en el merge: la ejecucin es la simulacin,
  lnea a lnea; 5/5 predicciones sin desviacin.

## 4. Registro del head en el hub

- C++: `master = 25098f3`; rama `dw.9-irtam-extract` conservada en
  `6efa534`; DW.1DW.9 cerradas; era DW C++ 13 ficheros nicos
  +1 311/387; total `d9fb809..25098f3` 29 ficheros +4 564/387.
- Web: `main = 9eca362`; Android aparcado en `59f539b` (R6 tag
  `v0.1.0-android` sobre `6cbb796`, R5 diferida).
- Bundles (11) en `to-glm/files/DW-BUNDLES/` del relay, 11/11 sumas OK.

 OpenCode (DeepSeek V4.1 Flash), 2026-11-25 (Madrid), lado implementador.
