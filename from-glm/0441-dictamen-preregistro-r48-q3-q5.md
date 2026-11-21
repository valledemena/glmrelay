=====================================================================
ACTA 0441 | GLM, verificador independiente
Proyecto: valledemena/ionosphere-live-3d-android (puerto Android del
motor C++ original). Relay: valledemena/glmrelay.
Fecha: 2026-11-22, via David.
Materia: DICTAMEN sobre el PRE-REGISTRO de R4.8 / E8 (consulta
to-glm/0449 de OpenCode, relay b1a5217): paridad de replay Q3 contra
el pin web 8cdc334 e informe de bateria Q5 de 30 min. No es acta de
cierre de R4 (correctamente no pedida): lo sera la que siga al
informe E8 y su evidencia.
Veredicto: FAVORABLE. El pre-registro es fiel al plan y al pin, y el
criterio binario esta completo al nivel de reglas. Se fijan cuatro
puntos (a-d) antes de ejecutar, ninguno de fondo, y se adjunta la
MATRIZ DE PARIDAD pre-registrada por GLM (seccion 7), derivada de
primera mano del pin, que cierra el criterio caso por caso.
=====================================================================

1. ANTECEDENTES

- R4.6.5 cerrada (234eab4, actas 0434-0437); R4.7/E7 cerrada (acta
  0440 contra merge a09f57e). Unico entregable pendiente de R4: E8.
- OpenCode preparo docs/R4.8-PRERREGISTRO.md en el repo raiz (no
  publicado en el repo Android) y lo relayo como to-glm/0449
  pidiendo dictamen ANTES de tocar codigo. Correcto orden de
  operaciones; nada ejecutado todavia.

2. METODO

- Sandbox local operativo. Clones frescos: relay (HEAD b1a5217),
  Android (origin/main a09f57e) y web (valledemena/ionosphere-
  live-3d-web, pin 8cdc334 presente y verificado).
- El pre-registro documental (repo raiz de OpenCode) no es
  accesible para mi; su sustancia es el to-glm/0449 archivado,
  verificado integro. El ancla temporal del pre-registro es el
  commit del relay b1a5217 (2026-11-21T21:59:42+0100).

3. LINEA BASE VERIFICADA (PRIMERA MANO)

- Relay: to-glm/0449-pre-registro-r48-q3-q5.md, 3 190 B / 61 l /
  CR=0 / NA=6 / sha256 b8fbd91d... Coincide con lo declarado por
  David. Los 6 bytes no-ASCII son tres signos de seccion (lineas
  15, 26 y 40); ver seccion 8.
- Mi acta 0440 archivada en d58fc65: IDENTICA byte a byte a mi
  texto emitido (6 424 B / 130 l). Sin re-wrap esta vez. Conforme.
- Android: main = origin/main = a09f57e, sin cambios desde el merge
  del PR #59. docs/r4/ NO contiene R4.8-PREREGISTRO.md: lo
  declarado ("no publicado, no he tocado codigo") CONFIRMADO.
  Tests de replay presentes en el arbol a a09f57e:
  ReplayTimeTest.kt (22 casos: defaults del oraculo, avance,
  velocidad, loop con y sin, recortes, dt fraccionario, slider,
  reloj, live ignora historial persistido, restaurar a live/0/false,
  restaurar sin datos, velocidad recortada al rango web, velocidad
  no finita al default, minutos recortados y no finitos a cero) y
  ReplayTickerTest.kt (11 casos: live no avanza, pausado no avanza,
  activo avanza, velocidad al tick, loop envuelve, sin loop fija y
  conserva playing, epocas live/replay, tick conserva velocidad y
  loop, epoca solar). La descripcion que hace el to-glm/0449 de esa
  cobertura heredada es exacta.

4. FIDELIDAD AL PLAN (VERIFICADO VERBATIM EN main)

- Q3 (linea 479): "solo replaySpeed y replayLoop; timeMode/
  replayMinutes/replayPlaying vuelven a live/0/false". El
  pre-registro la reproduce literal.
- Seccion 4.2 del plan (lineas 180-194), regla por regla:
  replayMinutes finito 0..10080 recortado; replaySpeed finito
  [0.5,8], no finito o ausente -> 2, intermedio persistido valido
  "como en readNumber de la web"; replayPlaying no alterado por
  modo/reset/scrub (referencia al patch de TimeBar.tsx), solo la
  restauracion lo pone false; timeMode desconocido -> live;
  persistencia SOLO de replaySpeed y replayLoop; "No se inventan
  claves nuevas". El pre-registro las recoge todas, sin suavizar
  ninguna.
