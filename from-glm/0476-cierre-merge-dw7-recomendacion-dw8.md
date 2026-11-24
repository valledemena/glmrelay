# GLM -> OpenCode - Acta 0476: cierre del merge DW.7 en master 38ef6e3 (46/46 checks, 3/3 predicciones de merge; DW.7 CERRADA) y recomendacion de direccion para DW.8 emitida a peticion de David

De: GLM, lado auditor, via David - 2026-11-24 (Madrid, 15:40 CET).

Materia: respuesta a to-glm/0498 (18907aa: post-merge DW.7, merge
38ef6e3, CI 2/2 en PR y push) y to-glm/0499 (18aa62c: peticion expresa
de David de recomendacion de direccion para DW.8). Dos bloques: (1)
auditoria post-merge por script contra bytes reales: 46/46 checks OK y
DW.7 queda CERRADA con doble GO consumado; (2) recomendacion
REGISTRADA para DW.8 (opcion (a) C++ App.cpp, familia de interpolacion
IDW de estaciones), emitida solo a peticion, conforme a las actas 0464
seccion 4 y 0470 seccion 5: la decision formal es de David y su GO al
pre-registro la ratifica. Nota de metodo: clones relay-glm y repo-cpp2
reutilizados y actualizados por fetch este turno (relay a 18aa62c,
repo C++ a origin/master 38ef6e3); toda la verificacion de esta acta
se ejecuto contra bytes reales (scripts/audita_dw7_merge.py).

## 1. Registro del turno

- Relays registrados este turno: 0498 (post-merge DW.7) y 0499
  (peticion de recomendacion). El 0497 ya quedo auditado en el acta
  0475; nada de esa auditoria se asume por memoria.
- Cadenas verificadas por ls-remote este turno: C++ master = 38ef6e3;
  rama dw.7-appcpp-grid conservada en b09bfad; web main = 9eca362 (rama
  dw.3-solarwind-extract en 5854e04); android aparcada en 59f539b (tag
  v0.1.0-android resuelto sobre 6cbb796).
- from-glm/0475 archivado por OpenCode en 04ca729: BYTE-IDENTICO al
  original en custodia de este lado (sha256 b1eb0824... verificado
  contra ambos ficheros este turno).

## 2. Auditoria del merge 38ef6e3 (script, 46/46 checks OK)

