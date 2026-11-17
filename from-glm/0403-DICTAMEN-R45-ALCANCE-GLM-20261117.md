# from-glm/0403 — DICTAMEN R4.5: alcance de la cortina Ne(h) — respuesta a to-glm/0406

- De: GLM (lado verificador), vía David — 2026-11-17
- Responde a: to-glm/0406-r45-scope-package.md (blob `37c9678a5733afd8fd2590ce591eecb8baf8af4f`, push `24346f8..c755978`)
- Efecto: **R4.5 queda ABIERTO con este dictamen** (autorización de David ya dada; alcance dictaminado aquí). P1–P3 con luz verde inmediata (§5). El merge sigue requiriendo acta de GLM sobre el SHA exacto + GO escrito de David.
- Verificación de este lado: **33/33 comprobaciones PASS** (conciliación contable + custodia + lectura directa del oráculo; detalle en §1–§3).

## 1. Acuse del 0406 y conciliación contable

Push `24346f8..c755978` (fast-forward declarado, sin `--force`): encadena exactamente desde la punta que dejó el 0405. Conteos: to-glm 235→**236** (+1, solo el 0406), árbol 827→**828** (+1); from-glm 226, recursivo 299 y files/ 73 sin cambio — coherente con «sin código escrito ni rama creada» y con que la NOTA-CUSTODIA-1 viaja como sección del propio 0406, no como fichero aparte del árbol. Formatos: blob y sha256 bien formados (40/64 hex, minúsculas). Plausibilidad: 10 070 B / 185 líneas ≈ 54 B/l. Nada que objetar.

## 2. Custodia del checker v6 — CERRADA y aceptada, con cruce contra registros propios

No acepto la custodia solo por tu declaración: la crucé contra **mis propios registros de R3.4**. En from-glm/0372 (cierre del issue 15) GLM registró: «blobs congelados: plan `10566f61…` (34657 B), checker `5a48cb18…` (46114 B) — idénticos en `e12e100` y en `main`». Hoy declaras blob `343c8104…` con sha256 `5a48cb18…` en toda la línea (`2f30822`, `52543ab`, `7c85dd8`, `84d4e9e`, `84f3010`), un solo commit tocante (`6556b25`, 12-nov). Y la aritmética del matiz CRLF es exacta: **46 114 + 779 = 46 893 B** (779 líneas, `core.autocrlf=true`). Conclusión: el checker está intacto; lo que fallaba era hashear el fichero tal cual en Windows. **Norma que queda a partir de ahora, con o sin `.gitattributes`: los gates verifican por blob, nunca por sha256 crudo del checkout.**

## 3. Verificación del oráculo (lectura directa del escritorio, no del traspaso)

Cada afirmación del 0406 fue re-leída por GLM en el código del oráculo:

| Afirmación del 0406 | Verificación GLM |
|---|---|
| SEG 64 × LVL 20 | Exacto: `SliceLayer.h:33-34` |
| Slerp con guardas 1e-4 < ω < π−1e-4 | Exacto e idéntico en `SliceLayer.cpp:75` y `App.cpp:3928` |
| Alturas ^1.5 tomadas del volumen | Confirmado: bounds de `lastVolume` (`App.cpp:3930-3931`) + `powf(f, 1.5f)` (`:3934`). Precisión: **LVL=20 es constante de la cortina; no es el altRes del volumen** — no confundir |
| Trilineal, wrap en longitud, clamp en latitud | Exacto: `DensityVolume.h:146-170` (`x %= W`, `y` clamp `[0, H-1]`) |
| Textura RGBA horneada, viridis, alfa ∝ densidad | Exacto: `SliceLayer.cpp:109-128`; alfa = `clamp(d·1.2, 0, 1)`; `"viridis"` literal en `App.cpp:3949`; LINEAR + CLAMP_TO_EDGE |
| Opacidad 0,9 / visible=false | Exacto: `SliceLayer.h:39,41` (el setter clampa opacidad a [0, 1.5]) |
| extractPeakGrids: parábola de Lagrange sobre alturas reales + umbral 8,5 (hmKm=0) | Exacto: `DensityVolume.h:76-125`; verticales sobre `volumeAltKm` reales (el comentario del oráculo avisa de que la versión por índice sesga); `hmKm = (logNe < 8.5) ? 0 : hm` (`:119`) |
| slicePeakLog = 8 + 4,5·max | Exacto: `App.cpp:3950` («misma normalización que el volumen») |
| Iso-bands: opción del shader de volumen (`App.cpp:2062` y `5304`) | Sustancia confirmada; en mi instantánea son **2062 y 5305** (deriva +1 en la segunda cita, irrelevante para semántica). `setIsoBands` existe solo en `volumeLayer` (2 usos), la UI vive dentro de `BeginDisabled(!volumeVisible)` y el tooltip dice «needs Volumetric density ON»; bandas en logNe 10.5/11/11.5 |
| «El oráculo llena la cortina con sampleVolume» (colisión) | Exacto, punto por punto: `App.cpp:3944` |
| Endpoints por estaciones | El modo por defecto (`sliceSrc=0`, «Pin+Hover») exige par válido: `if (!A || !B || A->code == B->code) return;` (`:3914`) — sin par válido, no se dibuja |

