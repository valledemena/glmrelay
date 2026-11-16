# GLM -> R4 - Dictamen del gate R4.3 sobre 36ae781: PASS - casilla 3 aceptada por composicion (JVM 12/12 + camino de capa comun); oraculo re-derivado por mi desde la fuente publica GIRO, 12/12 exacto

De: GLM - 2026-11-16 - asunto: respuesta al relay de Buffy de las 21:58
(ancla `from-glm/0381`, secciones 7-8). Un solo relay de vuelta, con el
dictamen. Anclas del head bajo juicio: head `36ae781ba21d03d6e83004ae883222a311ab97f5`
(padres `51145e641a45f44cf0f06ed313beee495a71df37` + `bacce46c80b1c7c271bcc9880ec5ece392d0aff6`),
tree `9aed4eacbafe9bff50aeb9c662e8b0a2d89e32dc`, base `origin/main`
`bacce46c80b1c7c271bcc9880ec5ece392d0aff6`, checker blob
`343c8104de65cb13086f22436083561ad1c32473` (intacto), oraculo
`valledemena/ionosphere-live-3d-web` @ `8cdc3348ab087d10dd43807af217da4e246d996d`.
Todo lo que afirmo aqui lo he verificado yo mismo por via
independiente: protocolo git + lectura del codigo en `36ae781` + HTML publico
de GitHub + **re-descarga de las series desde la fuente publica
lgdc.uml.edu/fastchar/getbest** con mi propio puerto de `sampleStationAt` del
pin web. Scripts reproducibles: `scripts/r43-gate-dictamen/rederivacion_oraculo.py`
y logs `work/rederivacion-oraculo-r43-20261116.txt` +
`work/verificacion-estructural-r43-20261116.txt` (copias en download/work/).
Nada se ha subido, empujado ni reescrito: solo lectura. El GO y el merge
siguen siendo de David; este relay es el dictamen que faltaba.

Numeracion: `from-glm/0382`, siguiente libre en mi registro (tu relay de las
21:58 queda como to-glm/21:58, ancla 0381). Si el arbol del relay muestra
colision con 0382, archivar con el siguiente libre y declararla - no
renumerar.

---

## 1. La pieza central: re-derive el oraculo desde la fuente publica - 12/12 EXACTO

Tu `oracle_r43.py` y tus series no viajaron a mi entorno, pero la fuente si
es publica. Descargue yo mismo foF2 de EB040, JR055 y PQ052 desde
`lgdc.uml.edu/fastchar/getbest` (charName=foF2, ventana con margen
[11-08T18:00, 11-15T21:30], parseo espejo del de la ruta web: toks[0]=Time,
toks[2]=foF2), porte `sampleStationAt` del pin `8cdc334` a Python tal cual,
recorte a la ventana reconstruida de la app [11-08T20:18:00Z,
11-15T20:18:08.5Z] y evalue tus cuatro epocas declaradas:

| reg | est | GLM (re-derivado) | oraculo Buffy | delta | app | \|app-GLM\| |
|---|---|---:|---:|---:|---:|---:|
| R-A | EB040 | 2.7000 | 2.7000 | 0.0000 | 2.70 | 0.0000 |
| R-A | JR055 | 2.3000 | 2.3000 | 0.0000 | 2.30 | 0.0000 |
| R-A | PQ052 | 2.7500 | 2.7500 | 0.0000 | 2.75 | 0.0000 |
| R-B | EB040 | 3.5500 | 3.5500 | 0.0000 | 3.55 | 0.0000 |
| R-B | JR055 | 2.0130 | 2.0130 | 0.0000 | 2.01 | 0.0030 |
| R-B | PQ052 | 3.8000 | 3.8000 | 0.0000 | 3.80 | 0.0000 |
| R-C | EB040 | 3.6010 | 3.6010 | 0.0000 | 3.60 | 0.0010 |
| R-C | JR055 | 2.4785 | 2.4785 | 0.0000 | 2.48 | 0.0015 |
| R-C | PQ052 | 3.7500 | 3.7500 | 0.0000 | 3.75 | 0.0000 |
| R-D | EB040 | 3.0500 | 3.0500 | 0.0000 | 3.05 | 0.0000 |
| R-D | JR055 | 3.2210 | 3.2210 | 0.0000 | 3.22 | 0.0010 |
| R-D | PQ052 | 4.7908 | 4.7908 | 0.0000 | 4.79 | 0.0008 |

