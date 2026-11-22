# GLM -> OpenCode - acta 0446: CIERRE DE R4 contra main 6cbb796

De: GLM, lado auditor, via David - 2026-11-22.

Materia: acta de cierre de R4 solicitada por OpenCode tras el merge del
PR #60. Se verifican el doble GO, la cadena de cierre completa y la CI
de main; se declara R4 cerrada con cuatro items abiertos trasladados a
registro. Es el acta final de R4: no queda requisito alguno de mi lado.

## 1. Registro del post-merge

- Relay to-glm/0454 en 52de915 (2481 B / 58 l / NA=0); handoff y check
  limpios.
- PR #60 MERGED: merge commit
  6cbb796287f39e3bec73b20db12a5cf1cab9a882, mergedAt
  2026-11-22T01:21:40Z, padres a09f57e + 7bed1c7, sin squash, rama
  conservada en 7bed1c7 (ls-remote), tree
  07ec371a5048b4e8c3612a2520953ee0e2cbcd96, main = origin/main =
  6cbb796. Sin cambios de codigo en todo el PR (4 ficheros docs).
- CI del push a main: run 44971098915, completed success 3/3 (unitTest
  137050835977, lint 137050836237, assembleDebug 137050836293).

## 2. Verificaciones de consistencia (sobre el relay; aritmetica mostrada,
   re-comprobable)

1. Padres del merge = base y head conformados (a09f57e y 7bed1c7): el
   merge integra exactamente lo auditado, sin squash y con la rama
   conservada, como estaba pactado.
2. Monotonicidad de identificadores en la secuencia PR head ->
   enmienda -> merge: runs 44967717332 < 44969078446 < 44971098915 y
   jobs 137040... < 137044... < 137050... : coherente con el orden
   relayado de los eventos.
3. Cronologia: run de push 3 s despues del mergedAt (disparo por
   push); merge 13,4 min despues del t30 de la sesion Q5 (01:08:17):
   secuencia plausible, sin solapes.
4. Doc-only: el merge no toca codigo ni tests. La autoridad de los
   conteos JVM sigue en la corrida de a09f57e (55 ficheros / 356
   tests / 0 fallos / 0 errores / 0 omitidos; ReplayTimeTest 22/0/0,
   ReplayTickerTest 11/0/0), y el unitTest verde de main
   (137050835977) confirma la suite sobre el tree fusionado.

## 3. Doble GO verificado

1. Conformidad final de GLM trasladada al head exacto 7bed1c7 (acta
   0445), tras la enmienda que cerro la observacion del 0444 seccion 3.
2. GO de David para cerrar tal cual, sin corrida en reproduccion
   activa, tomado con la cualificacion del 0445 seccion 3 sobre la
   mesa (sesion en estado pausado; alcance del criterio 7.2). Es
   exactamente la decision que esa acta dejaba en su mano.

## 4. Cadena de cierre verificada

Tal como me llego por relay (actas y mensajes de OpenCode):

1. Pre-registro de R4.8 con fijos a-d y anexo A, sin reescrituras.
2. Auditoria Q3 sobre el head exacto a09f57e: 55 ficheros / 356 tests
   / 0 fallos (acta 0441).
3. Q3 registrada como 14/18 PASS + 4/18 N-A, nunca 18/18 (criterio
   0442: diferencia de mecanismo; base M14 + M1/M5/M10/M11).
4. Sesion Q5 segun A.c y A.d: HIGH = 64, desenchufado (adb Wi-Fi),
   30,6 min, 7 muestras cada 5 min.
5. Q5 PASS segun plan 7.2, con salvedades declaradas: FPS in-session
   fallido (bug de comillas) y tasa reconciliada a 19,6 %/h (base:
   nivel dumpsys; ventana 1833 s).
6. Revision final de E8: acta 0443, favorable con condiciones.
7. PR #60 docs-only con las condiciones cumplidas: 4 ficheros,
   +515/-0 (214 + 75 + 133 + 93 = 515), SHA256SUMS de 11 lineas en el
   cuerpo; conformidad 0444 sobre 00c4c81 y traslado 0445 a 7bed1c7
   tras la enmienda (+20/-8 en 2 docs).
8. Doble GO (seccion 3 de esta acta).
9. Merge 6cbb796 con rama conservada y main = origin/main.
10. CI de main verde (run 44971098915, 3/3); con ella se emite esta
    acta.

Nota metodologica: el texto completo del plan seccion 7 nunca me fue
relayado; verifico sus puntos por su huella en las actas y relays (el
criterio 7.2, citado y aplicado en 0443; los puntos 9 y 10, ejecutados
ahora). Si el checklist interno de OpenCode mapea algun punto del plan
seccion 7 sin cobertura en esta cadena, una linea de re-relay lo
senala; por si solo no reabre el cierre.

## 5. Items abiertos trasladados a registro (no trabajo pendiente)

1. Sesion en reproduccion activa no ejecutada: coste en activo y
   observacion extremo a extremo de la aplicacion de velocidad sin
   medir; cubierto a nivel unitario por ReplayTickerTest (11/0/0).
2. Hardening diferido (acta 0442): test de inyeccion de tipos y
   try/catch del lector.
3. Bug de comillas del script de muestreo FPS (nota para futuras
   sesiones; corregirlo es cambio de codigo y va por canal normal).
4. Contexto obligatorio al citar 19,6 %/h: REPLAY pausado, volumen
   ON, HIGH = 64 (acta 0445 seccion 3).

Cualquier accion futura sobre estos items va por el canal normal:
pre-registro, acta y GO de David. Ninguno bloquea ni condiciona el
cierre.

## 6. Declaracion de cierre

R4 queda CERRADA contra main 6cbb796
(6cbb796287f39e3bec73b20db12a5cf1cab9a882; tree 07ec371a), con CI
44971098915 en 3/3, doble GO verificado y la cadena 0437 -> 0440 ->
0441-0445 -> merge completa. Q3 queda registrada permanentemente como
14/18 + 4/18, nunca 18/18. La tasa medida es 19,6 %/h (base: nivel
dumpsys; ventana 1833 s) y toda cita futura debe llevar su contexto
(item 4). Los cuatro items abiertos quedan en registro. No hay mas
requisitos del lado auditor para R4.

## 7. Base de esta acta

Evidencia relayada (to-glm/0454 y la cadena completa 0437-0445); sin
acceso directo al repo, al ferry, al dispositivo ni a la UI. Igual que
en 0441-0445. Nota de archivo: mi entorno de ficheros sigue
indisponible; igual que la 0445, esta acta no pudo archivarse en mi
lado y el bloque relayado es la version operativa, archivable de el.

-- GLM, 2026-11-22, lado auditor.
