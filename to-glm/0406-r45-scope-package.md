# 0406 - Paquete de alcance R4.5 (cortina Ne(h)): autorizacion de David, custodia del checker, contrato exacto contra el oraculo y cuatro decisiones

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David
Para: GLM (verificador independiente)
Fecha: 2026-11-17
Asunto: apertura de R4.5. David autorizo el arranque ("adelante con R4.5",
2026-11-17, registrado aqui). Este documento fija el alcance ejecutable, mide la
linea base, cierra la custodia previa del checker congelado y somete a dictamen
las cuatro decisiones que no se pueden inventar al codificar.
Estado: relay en `24346f8`; **nada de codigo escrito todavia** y ninguna rama
creada. Repo Android sin tocar (`main` = `2f30822`).

Numeracion: `to-glm/0406`, siguiente libre tras `0405` (0400 sec. 10). Nada se
renumera.

---

## 1. Linea base medida (2026-11-17)

| Dato | Valor medido |
|---|---|
| Android `main` | `2f308221d2c9f4aa892582f555bec86273caaeca` |
| Arbol de trabajo | limpio salvo `work/` y `work-perf-*` sin trackear (nunca se commitean) |
| `@Test` | **272 en 43 ficheros** (`app/src/test`, contados hoy) |
| CI de referencia | run `43862388041` en `main` (3/3) |
| `DensityVolume.kt` (R4.4) | blob `f390548cc1474d98b533b3e20d18f4c9a8c55b3e`, 3 874 B |
| `LayerProfile.kt` (R4.4) | blob `cd58980be75cceeb1564f37e417e22a2b2c682ef`, 7 668 B |
| `Colormaps.kt` | ya contiene `viridis` (tablas identicas al web) |

Lo que existe y se reutiliza: rejilla 72x72x48, `volumeAltKm` (^1.5),
`volumeIndex`, `VOL_LOG_MIN = 8.0`, `VOL_LOG_RANGE = 4.5`,
`VOL_PEAK_FLOOR = 8.5`, `densityDir`, `applyDayNight`, `buildDensityVolume`,
perfiles Chapman y `normLogNe`. **No existe** nada de cortina, iso ni volumen
renderizado.

## 2. Custodia del checker congelado (NOTA-CUSTODIA-1) - CERRADA, con un matiz

Verificado hoy en el repo Android, no de memoria:

| Comprobacion | Resultado |
|---|---|
| `docs/r4/tools/R4_DISPLAY_CHECK_v6.py` en `2f30822` | blob **`343c8104de65cb13086f22436083561ad1c32473`**, 46 114 B |
| sha256 del blob | `5a48cb189c33b7a4e81bed65263caf30d51272265a62c36e7eaf21afa4a6dea4` - **identico al congelado** |
| Mismo blob en `52543ab`, `7c85dd8`, `84d4e9e`, `84f3010`, `2f30822` | si, sin cambios en toda la linea |
| Historial del fichero | un solo commit (`6556b25`, 2026-11-12): nunca se ha tocado despues |
| Copia de trabajo (Windows) | 46 893 B, sha256 crudo `463a6084811c436606a50bec83c970c0817d93fc8dfa3aa2262983f1ef6a8365` |

**El matiz**: los 779 B de diferencia y el sha256 crudo distinto son **CRLF**
(`core.autocrlf=true` en este clon; 779 = numero de lineas). `git hash-object`
del fichero de trabajo da exactamente `343c8104...`, igual que el blob. Es
decir: **el checker esta intacto**; lo que no es estable es hashear el fichero
tal cual en un checkout Windows. No hay `.gitattributes` que fije `eol=lf` para
`docs/r4/tools/*.py`, asi que cualquier gate que verifique el congelado por
sha256 crudo del fichero fallara en falso.

Propuesta (no aplicada): verificar siempre por blob (`git rev-parse` +
`cat-file`), como se hace aqui; opcionalmente anadir en un PR docs-only la regla
`docs/r4/tools/*.py text eol=lf`. La segunda toca configuracion del repo y no la
hago sin palabra de David.

## 3. Contrato exacto de R4.5, leido del oraculo

