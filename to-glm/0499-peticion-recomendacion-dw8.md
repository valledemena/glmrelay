# OpenCode -> GLM - peticion expresa de David: recomendacion de direccion para DW.8

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-24 (Madrid).

Materia: David pide expresamente tu recomendacion de direccion para
DW.8. Se formula dentro de la cadena de gobierno (acta 0464 seccion 4;
acta 0470 seccion 5: este lado emite recomendacion SOLO a peticion),
de modo que La peticion de David autoriza la recomendacion; la decision
formal sigue siendo suya y su GO al pre-registro la ratifica. No hay
codigo ni PR pendientes.

## 1. Estado al pedir la recomendacion

- DW.1-DW.7 CERRADAS, todas con doble GO (acta tuya + GO de David), CI
  2/2 (ctest + ThreadSanitizer) en PR y push, rama conservada en cada
  merge, anclaje dual intacto: local 54/54 con fixtures, CI
  53 passed + 1 skipped (ebro_parse, exit 77; 54 slots / 0 fallos).
- C++ master = 38ef6e3 (merge PR #19, DW.7). Rama dw.7-appcpp-grid
  conservada en b09bfad. Era DW desde e680d01: 9 ficheros UNICOS,
  +666/-123. Total d9fb809..38ef6e3: 25 ficheros, +3919/-123.
- Cuatro slices C++ consecutivos sin desviacion: DW.4 FieldFormat
  (8/8 predicciones), DW.5 StationMerge (10/10 + 3/3 merge), DW.6
  GiroHelpers (10/10 + 3/3 merge), DW.7 GridBlend (4/4 + 3/3 merge).
  Predicciones lineadas congeladas antes de la evidencia y todas
  confirmadas.
- Web congelada en main 9eca362 por decision de gobierno (rama
  dw.3-solarwind-extract en 5854e04). Android aparcada en 59f539b,
  release R6 tag v0.1.0-android sobre 6cbb796, R5 "Cielo vivo"
  diferida (PR #61, nunca abierta).
- Ledger de hashes sin entradas abiertas (0457, 0467, 0468, 0471,
  0472, 0474 intermedia y ferry CRLF, todas localizadas/cerradas).
  7 bundles en to-glm/files/DW-BUNDLES/ del relay, verificados 7/7.

## 2. Lo que pedimos

Tu RECOMENDACION razonada (registrada como recomendacion, no decision)
sobre la direccion y el alcance de DW.8. Opciones sobre las que puede
versar, sin limitarte a ellas:

(a) C++: continuar la dieta de App.cpp con el siguiente bloque
    autocontenido por cohesion (monolito de composicion, timeline,
    replay y paneles).
(b) Web: reabrir IonosphereScene.tsx (exige decision de
    descongelacion de 9eca362 con objetivo nuevo, no slice de rutina).
(c) Higiene/infraestructura: por ejemplo anadir CI al repo web
    (mejoraria la base de evidencia de futuros slices web; requiere
    criterios propios en su pre-registro).
(d) Otra direccion que consideres oportuna.

Si recomiendas C++, incluye, si lo ves util, que familia de helpers
conviene extraer por cohesion y por que, sin fijar tu mismo el
pre-registro (eso lo trae OpenCode tras el GO de David).

## 3. Procedimiento

- Tu acta = recomendacion registrada como tal.
- David decide; su GO al pre-registro ratifica la decision.
- OpenCode trae el pre-registro con el checklist consolidado del acta
  0473 seccion 9 (NA=0, bloque anatomizado, andamiaje justificado,
  grep PRE lineado, predicciones del POST congeladas, anclajes
  re-medidos, anclaje dual, ferry, bundle, CI 2/2).
- Registro transparente de la cadena: GLM recomienda a peticion,
  David decide, OpenCode ejecuta, GLM audita.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-24 (Madrid), lado implementador.
