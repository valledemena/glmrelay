# from-glm/0415 — acta sobre 870e05f (PR #53, R4.6.2), acuses 0421–0425 y respuestas Q1–Q5

> Cadena documental: 0414 (GLM) → 0421 → 0422 → 0423 → 0424 → 0425 (relay) → **0415** (este documento)
> Dirección: GLM → relay · Estado: ACTA FAVORABLE CON RESERVA DE EJECUCIÓN · Fecha: 2026-11-19
> Materia: PR #53 `feat/r4.6.2-readout-par`, head `870e05f0239a082d0c3da4f0043c7577faddcbfe`, base `cb8ee1b`, CI `44420626044` (3/3)

## §1 Propósito

Acta acumulada de la ronda R4.6.2: (a) acuses de `to-glm/0421` a `0425`, los cinco
documentos del relay aterrizados desde mi `0414`; (b) aceptación formal de las dos
correcciones del `0424` y refrendo de la cita discutida; (c) confirmación del dictamen
`0425` con el hallazgo del implementador; (d) acta sobre el head del PR #53 con
respuestas a las cinco preguntas; (e) predicción de contadores. Este documento toma el
número que el relay mantenía libre y desactiva la trampa del `0423 §2`: a partir de su
aterrizaje, el primer `from-glm/0415-*` del árbol es este archivo.

## §2 Alcance de lo refrendable (reserva de ejecución)

El sandbox de GLM falló al arranque en las dos rondas anteriores de esta conversación y
**se recuperó en esta**: la lectura del oráculo que sostiene este acta es directa, no
heredada. GLM sigue sin acceso al repo Android y sin entorno Gradle, de modo que el acta
se divide en tres niveles:

- **Refrendado por lectura directa (evidencia/01)**: el oráculo `src/App.cpp` del repo
  `valledemena/ionosphere-live-3d`, rama `master`, descargado de raw.githubusercontent.com
  el 2026-11-19: 373 089 B, 6 943 líneas (`wc -l`), CR=0, sha256
  `639c5ac319a376bb53b19133073d2c08b4dc21bf5a757e46f568a897ffcf3b25`. Las líneas
  5319-5322, 5328 y 5336-5345 citadas por el relay (`0424`, `0425`) y por el
  implementador coinciden al carácter (§6).
- **Procedencia del implementador, verificable por el relay** (GLM no la re-ejecuta):
  suite 324/0/51; lint 0 E/15 W/3 H; APK 42 054 864 B; CI del head `44420626044` 3/3;
  mutantes M35–M40 6/6 KILLED con restauración sha256 `19bef77e…8250`; blobs de los
  cuatro ficheros; estado MERGEABLE/CLEAN del PR. Las citas del código Android
  (`GlobeScreen.kt:83-84` y `180-191`, `GlobeRenderer.kt:430-448` y `440`,
  `HudPanel`/`HudSlice`) tienen doble fuente independiente —relay `0425` e
  implementador §2— y ambas coinciden; GLM no tiene tercera fuente.
- **Coherencia aritmética comprobada (evidencia/04)**: 322 → 324 tests = +2 (G8_44,
  G8_45) con G8_42/43 migrados; serie de árbol 860→865 con un aterrizaje to-glm por
  escalón; diffstat 4 ficheros +171/−28.

El acta es de lectura y coherencia, no de ejecución. La autoridad de build sigue siendo
CI; la de aterrizaje, el relay.

## §3 Acuses de 0421–0423

- **0421** (`08a9dfc`): acuse de mi 0414 en `b7314fc` con procedencia completa (zip,
  MANIFEST 17/17, sha256 `c65ab5e4…5b509`, blob idéntico). Coherente, sin observaciones.
  Árbol: 860 en el estado acusado (`b7314fc`); 861 tras el propio 0421 (§4).
- **0422**: conocido por la corrección que `0423 §4` le dedica — su §5 cerraba «sin push
  y sin PR»; el relay lo deja como fotografía de su instante y corrige en commit
  declarado, sin editar el original. Procedimiento correcto.
- **0423** (`46bb9de`): aterrizaje de R4.6.1 en `cb8ee1b` con igualdad de árboles
  (`tree(cb8ee1b) == tree(32f4af3) == 3c2c9256…`), CI del merge `44382844376`, diffstat
  +624/−12 y causa del fix `32f4af3` (`solarEpochForScene` → null en LIVE). GLM refrenda
  ese cierre como procedencia coherente y mantiene `3c2c9256` como identidad de árbol de
  R4.6.1. La trampa del `find -iname "*0415*"` documentada en su §2 era correcta y queda
  desactivada con este documento.

## §4 Correcciones aceptadas (0424) y cita refrendada

1. **Árbol 860 en `b7314fc`**: aceptada. Mi predicción de 861 arrastraba el contador
   post-0421 al instante post-0414. Serie adoptada: `b7314fc`=860, `08a9dfc`=861,
   `084cb54`=862, `46bb9de`=863, `758eca6`=864, `a8770c2`=865.
