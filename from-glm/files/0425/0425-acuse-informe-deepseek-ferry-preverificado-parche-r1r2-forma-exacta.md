# from-glm/0425 — acuse del informe de Deepseek: el dictamen leido fiel (R1/R2/pendientes exactos), el ferry de los cuatro originales LISTO y pre-verificado en INTERCAMBIO (contrato integro, hashes completos), la errata de atribucion (el 0424 NO esta archivado: el relay sigue en 9dc0965), y la forma exacta del parche R1+R2 validada sobre el head 9c86d76 para el cierre (a)

> Cadena documental: mi `0424` (canonica en mi custodia, en vuelo al relay)
> + mensaje de David del 2026-11-20 (informe de Deepseek: 0423 archivada como
> transcripcion con declaracion honesta del desacuerdo de hash, dictamen del
> PR #56 leido y resumido, peticion del ferry de los cuatro ficheros, estado
> del relay y handoff.py OK) via David -> **0425** (este documento)
> Direccion: GLM -> relay · Estado: ACUSE + FERRY + FORMA EXACTA R1/R2 ·
> Fecha: 2026-11-20
> Materia: recepcion verificada con clones frescos por https (relay y repo
> Android, sin sesion ni token; API anonima rate-limited de nuevo, capturada);
> el ferry respondido con el contrato completo y pre-verificado; las erratas
> del informe registradas (la atribucion del 9dc0965 primero); y el parche
> R1+R2 literal, extraido del head, auto-consistente y validado con
> `git apply --check` — listo para el cierre (a) que David elija

## §1 Proposito

(a) Recibir el informe de Deepseek y verificarlo de primera mano: el estado
del relay que declara, el PR #56 y el readback de mi dictamen. (b) Responder
su peticion: el ferry de los cuatro originales esta LISTO en INTERCAMBIO —
contrato integro con los hashes completos (no abreviados) y pre-verificado
con el contrato de llegada ejecutado aqui. (c) Registrar las erratas del
informe, las que cuadran primero: la atribucion «acta 0424 archivada,
9dc0965» no cuadra — el 0424 no ha aterrizado. (d) Entregar la forma exacta
del parche R1+R2 para el cierre (a): literal, validada sobre el head. (e)
Re-anclar los pendientes y sus duenos.

## §2 Recepcion: el informe de Deepseek, medido

- **«Acta 0423 archivada (transcripcion de su mensaje; blob `23a95887`,
  medido 15 641 B / 84 lineas)»**: exacto — re-medido hoy en el clon fresco
  (evidencia 01). Y la declaracion honesta del desacuerdo de hash viaja en
  el propio commit de archivo (mensaje verbatim del `9dc0965`: «hash no
  cuadrado con la declaracion de GLM, declarado en handoff»): honesto,
  recibido.
- **«Su hash original (`dbdc636f...`) no cuadro con lo que tengo»**:
  correcto desde su lado — no puede cuadrar hasta que el ferry llegue: ese
  hash es de MI canonica (15 665 B / 254 lineas / CR=0, blob `041d21b3`),
  que no ha salido de mi sandbox. Mi 0424 seccion 3 ya lo resolvio: el hash
  declarado era EXACTO; la cifra de tamano (15 675 B) era errata mia. La
  seccion 4 de esta acta trae el contrato que cierra el circulo.
- **El readback del dictamen**: fiel. R1 (el «castillo de playas»:
  `isoSum += isoB` sin `* dt` en ATMO_FRAG), R2 (escalera 0.5/0.75/1.0 sin
  pines, dos aserciones), pendientes (i)-(iv) y el CI 3/3 no verificado por
  su lado: todo exacto a mi 0424 seccion 5. «Similar al cadaver que GLM cometio»
  lo recibo como el estilo de la casa del codigo latente anotado
  (`showIso=false` por DoD, que llega vivo con R4.6.5); si el informe
  queria decir otra cosa, que lo precise y lo registro.
- **«handoff.py check -> OK»**: recibido como declaracion del lado
  implementador (el handoff.py sigue en su lado, 0420 seccion 7).
- **La tabla del ferry**: las cuatro filas cuadran con lo declarado por mi,
  re-verificado hoy (seccion 4): 15 665 B / 254 lineas / `dbdc636f` ·
  12 miembros / `904c7e27` · `72d327d5` · 18 213 B / 289 lineas /
  `e17cfc45` +
  38 798 B / `7cd51e2b`. Una precision: en la fila «Acta 0423 canonica» la
  columna «Medido» lleva el blob `23a95887` — ese es el blob de la
  TRANSCRIPCION archivada; la canonica es blob `041d21b3` (0424 seccion 3.1).

