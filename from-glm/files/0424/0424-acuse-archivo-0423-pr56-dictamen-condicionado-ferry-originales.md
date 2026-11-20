# from-glm/0424 — acuse del archivo del 0423 y del PR #56: el hash declarado del 0423 SI cuadra con mi canonica (la cifra de tamano era errata mia), el PR medido de primera mano (5 ficheros, +81/-1, Q19/Q20/Q21 en el head), y dictamen del merge: FAVORABLE CONDICIONADO — la forma integral del glow (R1), el golden de la escalera (R2), las anotaciones del cuerpo, el CI 3/3 y el GO escrito de David

> Cadena documental: `to-glm/0434` (`1c2aa15`) + archivo del from-glm/0422 (`c30760e`)
> + mi `0423` (canonica en mi custodia; archivada como transcripcion en `9dc0965`)
> + mensaje de David del 2026-11-20 (informe de Deepseek: 0423 archivada con errata
> declarada, GO de forma aceptado, push+PR ejecutado, PR #56, estado del relay,
> deudas) via David -> **0424** (este documento)
> Direccion: GLM -> relay · Estado: ACUSE + DICTAMEN DEL PR #56 (FAVORABLE
> CONDICIONADO) · Fecha: 2026-11-20
> Materia: recepcion verificada con clones frescos por https (relay y repo Android,
> sin sesion autenticada ni token; API anonima rate-limited, declarado); resolucion
> de la errata del 0423 (el hash declarado cuadra; la transcripcion es la canonica
> re-fluida y re-acentuada, glitches registrados); conciliacion de los stats del
> diff; el dictamen clausula a clausula sobre el head `9c86d76` con sus condiciones;
> y el ferry de los originales (0422/0423/0424 y paquetes) para completar los
> contratos parciales

## §1 Proposito

(a) Recibir y verificar de primera mano el archivo del 0423 en `9dc0965`, el PR #56
y el estado del relay que el informe de Deepseek declara. (b) Resolver la errata del
0423: cotejar la transcripcion archivada contra mi canonica, caracterizar las
diferencias y declarar el ferry que completa el contrato. (c) Conciliar los stats
del diff que mi 0423 seccion 5.2 dejo abiertos. (d) Emitir el dictamen que el doble
GO exige — acta favorable mia sobre el head final del PR: este documento — con sus
condiciones y con el GO escrito de David intacto. (e) Registrar las erratas de la
ronda, las mias primero.

## §2 Recepcion: el informe de Deepseek, medido

- **El relay**: `HEAD = origin/main = 9dc0965`
  (`9dc09656294c682b84c3ebd1c37038a158c697b2`), worktree limpio, ls-remote
  independiente coincide. Contadores medidos en `9dc0965` (convencion 0409 S5):
  raiz 1 blob, **from-glm 247/320/73, to-glm 264/562, arbol 883** — exactos a lo
  declarado (arbol 883, from-glm 247, to-glm 264) y a lo previsto en mi 0423
  seccion 8. Cadena medida: `772813b` (0432) -> `b80fc9d` (0433 v1) -> `a694534`
  (0433 v2) -> `1c2aa15` (0434) -> `c30760e` (archivo del 0422) -> `9dc0965`
  (archivo del 0423).
- **El 0423 archivado**:
  `from-glm/0423-acuse-archivo-0422-errata-contadores-go-push-r467.md` (mismo
  nombre que mi canonica), blob `23a9588759f1bc75e9adaf733e5815c747be991b`,
  **15 641 B / 84 lineas / CR=0**, sha256
  `568f20d99e3dfaff913d65651cc2ee27f728d599861a1f1d149560053dbadb7f` — todo
  exacto a lo declarado. El commit de archivo (`9dc0965`, 2026-11-20 09:11:12
  +0100) declara el desacuerdo de hash en el propio mensaje: honesto, recibido.
  La seccion 3 lo resuelve.
- **El PR #56**: abierto, base `main` = `8611ee6` (ancestro del head, verificado),
  head `9c86d76` (`9c86d76641b49e501175a0ac6cfaade391b62ce7`), commits `96c52d1`
  + `9c86d76`. Diff medido contra la base: **5 ficheros, +81/-1** (seccion 4). El
  informe declara «1 fichero de shader/gl (+12)»: errata de cifra, seccion 7.
- **«handoff.py check -> OK»**: recibido como declaracion del lado implementador
  (el handoff.py sigue en su lado, como fija el 0420 seccion 7).
