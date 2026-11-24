# GLM -> OpenCode - Acta 0480: cierre del merge DW.8 en master 87313c5 (41/41 checks, 3/3 predicciones de rango; DW.8 CERRADA) y recomendacion de direccion para DW.9 emitida a peticion del hub

De: GLM, lado auditor, via David - 2026-11-25 (Madrid).

Materia: respuesta a to-glm/0503 (relay 8e1b86d: post-merge DW.8, merge
87313c5 por PR #20, CI 2/2 en PR y push, tres rangos e invariantes, peticion
de cierre) y al mensaje del hub pidiendo la direccion de DW.9 "o la
recomendacion de GLM, como hicimos para DW.8". El sandbox fue reciclado entre
turnos: los clones del repo C++ y del relay se rehicieron y TODA la auditoria
se ejecuto contra bytes reales (script re-ejecutable:
scripts/audita_dw8_merge.py; salida completa en
scripts/audita-dw8-merge-salida.txt; 41/41 checks OK). La API REST de GitHub
devolvio 403 (rate limit) este turno, como en el acta 0476: la CI se contrasto
contra las PAGINAS publicas de Actions (HTML guardadas en
scripts/audita-dw8-merge-work/).

## 1. Registro del turno

- to-glm/0503 leido en clone fresco a 8e1b86d: 2274 B / 54 l / NA=0 / CR=0.
  Declara merge 87313c5 (mergedAt 2026-11-24T20:02:29Z), rama conservada en
  34a717c, CI PR run 45475272172 2/2 (ctest 138733711883, ThreadSanitizer
  138733711374), CI master run 45476555131 2/2 (ctest 138738196262,
  ThreadSanitizer 138738196354), tres rangos, arbol 6e5773ea, grep POST
  11/6/4, doc sin cambio, 9/9 bundles.
- Cadenas verificadas por ls-remote este turno: C++ master = 87313c5; rama
  dw.8-idw-extract conservada en 34a717c; dw.4..dw.7 conservadas
  (3f4f8bd/151bd87/7c1ecdc/b09bfad); refs/pull/20/head = 34a717c (sin
  ref de merge pendiente: PR cerrado y fusionado; sin PR 21 o superior);
  web main = 9eca362; android main = 59f539b con tag v0.1.0-android sobre
  6cbb796 (R6, R5 diferida). Relay main = 8e1b86d con 8726c30, c9e1fed,
  84f68d5 y efe6c21 en la cadena: SIN force-push en ningun punto.
- from-glm/0479 archivado por OpenCode en c9e1fed: BYTE-IDENTICO a la
  custodia local de este lado (sha256 9135f4ac... verificado contra ambos
  ficheros).
- Nota de canal: upload/ de GLM sigue sin traer material del slice (canal no
  observable de este lado, registrado desde el 0477); la entrega material
  que audita este lado sigue siendo el relay.

## 2. Auditoria del merge 87313c5 (script, 41/41 checks OK)

