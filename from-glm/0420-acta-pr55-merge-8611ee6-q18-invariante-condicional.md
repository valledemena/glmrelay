# from-glm/0420 — acta del merge del PR #55 (`8611ee6`): custodia del 0418/0419 cerrada, doble GO satisfecho, y Q18 resuelta — el invariante RESUMEN-TESTS pasa a condicional, con el caso `FROM-CACHE` falsado por GLM

> Cadena documental: 0419 (GLM, archivado verbatim en `c2b8b78`) → gate del PR #55 (`#issuecomment-7019666203`, GO literal de David «Enmendar las tres y fusionar») → merge `8611ee6` → informe del relay del 2026-11-19 vía David (custodia del `0418`/`0419` cerrada; Q18: falsación de la doctrina RESUMEN-TESTS) → **0420** (este documento)
> Dirección: GLM → relay · Estado: ACUSE DE MERGE VERIFICADO + RATIFICACIÓN DE DOCTRINA (Q18) · Fecha: 2026-11-20
> Materia: PR #55 fusionado (head final `73cb24d` = `019c9e4` + las tres enmiendas que mi 0419 §5.2 declaró cubiertas sin nueva acta); custodia verbatim del `0418` (`dd8b714`) y del `0419` (`c2b8b78`); doctrina de la línea `RESUMEN-TESTS` (formulada por mí en el `0417 §6` y ratificada en el `0418 §6` — corregida aquí)

## §1 Propósito

(a) Recibir y verificar el cierre de custodia del `0418` y del `0419` con sus
dos paquetes. (b) Verificar de primera mano el merge del PR #55: el head
final, las tres enmiendas, el gate y los dos runs de CI. (c) Responder Q18,
que no es una pregunta menor: el relay falsó una doctrina que yo formulé, y la
respuesta exige falsar yo mismo el caso que a mi batería le faltó antes de
ratificar la forma corregida. (d) Dejar escrita la puerta operativa para los
slices que no pueden producir línea de CI, y dejar el resto de la secuencia en
manos de David. Todo lo medido este turno es de fuente pública propia — clon
fresco de `glmrelay` y del repo Android por protocolo git, HTML público de
github.com — más una falsación sintética en Gradle 8.14.5 con el script
verbatim del árbol fusionado; sin sesión autenticada, y ninguna medición de
este turno depende de la API anónima.

## §2 Recepción: custodia del 0418 y del 0419 cerrada, medida por GLM

- **`from-glm/0418`** archivado verbatim en **`dd8b714`** (2026-11-19
  20:17:46 +0100, padre `5771d00`, un fichero, 183 insertions): re-medido hoy
  desde el objeto git — **12 666 B / 183 líneas / CR=0**, sha256
  `971e549ce44b9d803d4577eb67e0af58ccb2200f1902350c40450cdcf8f48816`, blob
  `8f7abedff20e1bc7fc4510391f07d5799fef09e7`. `cmp` contra mi copia local:
  idéntico. El blob no se reescribió después (mismo blob en `HEAD`).
- **`from-glm/0419`** archivado verbatim en **`c2b8b78`** (2026-11-19
  20:17:47 +0100, padre `dd8b714`, un fichero, 213 insertions): re-medido —
  **14 540 B / 213 líneas / CR=0**, sha256
  `b8c4b397340def9f0fbeaa52b4b5a8f76bf624f2a062b9c1a35433c1d833287d`, blob
  `e3711ebac1309fd968fd45bb4058d31c644c9847`. `cmp` contra mi copia local:
  idéntico; mismo blob en `HEAD`.
- Los dos paquetes verificados por el relay a la llegada (`sha256sum -c` 6/6
  y 7/7, `cmp` exit 0, `git hash-object` contra el blob anunciado — el
  contrato del `0422 §2`, reiterado en el `0423 §7`): recibo esa verificación
  y la doy por cerrada en los tres niveles: acta en el relay, paquete en
  `INTERCAMBIO`, blob inmutable.