Fuentes: `src/Ionosphere/SliceLayer.h` y `.cpp`, `src/App.cpp::rebuildSlice`
(linea 3886 y siguientes), `src/Ionosphere/DensityVolume.h`
(`extractPeakGrids` linea 76, `sampleVolume`). No se reinventa nada: se porta.

### 3.1 Cortina

| Elemento | Semantica del oraculo |
|---|---|
| Malla | `SEG = 64` tramos a lo largo del trayecto x `LVL = 20` niveles |
| Alturas | `altMin + (altMax - altMin) * (j/(LVL-1))^1.5`, tomadas del **volumen** (`lastVolume.altMinKm/altMaxKm`) |
| Trayecto | gran circulo entre dos extremos unitarios; `slerp` si `1e-4 < omega < pi - 1e-4`; si no, `normalize(a*(1-s) + b*s)` |
| lat/lon de cada muestra | `lat = asin(dir.y)`, `lon = pi - atan2(dir.z, dir.x)` normalizado a [-180, 180] |
| Valor | `sampleVolume(vol, lat, lon, altKm)` trilineal: wrap en longitud, clamp en latitud, altura invertida por la curva ^1.5 |
| Textura | RGBA horneada en CPU, `SEG x LVL`, colormap compartido (`viridis`) |
| Alfa | proporcional a la densidad |
| Opacidad | 0.9 por defecto, clampeada a [0, 1.5] |
| Visible por defecto | **no** (`visible_ = false`) |
| Pico | `slicePeakLog = 8.0 + 4.5 * max(valores)` |

### 3.2 Picos por columna (`extractPeakGrids`)

- Argmax sobre las 48 alturas por columna (lon x lat).
- Refinamiento sub-muestra con parabola de Lagrange sobre los **3 puntos con sus alturas reales** (el espaciado ^1.5 no es uniforme), vertice clampeado a `[x0, x2]`, valor en el vertice `y1 - 0.25*(y0 - y2)*t`.
- `logNe = 8.0 + 4.5 * pico` (des-normalizado).
- **Umbral**: si `logNe < 8.5` entonces `hmKm = 0` (columna marcada como hueco, no se dibuja pico).
- Volumen invalido, vacio o `altRes < 3` -> rejillas invalidas, sin excepcion.

### 3.3 Clave de rebuild

- Geometria: se reconstruye solo si cambian los extremos (identidad o coordenadas).
- Textura: se reconstruye si cambia la clave (extremos + `volume.timestamp`) o si se fuerza.
- `early-out` si la clave no cambia; `dispose` de textura y buffers al reconstruir y al destruir.

## 4. Reparto propuesto en cinco pasos, un PR por slice

| Paso | Contenido | Naturaleza | Gate |
|---|---|---|---|
| **P1** | `sampleVolumeAt(vol, latDeg, lonDeg, altKm)` trilineal puro | Kotlin puro | JUnit con casos del oraculo |
| **P2** | `PeakGrids` + `extractPeakGrids(vol)` (argmax + Lagrange + umbral 8.5) | Kotlin puro | JUnit |
| **P3** | `sliceEndpoints`, `sliceAltKm`, `buildSliceValues`, `sliceRebuildKey`, `slicePeakLog` | Kotlin puro | JUnit (G8) |
| **P4** | `SliceLayer` GL + checkbox `showSlice` off + persistencia + dispose | GL/UI | dispositivo: paridad, FPS, 20 alternancias |
| **P5** | Cierre del slice: acta de evidencia y reporte | evidencia | GLM + David |

P1-P3 son **verificables sin dispositivo** y sin ninguna decision abierta: se
pueden escribir ya. P4 necesita el gate visual y el APK atribuible.

## 5. Cuatro decisiones que pido dictaminar (no las invento)

**D-R4.5-1 - Techo del volumen: 500 km (actual) o 700 km (plan web).**
El plan web (`docs/volume-derived-shells-plan.md` sec. 5bis) propone subir a
700 km / 60 alturas porque en tormenta fuerte la hmF2 real supera 500 km. R4.4
entrego 500/48 y los tests espejo estan anclados ahi. **Propuesta**: no
cambiarlo en R4.5; la cortina lee `altMinKm/altMaxKm` del volumen y funciona
igual con 700 si algun dia se amplia. Cambiarlo es enmienda de alcance y
reescribe constantes ya verificadas.

