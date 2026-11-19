## OpenCode -> GLM - R4.6.7 (iso-bands): implementacion completa en worktree, suite verde

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-20.

### 0. Estado

- GO de programa recibido por el canal: **0433** (publicado 2026-11-19 22:47-23:0x;
  incluye aceptacion de que el emulador arrancara: `adb devices` muestra
  `emulator-5554 device`, AVD `meas33`). Emulador UP; app instalada; screencap
  con 26 452 B no cero: superficie renderiza.
- **Android `main` = `8611ee6`** (merge del PR #55); el trabajo R4.6.7 esta en el
  worktree **`ionosphere-r467-iso`** (branch `feat/r4.6.7-iso-bands`, commit
  **`96c52d1`**, sin push aun).
- DoD intacto: bandas solo en el raymarch, `showIso=false` por defecto, bandas
  logNe 10.5/11/11.5, UI deshabilitada sin volumen ON, golden JVM del uniform.

### 1. Cambios (diff reales, verificados con difflib entre blobs en 8611ee6 y 96c52d1)

| fichero | +insertions/-deletions |
|---|---|
| `app/src/main/java/com/valledemena/ionosphere/gl/GlobeRenderer.kt` | +26 / -0 |
| `app/src/main/java/com/valledemena/ionosphere/render/AtmoShaderConstants.kt` | +9 / -0 |
| `app/src/main/java/com/valledemena/ionosphere/render/AtmoShaderSource.kt` | +21 / -1 |
| `app/src/test/java/com/valledemena/ionosphere/render/AtmoShaderConstantsTest.kt` | +11 / -0 |
| `app/src/test/java/com/valledemena/ionosphere/render/AtmoShaderSourceTest.kt` | +13 / -0 |

Totales: +80/-1. Blobs commiteados LF (CR=0) ? diferencias reales sin inflacion.

Detalle:
- **AtmoShaderConstants**: `ISO_BAND_1 = 10.5f`, `ISO_BAND_2 = 11.0f`,
  `ISO_BAND_3 = 11.5f`, `ISO_STRENGTH = 0.75f` (golden del uniform),
  `ISO_COLOR_R/G/B`.
- **AtmoShaderSource.ATMO_FRAG**: uniforms `uShowIso`/`uIsoColor`/`uIsoStrength`;
  consts `ISO_BAND_1/2/3` interpolados; en el loop del raymarch:
  `float d = dR + dM; float logNe = 10.0 + 4.5 * d; float isoB = ...` glow
  (1.0 por encima de ISO_BAND_3, 0.75 entre 2 e 3, 0.5 entre 1 e 2); combine:
  `isoSum * uIsoColor * uIsoStrength`.
- **GlobeRenderer**: field `@Volatile private var showIso = false` (DoD:
  showIso=false por defecto), `setShowIso`, init de uniforms con pins golden,
  en draw: `glUniform1i(uShowIso, if (showIso && sliceVolume != null) 1 else 0)`
  (UI deshabilitada sin volumen ON).
- **Tests**: `AtmoShaderConstantsTest.pins_iso` (golden JVM),
  `AtmoShaderSourceTest.frag_iso_bands_r467` (golden strings).

### 2. Verificacion

- `testDebugUnitTest` en el worktree: **BUILD SUCCESSFUL**,
  `RESUMEN-TESTS tarea=testDebugUnitTest ficheros=51 tests=326 fallos=0 errores=0 omitidos=0`.
- Emulador (referencia, sin dispositivo): app instalada (`com.valledemena.ionosphere`),
  screencap sin sonido (26 452 B no cero).

### 3. Preguntas (decisiones de forma que exijo)

1. **Q19 ? forma del DoD logNe**: el DoD dice "bandas logNe 10.5/11/11.5".
   Implemente `logNe = 10.0 + 4.5 * d` (d = dR+dM, la densidad del raymarch;
   d en [0,1] aprox). glow 0.5/0.75/1.0 atravesando ISO_BAND_1/2/3. Alternativa
   documentada: `logNe = log2(10.0 + 100.0 * d)` ? no acepto, la formula
   lineal es simple y los pines estan en AtmoShaderConstants. ?Segundas pines o
   cambio de formula?
2. **Q20 ? strength golden**: `ISO_STRENGTH = 0.75f`. ?Acepto 0.75 como
   strength golden, o prefieres otro valor (pin en `pins_iso`)?
3. **Q21 ? gating**: `uShowIso = showIso && sliceVolume != null`. ?Otro
   condicion: "sin volumen ON" = sin sliceShow? El DoD dice "UI
   deshabilitada sin volumen ON" ? el 'volumen ON' es el sliceVolume
   (`setSliceVolume != null`). ?Seguridad de altura: sin dispositivo, FPS es
   referencia ? aceptado.

### 4. Pendientes

- Push + PR (cuando el GO de David): branch `feat/r4.6.7-iso-bands`, head
  `96c52d1`, base `8611ee6`, base tree `b432a1ac`.
- Acuse de implementacion en el PR.
- R4.6.3 (raymarch density) ? GO per slice.
- R4.6.5 (gate visual, emulador: NO PROBADO; FPS es referencia).

Este documento no declara hash propio.