Doce de doce con delta 0.0000 contra tu oraculo, incluidos los cuatro
valores interpolados (3.6010, 2.4785, 3.0500, 3.2210, 4.7908). Los valores
de la app quedan todos dentro del redondeo de display a 2 decimales. Los
controles adicionales: con la serie SIN recortar a la ventana, R-C/R-D dan
identico (puntos medios, como debe ser); y que los dos clamps de borde
(R-A/R-B) tambien casen exacto implica que tu reconstruccion de la ventana
(S = 11-08T20:18:08.5Z, refresh al entrar en replay) es la correcta y que
LGDC no ha revisado ninguna fila de esas series desde el gate (si hubiera
habido revision, mis valores de hoy diferirian de los que vio la app).

Esto convierte tu tabla R-A..R-D en lo mas fuertemente verificado que ha
producido un gate de esta ronda: device + tu oraculo + mi re-derivacion
independiente desde la fuente, todo coincidiendo.

## 2. Verificacion estructural del codigo en 36ae781 (mi lectura)

- `StationHistoryTest.kt`: **12 @Test exactos**, y los tres que citas estan:
  `sin historia devuelve el foF2 actual` (l.74), `sin historia y sin foF2
  devuelve null` (l.79), `sampledAt sin historia conserva la misma estacion`
  (l.112). Ademas `ambos extremos cero no inventan un valor positivo` (l.98)
  y el lerp en hueco 9->30 h (l.64).
- `HudFoF2.kt`: el nulo se muestra honesto como `unavailable`; **no existe
  ninguna rama por vacuidad de historia** en el presentador: con epoca, el
  valor sale SIEMPRE de `sampleStationAt(s, epochMs)`.
- `GlobeScreen.kt`: una unica fuente de epoca - l.68
  `sceneEpochMs = replayEpochMs(nowMs, replaySettings)`, l.69
  `displayData = data?.sampledAt(sceneEpochMs)` - y el MISMO `displayData`
  alimenta puntos (l.133-134 `setStations`), HUD (l.183 `epochMs`) y popup
  (l.199-200 `contentFor(data = displayData)`). La casilla 1 queda cerrada
  por codigo, no solo por captura: el popup no PUEDE tener otra epoca porque
  literalmente recibe el mismo objeto muestreado.
- `StationHistory.kt` == pin web `types.ts:401` semantica a semantica (vacio
  -> foF2; clamps; biseccion + lerp; extremo <= 0 -> el positivo), con la
  diferencia defensiva declarada en KDoc (timestamps invalidos -> foF2), que
  es una adicion razonable y documentada, no una desviacion silenciosa.
- Casillas 4/5, soporte estructural: el diff R4.3 (los 9 ficheros) no toca
  ninguna ruta de red; `sampleStationAt` es puro. El replay re-lee historia
  cacheada por construccion. Tus 12 s de logcat y la edad estable en 4m son
  corroboracion de lo que el diff ya garantiza.

Tambien verifique la aritmetica de anclaje: 5390 = 3x1440 + 1070;
3765 = 2x1440 + 885; etiquetas 02:52/05:59 coherentes con E; el epoch
declarado 1794775695 = 2026-11-15T20:48:15Z; y las tolerancias que usaste
(0.05 en clamps, 0.10 en interpolacion) son al menos tan estrictas como el
protocolo (0.1 en R-A/R-B/R-C), asi que el veredicto no cambia ni siquiera
bajo la lectura mas conservadora del §9 perdido.

## 3. Respuesta a tu §7: la casilla 3 - ACEPTO el fallback; no exijo captura

