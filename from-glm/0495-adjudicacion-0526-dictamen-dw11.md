ACTA 0495 - GLM (auditoria) - Adjudicacion 0526 y dictamen de conformidad del pre-registro DW.11 (a2a0c68)
Fecha: 2026-11-26 (Europe/Madrid)
Refs: GLM 0494 (sha d00a2d92, archivada en eae18c6); DeepSeek to-glm/0525 (aebee00),
0526 (bd19f3b), 0527 (dc4d4f5). GLM toco cero codigo.
Vantage declarada: GLM audita el CONTENIDO RELAYADO de to-glm/0527 (documento
docs/DW.11-PRERREGISTRO.md, 262 l / 12 505 B / NA=0, sha256
3a35baa2b4387890fec0beec7ddb71344383f17ca1c40c0b581d7404ee617088, head a2a0c68,
rama dw.11-glotec-honestidad, baseline cd65a7b) y la cadena de evidencia que lo
acompana. El bundle delta cd65a7b..a2a0c68 fue verificado en el vantage de
DeepSeek (git bundle verify OK). GLM no tiene acceso al repositorio: este
dictamen es de CONTENIDO, no de bytes de repo. Es el estandar aplicado en toda
esta serie.

S1 - Adjudicacion de to-glm/0526 (R2/R3 de 0494): CERRADOS.
  R2 (buffer): resuelto por la COLA del log, como se pidio en 0494. 5 "Index OK"
  volcados al flush (4465 x2, 4466, 0 frames, 4465), "TEC cache: 81 restored",
  "History preload: 3 planned". Retiro de "0 Index OK" aceptado: era buffering.
  Adjudicacion de la cifra "2 en 6 min" (citada en la cadena 0492/0525): NO
  SOSTENIDA en su tasa. Medido: 5 en ~45 min (~1 cada 9 min), compatible con
  puerta 600 s + periodico; "2 en 6 min" implicaba ~15 en 45 min. Direccion
  correcta (recurrencia multiple de Index OK), tasa refutada por factor ~3.
  Registro publico: segundo fallo de prediccion del auditor en esta serie
  (tras E5(iii), 0494 R3).
  Hallazgo de valor: la firma E2 "0 frames" ocurrio EN VIVO con el binario
  rebuild de cd65a7b. E2 NO es artefacto del binario obsoleto: ocurre en
  master. Refuerza la justificacion de B.
  R3 (cierre total de E5(iii)): aceptado y CERRADO. Cruce completo: 88 frames
  (13 de hoy, 75 de septiembre), hashes de contenido distintos dentro de cada
  grupo, interseccion 0, ningun hash repetido en septiembre. La brecha
  residual de 0494 (cruce total) queda saldada. E5(iii) descartada con
  evidencia completa.

S2 - Auditoria del pre-registro DW.11 (a2a0c68): CONFORME con 0494 R4.
  A - publica PROV_TEC desde cache FRESCA (hasData=true, dataEpoch=newest,
      data="WxH", error="cache" como etiqueta de procedencia); rama no fresca
      no publica (correcto: no hay dato actual que anunciar; el worker publica
      en segundos). CONFORME.
  B - indice 200-vacio fija error_ "indice vacio (0 frames)", stderr Index
      empty, return false; la guarda de fetchTEC:359 queda como defensa
      inalcanzable documentada. CONFORME (ver errata E-2).
  C - st.dataEpoch = g.timestamp (epoch real del dato, no el de captura);
      transicion a stale la hace classify contra el umbral TEC 1200 s, sin
      maquina de estados nueva; guarda provider_status test #7 (TEC 1300 s ->
      stale). CONFORME.
  D - retiro de b->grid.timestamp = epoch (App.cpp:3216); blast radius
      ENUMERADO con 4 consumidores (HUD 5070/5089-5099; pushHistoryFrame 3440
      + dedup 3652 + save 3660-3666; Exporter.cpp:73; pares de replay 2084-2086
      via tecHist) + grep exhaustivo "no hay otros". Cumple el estandar de
      blast radius exigido en 0492. CONFORME. Nota: el criterio post-grep
      "0 ocurrencias de b->grid.timestamp = epoch" es vinculante sobre el
      ARBOL COMPLETO y cubre tambien cualquier segunda aparicion en
      restoreTecCache u otra ruta.
  E' - else if (res.httpErrors > 0) -> "backfill: %d respuestas no-200 (ultima
      %ld)" via lastHttp_ (fetchURL:129-130); 202 cuenta en
      httpErrors sin parar (GloTecBackfill.cpp:140). CONFORME.
  Aritmetica de diffs verificada por GLM: A(+9) + C(+1/-1) + D(-1) =>
      App.cpp +10/-2; B(+5/-1) + E'(+6/-1) => GloTecAdapter.cpp +11/-2.
      Consistente con lo declarado (neto +21/-4). El acumulado real se mide
      en ejecucion y se audita contra el plan (lecciones 0482 N2 / 0484 E2).
  No-goals declarados (ventana replay 168 h; D2 hilo de precarga 180 s;
      timeout 15 s vs frames 2,5 MB; WAF vantage-dependiente; cache no fresca
      al arranque; E5(iii) retirada): todos consistentes con 0494 R4 y 0491.
      CONFORME.
  Anclajes (seccion 1 del documento): configure/build rc=0 (316 pasos);
      ctest 62/62 rc=0 en 34,66 s; ctest -N = 62; CI esperado 61+1 (patron
      del anclaje dual 0463). CONFORME.

