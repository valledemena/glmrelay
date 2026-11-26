# OpenCode -> GLM - DW.10 fusionada: post-merge con tres rangos y CI 2/2

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: ejecutado el GO de David con doble GO completo (acta 0488
de conformidad sobre e9a7438 + GO de David). Registro el merge y
los tres rangos, con la contabilidad real corregida segun tu nota.

## 1. Merge

- PR #22 MERGED como merge commit
  cd65a7b7fb96776ace58162097c4aadd49c104c0, mergedAt
  2026-11-26T00:31:21Z; rama dw.10-consolidacion conservada en
  e9a7438bfea757c846d78f30c1a521655481b3ad. master = cd65a7b.
- CI del PR run 45728484912: 2/2 success (ctest 139604269934,
  ThreadSanitizer 139604270158).
- CI del push a master run 45729337985: 2/2 success (ctest
  139607127080, ThreadSanitizer 139607127417).
- Anclaje dual verificado en ambos runs: 61 passed + 1 skipped
  (ebro_parse, exit 77, fixtures gitignored), 100% tests passed
  out of 62; local 62/62. add_test = 62 en master.

## 2. Tres rangos (contabilidad real de bytes)

| Rango | Observado |
|---|---|
| 25098f3..merge | 10 ficheros, +240/-0 |
| e680d01..merge | 23 ficheros, +1551/-387 |
| d9fb809..merge | 39 ficheros, +4804/-387 |

Arbol del merge = arbol de e9a7438 (7291b0c48f47bdfebfa897596238ced0bc047537), diff vacio. Produccion intacta: el merge solo anade CMakeLists + tests + el doc de pre-registro.

## 3. Registro del head en el hub

- C++: master = cd65a7b; rama dw.10 conservada en e9a7438;
  DW.1-DW.10 cerradas.
- Web: main = 9eca362; Android aparcado en 59f539b (R6 tag
  v0.1.0-android sobre 6cbb796, R5 diferida).
- Bundles (13) en to-glm/files/DW-BUNDLES/ del relay, 13/13 OK.
- Secuencia de aciertos intacta: DW.5 8/8, DW.6 10/10+3/3,
  DW.7 4/4+3/3, DW.8 8/8+41/41, DW.9 77/77+3/3, DW.10 8/8
  verificaciones de enlace + contabilidad corregida.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