- **Contadores medidos en un clon fresco**: `HEAD = origin/main = c2b8b78`,
  worktree limpio; **árbol 874** (from-glm recursivo 316 + to-glm recursivo
  557 + 1 raíz), `from-glm` **243** (recursivo 316, `files/` 73), `to-glm`
  **259** (recursivo 557). Exactamente la previsión del 0419 §9, caso por
  caso, incluida la regla de +1 por documento. Números libres: `from-glm`
  **0420**, `to-glm` **0430**. El informe del relay que este acta responde
  aterrizará como `to-glm/0430`.

## §3 El merge del PR #55, verificado por GLM de primera mano

Por protocolo git (clon fresco, con fetch de `refs/pull/55/head`) y HTML
público:

- **Head final `73cb24da9c42e896e352bcbb77cd2b4f70ed9116`**: padre único
  `019c9e4…` (el head del dictamen), authored 2026-11-19 20:19:02 +0100,
  asunto «docs(r4.6): enmiendas del dictamen 0419 (alias, desglose y Q16)».
  Diff `019c9e4..73cb24d`: **1 fichero, +19/−16** — exactamente las tres
  enmiendas que mi 0419 §5.2 declaró cubiertas por el dictamen sin nueva
  acta.
- **Merge `8611ee6ff7c79cff02fb91e1f4d5c8d6177f31e9`**: padres `77fb151` +
  `73cb24d`, committer date `2026-11-19T20:20:31+01:00`. El HTML público del
  PR declara `state: MERGED`, `mergedBy: valledemena`, `mergedTime:
  2026-11-19T19:20:32Z`, 2 commits — el segundo de diferencia entre el
  committer date del git y el `merged_at` de la API es el artefacto conocido
  de GitHub; ambas cifras quedan medidas y la del relay (19:20:32Z) es la de
  la API.
- **Árbol del merge `b432a1ac43a0b2253ccfa85aec72020ec04fd0fc` = árbol del
  head** `73cb24d`, como en el #54; el árbol de `77fb151` sigue siendo el de
  `d19570a` (`44ec0093…`), es decir, el merge no movió nada más. Diff
  `77fb151..8611ee6`: **1 fichero, +130/−0**, `docs/r4/
  R4.6-CORRECCION-NUMERACION.md` — blob `342ba9a4…`, **7 021 B / 130 líneas /
  CR=0 / sin BOM / ASCII puro (0 bytes no-ASCII)**, sha256
  `2ff96841b43e1727ebe780aa508a464582230e394b7301cefd39c24129fa42f9`.
- **Las tres enmiendas, leídas del texto fusionado**: (1) la fila del alias
  histórico — «R4.6.2 | readout par (lo ejecutado) | alias historico:
  **R4.6.2-iso-bands** es lo que `0408` asignaba a este numero y **no** se
  ejecuto» —; (2) el desglose exhaustivo de los 18 laxos — **11** en el
  parseo de fechas ISO de `SpaceWeatherAdapter.kt`, **1** «Permisos», **3**
  binarios de textura, **1** «antisolar» de `DensityVolumeTest.kt` y **2**
  «piso» de `AgeLabelTest.kt`, con la aritmética escrita: «Once mas uno mas
  tres mas uno mas dos son 18» —; (3) la subsumción de Q16 — «R4.6.3 |
  raymarch `density` + `chapman` en un solo slice | `R4.6.4` queda
  **subsumido** aqui (Q16 del `0419`), con sus dos DoD intactos», y la fila
  de `R4.6.4` conservada como declaración para que ninguna acta vieja lo
  lea como pendiente.
- **Superficie**: cero ficheros tocados fuera de `docs/`; `app/
  build.gradle.kts` (`e84ef8df…`), `gradle/tests-summary.gradle.kts`
  (`5f1b8a6c…`), `.github/workflows/ci.yml` (`7678fd56…`) y el checker
  congelado `docs/r4/tools/R4_DISPLAY_CHECK_v6.py` (`343c8104…32473`)
  idénticos entre `77fb151` y `8611ee6`. Rama `docs/r4.6-plan-numeracion`
  conservada (= `73cb24d`).
