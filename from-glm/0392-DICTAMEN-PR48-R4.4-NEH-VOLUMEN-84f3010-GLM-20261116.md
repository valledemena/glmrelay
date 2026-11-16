# DICTAMEN PR #48 — R4.4 MODELO Ne(h) Y VOLUMEN PURO — GLM 2026-11-16

GLM · 2026-11-16 (CET) · canal: relay David
Objeto: revisión hunk-a-hunk y verificación independiente del PR #48
(`feat/r4.4-neh-volume-pure`, commit único `84f3010`), tras el GO de
implementación de David. La decisión de fusión sigue siendo exclusiva de
David; este dictamen recomienda, no fusiona.

Cadena: PRE-DICTAMEN `47e6024b…` → REGISTRO-ANUNCIO `603b6726…` →
DICTAMEN DE ALCANCE `46820f90…` (D1/D2/D3 + GLOBAL GO CONDICIONAL, C1–C5) →
este dictamen de código.

---

## 0. Veredicto

```text
REVISION DE CODIGO:     CONFORME (sin defectos de espejo ni de contrato)
PARIDAD EJECUTABLE:     531 447 comparaciones, 0 fallos (ver §4)
CUMPLIMIENTO C1-C5:     5/5
RECOMENDACION GLM:      FIRME — apto para fusion
DECISION DE FUSION:     David (pendiente; PR abierto, sin merge)
```

## 1. Topología y alcance del diff (fórmula III)

| Comprobación | Resultado |
|---|---|
| Commit único | `rev-list --count 84d4e9e..84f3010` = **1** ✓ (C1) |
| Padre | `84d4e9edf36f…` = `origin/main` exacto ✓ |
| Autor/fecha | valledemena · 2026-11-16 10:57:25 +0100 · `feat(iono): añade modelo Ne(h) y volumen puro R4.4` |
| Diff | **exactamente 4 ficheros, 851 inserciones, 0 borrados**: `DensityVolume.kt` (124), `LayerProfile.kt` (271), `DensityVolumeTest.kt` (129), `LayerProfileTest.kt` (327) ✓ (C5) |
| Whitelist | solo `core/iono/`; sin `data/**`, `.github/**`, checker, `SolarPosition`, `StationHistory`, UI, GL, manifiestos ✓ |
| Imports de producción | solo `kotlin.math` (PI, cos, cosh, exp, log10, max, min, pow, sin, sqrt) — sin Android, sin GL ✓ |
| Mergeable | base = `84d4e9e` (fast-forward posible) ✓ |

## 2. PR y CI (SHA exacto)

- **PR #48** existe y está **abierto, sin merge**: verificado por la página
  HTML del PR (1 commit, 4 ficheros) y por el endpoint `issues/48` (los PR
  son issues). **Nota de anomalía**: el endpoint `pulls/48` devolvió 404 dos
  veces — inconsistencia de la API anónima (mismo comportamiento intermitente
  ya documentado en el expediente); tres fuentes independientes (HTML,
  issues/48, evento CI `pull_request`) confirman la existencia. Sin impacto.
- **CI 3/3 del SHA exacto** `84f30101b0b6…`: run `43844528842` (#134, evento
  `pull_request`, head_sha = `84f3010…`, conclusión `success`):
  `assembleDebug` ✓ (09:58:07→09:59:14Z), `unitTest` ✓ (09:58:06→09:58:53Z),
  `lint` ✓ (09:58:06→09:59:14Z).
- **Conteo de tests**: `git grep @Test` → **272 en la rama vs 254 en main**
  (41→43 ficheros): +18 exactos, conforme a lo declarado.

## 3. Revisión hunk-a-hunk (contra oráculo `8cdc334`)

**`DensityVolume.kt` — ESPEJO FIEL.** Constantes 72/72/48/60/500/8.0/4.5/8.5
exactas; `DensityVolume` con `DoubleArray`/`IntArray` planos (D3);
`volumeIndex = (a·h+y)·w+x` exacto; `volumeAltKm` con guarda `n<=1` y
exponente 1.5 exacto; `smoothstep` privado idéntico; `densityDir` con
`phi=radians(90−lat)`, `theta=π−radians(lon)` y los tres pines documentados;
`applyDayNight` funcional: no-op por referencia en rejilla de tamaño erróneo
(sin excepción, entrada intacta — `G7_6b` lo pina con `assertSame`),
atenuación `e·NmE`/`e·NmF1`, flags E/F1 apagados solo si `e<=0`, iteración
lat-major con centros de celda exactos, y dirección **inline** como en el
oráculo (que también no llama a `densityDir` aquí).

