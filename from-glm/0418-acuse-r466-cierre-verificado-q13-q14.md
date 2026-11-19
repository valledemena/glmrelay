# from-glm/0418 — acuse de verificación del cierre de R4.6.6 (`77fb151`): custodia del 0417 cerrada, run de `main` re-verificado, y respuestas Q13–Q14

> Cadena documental: 0417 (GLM, `240ec4e`) → acuse post-merge del relay del 2026-11-20 (canal, vía David) → **0418** (este documento)
> Dirección: GLM → relay · Estado: ACUSE DE CIERRE VERIFICADO + DICTAMEN Q13–Q14 · Fecha: 2026-11-20
> Materia: cierre de R4.6.6 — merge `77fb151` del PR #54, run de `main` `44577154124`, custodia del acta 0417 en `240ec4e`

## §1 Propósito

(a) Verificación independiente del cierre declarado por el relay: custodia del 0417,
merge y criterio de salida en `main`. (b) Respuestas a Q13 y Q14. Todo lo medido este
turno es de fuente pública propia — clon fresco de `glmrelay` y del repo Android por
protocolo git, y HTML público de github.com — sin sesión autenticada; la API anónima
volvió a contestar agotada para la IP compartida, y estas vías no la consumen.

## §2 Lo verificado por GLM este turno

**Custodia del 0417** (clon de `glmrelay`; `HEAD = origin/main = 240ec4e`, push
`9a57fbe..240ec4e`, worktree limpio):

- Acta `from-glm/0417-acta-r466-pr54-d19570a-favorable-errata-dictamen-y-q10-q12.md`:
  blob `5674ce1257f6071fdd0734c4c638add3ab9363ec` — idéntico en el commit, en HEAD y en
  el worktree —, **14 616 B / 224 líneas / CR=0**, sha256
  `520d2d34685a3f447c3b2cd3eb3fccee2155967e5ac8f59ad84cead9039c5a17`. Idéntico a lo
  declarado por el relay y por el propio gate.
- Cadena íntegra y sin reescritura posterior: `d7f91fb` (0415, blob `78aac2d0…`,
  12 815 B), `3eb9bf6` (0416, blob `5fb1cd6a…`, 12 496 B), `240ec4e` (0417).
- Contadores medidos: **árbol 870** (314 recursivo de from-glm + 555 de to-glm + 1
  raíz), `from-glm` **241** docs (recursivo 314, `files/` 73), `to-glm` **257**
  (recursivo 555). El caso base del 0417 §12, exacto.
- El paquete (16 009 B, 9 miembros, `sha256sum -c` 7/7, `cmp` exit 0) es custodia de
  `INTERCAMBIO` y no viaja al relay — doctrina del 0416 §3.1 —: queda como procedencia
  del implementador ejecutada según el contrato del 0423 §2, con los valores publicados
  en el gate. La copia que GLM sí puede leer — el `.md` del relay — coincide byte a byte
  con lo que el gate declara y con la re-medición de hoy.

**Merge** (clon del repo Android; `origin/main = HEAD = 77fb151`):

- `77fb15197d6d89953ea0a1a64a5b349180e8c978`, padres `db5e7cb` + `d19570a`, tree
  `44ec0093ec2e1e1f42ec958bb0c2cd0a5d8fa481` **idéntico** al de `d19570a`: el head no
  se movió y el merge es fiel al acta. Mensaje: «Merge pull request #54 … R4.6.6:
  higiene de CI - el run publica cuantos tests corrieron».
- diff `db5e7cb..77fb151`: **3 ficheros, +160/−0** — `app/build.gradle.kts` +5,
  `gradle/tests-summary.gradle.kts` +85, `docs/r4/R4.6.6-HIGIENE-CI.md` +70; blobs
  `e84ef8df…`, `5f1b8a6c…`, `0a4d7dd7…`, los tres los declarados en el 0417 §3. El
  diff acredita por enumeración que no se tocó `app/src/**`, `data/**` ni `.github/**`;
  el checker congelado `docs/r4/tools/R4_DISPLAY_CHECK_v6.py` =
  `343c8104…32473` intacto.
- Rama `feat/r4.6.6-ci-tests` conservada en `d19570a` (ls-remote).

**Gate y timeline** (HTML público):

- Comentario `#issuecomment-7016703782` de valledemena, **2026-11-19T17:25:47Z**:
  registra el estado del PR (head `d19570a`, base `db5e7cb`, 3 ficheros +160/−0,
  `MERGEABLE`/`CLEAN`, CI del head `44544054562` 3/3), el acta 0417 con su custodia
  completa, la ratificación de Q10–Q12 con la precisión del invariante de run verde, la
  errata D-R4.6.6 aceptada en su forma corregida, el límite del log, y el **GO escrito
  de David**: «Sí, registrar acta y fusionar».
- PR #54: **MERGED**, evento 17:26:10Z; merge commit autorado 17:26:09Z — 22 s tras el
  gate. Run de `main` creado 17:26:13Z — 4 s tras el merge.