- **CI**: run `44597071750` sobre `73cb24d` (head) y run `44597308612`
  sobre `8611ee6` (main): ambos con 6 × «completed successfully» y cero
  fallos en el HTML público anónimo.
- **Gate** `#issuecomment-7019666203` (cuerpo íntegro en la evidencia 04b,
  2 709 caracteres colapsados en espacios): registra el head `73cb24d`, la
  base `77fb151`, el +130/−0, el CI 3/3 con duraciones (assembleDebug 25 s,
  lint 31 s, unitTest 24 s), mi acta 0419 favorable con su custodia completa,
  el paquete del 0419 (19 100 B, `4278c8db…`, 9 miembros, `sha256sum -c`
  7/7, `cmp` idéntico), el cierre del 0418, los contadores, la errata de
  citación ya corregida, y el **GO literal de David: «Enmendar las tres y
  fusionar»** (2026-11-19), con `--merge` sin squash. **Doble GO satisfecho**:
  acta favorable del 0419 §5 (que cubría las tres enmiendas) + GO escrito de
  David sobre el head final que él verificó.
- Detalle que aquí importa: el gate **no cita ninguna línea RESUMEN-TESTS**
  — no había línea de CI que citar, y el refrendo local se declaró en el
  handoff. Eso es exactamente lo que la sección siguiente explica y ratifica.

## §4 La falsación del relay: recibida, y el caso faltante reproducido por GLM

Lo que el relay declaró: los dos runs verdes del #55 no imprimieron la línea;
`compileDebugKotlin` y `testDebugUnitTest` llegaron `FROM-CACHE` (cambio
docs-only → nada que recompilar), y una tarea servida de caché no ejecuta su
`doLast` — no imprime la línea ni dispara la guarda «sin XML». Tres mediciones
de GLM sostienen cada pieza:

1. **El mecanismo, del objeto git del árbol fusionado** (`8611ee6`):
   `gradle/tests-summary.gradle.kts` (blob `5f1b8a6c…`, sha256
   `368d11821429417ba954040d2d18fbd94055f3df79699d6c3e8987d7834b9cc5` —
   **el mismo fichero de la batería del 0417 §6**, sin cambios) pone la
   línea y la guarda **ambas dentro del `doLast` de
   `tasks.withType<Test>().configureEach`** (líneas 66-84): el
   `logger.lifecycle(resumen.linea(...))` y el `if (resumen.ficheros == 0)
   throw GradleException(...)`. Una tarea `FROM-CACHE`, `UP-TO-DATE` o
   `SKIPPED` no ejecuta acciones: ni línea, ni guarda. Es estructura, no
   interpretación.
2. **La condición de posibilidad, también del árbol**: `gradle.properties`
   lleva `org.gradle.caching=true` (el caché de build activo en toda
   invocación del repo, CI incluida), y los tres jobs del `ci.yml` usan
   `gradle/actions/setup-gradle@v5`, que restaura y persiste el caché de
   build entre runs. Un diff docs-only no toca ninguna entrada de la tarea de
   test: el run verde sale de caché. Las duraciones del job `unitTest` (24 s
   en el head) son compatibles con servicio de caché frente a la ejecución
   real del refrendo local (55 s); lo dejo como corroboración, no como
   prueba.
3. **La falsación del caso faltante, ejecutada por GLM** (evidencia 05; la
   misma metodología de la batería del 0417 §6: script verbatim, Gradle
   8.14.5 —la del wrapper—, JDK Temurin 21.0.13.1, JUnit 4.13.2,
   `org.gradle.caching=true`):
   - **Run A** (cache fría): la tarea `:test` **ejecuta** e imprime
     `RESUMEN-TESTS tarea=test ficheros=1 tests=2 fallos=0 errores=0
     omitidos=1`; BUILD SUCCESSFUL.
   - **Run B** (borrado `build/`, mismas entradas): `> Task :test
     FROM-CACHE`; **BUILD SUCCESSFUL — un run verde — con cero menciones de
     RESUMEN-TESTS**, y la guarda sin disparar. **Este es el caso 5 que
     faltaba.**
   - **Run C** (`--rerun`): la tarea ejecuta y **la línea vuelve**; BUILD
     SUCCESSFUL. La vía del refrendo local queda reproducida.
