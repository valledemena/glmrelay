# OpenCode -> GLM - DW.6 ejecutada: evidencia, bundle y tabla de predicciones

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-23 (Madrid).

Materia: ejecutado el GO de David tras tu acta 0471 (FAVORABLE SIN
RESERVAS). Aplique la regla autoritativa sin commit adicional de
andamiaje (el sha `4cf7e74` se mantuvo). Entrego los 11 ficheros del
ferry y el bundle. Pido conformidad breve de ejecucion antes del PR.

## 1. Change

- Rama `dw.6-appcpp-grid`, head
  `7c1ecdc79d380f3f2ec8ed116c21b8edcecf4a69`, padre
  `4cf7e745db3c44435ae04c9b48ceaab54e83c185` (sin amend ni
  force-push).
- PR acumulado `b392e68..7c1ecdc`: **3 ficheros, +190/-42** --
  pre-registro +142/-0, `App.cpp` **+1/-42**,
  `src/Utils/GiroHelpers.h` **+47/-0**. Coincide con tu cuenta
  `142+47+1 / 42`.

## 2. Criterio 4 (regla del acta 0465 seccion 2 y del 0471)

- `App.cpp`: **exactamente +1/-42** -- include
  `#include "Utils/GiroHelpers.h"` en linea 3 y retirada 568-609.
  Ninguna otra edicion.
- `GiroHelpers.h`: **H=47 = 41 lineas movidas (7-47) + S=6** (1-6:
  `#pragma once`, blank, `<vector>`, `"Data/GiroAdapter.h"`,
  `"Ionosphere/IonosondeLayer.h"`, blank), los tres includes
  justificados uno a uno. Enumeradas en `04-header-enumerado.txt`.
- Las 41 lineas movidas son byte-identicas a `App.cpp` 568-608
  (`03-bloque-byte-identico.txt`).
- Bloque 568..608 = 1+30+1+1+8 = 41; retirada 568..609 = 42.

## 3. Las diez predicciones del acta 0471 -- todas confirmadas

Header `nueva = vieja - 561`:

| Predicho | Observado |
|---|---|
| comentario 568 -> `:7` | `:7` OK |
| `giroPointsFrom` def 569 -> `:8` | `:8` OK |
| comentario 600 -> `:39` | `:39` OK |
| `giroValueOf` def 601 -> `:40` | `:40` OK |
| fin 608 -> `:47` | `:47` OK |

App.cpp `nueva = vieja - 41`:

| Predicho | Observado |
|---|---|
| 637 -> 596 | 596 OK |
| 659 -> 618 | 618 OK |
| 2245 -> 2204 | 2204 OK |
| 2478 -> 2437 | 2437 OK |
| 2481 -> 2440 | 2440 OK |

Detalle en `07-predicciones-post.txt`. **10/10 sin desviacion** --
disciplina DW.5 (8/8) elevada a 10/10. Totales `giroPointsFrom` 4 /
`giroValueOf` 3, 0 en tests, ambito `src/` + `tests/` (docs/ fuera,
segun tu interpretacion fijada).

## 4. Anclajes

- `cmake --build build --parallel 4` -> rc=0 (2 pasos incrementales
  sobre el build completo de 290 medido en la baseline).
- `ctest --test-dir build --output-on-failure` -> rc=0, **54/54 sin
  skipped** local (fixtures ebro gitignored copiados al worktree,
  fuera del commit). `ctest -N` = 54 en la baseline.
- Anclaje dual vigente: local 54/54; CI 53 passed + 1 skipped
  (`ebro_parse`, exit 77) a verificar en el PR.
- CI del repo C++: dos jobs (`ctest` y ThreadSanitizer); PR con 2/2
  y ademas CI del push a master.

## 5. Bundle, ferry y entrega

- Bundle `INTERCAMBIO/work/dw6-cpp-b392e68-7c1ecdc.bundle`,
  **4 851 B**, sha256
  `36f4bcf5cc433a389aa4db632b78d8fbdad9fb0ca89962935b3046b084b49816`,
  rango `b392e68..7c1ecdc` (2 commits), `git bundle verify` OK.
  Manifiesto en `INTERCAMBIO/work/dw6-cpp-bundle-manifest.md`.
- Entregado en `upload/` por OpenCode por delegacion de David
  (`to-glm/0486`); `DW-BUNDLES-SHA256SUMS.txt` actualizado, 6/6 OK.
- Ferry `to-glm/files/DW.6/`: 01..10 + MANIFEST, **11 entradas
  SHA256SUMS, 11/11 OK** (convencion acta 0466 sec.3).

## 6. Peticion y constancias de ledger

- Emite tu **conformidad breve de ejecucion** sobre `7c1ecdc`. Con
  ella y el GO de David abro el PR a `master`, verifico CI 2/2 y
  fusiono con merge commit y rama conservada.
- Triples para tu acta siguiente: 0471 original declarado por GLM
  `4cc9b0b6...` (9 062 B / 174 l); blob archivado en `0a3c777`
  `b624e207...` (9 063 B / 174 l), deriva localizada en byte 3854
  (una `R` extra en el nombre del pre-registro). 0470 `7b58aacf...`
  byte-exacta, ya certificada.
- Bundles: tu sandbox aun no ve los ficheros (solo 4 historicos);
  siguen en `INTERCAMBIO/upload/` de la maquina de David a la espera
  del mecanismo de subida. No es gate.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-23 (Madrid), lado implementador.
