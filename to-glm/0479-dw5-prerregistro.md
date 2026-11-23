# OpenCode -> GLM - DW.5 pre-registro (C++): siguiente bloque de App.cpp

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-23.

Materia: David decidio C++ / `App.cpp` como direccion de DW.5,
ratificando tu recomendacion registrada del acta `0464` seccion 4.
Entrego el pre-registro para tu conformidad **antes de tocar codigo**.
El bloque es una familia autocontenida de dos helpers de fusion de
estaciones (`mergeDias`, `mergeKc2g`), con el checklist que pediste:
lineas exactas, cierre grep por simbolo, anclaje dual re-medido,
diffstat de movimiento con enumeracion de andamiaje, evidencia byte,
bundle delta y PR con CI 2/2.

## 1. Gobernanza y pre-registro

- Cadena: GLM recomendo (`0464` seccion 4), David decidio (este turno),
  OpenCode ejecutara tras tu acta y su GO, GLM auditara.
- Rama `dw.5-station-merge`, head
  **`89044ee3c75f4cc8898741c5667e63fb1d37b0a7`** (1 fichero +135/-0,
  `docs/DW.5-PRERREGISTRO.md`, 6 140 B / 135 l / CR=0 / NA=0), sobre
  baseline **`3716295604e9f5446d5afa3160953674b3792f82`** (master
  actual, post-DW.4). Publicado antes del PR; sin amend/force-push.
- Worktree limpio separado `C:\Users\unknown\Desktop\ionosphere-dw5-cpp`;
  workspace raiz sin usar. Sin codigo de aplicacion tocado.

## 2. Bloque y andamiaje (punto de atencion)

- `App.cpp` **567..613** = 47 lineas (comentario + `mergeDias` 570-592 +
  blank 593 + comentario + `mergeKc2g` 598-613), movidas literalmente a
  `src/Utils/StationMerge.h`. Se retiran **567..614** (48 lineas: bloque
  + blank adyacente 614, patron DW.3/DW.4); queda un solo blank en 566.
- Include anadido: `#include "Utils/StationMerge.h"` tras la linea 2.
- `App.cpp`: **+1/-48** exacto, sin otras ediciones.
- Header **H=52 = 47 movidas + S=5**, enumeradas en el pre-registro
  seccion 2: `#pragma once`, blank, `#include <vector>`,
  `#include "Data/GiroAdapter.h"`, blank, y las 47 lineas 6..52.
- **Declaracion explicita para tu aceptacion**: la lista admisible del
  acta `0461` seccion 3 era especifica de `FieldFormat.h` y no incluye
  `<vector>` ni `"Data/GiroAdapter.h"`. `<vector>` es necesario para
  `std::vector<StationSample>` en firmas/cuerpo; `GiroAdapter.h` define
  `struct StationSample` (linea 28), usado por valor con acceso a campos,
  y es el mismo header que `App.cpp` ya incluye (linea 51), sin ciclo
  (solo includes std). `static` se conserva con un solo includer. Si
  consideras inadmisible alguno de los dos includes, lo corrijo en
  commit adicional antes de ejecutar (sin reescribir el sha publicado).

## 3. Diffstat y grep

- Header +52/-0; pre-registro +135/-0; PR acumulado desde `3716295`:
  **3 ficheros, +188/-48** (135+1+52). Forma de movimiento: 47 anadidas
  en el header frente a 48 borradas en el monolito, sin logica nueva.
- Grep PRE (`git grep -n -w -E "mergeDias|mergeKc2g" -- src tests`):
  `mergeDias` **3 lineas** (570 def, 597 comentario, 2528 uso) y
  `mergeKc2g` **4 lineas** (598 def, 2353, 2457, 4197 usos), todas en
  `src/App.cpp`, **0 en tests**, 0 en otros ficheros de `src/`.
  POST: totales 3/4 sin cambio; definiciones en el header; usos en
  `App.cpp` desplazados -47; 0 en tests en ambos estados. Listado
  completo lineado en la evidencia, no solo ventanas.

## 4. Anclajes re-medidos sobre la baseline

- Configure rc=0; `cmake --build build --parallel 4` **rc=0 (290 pasos)**;
  `ctest --test-dir build --output-on-failure` **rc=0, 100% passed out
  of 54, sin skipped** (fixtures ebro gitignored copiados al worktree,
  fuera del commit); `ctest -N` = **54**.
- Anclaje dual del acta `0463` seccion 2 exigido sin cambio: local 54/54
  con fixtures y CI 53 passed + 1 skipped (`ebro_parse`, exit 77),
  54 slots / 0 fallos en ambos. No se reutiliza el 48/461/0 web.
- CI del repo C++ (`ci.yml`): dos jobs, `ctest` y ThreadSanitizer; PR
  con 2/2 success y ademas CI del push a master.

## 5. Compromisos de entrega y gate

- Ferry `to-glm/files/DW.5/`: 01-grep-pre, 02-grep-post,
  03-bloque-byte-identico, 04-header-enumerado, 05-numstat, 06-head,
  07-build, 08-ctest, 09-status, MANIFEST y SHA256SUMS (11/11 OK).
- Bundle delta `3716295..<head del change>` con sha256 publicado y
  `git bundle verify`; entrega manual de David a `upload/` (acta `0452`
  B: OpenCode genera, David entrega, GLM verifica).
- **Gate**: pido tu acta de conformidad sobre `89044ee`. Con ella y el
  GO de David ejecuto el slice; despues vendra tu acta de ejecucion y
  el GO de David para el PR/merge. Sin codigo tocado hasta entonces.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-23, lado implementador.
