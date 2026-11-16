# PRE-DICTAMEN R4.4 — VERIFICACIÓN PREVIA DE ALCANCE (SIN CÓDIGO) — GLM 2026-11-16

GLM · 2026-11-16 (CET) · canal: relay David
Objeto: paquete de revisión de alcance R4.4 «Modelo Ne(h) y volumen puro»
preparado por Deepseek (propuesta + nota de revisión para GLM), **sin
implementación**.

**Qué es y qué NO es este documento.** Es la verificación independiente previa
de todo lo afirmado que pudo comprobarse en origen (repositorios y oráculo
web), más una posición técnica provisional sobre D1/D2/D3. **NO es el
dictamen D1/D2/D3 + GLOBAL**: ese queda RESERVADO hasta que el relay entregue
los dos ficheros de INTERCAMBIO (§5). Nada de lo aquí verificado autoriza
rama, commit, PR o fusión.

---

## 0. Estado del expediente

Deepseek declara dos documentos nuevos en INTERCAMBIO (espacio compartido,
fuera de git — verificado §1.5):

| Ficha | sha256 declarado | Líneas | Convención |
|---|---|---|---|
| `PROPUESTA-R4.4-MODELO-NEH-VOLUMEN-PURO-20261116.md` | `fe98b00dcec0ca30228898e99edb9d60893e0eafef69ab94d08ec19b6466dc81` | 293 | ASCII sin BOM, CRLF |
| `PARA-GLM-REVISION-PROPUESTA-R4.4-20261116.md` | `7286f0930db2e674194e5dabb15c870b4f7d30260d3cb7bcdfa8effbb7289653` | 338 | ASCII sin BOM, CRLF |

Hash declarado sobre working tree CRLF (precedente del proyecto: git guarda
blob LF). **Ambos pendientes de entrega por relay a GLM.**

## 1. Hechos de repositorio verificados (todos FIEL)

Método GLM 2026-11-16 08:2x UTC: `git fetch` + `ls-tree`/`show`/`grep`
read-only sobre clones locales; endpoints individuales de PR vía
api.github.com.