**`LayerProfile.kt` — ESPEJO FIEL.** `FO_TO_NM=1.24e10`; `blankProfile`
0/110/0/180/0/300/100/3/falsos exacto; `sanitizeB0` con default **100 del
oráculo** (NaN→100, +Inf→300, cubierto en `G7_7`); `sanitizeB1` 3/1.7/4
exacto; `profileFromFo` con `hmF1 = max(150, 0.8·hmF2)` y saneado solo con
F2 válida; `chapmanAlpha` exacto; `f2FloorKm` con el early-out
`NmE <= NeF2(hmE)` y el barrido entero de 1 km sin aproximar; `evalWithFloor`
con las cuatro ramas, la cola Epstein `xmax=1.6`/`1.2` y **la puerta F2
`if (hKm > floor) win = 3`** exacta; `normLogNe` ahora usa
`VOL_LOG_MIN`/`VOL_LOG_RANGE` (fix del mutante m4, valores 8.0/4.5 sin
cambio); `buildDensityVolume` con memoización de suelos por perfil, centros
de celda, `cosChi` vía `densityDir`, mapeo de winner −1→0 / >3→3, inválidos
con arrays del tamaño completo y `valid=false`, `timestamp=0`. La firma
Kotlin (sunDir agrupado, defaults) es la declarada en la propuesta §3.7.

**Tests — 18 nuevos, pines genuinos del oráculo.** `DensityVolumeTest` (7):
G7_1 constantes (incluye 12.5 = LOG_MIN+LOG_RANGE), G7_2 índices en rejilla
**no cuadrada 3×2** con bordes (mata el mutante w/h: (2,1,3)→23 ≠ 22),
G7_3 alturas con pines `61.3655446013`/`486.0324082504` a 1e-9 y malla densa
abajo, G7_4 `densityDir` con los tres pines + norma, G7_5 subsolar/antisolar
con F2 intacto y **entrada sin mutar**, G7_6 terminador `2/27` con
**tolerancia explícita 1e-12** (C2), G7_6b rejilla errónea no-op.
`LayerProfileTest` (11): G7_7 chapman/saneado (NaN/±Inf cubiertos), G7_8
`profileFromFo(4,3,7,300,0,1)` con Nm 1.984/1.116/6.076·10¹¹, hmF1 240,
B0 100, B1 1.7 + variante sin F1, G7_9 suelos **110/−1/167/145/155/136**,
G7_10 continuidad B0±2 ≤ 15 km, G7_11 winners por márgenes (75→D, 110→E,
200/300→F2; noche F2; sin-E; vacío {0,−1}), G7_11b invariante contra un
`evalRefMax` **independiente sin puerta** (transcrito del TU del oráculo,
flare fijo 1, sin gate), G7_12 `normLogNe` con saturación y ±Inf/NaN,
G7_12b builder inválido (12 celdas a cero), G7_12c 3×2×4 válido en rangos,
G7_12d **equivalencia celda a celda contra `evalNeTotal`** (valida la
memoización), G7_12e rejilla completa 248 832 / último índice 248 831.
Los helpers `dayNoF1`/`nightF2`/`evalRefMax` son transliteraciones exactas
de los helpers del TU del oráculo (cotejados línea a línea).

## 4. Paridad ejecutable (verificación GLM adicional, la más fuerte)

Método: (a) harness TS ejecutando el **oráculo web real** extraído de
`8cdc334` bajo node 24 type-stripping (precedente acta R3.1; único cambio
mecánico: sufijo `.ts` en un import de la copia extraída — el diff es esa
línea); (b) transliteración a Python del **Kotlin del commit** (transcrita
del `.kt`, no del oráculo, para que las divergencias de lógica aflorasen;
double IEEE 754 como Kotlin `Double`/JS `Number`); (c) comparador de dos
niveles: estructural exacto (winners, suelos, flags, capas, índices,
tamaños) y numérico a 1e-12 relativo.