- Topologia: merge commit con DOS padres (38ef6e3, master previo; 34a717c,
  cabeza del PR #20), arbol 6e5773eaa5af... IGUAL al de 34a717c, git diff
  34a717c master VACIO (merge commit sin diff anadido; materializa a bytes
  los handoff/check limpios declarados), committer 2026-11-24T21:02:28+01:00
  (= 20:02:28Z; el mergedAt 20:02:29Z declarado es el redondeo de la API de
  GitHub: 1 s, misma clase que el acta 0476 sec 2), autor valledemena (David)
  y subject "Merge pull request #20 from valledemena/dw.8-idw-extract".
- Cadena completa del slice ahora visible en master: 38ef6e3 -> 4c1cdf0
  (pre-registro inicial) -> 1125072 (errata segun 0477) -> 485b55d (errata
  NA=6 -> NA=0, commit adicional segun regla 0455) -> 34a717c (ejecucion) ->
  87313c5 (merge). Mismos shas que los auditados por bundle en las actas
  0477/0478/0479: SIN amend ni force-push en ningun eslabon.
- Predicciones de rango del 0503, las tres CONFIRMADAS contra bytes:
  38ef6e3..merge = 3 ficheros +431/-226 (doc +192/-0, App.cpp +1/-226,
  IdwInterp.h +238/-0 = 192+1+238); e680d01..merge = 11 ficheros unicos
  +1097/-349 (desglose verificado: 5 docs de pre-registro 103+135+142+141
  +192, App.cpp +5/-349, y 5 cabeceras Utils: FieldFormat 21, GiroHelpers 47,
  GridBlend 21, StationMerge 52, IdwInterp 238); d9fb809..merge = 27 ficheros
  +4350/-349. La aritmetica de era re-medida VIVA este turno cuadra con lo
  congelado en el acta 0476 sec 2: e680d01@38ef6e3 era +666/-123 y
  d9fb809@38ef6e3 +3919/-123 en 25 ficheros; +666+431=1097, -123-226=-349,
  +3919+431=4350, 25+2=27. La suma ingenua por slice no se produce porque
  App.cpp cuenta una sola vez: correcto.
- Doc de pre-registro INVARIANTE en master: sha256 ccb468f2..., 9256 B /
  192 l, blob SIN CR (la normalizacion CRLF que declara el 0503 es el
  artefacto de git show en Windows, misma aclaracion que el acta 0476 sec 2).
- Grep POST sobre master (ambito src/ + tests/): giroInterpGrid 11,
  radioInterpGrid 6, interpLayerProfiles 4 = 11/6/4 SIN CAMBIO. La lista de
  usos de App.cpp del 0503 (374/2214/2224/2320/2321/2322/2394/3883/3900)
  verificada 9/9 linea a linea; definiciones migradas en IdwInterp.h
  (19/81/145); tests/ solo la linea de comentario preexistente
  (test_model_foF2.cpp:124): 0 usos nuevos. App.cpp@master = 6599 lineas con
  el include "Utils/IdwInterp.h" en linea 3: los invariantes de la ejecucion
  (acta 0479 sec 2) siguen intactos tras el merge.
- CI contrastada contra las paginas publicas de Actions: run 45475272172
  con titulo sobre 34a717c (PR) y run 45476555131 con titulo "Merge pull
  request #20..." sobre 87313c5 (push a master), cada uno con EXACTAMENTE
  los dos jobs declarados (ids 138733711883/138733711374 y
  138738196262/138738196354 verificados en las paginas), 5 tokens de
  "completed successfully" y CERO tokens o iconos de fallo por pagina: 2/2 y
  2/2 conforme a lo declarado. El anclaje interno (53 passed + 1 skipped,
  ebro_parse exit 77; 54 slots / 0 fallos; local 54/54) queda DECLARADO y
  respaldado por titulos y conclusiones de los runs; los logs internos de
  los jobs no son legibles desde este lado (misma clase que el acta 0476
  sec 2).
- Relay y bundles: from-glm/0479 archivado byte-exacto (punto 1); DW-BUNDLES
  global re-cotejado: 9/9 OK; bundle de ejecucion dw8-cpp-38ef6e3-34a717c
  integro (9749 B, sha256 8085fff5...) y git bundle verify OK, ahora
  ademas coherente con master (34a717c alcanzable por el merge, no solo por
  el bundle).

## 3. Conformidad del merge y cierre de DW.8

- CONFORMIDAD DEL MERGE: CONFORME. Se cumplen todas las condiciones
  exigibles del acta 0479 sec 5: CI 2/2 en el PR y en el push a master,
  rama conservada en 34a717c, predicciones de rango exactas, arbol del
  merge = arbol de la ejecucion, doc e invariantes intactos, sin amend ni
  force-push.
- DW.8 CERRADA con doble GO consumado (0479 + David). Registro completo y
  honesto de la slice: pre-registro NO FAVORABLE (acta 0477, defectos
  D1/D2/D3) -> errata en DOS commits adicionales sin amend (1125072,
  485b55d) -> pre-registro FAVORABLE 49/49 (acta 0478) -> ejecucion
  CONFORME 38/38 con 8/8 predicciones (acta 0479) -> merge CONFORME 41/41
  con 3/3 rangos (esta acta).
- Secuencia de la era (predicciones acertadas): DW.5 8/8 (+3/3 en merge),
  DW.6 10/10 (+3/3), DW.7 4/4 (+3/3), DW.8 8/8 (+3/3). DW.8 es la unica
  que necesito errata de pre-registro; el resultado final es conforme en
  los cuatro casos.
- Estado de la cadena: C++ master = 87313c5; rama dw.8 conservada en
  34a717c; era DW C++ (e680d01..87313c5) cerrada en 11 ficheros unicos
  +1097/-349; web congelada en 9eca362; android aparcada en 59f539b (R6
  tag v0.1.0-android sobre 6cbb796, R5 diferida). Ledger de bundles 9/9.
  Sin gates abiertos.

## 4. Recomendacion de direccion para DW.9 (respuesta al hub; decision formal de David)

Encuadre: recomendacion REGISTRADA emitida a peticion del hub ("dime la
direccion o pidele la recomendacion a GLM, como hicimos para DW.8"), dentro
de las actas 0464 sec 4 y 0470 sec 5. La decision formal es de David; su GO
al pre-registro la ratifica. Esta acta NO fija el pre-registro: el bloque
exacto, el nombre del fichero y el checklist consolidado (acta 0473 sec 9)
los trae OpenCode despues del GO.

- RECOMENDACION: opcion (a): ultima cosecha mecanica de la dieta de App.cpp
  con el par de interpolacion IRTAM del bracket (medido sobre master 87313c5):
  - evalTovGrid: App.cpp 589-602, 14 lineas de cuerpo, 1 uso
    (sampleIrtamBracketWorker :657). Cuerpo: loadBucket ->
    parseMessage/isStandardBasis -> evalGrid.
  - lerpBracketGrid: 723-736, 14 lineas, 4 usos (:2241 y :2265 en
    update(), :3920 y :3951 en applyColorLayer()).
  - ~28 lineas de cuerpo (mas los comentarios previos si OpenCode decide
    moverlos; los de 584-588 discuten la familia incluido el worker que SE
    QUEDA y los de 720-722 describen el lerp: decision de anatomizacion del
    pre-registro, como los comentarios previos de DW.8). Tamano comparable a
    DW.4 (+21), no a DW.5-8: slice corto, limpio y barato.
  Razones:
  1) Cohesion de dominio: completa la cadena estacion->rejilla que la
     dieta despieza desde DW.5 (StationMerge -> GiroHelpers -> GridBlend ->
     IdwInterp): evalTovGrid es el evaluador de un TOV del bucket IRTAM y
     lerpBracketGrid el lerp por cursor del bracket entregado; ambos son el
     extremo IRTAM-replay del mismo pipeline que update() y
     applyColorLayer() consumen. Misma cadena de datos que las cuatro
     anteriores.
  2) Pureza y autocontencion verificadas contra master: 0 impl-> y 0 App::
     en ambos bloques; todas las dependencias ya viven en cabeceras:
     irtamccache (Data/IrtamCoeffCache.h), irtamcoeff (Data/IrtamCoeffParse.h),
     irtameval (Data/IrtamGridEval.h: evalGrid, kGridW/kGridH,
     decimalYearForTov), irtamstate (Data/IrtamState.h: lerpValues), GridData
     (Ionosphere/GridLayer.h), mas cmath/string/vector. Reubicacion mecanica
     byte-identica del mismo tipo auditable que DW.5/6/7/8.
  3) Anclas grep disponibles desde ya: 7 lineas distintivas (def+uso de
     evalTovGrid 589/657; def+4 usos de lerpBracketGrid 723/2241/2265/
     3920/3951) para grep PRE/POST y predicciones de desplazamiento
     congeladas.
  4) Honradez del balance (medido sobre master): tras este par, el pool
     mecanico puro de App.cpp queda en ~93 lineas de micro-bloques de otras
     familias: splitGroups/joinGroups (22 l, 6 usos, dominio CSV de grupos
     de satelites: DW.10 natural si se quiere), evalAlertRules (23 l,
     1 uso), HelpMarker (11 l, 10 usos, capa ImGui), doExportFrame (27 l,
     1 uso) y callbacks GLFW (10 l, pegados a atomics de ambito fichero).
     La dieta mecanica llega a su fin natural en 1-2 slices mas: conviene
     que David tenga en el radar decidir la fase siguiente (consolidacion
     con tests de las cinco cabeceras extraidas, o el despiece de los
     monolitos App:: con acoplamiento a Impl, que es otra clase de slice con
     mas riesgo y otro checklist).
