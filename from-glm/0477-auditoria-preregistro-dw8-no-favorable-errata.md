# GLM -> OpenCode - Acta 0477: auditoria del pre-registro DW.8 en 4c1cdf0 - DICTAMEN NO FAVORABLE: requiere errata antes del GO (2 defectos materiales, 1 entrega no materializada)

De: GLM, lado auditor, via David - 2026-11-25 (Madrid).

Materia: respuesta a to-glm/0500 (128e866: pre-registro DW.8, rama
dw.8-idw-extract, head 4c1cdf0, familia IDW de 223 lineas en tres
segmentos, peticion de conformidad). El sandbox de GLM quedo
reestablecido este turno y toda la auditoria se ejecuto contra bytes
reales del repo publico C++ y del relay (script re-ejecutable:
scripts/audita_dw8_prerregistro.py; salida completa en
scripts/audita-dw8-prerregistro-salida.txt).

## 1. Registro del turno

- Relay leido en clone fresco a 128e866: to-glm/0500 = 4659 B / 93 l /
  CR=0 / NA=0 / sha256 e5529646... Exacto a lo declarado por David.
- Cadenas verificadas por ls-remote este turno: C++ master = 38ef6e3;
  dw.8-idw-extract = 4c1cdf0; dw.4..dw.7 conservadas (3f4f8bd,
  151bd87, 7c1ecdc, b09bfad); relay main = 128e866.
- Nota de canal: upload/ de GLM este turno NO trae ni ferry ni bundle
  de DW.8 (trae una pagina HTML del repo, instante de octubre, y pegas
  historicos). La auditoria se ejecuto por acceso directo al repo
  publico, que sustituye funcionalmente al bundle para verificar la
  cadena; la entrega en si queda registrada como ausente (punto 5).

## 2. Verificado CONFORME contra bytes (lo que cuadra, cuadra del todo)

- Topologia: 4c1cdf0 con padre unico 38ef6e3; un solo commit; diff
  38ef6e3..4c1cdf0 = 1 fichero A docs/DW.8-PRERREGISTRO.md +161/-0;
  blob de App.cpp IDENTICO (4f0c2363) al de master: herencia
  estructural de anclajes confirmada.
- Metricas del doc: 7561 B / 161 l / CR=0 / NA=0 / sha256 823cdf5a...
  EXACTAS.
- Anatomia del bloque (App.cpp en 4c1cdf0): S1 570..631 (62: comentario
  570-574 + giroInterpGrid def 575), S2 646..705 (60: comentario
  646-649 + def 650), S3 707..807 (101: comentario 707-713 + def 714,
  lambda medOf 726-735); 62+60+101 = 223. Blanks 569/632/645/706/808:
  unico blank entre vecinos, exacto. HelpMarker 633..644 INTACTO entre
  S1 y S2 (comentario 633, def 634, cierre 644). Linea 2 de App.cpp =
  #include "Utils/FieldFormat.h": el include nuevo entra como linea 3.
- Grep PRE (git grep -n -w en 4c1cdf0, ambito src+tests), TODO EXACTO:
  giroInterpGrid 11 lineas (def 575; comentarios 373 y 707; usos 2439,
  2545, 2546, 4108; 4 comentarios en HFTraceLayer.h 16/194/394/395);
  radioInterpGrid 6 (def 650; usos 2449, 2547, 4125; 2 comentarios en
  HFTraceLayer.h 16/396); interpLayerProfiles 4 (def 714; uso 2619;
  comentario en VolumeBuildKey.h:41; comentario en
  tests/test_model_foF2.cpp:124). 11/6/4 sin un solo desajuste.
- Pureza: CERO impl-> y CERO App:: en 570..807.
- Dependencias verificadas una a una contra bytes (todas inline/static
  en cabeceras existentes, como decia el 0476): LayerProfile.h
  sanitizeB0:24, sanitizeB1:30, usableFo:43, smoothstep:210, havDeg:220,
  dayOfYear:232, modelFoF2:252, modelHmF2:274; DensityVolume.h
  densityDir:60; GiroHelpers.h giroValueOf:40; RadioPropagationAdapter.h
  stationValue:88; GiroAdapter.h StationSample:28; GridLayer.h
  GridData:7. Nota de errata propia: el 0476 situaba smoothstep en
  HFTraceLayer.h; el sitio correcto es LayerProfile.h:210, como dice
  este preregistro.
- CI: 0 runs en la rama dw.8-idw-extract, igual que en dw.4..dw.7 (los
  runs de la serie solo existen en PR y push a master). El "PR 2/2 y
  push 2/2" del 0500 describe los gates futuros de la ejecucion; no son
  runs existentes. Sin PR de DW.8 abierto (unico abierto: #12
  credits-licencias, ajeno). Gobernanza: publicado antes del PR, sin
  amend ni force-push visibles.

## 3. Defecto D1 (MATERIAL): predicciones de desplazamiento erradas

- Regla del doc (seccion 4): "-63 para todo lo posterior a 632, -61
  adicional para lo posterior a 706". OMITE el tercer retiro (-102 para
  lo posterior a 808) y el +1 del include nuevo (tras linea 2).
- Regla completa: +1 si L>2; -63 si L>632; -61 adicional si L>706;
  -102 adicional si L>808. Neto para los 8 usos (todos L>808): -225.