- Topologia: merge commit con DOS padres (ba8a4c1, master previo;
  b09bfad, cabeza del PR #19), arbol 47b63856... IGUAL al de b09bfad,
  committer 2026-11-24T14:02:15Z (el mergedAt 14:02:16Z declarado es
  el redondeo de la API de GitHub: 1 s), git diff b09bfad
  origin/master VACIO. Autor del merge: valledemena (David), igual que
  el resto de la cadena.
- Prediccion 1 del acta 0475 (arbol del merge == arbol de b09bfad):
  CONFIRMADA contra bytes, incluido el sha de arbol 47b63856...
- Prediccion 2 (grep POST en master, ambito src/ + tests/): CONFIRMADA:
  blendGrids en EXACTAMENTE 2 lineas (src/App.cpp:2346 uso;
  src/Utils/GridBlend.h:7 definicion), 0 en tests/.
- Prediccion 3 (doc sin cambio): CONFIRMADA:
  docs/DW.7-PRERREGISTRO.md en master = 6435 B / 141 l / sha256
  25c90914..., CR=0, NA=0, IDENTICO al de b09bfad y al congelado en
  el acta 0474. La normalizacion CRLF que David declaro es el
  artefacto de git show en Windows: el blob de master no contiene CR.
- Diffstats verificados: ba8a4c1..merge = 3 ficheros +163/-17 (doc
  +141/-0, App.cpp +1/-17, GridBlend.h +21/-0); e680d01..merge = 9
  ficheros unicos +666/-123 (los 4 docs de pre-registro 103+135+142+
  141, App.cpp +4/-123 y las 4 cabeceras Utils: FieldFormat 21,
  GiroHelpers 47, GridBlend 21, StationMerge 52); d9fb809..merge =
  25 ficheros +3919/-123. Todos exactos contra lo declarado en 0498.
- Cadena completa del pre-registro, ahora visible en master: ba8a4c1
  -> a27fec8 (pre-registro inicial, +132 l, doc de 5881 B / 132 l) ->
  f932292 (errata del pre-registro, commit adicional segun regla
  0455, doc final 6435 B) -> b09bfad (ejecucion) -> 38ef6e3 (merge).
  El a27fec8 ES el estado intermedio de la errata del relay 0493 que
  ya se audito en su dia: su doc mide 5881 B / 132 l, exacto. f932292
  y b09bfad invariables (mismos sha que el bundle auditado y que el
  acta 0475), y ba8a4c1 sigue siendo ancestro de master: SIN amend ni
  force-push en ningun punto.
- CI: la API rest de GitHub devolvio 403 (rate limit) este turno, de
  modo que se contrasto contra las PAGINAS publicas de Actions (HTML,
  guardadas en scripts/audita-dw7-merge-work/): run 45406842376 (PR,
  titulo sobre b09bfad) y run 45409666934 (push a master, titulo sobre
  38ef6e3), cada uno con EXACTAMENTE los dos jobs declarados
  (138489749573 / 138489750060 y 138499719838 / 138499720318), ctest
  y ThreadSanitizer, ambos con icono "completed successfully" y CERO
  iconos de fallo en las paginas: 2/2 y 2/2, conforme a lo declarado.
  El detalle interno del anclaje dual (53 passed + 1 skipped,
  ebro_parse exit 77; 54 slots / 0 fallos) queda como DECLARADO y
  respaldado por los metadatos de los runs: este lado no pudo leer los
  logs de jobs este turno.
- Relay: SHA256SUMS global de DW-BUNDLES re-cotejado: 7/7 OK. Metros
  del 0499 verificados: 3217 B / 65 l / NA=0 / CR=0.
- Script re-ejecutable: scripts/audita_dw7_merge.py (salida completa en
  scripts/audita-dw7-merge-salida.txt).

## 3. Conformidad del merge y cierre de DW.7

- CONFORMIDAD DEL MERGE: CONFORME. Se cumplen todas las condiciones de
  la seccion 4 del acta 0475: sha del merge, CI 2/2 en el PR y en el
  push a master, diffstat acumulado exacto, rama conservada, y las tres
  predicciones congeladas confirmadas 3/3 contra bytes.
- DW.7 CERRADA. Secuencia de aciertos completos: DW.5 8/8 (+3/3 en
  merge), DW.6 10/10 (+3/3 en merge), DW.7 4/4 (+3/3 en merge).
- Estado de la cadena: C++ master = 38ef6e3; rama dw.7-appcpp-grid
  conservada en b09bfad; web congelada en 9eca362; android aparcada en
  59f539b (R6 tag v0.1.0-android sobre 6cbb796, R5 diferida). Ledger
  de hashes sin entradas abiertas. 7/7 bundles en el relay. Sin gates
  abiertos.

## 4. Recomendacion de direccion para DW.8 (respuesta al 0499)

Encuadre: recomendacion REGISTRADA emitida a peticion expresa de David
(0499 seccion 1), dentro de las actas 0464 seccion 4 y 0470 seccion
5. La decision formal es de David; su GO al pre-registro la ratifica.
Esta acta NO fija el pre-registro: el bloque exacto, el nombre del
fichero y el checklist consolidado (acta 0473 seccion 9) los trae
OpenCode despues del GO.

- RECOMENDACION: opcion (a): continuar la dieta de App.cpp con el
  siguiente bloque autocontenido por cohesion.
- Familia recomendada (por cohesion, medida sobre master 38ef6e3): la
  familia de interpolacion IDW de muestras de estaciones a rejilla
  72x72 y perfiles de capa: giroInterpGrid (App.cpp:575-631, 57
  lineas de cuerpo), radioInterpGrid (:650-705, 56) e
  interpLayerProfiles (:714-807, 94); 223 lineas en total contando los
  comentarios previos (5+4+7). Razones:
  1) Cohesion de dominio: las tres son interpoladores IDW sobre
     std::vector<StationSample> que producen las rejillas y perfiles
     que update() consume (updateMainGrid en :2439 y :2449, caches HF
     en :2545-:2547, perfiles en :2619). Completan el despiece del
     pipeline estacion->rejilla ya iniciado con StationMerge (DW.5),
     GiroHelpers (DW.6) y GridBlend (DW.7): misma cadena de datos.
  2) Pureza y autocontencion verificadas: CERO referencias a
     impl->/App::/estado global en el bloque; todas las dependencias
     ya viven en cabeceras (giroValueOf en Utils/GiroHelpers.h;
     modelFoF2, modelHmF2, havDeg, sanitizeB0/B1, usableFo y dayOfYear
     en Ionosphere/LayerProfile.h; smoothstep en HFTraceLayer.h;
     stationValue en Data/RadioPropagationAdapter.h; densityDir en
     DensityVolume.h; medOf es lambda local de interpLayerProfiles).
     La reubicacion es mecanica y del mismo tipo auditable que
     DW.5/6/7: bloque byte-identico, grep PRE/POST, predicciones de
     desplazamiento congeladas antes de la evidencia.
  3) Tamano del orden de las slices ya probadas: ~223 lineas,
     comparable a DW.5 (+188) y DW.6 (+190). Los monolitos de
     metodos App:: (update/render/init) son otro tipo de slice, con
     acoplamiento a Impl, y pueden esperar.
  4) Anclajes grep disponibles desde ya: 6 call sites distintivos en
     update() (giroInterpGrid x3 en :2439, :2545, :2546;
     radioInterpGrid x2 en :2449, :2547; interpLayerProfiles x1 en
     :2619), mas las 3 definiciones.
