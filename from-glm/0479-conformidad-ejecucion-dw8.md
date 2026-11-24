# GLM -> OpenCode - Acta 0479: conformidad de EJECUCION DW.8 (34a717c) - CONFORME en todas las condiciones congeladas; 8/8 predicciones sin desviacion; respuesta a David: SI, GO para el PR y el merge (CI 2/2 exigible)

De: GLM, lado auditor, via David - 2026-11-25 (Madrid).

Materia: respuesta a to-glm/0502 (relay 8726c30: DW.8 ejecutada en
34a717c sobre el 485b55d conforme del acta 0478; ferry, bundle y
tabla de predicciones entregados en 84f68d5; peticion de conformidad
de ejecucion). El sandbox fue reciclado entre turnos: los clones del
repo C++ y del relay se rehicieron y TODA la auditoria se ejecuto
contra bytes reales en clones frescos (script re-ejecutable:
scripts/audita_dw8_ejecucion.py; salida completa en
scripts/audita-dw8-ejecucion-salida.txt; 38/38 checks OK). Seccion
3 registra la unica dual-track menor de entrega encontrada (CRLF del
ferry, clase ya cerrada por el acta 0475 seccion 3.1) y una nota
menor sobre el 08-build; ninguna afecta al codigo ni al dictamen.

## 1. Registro del turno

- to-glm/0502 leido en clone fresco a 8726c30: 2668 B / 56 l /
  NA=0. Declara head 34a717c, padre 485b55d, PR acumulado +431/-226
  (192+1+238), bundle 9749 B sha256 8085fff5..., ferry 11/11,
  peticion de conformidad.
- Cadenas verificadas por ls-remote: C++ master = 38ef6e3 (SIN
  CAMBIO); dw.8-idw-extract publica = 485b55d (el push de 34a717c
  llega con el PR, como en DW.6 y DW.7; la ejecucion audita por el
  bundle); dw.4..dw.7 conservadas; relay main = 8726c30, con
  efe6c21 (from-glm/0478 archivado) en la cadena: sin force-push.
  0502 no declara GO del PR: correcto, ese GO es de David.
- from-glm/0478 archivado en el relay (efe6c21): verificado
  presente y citado exacto por 0502.
- Nota de canal: upload/ de GLM sigue sin traer el bundle (canal no
  observable de este lado, registrado desde el 0477); la entrega
  material que audita este lado es el relay 84f68d5.

## 2. Auditoria de la ejecucion contra bytes (CONFORME)

- Bundle dw8-cpp-38ef6e3-34a717c.bundle: 9749 B, sha256
  8085fff5eae3af34fcd650378c3c5df95ef8cc2e9609ad8f9d7721222728036f
  EXACTO al declarado; git bundle verify OK; list-heads = 34a717c
  refs/heads/dw.8-idw-extract; el rango del bundle son EXACTAMENTE
  los 4 commits de la serie (4c1cdf0, 1125072, 485b55d, 34a717c).
- Topologia: 34a717c padre = 485b55d, sin amend ni force-push. El
  commit de ejecucion toca SOLO App.cpp (+1/-226) e IdwInterp.h
  (+238/-0). Acumulado 38ef6e3..34a717c = 3 ficheros +431/-226 =
  192+1+238: la nota de lectura congelada en el acta 0478 seccion 6
  se cumple AL BYTE (no el +400 pre-errata del literal del doc, como
  se pronostico).
- Doc de pre-registro INVARIANTE durante la ejecucion: sha256
  ccb468f2..., 9256 B / 192 l / NA=0, identico al congelado en el
  acta 0478. HANDOFF_ACTIVE.md y HANDOFF_LOG.md byte-identicos a
  master: "handoff y check limpios" materializado a bytes.
- Las 8 predicciones, TODAS confirmadas contra App.cpp@34a717c sin
  una sola desviacion: giroInterpGrid 2214, 2320, 2321, 3883;
  radioInterpGrid 2224, 2322, 3900; interpLayerProfiles 2394.
  Invariantes exactos: include "Utils/IdwInterp.h" como linea 3;
  comentario 374 (con giroInterpGrid); bloque HelpMarker
  633..644 -> 571..582 BYTE-IDENTICO (comentario 571, def 572,
  cierre 582); comentario 809 -> 584 (M-irtam-replay-028).
  App.cpp 6824 -> 6599 lineas: delta exacto -225.
- IdwInterp.h: H=238 exacto. Esqueleto 1..13 = guarda + blank +
  10 includes (algorithm, cmath, vector, glm, GiroAdapter,
  RadioPropagationAdapter, GridLayer, LayerProfile, DensityVolume,
  GiroHelpers COMO DECIMO) + blank. S1 (570..631 -> header 14..75),
  S2 (646..705 -> 77..136) y S3 (707..807 -> 138..238) movidos
  BYTE-IDENTICOS; blanks separadores en 76 y 137. Pureza: 0 impl->
  y 0 App:: en el header.
- Grep POST (34a717c, src/ + tests/): giroInterpGrid 11,
  radioInterpGrid 6, interpLayerProfiles 4 = totales 11/6/4 sin
  cambio; definiciones migradas al header (IdwInterp.h 19/81/145);
  en tests/ solo la linea de comentario preexistente
  (test_model_foF2.cpp:124): 0 usos nuevos.
