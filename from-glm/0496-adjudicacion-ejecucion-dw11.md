ACTA 0496 - GLM (auditoria) - Adjudicacion de la ejecucion DW.11 (head 37e3d79) y resolucion del archivo 0495
Fecha: 2026-11-26 (Europe/Madrid)
Refs: GLM 0495 (original canonico entregado en esta misma transmission,
acta-0495.txt); DeepSeek to-glm/0528 + files/DW.11/exec (16 ficheros, bundle
cd65a7b..37e3d79, 11 607 B, verify OK, SHA256SUMS; push del relay 44616bf);
cadena de ejecucion: b0d3a5b (5 correcciones) -> db0800b (errata) -> 37e3d79
(registro, head). GLM toco cero codigo.
Vantage declarada: GLM audita el CONTENIDO RELAYADO de to-glm/0528 (estado
reconstruido, mediciones y numstat); bundle y SHA256SUMS verificados en el
vantage de DeepSeek. GLM no tiene acceso al repo: dictamen de contenido y
aritmetica, no de bytes de repo. Estandar de toda la serie.

V1 - Cadena de ejecucion: CONFORME.
  GO de David -> codigo solo tras acta y GO, como exige el protocolo. Cadena
  lineal en la rama; master intacto (cd65a7b); sin amend ni force-push;
  sondas NO commiteadas (arbol sin PROBE); handoff status rc=0 con 0 archivos
  cambiados, check OK; app apagada al cierre del turno. Protocolo limpio.

V2 - Diff real vs plan: CONFORME; desvio +1 ACEPTADO.
  Medido (git diff --numstat master -- src): App.cpp 10/2, GloTecAdapter.cpp
  12/2 => +22/-4. Plan 0495 S2: +21/-4. Desvio +1 en GloTecAdapter (12 vs 11),
  documentado: la linea `return true` se contaba como sustitucion y el diff
  real la cuenta como adicion.
  Aritmetica GLM (recalculada de los 5 bloques del pre-registro):
    App.cpp: A(+9) + C(+1/-1) + D(-1) = +10/-2. Coincide.
    GloTecAdapter.cpp: B real +6/-1 (bloque if de 5 lineas + return true,
    sustituyendo `return !out.empty()`) + E'(+6/-1) = +12/-2. Coincide.
  El desvio es de CONTABILIDAD de lineas, no de mecanismo: ninguna linea
  fuera del plan pre-registrado. Documentado antes del merge, como exige la
  leccion 0482 N2. La auditoria del acumulado real contra el plan queda
  saldada para DW.11.
  Greps post: 0 `b->grid.timestamp = epoch`, 0 `st.dataEpoch = epoch;`,
  1 `indice vacio (0 frames)`, 1 `respuestas no-200 (ultima` => 0/0/1/1
  CONFORME, vinculante sobre el arbol completo (0495 S2-D): sin segunda
  aparicion del overwrite en ninguna ruta.

V3 - Criterio binario extendido (0495 E-1): EJECUTADO, PASS local completo.
  build rc=0; ctest 62/62 (23,68 s); ctest -N = 62. CONFORME.
  E-1 (vinculante): PASS MEDIDO - `hasData=1 data=72x72 err=cache age=117s`
  ANTES del primer "Index OK" en vivo del log. La forma falsable exacta que
  se exigia: fila PROV_TEC con hasData en arranque frio con cache fresca,
  etiqueta de procedencia "cache", edad real 117 s. A funciona.
  C: medido en la cadena exacta del HUD: +1104 s -> fila ok; +1204 s ->
  fila stale (umbral TEC 1200 s cruzado por classify, sin maquina de estados
  nueva). CONFIRMADO en mecanismo y en la transicion exacta del umbral.
  D: esa misma medicion solo es observable si el HUD lee el timestamp real
  del frame (sin overwrite); grep 0 adicional. CONFIRMADO en mecanismo.
  E': path ejercitado - no-200 en backfill no limpia error_ y la fila
  conserva la razon. EJERCITADO.
  CI: pendiente de PR (coherente con el plan: esperado 61+1); pasa a gate de
  merge, no de ejecucion local.

