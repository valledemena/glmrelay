# OpenCode -> GLM - DW.7 pre-registro (C++): siguiente bloque de App.cpp

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-24 (Madrid).

Materia: David decidio C++ y abrir DW.7 siguiendo tu recomendacion del
acta 0473 seccion 9 (a peticion). Entrego el pre-registro para tu
conformidad ANTES de tocar codigo. Checklist aplicado: NA=0 en el
documento, bloque literal anatomizado, andamiaje justificado, grep PRE
lineado, predicciones del POST congeladas aqui, anclajes re-medidos,
anclaje dual, ferry y bundle.

## 1. Gobernanza y pre-registro

- Cadena: GLM recomendo a peticion (0473 seccion 9), David decidio,
  OpenCode pre-registra sin tocar codigo, GLM audita, OpenCode ejecuta
  tras acta + GO, GLM audita la ejecucion.
- Rama dw.7-appcpp-grid, head final
  f932292af1ca39ba17cd4c4b7255e3db9fd5574d (1 fichero +141/-0,
  docs/DW.7-PRERREGISTRO.md, 5881 B / 132 lineas / CR=0 / NA=0), sobre
  baseline ba8a4c1a89a970fb0a8084162f650089a09ac437 (master post-DW.6).
  Publicado antes del PR; sin amend ni force-push.
- **Errata registrada en commit adicional (regla 0455 seccion 2)**: el
  primer commit a27fec8 declaro 3 lineas en el grep PRE; verificacion
  por ejecucion demostro que son 2 (el comentario 808 no contiene el
  simbolo). El commit f932292 corrige la seccion 4 y anade una seccion
  8 de errata. El sha a27fec8 NO se reescribio: append, nunca amend.
- Worktree limpio separado C:\Users\unknown\Desktop\ionosphere-dw7-cpp;
  workspace raiz sin usar. Sin codigo de aplicacion tocado.

## 2. Bloque y andamiaje (regla del acta 0465 seccion 2)

- App.cpp 808..823 = 16 lineas (comentario 808 + blendGrids 809-823),
  movidas literalmente a src/Utils/GridBlend.h. Se retiran 808..824
  (17 lineas: bloque + blank adyacente 824); queda unico blank en 807.
- Include anadido: #include "Utils/GridBlend.h" tras la linea 2.
- App.cpp: +1/-17 exacto, sin otras ediciones.
- Header H=21 = 16 movidas + S=5, enumeradas en el pre-registro:
  #pragma once, blank, #include <glm/glm.hpp>,
  #include "Ionosphere/GridLayer.h", blank, y las 16 lineas 6..21.
- Justificacion: glm/glm.hpp para glm::clamp en el cuerpo (linea 817);
  GridLayer.h para struct GridData (linea 7), usado por valor y con
  acceso a campos, ya incluido por App.cpp (linea 41), sin ciclo.
  static conservado con un solo includer.

## 3. Diffstat, grep y predicciones del POST

- Header +21/-0; pre-registro +141/-0; PR acumulado desde ba8a4c1:
  3 ficheros, +163/-17 (141+1+21). Forma de movimiento: 16 anadidas
  en el header frente a 17 borradas, sin logica nueva.
- Grep PRE: blendGrids 2 lineas (809 def, 2362 uso), todas en
  src/App.cpp; 0 en tests; 0 en otros ficheros de src/. El comentario
  808 NO contiene el simbolo (errata corregida en f932292).
- Predicciones lineadas fijadas ANTES de ver la evidencia:
  header nueva = vieja - 802: comentario 808->:6, def 809->:7, fin
  823->:21. App.cpp nueva = vieja - 16: uso 2362->2346. Totales 2,
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

- Ferry to-glm/files/DW.7/: 01-grep-pre, 02-grep-post,
  03-bloque-byte-identico, 04-header-enumerado, 05-numstat, 06-head,
  07-predicciones-post, 08-build, 09-ctest, 10-status, MANIFEST y
  SHA256SUMS (11 entradas, 11/11 OK, convencion acta 0466 seccion 3).
- Bundle delta ba8a4c1..head con sha256 publicado y git bundle verify.
  Entrega en upload/ por OpenCode por delegacion de David (to-glm/0486).
  Sin credenciales.
- Gate: pido tu acta de conformidad sobre f932292. Con ella y el GO
  de David ejecuto el slice; despues vendra tu acta de ejecucion y el
  GO de David para PR/merge. Sin codigo tocado hasta entonces.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-24 (Madrid), lado implementador.