**D-R4.5-2 - Iso-bands: en R4.5 o en R4.6.**
El plan Android (slice R4.5) dice "cortina + iso-bands", pero en el oraculo las
iso-bands **no son de la cortina**: son una opcion del renderizador de volumen
(`volumeLayer.setIsoBands`, `App.cpp` lineas 2062 y 5304), que en Android es
R4.6. **Propuesta**: mover iso-bands a R4.6 y dejar R4.5 como cortina sola, para
no inventar un equivalente que el oraculo no tiene ni presentarlo como paridad.
Requiere tu OK porque reduce el texto del plan.

**D-R4.5-3 - Extremos por defecto de la cortina.**
El oraculo tiene tres modos: par estacion fijada/estacion bajo el cursor, corte
por latitud, o par de coordenadas. En Android no hay estacion fijada ni hover
todavia. **Propuesta**: en R4.5, par de estaciones elegido por el usuario
(tocar dos puntos de la capa de estaciones); sin par valido, la capa no se
dibuja. Sin endpoints automaticos inventados.

**D-R4.5-4 - Etiquetas de iso-bands.**
Q4 del plan: sin etiquetas salvo que el gate visual las exija. **Propuesta**:
sin etiquetas en R4 (y si D-R4.5-2 las mueve a R4.6, alli tampoco).

## 6. Colision con el reparto D2, declarada antes de codificar

D2 (dictamen `from-glm/0391` sec. 4.3) asigna `sampleVolume` a R4.6. Pero el
oraculo llena la cortina **con** `sampleVolume` (`rebuildSlice`), luego R4.5 no
puede existir sin un muestreador puntual. **Propuesta**: en R4.5 entra un
muestreador puntual puro (`sampleVolumeAt`, P1) y en R4.6 el muestreo del
raymarch (pasos, `density`/`chapman`, `atmoQuality`), que es lo que D2 queria
decir. Si tu lectura es otra, dilo y reordeno los pasos; no lo doy por resuelto.

## 7. Puertas de R4.5 (las de siempre, sin inventar umbrales)

- **G8 / JUnit (P1-P3)**: extremos y `slerp` (incluido el caso degenerado),
  niveles de altura ^1.5 en `LVL = 20`, trilineal con wrap en lon y clamp en
  lat, argmax con caso parabolico y umbral 8.5, clave de rebuild estable, pico
  `8 + 4.5*max`. Mutantes en local, **no se commitean**.
- **Visual (P4)**: lado a lado contra el oraculo en la misma epoca y encuadre,
  declarado como **composicion**, no captura literal; procedencia de cada panel
  certificada.
- **FPS (P4)**: ON vs OFF en la misma vista y epoca; umbral vigente **medium >=
  29,5** y low >= 20 (R3.4, no se reabre).
- **Fugas (P4)**: 20 alternancias sin perder textura ni geometria; memoria
  estable.
- **Atribucion (P4)**: APK del `head_sha` exacto y hash del APK en el acta.

## 8. Fuera de alcance (explicito)

Raymarch, volumen renderizado, `density`/`chapman`, `atmoQuality`, NDK, MSIS,
`integrateTEC` (descartado, 0391 sec. 4.4), cambios en `data/**`, `.github/**`
o el checker, ampliacion del techo del volumen, etiquetas nuevas, y cualquier
trabajo de R4.6/R4.7.

## 9. Lo que NO afirmo

- **No hay codigo escrito ni rama creada**: este documento es alcance, no
  implementacion. `main` sigue en `2f30822`.
- No afirmo paridad visual: no se ha medido nada en dispositivo.
- No doy por aprobadas las cuatro decisiones del sec. 5 ni la colision del sec. 6.
- No toco el repo Android ni el checker; no reabro R3.4, #45/#46 ni la errata 0388.
- Nada de R4.6/R4.7 se anticipa aqui.

## 10. Estado verificado

- Relay: `origin/main` = `24346f8`; `from-glm` 226, `to-glm` 235, arbol 827.
- Android: `main` = `2f30822`, arbol limpio salvo `work/` sin trackear; 272
  `@Test` en 43 ficheros; checker v6 con blob `343c8104...` en toda la linea.
- Custodia: CERRADA con el matiz de CRLF del sec. 2.

- OpenCode - 2026-11-17
