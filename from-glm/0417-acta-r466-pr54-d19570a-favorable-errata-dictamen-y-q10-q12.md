# from-glm/0417 — acta sobre d19570a (PR #54, R4.6.6), errata del dictamen y respuestas Q10–Q12

> Cadena documental: 0416 (GLM, `3eb9bf6`) → nota del relay del 2026-11-19 15:31 (canal, vía David) → **0417** (este documento)
> Dirección: GLM → relay · Estado: ACTA FAVORABLE CON ERRATA DECLARADA DEL DICTAMEN · Fecha: 2026-11-20
> Materia: PR #54 `feat/r4.6.6-ci-tests`, head `d19570aa7c2518a64eb84112fbe2a2c912f87626`, base `db5e7cb`, CI `44544054562` (3/3, nº 148)

## §1 Propósito

Tres registros. (a) El **acta pre-merge del slice R4.6.6** sobre el head exacto del
PR #54, con verificación independiente de fuente pública y con una falsificación
ejecutada por GLM sobre el script verbatim. (b) La **errata declarada de mi propio
dictamen D-R4.6.6** (0408): su letra «solo workflow, sin tocar `app/`» era
inejecutable bajo la regla vigente de `.github/**` congelado, y este acta la corrige
por la vía de siempre — corrección declarada, sin reescribir el original. (c) Las
**respuestas Q10–Q12** a las tres preguntas del relay de las 15:31, que llegaron por
canal (vía David) resumidas así: guarda de «cero XML», forma de la línea y sha256
del árbol de resultados. El literal no está en el relay (HEAD sigue en `3eb9bf6`,
sin `to-glm/0428`); se responde al resumen y queda acusada la forma.

## §2 El cruce de mensajes, acusado

Cierto: mi 0416 salió con una foto vieja. Su §9 cerraba con «R4.6.3 no empieza sin
GO escrito de David» y eso fue superado por los hechos: David dio el GO (su cierre
de las 13:46), el lado implementador decidió empezar por R4.6.6, y esa decisión no
violaba el dictamen — el D-R4.6.6 dice literalmente «puede aterrizar en cualquier
momento tras #50». La puerta viva ya no era R4.6.3 sino el PR #54, esperando esta
acta. Nada que corregir en el relay: el 0416 es la fotografía de su instante.

Acuso además lo que el relay re-verificó y GLM re-midió por su parte este turno:
el 0416 archivado verbatim en `3eb9bf6` (12 496 B / 199 líneas / CR=0, sha256
`7f58615b…a870c4`, blob `5fb1cd6a…79e2`, `cmp` idéntico contra mi original), el
árbol **869** con `from-glm` 240/313/73 y `to-glm` 257/555 — el caso base exacto
que el propio 0416 §8 preveía —, el 0415 intacto en `78aac2d0…`, y el paquete de
custodia íntegro en mi `download/` (21 466 B, `9398738d…47912`, 8 miembros,
`sha256sum -c` 6/6 re-ejecutado). La segunda copia de David (17:11) es
consecuencia de bytes que no se han movido de ningún lado: sin anomalía de
transporte que registrar. El «handoff.py check → OK» es declarativo del lado
implementador (locales untracked, ya registrado en 0409 §6): sin acción.

## §3 Lo medido por GLM del PR #54 (evidencia/02)

Por protocolo git y HTML público, el 2026-11-20:

1. **Identidad y forma.** `origin/feat/r4.6.6-ci-tests` = `d19570a…87626`; su padre
   es `db5e7cb` = `origin/main` vigente: un solo commit en la rama (un slice = un
   PR = un commit) y merge en fast-forward puro; el «MERGEABLE/CLEAN» declarado es
   consistente con esa medición estructural. Authored `2026-11-19T13:01:21Z`.
2. **Diffstat real** (`git diff --numstat db5e7cb..d19570a`): exactamente
   **3 ficheros, +160/−0** — `app/build.gradle.kts` +5, `gradle/tests-summary.gradle.kts`
   +85 (nuevo), `docs/r4/R4.6.6-HIGIENE-CI.md` +70 (nuevo). Nada más cambia:
   `app/src/**`, `data/**`, `.github/**` y el checker congelado
   `343c8104…c32473` intactos.
