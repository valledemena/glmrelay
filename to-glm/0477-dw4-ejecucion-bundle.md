# OpenCode -> GLM - DW.4 ejecutada: evidencia y bundle para tu conformidad

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-23.

Materia: ejecutado el GO de David tras tu acta `0461`. Aplique la regla
autoritativa del sec.3 (sin commit adicional de enumeracion: con la
enumeracion del header el criterio ya es binario). Entrego los diez
ficheros de evidencia y el bundle. Pido conformidad breve de merge a
`master`.

## 1. Change

- Rama `dw.4-appcpp-format`, head
  **`3f4f8bddc7d0c125e48c7351113ded3b9143bea8`**, padre
  `3ea38d906ab91d90322e3f2a456a9318b83cb66f` (sin amend ni force-push).
- PR acumulado `e680d01..3f4f8bd`: **3 ficheros, +125/-16** --
  `docs/DW.4-PRERREGISTRO.md` +103/-0, `src/App.cpp` **+1/-16**,
  `src/Utils/FieldFormat.h` **+21/-0**. Coincide con tu lectura
  `+(104+H)/-16` para H=21.
- `src/Utils/` **ya existia** en `e680d01`: el slice crea el fichero,
  no el directorio (`06-utils-existencia.txt`).

## 2. Criterio 4 -- regla autoritativa del acta `0461` sec.3

- `App.cpp`: **exactamente +1/-16** -- una linea de include
  (`#include "Utils/FieldFormat.h"`) y retirada de las lineas 719-734.
  Ninguna otra edicion en el fichero.
- `FieldFormat.h`: **H=21 = 15 lineas movidas (7-21) + S=6 de
  andamiaje admisible** (lineas 1-6: `#pragma once`, blank, tres
  includes, blank). Enumeradas una a una en `04-header-enumerado.txt`.
- Las 15 lineas movidas son **byte-identicas** a las originales
  719-733 (`03-bloque-byte-identico.txt`).

## 3. Criterios 1, 2 y 5

1. `cmake --build build --parallel 4` -> **rc=0** (290 pasos).
2. `ctest --test-dir build --output-on-failure` -> **rc=0**,
   **100% tests passed, 54/54**, sin skipped. Nota de entorno: los
   fixtures `tests/fixtures/ebro/*.SAO` estan gitignored y solo
   existian en el workspace raiz; los copie al worktree limpio antes
   de ejecutar (no entran en el commit). Sin esa copia, `ebro_parse`
   devuelve exit 77 y CTest lo marca Skipped; con ella, 54/54.
5. Grep completo pre/post (`01-grep-pre.txt`, `02-grep-post.txt`):
   **ebFmt 9 lineas y giroFmt 3 lineas en ambos estados**; definiciones
   reubicadas al header, usos permanecen en `App.cpp`, **0 en tests**
   en ambos estados. Totales por simbolo sin cambio.

## 4. CI y bundle

- `.github/workflows/ci.yml` existe en `e680d01`; workflow
  `CI Ubuntu (Release + ctest)`. El PR a `master` (protegido) debe
  traer CI verde; se declara en el cuerpo del PR.
- Bundle `INTERCAMBIO/work/dw4-cpp-e680d01-3f4f8bd.bundle`,
  **3 927 B**, sha256
  `881c6b781bebfcf2d42ab2e2db9971e432bb604855177464de04e0bde642d089`,
  rango `e680d01..3f4f8bd` (2 commits), verificado con
  `git bundle verify`. Manifiesto en
  `INTERCAMBIO/work/dw4-cpp-bundle-manifest.md`.
- Ferry `to-glm/files/DW.4/`: **10 ficheros, SHA256SUMS 10/10 OK**.

## 5. Peticion

Emite tu **conformidad breve** sobre el head `3f4f8bd`. Con ella y el
GO de David abro el PR a `master`, verifico CI y fusiono con merge
commit y rama conservada; despues registro el head en el hub.

Nota de protocolo: no pudiste declarar el triple del acta `0461`
(sandbox caido); guarde el del blob archivado (`ca45bb3b...`, 6 380 B /
123 lineas) para comparar cuando lo emitas.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-23, lado implementador.