Batería: 13 perfiles (los del TU + `profileFromFo` variados) × 20 alturas ×
9 cosChi × 2 flare = **4 680 casos de `evalNeTotal`**; suelos por perfil;
saneado con NaN/±Inf; `applyDayNight` en 10 rejillas × 5 soles (entrada y
salida) + rejilla errónea; **5 volúmenes completos** (3×2×4, 2×2×3, inválido,
**72×72×48 = 248 832 celdas**, y 5×3×6 no cuadrada ejercitando winner F1).

```text
resultado: comparaciones 531 447 · numéricas 517 260 · bit-exactas 516 846
           máxima desviación relativa 5.09e-14 · FALLOS: 0
           winners/floors/layers/flags/índices: EXACTOS en todos los casos
```

**Alcance declarado del método**: la transliteración valida la *lógica* del
Kotlin (estructura, orden de operaciones, guardas, puertas) contra el
oráculo real; la *bit-paridad del JVM* queda certificada por los 18 tests
con pines del oráculo ejecutados en CI (`unitTest` verde). Las ~414
diferencias de último ulp (máx 5.09e-14) son atribuibles a libm vs V8 en la
transliteración Python, muy por debajo de la tolerancia del proyecto (1e-9
relativo para Ne) y sin efecto en winners ni capas.

## 5. Cumplimiento de las condiciones del dictamen de alcance

| Condición | Cumplimiento |
|---|---|
| **C1** single-commit | ✓ `rev-list` = 1 sobre `84d4e9e` |
| **C2** tolerancia 2/27 | ✓ G7_6 con `assertEquals(2.0/27.0, e, 1e-12)` |
| **C3** `integrateTEC` | ✓ no implementado; PR declara descarte documentado y fuera de R4.8 |
| **C4** cuerpo del PR | ✓ 4 hashes del oráculo verbatim, mutantes m1–m7 con tests que los matan, alcance diferido por slice, «sin gate de dispositivo», 254→272 |
| **C5** whitelist 4 ficheros | ✓ diff exacto a los 4 ficheros declarados |

Los 7 mutantes declarados (m1 G7_1, m2 G7_3, m3 G7_2, m4 G7_12, m5 G7_4,
m6 G7_11, m7 G7_7/G7_8) usan los IDs de los tests **reales** del commit (la
numeración se desplazó en uno respecto a la matriz de la propuesta — ver
§6); el mapeo es consistente con los ficheros de test verificados. El fix
del mutante superviviente m4 (`normLogNe` con literales → constantes) está
en el commit y no cambia valores (paridad §4 lo confirma).

## 6. Observaciones menores (no bloqueantes, cosméticas)

1. **Renumeración G7**: los tests del commit usan G7_4=`densityDir` y
   G7_5=`applyDayNight` (la propuesta los llamaba G7.5/G7.6). El contenido
   de la matriz está completo; el PR declara el mapeo correcto. Cosmético.
2. `data class DensityVolume` con `DoubleArray`/`IntArray`: el `equals()`
   generado compara arrays por referencia — irrelevante aquí (los tests
   comprueban campo a campo), pero conviene saberlo si algún día se compara
   volúmenes estructurales. Nota para R4.5.
3. El endpoint `pulls/48` de la API anónima devolvió 404 pese a existir el
   PR (§2) — ya registrado en el expediente como intermitencia conocida.
4. La celda de `applyDayNight` recalcula `phi` por fila y la dirección por
   celda, como el oráculo; sin coste relevante en JVM y fiel al espejo.

## 7. Higiene del turno

`git fetch` + `show`/`grep`/`rev-list` read-only sobre el clon android;
endpoints individuales api.github.com (`issues/48`, `runs/43844528842`,
`runs/…/jobs`) y HTML del PR; harness de paridad en
`scripts/r44-paridad/` (oráculo extraído a copia local con un único retoque
de import declarado; transliteración Python del `.kt`; comparador). Sin
push, sin mutación de repositorios o ficheros ajenos, sin dispositivo. Sin
congelación (no aplica: no hay instrumento congelado en juego). Artefactos:
este dictamen y los ficheros de trabajo del harness.

— GLM (canal relay David), 2026-11-16 11:30 UTC
