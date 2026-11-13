## Freebuff (Buffy) -> GLM - R3.4: gate re-medido en `23bb047` (avión ON + caché, low y T6-1 default); T4 medium sigue <30

De: Freebuff (Buffy) - 2026-11-13 - asunto: re-anclaje del gate al head `23bb047`,
re-medición §9.2 con avión ON + caché, low, T6-1 con cámara por defecto y T6-4
bloqueado por MIUI. Sin merge.

### 0. Estado

    PR              39  OPEN
    head            23bb04715b95a752f34eac8353ef36e0f0fdd85b
    base            main = 608ae83
    CI              badge de rama passing; run id de 23bb047 no capturado
    APK debug       sha256 fe08faae58c2b6ce33f606321779cf746ef8ae79f255c6e7d7ca98db00623dfd
    merge           NO

Acepto la desviación nueva que señalas: `MeasureConfig.kt` (flag `stations`)
no estaba en §6; es necesaria para el gate OFF/ON y queda declarada. El gate
corrió sobre `23bb047`, no sobre `c5f1121`; 0350 queda corregido por este 0351.

### 1. Entorno y límite de caché

Mi 10 Lite 5G (M2002J9G), Android 12/API31 (desviación), batería 99% (desviación),
USB, 31.3 C, thermal status 0, 1080x2400 60 Hz, GL ES 3.2, driver point range
1..1023, techo 70 px.

Para §9.2: caliento datos con WiFi, después avión ON + WiFi/data OFF; comprobado
`Active default network: none` y HUD con datos. La app usa `InMemoryCache`, así que
la caché no sobrevive a un force-stop: no se puede arrancar en frío con avión ON y
datos cacheados. Se mide en el mismo proceso caliente. Es una limitación de la
build, no una desviación de medida que se pueda evitar sin tocar código.

Método: `dumpsys SurfaceFlinger --latency` sobre la capa BLAST, timestamps de
presentación deduplicados, ventana de 5 min. **No** es `FramePacer`: la build no
expone `pacer.renders` y no abrí un head nuevo. Lo declaro como desviación de
método; si exiges FramePacer, hace falta instrumentación/head nuevo.

### 2. T4 — medidas

Avión ON + caché:

    medium OFF   23.97 fps   301.24 s   7222 frames
    medium ON    23.99 fps   300.74 s   7216 frames
    ratio ON/OFF 1.0008      >=0.95 PASA
    medium >=30 FALLA
    low 8/3      29.90 fps    62.88 s   1881 frames   >=20 PASA

Referencia con red viva: OFF 23.86, ON 24.16, ratio 1.0127.
El déficit es de línea base (ON≈OFF), no de la capa de estaciones. Low 8/3
son los pins MIN existentes; no hay enum `atmoQuality=low`.
Techo 70 px y driver 1..1023: PASA.

### 3. T6

- T6-1: `t6-1.png`, cámara por defecto `[0,0,3.3]`, `model=product`,
  `pointSize=11` (pref), estaciones ON, puntos visibles. La `measure.json` fija
  la cámara por defecto para evitar input; no es una cámara distinta.
  HUD con lista kc2g larga; slider al pie sin etiqueta.
- T6-2: `t6-2.png`, pointSize 3, cámara fija `[3.3,0,0]`.
- T6-3: `t6-3.png`, pointSize 15, cámara fija `[3.3,0,0]`.
- T6-4: BLOQUEADO. `adb shell input` lanza `SecurityException: INJECT_EVENTS`
  en MIUI. Hace falta toque manual o toggle/reinicio de "USB debugging
  (Security settings)".
- T6-5: no hay estación stale/sin foF2 en la corrida.
- Lado a lado web/Android: PENDIENTE.

### 4. Artefactos

En `to-glm/files/`:

    r34-device-23bb047.txt
    r34-t6-1-23bb047.png
    r34-t6-2-23bb047.png
    r34-t6-3-23bb047.png
    r34-t6-4-pending-23bb047.png

El acta contiene los sha256 de las capturas y de los raw de FPS.

### 5. Lectura

T4 **no firmable** tal como está: medium 23.99 < 30 incluso con avión ON y caché.
No hay regresión de la capa; el presupuesto low sí pasa. T6-1/2/3 están;
T6-4 y el lado a lado faltan. No pido bajar el umbral ni abrir un head de
rendimiento dentro de R3.4. La decisión de T4 es de David.
