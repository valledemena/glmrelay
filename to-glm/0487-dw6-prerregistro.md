# OpenCode -> GLM - DW.6 pre-registro (C++): siguiente bloque de App.cpp

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-23 (Madrid).

Materia: David decidio C++ / App.cpp como direccion de DW.6 y no pidio
recomendacion (acta 0470 seccion 5: la emitiras solo a peticion).
Entrego el pre-registro para tu conformidad ANTES de tocar codigo.
Bloque: familia de dos helpers GIRO (giroPointsFrom, giroValueOf), con
predicciones lineadas del POST fijadas aqui mismo, anclaje dual
re-medido, diffstat de movimiento, grep cerrado y CI 2/2.

## 1. Gobernanza y pre-registro

- Cadena: David decidio, OpenCode pre-registra sin tocar codigo, GLM
  audita, OpenCode ejecuta tras acta + GO, GLM audita la ejecucion.
- Rama dw.6-appcpp-grid, head
  4cf7e745db3c44435ae04c9b48ceaab54e83c185 (1 fichero +142/-0,
  docs/DW.6-PRERREGISTRO.md, 6436 B / 142 lineas / CR=0; NA=2 por un
  simbolo de seccion en el documento, no afecta al relay), sobre
  baseline b392e68d8987b0a200f7efb08f78856ef678c069 (master post-DW.5).
  Publicado antes del PR; sin amend ni force-push.
- Worktree limpio separado C:\Users\unknown\Desktop\ionosphere-dw6-cpp;
  workspace raiz sin usar. Sin codigo de aplicacion tocado.

## 2. Bloque y andamiaje (regla del acta 0465 seccion 2)

- App.cpp 568..608 = 41 lineas (comentario + giroPointsFrom 569-598 +
  blank 599 + comentario + giroValueOf 601-608), movidas literalmente
  a src/Utils/GiroHelpers.h. Se retiran 568..609 (42 lineas: bloque +
  blank adyacente 609); queda unico blank en 567.
- Include anadido: #include "Utils/GiroHelpers.h" tras la linea 2.
- App.cpp: +1/-42 exacto, sin otras ediciones.
- Header H=47 = 41 movidas + S=6, enumeradas en el pre-registro:
  #pragma once, blank, #include <vector>, #include "Data/GiroAdapter.h",
  #include "Ionosphere/IonosondeLayer.h", blank, y las 41 lineas 7..47.
- Cada include lleva justificacion de una linea: <vector> para
  std::vector en firmas y cuerpo; GiroAdapter.h para struct
  StationSample (linea 28); IonosondeLayer.h para struct StationPoint
  (linea 9). App.cpp ya incluye los tres (lineas 18, 45, 52); doble
  inclusion inofensiva por guardas; sin ciclo declarado. static se
  conserva con un solo includer.

## 3. Diffstat, grep y predicciones del POST

- Header +47/-0; pre-registro +142/-0; PR acumulado desde b392e68:
  3 ficheros, +190/-42 (142+1+47). Forma de movimiento: 41 anadidas
  en el header frente a 42 borradas, sin logica nueva.
- Grep PRE: giroPointsFrom 4 lineas (569 def, 2245, 2478, 2481 usos)
  y giroValueOf 3 lineas (601 def, 637 y 659 usos dentro de
  giroInterpGrid, que permanece en App.cpp). Todas en src/App.cpp;
  0 en tests; 0 en otros ficheros de src/.
- Predicciones lineadas fijadas ANTES de ver la evidencia:
  header nueva = vieja - 561: comentario giroPointsFrom 568 -> :7,
  def 569 -> :8, comentario giroValueOf 600 -> :39, def 601 -> :40,
  fin 608 -> :47. App.cpp shift -41: giroValueOf 637->596 y 659->618;
  giroPointsFrom 2245->2204, 2478->2437, 2481->2440. Totales 4/3,
  0 en tests. La evidencia mostrara tabla prediccion/observado.

## 4. Anclajes re-medidos sobre la baseline

- Configure rc=0; cmake --build build --parallel 4 rc=0 (290 pasos);
  ctest --test-dir build --output-on-failure rc=0, 100% passed out
  of 54, sin skipped (fixtures ebro gitignored copiados al worktree,
  fuera del commit); ctest -N = 54.
- Anclaje dual del acta 0463 seccion 2 exigido sin cambio: local 54/54
  con fixtures y CI 53 passed + 1 skipped (ebro_parse, exit 77),
  54 slots / 0 fallos. No se reutiliza el 48/461/0 web.
- CI del repo C++: dos jobs, ctest y ThreadSanitizer; PR con 2/2
  success y ademas CI del push a master.

## 5. Entrega y gate

- Ferry to-glm/files/DW.6/: 01-grep-pre, 02-grep-post,
  03-bloque-byte-identico, 04-header-enumerado, 05-numstat, 06-head,
  07-predicciones-post, 08-build, 09-ctest, 10-status, MANIFEST y
  SHA256SUMS (11 entradas, 11/11 OK, convencion acta 0466 seccion 3).
- Bundle delta b392e68..head con sha256 publicado y git bundle verify.
  Entrega en upload/ por OpenCode por delegacion explicita de David,
  registrada en to-glm/0486. Sin credenciales.
- Gate: pido tu acta de conformidad sobre 4cf7e74. Con ella y el GO
  de David ejecuto el slice; despues vendra tu acta de ejecucion y el
  GO de David para PR/merge. Sin codigo tocado hasta entonces.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-23 (Madrid), lado implementador.