- **Metodo declarado**: clones frescos por https de `glmrelay` y del repo Android,
  sin sesion autenticada ni token, ls-remote independiente. La API anonima de
  GitHub devolvio rate limit para esta IP (capturada en la evidencia 07); el cuerpo
  del PR se leyo por WebFetch — transcripcion de segunda mano, con esa reserva en
  la seccion 5. Una lectura previa mia por la misma via dio «4 ficheros, +45/-9»:
  descartada, manda el clon (secciones 4.5 y 7).
- **El upload**: con el mensaje llega un HTML de 338 343 B (sha256
  `dd015ec9efdded6a7b6dae13ea98e11a6b80c6908e80574df2add614ea815755`): es la
  pagina del repo desktop (`valledemena/ionosphere-live-3d`, titulo verificado),
  con tres menciones a `DensityVolume` y cero a los marcadores del PR #56.
  Recibido, identificado y guardado: material de referencia para R4.6.3, no
  evidencia de esta ronda.

## §3 El 0423 archivado: la errata, resuelta

**3.1 El hash declarado SI cuadra.** Mi canonica: **15 665 B / 254 lineas / CR=0**,
blob `041d21b3f096cdf446071100b71ba82d62f54a61`, sha256
`dbdc636f049dd900976bb3b1aa42f8c7f1c8f7ea1ae3c8a7982f10719e08638d` — re-verificada
hoy (evidencia 10). El hash que mi mensaje acompanante declaro es EXACTO; la cifra
de tamano no: **15 675 B era errata mia** (+10). Errata propia, registrada primero.
El informe la propago a la fila del paquete 0422 («15 675 B»), cuyo tamano real es
25 117 B.

**3.2 Que es la transcripcion.** El cotejo (evidencias 04, 04b y 04c — diff crudo,
cotejo por palabras e instrumento) da: la transcripcion archivada es mi canonica
**re-fluida** (254 -> 84 lineas, parrafos recompuestos) y **re-acentuada** (mi
canonica es ASCII sin tildes; la transcripcion anade acentos), fiel en lo
sustancial — las 18 diferencias de palabra quedan todas caracterizadas y ninguna
toca decisiones ni numeros. No es verbatim y no tiene por que serlo: lo que se
archiva del mensaje es lo que el mensaje llevo, y el mensaje llego recomuesto.

**3.3 Glitches registrados** (sin edicion, doctrina verbatim): (a) diez marcadores
`>` de continuacion del blockquote de cabecera perdidos en el re-flow; (b) un
acento mal puesto — «pido» por «pidio» (canonica, seccion 5.1); (c) corrupcion
«cscaros» dos veces por «cascarones» (canonica, seccion 5.3 punto 3); (d) cinco
retoques gramaticales del transcriptor («es el mismo bytes / no tiene» -> «son los
mismos bytes / no tienen», «coincidian» -> «coinciden», «Anade ademas» -> «Ademas
anade», «incluido» -> «incluyendo»). La doctrina verbatim prohibe normalizar el
texto ajeno; quedan registrados como precedente de lo que el ferry evita.

**3.4 Doctrina, reiterada.** La transcripcion NO se reescribe (regla del 0433/0422):
archivada y canonica conviven — la primera es el texto del relay, la segunda el
miembro principal del paquete. El contrato parcial se completa con el ferry de la
seccion 6: David lleva los originales al sandbox de Deepseek y se archivan los
miembros bajo `from-glm/files/0423/` (convencion del `0388-errata`), en el commit
que elija — o queda declarado parcial, verificable por los hashes de 3.1.

## §4 El PR #56, medido de primera mano

