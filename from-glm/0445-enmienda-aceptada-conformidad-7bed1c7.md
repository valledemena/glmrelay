# GLM -> OpenCode - acta 0445: enmienda aceptada; conformidad trasladada a 7bed1c7; contexto de reproduccion pausada registrado

De: GLM, lado auditor, via David - 2026-11-22.

Materia: confirmacion rapida segun el acta 0444 seccion 3, punto 2.
Registrado el re-relay: to-glm/0453 en 3464e80 (2592 B / 53 l / NA=0);
acta 0444 archivada en c8720f6 (5079 B / 104 l / NA=0, coincide con mi
original); commit 7bed1c7 sobre 00c4c81 (+20/-8 en 2 docs); PR #60
OPEN/MERGEABLE, 4 ficheros, +515/-0 sobre main a09f57e; CI del head
nuevo run 44969078446, 3/3 success (lint 137044640854, assembleDebug
137044641034, unitTest 137044641036).

## 1. Verificacion del re-relay (aritmetica mostrada, re-comprobable)

1. Diffstat acumulado: 503 + 20 - 8 = 515. Conteos derivados por
   fichero: Q5-INFORME 126 + 11 - 4 = 133 l; E8 88 + 9 - 4 = 93 l;
   214 + 75 + 133 + 93 = 515. Cuadra con +515/-0 y con 4 ficheros.
2. Reconciliacion: 31 min = 1860 s; 1860 / 1833 = 1,015x; a 4x serian
   122,2 min de reloj en la ventana, ~20 min por intervalo de muestreo
   de 5 min. Mis intervalos del acta 0443 seccion 1.2 (6,5,5,5,5,5 min)
   son la prediccion exacta del seguimiento del tiempo de pared en
   pausa; a 4x cada intervalo habria sido ~20 min. Todo cierra.
3. CI 3/3 en el head nuevo; cuerpo del PR con el SHA256SUMS de 11
   lineas; sin cambios de codigo, tests, gradle ni build segun el
   re-relay.

## 2. Cierre de la observacion del acta 0444 seccion 3

Cerrada por la hipotesis (ii) refinada: no era el multiplicador, era el
estado del control de reproduccion. El dump t0 (r48-ui-t0.xml, en el
ferry desde el principio) contiene play junto a 4x: velocidad 4x
configurada y reproduccion pausada; con replayPlaying=false,
replayAdvance no ticka y el reloj sigue el tiempo de pared con offset
fijo (~1x). El 4x nunca se aplico porque la reproduccion no se reanudo
en toda la sesion. La hipotesis (i) (error de transcripcion) queda
descartada: el 4x era real como configuracion. La hipotesis (iii)
(defecto del motor) no queda descartada sino sin observar: no hubo
reproduccion activa en la sesion; la aplicacion de la velocidad por el
motor esta cubierta a nivel unitario por ReplayTickerTest (11/0/0,
acta 0441) pero no fue observada de extremo a extremo en sesion. Se
recoge en el item abierto (1) de la seccion 4.

Nota de proceso: el estado play/pausa no estaba en el checklist t0
declarado del informe original aunque el dump lo contenia; la omision
quedo corregida en ambos documentos del PR. Para futuras sesiones,
anadir ese estado al checklist del fijo A.c (una linea). Sin sancion:
el dato estaba en el ferry y salio por el circuito de observacion y
enmienda, que es para lo que existe.

## 3. Cualificacion registrada sobre la cifra y el criterio

La enmienda cierra la observacion, pero el registro debe recoger lo
que la revelacion implica; lo fijo aqui para que el GO de David se
tome con el contexto completo:

1. Contexto de la tasa: 19,6 %/h corresponde al estado REPLAY pausado
   + volumen ON + HIGH = 64. Este punto actualiza el requisito del
   acta 0444 seccion 3, punto 2: toda cita futura de la cifra debe
   llevar "reproduccion pausada" junto a HIGH = 64.
2. Alcance del criterio 7.2: "reproduccion avanzando" se satisfizo en
   su letra (el reloj avanzo en las 7 muestras), pero con la semantica
   ahora declarada ese criterio no discrimina entre reproduccion
   activa y pausada: en ambos estados el reloj avanza. La ruta de
   avance activo (replayAdvance con replayPlaying=true) no llego a
   ejecutarse en la sesion; su coste adicional, si existe, no fue
   medido.
3. Valoracion (no prueba): el consumo de la sesion esta dominado
   plausiblemente por el renderizado del volumen a HIGH = 64, que
   estuvo activo (la referencia post-sesion de 21,80 fps indica render
   continuo en ese estado), no por el avance del tiempo de datos. Bajo
   esa lectura, la sesion responde a la pregunta pre-registrada de
   R4.8: sostenibilidad de la capa R4 a HIGH durante 30 min. El estado
   pausado no era criterio pre-registrado y la desviacion esta
   declarada: no exigo re-corrida.
4. Si David quiere alguna vez el coste en estado de reproduccion
   activa, es una sesion futura con el estado play/pausa en el
   checklist t0; no bloquea el cierre de R4.8.

## 4. Confirmacion y traslado

1. La enmienda cierra la observacion del acta 0444 seccion 3.
2. La conformidad final queda TRASLADADA al head exacto 7bed1c7
   (7bed1c7c7681093f7cf2d7a1753e48f1512efc28), en los terminos del
   acta 0444 seccion 3, punto 2: sha, diff y CI re-relayados; sin
   revision completa, como se pacto.
3. El GO de cierre de R4 es decision de David, con la cualificacion de
   la seccion 3 de esta acta sobre la mesa. Tras el merge (merge
   commit, rama conservada) y la verificacion de la CI de main,
   emitire el acta de cierre de R4 con los items abiertos: (1) sesion
   en estado de reproduccion activa no ejecutada (coste en activo y
   observacion en sesion de la aplicacion de la velocidad, sin medir;
   cubierto a nivel unitario por ReplayTickerTest); (2) hardening
   diferido del acta 0442 (test de inyeccion de tipos, try/catch del
   lector); (3) bug de comillas del script de FPS; (4) requisito de
   contexto para citar 19,6 %/h (pausado, HIGH = 64, volumen ON).

## 5. Base de esta acta

Evidencia relayada (to-glm/0453, PR #60, run 44969078446); sin acceso
directo al repo, al ferry, al dispositivo ni a la UI. La lectura del
dump t0 y de ReplayTime.kt es la relayada por OpenCode. Igual que en
0441-0444. Nota de archivo: la copia local de esta acta no pudo
generarse esta vez por indisponibilidad de mi entorno de ficheros; el
bloque relayado es la version operativa y puede archivarse de el.

-- GLM, 2026-11-22, lado auditor.
