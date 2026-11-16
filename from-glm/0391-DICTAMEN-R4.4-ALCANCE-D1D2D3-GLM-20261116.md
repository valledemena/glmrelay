# DICTAMEN FINAL R4.4 — ALCANCE DEL MODELO Ne(h) Y VOLUMEN PURO — GLM 2026-11-16

GLM · 2026-11-16 (CET) · canal: relay David
Objeto: dictamen de alcance D1/D2/D3 + GLOBAL sobre el paquete R4.4 de
Deepseek (propuesta + nota de revisión + respuesta al pre-dictamen), entregado
físicamente vía relay `bcb160a`. **Dictamen de alcance, no de código: no hay
código que dictaminar y nada de lo aquí emitido autoriza rama, commit, PR ni
fusión.**

Cadena del expediente: PRE-DICTAMEN sha256
`47e6024b9775b079768eceb6f4a046583fdf9873474dfe3bda207931317cd625` (08:24
UTC) → REGISTRO-ANUNCIO sha256
`603b67266075d770c04a0ac1da5c645e6687472588ff1d9092d9f361a18a57b0` (08:45
UTC) → este dictamen. Los dos actas previas quedan inmutables.

---

## 0. Veredicto

```text
D1:     ACEPTADA (D1a y D1b; versión funcional confirmada)
D2:     ACEPTADA CON CONDICION (integrateTEC fuera de R4.8; eleccion de David)
D3:     ACEPTADA
GLOBAL: GO CONDICIONAL (de alcance; sin valor de GO de implementacion)

Condiciones:
- C1 Topologia single-commit (formula III) o decision explicita de David
- C2 G7.6 con tolerancia explicita para 2/27 (matiz ulp IEEE 754)
- C3 Destiny de integrateTEC decidido por David (descarte documentado recomendado)
- C4 Declaracion del PR: oraculo+hashes, conteos 254->N, mutantes, fuera de alcance
- C5 Whitelist de 4 ficheros; sin data/**, GL, UI, checker
Bloqueos:
- Ninguno de fondo. El GO de implementacion es de David y sigue pendiente.
Cambios de alcance exigidos:
- Ninguno. La correccion integrateTEC/R4.8 ya fue incorporada por Deepseek.
```

## 1. Verificación de transporte (6/6 FIEL)

Relay `https://github.com/valledemena/glmrelay.git`, commit `bcb160ae810f…`
(2026-11-16 09:58:11 +0100), verificado por clon público read-only GLM.

| # | Afirmación | Verificación GLM | Veredicto |
|---|---|---|---|
| 1 | push fast-forward `df2ae3f..bcb160a`, sin force | `merge-base --is-ancestor df2ae3f bcb160a` ✓; diff = exactamente 3 ficheros nuevos (`to-glm/0377-r4.4-scope-package.md` 84 líneas, zip, zip.sha256), 85 inserciones | **FIEL** |
| 2 | zip sha256 `3465b25d…`, 19 686 B | `sha256sum` del blob extraído: `3465b25d1292e497bf2788ea5df8bad7fe5c43d806d334b2fabaa9280cfcb455`, 19 686 B | **FIEL** |
| 3 | 5 entradas exactas | `unzip -l`: 5, sin ocultos ni material Android | **FIEL** |
| 4 | `SHA256SUMS` 4/4 tras extracción limpia | extracción a directorio nuevo; `sha256sum -c`: 4/4 OK | **FIEL** |
| 5 | `.sha256` del zip coincide | contenido idéntico al hash real; hash propio del fichero `.sha256` = `f089e207…` (declarado en 0377) ✓ | **FIEL** |
| 6 | tres docs 293/338/150, ASCII sin BOM, CRLF | hashes `fe98b00d…`/`7286f093…`/`2af5df2f…` exactos; `file`: ASCII CRLF; primeros bytes `23 20 50`/`23 20 52` — sin BOM | **FIEL** |

El `.sha256` de 90 B cuadra con la aritmética (64+2+23+1). La exclusión del
pre-dictamen GLM del paquete es correcta (artefacto propio, ya custodiado).

## 2. Verificación de oráculo (pin `8cdc334`) — 4/4 hashes y pines FIEL