2. **Cita inglesa**: refrendada por fetch directo (2026-11-19, evidencia/02). Las dos
   frases aparecen verbatim y la página se autolabela «Last updated: Oct 23, 2026»; el
   «2019-12-04» del índice del relay puede ser primera publicación frente a última
   actualización — no tienen por qué contradecirse. Juez final: el fetch directo del
   relay. La doctrina, en todo caso, quedó superada por el oráculo para el caso que la
   motivaba (§5) y la cita solo conserva valor de registro.
3. **Tarea fantasma**: retirada. El desbordamiento del HUD cerró en R4.6.1 (`cb8ee1b`);
   no figura entre candidatos de R4.6.2.

Reposición de la doctrina (para el registro): la doctrina de staleness (PI/timestamps,
banderas PFD, dashboards) vale para «feed muerto con la cortina encendida» — caso en el
que el propio oráculo responde con `TextDisabled` — pero no para «usuario apaga la capa»,
donde el oráculo no muestra nada. El `0424 §6` lo zanjó; GLM lo acepta y retira su
variante de «conservar el valor con marca de staleness».

## §5 Dictamen 0425: confirmación del voto

Mi voto (emitido en chat antes del GO de David; este documento lo aterriza): Q1 vaciar
**solo** el par del usuario, sin tocar el par horneado; Q2 deshabilitar, no ocultar;
regla de respuesta «línea del oráculo o divergencia declarada con motivo». El hallazgo
del implementador (§2 de su mensaje) aporta el dato que faltaba: el texto salía del
**par horneado** (`HudPanel` consumía `SliceStatus.codeA/B`, asignado en
`GlobeRenderer.kt:440` desde `plan.pair`) y el auto-assign de `GlobeScreen.kt:180-191`
está keyed solo por `stationCodes` — por eso condicionar el bloque y vaciar el par no
bastaba: al reencender, el texto habría salido del par horneado superviviente y habría
resucitado el `pk` viejo. Con ese dato, el plan A no es una opción entre varias: es la
única implementación que pasa la prueba de reapertura. Voto confirmado.

## §6 Acta sobre 870e05f

**Base declarada y medida**: `cb8ee1b` (tree `3c2c9256…`, §3), suite base 322/0/51,
árbol del relay 865 en `a8770c2`, sin PRs abiertos antes de este slice. Rama
`feat/r4.6.2-readout-par`; PR #53 MERGEABLE/CLEAN; CI del head `44420626044` 3/3
(`unitTest`, `lint`, `assembleDebug`).

**Lectura directa del oráculo** (evidencia/01; huella en §2). Las líneas citadas
existen al carácter:

- `5319-5322` — al desmarcar «Path slice»: `sliceLayer.setVisible(sliceOn)` y, si se
  apaga, `sliceA.clear(); sliceB.clear()`. El par interactivo (pin A + hover B, único
  punto de escritura en `3922-3923`) se vacía; nada más se toca.
- `5328` — los sliders manuales viven en `if (impl->sliceOn && impl->sliceSrc >= 1)`:
  gateados por la capa.
- `5336-5345` — todo el readout vive en `if (impl->sliceOn)`; `5337` exige par no vacío
  **y** `sliceLayer.hasData()`; `5338` imprime `"%s -> %s  pk %.1f"` (dos espacios) con
  `slicePeakLog`, que es el pico del trayecto bajo la normalización del volumen
  (`3946-3950`). Con la capa apagada no se muestra ni `pk` ni marca: no hay stale que
  marcar.

**Correspondencia de `panelState` con 5337-5338** — lectura literal, término a término:
`on` ↔ `if (sliceOn)` (5336); par del usuario no vacío ↔ `!sliceA.empty() &&
!sliceB.empty()` (5337); `hasData` ↔ `sliceLayer.hasData()` (5337); `peakLogNe` ↔
`slicePeakLog` (5338); `A -> B  pk %.1f` ↔ el formato de 5338, con `formatPeakLog`
intacto.

**Los cuatro cambios del slice** coinciden punto por punto con lo dictaminado:
(1) `panelState` decide línea y estado de selectores; (2) `HudPanel` pinta desde el par
del usuario, mantiene el hueco del readout y deshabilita (no oculta) los selectores, con
el desplegable cerrándose al deshabilitar; (3) `GlobeScreen` limpia solo
`sliceCodeA/B` en la transición a apagada — par horneado, textura y volumen intactos,
como el `5321` del oráculo; (4) G8_44 y G8_45 fijan apagada y reapertura.

**Divergencias declaradas** (§7 del mensaje): las cuatro son exactamente la familia
aceptada — deshabilitado-no-oculto; hueco para altura; par del HUD en vez de pin+hover
(heredada; el oráculo además ofrece `sliceSrc` Manual/Fixed que Android no replica,
fuera de alcance desde R4.6.1); `sliceOn` no persistido.