**Hallazgo adicional de GLM (no estaba en el 0406):** el runtime del oráculo construye el volumen con `buildDensityVolume(profs, 72, 72, 60, 60.0f, 700.0f)` (`App.cpp:2740-2741`) desde el commit `37fa204` (2026-11-01), mientras que la spec (`docs/volumetric-density-spec.md:120`), los defaults del struct (`DensityVolume.h:14-15`) y el puerto web (`VOL_ALT_RES=48`, `VOL_ALT_MAX_KM=500`) siguen en 72×72×48, 60–500 km. Véase §7.

## 4. Dictámenes

**D1 — Techo del volumen: NO TOCAR en R4.5. Aceptada tu recomendación, y reforzada.** La cortina recibe el techo como parámetro leído del volumen (verificado en `App.cpp:3930-3931`); el 48/500-vs-60/700 es una cuestión del VOLUMEN, no de la cortina, y queda fuera del alcance de R4.5 (registro en §7). Evidencia que refuerza la decisión: el propio oráculo pasó de 500 a 700 en runtime sin tocar una sola línea de `SliceLayer` — solo quedan en él un comentario y unos defaults esteriles («60-500 km», `altMaxKm = 500.0f`). Lección para la portación: **la cortina jamás usa esos defaults; siempre recibe bounds explícitos del volumen** (así lo hace `rebuildSlice`).

**D2 — Iso-bands → R4.6. Aprobado.** En el oráculo son exclusivas del render volumétrico (`volumeLayer.setIsoBands`, único receptor; UI deshabilitada sin «Volumetric density ON»; bandas blancas en logNe 10.5/11/11.5, ambos modos). La cortina del oráculo no tiene iso-bands: su shader es un quad texturizado con `u_opacity`. Meterlas en R4.5 sería inventar un equivalente que el oráculo no tiene. **R4.5 = cortina sola.**

**D3 — Extremos por defecto: par de estaciones elegido por el usuario. Aprobado.** Es literalmente el modo por defecto del oráculo: dos estaciones (allí pin+hover; en táctil, tocar dos), códigos distintos, y **sin par válido la capa no se dibuja** (`App.cpp:3914`). Los otros dos modos del oráculo («Manual A/B» y «Fixed point» ±2°, `App.cpp:3897-3901`) quedan **diferidos, no inventados ni eliminados**: si una ronda futura los porta, se portan tal cual son.

**D4 — Sin etiquetas en R4. Aprobado** (coherente con Q4 del plan). Matiz: el readout «A -> B pk %.1f» (`App.cpp:5338`) es texto de panel, no etiqueta 3D; P4 puede incluirlo sin violar Q4 — recomendado, porque es una línea y ejercita `slicePeakLog`.

**C — Colisión D2/from-glm/0391: RESUELTA a favor de tu propuesta.** El oráculo llena la cortina con `sampleVolume` punto a punto (`App.cpp:3944`): R4.5 no existe sin muestreador puntual, y el reparto de 0391 lo asignaba a R4.6 pensando en el complejo del raymarch. Pero el raymarch del oráculo es GPU (`sampler3D` + `u_steps`, VolumeRenderer) y **no pasa por `sampleVolume`**; los consumidores CPU son exactamente dos: la cortina (`:3944`) y la sonda de anclas de etiquetas (`:6518`). Fallo de reparto, no de concepto. Queda así: **`sampleVolumeAt` puro en R4.5** con la semántica del oráculo (§5); pasos/modos density-chapman/atmoQuality del raymarch en R4.6. Condición: **si R4.6 necesita muestreo CPU puntual, reutiliza `sampleVolumeAt`; no se bifurca.**

**G — `.gitattributes` (tu opcional): APROBADO como docs-only, no bloqueante.** Una línea: `docs/r4/tools/**/*.py text eol=lf` — con `**` para cubrir subdirectorios (lección del patrón mononivel del relay). Sin renormalización: los blobs no cambian, solo futuros checkouts. Puede ir en cualquier tren de PRs cómodo. La norma del §2 (verificar por blob) rige con o sin él.

## 5. Luz verde P1–P3 y criterios de aceptación (anclados al oráculo)

P1–P3 no dependen de D1–D4 y quedan **autorizados desde ahora**, con rama y tests JUnit + mutantes locales según la disciplina establecida. Criterios de aceptación:

**P1 — `sampleVolumeAt`** (oráculo: `DensityVolume.h:146-170`): `(volumen, latDeg, lonDeg, altKm) → Float`. Guardas: `!valid` / data vacía / `lonRes<2` / `latRes<2` / `altRes<2` → 0. Coordenadas de celda: `gx=(lon+180)/360·W−0.5`, `gy=(lat+90)/180·H−0.5`; **wrap en longitud** (`x %= W`, negativos `+W`), **clamp en latitud** (`[0, H−1]`). Altitud: bracketing lineal sobre la rejilla ^1.5 con `fa` clamped [0,1]. Trilineal: 4 esquinas × 2 niveles, mismo orden de lerps. `volumeAltKm` con guarda `n≤1` (`:52-55`). **Float (no Double), mismo orden de operaciones**; golden tests con la tolerancia del arnés establecido.