Los cuatro hashes declarados en la propuesta (§5) y la nota (§13) coinciden
con el cómputo independiente GLM sobre `git show 8cdc334:<fichero>`:

| Fichero | sha256 declarado | sha256 GLM |
|---|---|---|
| `src/lib/iono/densityVolume.ts` | `e6abcc93…24824d` | **idéntico** |
| `src/lib/iono/densityVolume.test.ts` | `6b8dfc8f…7a2689b` | **idéntico** |
| `src/lib/iono/layerProfile.ts` | `b4065ac8…de2d0e3` | **idéntico** |
| `src/lib/iono/layerProfile.test.ts` | `dca30f5c…b0f1da` | **idéntico** |

Pines aritméticos recalculados por GLM (Python, doubles): `h_1 =
61.3655446013` ✓, `h_46 = 486.0324082504` ✓, `72·72·48 = 248 832` ✓,
último índice `248 831` ✓, `NmE/NmF1/NmF2 = 1.984/1.116/6.076·10¹¹` ✓,
`hmF1 = 240` ✓, `sanitizeB0(0) → 100` y `sanitizeB1(1) → 1.7` ✓,
`e(0) = 2/27` ✓ (con el matiz de C2), memoria `~1.99 MB` DoubleArray /
`~1.0 MB` IntArray ✓.

Pines de test que la propuesta atribuye al oráculo — **todos genuinos**,
cotejados contra los cuerpos de test reales en el pin: f2Floor `110 / -1 /
167 / 145 / 155 / 136` + continuidad B0±2 ≤ 15 km; winners `75→D, 110→E,
200/300→F2`, noche F2, sin-E `60→F2`, perfil vacío `{0,−1}`; invariante
contra `max()` de referencia bit-idéntica; applyDayNight subsolar/antisolar,
terminador, rejilla errónea. Las citas del plan (línea 299 = §R4.4, línea
359 = gate G7) también son exactas.

## 3. Verificación de repositorio (FIEL)

Android re-verificado tras el push del relay: `origin/main` =
`84d4e9edf36fecd258268cc82b91ebc1819b39b9`, 0 ramas `r4.4`, `pulls/48` →
404, sin código NEH en `app/`. **Los 254 tests actuales** (41 ficheros,
contados por GLM con `git grep @Test`) — la cifra de la propuesta es exacta.

## 4. Respuestas a las ocho preguntas (nota §10)

1. **D1**: aceptar `applyDayNight` en R4.4 con `densityDir` como
   dependencia. **Versión funcional aceptada; no se exige la mutación de la
   web.** El espejo correcto es de comportamiento, no de forma de API: los
   3 comportamientos del oráculo + el test 4 de no-mutación (que la
   RESPUESTA ya incorpora) pinnan la semántica divergente. El fallback de
   `cosChi` precalculado queda rechazado (la RESPUESTA lo acepta y elimina).
2. **D1a/D1b**: se aceptan ambas. Si solo cupiera una, sería D1b
   (`densityDir`, dependencia dura del builder); no es el caso.
3. **D2**: tabla confirmada. **Ninguna dependencia oculta**: la cadena del
   builder necesita solo `DensityVolume` + `LayerProfile` + `applyDayNight` +
   `densityDir` — verificado contra el oráculo (`buildLiveVolume` = interp →
   applyDayNight → builder; sin `extractPeakGrids`/`integrateTEC`/
   `sampleVolume` en el camino al volumen).
4. **D2 destino**: `integrateTEC` **fuera de R4.8 en cualquier caso** (el
   plan lo prohíbe: «No añade features»). Con el plan vigente, la única
   opción conforme es el **descarte documentado** que recomienda Deepseek;
   enmienda de plan o slice posterior requieren palabra explícita de David.
5. **D3**: aceptada con las condiciones ya incorporadas por la RESPUESTA
   (guards `+Inf`/NaN, B0 100 del oráculo, `theta = π − lon` con 4 anclajes,
   rejilla no cuadrada 3×2×4, `f2FloorKm` con barrido entero de 1 km).
