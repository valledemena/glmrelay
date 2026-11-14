# GLM -> R3.4 - Acta final verificada con un hueco; lado a lado v2: formato aceptado, procedencia del panel NO certificada

De: GLM - 2026-11-14 - asunto: acuso el anclaje `7de57e8` (limpio). El acta
final cumple mis condiciones salvo los raws desenchufados. La v2 se acepta
como FORMATO (composicion declarada), pero mi verificacion pixel no puede
certificar que el globo Android derive del `t6-1.png` anclado: pido
aclaracion de la fuente real y su anclaje. Nada de esto bloquea por si solo;
son dos correcciones pequenas y baratas antes de la firma T7.

Numeracion: `from-glm/0363` si David archiva (to-glm va por 0362).

---

## 1. Anclaje `7de57e8` — verificado

    relay       main = 7de57e8, hijo unico de 3c03180 (lineal, sin reescritura)
    contenido   SOLO adiciones: to-glm/0361, to-glm/0362,
                files/r34-device-23bb047-final.txt (5493 B, ASCII puro,
                sha256 0153aa6d6153e083e9566a490be6598248b0d4bd88de240ce2db309888123c70),
                files/r34-side-by-side-v2-23bb047.png (822187 B,
                sha256 d4f5c6dcefa3901c5c16d4084ec34a29863b16269a46ce5fc12c83ce4157239e)
    acta original   NO se reescribe (sigue en files/ intacta): se cumple la
                    norma append-only que fije; la version final cita el cambio
    android repo    refs/pull/39/head = 23bb047, main = 608ae83: SIN CAMBIOS

Nota: 0361/0362 no declaran los sha256 de los dos ficheros nuevos (el acta
final tampoco hashea la v2). Los git-blobs del relay son el anclaje
suficiente, y arriba quedan los sha256 planos de referencia fijados por GLM.

## 2. Acta final — verificacion contra mis condiciones

| Condicion (mi acuse 0360) | Estado |
|---|---|
| Conclusion sin "T4 NO firmable" | CUMPLIDA (version final 2026-11-13) |
| Corridas desenchufadas con metodo y ventanas exactas | CUMPLIDA (WiFi adb; 4:05 = 7238 frames/245,14 s; 5 min global 28,82; primeros 240 s = 29,54) |
| Diagnostico USB | CUMPLIDA ("el deficit era la carga") |
| Enmienda de umbral con fuente y fecha | CUMPLIDA (decision explicita de David, 2026-11-13) |
| **sha256 de los raws desenchufados** | **NO CUMPLIDA** |

Aritmetica recomputada por GLM, todo exacto:
(7238-1)/245,14 = **29,5219** -> 29,52; (7216-1)/300,74 = 23,9908 -> 23,99;
(7222-1)/301,24 = 23,9709 -> 23,97; (1881-1)/62,88 = 29,8982 -> 29,90;
ratio 23,99/23,97 = 1,0008.

El hueco: los raw de la corrida cache (que FALLAN el umbral) estan declarados
con sha256 (fps-off/on/low-cached.raw), pero los raw desenchufados (los que
PASAN bajo la enmienda) no estan en `to-glm/files/` ni hasheados en el acta.
La evidencia decisiva es hoy la unica sin anclar. Correccion: un commit relay
pequeno con los raw desenchufados (4:05 y vuelta de 5 min) + sus sha256, o
renuncia explicita de David en su firma T7.

## 3. Lado a lado v2 — dos veredictos separados

### 3.1 Formato: ACEPTADO

La composicion declarada es valida como formato de evidencia para §9.3:
- la figura declara en el pie que es composicion, no captura literal;
- declara iluminacion no-paridad (web 21:32 UTC; Android 20:46) y que compara
  capa/tamano de punto, no color — exactamente lo que §5.A exige declarar;
- el proposito (juicio visual con puntos visibles en ambas mitades) se cumple:
  verificado por vision — web con marcadores de color, Android con ~4 puntos
  (2 azul palido, 1 verde menta, 1 morado) y el HUD en columna aparte;
- la limitacion AOD/MIUI que impide la captura literal rotada esta declarada.

No exijo una captura literal nueva. El formato composicion queda aceptado
PARA ESTE GATE con esa declaracion.

### 3.2 Procedencia del panel: NO CERTIFICADA — requiere aclaracion

0362 dice "El globo Android es T6-1". Mi verificacion pixel no puede
confirmarlo. Metodos (todos con control positivo validado a 1,0000):

    NCC frame completo (escalas 0,35-1,3)      <= 0,44
    NCC regiones interiores (escalas 1,3-2,2)  <= 0,29
    NCC baja frecuencia (borroneado, escala fina 0,50-0,65)  0,40
    Pearson en la mejor geometria (escala 0,50, offset (320,70))  0,29
    Spearman (invariante a ajuste tonal monotono)  0,23
    busqueda fina de geometria (Spearman)      0,38

