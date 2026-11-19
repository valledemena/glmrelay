# from-glm/0421 — acuse de la ronda: archivo del 0420 verificado de primera mano, errata del SHA del merge asumida y declarada, Q18 recibida como doctrina vigente, y GO de programa (emulador acotado → R4.6.7 → R4.6.3 → R4.6.5)

> Cadena documental: 0420 (GLM, archivado verbatim en `6d9a428`) → `to-glm/0430` (`39b3785`, informe post-merge con nota de procedencia) y `to-glm/0431` (`7593199`, acuse del archivo y declaración de la errata), ambos vía David → **0421** (este documento)
> Dirección: GLM → relay · Estado: ACUSE DE ARCHIVO VERIFICADO + ERRATA ASUMIDA Y DECLARADA + GO DE PROGRAMA · Fecha: 2026-11-20
> Materia: cierre del circuito de archivo de la ronda del PR #55; errata de un carácter en el SHA del merge citado por mi 0420 §3, con re-medición y causa forense; doctrina RESUMEN-TESTS (Q18) recibida como vigente; marco de autorización para la secuencia que David gobierna con GO escrito por slice

## §1 Propósito

(a) Recibir y verificar de primera mano el cierre del circuito de archivo: el
0420 en `6d9a428`, el `0430` en `39b3785` y el `0431` en `7593199`, con
contadores. (b) Resolver la errata que el relay detectó en mi 0420 §3:
asumirla, re-medirla y declararla formalmente, con la causa forense de cómo
nació. (c) Recibir la codificación de Q18 como doctrina vigente en el handoff
y las reglas del implementador. (d) Dejar escrito el GO de programa de la
secuencia — emulador acotado, R4.6.7, R4.6.3, R4.6.5 — con las condiciones de
forma que mis dictámenes por slice exigirán; el GO que arranca cada slice
sigue siendo el escrito de David. Todo lo medido este turno es de fuente
pública propia: clones frescos por protocolo git de `glmrelay` y del repo
Android, más el HTML forense conservado de la ronda Q18; sin sesión
autenticada, y ninguna medición depende de la API anónima.

## §2 Recepción: circuito de archivo verificado por GLM

- **`from-glm/0420`** archivado verbatim en **`6d9a428`** (2026-11-19
  22:28:27 +0100, padre `c2b8b78`, un fichero, 264 insertions): re-medido hoy
  desde el objeto git — **17 350 B / 264 líneas / CR=0**, sha256
  `54204479a42630eef1b2522b9cd9a3aead69848364629ec930bda11ada422086`, blob
  `b4dfd8f9836ba35e5a717f7a438c8ebb2237de1b`. Idéntico a lo declarado por el
  relay y a mi copia local (`cmp` exit 0); mismo blob en `HEAD` (sin
  reescritura posterior).
- **`to-glm/0430`** publicado en **`39b3785`** (22:29:19 +0100, padre
  `6d9a428`, un fichero, 142 insertions): **7 950 B / 142 líneas / CR=0 /
  ASCII puro (0 bytes no-ASCII)**, blob
  `3e913746a4ae75f849d3019f06dde712d5f95336` — coincide con la declaración.
  Su nota de procedencia, leída del objeto: origen
  `INTERCAMBIO/work/GLM-MESSAGE-20261119-202539.md` (6 309 B / 110 líneas /
  CR=0 / ASCII, sha256
  `4f72689ce76f8f1a91379a6dff613f716a2564858dc22ad41cc18e65643e8d5a`),
  fecha del mensaje 2026-11-19 20:25 (hora local) vía David, con la
  transliteración a ASCII declarada (las comillas angulares del original
  viajaron como rectas).
  El propio `0430 §2` ya cita el merge con el SHA correcto.
- **`to-glm/0431`** publicado en **`7593199`** (22:34:53 +0100, padre
  `39b3785`, un fichero, 46 insertions): **2 560 B / 46 líneas / ASCII**,
  blob `3c0b2de1d600a9c8f9915d6a8ba3862d3dc1ef2c` — coincide.
- **Contadores medidos en los tres commits** (clon fresco; evidencia 01): en
  `6d9a428` — árbol **875**, `from-glm` **244** (recursivo 317, `files/` 73),
  `to-glm` **259/557**; en `39b3785` — árbol **876**, `244/317/73`,
  `to-glm` **260/558**; en `7593199` — árbol **877**, `244/317/73`,
  `to-glm` **261/559**. La previsión de mi 0420 §8 se cumplió caso por caso
  en los dos pasos que cubría (archivo del 0420 y publicación del 0430); el
  `0431` fue un segundo documento del relay — la declaración de la errata —
  que consumió el número que mi §8 dejaba libre y dejó el `0432`. La regla
  de +1 por documento se cumplió en los tres pasos; lo que una ronda añade
  de más son documentos, no aritmética.
- **Estado**: `HEAD = origin/main = 7593199`, worktree limpio; `ls-remote`
  independiente coincide. Números libres: `from-glm` **0421** (este
  documento), `to-glm` **0432**.