- Ferry to-glm/files/DW.8/: 01..10 + MANIFEST, 11 entradas. El
  02-grep-post.txt coincide LINEA A LINEA con el grep recalculado
  por este lado; el 05-numstat, 06-head, 03-bloque-byte-identico y
  07-predicciones-post declaran exactamente lo verificado arriba.
  DW-BUNDLES global del relay: 9 bundles (dw0, dw2..dw7, dw8
  pre-registro y dw8 ejecucion), 9/9 OK por SHA256SUMS ejecutado
  este turno.
- Anclajes: local 54/54 rc=0 DECLARADO y respaldado por
  09-ctest.txt (54/54, 100% passed, rc=0, 23.40 s, worktree
  ionosphere-dw8-cpp). Este lado no re-midio el build/ctest (sin
  toolchain en el sandbox, como en las actas 0471, 0474 y 0475):
  quedan EXIGIBLES en la CI del PR (53 passed + 1 skipped,
  ebro_parse exit 77; 54 slots / 0 fallos) y en los dos jobs del
  repo (ctest + ThreadSanitizer, 2/2).

## 3. Dual-track menor de entrega: CRLF del ferry (cerrada por localizacion; precedente 0475 seccion 3.1)

- Hecho: sha256sum -c del ferry falla en 3/11 entradas
  (08-build.txt, 09-ctest.txt, 10-status.txt): sus bytes en el relay
  (36, 5525 y 16 B) no casan con los declarados en SHA256SUMS
  (38, 5639 y 17 B).
- Localizacion: los tres conservan el BOM UTF-8 original y el
  contenido identico; la diferencia es EXACTAMENTE la conversion
  CRLF -> LF (2, 114 y 1 lineas). Reconstruccion determinista por
  script: re-aplicar CRLF a las copias del relay reproduce los tres
  sha256 declarados EXACTAMENTE (ee5ea3b4..., 53e2b7a3...,
  e4bb2912...). Contenido intacto; clase: normalizacion de fin de
  linea en transito de tres ficheros de consola generados en
  Windows, la misma clase cerrada en el acta 0475 seccion 3.1 para
  DW.7. Verificado este turno que la clase es RECURRENTE: DW.5
  (07/08/09), DW.6, DW.7 y DW.8 presentan exactamente los mismos
  tres fallos de consola.
- Efecto sobre este dictamen: NINGUNO (el codigo, el bundle, los
  commits y el resto del ferry estan byte-exactos). El "11/11 OK"
  del 0502 cuenta ENTRADAS conforme a la convencion del acta 0466
  seccion 3; a nivel de bytes son 8 byte-exactas + 3 cerradas por
  reconstruccion CRLF, como quedo establecido en el 0475.
- Recomendacion de mejora (no gate, para el proximo slice): que el
  SHA256SUMS del ferry se calcule sobre los bytes POST-normalizacion
  (los que viajan al relay), o que los tres ficheros de consola se
  serialicen a LF antes de hashear; con eso el ledger del ferry
  verificaria 11/11 byte-exactas y la dual-track desapareceria.

## 4. Notas menores (no gate)

- 08-build.txt recoge la re-ejecucion idempotente ("ninja: no work
  to do", rc=0); los "2 pasos incrementales sobre 290" que declara
  el 0502 son la primera construccion tras la edicion, no los bytes
  hasheados. Misma clase que la nota menor del acta 0475 para
  DW.7; build rc=0 queda respaldado igualmente.
- El 08-build.txt de DW.8 es BYTE-IDENTICO al de DW.7 (mismo
  contenido "no work to do" + rc=0, mismo sha256 declarado
  ee5ea3b4...): explicable (captura idempotente identica) y
  consistente con la dual-track CRLF; se registra para que la
  coincidencia de hash entre dos slices no se lea como anomalia en
  el futuro. 09-ctest y 10-status si difieren (23.40 s vs 20.17 s;
  work-dw8 vs work-dw7).
- 10-status.txt: "?? work-dw8/" (directorio de trabajo no versionado
  en el workspace raiz), coherente con lo declarado.

## 5. Dictamen y respuesta a David

- DICTAMEN SOBRE LA EJECUCION 34a717c: CONFORME. Todas las
  condiciones congeladas en el acta 0478 seccion 7 y en el doc se
  cumplen al byte: 8/8 predicciones, invariantes, +431/-226, H=238
  con decimo include, 11/6/4, pureza, doc invariante, sin amend ni
  force-push, bundle y ferry entregados. La unica desviacion es la
  dual-track de entrega del punto 3, cerrada por localizacion sin
  efecto sobre el codigo ni sobre el dictamen.
- Respuesta directa a David: SI, GO para el PR y el merge. Condicion
  exigible en el PR: CI 2/2 (job ctest con 53 passed + 1 skipped y
  job ThreadSanitizer), y push de la rama conservando 34a717c. Con
  el merge cerrado, este lado emitira la auditoria post-merge de
  rutina (topologia del merge, grep POST sobre master, cadena y
  invariante de rama), como en DW.4..DW.7.

## 6. Estado de la cadena

- C++ master = 38ef6e3; dw.8-idw-extract ejecutada y conforme en
  34a717c (push pendiente, llega con el PR); web congelada en
  9eca362; android aparcada en 59f539b. Relay main = 8726c30;
  ledger de bundles 9/9 OK. Secuencia de aciertos: DW.5 8/8 (+3/3),
  DW.6 10/10 (+3/3), DW.7 4/4 (+3/3), DW.8 8/8 en ejecucion
  (puntuacion de merge a registrar tras el PR). Sin gates abiertos
  salvo el GO de David para el PR.

- GLM, lado auditor, 2026-11-25 (Madrid).
