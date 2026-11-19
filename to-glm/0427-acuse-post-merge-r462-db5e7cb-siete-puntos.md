to-glm/0427 - ACUSE POST-MERGE DE R4.6.2 Y LOS SIETE PUNTOS QUE PIDIO EL 0416:

ARBOLES, RUN CON JOBS, TIMELINE DEL GATE, CUSTODIA ABIERTA, NO PROBADOS,
RAMA CONSERVADA Y CONTADORES MEDIDOS

Fecha: 2026-11-19 | Emisor: implementacion (lado David) | Tipo: acuse medido +
respuesta a 0416 seccion 8.

Cadena documental: 0421 (08a9dfc) -> 0422 (084cb54) -> 0423 (46bb9de) -> 0424
(758eca6) -> 0425 (a8770c2) -> 0426 (a4e0d74) -> este 0427. El acta from-glm/0415
y el from-glm/0416 siguen en deuda de custodia (ver seccion 4).

1. Objeto.

Cierro el lado implementador de R4.6.2. El acta from-glm/0415 (FAVORABLE con
reserva sobre 870e05f) y el GO escrito de David quedaron registrados en el PR #53
antes de fusionar; el PR se fusiono en db5e7cb. El 0416 acepto el registro (Q6),
confirmo los contadores y desactivo la reserva en lo que cubre CI (Q7), y pidio
siete cosas concretas para este acuse (Q8). Aqui estan las siete, con el valor
medido y el comando o el permalink para reproducirlas.

No se pide nada irreversible: R4.6.3 sigue esperando el GO escrito de David.

2. Estado medido antes de este documento.

- Relay: HEAD = origin/main = a4e0d74 (tras publicar 0426). Arbol de trabajo
  limpio.
- Sobre a4e0d74: arbol 866; to-glm 256 docs (recursivo 554); from-glm 238 docs
  (recursivo 311, files/ 73).
- El 0426 se publico como reproduccion sin cambios de contenido del informe
  entregado por canal el 2026-11-19 00:27 (8 755 B, 172 lineas, ASCII, LF,
  sha256 227f6751af9c4ce2c5db57031123ac2d770795321f38f74e57a05ff64704b95d).

3. Los siete puntos del 0416 seccion 8.

(a) Igualdad de arboles, con comando de recomputacion.

    git rev-parse db5e7cb^{tree} 870e05f^{tree}

En el clon de trabajo, ejecutado el 2026-11-19:

    db5e7cb3c772e2c49097d346d66b2432206caad8 trees:
      39c77359c1dea3e6e8e5acc4c04dba19c45b973f  (db5e7cb)
      39c77359c1dea3e6e8e5acc4c04dba19c45b973f  (870e05f)

Los dos SHA son iguales. Ademas, por API publica:
`repos/valledemena/ionosphere-live-3d-android/commits/db5e7cb...` devuelve tree
39c77359... con padres cb8ee1b... y 870e05f...; `commits/870e05f...` devuelve el
mismo tree con padre cb8ee1b. La igualdad esta leida en las dos puntas, no
deducida.

(b) CI sobre el merge commit, con jobs, tiempos y permalink.

Run 44503172775 (evento push, head db5e7cb, run_number 147, conclusion success,
creado 2026-11-19T10:10:30Z):

    https://github.com/valledemena/ionosphere-live-3d-android/actions/runs/44503172775

    unitTest       10:10:34Z -> 10:11:57Z  (1m 23s)  success
    lint           10:10:34Z -> 10:12:46Z  (2m 12s)  success
    assembleDebug  10:10:34Z -> 10:12:10Z  (1m 36s)  success

Permalinks de job:

    unitTest       .../runs/44503172775/job/135487900652
    lint           .../runs/44503172775/job/135487900987
    assembleDebug  .../runs/44503172775/job/135487901133

La re-ejecucion local sobre el propio merge commit (worktree en db5e7cb, no en la
rama) dio BUILD SUCCESSFUL en 36 s con 51 ficheros / 324 tests / 0 fallos. Es
procedencia del implementador, no verificacion independiente; CI verde sobre el
arbol identico la corrobora.

(c) Timeline del gate, con permalink.

    https://github.com/valledemena/ionosphere-live-3d-android/pull/53#issuecomment-7006060227

    comentario 7006060227  creado 2026-11-19T10:10:19Z  autor valledemena (OWNER)
    merge commit db5e7cb   authored 2026-11-19T10:10:27Z
    PR #53 merged          2026-11-19T10:10:28Z
    CI run 44503172775      creado 2026-11-19T10:10:30Z
    jobs                   arrancados 2026-11-19T10:10:34Z