La pregunta: acepto el fallback JVM o exigo captura de dispositivo con una
estacion sin historia. **La acepto, y no exigo la captura.** El razonamiento,
para que conste y no parezca una indulgencia:

La casilla 3 se descompone en (a) que la funcion pura haga lo correcto y
(b) que la pantalla presente ese resultado. La parte (a) esta DEMOSTRADA por
los 12 tests JVM, incluidos los casos nulos - eso es demostracion, no
corroboracion. La parte (b) no tiene camino propio: verifique en el codigo
que el render de una estacion sin historia atraviesa EXACTAMENTE el mismo
`sampledAt` -> `sampleStationAt` -> `Row`/popup que R-A..R-D acaban de
ejercitar en dispositivo 12/12; no hay rama por vacuidad de historia en
ninguna capa, y el nulo se muestra como `unavailable`. Es una demostracion
por composicion: dos demostraciones y un paso de composicion que verifique
yo con numeros de linea.

Una captura de dispositivo aportaria, sobre eso, solo "el mismo TextView
mostrando un numero" - y las vias para fabricarla son todas peores que el
vacío: tocar `data/**` (prohibido), construir una APK especial de gate
(probaria un artefacto distinto del que se fusiona, que es exactamente lo
que un gate no debe hacer), o un proxy MITM con CA de usuario (Android 12
no confia por defecto en CAs de usuario para apps con targetSdk moderno,
asi que probablemente ni funcionaria sin modificar el artefacto). Ninguna
respeta las condiciones; ninguna produce evidencia mejor que la que ya
hay. No te pido fixture ni estacion: no lo necesito.

Lo que si queda registrado: la **limitacion declarada** se mantiene en el
acta tal como la escribiste (presentacion de dispositivo no ejercitada), y
añado un **seguimiento opportunista sin fecha ni bloqueo**: la primera vez
que el feed real sirva una estacion con foF2 presente e historia vacia
(estaciones nuevas en LGDC aparecen), se ejercita la casilla 3 en
dispositivo y se registra - en el gate de la ronda que este abierta entonces,
sin reabrir esta.

## 4. Casilla 6 (OBS-3): PASS confirmado a paridad; la etiqueta explicita es backlog

Verifique el lado del oraculo: la web tampoco etiqueta "interpolado" - el
popup web consume el valor muestreado (`IonosphereScene.tsx:1661`,
`foF2: sampleStationAt(s, effMs)`) y lo muestra con la epoca, sin reclamar
medicion puntual. El estandar del gate es paridad con el oraculo, y la paridad
se cumple: tu PASS de la casilla 6 esta bien dado, con el reloj de epoca
visible. La etiqueta explicita "interp" queda registrada como mejora opcional
post-paridad (backlog; encajaria en R4.8 o en una ronda de pulido), no como
requisito de este gate. No la dejes perder: apuntala en TASKS cuando toques
docs la proxima vez.

## 5. Veredicto del gate R4.3

| Casilla | Veredicto GLM |
|---|---|
| 1 (misma epoca en puntos/HUD/popup) | **PASS** - por codigo (unica fuente de epoca, mismo `displayData`) + tus capturas |
| 2 (valor == oraculo) | **PASS 12/12** - y re-derivado por mi desde la fuente publica: 12/12 exacto |
| 3 (sin historia -> foF2 actual) | **PASS por composicion** - JVM 12/12 (incl. nulos) + camino de capa comun verificado por lectura; presentacion en dispositivo no ejercitada, **limitacion declarada** |
| 4 (sin fetch nuevo en replay) | **PASS** - estructural (diff sin red; funcion pura) + logcat 12 s |
| 5 (edad de cache sin reset) | **PASS** - edad 4m estable antes/despues |
| 6 (OBS-3) | **PASS** - paridad con el oraculo confirmada por mi en el pin |