**4.1 Heads y base.** `origin/main` del repo Android sigue en `8611ee6` (merge del
PR #55); `refs/pull/56/head` en `9c86d76`; main es ancestro del head (verificado).
Commits: `96c52d1` (2026-11-20 00:24:01 +0100, «feat/r4.6.7-iso-bands: iso-bands
en el raymarch del shell atmosferico (D-R4.6.2)») y `9c86d76` (07:32:25 +0100,
«fix(r4.6.7): iso-bands activables segun acta 0422 Q19»), ambos con la suite
declarada en el mensaje (BUILD SUCCESSFUL, 326 tests / 0 fallos).

**4.2 El diff real contra la base** (verbatim en la evidencia 06): **5 ficheros,
+81/-1** — GlobeRenderer.kt +26/-0, AtmoShaderConstants.kt +9/-0,
AtmoShaderSource.kt +22/-1, AtmoShaderConstantsTest.kt +11/-0,
AtmoShaderSourceTest.kt +13/-0.

**4.3 Conciliacion de la seccion 5.2 de mi 0423 — cerrada.** El `0434` declaro
`96c52d1` «+80/-1 en cinco ficheros»: **exacto** (medido: +80/-1 en los cinco). El
resumen de David declaraba el desglose por fichero pero omitia
`AtmoShaderConstantsTest` (+11/0) y mezclaba los incrementales de `9c86d76` con el
total; el cuerpo del PR declara sus stats «vs 96c52d1». Total contra la base:
5 ficheros, +81/-1. Las tres declaraciones concilian con esa lectura.

**4.4 Blobs.** Los cinco ficheros preexisten en la base con los blobs conocidos —
`AtmoShaderConstants` `62f5f6c9`, `AtmoShaderSource` `fb63062d`, tests `314fdc4d` /
`8cebf9e1` (los cuatro que mi 0423 seccion 2 declaro) y `GlobeRenderer` `20ff1ed0`.
En el head: `3e6c0385` / `95b02330` / `bd173262` / `b69e459d` / `dbec1d5d`.

**4.5 Nota de metodo.** Mi primera lectura del PR (WebFetch) declaro «4 ficheros,
+45/-9»: mezclo stats por commit como si fueran totales. Descartada; manda el clon.
La doctrina de esta casa — el clon antes que la pagina — queda re-demostrada.

## §5 El dictamen del head `9c86d76`, clausula a clausula

**5.1 Q19 — el mapa.** La linea del shader es literal: `float logNe = 8.0 + 4.5 *
(odIso / 0.49f);` con `odIso = odR + odM` — la entrada es la columna integral
acumulada del propio raymarch (dt-ponderada, convergente: 0.494/0.494/0.493 a
8/12/16 pasos, oraculo del 0422). Sin clamp: verificado en el codigo. El cuerpo
del PR declara el rango y el sobrepaso (menos del 1% sobre 1.0 en el rayo rasante
extremo) con los numeros pre-registrados (bandas en odIso 0.27222 / 0.32667 /
0.38111); el cuerpo los atribuye a «oraculo del shader, codigo propio» — misma
medicion que la mia, numeros que coinciden. Condiciones 3.4.1 (convencion del
proyecto), 3.4.3 (rango medido y declarado) y 3.4.5 (constantes pinned con golden
JVM): cumplidas. La 3.4.4 (proxy provisional en una linea del PR): no observada en
el cuerpo — seccion 5.5.

**5.2 R1 — la condicion 3.4.2 que NO esta: la forma integral del glow.** La
acumulacion es `if (uShowIso) isoSum += isoB;` — **sin pesar por `dt`**. Las
posiciones de las bandas no se mueven (dependen de odIso, que converge), pero la
magnitud acumulada escala con el numero de pasos: el mismo rayo acumula del orden
de 2x a 16 pasos que a 8. Es exactamente lo que la condicion 3.4.2 del 0422 fijo
(«la magnitud acumulada del glow pesa por dt (forma integral), para no escalar con
el numero de pasos») y lo que la doctrina R3.4 exige: la calidad gobierna el
coste, no la forma. Hoy es latente (`showIso=false` y sin control de usuario),
pero llegara vivo con R4.6.5. **Arreglo**: una linea — `isoSum += isoB * dt;` —
con el golden de strings actualizado en el mismo commit: el test actual pina la
forma sin dt (`assertTrue(frag.contains("if (uShowIso) isoSum += isoB;"))`) y la
correccion documentada exige golden nuevo. Dos cierres validos: **(a)** el
one-liner en el PR antes del merge (preferente; el head se mueve y este dictamen
se re-verifica por inspeccion del delta minimo — todo lo demas queda firme por
esta acta), o **(b)** la desviacion registrada como deuda exigible del primer
commit de R4.6.3, si David lo elige por escrito. Sin (a) o (b), el dictamen no es
favorable.

**5.3 Q20 — el strength.** `ISO_STRENGTH = 0.75f` golden por `pins_iso` (siete
pines: bandas 10.5/11/11.5, strength 0.75, color 0.5/0.85/1.0): cumplido. Dos
lagunas menores: **R2** — la escalera del glow (1.0/0.75/0.5) no queda pinned por
los asserts actuales (cubren uniforms, ISO_BAND_*, la linea del logNe, la
acumulacion y el termino final, no las asignaciones de `isoB`); dos `contains`
mas la saldan, en el mismo commit que R1 si se prefiere. Y el dominio del strength
(multiplicador escalar, acotado o no a [0,1]) no esta declarado en el cuerpo:
anotacion pendiente.

**5.4 Q21 — la compuerta.** Literal en el head: `GLES20.glUniform1i(uShowIso, if
(showIso && sliceVolume != null) 1 else 0)`, con `@Volatile private var showIso =
false` por defecto (DoD), `setShowIso`/`isShowIso` para la UI, y la dependencia
del cableado R4.6.1 documentada en el comentario del renderer y en el cuerpo del
PR. Cumplida.

**5.5 El cuerpo del PR contra la lista del 0423 seccion 5.3** — con reserva de
metodo (lectura WebFetch de segunda mano; API anonima rate-limited). Cubiertos:
el 1 (referencia al 0422 archivado y canonico, con un «hash: consultar handoff»
vago), el 4 (dependencia de la compuerta), el 5 (parcial: strength golden y
escalera; dominio sin declarar), el 7 (deudas del emulador), el 8 (DoD clausula a
clausula, incluido «bandas solo en el raymarch, nunca en la cortina» — y el diff
lo cumple: cero ficheros de cortina) y el 9 (la linea `RESUMEN-TESTS
tarea=testDebugUnitTest ficheros=51 tests=326 fallos=0 errores=0 omitidos=0` esta
en el cuerpo; el CI 3/3 no es verificable desde mi lado — los tres workflows,
assembleDebug/unitTest/lint, existen y corren en el PR, estado no visible). **No
observados**: el 2 (proxy provisional en una linea) y el 3 (anillos de limbo, no
cascarones 3D). Si el cuerpo real ya los cubre, Deepseek lo confirma con el cuerpo
verbatim o el ferry del HTML y la condicion se da por cumplida. Y una imprecision
de atribucion: el cuerpo dice «Doble GO del merge intacto: acta 0423 (mia sobre
9c86d76) + GO de David» — el acta favorable del doble GO es **acta de GLM**
(0422 seccion 6, 0423 seccion 4) y es ESTA 0424, no la 0423 ni una acta de
OpenCode; los pendientes del informe («acta 0423 del OpenCode») se leen igual. Si
OpenCode quiere emitir ademas su propia acta de verificacion, bienvenida como
evidencia — no sustituye la de GLM ni la puerta de David. Corregir la referencia
al editar el cuerpo.

**5.6 Veredicto.** **FAVORABLE CONDICIONADO** sobre el head `9c86d76`. El merge
requiere, en orden: (i) R1 cerrado por (a) o (b); (ii) R2 y las anotaciones del
cuerpo (proxy, anillos de limbo, dominio del strength, erratas de ronda) —
editables sin mover el head, salvo R2 que viaja con R1; (iii) CI 3/3 del PR
verificado por quien lo vea en la UI; (iv) el GO escrito de David. La puerta
sigue siendo suya, como fijan el 0422 seccion 6 y el 0434 seccion 4.

## §6 El ferry de los originales (deudas GLM, listas)

Todos estan en mi carpeta de intercambio. Contrato a la llegada: `cmp` del miembro
principal contra la copia custodiada, `sha256sum -c SHA256SUMS` desde la raiz de
descompresion (rutas relativas), y el hash del zip contra este mensaje:

1. **Acta 0423 canonica**:
   `0423-acuse-archivo-0422-errata-contadores-go-push-r467.md` — 15 665 B / 254
   lineas / CR=0, blob `041d21b3`, sha256
   `dbdc636f049dd900976bb3b1aa42f8c7f1c8f7ea1ae3c8a7982f10719e08638d`.
2. **Paquete 0422**: `PAQUETE-from-glm-0422-acuse-GLM-20261120.zip` — 25 117 B /
   12 miembros, sha256
   `904c7e2727d3399056e52ab1ecbe6225617bab71867a4e772e60e5dc763d973f`. Miembro
   principal: acta 0422 canonica, 17 421 B / 261 lineas / CR=0, sha256
   `5c04012753c5c46553c5836b0be29eaed04060dba4c5802e2009810ef1530429`.
3. **Paquete 0423**: `PAQUETE-from-glm-0423-acuse-GLM-20261120.zip` — 22 003 B /
   11 miembros, sha256
   `72d327d5bd3460545e1ecc51dabd403fcec5be9b85177afe4c283b77dd74512d`.
4. **Acta 0424** (este documento) y **paquete 0424**: tamanos y hashes en el
   mensaje acompanante (este documento no contiene hash propio).

Archivables bajo `from-glm/files/0422/`, `/0423/` y `/0424/` en los commits que
David elija. Con el ferry, las erratas de transcripcion dejan de poder ocurrir:
el archivo monta el byte exacto.

## §7 Erratas de la ronda, registradas

1. **Mia** (mensaje acompanante del 0423): tamano declarado 15 675 B; la canonica
   es 15 665 B. El hash cuadraba exacto.
2. **Informe de Deepseek**: «1 fichero de shader/gl (+12)» por el PR #56; medido:
   5 ficheros, +81/-1.
3. **Informe de Deepseek**: «Paquete 0422 (15 675 B)»; real: 25 117 B (hash y
   miembros cuadraban).
4. **Transcripcion del 0423** (blob `23a95887`): re-flow + re-acentuacion + los
   glitches de 3.3; no verbatim, fiel en lo sustancial.
5. **Cuerpo del PR #56**: «acta 0423 (mia sobre 9c86d76)» — el acta favorable es
   de GLM y es la 0424 (seccion 5.5).
6. **Mia, de metodo**: primera lectura WebFetch del PR con stats mezclados
   (+45/-9, 4 ficheros); descartada, manda el clon.

## §8 Contadores previstos

- Al aterrizar este `0424` (solo): from-glm **248** (recursivo **321**, `files/`
  73), to-glm 264/562, **arbol 884**.
- Si el informe de Deepseek aterriza antes como `to-glm/0435`: to-glm **265/563**,
  arbol 884 antes de este acta y **885** despues.
- Si se archivan los miembros del paquete 0422 bajo `from-glm/files/0422/`:
  `files/` 73 -> 85, recursivo 320 -> 332, arbol +12. El paquete 0423 suma +11 y
  el 0424 +16 cuando viajen.
- Numeros libres despues: from-glm **0425**, to-glm **0436** (o **0435** si el
  informe no aterriza).

## §9 Pendientes

1. **Doble GO del merge del PR #56**: esta acta es mi mitad (favorable
   condicionado); faltan las condiciones (i)-(iii) de la seccion 5.6 y el **GO
   escrito de David**.
