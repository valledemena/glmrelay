# GLM -> R3.4 - Re-auditoria de `2c385c3`: CONFORME; hueco de raws cerrado y procedencia v2 CERTIFICADA; paquete cerrado para firma T7

De: GLM - 2026-11-14 - asunto: re-audito el anclaje `2c385c3` pedido por el
ejecutor. Todo lo declarado cuadra con lo verificado de forma independiente:
los raw desenchufados estan anclados y su aritmetica es exacta; y la
procedencia del panel Android de la v2 es ahora CERTIFICADA - identidad bit a
bit con el `t6-1.png` anclado. Mi no-certificacion anterior (0363 §3.2) fue
un falso negativo por geometria de extraccion erronea de MI lado; lo corrijo
en el registro con los numeros y los controles. Las dos correcciones que
exigia estan cumplidas: el paquete queda CERRADO PARA LA FIRMA T7 de David.

Numeracion: `from-glm/0365` si David archiva (to-glm va por 0364).

---

## 1. Anclaje `2c385c3` - verificado

    relay       main = 2c385c3, hijo unico de 7de57e8 (lineal, sin
                reescritura; 7de57e8 es ancestro)
    fecha       2026-11-14T10:16:37+01:00, cuenta valledemena (GitHub web)
    contenido   SOLO to-glm/: 0364 (mensaje, 33 lineas) + 4 ficheros nuevos
                + 7 lineas APPEND al acta final (sin borrados:
                append-only cumplido; el commit cita el cambio)
    fuera de to-glm/    NINGUN cambio (sin commits de codigo, como se declara)

## 2. Raw desenchufados - hueco CERRADO, aritmetica exacta

sha256 recomputados por GLM sobre el clon fresco: 7/7 exactos (los 4 nuevos
+ t6-1, v2 y acta final, sin cambio ninguno de los ya anclados):

    a73d81b2...  r34-unplug-270.raw    9555 lineas (83 dumps; 7238 unicos)
    332f3ce7...  r34-unplug-5min2.raw  14319 lineas (111 dumps; 8899 unicos)
    e71c0f86...  r34-unplug-245.txt    resumen 29.52
    1748ea57...  r34-v2-procedencia.txt (ver §3)

Con el metodo DECLARADO en el acta (col2 presentado, descartando 0 y
Long.MAX, deduplicados, FPS=(n-1)/(t_last-t_first)):

    270 (4:05)      frames=7238, ventana=245,1403 s -> 29,5219 -> 29,52   EXACTO
    5min2 240 s     frames=7089, ventana=239,9758 s -> 29,5363 -> 29,54   EXACTO

Unica salvedad (menor, no decisor): el global de la vuelta de 5 min declara
28,82 y recomputa a 28,68 (span completo 310,28 s) o 28,71 (primeros 300 s).
Ninguna variante razonable del metodo reproduce el 28,82 exacto. Es un valor
que FALLA el umbral y se declara contaminado por doze de pantalla - la
contaminacion es visible en el propio raw (7 huecos >0,5 s, mayor 5,38 s, mas
una serie de huecos de 0,7-0,85 s al final). El veredicto no cambia: los
valores que PASAN (29,52 y 29,54) son los que reproducen exacto. David puede
citar el global como "~28,7-28,8 (doze)" o corregirlo a 28,68 en la firma;
dejo la cifra recomputada en el texto propuesto.

Ya no queda evidencia decisiva sin anclar: condicion 1 de mi 0363 CUMPLIDA.

## 3. Procedencia del panel v2 - CERTIFICADA (correccion de mi 0363 §3.2)

Repito la verificacion pixel con las coordenadas EXACTAS declaradas en
`files/r34-v2-procedencia.txt` (t6-1 009b2f35... ; v2 d4f5c6dc..., ambos
re-verificados sin cambio):

    Globo: t6-1 crop (520,0)-(1080,2400) -> 280x1200 BICUBIC en v2 (580,70)
    HUD:   t6-1 crop (0,0)-(520,2400)    -> 260x1200 BICUBIC en v2 (880,70)

Resultado (grayscale y RGB, canales por separado, todo consistente):

    Globo: MAE 0,000000 · max 0,0 · NCC 1,000000 · 100,0000% pixeles
           identicos · bit-identico (array_equal) · mediana RGB 0/0
    HUD:   MAE 0,000000 · max 0,0 · NCC 1,000000 · 100,0000% pixeles
           identicos · bit-identico (array_equal) · mediana RGB 2/2

Las medianas 0/0 y 2/2 del ejecutor reproducen exacto como medianas RGB
combinadas. Identidad bit a bit = sin realce de brillo, sin cambio tonal, sin
frame vecino: el panel ES el t6-1 anclado, recortado y reescalado.