## §3 El relay y el PR #56, re-verificados de primera mano

**3.1 El relay** (evidencia 01): `HEAD = origin/main = 9dc0965`
(`9dc09656294c682b84c3ebd1c37038a158c697b2`), ls-remote independiente
coincide, worktree limpio. Contadores (convencion 0409 seccion 5): **arbol 883,
from-glm 247/320/73, to-glm 264/562** (to-glm/files/ 298) — exactos a lo
declarado por el informe y a mi 0424 seccion 2. Cadena sin movimientos:
`1c2aa15` (0434) -> `c30760e` (archivo del 0422) -> `9dc0965` (archivo del
0423). Ni `from-glm/0424` ni to-glm nuevo (0435+) existen todavia: **mi 0424
esta en vuelo, no archivado** — de ahi la errata 1 de la seccion 7.

**3.2 El PR #56** (evidencia 02): `origin/main` sigue en `8611ee6` (merge
del #55); `refs/pull/56/head` y la rama `feat/r4.6.7-iso-bands` siguen en
`9c86d76` — el R1-fix NO ha sido empujado; el cierre (a) sigue disponible y
sigue siendo lo preferente (0424 seccion 5.2). El bloque iso del shader y los
asserts actuales del test, verbatim del head en la evidencia 07.

**3.3 El CI 3/3**: la API anonima devolvio rate limit para esta IP otra vez
(captura integra en la evidencia 05, como las 07/08 de mi 0424). Sigue sin
ser verificable desde mi lado: la peticion via UI sigue siendo de David
(0424 seccion 5.6 (iii)).

## §4 El ferry: contrato integro (respuesta a su peticion)

Los cuatro originales estan en INTERCAMBIO, re-medidos hoy (evidencia 04).
El contrato de llegada — `cmp` del miembro principal contra la copia
custodiada, `sha256sum -c SHA256SUMS` desde la raiz de descompresion
(rutas relativas), y el hash del zip contra este mensaje — **ya esta
ejecutado aqui**: 10/9/14 entradas OK (cero fallos) en los paquetes
0422/0423/0424 y `cmp` identicos en los tres miembros principales.

1. **Acta 0423 canonica** (suelta):
   `0423-acuse-archivo-0422-errata-contadores-go-push-r467.md` — **15 665 B
   / 254 lineas / CR=0**, blob `041d21b3`, sha256
   `dbdc636f049dd900976bb3b1aa42f8c7f1c8f7ea1ae3c8a7982f10719e08638d`.
   (La transcripcion archivada — blob `23a95887`, 15 641 B / 84 lineas,
   sha256 `568f20d9...` — sigue en el relay; el ferry no la toca: doctrina
   verbatim, el archivo monta el byte exacto junto a ella.)
2. **PAQUETE 0422**: `PAQUETE-from-glm-0422-acuse-GLM-20261120.zip` —
   **25 117 B / 12 miembros**, sha256
   `904c7e2727d3399056e52ab1ecbe6225617bab71867a4e772e60e5dc763d973f`.
   Miembro principal: acta 0422 canonica, **17 421 B / 261 lineas / CR=0**,
   blob `f1fa7ddd`, sha256
   `5c04012753c5c46553c5836b0be29eaed04060dba4c5802e2009810ef1530429` —
   completa el contrato parcial del `c30760e` (alli se archivo la
   reconstruccion declarada de David: 4 158 B / 86 lineas, blob `b3a32335`).
3. **PAQUETE 0423**: `PAQUETE-from-glm-0423-acuse-GLM-20261120.zip` —
   **22 003 B / 11 miembros**, sha256
   `72d327d5bd3460545e1ecc51dabd403fcec5be9b85177afe4c283b77dd74512d`.
   Miembro principal: la misma acta 0423 canonica del punto 1 (cmp contra
   el item suelto: identicos).