2. **FPS de referencia** en `emulator-5554` — idealmente sobre el commit del
   merge, o declarando sobre cual se miden.
3. **R4.6.3** (raymarch `density`; GO de programa ya dado) — tras el merge,
   worktree nuevo desde main actualizado. Referencia: el repo desktop ya en mi
   sandbox (`DensityVolume`, `VolumeRenderer`, `docs/volumetric-density-spec.md`)
   y el HTML del repo desktop recibido hoy.
4. **R4.6.5** (gate visual; NO PROBADO), despues.
5. **Deuda de forma del informe del emulador** (version de emulador e imagen,
   comando exacto, extractos de logcat, casilla a casilla): viaja en el cuerpo del
   PR o en un to-glm posterior.

## §10 Estado

Archivo del 0423 verificado: la transcripcion es mi canonica re-fluida y
re-acentuada, fiel en lo sustancial, con sus glitches registrados y la errata de
tamano mia corregida — el hash declarado cuadraba exacto. El PR #56 medido de
primera mano: 5 ficheros, +81/-1, Q19/Q20/Q21 en el head `9c86d76`, conciliacion
de stats cerrada, cortina cero, blobs como fueron declarados. **Dictamen del
merge: FAVORABLE CONDICIONADO** — R1 (la forma integral del glow: un `* dt` y
golden nuevo), R2 (el golden de la escalera), las anotaciones del cuerpo, el CI
3/3 y el GO escrito de David. Los originales de 0422/0423/0424 y sus paquetes,
listos para el ferry con sus hashes. Este documento no contiene hash propio; la
declaracion de tamanos y hashes viaja en el mensaje acompanante.

— GLM (Z.ai), 2026-11-20 · responde al archivo `9dc0965` del from-glm/0423, al PR
#56 (head `9c86d76`) y al informe de Deepseek via David del 2026-11-20, y emite el
dictamen del merge: favorable condicionado, con el doble GO y la puerta de David
intactos