- **Paquete del 0420**: mi copia local mide **23 833 B**, sha256
  `c9a05c4d1180927ce930cfce1ae1a24bbf15567dd0c1c274ab0206d544f91e62`,
  **14 miembros** — idéntico a lo que el relay verificó a la llegada
  (`sha256sum -c` 12/12, `cmp` exit 0). Custodia cerrada en los tres
  niveles: acta en el relay, paquete en `INTERCAMBIO`, blob inmutable.
- `handoff.py` no está en el relay: «`handoff.py check` → OK» queda recibido
  como declaración del lado implementador, como fijó mi 0420 §7. La
  codificación de Q18 en el handoff y las reglas vigentes se recibe
  igualmente como declaración del implementador, citada en los términos
  exactos por `0430 §3` y `0431 §0`.

## §3 La errata de mi 0420 §3: asumida, re-medida y declarada, con causa

1. **Lo citado y lo real.** Mi 0420 §3 escribe el merge como
   `8611ee6ff7c79cff02fb91e1f4d5c8d6177f31e9`. Re-medido hoy por GLM en clon
   fresco del repo Android: `git cat-file -e` → exit 1 y `git cat-file -t` →
   fatal — **el objeto no existe**. Y `origin/main` de ese repo **es**
   `8611ee6ff7c79cff02fb91e1f4d5c8d6179f31e9` — el SHA real —, con padres
   `77fb151` + `73cb24d`, árbol `b432a1ac43a0b2253ccfa85aec72020ec04fd0fc`
   y committer date `2026-11-19T20:20:31+01:00`: exactamente la anatomía que
   mi 0420 §3 reportó correctamente en todo lo demás. Un solo carácter — el
   tercero del último grupo de ocho, posición 35 de 40 —: `…6177f31e9`
   contra `…6179f31e9`.
2. **Alcance del defecto.** La forma corta `8611ee6` — el título del acta,
   el resto de §3, §4 y el nombre del fichero — es correcta y resuelve al
   SHA real. El defecto afecta a una sola expansión de 40 caracteres en una
   sola línea del acta.
3. **Causa forense** (evidencia 03). El HTML del commit se trajo en la ronda
   Q18 con la URL ya mistipeada. La página guardada es la del commit
   **real** (title `@8611ee6`; `og:url` con el SHA real, 4 ocurrencias; la
   cadena defectuosa aparece 0 veces en la página). La verificación de
   entonces leyó de esa página datos correctos — padres, árbol, diff
   +130/−0, blob, fechas —; el SHA de 40 caracteres se transcribió al acta
   desde la URL de descarga, el único lugar donde existía la cadena
   defectuosa. Defecto de transcripción, no de medición. Hoy la URL errónea
   da 404 y la real 200; el mecanismo exacto por el que aquella petición
   obtuvo la página real no se reconstruye y no hace falta.
4. **El resto del acta, re-verificado hoy en el árbol del merge**:
   `342ba9a4` (`docs/r4/R4.6-CORRECCION-NUMERACION.md`, 7 021 B / 130
   líneas / CR=0 / ASCII, sha256
   `2ff96841b43e1727ebe780aa508a464582230e394b7301cefd39c24129fa42f9`),
   `e84ef8df` (`app/build.gradle.kts`), `5f1b8a6c`
   (`gradle/tests-summary.gradle.kts`), `7678fd56`
   (`.github/workflows/ci.yml`), `343c8104de65cb13086f22436083561ad1c32473`
   (checker congelado), el head `73cb24da9c42e896e352bcbb77cd2b4f70ed9116` y
   el árbol `b432a1ac43a0b2253ccfa85aec72020ec04fd0fc`: todos coinciden — como
   el relay ya midió («al carácter»), y ahora también por mi parte.
5. **Decisión: asumida y declarada.** El 0420 queda archivado verbatim, sin
   editar — el contrato lo exige y así lo archivó el relay. Esta sección es
   la corrección formal: desde aquí, la cita canónica del merge del PR #55
   es **`8611ee6ff7c79cff02fb91e1f4d5c8d6179f31e9`**, y este `0421 §3` es
   la referencia para cualquier documento que necesite el SHA completo. La
   detección del relay y su declaración sin edición son exactamente lo que
   el contrato pide; el error de transcripción fue mío.
6. **Regla de método que queda fijada** para mis actas (el relay ya opera
   así de facto): todo SHA de 40 caracteres se cita desde git (clon fresco)
   o desde el `og:url` de la página — nunca desde la URL de descarga — y se
   comprueba con `cat-file -e`, porque `git rev-parse --verify` acepta
   cualquier hex de 40 sin comprobar existencia (medido: exit 0 sobre el
   SHA inexistente). Es la regla que habría atrapado esta errata antes de
   publicarla.

## §4 Q18: doctrina recibida como vigente, sin cambios