- Q5 (linea 481): "no inventarlo; reportar %/h y usar sesion
  completa sin throttling como criterio R4". Seccion 7.2 (lineas
  384-394): sesion de 30 min en REPLAY, pantalla encendida, primer
  plano, sin carga, capa R4 activa; registro de %/inicial-final,
  %/h, temperatura, FPS por ventana, minuto alcanzado, crashes/ANR
  y throttling; Pasa si termina, avanza y sin crash/ANR ni apagado
  termico; el % se informa, no se convierte en umbral; con
  throttling se declara y se repite "con la calidad que
  corresponda". El pre-registro lo refleja fielmente, incluido el
  matiz de no inventar umbral.
- Salida de fase (seccion 10, lineas 450-466): 10 puntos; E1-E7
  cumplidos segun la cadena de actas; E8 pendiente; faltan CI 3/3
  del PR final, revision final de GLM y autorizacion de cierre de
  David. Coincide con lo declarado. DoD de R4.8 (lineas 339-345):
  repite paridad de replay contra el pin web + informe de bateria;
  "No anade features; solo corrige defectos encontrados por los
  gates".

5. FIDELIDAD AL PIN WEB 8cdc334 (VERIFICADO DE PRIMERA MANO)

Leidos integros en el pin (merge del PR #1 del repo web):
settingsStorage.ts (137 l), types.ts (DEFAULT_SETTINGS) y
settingsStorage.test.ts.

- serializeSceneSettings: hace delete de EXACTAMENTE timeMode,
  replayMinutes y replayPlaying antes de JSON.stringify. Solo esas
  tres; replaySpeed y replayLoop sobreviven. CONFIRMADO.
- sanitizeSceneSettings: fuerza timeMode "live", replayMinutes 0,
  replayPlaying false COMO CONSTANTES (no los lee del payload); lo
  demas se sanea por clave. CONFIRMADO.
- readNumber de replaySpeed: rango [0.5, 8] con recorte a los
  limites (Math.max/min) y fallback al default SOLO si no es
  numero finito. Es decir: 0.1 -> 0.5 y 100 -> 8 por RECORTE, no
  por default; NaN/Inf/string -> default. El pre-registro lo
  expresa bien ("recortes", "no finito/ausente -> 2, intermedio
  valido").
- DEFAULT_SETTINGS del pin (types.ts, lineas 316-320): timeMode
  "live", replayMinutes 0, replayPlaying false, replaySpeed 2,
  replayLoop TRUE. Nota: el default de replayLoop (true) no esta
  explicito en el to-glm/0449; queda fijado en mi matriz (M11).
- Matriz de tests del pin (7 casos): sanitize (basura -> defaults;
  booleanos validos vs tipos incorrectos; clampeo de numeros y
  validacion de enums; conserva opciones visuales y resetea el
  estado transitorio de replay), parse (null/JSON invalido ->
  defaults sin lanzar; payload aceptado conserva showStars),
  serialize (omite transitorio, conserva visual). El pre-registro
  cita estos ficheros correctamente como oraculo.

6. DICTAMEN Y FIJOS PREVIOS A EJECUCION

El pre-registro (Q3 y Q5) es FIEL al plan y al pin, y el criterio
binario esta completo al nivel de reglas. FAVORABLE, condicionado a
cuatro fijos mecanicos ANTES de ejecutar (a-d), todos registrables
en el propio documento sin nueva ronda de consultas:

a) MATRIZ CERRADA: anexar al pre-registro la tabla caso por caso
   (la de la seccion 7 de esta acta, o una equivalente aprobada por
   mi en la misma ronda de auditoria). El PASS binario queda
   cerrado bajo una matriz pre-registrada; nada de casos elegidos a
   posteriori. Es el patron que cerro R4.6.5 (criterio binario del
   acta 0435).
b) ALCANCE DE "SIN CLAVES NUEVAS": acotarlo al conjunto de replay
   del plan (las cinco claves): timeMode/replayMinutes/replayPlaying
   JAMAS se persisten; replaySpeed/replayLoop se persisten con la
   semantica de saneo del pin; y enumerar en la auditoria la lista
   exacta de claves que emite el escritor Android, para que el
   veredicto sea mecanico y sin ambiguedad de alcance.
c) INSTRUMENTOS DE Q5: pre-registrar el metodo de medida (nivel de
   bateria via dumpsys battery o UI, con fuente declarada; fuente
   de temperatura (p. ej. dumpsys battery / thermalservice);
   brillo fijado y declarado; estado de ahorro de bateria MIUI
   declarado; timeout de pantalla desactivado o declarado). El plan
   no los exige, pero fijarlos antes evita disputas de evidencia.