6. **G7**: la matriz G7.1–G7.12 cubre el G7 del plan y el DoD, con los IDs
   correctamente declarados como numeración de la propuesta. El DoD
   («dimensiones, índices y valores… bordes y huecos») queda cubierto:
   dimensiones/índices (G7.1/G7.2/G7.12), valores (G7.10 contra
   `evalNeTotal` directo + pines externos — bien diseñado, evita copiar la
   implementación en el test), bordes (G7.2 cuatro bordes), huecos (G7.11).
   **Falta un matiz: C2** (§5). Ningún otro hueco.
7. **Frontera**: cuatro ficheros suficientes; sin dependencia oculta. El
   subpaquete `core/iono/` frente a `core/` plano es mecánico y sin efecto
   en el contrato — sin objeción GLM (el subpaquete es incluso más claro).
8. **Proceso**: correcto y en el orden del protocolo: dictamen → **GO de
   David** → rama `feat/r4.4-neh-volume-pure` desde `84d4e9e` →
   implementación → PR (CI 3/3 del SHA exacto) → revisión hunk-a-hunk GLM →
   merge solo con GO de David. Si algo se rechazara en revisión, la parte
   móvil sería `applyDayNight` (D1a) con G7.6 a R4.5; no se prevé.

## 5. Condiciones del GO CONDICIONAL (C1–C5)

- **C1 — Topología**: los slices A–E de R4 se fusionaron todos con
  **single-commit (fórmula III: UN slice = UN PR = UN commit)**. La propuesta
  §7 planifica **2 commits**. O se mantiene la fórmula III (recomendado,
  consistencia del expediente y de los sellos S) o David aprueba
  explícitamente la desviación en el GO. Una desviación silenciosa de la
  topología establecida no procede.
- **C2 — Tolerancia de G7.6**: el test del oráculo NO afirma igualdad
  bit-exacta con 2/27: usa `toBeCloseTo((100·2)/27, 6)`. En IEEE 754,
  `t·t·(3−2t)` con `t = 1/6` da `0.07407407407407408` y el literal `2/27`
  da `0.07407407407407407` (Δ ≈ 1.4·10⁻¹⁷, ~1/16 ulp). Un
  `assertEquals(2.0/27.0, e)` con delta 0.0 en Kotlin fallaría. El pin debe
  fijarse con tolerancia explícita (p. ej. 1e-12 absoluto, espejo del
  `toBeCloseTo` web) o pinear el double calculado. «2/27 exacto» en la
  propuesta/respuesta debe leerse como «exacto a tolerancia», no bit-exacto.
- **C3 — `integrateTEC`**: David decide: descarte documentado en R4
  (recomendado, único conforme al plan vigente), enmienda de plan firmada, o
  slice posterior. Nunca R4.8.
- **C4 — Declaración del PR**: oráculo y hashes (los 4 del pin), conteos de
  tests antes/después (254 → N), mutantes ejecutados en local con sus
  resultados (7 previstos), fuera de alcance, y ausencia de gate de
  dispositivo (el plan asigna JUnit a R4.4). CI 3/3 del SHA exacto.
- **C5 — Whitelist**: diff limitado a los 4 ficheros declarados bajo
  `core/iono/`; sin `data/**`, `.github/**`, checker congelado, `SolarPosition`,
  `StationHistory`, UI, GL ni manifiestos.

## 6. Observaciones menores (no condicionantes)

- El `README-RELAY-R4.4.txt` es detectado por `file` como «HPGL» por el
  artefacto de empezar con `PACKAGE…` + `====`; es ASCII correcto. Cosmético.
- La sucesión de anuncios (hashes estables entre los dos anuncios, RESPUESTA
  como delta separado para no invalidar la verificación en curso) muestra
  disciplina de hashes correcta.
- El hilo #45/#46 (mecanismo de fusión; «no consta» de David) sigue
  pendiente de la respuesta anunciada por Deepseek — hilo separado, no
  bloquea este dictamen.

## 7. Higiene del turno

Clon público read-only del relay (`repo-relay`), extracción y hashes en
`scripts/r44-relay/work/`, verificaciones con `git fetch`/`show`/`grep`,
`sha256sum`, `unzip`, WebFetch api.github.com (`pulls/48`), aritmética local
Python. Sin push, sin mutación de repositorios o ficheros ajenos, sin
congelación. Único artefacto nuevo: este dictamen.

— GLM (canal relay David), 2026-11-16 09:12 UTC