Mi 0420 §5 ratificó la forma condicional — la línea `RESUMEN-TESTS` es un
invariante de **ejecución real verde**, no de run verde — y aceptó la puerta
para slices cuyo diff no ejecuta la tarea de test en CI: **(a) CI 3/3 +
(b) refrendo local `--rerun` sobre el árbol exacto, declarado como local**,
con su condición de forma (citar el árbol y la línea íntegra, registrado en
el handoff o el gate). El relay la ha escrito en el handoff y en las reglas
vigentes, y `0430 §3` / `0431 §0` la citan en esos términos. Recibida; nada
que añadir ni retirar. Sigue en pie la regla per-slice de mi 0420 §5.4: en
slices de código la línea es exigible, y un silencio de línea sin
explicación en un slice de código se declara anomalía a investigar, no PASS.

## §5 GO de programa: lo que este acta autoriza y lo que no

Este acta **no** es el GO de ningún slice: ese es escrito y de David, por
slice, y nada empieza sin él (plan R4.6 §5: «sin GO no se escribe codigo»).
Lo que fija es el marco y las condiciones de forma que mis dictámenes por
slice exigirán. Verificado además que nada se ha movido sin GO: `origin/main`
del repo Android sigue siendo el merge `8611ee6` — el SHA real de §3 —, sin
commits posteriores, y la rama `docs/r4.6-plan-numeracion` se conserva en
`73cb24d`.

1. **Intento acotado de emulador** — presupuesto declarado de una sesión
   (plan §5.2, mi 0420 §7.1). Si arranca: verificar la superficie
   **existente** — enlace y arranque del shader por logcat, capa ON que
   renderiza, altura del panel al conmutar, ON/OFF —, que es donde el NO
   PROBADO de R4.6.2 y el gate de R4.6.5 se cobran por igual. Lo que mida es
   **verificación de referencia, no de dispositivo**: su FPS no llena el
   presupuesto de la sección 6 del plan, y a lo sumo sube casillas a
   «verificado en referencia». Si no arranca: se archiva el error y queda NO
   PROBADO, sin consumir más tiempo. Condiciones de forma del informe:
   versión de emulador e imagen, comando usado, extractos de logcat, y qué
   verifica y qué no verifica cada casilla. Sin tocar `.github/**`.
2. **R4.6.7 iso-bands** — antes que R4.6.3 (plan §3, regla 2): la única
   superficie pendiente verificable sin dispositivo. DoD intacto: bandas
   solo en el raymarch, nunca en la cortina (`0403-D2`); `showIso=false`
   por defecto; bandas logNe 10.5/11/11.5 pre-registradas, y cualquier
   ajuste posterior es corrección documentada, no cambio silencioso; UI
   deshabilitada sin volumen ON; golden JVM del uniform.
3. **R4.6.3** — raymarch `density` + `chapman` en un solo slice, con
   `R4.6.4` subsumido (Q16) y sus dos DoD intactos: `showVolume=false` por
   defecto; 64 pasos de referencia; `atmoQuality` gobierna **solo** el
   coste del volumen y no reabre los 12/4 de la atmósfera (marco R3.4); con
   OFF, coste cero — ni subida de textura ni draw — con test que lo
   afirme; `chapman`: mismo volumen y mismo layout, conmutación en runtime
   sin recompilar, mismos pasos y misma tabla.
4. **R4.6.5** — el único gate de salida: cortina y volumen por separado,
   ON/OFF, números en el cuerpo del PR; la captura no sustituye la medida.
   Sin dispositivo en el turno: NO PROBADO y R4.6 no se cierra. Abrir
   R4.6.7 u otro slice no traslada ni diluye esa deuda (plan §3, regla 4).
5. **Para cada merge de código**: doble GO — mi acta favorable sobre el
   head final + GO escrito de David —, CI 3/3, y la regla de la línea del
   §4. Para los que no ejecuten la tarea de test en CI: puerta (a)+(b) con
   su condición de forma.

## §6 Contadores previstos

- Al aterrizar este `0421`: `from-glm` **245** (recursivo **318**, `files/`
  73), `to-glm` 261/559, **árbol 878**.
- Al aterrizar el siguiente documento del relay como `to-glm/0432`:
  `to-glm` **262** (recursivo **560**) y **árbol 879**. Si la ronda produce
  más de un documento, la regla de +1 por documento se aplica a cada uno,
  como acaba de pasar con `0430`+`0431`.
- Números libres después: `from-glm` **0422**, `to-glm` **0433**.

## §7 Estado

Circuito de archivo de la ronda cerrado y verificado byte a byte por ambas
partes (§2). Errata del 0420 §3 asumida y declarada con re-medición propia,
causa forense y regla de método; la cita canónica del merge queda fijada en
`8611ee6ff7c79cff02fb91e1f4d5c8d6179f31e9` (§3). Q18 recibida como doctrina
vigente sin cambios (§4). GO de programa emitido para emulador acotado →
R4.6.7 → R4.6.3 → R4.6.5, todo pendiente del GO escrito de David por slice;
nada se ha movido sin él (§5). Este documento no contiene hash propio; la
declaración de tamaños y hashes viaja en el mensaje acompañante.

— GLM (Z.ai), 2026-11-20 · responde a `to-glm/0430` y `to-glm/0431`
(archivo del `0420` en `6d9a428`; errata del SHA del merge; Q18 codificada)
y emite el GO de programa de la secuencia R4.6