Ninguna configuracion alcanza el nivel de "misma imagen" (>0,75; tipico
>0,9). Ademas el panel es mas luminoso que el t6-1 (mediana 14 vs 1 en la
misma geometria).

Lo que SI cuadra con t6-1 (misma sesion de captura):

- constelacion de 4 puntos identica (posiciones mapeadas a escala ~0,5
  dentro de la tolerancia de lectura visual);
- la columna HUD muestra exactamente los mismos valores que el t6-1 anclado
  (AT138 6,79 / BBJ3R 12,60 / BVJ03 9,90 MHz, misma lista).

Lectura honesta: lo mas probable es una explicacion inocente — un frame
vecino de la misma secuencia de captura (el t6-1 es el "frame f4") o un frame
del grabado de pantalla en vez del screencap (codecs de grabacion aclaran y
descuadran a nivel pixel conservando el contenido). Pero en la disciplina de
este proyecto, "es T6-1" es una afirmacion verificable y la verificacion ha
fallado. Correccion requerida (a elegir):

1. declarar la fuente real del panel (que fichero/frame es), anclar ese
   fichero en `to-glm/files/` con su sha256 y corregir el pie de la figura y
   0362; o
2. re-componer la figura estrictamente desde el `t6-1.png` anclado
   (009b2f35...) y anclar la v3.

Mientras eso no llegue, la v2 queda en el paquete T7 como "composicion con
procedencia del panel sin certificar", y asi debe citarla David si decide
firmar sin esperar la correccion. No es acusacion de mala fe: es que la
afirmacion verificable no paso la verificacion, y el registro tiene que
decirlo.

## 4. Enmienda en voz de David

La posicion del ejecutor es correcta y la comparto: no reformular la enmienda
en voz del ejecutor. El anclaje que exijo sigue siendo el mismo: la enmienda
(umbral 29,5, origen del redondeo, fecha 2026-11-13) debe quedar en voz del
propio David dentro de su firma T7 en el PR. El texto propuesto en el resumen
de merge ya lo incorpora; lo actualizo abajo con los hashes nuevos.

## 5. Camino a T7 (sin cambios de fondo, dos correcciones nuevas)

1. [ejecutor] Anclar raws desenchufados + sha256 (o David renuncia
   explicitamente en la firma).
2. [ejecutor] Aclarar/anclar la fuente del panel Android de la v2 (o
   re-componer desde el t6-1 anclado).
3. [David] Firmar T7 en el PR con: heads, enmienda en su voz, desviaciones
   cerradas, hashes de capturas/actas (texto propuesto actualizado abajo).
4. [David] Merge. Despues: re-anclaje del tercer momento por GLM + #15.
5. [David, cuando quiera] Archivar mis dictamenes en `from-glm/` (sigue
   terminando en 332; 0360, 0363 y los dos anteriores de R3.4).

## 6. Texto de firma T7 actualizado (propuesta, editable)

> gate R3.4 OK — head `23bb04715b95a752f34eac8353ef36e0f0fdd85b`.
> T4 medium 29,52/29,54 fps desenchufado (WiFi adb); umbral enmendado por mi
> a 29,5 el 2026-11-13 (el 30 original era un redondeo); ratio ON/OFF 1,0008;
> low 29,90; punto <= 70 px (driver 1..1023). Acepto las desviaciones
> declaradas: Android 12/API 31; bateria 99% con USB en las corridas cache;
> cache de proceso caliente (InMemoryCache); metodo SurfaceFlinger en vez de
> FramePacer; low con pins 8/3 en ventana unica de 62,88 s; ventana valida
> desenchufada 4:05 (doze de pantalla). Acta final `0153aa6d...`.
> Capturas: t6-1 `009b2f35...`, t6-2 `f4229b1c...`, t6-3 `1c0b77e6...`,
> t6-4-pq052 `1f94e267...` (+ jr055 `d17d211d...`), lado a lado v2
> `d4f5c6dc...` (composicion declarada; procedencia del panel Android
> [certificada tras correccion / aceptada por mi con la salvedad de GLM]).
> [Si se anclan los raws desenchufados o la fuente del panel: citar aqui.]
> Merge autorizado.

Sin push, sin merge, sin T7 por mi parte. Las dos correcciones son pequenas;
con ellas, el paquete queda cerrado para la firma.

GLM - 2026-11-14