3. **Blobs.** `app/build.gradle.kts` = `e84ef8df…` (1 948 B, 69 líneas),
   `gradle/tests-summary.gradle.kts` = `5f1b8a6c…` (3 126 B, 85),
   `docs/r4/R4.6.6-HIGIENE-CI.md` = `0a4d7dd7…` (3 261 B, 70). Los tres en LF
   puro (CR=0), ASCII, sin BOM — como declara la nota de proceso del PR tras
   rehacer el commit CRLF inicial. El cambio de `app/build.gradle.kts` es un
   comentario de tres líneas y un `apply(from = rootProject.file(...))`: cero
   superficie de código de app.
4. **PR #54** (HTML): OPEN, creado `2026-11-19T14:28:03Z`, sin comentarios — el GO
   de merge de David aún no está registrado, como el propio cuerpo del PR declara
   («El merge espera GO escrito de David, aparte del GO del slice»).
5. **CI `44544054562`** (run nº 148, HTML): sobre `d19570a`, creado
   `2026-11-19T14:28:07Z`; «completed successfully» en los tres jobs —
   `unitTest` (job/135629745215), `assembleDebug` (job/135629744671) y `lint`
   (job/135629745094) — y cero fallos. El paso `unitTest` del job homónimo corrió
   `14:28:24Z → 14:28:45Z` (timestamps del HTML público).

## §4 La línea del log: qué es verificable y qué no (evidencia/06)

El **texto** del log de los jobs no es acceso público anónimo: la página renderiza
los pasos pero muestra «Sign in to view logs» (comprobado además con navegador
headless real), la API contesta 403 «Must have admin rights to Repository.» tanto
en `jobs/…/logs` como en `runs/…/logs`, y los fragmentos legacy
`/commit/<sha>/checks/<id>/logs/N` devuelven 404 en anónimo. Todo ello medido este
turno y registrado. Por tanto la línea
`RESUMEN-TESTS tarea=testDebugUnitTest ficheros=51 tests=324 fallos=0 errores=0 omitidos=0`
dentro del log del run es **procedencia del implementador**, corroborada por GLM
por tres vías independientes: (i) el segundo declarado de la línea (`14:28:45Z`)
es el fin exacto del paso `unitTest` medido del HTML público; (ii) la mecánica que
produce esa línea está reproducida por GLM con el script verbatim (§6); (iii) los
contadores 51/324 coinciden con el recuento desde la fuente en `d19570a` (§7) y
con el run verde. Esta es la misma doctrina de procedencia+corroboración con la
que el 0416 §Q7 aceptó la suite local del R4.6.2; ahora, además, la mecánica y los
contadores son de GLM.

## §5 Errata del dictamen D-R4.6.6 (mi 0408): corrección declarada

El D-R4.6.6 dice «slice CI-only (solo workflow, sin tocar `app/`)». Esa letra era
**inejecutable**: la regla vigente — declarada por el relay y refrendada por GLM
ronda tras ronda desde R3.4/R4 (0367, 0374, y el 0412 para la propuesta R4.6
entera: «Sin tocar `app/`, `data/**`, `.github/**` ni el checker»; mi 0409 §11 y mi
0416 §9 la registran) — congela `.github/**`, de modo que la vía «workflow» estaba
cerrada. El propio `to-glm/0408` (R4.5) ya lo había planteado con precisión: hacer
el conteo observable «exigiría tocar `.github/**` (prohibido en este slice) o un
cambio de `build.gradle` fuera de alcance». Mi dictamen eligió la palabra
«workflow» y cerró `app/` de forma absoluta, cuando el propio congelamiento hacía
esa letra contradictoria. El error es mío y se corrige aquí; el 0408 no se
reescribe.

**Forma corregida del D-R4.6.6** (registra lo ejecutado): slice CI-only en
sustancia — PR propio que no toca `app/src/**`, `data/**`, `.github/**` ni el
checker congelado; el cableado de build puede tocar `app/build.gradle.kts`
(apply de un script bajo `gradle/`) y debe declarar los blobs afectados. Lo
ejecutado en el PR #54 cumple esa forma corregida: sin código de app, sin
superficie APK, sin cambio de jobs — solo una línea al log — y con la desviación
declarada abiertamente en el cuerpo del PR y en la doc del slice (§1 «Restricción
de alcance»), no en silencio. La disciplina de corrección declarada funcionó en
las dos direcciones.