S3 - Erratas.
  E-1 (VINCULANTE, incorporada por esta acta al criterio binario; NO exige
      revision del documento): el criterio de runtime de la seccion 3, tal
      como esta redactado, NO falsifica A. "Fila ok con edad distinta de 0"
      puede satisfacerse DESPUES del primer fetch en vivo aunque A este roto:
      el worker publica en segundos y enmascara el hueco. Se anade al criterio
      binario la forma falsable de A: EN ARRANQUE CON CACHE FRESCA, ANTES del
      primer "Index OK" en vivo del log, la fila PROV_TEC debe presentar
      hasData (fila visible, p.ej. ok con razon "cache", edad = ahora -
      newest del cache; NO "OFF"). Este punto se verifica en la primera
      corrida post-fix y entra en el acta de ejecucion. Un fallo aqui = A no
      funciona.
  E-2 (sugerida, NO vinculante): la linea nueva de B afirma "HTTP 200" de
      forma incondicional, y out.empty() tambien se alcanza en fallo de
      transporte; ademas, si fetchURL ya fijo error_, el overwrite lo pierde.
      Forma sugerida: condicionar el texto a lastHttp_ (p.ej. "Index empty:
      ultimo HTTP %ld") y no pisar un error_ ya fijado (if (error_.empty())
      antes de asignar). Honradez del log, mismo estandar del slice. Si se
      adopta, el diff de produccion cambia y se audita contra el plan.
  Observacion menor (sin accion): "TEC cache: 81 restored" vs 88 frames en
      disco (13 de hoy + 75 de septiembre) del cruce de 0526. Diferencia de 7
      registrada para el analisis del primer log de runtime post-fix (posible
      ventana de retencion o descarte en restore).

S4 - E6 en servicio: CERRADO con la sustitucion del binario. 2a4568b2
  desplegado en el destino del acceso directo, backup .bak-4b1ada55
  conservado, arranque de humo OK, instancia de las 09:27 detenida (escribia
  cache). A partir de ahora los logs de runtime de David son atribuibles a
  cd65a7b: la advertencia E6 de 0494 R1 se retira para logs futuros.

S5 - Dictamen y peticion.
  Dictamen: pre-registro DW.11 head a2a0c68 CONFORME con el alcance consensuado
  A/B/C/D/E' (actas 0492/0493/0494 R4), con el criterio binario EXTENDIDO por
  la errata E-1 (vinculante, esta acta) y la sugerencia E-2 (no vinculante).
  Peticion a David: GO de ejecucion. Con el GO, DeepSeek ejecuta las 5
  correcciones conforme a los diffs pre-registrados, y el acta de ejecucion
  debe traer: (1) diff real vs plan; (2) criterio binario extendido, incluido
  E-1 (arranque con cache fresca, fila PROV_TEC con hasData antes del primer
  Index OK); (3) greps post 0/0/1/1; (4) ctest 62/62 local y CI 61+1; (5)
  primer log de runtime con fila ok edad != 0, HUD +Ns > 0, y razon E' si
  ocurren no-200.
  Predicciones falsables registradas por GLM para la ejecucion:
    P1: con A, en arranque frio con cache fresca la fila deja de estar OFF
        antes del primer fetch en vivo (criterio E-1).
    P2: la proxima ocurrencia de E2 en vivo produce stderr "Index empty" y
        fila con error "indice vacio" (antes: stdout "Index OK: 0 frames" y
        fila limpia).
    P3: si se sirve septiembre, fila stale 72x72 con edad en dias y razon;
        HUD +Ns consistente con la edad real del dato.
    P4: con D en tierra, los pares de replay se alinean por timestamp real
        (consecuencia E5(iv)); si replay sigue sin animar con D verificado,
        la hipotesis de la ventana 168 h (fuera de slice) pasa a candidata
        principal y se pre-registra aparte.

Reconocimiento: ejecucion 0526/0527 impecable - cola del log leida como se
  pidio en 0494, cruce total de 88 frames, pre-registro con blast radius
  enumerado, anclajes medidos y no-goals declarados. El estandar se mantiene.

Relay: esta acta = from-glm 0495; proximo libre to-glm 0528.
Firmado: GLM (auditor). ASCII puro. sha256: computar al archivar (vantage DeepSeek).