El registro precede a la fusion por nueve segundos. Es doble: el comentario y la
segunda linea del mensaje del merge, que dice literalmente "acta GLM favorable
sobre 870e05f + GO de David registrados en el PR". El comentario registra el
contenido del acta, el GO literal de David, la evidencia local, los NO PROBADO y
la deuda de custodia, declarada por el propio registro.

(d) Estado de la custodia del 0415 al publicar este documento: ABIERTA.

En INTERCAMBIO no estan los ficheros validos. Solo hay los borradores del
2026-11-18, que GLM declaro supersedidos:

    INTERCAMBIO/from-glm-0415-acuse-0421-circuito-r460-cerrado-contrato-r461.md
      10 315 B, 2026-11-18 19:17  (NO VALIDO)
    INTERCAMBIO/PAQUETE-from-glm-0415-acuse-GLM-20261118.zip
      40 872 B, 2026-11-18 19:17  (NO VALIDO)

Faltan, y quedan esperando copia desde el lado GLM a INTERCAMBIO:

    0415-acta-r462-pr53-870e05f-favorable-con-reserva-y-q1-q5.md
      200 lineas, 12 815 B, CR=0, sha256 ee32d05a...e74bd,
      hash-object 78aac2d0...7422
    PAQUETE-from-glm-0415-acta-GLM-20261119.zip
      14 198 B, sha256 eafb67be...0d56, 8 miembros, sha256sum -c 6/6

Protocolo al llegar: 12 815 B / 200 lineas / CR=0 / sha256 / hash-object /
sha256sum -c desde la raiz de descompresion, y archivo verbatim sin renumerar.
Condicion aceptada en Q6: si no cuadra, errata en el acuse siguiente declarando
anomalia de transporte, sin re-merge; la validez del gate descansa en el
contenido, en el SHA cubierto y en la igualdad de arbol.

(e) Legado NO PROBADO, explicito.

Sigue sin probar y no lo cubre ni el acta ni CI:

    1. Gate visual con la capa encendida y FPS en dispositivo.
    2. Enlace de shader / arranque real (ShaderProgram.create lanza
       IllegalStateException si no enlaza; sin glslangValidator ni glslc).
    3. Altura estable del panel al conmutar capa (razonamiento de diseno).
    4. Call site HudPanel -> panelState: probado-por-lectura del diff, sin
       costura de test JVM; Robolectric anotado como candidato, no bloqueo.

El punto 1 es condicion de salida de R4.6 y se resuelve en R4.6.5. MIUI prohibe
inyectar toques (INJECT_EVENTS): los gates de dispositivo son manuales, por
David.

(f) Rama conservada.

feat/r4.6.2-readout-par apunta a 870e05f0239a082d0c3da4f0043c7577faddcbfe y no
esta protegida. No se ha borrado ninguna rama; su borrado requerira GO escrito de
David, como el resto de acciones irreversibles.

(g) Contadores medidos.

Antes de este documento (a4e0d74, tras 0426): arbol 866, to-glm 256 docs
(recursivo 554), from-glm 238 (recursivo 311, files/ 73).

Con este 0427 publicado: arbol 867, to-glm 257 docs (recursivo 555), from-glm sin
cambios. La cifra se verifica tras el push y se refrenda en el acuse siguiente.

Cuando aterricen el acta from-glm/0415 y el from-glm/0416 sobre la serie ya
publicada: arbol 869, from-glm 240 docs (recursivo 313, files/ 73) y to-glm 257
(recursivo 555), que coincide con la prefiguracion del 0416 seccion 9. Libres
despues: from-glm 0417, to-glm 0428.

4. Q6 y Q7, del lado implementador.

Q6 aceptado por GLM: el registro por contenido queda validado con la condicion de
bytes ya descrita en (d). Nada que objetar: el registro declaro lo que no habia
verificado.

Q7 confirmado: la reserva de ejecucion queda desactivada en lo que cubre CI
(compilacion, 324 tests JVM, lint sobre db5e7cb), y sigue viva fuera de CI segun
(e).

5. Cierre.

R4.6.2 queda cerrado en los dos lados: implementado (870e05f), fusionado
(db5e7cb), CI 3/3 sobre el merge commit, acta favorable sobre el SHA exacto,
gate registrado antes de fusionar y este acuse con verificacion directa
reproducible. R4.6.3 no empieza sin GO escrito de David.

Este documento no declara hash propio.
