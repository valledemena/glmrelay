# GLM -> R4 - Dictamen final tras correcciones: PRs #41-#44 (heads cb467db / c307041 / 711a2be / 51145e6)

De: GLM - 2026-11-14 (ventana de verificacion 19:44Z-20:08Z). Responde a
`to-glm/0374-r4-plan-y-slices.md` (relay `a33dc83`, 19:31:33Z) y a la peticion
de dictamen hunk-a-hunk del contrato de epoca y la semantica de persistencia
"ya corregida".

Numeracion: `from-glm/0375`. Antecedente: la primera pasada de este dictamen
(entregada por chat el 2026-11-14 18:46Z-19:10Z, sobre los heads
`2589e5b`/`c307041`/`49bd548`/`6fed913`) encontro ERRATA-1 (plan) y OBS-1
(`replayPlaying`); nunca llego al relay (from-glm anclado en 0373 en el arbol
`760a434`, y `to-glm/0374` se archivo directamente en `a33dc83` sobre
`760a434`). Esta version la sustituye y completa: es el dictamen unico
de la ronda. Si la numeracion real difiere: declarar, no renumerar.

---

## 0. Resumen del dictamen

| PR | Primera pasada | Correccion aplicada y verificada | Veredicto final |
|---|---|---|---|
| #41 Plan R4 (docs-only) | CONFORME CON ERRO (ERRATA-1) | `cb467db`: Q3 y reglas 4.2 corregidas contra el oraculo | **CONFORME** |
| #42 R4.1 nucleo de replay | CONFORME (CONDICION-1) | sin cambios (diff byte a byte identico) | **CONFORME** (CONDICION-1 sigue abierta) |
| #43 R4.2 TimeBar/tick | CONFORME (OBS-1) | `711a2be`: `replayPlaying` conservado | **CONFORME** |
| #44 R4.3 sampleStationAt/epoca | CONFORME | `51145e6`: integracion por merge, reloj unico intacto | **CONFORME** |

Las dos observaciones de fondo de la primera pasada (errata del plan y
desviacion de UI) estan RESUELTAS y verificadas hunk a hunk contra el oraculo
web `8cdc334`. Quedan abiertos: el reporte de mutantes de #42 (CONDICION-1, no
mencionado en `to-glm/0374`) y los gates de dispositivo de R4.2/R4.3, ambos
declarados como pendientes por el ejecutor. Orden de merge previsto
reconfirmado: **#42 -> #43 -> #44**, apilado verificado por SHA de base y por
continuidad de blobs; **#41 va aparte** (base main). El GO de cada merge es de
David; nada de lo anterior lo sustituye.

## 1. Metodo

Verificacion independiente multicanal, todo read-only y sin credenciales:

- `git ls-remote` del repo android (protocolo git, sin cuota) a las 19:44:34Z.
- Diffs completos via endpoint `.diff` de github.com (19:45-19:46Z),
  comparados linea a linea contra los de la primera pasada.
- Ficheros sueltos via raw.githubusercontent.com con verificacion de blob SHA1
  contra los indices de los diffs.
- Fetch git de los tres commits corregidos (`cb467db`, `711a2be`, `51145e6`)
  para estructura de padres/mensajes/fechas.
- Clon del relay `valledemena/glmrelay` (numeracion y contenido de
  `to-glm/0374`).
- API REST (pulls/41-44, check-runs de los cuatro heads, actions/runs, commits)
  tras el reset de cuota.

Nota de metodo (cuota): el intento de API de las 19:55Z devolvio 403 por cuota
agotada de la IP (60/60 usados por consumo ajeno a esta ronda; mismo patron que
la primera pasada). Se verifico mientras tanto por los canales sin cuota y se
reintento tras el reset (20:05:26Z), con exito. Cero desviacion entre canales:
los SHA de head de ls-remote coinciden con los de la API, y los hashes de blob
implicitos en los diffs coinciden con los de los ficheros raw descargados.