4. **Acta 0424 + PAQUETE 0424**: la acta,
   `0424-acuse-archivo-0423-pr56-dictamen-condicionado-ferry-originales.md`
   — **18 213 B / 289 lineas / CR=0**, blob `bdef5bb5`, sha256
   `e17cfc4546f7a2d7692cb24c00e5a36262a7c792067f4bc5424ffc1530e48c4b`; el
   paquete, `PAQUETE-from-glm-0424-acuse-GLM-20261120.zip` — **38 798 B /
   16 miembros**, sha256
   `7cd51e2bba74c3d5ae95f3284f67f622e31277a07e4bb8ae1056df6053dd7642`.

David los lleva al sandbox de Deepseek; los miembros se archivan bajo
`from-glm/files/0422/`, `/0423/` y `/0424/` (convencion del `0388-errata`)
en los commits que el elija — o quedan declarados parciales, verificables
por estos hashes. Con el ferry montado, las erratas de transcripcion dejan
de poder ocurrir.

## §5 El cierre (a): el parche R1+R2, forma exacta y validada

Extraido del head `9c86d76` (clon fresco), literal en la evidencia 03.
Tres ediciones, un commit:

- **AtmoShaderSource.kt** (la linea R1): `if (uShowIso) isoSum += isoB;`
  pasa a `if (uShowIso) isoSum += isoB * dt;` — `dt` esta en alcance
  (declarado antes del bucle, `segLen / uSteps`) y la forma replica la de
  `dR`/`dM`: integral, no suma por paso. La magnitud acumulada deja de
  escalar con el numero de pasos; las posiciones de las bandas no se mueven
  (dependen de odIso, que converge).
- **AtmoShaderSourceTest.kt** (el golden, misma linea): el contains de la
  forma vieja pasa a la nueva —
  `assertTrue(frag.contains("if (uShowIso) isoSum += isoB * dt;"))`.
- **AtmoShaderSourceTest.kt** (R2, dos contains nuevos, colocacion libre;
  propuesta: junto a los pines `ISO_BAND_*`):
  `assertTrue(frag.contains("if (logNe >= ISO_BAND_3) isoB = 1.0;"))` y
  `assertTrue(frag.contains("else if (logNe >= ISO_BAND_1) isoB = 0.5;"))`.
  El 0.75 intermedio queda encerrado por la cadena if/else entre ambos
  pines y los `ISO_BAND_*` ya pinnados; si el implementador prefiere pinnar
  tambien el peldano medio, valido — el delta se inspecciona igual.

Validado aqui: auto-consistencia (la forma nueva esta, la vieja fuera, la
escalera pinnada) y `git apply --check` en un worktree `--detach` al head
`9c86d76`: **aplica limpio, delta 2 ficheros, +4/-2** (worktree limpio tras
revertir; instrumento re-derivable en la evidencia 03 y el script de la
misma). Al aterrizar el commit, el head se mueve y mi dictamen se
re-verifica por inspeccion del delta minimo — todo lo demas queda firme por
el 0424. Si David prefiere el cierre (b) (desviacion registrada como deuda
exigible del primer commit de R4.6.3), lo elige por escrito. Sin (a) o (b),
el dictamen no es favorable.

## §6 Las anotaciones del cuerpo: tres lineas propuestas

Editables sin mover el head (0424 seccion 5.6 (ii)), en el estilo del latente
anotado — el cuerpo del PR o el to-glm que elijan:

1. **Proxy provisional**: «Proxy provisional: odIso = odR + odM (columna
   integral del propio raymarch) como proxy de la densidad electronica;
   des-normalizacion 8 + 4.5 * (odIso / 0.49), rango medido max 0.494 — a
   sustituir por el raymarch density de R4.6.3.» (el comentario del shader
   ya lo lleva; el cuerpo debe declararlo en una linea — 0423 seccion 5.3
   punto 2.)
2. **Anillos de limbo**: «Las bandas ISO se renderizan como anillos de
   limbo en el raymarch del shell atmosferico — nunca en la cortina (R4.5),
   sin cascarones 3D ni geometria nueva.» (canonica 0422 seccion 3.5.)
3. **Dominio del strength**: «ISO_STRENGTH: multiplicador escalar del
   termino `isoSum * uIsoColor * uIsoStrength`, sin clamp en el shader
   (verificado en el head); valor golden 0.75; la acotacion de UI se decide
   en R4.6.5 (gate visual).»

Y las erratas de ronda del cuerpo: corregir «acta 0423 (mia sobre
9c86d76)» por «acta de GLM (la 0424)» (0424 seccion 5.5) y el «hash: consultar
handoff» vago del punto 1 por los hashes de la seccion 4 de esta acta.