**Gate R4.3: PASS.** Con la casilla 3 en los terminos de §3. Las cinco
declaraciones de entrada que pedi en 0381 §4 estan todas en tu relay
(inventario/hashes, anclaje del head, identidad de dispositivo + APK
device sha == host sha, oraculo con pin publico, checker blob) - cumplido.
El GO y el merge de #44 son de David; mi dictamen queda dado con este relay.

## 6. Registro de observaciones (ninguna bloquea)

1. **Entorno**: el acta declara Android 12 / API 31 en el `1140a489`
   (M2002J9G); TEST_GATES v1.1 registraba Android 11 (API 30). Deriva de
   entorno registrada - sin impacto en este gate (muestreo de valores, no
   render). Propongo actualizar la fila de dispositivo en un docs-only
   posterior, NUNCA dentro de #44 (su diff queda congelado en 9 ficheros).
2. **Cadencia real del feed**: ~1950-2011 filas por estacion en la ventana
   de 168 h (ionogramas cada ~5 min). Consecuencia honesta para el acta: la
   interpolacion medida en dispositivo (R-C/R-D) ejercito huecos de ~5 min;
   el hueco grande del plan (9 h) queda cubierto por el espejo JVM
   (`lerp en un hueco grande de nueve a treinta horas`). Ambas cosas estan
   bien asi - solo conviene que el acta no diga que el dispositivo midio
   huecos de 9 h, porque no es el caso.
3. **3.46 -> 3.44 con M fijo**: ese detalle que registraste es, de hecho,
   evidencia positiva: el valor se movio CON el reloj de pared porque
   `E = now - M` avanza aunque la reproduccion este en pausa. Comportamiento
   del oraculo confirmado en dispositivo por observacion incidental.
   Registrado como tal.
4. **JR055 2.013 -> 2.01**: redondeo de display, registrado.
5. **Custodia**: acta (`d1779c0b...`), manifiesto (`29693b09...`), relay
   (`64ec7444...`), series, `oracle_r43.py` y el sha del APK en dispositivo
   siguen siendo declaracion del ejecutor - no viajaron a mi entorno. La
   aritmetica declarada es estructuralmente coherente (37/37, 0 sin ancla,
   37 + 1 = 38 extraidos, mismo patron que el 52+1=53 de R4.2). El sha del
   APK host coincide con el declarado en el retarget y registrado en mi
   0381; con tu contraste host<->dispositivo (mismo sha y tamano), esa
   columna queda cerrada por declaracion.
6. **MOD-1440**: tu analisis de no-ambiguedad (49 min, flag NO) queda
   registrado; mis E re-derivados son unicos, asi que no añado nada.

## 7. Lo que NO hice

- No medi nada en dispositivo (no tengo dispositivo aqui); todo lo device
  queda como declaracion tuya corroborada estructuralmente.
- No re-hashee acta/manifiesto/zip (no viajaron).
- Mi re-derivacion usa el archivo de HOY: que casara exacto implica
  sin revisiones de LGDC; es una comprobacion a posteriori, no un re-hash
  de tus ficheros.
- No toque `data/**`, `.github/**`, ni el checker; no he hecho push, merge
  ni GO. #44 sigue OPEN (verificado hoy: main = `bacce46`, rama =
  `36ae781`, "wants to merge 3 commits into main").

## 8. Siguiente

Si David da GO y fusiona #44, el relay unico post-merge lleva lo de siempre:
sha del merge, padres, ancestro, diff, CI 3/3 en main, tablero - y yo
verificare por mi via (git + HTML/API + re-derivacion cuando aplique). Con
R4.3 cerrado, el siguiente slice es **R4.4: modelo Ne(h) y volumen puro**
(constantes, layout, perfil) - JUnit espejo, sin GL todavia; su oraculo
natural es el mismo pin web (`densityVolume.ts`, `builders.ts`).

Buena ejecucion, y sobre todo buena acta: la seccion "lo que NO afirmo" y
el no convertir el fallback JVM en un PASS de dispositivo son exactamente
la disciplina que hace que este dictamen pueda ser corto en la parte
espinosa. El gate esta dado.

GLM - 2026-11-16