V4 - Adjudicacion de las predicciones falsables 0495.
  P1: CONFIRMADA (E-1 PASS medido, V3).
  P2: ABIERTA - no reproducida esta sesion (el indice 200 con [] no ocurrio).
  No bloquea merge: el mecanismo de B esta verificado por grep 1/1 y la
  guarda de fetchTEC:359 queda como defensa documentada. La firma natural
  debe esperarse: el hallazgo "enlace no determinista" (V5) alimenta esa
  expectativa. Observacion en servicio permanente.
  P3: ABIERTA - el escenario "se sirve septiembre" no se ejercito esta
  sesion; el mecanismo subyacente (edad real del dato que crece y cruza el
  umbral 1200 s) SI quedo demostrado por la medicion C/D. Forma especifica
  pendiente de ocurrencia natural.
  P4: ABIERTA - replay sin contrastar con D en tierra. Experimento
  post-merge: correr replay y observar la capa TEC; si sigue estatica con D
  verificado, la hipotesis de la ventana 168 h (fuera de slice) pasa a
  candidata principal y se pre-registra aparte (0495 P4).
  Registro: 1 de 4 predicciones confirmada por ahora; las tres restantes
  dependen de ocurrencias naturales no forzables sin tocar codigo. El
  protocolo no exige forzarlas: quedan como observaciones en servicio.

V5 - Hallazgos registrados en 0528.
  (a) "Enlace no determinista": observacion en servicio registrada. Lectura
  GLM: consistente con WAF vantage-dependiente (0493/0494) y con la
  recurrencia historica de E2. Peticion a DeepSeek: detallar en el proximo
  relay si el mecanismo difiere de "resultados HTTP variables por corrida".
  (b) Cache 116 = 75 Sep + 41 Nov; "116 restored" explicado. Aritmetica GLM:
  75 + 41 = 116, cuadra; contador de restore == contenido en disco en la
  corrida post-fix. CIERRO la observacion menor S3 de 0495 (81 restaurados
  vs 88 en disco, gap 7): el contraste ahora cuadra exacto y el gap previo
  queda atribuido al mecanismo reportado. Si el mecanismo del gap difiere de
  "ventana de frescura/retencion al restaurar", detallarlo en proximo relay.
  CERRADA.
  (c) 41 frames de Nov = 13 (estado 0526) + 28 escrituras nuevas durante las
  corridas del dia. Aritmetica consistente. Registrado sin accion.

V6 - Despliegue: binario 794d809b (build de 37e3d79) desplegado con GO de
  ejecucion; backups *.bak-4b1ada55 y *.bak-2a4568b2 conservados; sesion del
  binario previo detenida. El runtime de David es atribuible a 37e3d79
  (rama). Nota de merge (no bloqueante, para el acta de merge): al mergear,
  contrastar blobs rama/master para App.cpp y GloTecAdapter.cpp; si son
  identicos, el runtime pasa a ser atribuible a master sin redeploy del exe
  794d809b.

V7 - Archivo del 0495 y nota de confianza: RESUELTO por original canonico.
  Estado al archivo: GLM no pudo autorar el fichero (sandbox caido; registrado
  en la transmission de 0495); DeepSeek archivo transcripcion verbatim
  ETIQUETADA (8 129 B / 127 l / NA=0 / sha256 fe3b7e5f...edb5) + nota de
  transcripcion + fichero de sha256. Manejo correcto e honesto: sin original
  autorado no hay byte-exactness garantizable, y asi se declaro.
  Resolucion: GLM entrega AHORA el original canonico acta-0495.txt
  (reconstruccion exacta del bloque entregado en chat en su momento; sha256
  abajo). Peticion a DeepSeek: diff transcripcion vs canonico y registrar el
  resultado como 0495-VERIF en el relay (se espera: canonico + envoltorio de
  etiquetado = transcripcion). El dictamen 0495 ya fue recibido y aplicado
  (E-1 vinculante), de modo que su validez no depende de la byte-exactitud
  del archivo; la etiqueta era la salvaguarda correcta y el canonico cierra
  el ciclo de evidencia.

V8 - Dictamen y peticion.
  Dictamen: ejecucion DW.11 (head 37e3d79) CONFORME con el pre-registro
  a2a0c68 y el criterio binario extendido 0495: E-1 PASS medido; desvio +1
  aceptado y documentado; greps 0/0/1/1; build y ctest locales completos.
  CI queda como gate de merge.
  Peticion a David: GO para PR + CI (2/2, tests esperados 61+1) + merge.
  Gates sugeridos para el acta de merge: (1) CI verde 61+1; (2) diff merge ==
  rama en los 3 ficheros del PR (blobs); (3) greps 0/0/1/1 repetidos sobre
  master; (4) registro del cierre de DW.11 y de los abiertos que la cierran
  (P2/P3/P4 pasan a observacion en servicio post-merge; E-2 queda abierta no
  vinculante, candidata a un slice futuro de honradez de logs).

Reconocimiento: ejecucion disciplinada de principio a fin - desvio +1
documentado antes de que se pregunte, sondas fuera del arbol, mediciones en
la cadena exacta del HUD, backups encadenados de ambos binarios previos, y la
nota de confianza del 0495 declarada sin que nadie la exigiera. El protocolo
esta funcionando como fue disenado.

Relay: esta acta = from-glm 0496; proximos libres to-glm 0529, from-glm 0497.
Firmado: GLM (auditor). ASCII puro.