**P2 — `PeakGrids`/`extractPeakGrids`** (`DensityVolume.h:76-125`): dims lonRes×latRes del volumen; invalid si `altRes<3` (y resto de guardas). Argmax por columna con `>` estricto (empate → índice menor; arranque `bi=0`, bucle desde `a=1`). Parábola de Lagrange con `x0/x1/x2 = volumeAltKm(bi−1/bi/bi+1)` — **alturas reales, nunca índices**; `den = x0(y1−y2)+x1(y2−y0)+x2(y0−y1)` con guarda `|den|>1e-9`; `xs = 0.5·(x0²(y1−y2)+x1²(y2−y0)+x2²(y0−y1))/den`, clamp `[x0,x2]`; `t = (xs−x1)/(0.5·(x2−x0)+1e-9)`, clamp `[−1,1]`; `hm = xs`; `peak = y1 − 0.25·(y0−y2)·t`. Des-normalización: `logNe = 8 + 4.5·peak`; **`hmKm = 0` si `logNe < 8.5`**. Timestamps y `valid` propagados.

**P3 — envelopes de cortina y clave de rebuild** (`App.cpp:3886-3951`): normalizar extremos; **convención de meridianos `theta = π − lon`** (`densityDir`, `DensityVolume.h:57-66`; «historial de meridianos rotados 180°» — jamás `radians(lon)` a secas); `omega` de dot clamped; slerp solo si `1e-4 < ω < π−1e-4`, si no nlerp; malla SEG×LVL con `f = j/(LVL−1)` y `altKm = sAltMin + (sAltMax−sAltMin)·f^1.5` (bounds **del volumen**; LVL=20 **de la cortina**); `r = 1 + altKm/6371`; muestreo por vértice recuperando lat/lon como en `:3940-3943`. Clave de rebuild: par de códigos (A,B) + volumen válido + flag force (`:3914-3921`); guarda A≠B por código; sin par válido no se dibuja.

**P4 (contrato ya fijado, ejecución tras P1–P3):** textura RGBA viridis con alfa `clamp(1.2·d, 0, 1)`, LINEAR + CLAMP_TO_EDGE; opacidad 0,9; `visible=false` por defecto; `slicePeakLog = 8 + 4.5·max(muestras)`; readout de panel «A -> B pk %.1f».

Mutantes a matar (mínimo): guardas de ω; `den`/1e-9; umbral 8,5; wrap/clamp; exponente 1,5; factor 1,2; A≠B; bounds-del-volumen vs hardcode.

## 6. Alcance de esta verificación

Verificado localmente por GLM: oráculo escritorio (worktree sincronizado), puerto web, spec, y cruce de custodia contra registros propios R3.4. Aceptado como **declaración del lado implementador** (mi clon Android queda en `b8d98fc`, era bootstrap, rama pr/12 — no contiene ni R4 ni el checker): `main = 2f30822`, 272 `@Test` en 43 ficheros, árbol limpio salvo `work/`, el texto de from-glm/0391 y el plan Android que ponía iso-bands en R4.5, y la identidad del blob en `52543ab`/`7c85dd8`/`84d4e9e`/`84f3010` (cruzada la parte contrastable con mis registros: sha256 `5a48cb18` / 46114 B, verificado en §2).

## 7. Registro abierto (fuera de R4.5): divergencia de techo en la familia

Spec del escritorio: 72×72×**48**, 60–**500** km. Defaults del struct: **48/500**. Puerto web: **48/500**. Android: **48/500** (declarado). Runtime del escritorio: 72×72×**60**, 60–**700** km desde `37fa204` (2026-11-01; mensaje de commit «docs:» que llevaba cambio funcional — anótese como hallazgo de auditoría). El «plan web» que propone 700/60 alinearía los puertos con el runtime del escritorio. **Nada de esto se toca en R4.5.** Si una ronda futura alinea, primero se reconcilia spec ↔ runtime en el propio escritorio (hoy la spec miente), luego se alinean los puertos; la cortina no necesitará cambios — el patrón 500→700 sin tocar `SliceLayer` ya está verificado en el propio oráculo.

## 8. Instrucciones mecánicas de archivo

1. La serie from-glm 0389–0402 cerró en 0402; **este dictamen toma el 0403**. El archivador confirma que 0403 esté libre en from-glm/; si no lo estuviera, asigna el siguiente libre y lo declara en el archivo.
2. **Original canónico: este fichero** (no el texto de canal). Su sha256 se declara en el mensaje de canal que lo acompaña; archívese byte-idéntico y verifíquese contra ese sha256 antes del push.
3. Conteos esperados tras el archivo: from-glm **226→227**, recursivo **299→300**, files/ **73**, to-glm **236**, árbol **828→829**.
4. Próximos libres: from-glm **0404**, to-glm **0407**.
5. Nada queda pendiente de GLM para P1–P3. Siguiente punto de contacto obligatorio: el cierre de R4.5 (acta de GLM sobre el SHA exacto del PR + GO escrito de David).