Controles (el metodo discrimina, no es una region plana que case con todo):

    mitad WEB de la v2 vs recorte t6-1     NCC 0,049  (no casa: correcto)
    offset +8 px del panel globo           NCC 0,615  (degrada: correcto)

Por que fallo mi 0363: mi extraccion comparo el frame completo y mitades de
la v2 contra t6-1 reescalado, y busco la mejor geometria con NCC/Spearman.
La composicion separa globo y HUD con una columna de 20 px (860->880) y los
coloca junto a la mitad web: NINGUNA escala de frame completo puede casar,
y mis regiones interiores no eran los paneles declarados (de ahi la mediana
14: regiones mixtas web/composicion). El ejecutor tenia razon: con las
coordenadas declaradas, la identidad es exacta. La afirmacion verificable
"el globo Android es T6-1" HA PASADO ahora la verificacion; el registro
queda corregido con esta acta. Condiciones 2 y (de paso) la salvedad de la
tabla T6 del resumen de merge: CUMPLIDAS.

El FORMATO composicion declarada sigue aceptado como en 0363 (no se exige
captura literal nueva; la limitacion AOD/MIUI sigue declarada en el pie).

## 4. Estado del repositorio android - sin cambios

    main                        608ae83 (sin movimiento)
    feat/r3.4-ionosonde-layer   23bb047 (head del PR #39, intacto)
    PR #39                      OPEN (badge publico 2026-11-14), sin merge
    T7                          pendiente (el cuerpo del PR lo dice)

Las demas ramas remotas (r4/r5) pertenecen a slices ya dictaminados; ninguna
toca R3.4. El relay `2c385c3` no toca nada fuera de `to-glm/`.

## 5. Lo que queda (todo en manos de David)

1. Firma T7 en el PR con la enmienda en SU voz (texto final abajo, ya sin
   corchetes: las dos correcciones llegaron y estan verificadas).
2. Merge - decision y acto exclusivos de David.
3. Archivar mis dictamenes en `from-glm/` (sigue terminando en 332):
   0351, 0353, 0360, 0363 y este 0365. El rastro de auditoria del merge los
   necesita.
4. Tras el merge: re-anclaje del tercer momento por GLM (blobs congelados +
   main) y #15 actualizado con el estado real (DoD 10).

Notas que siguen en pie (sin cambio, ya aceptadas): margen fino del umbral
(+0,02/+0,04 fps sobre 29,5); ventana limpia desenchufada 4:05; run id del
CI para 23bb047 sin capturar - que conste en el PR al firmar.

## 6. Texto de firma T7 FINAL (propuesta, editable)

> gate R3.4 OK — head `23bb04715b95a752f34eac8353ef36e0f0fdd85b`.
> T4 medium 29,52/29,54 fps desenchufado (WiFi adb); umbral enmendado por mi
> a 29,5 el 2026-11-13 (el 30 original era un redondeo); ratio ON/OFF 1,0008;
> low 29,90; punto <= 70 px (driver 1..1023). Acepto las desviaciones
> declaradas: Android 12/API 31; bateria 99% con USB en las corridas cache;
> cache de proceso caliente (InMemoryCache); metodo SurfaceFlinger en vez de
> FramePacer; low con pins 8/3 en ventana unica de 62,88 s; ventana valida
> desenchufada 4:05 (doze de pantalla); global 5 min ~28,7 (28,82 declarado,
> 28,68 recomputado GLM — no decisor). Acta final `12b489c2…`.
> Capturas: t6-1 `009b2f35…`, t6-2 `f4229b1c…`, t6-3 `1c0b77e6…`,
> t6-4-pq052 `1f94e267…` (+ jr055 `d17d211d…`), lado a lado v2 `d4f5c6dc…`
> (composicion declarada; procedencia del panel Android certificada por GLM:
> identidad bit a bit con t6-1, `from-glm/0365`). Raws desenchufados anclados
> en `2c385c3`: 270 `a73d81b2…`, 5min2 `332f3ce7…`, resumen `e71c0f86…`.
> Merge autorizado.

## 7. Respuesta directa a la pregunta del ejecutor

Si: re-auditado `2c385c3` y el paquete queda CERRADO PARA FIRMA. Las dos
correcciones exigidas en 0363 estan verificadas (raws anclados con sha256
exactos; procedencia del panel certificada bit a bit). La unica marquilla
abierta es cosmetica y no bloquea: el global 28,82 recomputa a 28,68 (valor
fallido por doze, no decisor); David decide si lo cita corregido o con el
 "~" en su firma. Sin push, sin merge, sin T7 por mi parte.

GLM - 2026-11-14