| # | Afirmación de Deepseek | Verificación GLM | Veredicto |
|---|---|---|---|
| 1 | main sigue en `84d4e9e` | `origin/main` = `84d4e9edf36fecd258268cc82b91ebc1819b39b9` (Merge PR #47 `chore/ci-node24-actions`, 2026-11-16 01:51 +0100) | **FIEL** |
| 2 | no existe `feat/r4.4-neh-volume-pure` | 17 refs remotas listadas; ninguna r4.4 | **FIEL** |
| 3 | no hay PR | `pulls/48` y `pulls/49` → 404; #47 es el último PR creado | **FIEL** |
| 4 | sin cambios en `app/src` por este trabajo | último commit toca solo `.github/workflows/ci.yml`; grep `applyDayNight\|densityDir\|buildDensityVolume` en `app/` @main → NINGUNO; sin fichero alguno layer/volume/profile/density/neh en `app/src` | **FIEL** |
| 5 | solo se crearon los dos documentos | `INTERCAMBIO/` no existe en android (barridas las 17 refs), web ni desktop ⇒ el paquete vive fuera de git, consistente con la declaración | **FIEL** (en lo verificable) |
| 6 | la revisión es de alcance, no de diff | confirmado: no hay rama, ni PR, ni código nuevo que auditar | **FIEL** |

## 2. Oráculo verificado en pin web `8cdc334` (todos FIEL)

Pin re-verificado: `8cdc3348ab087d10dd43807af217da4e246d996d` (main web,
post-R3.0, sin cambios desde el pin de colormap del 2026-11-06).

| # | Afirmación de Deepseek | Verificación GLM | Veredicto |
|---|---|---|---|
| 1 | `buildDensityVolume` vive en `layerProfile.ts` | `src/lib/iono/layerProfile.ts:219` (blob `4184bdb1…`); `densityVolume.ts:9` lo declara literalmente («buildDensityVolume vive en…», desde el drop 167) | **FIEL** |
| 2 | no llama a `applyDayNight` | cuerpo del builder: `densityDir` → `cosChi`; `volumeAltKm`; `evalWithFloor` con suelos `f2FloorKm` memoizados por perfil; `normLogNe`. `applyDayNight` solo aparece en `layerProfile.ts:14` como comentario | **FIEL** |
| 3 | calcula `cosChi` con `densityDir` | `const [cx,cy,cz] = densityDir(latDeg, lonDeg); const cosChi = cx*sunX + cy*sunY + cz*sunZ` | **FIEL** |
| 4 | la web muta los perfiles | `applyDayNight` (`densityVolume.ts:75`) devuelve **void** y muta in situ: `p.NmE *= e; p.NmF1 *= e;` y flags E/F1 a `false` si `e <= 0` | **FIEL** |
| 5 | cadena viva del oráculo | `buildLiveVolume` (`profileGrid.ts`): interp → **applyDayNight** → **builder** (P2-174: atenuar E/F1 nocturnas ANTES de construir) | **FIEL** |
| 6 | fórmula de atenuación | `smoothstep(-0.05, 0.25, cosChi)`; en `cosChi = 0` → `e = 2/27` exacto (aritmética GLM: `t = 1/6`, `t²(3−2t) = 2/27` = 0.074074074…) — coincide con el test del oráculo «terminador parcial: e == 2/27» | **FIEL** |

**Anclas blob GLM del oráculo @ `8cdc334`** (para cotejo inmediato de los
hashes «declarados» cuando la propuesta llegue; sha256 sobre blob LF):

| Fichero (`src/lib/iono/`) | blob git | sha256 (LF) |
|---|---|---|
| `layerProfile.ts` | `4184bdb1dcb2f2920915e0f12f61fd0100b70f7a` | `b4065ac86f1925a661d3411959b90e0ead20ab71dc323aea8a37fc73ede2d0e3` |
| `densityVolume.ts` | `63c16fd569c19a379a6b4a58ec5c006539a69671` | `e6abcc93b1fffc2f355d4f2e8b6c27f731dd1aecfb106971b4db19a45a24824d` |
| `profileGrid.ts` | `73207e86298742c3928078660b9ee2d93e9fde33` | `7060a36ccb49bcb654f2bd2f958a9db6a42fff4fa24729b7c4e846cbabe8a4af` |
| `volumeMarch.ts` | `419cfdec1d39b94aebe0aa77b64afa0446b0fee1` | `038d32911e5fe6b373f9a5879179a3f11dfd82c47fe2963ac8aec633b9473ea1` |
| `volumeJitter.ts` | `9222237ee1d42b8c3a07da13bf8b8494e78c5971` | `0c1d95d28ebf702358fa16bd69de7c8fd485f8b6f2b127c9bad20c2353f8d2d7` |
| `volumeShadow.ts` | `cf20cc709f7eef5e7dddc732d90d405ba6ab14bc` | `bce86dd825443959730afd845e23388f43e7802a3cde6b46d02c6fc7eeaa28ab` |

## 3. Plan R4.4 vs propuesta — verificación y un hallazgo decisivo

Fuente: `docs/r4/PLAN-R4-TIEMPO-PROFUNDIDAD.md` @ `origin/main` (`84d4e9e`).

1. **Lo que el plan nombra en R4.4**: constantes, layout, curva de alturas,
   normalización logarítmica, `volumeIndex`, `volumeAltKm` y el perfil de
   capas; tests espejo de `densityVolume.test.ts` y `layerProfile.test.ts`
   «para la parte pura; sin GL»; DoD: rejilla de prueba con las mismas
   dimensiones, índices y **valores** que el oráculo, bordes y huecos (`<= 0`)
   cubiertos. Grep integral del plan: `applyDayNight`, `densityDir`,
   `buildDensityVolume`, `extractPeakGrids`, `sampleVolume`, `integrateTEC`,
   `profileGrid` → **cero ocurrencias**; los únicos identificadores que el
   plan contiene son `volumeIndex` y `volumeAltKm` (línea 302). Afirmación de
   Deepseek **FIEL con precisión**.
2. **HALLAZGO GLM (a favor de D1)**: el plan nombra como fuente espejo
   `densityVolume.test.ts` — y ese fichero (14 tests) CONTIENE los bloques
   «densityVolume: direccion del motor» (densityDir: `(0,0) → −X`,
   `(0,90E) → +Z`, polo → `+Y`, unitaria) y «densityVolume: applyDayNight»
   (3 tests: subsolar intacto / antisolar apaga E/F1; terminador parcial
   `e == 2/27`; rejilla de tamaño erróneo → no toca nada). Es decir: incluir
   `densityDir` y `applyDayNight` tiene **anclaje en el plan vía el fichero
   de tests nombrado**, no es una extensión arbitraria. La ambigüedad de «la
   parte pura» es real, y por eso Deepseek hace bien en plantearlo como
   decisión D1 sometida a GLM en vez de alcance ratificado.
3. **El DoD exige el builder**: «mismas … **valores** que el oráculo» no es
   verificable sin `buildDensityVolume`. La afirmación de que el constructor
   entra en R4.4 pese a no estar nombrado es **FIEL**.
4. **G7**: el plan define UN solo gate («Volumen/perfil | 72×72×48; alturas;
   rango log; índice; capas; bordes»). Los IDs `G7.1`–`G7.12` son
   numeración de la propuesta; marcarlos como tal es **correcto**.
5. **Puertas puras del plan (referencia para el dictamen)**: el plan solo
   fija G1–G8; cualquier matriz de aceptación más fina que la propuesta
   añada debe trazarse contra el G7 del plan, no sustituirlo.

## 4. Posición técnica provisional (NO es el dictamen)

Anclada a los hechos de §2–§3; sujeta a lo que digan los dos documentos.

**D1 — ACEPTABLE EN SUSTANCIA, CON DOS CONDICIONES.**
- (a) `densityDir` es **dependencia dura** del builder (calcula `cosChi` por
  columna). Sin ella, la única salida es «el builder recibe `cosChi`
  precalculado», que desvía la estructura del oráculo y crea superficie de
  divergencia nueva. Posición GLM: `densityDir` entra en R4.4 **por
  dependencia del DoD**, no como extensión discrecional; el fallback
  precalculado se rechaza.
- (b) `applyDayNight` entra apoyado en el fichero espejo nombrado por el
  plan (3 tests del oráculo). La divergencia declarada — lista nueva en
  Kotlin vs mutación in situ en la web — es aceptable SI queda pinned: los 3
  comportamientos del oráculo (subsolar intacto; antisolar apaga E/F1;
  terminador `e == 2/27` exacto) **más** el contrato de no-mutación (la
  entrada queda idéntica tras la llamada; rejilla de tamaño erróneo →
  entrada intacta, sin excepción). Ese cuarto test no existe en el oráculo
  (allí es void) y es la cobertura nueva que exige la semántica divergente.

**D2 — ACEPTABLE CON UNA CORRECCIÓN.**
Mapa cotejado contra el plan: `extractPeakGrids`, `profileGrid`, cortina,
iso-bands → R4.5 («Cortina Ne(h) + iso-bands») ✓; `sampleVolume`, params de
render (`volumeModeIndex`, `volumeOpacityClamp`, `CHAPMAN_WINNER_COLORS`) y
raymarch → R4.6 («Raymarch density/chapman») ✓; NDK-MSIS → R4.7 ✓.
**Corrección**: `integrateTEC` → «R4.8/HUD» **choca** con el plan R4.8
(«No añade features; solo corrige defectos encontrados por los gates»).
Portar `integrateTEC` en R4.8 sería feature nueva en el slice que las
prohíbe. Destinos conformes: R4.6 (si el HUD de TEC va con el render),
enmienda explícita del plan firmada por David, o descarte documentado si el
móvil no llevará HUD de TEC. La elección es de David.

**D3 — ACEPTABLE.**
`Double` es el dominio numérico del oráculo (números JS = doubles): la
paridad de valores del DoD exige `Double`/`DoubleArray` en el modelo puro, y
`Float` solo en el límite GL (R4.5) es la conversión correcta y tardía.
Condiciones que el dictamen final exigirá ver reflejadas en tests: guards de
`+Inf`/NaN; **B0 90/100 resuelto a favor del oráculo** (`sanitizeB0`
default 100 — divergencia declarada en la propia cabecera del oráculo frente
al 90 legacy de ionomath); convención de meridianos `theta = π − lon` con
los 4 anclajes direccionales del oráculo; rejilla no cuadrada (`lonRes` y
`latRes` independientes en la firma del builder) ejercitada en tests.

**GLOBAL — RESERVADO.** No hay dictamen global sin leer la propuesta y la
nota: las 8 preguntas, la matriz G7.1–G7.12, las tolerancias y los 7
mutantes locales viven ahí. Hasta ahora, **ninguna** afirmación verificable
de Deepseek resultó NO FIEL.

## 5. Pendiente para el dictamen final

1. Entrega por relay de los dos ficheros INTERCAMBIO y verificación de sus
   sha256 declarados (`fe98b00d…`, `7286f093…`) bajo la convención
   ASCII-sin-BOM/CRLF y los recuentos 293/338 líneas.
2. Cotejo de los «hashes del oráculo web declarados» (viven dentro de la
   propuesta) contra las anclas blob del §2 — verificación inmediata a la
   entrega. El claim de Deepseek «coinciden con los declarados» queda
   **pendiente de reproducción GLM**.
3. Lectura de las 8 preguntas exactas y respuesta en el formato
   D1/D2/D3 + GLOBAL.
4. Recordatorio de protocolo conforme: dictamen GLM → GO de David → rama →
   implementación → PR. Sin GO no hay rama; este pre-dictamen no autoriza
   nada.
5. Nota de expediente: sigue pendiente de relay la respuesta de Deepseek
   sobre #45/#46 (mecanismo de fusión; «no consta» de David) — hilo
   separado, no bloquea este.

## 6. Higiene del turno

Turno read-only: `git fetch` (android, web, desktop), `ls-tree`/`show`/
`grep`/`rev-parse`, WebFetch a api.github.com (`pulls/48`, `pulls/49`),
aritmética local del smoothstep (Python). Sin push, sin mutación de
repositorios, remoto o ficheros ajenos, sin congelación. Único artefacto
nuevo: este acta.

— GLM (canal relay David), 2026-11-16 08:24 UTC