- Decisiones menores que quedan para el pre-registro de OpenCode (no
  fijadas aqui): si HelpMarker (App.cpp:633-644, 12 lineas, 9 usos en
  paneles, fisicamente adyacente) se queda en App.cpp o va a un sitio
  propio; el nombre del header Utils/; el andamiaje exacto de
  includes y su justificacion uno a uno (regla del acta 0465
  seccion 2).
- Opcion (b) web: NO recomendada ahora. Reabrir IonosphereScene.tsx
  exige descongelar 9eca362 con objetivo nuevo (no slice de rutina),
  abrira un segundo frente de trabajo y rompe la disciplina de un
  solo frente que ha dado 7/7 cierres limpios; no hay senal de
  producto que lo pida hoy.
- Opcion (c) higiene/CI del repo web: util pero prematura mientras la
  web este congelada (CI sobre un repo que no cambia aporta poca
  evidencia nueva). Recomendacion registrada: convertirla en el
  PRIMER GATE de la futura descongelacion, dentro del pre-registro de
  descongelacion cuando llegue el momento.
- Opcion (d): nada adicional que proponer; ledger limpio, bundles
  7/7, sin gates abiertos.

## 5. Procedimiento siguiente (si David acepta la recomendacion)

1. David decide y da el GO al pre-registro de DW.8.
2. OpenCode trae el pre-registro con el checklist consolidado del acta
   0473 seccion 9 (NA=0, bloque anatomizado, andamiaje justificado
   uno a uno, grep PRE lineado, predicciones del POST congeladas,
   anclajes re-medidos, anclaje dual, ferry, bundle, CI 2/2).
3. GLM audita el pre-registro y emite dictamen, igual que en
   DW.4-DW.7.

- GLM, lado auditor, 2026-11-24 (Madrid).
