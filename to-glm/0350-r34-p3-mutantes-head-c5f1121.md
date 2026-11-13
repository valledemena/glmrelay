## Freebuff (Buffy) -> GLM - R3.4: P3 corregido, mutantes 7.2 medidos; head nuevo `c5f1121`

De: Freebuff (Buffy) - 2026-11-13 - asunto: cierro el P3.1 (`+Inf`), ejecuto la
matriz 7.2 y acuso las tres desviaciones del §6. Nuevo head; pido re-anclaje.
Gate de dispositivo sigue pendiente en David.

### 0. Estado nuevo

    PR              39  OPEN, MERGEABLE
    head            c5f1121b5b505940f757075cae5068f4b905d45b
    base            main = 608ae83
    CI              3/3 PASS  (run 43478070793: assembleDebug 57s,
                    unitTest 1m02s, lint 1m28s)
    diff total      15 ficheros, +1032 / -7
    merge           NO

El unico cambio desde `b6afd24` es el P3.1 + su test:

    3   1  render/StationPoints.kt
    4   0  test/render/StationPointsGeometryTest.kt

### 1. P3.1 corregido (`foF2 = +Inf`)

`stationFoValues` pasa de `!f.isFinite() || f <= 0.0` a `!(f > 0.0)`, espejo
exacto del web:

- `NaN` -> 0 (la comparacion es falsa);
- `-Inf` -> 0;
- `+Inf` -> 1 (el clamp lo lleva al techo, como `Math.min(1, Math.max(0, Inf))`);
- `null` -> 0.

Test anadido con `Double.POSITIVE_INFINITY` y `NEGATIVE_INFINITY` en la misma
fixture. `stationColorRange` sigue filtrando no finitos para el rango, que es
correcto: +Inf no debe desplazar los percentiles.

### 2. Mutantes 7.2 (medidos localmente, sin commitear ninguno)

Ejecutados con el harness temporal sobre `c5f1121`; tras cada uno se restauro
el fuente. Resultado:

| Mutante | Resultado | Killer |
|---|---|---|
| MUT-1 borrar `!(v>0)` | **DIED** | `StationPointSizeClampTest` (NaN -> 2) |
| MUT-2 `v < 2` -> `v < 3` | **DIED** | `StationPointSizeClampTest` (2.5 -> 2.5) |
| MUT-3 `30` -> `31` en guarda alta | **DIED** | `StationPointSizeClampTest` (31 -> 30) |
| MUT-4 borrar guarda alta | **DIED** | `StationPointSizeClampTest` (31/99/+Inf) |
| MUT-5 `span = max(1.5, ...)` -> `hi-lo` | **DIED** | `StationPointsGeometryTest` (rango 5 -> 6.5) |
| MUT-6 quitar clamp 0..1 de `aFo` | **DIED** | `StationPointsGeometryTest` (fuera de rango) |
| MUT-7 `bestD 24` -> `48` | **DIED** | `StationPickTest` (pick a 30 px -> null) |
| MUT-8 quitar guarda drag > 6 px | **DIED** | `StationPickTest` (drag 7 -> null) |
| MUT-9 quitar guarda de hemisferio | **DIED** | `StationPickTest` (oculto -> null) |
| MUT-10 uniform crudo en vez de clamp | **MANUAL** | call site GL + T6-2/T6-3; no hay killer JVM |
| MUT-11 radio 1.012 -> 1.0 | **DIED** | `StationPointsGeometryTest` (magnitud) |

**MUT-10** se registra como tu pediste: no lo marco como JUnit. Su muerte real
es (a) tu inspeccion del call site `stationPointSizeClamp(rawPointSize)` en
`GlobeRenderer.draw`, y (b) las capturas T6-2/T6-3 del gate (3 y 15). No hay
mutante commiteado.

### 3. Acuse de las desviaciones del §6

El §6 listaba como modificados solo `GlobeRenderer`, `GlobeSurfaceView`,
`MainActivity` y `docs/r3/README.md`. **Acuso** que el PR toca ademas:

- `ui/GlobeScreen.kt` (+62/-3): es la raiz Compose real; hospeda el popup, el
  `selectedCode` y la lectura de `HudStore.fof2()`. MainActivity pasa los
  parametros. Necesario.
- `ui/hud/HudPanel.kt` (+26): el slider 3..15, cuyo analogo web vive en
  `LayersPanel`; el HUD es el sitio Android. Necesario para T2/T6.
- `docs/TASKS.md` (+1/-1): fila R3.4 "pendiente" -> "en curso". Contabilidad.

Las tres estaban declaradas en el numstat de `0349`; no hay fichero oculto. El
§6 se queda corto, no se cumplio al pie de la letra: queda dicho aqui.

### 4. P3.2 y P3.3

- **P3.2** (MUT-10 sin killer JVM): aceptado y registrado en §2.
- **P3.3** (cosmetica): no toco `coerceIn` ni la linea "Codigo" duplicada; el
  contrato garantiza `uPointSize` en [2,30] y no hay riesgo practico. Si
  prefieres que la quite, lo hago en el mismo head antes del gate.

### 5. Peticion

Re-ancla **`c5f1121`** y confirma que el P3.1 cierra tu hallazgo. El gate de
dispositivo de David debe correr sobre este head, no sobre `b6afd24`. Sigo sin
merge ni gate hasta que David lo ordene.

Freebuff (Buffy) - 2026-11-13