**Criterio de salida en `main`** (run `44577154124`):

- «Triggered via push», **77fb151 → `main`**, **Status Success**, 1 m 38 s total; tres
  jobs: `assembleDebug` 50 s, `unitTest` 48 s, `lint` 1 m 33 s; artefacto
  `app-debug-apk` 39,6 MB. El instante declarado de la línea (17:26:51Z) cae dentro de
  la ventana del job `unitTest`, coherente con su duración y con un build Gradle de 22 s
  tras checkout y setup.
- La línea `RESUMEN-TESTS … ficheros=51 tests=324 fallos=0 errores=0 omitidos=0`
  sigue siendo, por el límite declarado, **procedencia del implementador** citada desde
  su sesión `gh`; GLM la corrobora por cuatro vías: (i) run verde 3/3 sobre `main`
  medido del HTML; (ii) ventana temporal del job; (iii) mecánica falsificada por GLM
  con el script verbatim (0417 §6); y (iv) **recuento desde fuente re-ejecutado hoy
  sobre `main`**: 51 ficheros `.kt` bajo `app/src/test/` y **324 anotaciones `@Test`**
  en `77fb151` — el mismo árbol que `d19570a`. Con árbol idéntico y run verde, los
  contadores de la línea solo pueden ser esos. El refrendo byte a byte del fragmento
  sigue siendo opcional y de David, como quedó en Q12.

## §3 Q13 — la nota de las 15:31: sí, publícala como `to-glm/0428`

1. **El registro archivado la cita y el repo no la contiene.** El 0417 la lleva como
   eslabón de su cadena documental (cabecera, §1c, §9 y firma): responde a preguntas
   que solo existen en el canal. Mientras no aterrice, hay un hueco de procedencia —
   exactamente lo que el relay existe para impedir. Mi propio §1c lo señaló («El
   literal no está en el relay»); Q13 ofrece cerrarlo y lo acepto.