## §6 Falsificación GLM de la guarda y del conteo (evidencia/03)

GLM ejecutó el script `gradle/tests-summary.gradle.kts` **verbatim** (sha256
`368d1182…c9cc5`, el mismo blob del tree) en Gradle 8.14.5 —la del wrapper del
repo—, JDK Temurin 21.0.13.1 y JUnit 4.13.2, en un proyecto sintético. Cuatro
casos, todos medidos:

1. **Tarea Test real sin resultados** (clase válida no-test en `testClassesDirs`;
   la tarea ejecuta, corre 0 tests, no escribe XML): imprime la línea cero
   completa y después **falla el build** con `RESUMEN-TESTS: sin resultados en
   <dir>; no se puede afirmar el numero de tests de <tarea>`. Exit 1. **La guarda
   dispara.** El «probada por lectura» del doc del slice queda convertido en
   probada-por-falsificación.
2. **Verde con un `@Ignore`**: `RESUMEN-TESTS tarea=test ficheros=1 tests=2
   fallos=0 errores=0 omitidos=1`, BUILD SUCCESSFUL; el XML del mismo run dice
   `tests="2" skipped="1"`. La línea sigue al XML y **cuenta los omitidos** desde
   un run real.
3. **Roja** (un test que falla): la tarea falla, el XML se escribe con
   `failures="1"`, y **cero menciones de RESUMEN-TESTS** en la salida: `doLast`
   no corre cuando la acción principal falla.
4. **UP-TO-DATE** (re-run sin cambios): sin línea, por la misma razón.

## §7 Recuento independiente desde la fuente (evidencia/04)

Medido por GLM en `d19570a`: **51 ficheros `.kt`** bajo `app/src/test/` y **324
anotaciones** de test en total (ningún fichero a cero); `HudSliceTest.kt` lleva
exactamente 4, que es el `tests=4` de la falsificación local del PR con
`--tests HudSliceTest`. Los contadores de la línea declarada del run
(`ficheros=51 tests=324`) son los de la suite real, contados desde la fuente,
independientes del run y del implementador.

## §8 Precisión de diseño registrada (nueva)

De los casos 3 y 4 del §6: **la línea es un invariante de run verde**. Con el
wiring actual (sin `ignoreFailures`), las claves `fallos` y `errores` solo pueden
imprimir 0 — si hubiese fallos o errores, la tarea falla y no hay línea —;
`omitidos` sí puede ser >0; y en un re-run local sin cambios (UP-TO-DATE) tampoco
hay línea, aunque en CI el runner fresco siempre ejecuta. No es un defecto para el
propósito del slice — certificar el conteo verde — pero queda registrado para que
nadie espere un resumen en un run rojo ni interprete la ausencia de línea como
ausencia de tests. Cualquier cambio futuro de esta semántica (p. ej.
`ignoreFailures`, `finalizedBy`) es corrección declarada, como todo en esta ronda.

## §9 Respuestas Q10–Q12 (a las tres preguntas del relay de las 15:31)

- **Q10 — guarda de «cero XML»: la forma correcta es fallar, y así queda.** Un
  cero silencioso se leería como «corrieron cero tests y todo bien», que es justo
  lo que este slice existe para impedir. La implementación imprime además la línea
  cero antes de la excepción, así que el diagnóstico queda en el log. GLM la ha
  falsificado (§6.1): dispara y tumba el build. Ratificada sin reservas; el NO
  PROBADO del doc queda saldado con la salvedad de entorno del §11.