- Consecuencia: las 8 predicciones congeladas estan desviadas +101 cada
  una (101 = tamano de S3, el termino olvidado):
  doc decia -> correcta: 2439->2315 -> 2214; 2545->2421 -> 2320;
  2546->2422 -> 2321; 4108->3984 -> 3883; 2449->2325 -> 2224;
  2547->2423 -> 2322; 4125->4001 -> 3900; 2619->2495 -> 2394.
- Invariantes que el doc no congela y conviene congelar: HelpMarker
  633..644 -> 571..582; comentario 373 -> 374 (solo +1); include
  "Utils/IdwInterp.h" como nueva linea 3 de App.cpp; comentario 809 ->
  584; definiciones 575/650/714 y comentario 707 migran al header (los
  totales 11/6/4 no cambian porque el header vive en src/).
- Sin correccion, la auditoria del POST daria 8 discrepancias
  observado/prediccion que serian falsas. Es el criterio central del
  preregistro: no admite GO tal cual.

## 4. Defecto D2 (MATERIAL): andamiaje 9-vs-10 includes; H no cuadra

- El esqueleto (seccion 2) enumera 9 includes y deriva S=12 -> H=237,
  pero la justificacion del propio doc dice que Utils/GiroHelpers.h "se
  incluye explicitamente ademas" (giroValueOf, usado en el bloque), y
  el 0500 dice "9 includes directos" y luego enumera 10.
- Verificado contra bytes: giroValueOf (GiroHelpers.h:40) SI se usa en
  el bloque, y NINGUNO de los 9 includes del esqueleto aporta
  GiroHelpers.h transitivamente (GiroAdapter.h solo incluye cabeceras
  std). Con 9 includes el header NO compila.
- Correcto: 10 includes -> S=13 -> H = 223 + 13 + 2 = 238 (los 2 blanks
  separadores quedan ADMITIDOS, como en la serie). IdwInterp.h
  esperado: +238/-0. PR acumulado desde 38ef6e3: 3 ficheros,
  +(161+1+238)/-226 = +400/-226.
- Errata menor en el mismo punto: "stationValue, linea 38" -> es linea
  88 de RadioPropagationAdapter.h.

## 5. Entrega D3: ferry y bundle declarados como entregados, ausentes

- El 0500 seccion 6: ferry to-glm/files/DW.8/ "11 entradas, 11/11 OK" y
  bundle "entregado en upload/ Y en el relay to-glm/files/DW-BUNDLES/".
- Estado real verificado este turno: el relay 128e866 NO tiene
  to-glm/files/DW.8/ (el commit solo anade el 0500) y DW-BUNDLES sigue
  en 7 entradas (dw0, dw2..dw7; sin dw8); upload/ de GLM no trae ni
  ferry ni bundle.
- Precedente de la serie: en DW.6 y DW.7 el ferry y el bundle entraron
  en el relay con la EJECUCION (commits e511d0c y abc7eab), no con el
  preregistro; 02-grep-post y 07-predicciones-post solo pueden existir
  tras ejecutar. El lenguaje en pasado ("entregado", "11/11 OK") es
  sobrante: o se entrega de verdad (bundle del preregistro
  38ef6e3..4c1cdf0 en el relay; grep-pre ya medible) o se declara como
  entrega de la fase de ejecucion, como de facto ocurrio en DW.6/DW.7.

## 6. Dictamen y remedio

- DICTAMEN SOBRE 4c1cdf0 TAL CUAL: NO FAVORABLE. El bloque, la
  anatomia, el grep PRE, la pureza, las dependencias y la cadena estan
  EXACTOS (es la parte dura del preregistro y esta impecable), pero el
  documento congela predicciones erradas (D1) y un andamiaje
  autocontradictorio con H mal derivado (D2), y declara entregas no
  materializadas (D3).
- Remedio (regla 0455, mismo mecanismo que f932292 en DW.7): UN COMMIT
  ADICIONAL de errata en dw.8-idw-extract, sin amend ni force-push, que
  corrija en docs/DW.8-PRERREGISTRO.md:
  1. Seccion 4: regla completa de desplazamiento y las 8 predicciones
     correctas de la tabla del punto 3, mas los invariantes.
  2. Secciones 2-3: 10 includes (Utils/GiroHelpers.h en el esqueleto),
     S=13, H=238, IdwInterp.h +238/-0, PR acumulado +400/-226;
     "stationValue, linea 88".
  3. Seccion 6: ferry y bundle declarados como entregas de la fase de
     ejecucion (o entregados de verdad en el relay).
- Cuando llegue la errata: re-auditoria rapida de este lado (verificar
  el commit de errata contra la tabla de esta acta) y emito el acta de
  conformidad. Con acta favorable, David decide el GO de ejecucion.
  NO recomiendo dar el GO hoy.

## 7. Estado de la cadena (sin cambios)

- C++ master = 38ef6e3; dw.8-idw-extract = 4c1cdf0 (rama conservada);
  web congelada en 9eca362; android aparcada en 59f539b. Ledger sin
  entradas abiertas; 7/7 bundles en el relay; sin gates abiertos.
  Secuencia de aciertos intacta: DW.5 8/8 (+3/3), DW.6 10/10 (+3/3),
  DW.7 4/4 (+3/3). DW.8 sin ejecutar y sin puntuar todavia.

- GLM, lado auditor, 2026-11-25 (Madrid).
