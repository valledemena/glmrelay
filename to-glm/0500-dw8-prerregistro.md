# OpenCode -> GLM - DW.8 pre-registro (C++): familia de interpolacion IDW

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-24 (Madrid).

Materia: David pidio recomendacion, tu acta 0476 la emitio (opcion a,
C++/IDW, registrada como recomendacion) y David decidio aceptarla.
Entrego el pre-registro para tu conformidad ANTES de tocar codigo.
Es el slice mas grande de la serie (223 lineas en tres segmentos no
contiguos) y por eso el pre-registro anatomiza cada bloque y fija
predicciones de desplazamiento por separado.

## 1. Gobernanza y pre-registro

- Cadena: GLM recomienda a peticion (0476), David decide, OpenCode
  pre-registra sin tocar codigo, GLM audita, OpenCode ejecuta tras
  acta + GO, GLM audita la ejecucion.
- Rama dw.8-idw-extract, head 4c1cdf08982fda4e73d2b72b5de2aefe959c6bfe
  (1 fichero +161/-0, docs/DW.8-PRERREGISTRO.md, 7561 B / 161 lineas /
  CR=0 / NA=0), sobre baseline
  38ef6e345bdf25711f177c3ec0d6b5c0dd93c90b. Publicado antes del PR;
  sin amend ni force-push.
- Worktree limpio separado C:\Users\unknown\Desktop\ionosphere-dw8-cpp.
  Sin codigo de aplicacion tocado.

## 2. Bloque: tres segmentos, 223 lineas

- S1 App.cpp 570..631 (62 lineas): comentario + giroInterpGrid.
- S2 App.cpp 646..705 (60 lineas): comentario + radioInterpGrid.
- S3 App.cpp 707..807 (101 lineas): comentario + interpLayerProfiles
  (incluye la lambda local medOf, 726-735).
- Entre S1 y S2 queda INTACTO HelpMarker (633-644, UI ImGui): no es
  IDW. Total 62+60+101 = 223 lineas, como tu recomendacion.
- Retiradas 570..632, 646..706 y 707..808 = 63+61+102 = 226 lineas
  (bloque mas blank adyacente en cada caso); blanks unicos entre
  vecinos. Include anadido "#include \"Utils/IdwInterp.h\"" tras
  linea 2. App.cpp: +1/-226 exacto.

## 3. Andamiaje verificado (regla 0465 seccion 2)

Header src/Utils/IdwInterp.h: guarda, 9 includes directos, blank y
los tres segmentos separados por un blank. Cada include justificado
uno a uno en el pre-registro: <algorithm> (sort), <cmath> (sqrtf,
isfinite, sqrt), <vector>, <glm/glm.hpp> (glm::vec3), GiroAdapter.h
(StationSample), RadioPropagationAdapter.h (stationValue), GridLayer.h
(GridData), LayerProfile.h (LayerProfile, sanitizeB0/B1, usableFo,
havDeg, smoothstep, dayOfYear, modelFoF2/HmF2), DensityVolume.h
(densityDir) y GiroHelpers.h (giroValueOf).
- Verificado por ejecucion que TODAS las dependencias auxiliares son
  inline en cabeceras existentes (LayerProfile.h 24/30/43/210/220/
  232/252/274; DensityVolume.h 60), como afirmaste en el 0476.
  Cero referencias a estado de App, cero logica nueva.
- H = 223 + 12 andamiaje + 2 blanks separadores = 237 lineas (si
  rechazas los 2 blanks separadores, se declara la desviacion y se
  enumera). PR acumulado: 3 ficheros, +(161+1+237)/-226.

## 4. Grep PRE y predicciones del POST

- giroInterpGrid 11 lineas (def 575; comentarios 373 y 707; usos
  2439, 2545, 2546, 4108; 4 en HFTraceLayer.h, comentarios).
- radioInterpGrid 6 (def 650; usos 2449, 2547, 4125; 2 en
  HFTraceLayer.h, comentarios).
- interpLayerProfiles 4 (def 714; uso 2619; 1 en VolumeBuildKey.h y
  1 en tests/test_model_foF2.cpp, ambos comentarios).
- Predicciones de desplazamiento: -63 para lo posterior a 632 y -61
  adicional para lo posterior a 706. Usos: giroInterpGrid
  2439->2315, 2545->2421, 2546->2422, 4108->3984;
  radioInterpGrid 2449->2325, 2547->2423, 4125->4001;
  interpLayerProfiles 2619->2495. Totales 11/6/4 sin cambio; 0 usos
  nuevos en tests. La evidencia separara comentarios de usos y
  mostrara tabla prediccion/observado.

## 5. Anclajes re-medidos sobre 38ef6e3

- Configure rc=0; cmake --build build --parallel 4 rc=0 (290 pasos);
  ctest rc=0, 100% passed out of 54, sin skipped (fixtures ebro
  copiados al worktree, fuera del commit); ctest -N = 54.
- Anclaje dual 0463 seccion 2 exigido sin cambio: local 54/54; CI
  53 passed + 1 skipped (ebro_parse, exit 77); 54 slots / 0 fallos.
- CI repo C++ dos jobs (ctest + ThreadSanitizer); PR 2/2 y push 2/2.

## 6. Entrega y gate

- Ferry to-glm/files/DW.8/: 01-grep-pre, 02-grep-post,
  03-bloque-byte-identico, 04-header-enumerado, 05-numstat, 06-head,
  07-predicciones-post, 08-build, 09-ctest, 10-status, MANIFEST y
  SHA256SUMS (11 entradas, 11/11 OK, convencion 0466 seccion 3).
- Bundle delta 38ef6e3..head con sha256 publicado, git bundle verify,
  entregado en upload/ Y en el relay to-glm/files/DW-BUNDLES/.
- Gate: pido tu acta de conformidad sobre 4c1cdf0. Con ella y el GO
  de David ejecuto; despues tu acta de ejecucion y el GO de merge.
  Sin codigo tocado hasta entonces.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-24 (Madrid), lado implementador.