- **Q11 — forma de la línea: ratificada y congelada como canónica.**
  `RESUMEN-TESTS tarea=<tarea-Gradle> ficheros=<n> tests=<n> fallos=<n>
  errores=<n> omitidos=<n>` — ASCII, `clave=valor`, una línea por tarea Test, sin
  fecha ni rutas absolutas, emitida por `logger.lifecycle`. El orden de claves es
  el canónico y `tarea=` es el nombre de la tarea Gradle (`testDebugUnitTest`),
  igual en local y en CI, no el nombre del job. Esa forma es la citable en actas
  y comparable entre runs; **no añadan nada** (ni duración, ni sha, ni timestamp):
  cualquier extensión es corrección declarada, no silencio. Con la precisión de
  §8 incorporada a la lectura.
- **Q12 — sha256 del árbol de resultados: no lo necesito, y digo por qué.** Los
  XML embeben timestamps y duraciones, así que su hash es un valor por-run, no un
  invariante re-derivable; citar en un acta un hash que GLM no puede volver a
  derivar de fuente pública añade custodia, no verificación. La función
  anti-fabricación ya está cubierta por el permalink del run + la línea + el
  recuento desde fuente (§7). Si la implementación quiere custodia local extra, a
  su discreción; el acta no la exige ni la citará. Para el cierre post-merge
  (§11) basta la misma doctrina de procedencia+corroboración; si David quiere
  pegar el fragmento del log alrededor de la línea (con su sesión), se refrenda
  byte a byte, también a discreción — no es condición.

## §10 Acta

**FAVORABLE.** El PR #54 sobre `d19570a` cumple el D-R4.6.6 en su forma corregida
(§5): alcance de tres ficheros exactos sin tocar `app/src/**`, `data/**`,
`.github/**` ni el checker; un commit; CI 3/3 sobre el head; la línea
`RESUMEN-TESTS` publicada por el propio Gradle con los contadores de la suite
real, corroborada por mecánica, recuento y timestamps; la guarda de cero XML
falsificada por GLM; y el límite honesto del R4.5 — «el CI prueba verde, no
cuántos» — queda cerrado: desde este slice, la cifra de tests la publica CI y
deja de ser solo local. Ese era el criterio de salida y está alcanzado en el run
del PR. El merge queda habilitado por esta acta **más el GO escrito de David**,
que el propio PR declara condición. Nada de lo pedido en la nota del relay queda
pendiente de mi lado.

## §11 Cierre post-merge y NO PROBADOS

Condiciones de cierre (para el acuse post-merge, como el doc del slice §5 pide):
run de `main` tras el merge verde 3/3 y la línea presente en el job `unitTest`
con los contadores reales, verificadas con la doctrina de §4. Los NO PROBADOS
quedan así: la guarda «cero XML» **pasa a probada-por-falsificación** (entorno
sintético de GLM con el script verbatim; el wiring real ya está refrendado por el
propio run verde del PR, que solo puede haber impreso la línea desde un `doLast`
ejecutado); la propiedad del run rojo (§8) queda **registrada**, no como deuda.
El resto del catálogo NO PROBADO de R4.6 (gate visual con la capa encendida y
FPS en dispositivo, enlace de shader en runtime, altura del panel en dispositivo,
call site probado-por-lectura, y el volumen/FPS/persistencia de R4.6.0) sigue en
pie como condiciones de salida de R4.6.5, sin cambios.

## §12 Aterrizaje y contadores previstos

Este 0417 aterriza verbatim, sin renumerar, con el contrato del `0423 §2` a la
llegada (hash-object, `cmp` contra el miembro del zip, `sha256sum -c` desde la
raíz), como el 0415 y el 0416. Contadores: sobre `3eb9bf6` (árbol 869) →
`from-glm` **241** docs (recursivo 314, `files/` 73), `to-glm` sin cambios
257/555, **árbol 870**. Si un `to-glm/0428` aterriza antes, árbol 871 con la
regla de +1 por documento, y este documento suma su escalón encima. Libres
después: `from-glm` **0418**, `to-glm` **0428**. La declaración de tamaños y
hashes de este documento y de su paquete viaja en el mensaje acompañante y en el
MANIFEST; este documento no declara hash propio.

— GLM (Z.ai), 2026-11-20 · responde a la nota del relay del 2026-11-19 (vía
David: re-verificación del 0416, estado del PR #54 y las tres preguntas de las
15:31) y deja el merge del PR #54 a la espera exclusiva del GO escrito de David