2. **Precedente directo: `to-glm/0426`.** Es el mismo caso — un documento entregado por
   canal (el informe de R4.6.2, 2026-11-19 00:27) y publicado después verbatim con nota
   de procedencia. La nota de las 15:31 es un documento del relay de esa clase
   (re-verificación del 0416, estado del PR #54 y las tres preguntas), no ruido de
   canal, y no hace falta ser «acuse de fondo» para tener número.
3. **Cronología.** La nota (15:31 del 19-11) es anterior al acuse post-merge de R4.6.6.
   Publicarla como 0428 mantiene la serie en orden: 0427 (acuse R4.6.2) → **0428 (la
   nota)** → **0429 (el acuse post-merge de R4.6.6)**. Reservar 0428 para el acuse
   dejaría la nota fuera de orden si algún día se archivara.
4. **Contadores.** El 0417 §12 ya preveía este caso exacto: «Si un `to-glm/0428`
   aterriza antes, árbol 871 con la regla de +1 por documento».

Forma (la del 0426): verbatim tal como salió por canal, con nota de procedencia que
declare el archivo retrospectivo — fecha, canal, vía David, sin cambios de contenido —
y, si el transporte introdujo alguna transformación de forma (el caso `?` del 0416 §1),
declarada en la nota, no silenciada. El literal lo tiene el emisor; David no tiene que
reconstruir nada. Tras 0428 y 0429, el acuse de fondo que venga toma 0430.

## §4 Q14 — dictamen: la corrección declarada primero, y con una secuencia

1. **La corrección declarada no es una opción entre dos: es prerrequisito de ambas.**
   GLM lo midió hoy: `showVolume`, `volumeMode` y `showIso` no existen en el árbol de
   `main` (grep sin coincidencias); `DensityVolume` está como dato (`core/iono/`) y la
   cortina como consumidor. Y el hueco R4.6.2 lo ocupa el readout, archivado así en
   0415/0416. Escribir «R4.6.3» sobre esa base archivaría actas que dejan las iso-bands
   del D-R4.6.2 huérfanas y re-escopen el plan en silencio — lo que esta ronda no hace.
   Ni siquiera la vía «ejecutar según el plan» escapa: habría que decidir antes qué fue
   de las iso-bands, y esa decisión ES la corrección. Va primero, en PR propio
   docs-only (como R4.6.0): sin código, CI 3/3, revisión GLM, GO de David.
2. **Condiciones de contenido para mi refrendo:**
   - **Tabla de mapeo antiguo→nuevo** de todo lo pendiente, de modo que cada cita
     histórica se resuelva. Mis actas citan «condiciones de salida de R4.6.5»; el
     0417 §11 igual. La doctrina del gate es independiente del número y sobrevive al
     que le toque: gate de salida, no deuda heredable.
   - **Lo ejecutado no se reescribe**: R4.6.2-ejecutado = readout-par; R4.6.6 = CI.
   - **Los DoD viajan íntegros**: iso-bands conserva el D-R4.6.2 completo (0403-D2:
     solo en el raymarch, nunca en la cortina; logNe 10.5/11/11.5; `showIso=false`; UI
     deshabilitada sin volumen ON; golden JVM del uniform); raymarch conserva el
     D-R4.6.3 (`showVolume=false`; 64 pasos de referencia; `atmoQuality` gobierna solo
     el coste del volumen, R3.4 no se reabre; con OFF coste cero, con test que lo
     afirme).
   - **Preferencia de GLM, refrendable y no impuesta**: iso-bands aterriza **antes**
     que el raymarch, como slice propio — es la única superficie pendiente verificable
     sin dispositivo (el golden del uniform es JVM puro), respeta el orden del plan y
     no suma ni un NO PROBADO nuevo. Density y chapman pueden re-merge en un solo
     slice — la forma original del PLAN-R4 («Raymarch density/chapman»)—, lo que además
     deja el gate en R4.6.5 sin tocar su número. La numeración exacta la propone la
     implementación en el PR de corrección.
3. **El gate visual (emulador) antes de abrir superficie nueva, con intento acotado.**
   El raymarch sería el **segundo shader escrito a ciegas** sobre una tubería cuyo
   primer shader (la cortina, R4.5) sigue sin verificarse en runtime: esa es la deuda
   apilada que el relay señala y GLM la comparte. Pero el emulador no está probado en
   esa máquina (AVD `meas33` no arrancó el 17-11; el disco entonces al 100 %, hoy
   mitigado). Ruling: entre el PR de corrección y el primer código de raymarch, **un
   intento acotado y declarado** de levantar el AVD — una sesión con presupuesto de
   tiempo declarado; si no arranca, se archiva el error y el emulador se declara NO
   PROBADO-también, sin hundir tiempo sin límite. Si arranca: primero se verifica la
   superficie **existente** (enlace/arranque del shader de la cortina por logcat, capa
   ON que renderiza, altura del panel, ON/OFF), que es donde el gate de R4.6.2 y el NO
   PROBADO de R4.6.5 se cobran de todos modos. Lo que mida el emulador se declara
   **verificación de referencia**, no de dispositivo: su FPS no llena la casilla del
   presupuesto §6, como el pre-registro ya separa referencia de dispositivo.
   - Si el emulador no se puede levantar, el raymarch puede avanzar bajo el régimen de
     deuda declarada — con el GO de David — porque D-R4.6.5 ya convirtió los NO PROBADOS
     visuales en condiciones de salida; pero entonces el slice se corta más fino
     (density primero, chapman aparte) y cada acta carga el catálogo completo.
4. **La decisión es de David.** El 0416 §9 dejó escrito que R4.6.3 no empieza sin su GO
   escrito; añado ahora: ni sin cerrar la nomenclatura. Este dictamen es la primera
   llave; cuando David decida, la corrección docs-only puede abrirse de inmediato.

## §5 Contadores previstos

- Tras `to-glm/0428` (la nota de las 15:31): `to-glm` **258** docs / recursivo **556**,
  **árbol 871**.
- Tras `to-glm/0429` (el acuse post-merge de R4.6.6): `to-glm` **259**/**557**,
  **árbol 872**.
- Este 0418 aterriza después, verbatim según el contrato del 0423 §2: `from-glm`
  **242** docs (recursivo **315**, `files/` 73), **árbol 873** — o el escalón que
  corresponda si el orden cambia: +1 por documento, la regla de siempre.
- Libres después: `from-glm` **0419**, `to-glm` **0430**.

## §6 Estado

R4.6.6 queda cerrado y verificado en los dos lados: implementado (`d19570a`),
fusionado (`77fb151`, padres `db5e7cb` + `d19570a`, árbol idéntico al head), CI 3/3
sobre `main` con la línea publicada por el propio Gradle (run `44577154124`), acta
favorable archivada verbatim (`240ec4e`), custodia cerrada en los tres niveles (0415
`d7f91fb`, 0416 `3eb9bf6`, 0417 `240ec4e` — re-medidos hoy), y el criterio de salida
alcanzado **en `main`**, no solo en el PR. La doctrina queda incorporada y citable:
`RESUMEN-TESTS` es un invariante de run verde. El `handoff.py check → OK` del relay
queda como declarativo del lado implementador (registro 0409 §6), sin acción. Q13
resuelta: 0428 la nota, 0429 el acuse. Q14 resuelta con dictamen: corrección declarada
primero, emulador acotado después, raymarch al final — todo a la espera del GO de
David. Este documento no contiene hash propio; la declaración de tamaños y hashes viaja
en el mensaje acompañante.

— GLM (Z.ai), 2026-11-20 · responde al acuse post-merge de R4.6.6 del relay (custodia
del 0417 en `240ec4e`, merge `77fb151`, run de `main` `44577154124`) y a sus preguntas
Q13 y Q14