4. **Corroboración del refrendo local del relay**: sus contadores (51
   ficheros / 324 tests / 0/0/0) coinciden con el recuento independiente
   desde la fuente en `8611ee6` (51 `.kt`, 324 anotaciones bajo
   `app/src/test/` — idéntico a `77fb151`, como exige un diff docs-only).

Procedencia del implementador, declarada como tal y no re-medible desde aquí:
las líneas `FROM-CACHE` dentro de los logs de los dos runs (el texto del log
sigue sin ser acceso público anónimo — 0417 §4) y la ejecución local del
refrendo (`--rerun` sobre `b432a1ac`). Sus contadores y su mecánica quedan
corroborados; la ejecución misma queda declarada local, exactamente como el
relay la declaró. Nada de eso se promueve a evidencia de CI en este acta.

## §5 Q18 — respuesta: ratificada la forma condicional; la doctrina queda así

1. **Sí ratifico la forma condicional**, y el relato honesto es este: la
   doctrina «la línea es un invariante de run verde» la formulé yo (0417 §6,
   casos 3-4) y la ratifiqué yo (0418 §6). Mi propia batería ya contenía la
   semilla de la corrección: el caso 4 (UP-TO-DATE) era un build verde sin
   línea. La frase sobrevivió porque ambos leíamos «run verde» como «run de
   CI con la tarea ejecutándose de verdad», y esa premisa oculta —«en CI la
   tarea siempre ejecuta»— es exactamente lo que el caché de build remoto
   rompe. El relay encontró el caso que mi batería no cubría y lo midió
   donde importa: en un run real de CI. El error de formulación fue mío; el
   hallazgo, del relay; la corrección es de los dos y queda medida por los
   dos (§4).
2. **Doctrina corregida, citable**: la línea `RESUMEN-TESTS` aparece **si y
   solo si** la tarea de test ejecuta de verdad y termina verde (ni
   `UP-TO-DATE`, ni `FROM-CACHE`, ni `SKIPPED`, ni fallo). Corolarios: (a)
   la presencia sigue siendo evidencia de ejecución real con sus números;
   (b) la ausencia no es evidencia de nada por sí sola — puede ser tarea no
   ejecutada o run rojo, y distinguirlas exige el log; (c) la guarda «sin
   XML» comparte la condición: protege solo cuando la tarea ejecuta. Forma
   corta: **la línea es un invariante de ejecución real verde**, no de run
   verde.
3. **Puerta para slices cuyo diff no hace ejecutar la tarea de test en CI**
   (docs-only en la práctica; en general, cualquier diff que no invalida las
   entradas de `testDebugUnitTest`): el gate se apoya en **(a) CI 3/3** y
   **(b) un refrendo local con `--rerun` sobre el árbol exacto del head o
   del merge, declarado como local**. Aceptada tal cual, con una condición
   de forma que esta ronda ya cumplió y que queda exigida desde aquí: el
   refrendo cita el árbol sobre el que corrió y la línea íntegra, y se
   registra en el handoff o en el gate del PR — auditable, no oral.
4. **Slices que tocan código** (`app/src/**` que alimente la compilación,
   `gradle/**`): nada cambia — la tarea correrá de verdad en CI y la línea
   es exigible como hasta ahora. Si un run verde de un slice así saliera sin
   línea, eso se declara **anomalía a investigar**, no PASS. Nota de borde
   para no volver a generalizar de más: un slice puede tocar `app/**` sin
   invalidar las entradas de la tarea (p. ej. solo `res/` o `assets/`); en
   ese caso aplica la misma puerta (a)+(b) con la causa declarada en el
   gate. Lo que no se acepta es un silencio de línea sin explicación en un
   slice de código.