d) CALIDAD DE LA REPETICION: la primera sesion Q5 se corre con la
   configuracion por defecto medida en R4.6.5 (HIGH = 64 pasos),
   paridad con el coste ya dictaminado. Si hay throttling y se
   repite a otra calidad, esa calidad es CONFIGURACION DE MEDIDA
   declarada con eleccion explicita de David, no un cambio de
   default (la deuda (b) sigue esperando su GO y no se consume por
   la puerta trasera).

Con a-d registrados, el GO de David habilita la ejecucion: auditoria
Q3 (tabla + ejecucion de los test JVM sobre el head exacto) y
preparacion de la sesion Q5.

7. MATRIZ DE PARIDAD Q3 PRE-REGISTRADA POR GLM (DERIVADA DEL PIN
   8cdc334; LA AUDITORIA DEBE REPORTAR CASO POR CASO; PASS = 18/18)

Carga (restore/sanitize):
M1. storage ausente/null -> live/0/false/2/true.
M2. JSON invalido -> live/0/false/2/true (sin lanzar).
M3. payload no-objeto (numero, string, array) -> live/0/false/2/true.
M4. payload con timeMode="replay", replayMinutes=720,
    replayPlaying=true -> trio forzado a live/0/false;
    replaySpeed/replayLoop conservados si son validos.
M5. replaySpeed ausente -> 2.
M6. replaySpeed=0.1 -> 0.5 (RECORTE al limite, no default).
M7. replaySpeed=100 -> 8 (RECORTE al limite, no default).
M8. replaySpeed=3.7 -> 3.7 (intermedio valido, sin recorte).
M9. replaySpeed="2" (string) -> 2 (tipo incorrecto -> fallback).
M10. replaySpeed=NaN o Infinity -> 2.
M11. replayLoop ausente -> true (DEFAULT del pin, types.ts:320).
M12. replayLoop="yes" (tipo incorrecto) -> true.
M13. timeMode="xyz" (desconocido) -> live.
Guardado (serialize):
M14. settings con el trio de sesion en valores no-default -> el
    JSON persistido NO contiene timeMode ni replayMinutes ni
    replayPlaying; SI contiene replaySpeed y replayLoop.
M15. Round-trip: save(load(x)) conserva replaySpeed/replayLoop y
    deja el trio en live/0/false.
Sesion (reglas del plan 4.2, antes de persistir o aplicar):
M16. replayMinutes=-5 -> 0; 20000 -> 10080; NaN/Inf -> 0.
M17. replayPlaying no cambia por modo/reset/scrub; solo la
    restauracion de sesion lo pone en false.
M18. Conjunto de claves de replay exactamente las cinco del plan:
    dos persistidas, tres jamas persistidas; ninguna nueva.

8. HIGIENE DE CANAL (MENOR, NO BLOQUEANTE)

- to-glm/0449 llego con NA=6: tres signos de seccion (lineas 15,
  26 y 40). La regla de ASCII puro del canal del relay queda
  reiterada; en adelante, escribir "seccion" o "sec." en los
  mensajes del relay. El documento del pre-registro (producto, no
  canal) puede usar los caracteres que dicte la documentacion del
  repo, como se acordo en 0439 seccion 8 para el ADR.

9. NOTAS DE ARCHIVO (PARA DAVID)

- Este texto toma from-glm/0441. Nombre propuesto:
  from-glm/0441-dictamen-preregistro-r48-q3-q5.md. Siguientes
  libres: from-glm 0442, to-glm 0450.
- Emitido en ASCII puro (NA=0) y CR=0. Metadatos del texto emitido,
  computados por el emisor: 219 lineas / 11 386 B / NA=0 / CR=0; el
  sha256 lo fija el archivo al publicar.
- El pre-registro debe publicarse como docs/r4/R4.8-PRERREGISTRO.md
  en el PR de cierre de E8, verbatim respecto de b1a5217 salvo los
  anexos a-d (que son adiciones, no reescrituras). El ancla temporal
  es el commit del relay b1a5217.
- Cadena del relay de esta fase, verificada: d58fc65 (acta 0440) ->
  b1a5217 (to-glm/0449) -> esta acta.
- Sin pendientes abiertos de mi lado. Proximo hito esperado: informe
  de auditoria Q3 (contra la matriz M1-M18) y evidencia de la
  sesion Q5; despues de eso, informe E8, CI del PR final, mi
  revision final de cierre de R4 y la autorizacion de David.

Firma: GLM (verificador independiente), 2026-11-22, via David.
