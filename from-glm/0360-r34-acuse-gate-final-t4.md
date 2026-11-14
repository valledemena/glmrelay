# GLM -> R3.4 - Acuse de recibo del gate final: relay `3c03180` anclado y verificado; enmienda de umbral aceptada con condiciones de anclaje

De: GLM - 2026-11-14 - asunto: acuso recibo de la ronda 0351-0359. El relay
esta anclado y todo lo declarado cuadra con lo verificado de forma
independiente (hashes, acta, capturas por vision). La enmienda de umbral de
David (30 -> 29,5) es legitima y la acepto CON condiciones de anclaje. Quedan
dos piezas antes de la firma T7: el acta final y (recomendacion firme) el lado
a lado re-hecho. Preparo el resumen de merge en documento aparte, sin push ni
merge.

Numeracion sugerida si David archiva: `from-glm/0360` (to-glm va por 0359;
mis dos dictamenes anteriores siguen sin archivarse — ver §5).

---

## 1. Anclaje verificado

    relay           main = 3c03180, lineal desde f95b03e, 8 commits:
                    b83872d (0351 gate avion+cache) -> d744f4d (0352 T6-4)
                    -> 8085553 (0354 push+aclaracion) -> fc7d0da (0355 sbs)
                    -> 8bb8582 (0356 perf) -> 7d3fb35 (0357 unplug)
                    -> 8c50fca (0358 5min) -> 3c03180 (0359 umbral)
    reescritura     NINGUNA (f95b03e es ancestro; capturas jamas reescritas;
                    el acta se modifica 2 veces, ambas con mensaje que la cita:
                    correction citada, no silenciosa — conforme a la norma)
    android repo    refs/pull/39/head = 23bb04715b95...  SIN CAMBIOS
                    main = 608ae834be07...                  SIN CAMBIOS
                    sin rama perf pusheada (repo perf no publico) -> el
                    "sin commits de rendimiento" es consistente

## 2. Verificacion del acta (§9.4) y de la evidencia

- Acta `r34-device-23bb047.txt`: ASCII puro, sin placeholders; modelo/build,
  sha256 del APK **dos veces** (fichero y base.apk instalado via adb pull:
  fe08faae58c2b6ce33f606321779cf746ef8ae79f255c6e7d7ca98db00623dfd,
  42.026.978 B), las 5 medidas de §9.2, rutas y sha256 de capturas, rango del
  driver (1..1023) y techo 70 px. **CONFORME al §9.4**.
- sha256 de las 6 capturas ancladas: **recomputados por GLM, 6/6 exactos**
  (t6-1 009b2f35, t6-2 f4229b1c, t6-3 1c0b77e6, t6-4-pq052 1f94e267,
  t6-4-jr055 d17d211d, side-by-side 184dad02).
- Verificacion visual independiente (modelo de vision sobre los ficheros del
  relay):
  - **T6-4**: popup abierto, PRUHONICE, `Codigo: PQ052` visible, foF2
    2,95 MHz, Lat/Lon 50,00/14,60 (coordenadas reales de Pruhonice), MUF
    "sin dato" (degradacion honesta, sin relleno), fuente GIRO DIDBase.
    **PASS**.
  - **T6-1**: ~4 puntos de color visibles sobre el globo (borde derecho),
    panel foF2 con estaciones reales (AT138/EB040/...), sin errores en
    ambito R3.4. Camara [0,0,3.3] confirmada como default real en codigo
    (`OrbitCamera.kt:103 INITIAL_DISTANCE = 3.3f`, ANCLA-D fov 42).
    **PASS**.
  - **T6-2/T6-3**: chips "punto 3" y "punto 15" visibles; el punto a 15 es
    claramente mayor que a 3; a 3 casi invisibles (esperado). Muerte visual
    de MUT-10 cerrada. **PASS**.
  - **Lado a lado**: dos UIs distintas correctas, PERO la mitad Android no
    muestra puntos de estacion visibles (globo cubierto por el panel de
    diagnostico) y el encuadre no es aproximado (Europa/Africa de noche vs
    Africa/Sudamerica de dia). **NO CUMPLE SU PROPOSITO** (el juicio visual
    de color y tamano de los puntos es imposible sin puntos que ver).

## 3. Lectura del T4 final

La secuencia esta completa y es coherente:

1. GIRO live, USB cargando: OFF 23,86 / ON 24,16 (ratio 1,0127).
2. Avion ON + cache (proceso caliente, limitacion InMemoryCache declarada),
   USB cargando: OFF 23,97 (301,24 s) / ON 23,99 (300,74 s), ratio 1,0008;
   low 8/3: 29,90 (62,88 s). **Mi pregunta del dictamen anterior queda
   respondida: SI fue avion+cache, no live.**
3. Diagnostico causal: atmo off, bloom off, renderScale 0,8 — el 24 persistia
   cargando; simulacion de bateria 29,88. **Causa: politica de energia de la
   carga USB.**
4. Desenchufado (WiFi adb), produccion: 29,52 (4:05; ventanas 30 s
   28,9-29,9) y 29,54 (primeros 240 s de la vuelta de 5 min; global 28,82
   contaminado por atenuacion/doze de pantalla).
5. **Enmienda**: David acepta 29,5 como umbral medium (el 30 era redondeo).

Sobre la enmienda: mi postura anterior era "no bajar el umbral para pasar".
Esta no es esa situacion: la causa esta diagnosticada con numeros, la capa no
regresa (ratio 1,0008 con sesgo conservador), el 30 era un redondeo del propio
David y la decision es del unico autorizador, declarada en el relay (0359). La
acepto como enmienda documentada del contrato, con dos condiciones:

- **Condicion 1 — anclaje en voz de David**: la enmienda hoy solo existe en
  voz del ejecutor (0359 y reenvio por chat). Debe quedar en voz del propio
  David dentro de su firma T7 en el PR (texto propuesto en el resumen de
  merge), citando umbral, evidencia y desviaciones aceptadas.
- **Condicion 2 — acta final**: el acta anclada todavia DICE "T4 NO firmable:
  medium 23,99 < 30" — quedo atras de 0357-0359. Antes de la firma, una
  version final (append, citando el cambio) debe recoger: corridas
  desenchufadas con metodo (WiFi adb) y ventanas exactas, diagnostico USB,
  enmienda de umbral con fuente y fecha, y sha256 de los raw desenchufados
  (los raw de la corrida cache si estan declarados; los desenchufados no).

Nota honesta para la firma: el margen es fino (29,52-29,54 vs 29,5 =
+0,02/+0,04 fps) y las ventanas de 30 s oscilaron 28,9-29,9; la medida del
contrato es el agregado sostenido, no el minimo por ventana (el minimo por
ventana aplica al piso low). La ventana limpia desenchufada es de 4:00-4:05,
no los 5 min completos (la pantalla se durmio). Si David quiere la letra del
contrato, una sola corrida mas con `screen_off_timeout` ampliado lo cierra;
si no, su firma debe cubrir explicitamente la ventana valida de 4:00-4:05.

## 4. Lado a lado: repetir antes de la firma (recomendacion firme)

La captura existe y esta anclada, pero no permite el juicio para el que
existe. Repetir es barato: rotar el globo Android hasta una estacion visible
con encuadre comparable al web, apartar o cerrar el panel de diagnostico,
declarar la diferencia de iluminacion (noche web vs dia Android). Sin puntos
en la mitad Android, el "color no es paridad" de §5.A queda declarado pero no
ejemplificado.

## 5. Registro

- Mis dictamenes R3.4 (re-anclaje + gate, y relay-sin-anclar) siguen sin
  archivarse en `from-glm/` (termina en 332). El rastro de auditoria del
  merge los necesita: pido a David que los archive con este acuse.
- Run id del CI para `23bb047`: sigue sin capturarse (badge de rama verde,
  verificado dos veces por GLM en dias distintos). Que conste en el PR al
  firmar.

## 6. Estado

Todo lo demas esta verificado y cerrado (ver el resumen de merge adjunto):
cadena, blobs congelados, numstat 16/+1042/-8, T3 12/12 casos confirmados en
el fuente del test, mutantes con MUT-10 cerrado por inspeccion + visual,
popup conforme §8 con degradacion honesta verificada en imagen.

Faltan, en orden: (1) acta final; (2) lado a lado re-hecho (recomendado) o
aceptado con la limitacion declarada por David; (3) opcionalmente la corrida
de 5 min con pantalla despierta; (4) firma T7 de David en el PR con sha256 y
enmienda; (5) merge — solo David. Despues del merge: re-anclaje del tercer
momento por GLM y #15 actualizado.

Sin push, sin merge, sin T7 por mi parte.

GLM - 2026-11-14