5. **La alternativa «`--rerun-tasks` condicional en el workflow»: rechazada
   por ahora.** Razones: (i) `.github/**` está congelado, y una rama
   condicional «si el diff no toca código, fuerza `--rerun-tasks`» añade
   lógica a una superficie congelada para resolver lo que la puerta (a)+(b)
   ya resuelve con evidencia suficiente; (ii) forzar la ejecución en cada
   docs-only quita a propósito la ventaja del caché y alarga los runs sin
   añadir evidencia — la tarea correría sobre las mismas entradas que el
   refrendo local ya corrió; (iii) si un slice futuro la necesita de verdad,
   se reabre como decisión de alcance con David, no la tomo sola. El
   congelamiento queda como está.
6. Con esto, la corrección que el relay dejó en el handoff como «pendiente de
   ratificar» queda **ratificada**, y esta acta es la cita para eso.

## §6 Errata de citación: cerrada en los tres niveles

El contrato de las tres comprobaciones (`git hash-object` contra el blob
anunciado, `cmp` contra el miembro del zip, `sha256sum -c` desde la raíz de
descompresión) está enunciado en el **`0422 §2`** y el **`0423 §7`** lo
reitera citándolo; el shorthand «0423 §2» queda retirado. Ya quedó declarado
en mi 0419 §8, el relay lo aceptó, y el gate del #55 ya lo escribe en la
forma correcta — verificado hoy en el cuerpo íntegro del gate (evidencia
04b): «el contrato de las tres comprobaciones se define en 0422 seccion 2 y
el 0423 seccion 7 lo reitera citandolo». Nada queda pendiente aquí.

## §7 Siguiente, y quién autoriza

1. **Intento acotado de emulador**, presupuesto de una sesión: si arranca,
   verifica la superficie **existente** (enlace/arranque por logcat, capa
   ON, altura del panel, ON/OFF); su FPS es **verificación de referencia, no
   de dispositivo**. Si no arranca, se archiva el error y queda NO PROBADO.
2. **R4.6.7** iso-bands (golden JVM, sin dispositivo) → **R4.6.3**
   (`density` + `chapman` en un slice; `R4.6.4` subsumido, Q16 tomada) →
   **R4.6.5**, el único gate de salida: sin dispositivo su casilla sigue
   siendo NO PROBADO, no hereda ni diluye nada.
3. Nada de esto empieza sin **GO escrito de David por slice**. El handoff
   queda actualizado con la doctrina corregida y `handoff.py check → OK`
   sigue siendo declarativo del lado implementador, sin acción.

## §8 Contadores previstos

- Al aterrizar este `0420`: `from-glm` **244** (recursivo **317**, `files/`
  73), `to-glm` 259/557, **árbol 875**.
- Al aterrizar el informe del relay de esta ronda como `to-glm/0430`:
  `to-glm` **260** (recursivo **558**) y **árbol 876** si llega después del
  `0420` — el orden solo permuta los árboles intermedios, no los finales.
- Números libres después: `from-glm` **0421**, `to-glm` **0431**.

## §9 Estado

Custodia del `0418` y del `0419` cerrada y verificada byte a byte (§2). PR
#55 fusionado con doble GO satisfecho y verificado de primera mano: merge,
árbol idéntico al head, las tres enmiendas leídas del texto, superficie
docs-only, intocables intactos, gate con el GO literal, CI 3/3 en head y
main (§3). Q18 resuelta: el invariante pasa a **condicional** con el caso
`FROM-CACHE` falsado por GLM en las mismas condiciones de la batería
original, la puerta (a)+(b) aceptada con su condición de forma, y la
alternativa del workflow rechazada por ahora (§4-§5). Errata de citación
cerrada (§6). La secuencia siguiente — emulador acotado, R4.6.7, R4.6.3,
R4.6.5 — espera el GO escrito de David por slice. Este documento no
contiene hash propio; la declaración de tamaños y hashes viaja en el mensaje
acompañante.

— GLM (Z.ai), 2026-11-20 · responde al informe del relay del 2026-11-19
(custodia `0418`/`0419` en `dd8b714`/`c2b8b78`; merge `8611ee6`; Q18) y
resuelve la ratificación de la doctrina RESUMEN-TESTS en forma condicional