## §7 Erratas de la ronda, registradas

1. **Informe de Deepseek**: «acta 0424 archivada, `9dc0965`» — el 0424 NO
   esta archivado; medido hoy: HEAD = `9dc0965` (el commit del archivo del
   0423, transcripcion), sin `from-glm/0424` y sin to-glm/0435+. El
   dictamen le llego al informe por el mensaje via David, no por el relay.
2. **Informe de Deepseek** (tabla del ferry): la fila «Acta 0423 canonica»
   lleva el blob `23a95887` en «Medido» — es el blob de la transcripcion;
   la canonica es `041d21b3` (seccion 4.1).
3. **Informe de Deepseek**: «to-glo 264» — to-glm 264 (nombre; la cifra
   cuadra).
4. **Mias**: ninguna nueva esta ronda — las cuatro cifras de mi mensaje
   acompanante del 0424 (18 213 B / 289 lineas / `e17cfc45` y 38 798 B /
   `7cd51e2b`, mas las de los paquetes 0422/0423) re-verificadas hoy:
   todas cuadran.

## §8 Contadores previstos

- Estado hoy (`9dc0965`): arbol 883, from-glm 247/320/73, to-glm 264/562.
- Al aterrizar mi 0424: from-glm **248/321/73**, arbol **884**.
- Al aterrizar el informe de Deepseek (to-glm/0435 si nadie se le adelanta):
  to-glm **265/563**, arbol +1.
- Al aterrizar este 0425: from-glm **249/322/73**, arbol +1.
- Con los miembros del ferry archivados: files/ 73 -> **85** (+12, paquete
  0422) -> **96** (+11, paquete 0423) -> **112** (+16, paquete 0424);
  recursivo 320 -> 359; arbol +39 por los tres paquetes.
- Numeros libres: from-glm **0426** despues de este; to-glm **0435** para el
  informe si aterriza, **0436** despues.

## §9 Pendientes

1. **Ferry**: David lleva los cuatro originales al sandbox de Deepseek;
   Deepseek ejecuta el contrato (seccion 4) y archiva bajo `from-glm/files/`.
2. **R1+R2 (cierre (a))**: el parche literal de la seccion 5 en un commit,
   push de David; GLM re-verifica el delta minimo. O el cierre (b) por
   escrito.
3. **Anotaciones del cuerpo** (seccion 6) — editables sin mover el head.
4. **CI 3/3 via UI** — David (API anonima rate-limited, evidencia 05).
5. **Doble GO del merge**: mi mitad esta (0424, favorable condicionado);
   falta el **GO escrito de David** — la puerta sigue siendo suya (0422
   seccion 6, 0434 seccion 4).
6. **FPS de referencia** en `emulator-5554`, idealmente sobre el commit del
   merge, o declarando sobre cual se miden (0424 seccion 9.2).
7. **R4.6.3** tras el merge (worktree nuevo desde main actualizado);
   **R4.6.5** despues; deuda de forma del informe del emulador via cuerpo
   del PR o to-glm posterior (0424 seccion 9.5).

## §10 Estado

Informe recibido y verificado: el relay cuadra (`9dc0965`, 883/247/264), el
PR #56 sigue en el head `9c86d76` sin R1-fix, el readback del dictamen es
fiel y el handoff.py OK queda recibido como declaracion del implementador.
El ferry pedido esta LISTO: cuatro originales en INTERCAMBIO con el
contrato completo de esta acta, pre-verificado (10/9/14 entradas OK, cmp
identicos). El parche R1+R2 entregado en forma exacta y validado sobre el
head (aplica limpio, +4/-2). Una errata de atribucion registrada (el 0424
no esta archivado) y dos mas de forma. El dictamen sigue siendo FAVORABLE
CONDICIONADO: R1 por (a) o (b), R2 con R1, anotaciones del cuerpo, CI 3/3 y
el GO escrito de David. Este documento no contiene hash propio; la
declaracion de tamanos y hashes viaja en el mensaje acompanante.

— GLM (Z.ai), 2026-11-20 · responde al informe de Deepseek via David del
2026-11-20 (0423 archivada, dictamen leido, ferry pedido, relay cuadrado),
entrega el ferry pre-verificado y la forma exacta del parche R1+R2, y deja
la puerta del merge donde esta: en el GO escrito de David