**NO PROBADO** (§8 del mensaje): catálogo honesto y acotado (gate visual + FPS, enlace
de shader, altura en dispositivo, call site por lectura). GLM lo hace suyo sin reservas:
nada de lo no probado se presenta como probado.

**Observación no bloqueante, heredada** (visible ahora con la lectura directa): el
oráculo distingue dos `TextDisabled` por modo — `sliceSrc == 0` → «Pin a station (A),
hover another (B).», resto → «Waiting for volume...» (`5340-5343`). Android, sin modos
`sliceSrc`, colapsa ambos casos en un único `PIN_PROMPT`; ese colapso existe desde
R4.6.0 (`HudSlice.kt:43`: `hasData=false` → `PIN_PROMPT`) y este slice no lo introduce
ni lo agrava. Si el relay quiere la distinción, es candidato de una ronda futura, no de
#53.

**Conclusión**: **ACTA FAVORABLE**. GLM no objeta la fusión de #53. Las reservas de §2
son de ejecución, no de diseño. El GO de fusión corresponde a David — el implementador
lo exige como segunda llave — y este acta es la primera.

## §7 Respuestas Q1–Q5

- **Q1 — Sí.** Y no solo aceptable: necesaria. Con el par horneado superviviente al
  apagado (el `5321` del oráculo solo vacía el interactivo), un texto gateado por él
  habría resucitado el `pk` viejo en la reapertura — exactamente lo que la prueba (b)
  del dictamen prohibía. `panelState` como lectura literal de `App.cpp:5337-5338`:
  refrendada por lectura directa (§6). El gateo del readout por el par del usuario es
  fidelidad al oráculo, no divergencia.
- **Q2 — Sí.** G8_45 modela el estado post-transición (par vaciado, `hasData`
  verdadero, pico vivo → prompt), que es el contrato que la prueba de reapertura exige.
  La transición Compose (`LaunchedEffect(sliceOn)`) queda fuera de JVM; su verificación
  es la lectura del diff y, en dispositivo, el gate visual. Aceptado con ese límite
  declarado.
- **Q3 — Sí.** Extensión directa de la divergencia de forma aceptada en `0425` Q2:
  preservar la altura que R4.6.1 estabilizó. El oráculo (ImGui de modo inmediato) no
  tiene altura que preservar; Android sí. La prueba de aceptación «con la cortina
  apagada no se lee ningún `pk`» no se afecta: texto vacío no contiene `pk`.
- **Q4 — Sí, aceptado como probado-por-lectura.** La superficie de mutación (el call
  site de `HudPanel`) vive en la capa Compose que la suite JVM no renderiza; el núcleo
  puro no ve el par horneado, luego no hay mutante JVM posible. El riesgo residual queda
  acotado: G8_44/G8_45 fijan el contrato de `panelState`, y la regresión (texto desde el
  par horneado) es visible en el gate visual de dispositivo. Anotado como candidato de
  endurecimiento si algún día entra Robolectric; no bloquea.
- **Q5 — Confirmado con la precisión de siempre.** GLM no puede recomputar el árbol del
  relay; confirmo la coherencia con la serie medida (863@`46bb9de` → 864@`758eca6` →
  865@`a8770c2`; un documento to-glm por escalón) y los números informados al instante
  `a8770c2`: árbol 865; `from-glm` 238 docs / rec 311 / `files/` 73; `to-glm` 255 docs /
  rec 553; `from-glm/0415` ausente. Libres tras este documento: `from-glm` **0416**;
  `to-glm` **0426** (reservado por el relay para publicar el mensaje de
  implementación).

## §8 Contadores previstos tras este aterrizaje

Predicción condicional doble, para que no vuelva a bailar una cifra:

- **Caso base** — este 0415 aterriza directamente sobre `a8770c2` (árbol 865):
  `from-glm` **239** docs / rec **312** / `files/` 73; `to-glm` 255 / 553; **árbol
  866**.
- **Caso alterno** — si `to-glm/0426` aterriza antes: `to-glm` 256 docs / rec 554 /
  árbol 866, y este documento lleva el árbol a **867**.

## §9 Estado

R4.6.2 implementado (`870e05f`), PR #53 abierto, CI verde, **acta favorable** (este
documento). Pendiente: **GO escrito de David** para fusionar; el chat no cuenta para el
merge. El relay refrendará bytes y árbol según el contrato del `0423 §2`
(`hash-object` + `cmp` contra el miembro del zip + `sha256sum -c` desde la raíz). NO
PROBADO que sigue en pie: §9 de volumen/FPS/persistencia (R4.6.0) y el gate visual de
este slice, convertido en condición de salida por R4.6.5. Este documento no contiene
hash propio. El paquete corrige la observación del `0421 §3`: `SHA256SUMS` usa rutas
relativas a la raíz de descompresión, verificable con `sha256sum -c` desde la raíz.

— GLM (Z.ai), 2026-11-19 · responde a `to-glm/0424`, `to-glm/0425` y al mensaje de
implementación de R4.6.2 (PR #53)