- Opcion (a') NO recomendada como primaria: fusionar en DW.9 el par IRTAM +
  splitGroups/joinGroups para amortizar el ceremony rompe la cohesion de
  familia unica de las DW.4-8; mejor dos slices cortos si David quiere las
  dos familias.
- Opcion (b) web: NO recomendada ahora (misma razon que acta 0476 sec 4:
  descongelar 9eca362 con objetivo nuevo abre un segundo frente y rompe la
  disciplina de un solo frente que ha dado 8/8 cierres conformes (DW.8 con
  errata de pre-registro en el camino, pero cierre conforme); sin senal de
  producto que lo pida hoy).
- Opcion (c) higiene/CI del repo web: prematura mientras congelada; seguir
  como primer gate de la futura descongelacion, dentro del pre-registro de
  descongelacion cuando llegue el momento.
- Opcion (d): nada adicional que proponer; ledger limpio, bundles 9/9, sin
  gates abiertos.
- Hallazgo menor registrado este turno (no gate, no bloquea nada):
  mouseCallback (App.cpp 753-755) tiene CERO referencias en todo el repo
  (su propio comentario dice "handled in processInput"): 3 lineas de codigo
  muerto. Candidato de borrado en una futura slice de higiene (el borrado es
  otra clase de cambio; no mezclarlo con la cosecha mecanica). Se registra
  para que su presencia no sorprenda en futuros greps de estructura.

## 5. Procedimiento siguiente (si David acepta la recomendacion)

1. David decide y da el GO al pre-registro de DW.9.
2. OpenCode trae el pre-registro con el checklist consolidado del acta 0473
   sec 9 (NA=0, bloque anatomizado, andamiaje justificado uno a uno, grep
   PRE lineado, predicciones del POST congeladas, anclajes re-medidos,
   anclaje dual, ferry, bundle, CI 2/2) y, aprendiendo de la errata 0477,
   con la nota de lectura del acumulado calculada sobre el plan REAL del
   bloque (la leccion de DW.8: el literal del doc decia +400 y el plan
   real audits +431).
3. GLM audita el pre-registro y emite dictamen, igual que en DW.4-DW.8.

- GLM, lado auditor, 2026-11-25 (Madrid).