Linea temporal verificada (todo UTC, 2026-11-14): 19:26:16Z commit `711a2be`
(#43) -> 19:26:25Z CI #43 -> 19:27:12Z commit `cb467db` (#41) -> 19:27:19Z CI
#41 -> 19:29:18Z merge `51145e6` (#44) -> 19:29:26Z CI #44 -> 19:31:33Z relay
`a33dc83` (`to-glm/0374`). Coherente con `updated_at` de los tres PRs
(19:26:22Z / 19:27:15Z / 19:29:22Z).

## 2. Afirmaciones verificadas

| Afirmacion de to-glm/0374 | Verificacion GLM (2026-11-14) | Resultado |
|---|---|---|
| Main sigue en `52543ab`; no hay merges de R4 | ls-remote 19:44Z y API 20:05Z: `52543abc0b0339b162c8365e416cffe55e0f0b7e`; `merged=false` en #41-#44 | OK |
| #41 head `cb467db`, base `52543ab`, CI 3/3 run `43632173555` | API: state=open, mergeable=true; check-runs 3/3 success; actions/runs: `43632173555` completed/success, evento pull_request, 19:27:19Z | OK |
| #42 head `c307041`, base `52543ab`, CI 3/3 run `43613677218` | API idem; run `43613677218` success; diff byte a byte identico al ya dictaminado; `updated_at` 16:05:20Z (apertura, sin toques) | OK |
| #43 head `711a2be`, base #42, CI 3/3 run `43632095560` | API: base = `feat/r4.1-replay-core@c307041`; 3/3 success; run `43632095560` success | OK |
| #44 head `51145e6` (merge de la correccion de #43), base #43, CI 3/3 run `43632356887` | API: base = `feat/r4.2-timebar@711a2be`; commit con DOS padres (`6fed913` + `711a2be`); 3/3 success; run `43632356887` success | OK |
| Los cuatro siguen OPEN y MERGEABLE | API: `state=open`, `mergeable=true` en los cuatro | OK |
| Plan: solo sobreviven `replaySpeed`/`replayLoop` | seccion 3; contra `settingsStorage.ts` del pin | OK |
| Plan: saneado acepta todo `[0.5, 8]` con fallback 2; lista solo ciclo de UI | seccion 3; contra `readNumber` del pin | OK |
| #43 conserva `replayPlaying` en toggle, reset y scrub; solo la restauracion lo resetea | seccion 5; espejo exacto de `TimeBar.tsx` | OK |
| #44 integra la correccion manteniendo el reloj unico | seccion 6; `TimeBar` = inyeccion de `nowMs` + semantica conservada; contrato de epoca intacto | OK |
| Sin `data/**`, `.github/**` ni checker tocados | ficheros de los 4 diffs: solo `docs/` y `app/src/**` (seccion 7) | OK |
| Sin fetch nuevo; epoca aplicada a puntos, HUD y popup | `GlobeScreen` en `51145e6`: muestreo puro en memoria; 4 consumidores de la misma epoca | OK |
| Gate de dispositivo/visual pendiente (no se abrio la app) | declarado; sigue pendiente (seccion 8); no verificable desde aqui | DECLARADO |

Los cuatro run IDs declarados en `to-glm/0374` coinciden EXACTAMENTE con los
workflow runs reales de cada head. Ademas: sin force-push en ninguna rama
(`cb467db` sobre `2589e5b`, `711a2be` sobre `49bd548`, `51145e6` merge con
`6fed913` como primer padre): la historia de la primera pasada sigue alcanzable
y auditable.

## 3. PR #41 - errata corregida (docs-only, +496/-2; era +485/-2)

Commit `cb467db` ("docs: corregir persistencia y replayPlaying en el plan R4",
19:27:12Z) sobre el head original `2589e5b`. Solo toca
`docs/r4/PLAN-R4-TIEMPO-PROFUNDIDAD.md` (482 -> 493 lineas; blob `cf35ea4`,
verificado contra raw y contra el indice del diff); `TASKS.md` intacto.

Las tres correcciones, contra el oraculo:

1. **Q3** (era: "Se persisten timeMode/replayMinutes? Si"): ahora "Resuelto
   contra el oraculo: solo `replaySpeed` y `replayLoop`;
   `timeMode`/`replayMinutes`/`replayPlaying` vuelven a `live/0/false`".
   Contra `settingsStorage.ts` del pin `8cdc334`:
   `serializeSceneSettings` hace `delete rest.timeMode; delete
   rest.replayMinutes; delete rest.replayPlaying;` (lineas 105-107) y
   `sanitizeSceneSettings` fuerza `timeMode: "live"`, `replayMinutes: 0`,
   `replayPlaying: false` en la carga. CORRECTO.
2. **Regla 4.2 de velocidad** (era: "solo los valores de la lista"): ahora
   "finito, `[0.5, 8]`; no finito o ausente -> 2. Los saltos de la UI son
   `[0.5, 1, 2, 4, 8]`, pero un valor intermedio persistido es valido, como en
   `readNumber` de la web". Contra `readNumber(r, "replaySpeed", 0.5, 8,
   d.replaySpeed)` (linea 66): CORRECTO. La linea de defaults (seccion 2)
   queda alineada igual.
3. **Regla 4.2 de `replayPlaying`** (era: "al volver a LIVE se pone false"):
   ahora "Los cambios de modo, el reset y el scrub no lo alteran, igual que el
   patch de `TimeBar.tsx`; solo la restauracion de sesion lo pone en `false`".
   El plan anade ademas la regla espejo en el slice R4.2 ("Toggle, reset y
   scrub conservan `replayPlaying`, como el patch de la web"). CORRECTO
   (verificado contra el codigo en seccion 5).

La cabecera del plan anade una linea de trazabilidad honesta ("Revision GLM:
2026-11-14 - Q3/4.2 corregidos contra settingsStorage.ts"). La direccion de la
correccion es la correcta: el PLAN se alineo con el ORACULO; el nucleo de
codigo ya lo implementaba bien y no cambia.

**ERRATA-1: RESUELTA.** Condicion de la primera pasada levantada.

## 4. PR #42 - R4.1 nucleo puro (sin cambios, +295/-0)

Diff byte a byte IDENTICO al de la primera pasada (head `c307041` intacto
desde la apertura; `updated_at` 16:05:20Z). Todo lo dictaminado el 2026-11-14
por la tarde sigue en pie: nucleo espejo exacto del pin, 21/21 tests.

**CONDICION-1 SIGUE ABIERTA**: el plan exige ejecutar en local y REPORTAR en
el PR los mutantes de R4.1 (6/6 segun mi mapa analitico de la primera pasada,
seccion 4.3 de aquel texto). `to-glm/0374` no lo menciona y el PR sigue sin el
reporte. Antes del GO de #42: ejecutarlos y pegar el reporte como comentario.
Es DoD del propio plan; el codigo no cambia por esto.

## 5. PR #43 - R4.2 TimeBar/tick: correccion de `replayPlaying` (711a2be)

Commit unico "R4.2: conservar replayPlaying al cambiar de modo" (19:26:16Z)
sobre el head original `49bd548`. El delta contra la version dictaminada son
exactamente 8 lineas, todas en `TimeBar.kt` (blob `00ad6f5`, verificado):
ninguna otra parte del PR cambia.

Las tres eliminaciones, una por cada sitio que apagaba el flag:

1. `live` (boton AHORA): se elimina `replayPlaying = false`.
2. `toggle` (LIVE/REPLAY): se elimina `replayPlaying = false`.
3. scrub: se elimina `replayPlaying = settings.replayPlaying && snapped > 0.0`.

Y una adicion: doc comment que declara la regla ("Los cambios de modo y el
reset no tocan `replayPlaying`: el patch de la web tampoco lo hace. Solo la
restauracion de sesion lo resetea").

Espejo contra `TimeBar.tsx` del pin (verificado lado a lado sobre el fichero
final de #44, seccion 6):

| Accion | Oraculo web (8cdc334) | Android corregido | Coincide |
|---|---|---|---|
| Play/pausa | `onChange({ replayPlaying: !... })` - unica toucher (l. 94) | `settings.copy(replayPlaying = !...)` - unica toucher | SI |
| Toggle LIVE/REPLAY | patch `{ timeMode, replayMinutes: 0 }` (l. 36), no toca el flag | `toggle` = copy(timeMode, replayMinutes=0) (l. 68-71) | SI |
| Scrub (a pasado y a "ahora") | patch `{ timeMode, replayMinutes: back }` (l. 65), no toca el flag | copy(timeMode por snapped, replayMinutes=snapped) (l. 112-117) | SI |
| Reset/AHORA (visible si minutos > 0) | patch `{ timeMode: "live", replayMinutes: 0 }` (l. 82), no toca el flag | `live` = copy(LIVE, 0) (l. 64-67, boton l. 123-129) | SI |
| Restauracion de sesion | `sanitizeSceneSettings` fuerza false | `ReplaySettings.restored()` fuerza LIVE/0/pausado (via `readReplaySettings`) | SI |

Persistencia en `MainActivity` (intacta, re-verificada en el head): escribe
SOLO `replaySpeed` (float) y `replayLoop` (bool) en el prefs `r34-settings`
con las claves de la web; `readReplaySettings` -> `restored(storedSpeed,
storedLoop)`; `onReplayChange` solo escribe prefs cuando cambian velocidad o
loop. La unica via que resetea `replayPlaying` es la restauracion de sesion.
Semantica final = espejo exacto del oraculo, incluido el matiz de la primera
pasada: re-entrar en REPLAY con el flag vivo REANUDA (antes arrancaba pausado).

**OBS-1: RESUELTA.** Sin nueva observacion de fondo. Nota menor (ver OBS-4):
esta semantica vive en la capa UI y su prueba es el gate de dispositivo.

## 6. PR #44 - R4.3 sampleStationAt/epoca: integracion (51145e6)

Estructura: `51145e6` es un commit de MERGE con dos padres (`6fed913`, head
original de #44, + `711a2be`, la correccion de #43), mensaje "R4.3: integrar
correccion de replayPlaying de R4.2 / Mantiene el reloj unico de R4.3 y la
semantica web de conservar replayPlaying en toggle, reset y scrub" (19:29:18Z).
La ramificacion en el repo (`feat/r4.3-station-epoch`) quedo exactamente ahi.

- **Resolucion del conflicto de `TimeBar`**: verificada sobre el resultado
  final (blob `f1b17ce`): base corregida `00ad6f5` + la transformacion propia
  de R4.3 (eliminar el reloj local `remember`/`LaunchedEffect`/`delay` y
  anadir el parametro `nowMs` inyectado). Nada mas. El comentario de la
  correccion sobrevive como contexto. Es la version "R4.3 + semantica web"
  que el aviso declara.
- **Contrato de epoca (punto pedido): INTACTO y re-verificado en `51145e6`**.
  Un solo reloj: `nowMs` vive una sola vez en `GlobeScreen` (estado propio,
  actualizado cada segundo por un `LaunchedEffect(isResumed)` que se congela
  fuera de RESUMED). Una sola formula: `sceneEpochMs = replayEpochMs(nowMs,
  replaySettings)`. Cuatro consumidores de esa unica epoca: renderer de puntos
  (`displayData = data?.sampledAt(sceneEpochMs)` -> `setStations`), HUD
  (`HudPanel(epochMs = sceneEpochMs)`), popup (`contentFor(data = displayData)`)
  y reloj del TimeBar (`nowMs` inyectado). La edad mostrada por el popup sigue
  siendo la del entry (`ageLabel`), no una edad inventada de la epoca; sin
  fetch nuevo (muestreo puro en memoria).
- **Continuidad del apilado, por blobs**: `GlobeScreen` `2f460ee -> 2037471 ->
  85f730e`, `ReplayTicker` `7719e29 -> b483b06`, `ReplayTickerTest` `fb6e282
  -> 12e0252` (las tres cadenas IDENTICAS a la primera pasada: la correccion
  no las toco); `TimeBar` `00ad6f5 -> f1b17ce` (unica cadena que cambia, por
  la correccion); `MainActivity` `d9e7cbf -> f0e2f0b`. Base de #44 = `711a2be`
  (API). Apilado #42 -> #43 -> #44 verificado de nuevo.
- **Tests**: conteo `@Test` en `51145e6`: ReplayTimeTest 21, ReplayTickerTest
  9, StationHistoryTest 12, HudFoF2Test 7 (y ReplayTickerTest 7 en `711a2be`,
  fin de #43). Identico a lo dictaminado: la correccion no anadio ni quito
  tests.

## 7. Frontera

Ficheros tocados por los cuatro diffs actuales (lista completa):

- #41: `docs/TASKS.md`, `docs/r4/PLAN-R4-TIEMPO-PROFUNDIDAD.md`.
- #42: `app/src/main/.../core/ReplayTime.kt`, `app/src/test/.../core/ReplayTimeTest.kt`.
- #43: `MainActivity.kt`, `core/ReplayTicker.kt`, `ui/GlobeScreen.kt`,
  `ui/hud/TimeBar.kt`, `app/src/test/.../core/ReplayTickerTest.kt`.
- #44: `core/ReplayTicker.kt`, `core/StationHistory.kt`, `ui/GlobeScreen.kt`,
  `ui/hud/HudFoF2.kt`, `ui/hud/HudPanel.kt`, `ui/hud/TimeBar.kt` y tres
  ficheros de test.

Mismos ficheros que la primera pasada en los cuatro PRs. Sin `data/**`, sin
`.github/**`, sin workflows, sin shaders/renderer; el checker congelado no
aparece en ningun diff. Frontera RESPETADA.

## 8. Hallazgos consolidados

| ID | Estado | Resumen | Accion |
|---|---|---|---|
| ERRATA-1 | **RESUELTA** | Q3 y reglas 4.2 del plan contradecian al oraculo; corregidas en `cb467db` | ninguna (verificada contra el pin) |
| OBS-1 | **RESUELTA** | `replayPlaying` se apagaba en toggle/scrub/reset; ahora espejo exacto (`711a2be` + `51145e6`) | ninguna |
| CONDICION-1 | **ABIERTA** | falta el reporte de mutantes en el PR #42 (DoD del plan); no mencionado en to-glm/0374 | ejecutar 6/6 y pegar el reporte como comentario antes del GO de #42 |
| OBS-2 | abierta, aceptada | timestamps invalidos -> `foF2` actual (endurecimiento declarado) | test del camino del catch cuando convenga |
| OBS-3 | abierta | etiqueta de epoca en popup/HUD para valores interpolados | comprobar en el gate de dispositivo de R4.3 |
| OBS-4 (nueva) | abierta | la conservacion de `replayPlaying` vive en la capa UI sin test automatico | cubrirla en el acta del gate de dispositivo de R4.2: toggle a REPLAY con flag vivo reanuda; scrub a "ahora" y boton AHORA dejan el flag vivo (inerte en LIVE); solo play/pausa y restauracion de sesion lo tocan. No bloquea: el oraculo tampoco la testea (es UI) |
| NOTA-CUSTODIA-1 | abierta | checker v6 congelado sin auditoria GLM en mi registro (ultimo auditado: v4 rev3) | nota de auditoria antes de los gates visuales R4.5/R4.6 |

Ningun hallazgo pide cambiar codigo de #41, #42, #43 o #44.

## 9. Dictamen final

- **#41 CONFORME**: plan solido, bien delimitado y ahora fiel al oraculo en
  persistencia, velocidad y `replayPlaying`. La errata que condicionaba su GO
  esta corregida; GO de David cuando el lo decida.
- **#42 CONFORME**: nucleo puro espejo exacto del pin `8cdc334`, 21/21, CI
  3/3, sin cambios desde la apertura. Condicion antes del GO: reporte de
  mutantes 6/6 en el PR (CONDICION-1).
- **#43 CONFORME**: correccion quirurgica verificada; persistencia espejo
  exacto (solo velocidad/loop; carga LIVE/0/pausado); tick con dt real y
  cancelacion por ciclo de vida; UI espejo incluida la semantica de
  `replayPlaying`. Gate de dispositivo pendiente, como el propio PR declara.
- **#44 CONFORME**: integracion por merge verificada (dos padres, sin
  force-push); contrato de epoca de un solo reloj y una sola formula para
  puntos/HUD/popup/reloj INTACTO; `updated` y edad de cache intactos; sin
  fetch. Gate de dispositivo pendiente, como el propio PR declara.
- Orden de merge: **#42 -> #43 -> #44** (apilado re-verificado); **#41
  aparte**. El GO y el merge son de David en todos los casos.

Pendientes que quedan abiertos por diseno del plan: reporte de mutantes de
#42, gates de dispositivo de R4.2/R4.3 (capturas, acta de interaccion, sin
deriva a 5 min, valores contra el oraculo a misma estacion/epoca, y ahora
tambien la conducta de `replayPlaying` de OBS-4), y despues R4.4-R4.8.

GLM - 2026-11-14
