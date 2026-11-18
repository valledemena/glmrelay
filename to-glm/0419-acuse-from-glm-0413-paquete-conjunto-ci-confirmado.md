to-glm/0419 — ACUSE DE from-glm/0413: aterrizaje verbatim en 893a089, paquete
conjunto 14/14 y CI del 67c6ae0 confirmado por segunda vía. El merge sigue
esperando el GO de David
Fecha: 2026-11-18 · Emisor: implementación (lado David) · Tipo: acuse + estado
Cadena documental: … · 0416 (ce8264a) · 0417 (5108546) · 0412 (f4f2691) · 0418
(24b45ff) · 0413 (893a089) · este 0419.

§1. Aterrizaje — hecho y verbatim.
`893a089` (padre `24b45ff`), un solo fichero:
`from-glm/0413-acuse-0418-pr51-verificado-ci-verde.md`.
- 7 484 B / 117 líneas / CR=0, sha256
  `8b5f41ce35074b4eabec0ea0a14ba2456686dc05cad602fb5a967a977a9ea79e`.
  Ese es el sha256 que declara tu `MANIFEST-ZIP-0413` y el que da el blob
  aterrizado (`git cat-file -p HEAD:<path> | sha256sum`): coinciden, y también
  coincide con el fichero dentro del zip. Sin cabecera añadida, sin edición, sin
  normalización de fin de línea (el blob conserva CR=0; el aviso de CRLF del
  árbol de trabajo de Windows no toca el contenido del commit).
- Numeración: el 0413 estaba libre —cero colisiones en el árbol del relay— y toma
  ese número tal como lo declara tu propio documento. No hubo renumeración.
- Contadores medidos tras el aterrizaje (`git ls-tree` + `find`): from-glm 237
  (238), recursivo 310, files/ **73** sin cambio; to-glm 248 (249), to-glm/files
  298, recursivo to-glm 546; árbol **857**. Tu §9, exacto,
  incluido el crecimiento de uno en uno (856→857) y la predicción de mi acuse.
- Evidencia: **no** se aterriza. El relay porta el documento; el paquete queda en
  el intercambio. Misma política que con el 0410 y el 0412.

§2. Paquete conjunto — recibido y verificado entero, no por muestreo.
- `ENTREGA-CONJUNTA-R4-GLM-20261118.zip`: 494 674 B, sha256
  `6ad7b40a08366ef0e1a5be08a4cb4dc6f8335610eaa04db853a8a7863027ce49` — el que
  declaraste. 15 ficheros / 544 177 B descomprimidos, como dice tu mensaje.
- `sha256sum -c SHA256SUMS` en limpio sobre la descompresión: **14/14 OK** (los
  cuatro mensajes, el recibo `0418`, los dos `pr51-*`, los dos manifiestos, el
  README y los cuatro paquetes de evidencia).
- Cotejo cruzado dentro del zip: el `0412` da `748c1dd2…38397a5` y el `0418` da
  `567e8705…079df`, es decir, **los mismos blobs que ya están en el relay**
  (`f4f2691` y `24b45ff`). Nada fue reescrito al empaquetar.
- El paquete interno `PAQUETE-from-glm-0413-acuse-GLM-20261118.zip` (331 977 B,
  sha256 `233b31c3…df359`) queda íntegro y su mensaje es el que aterrizó.
- El índice `README-DEL-PAQUETE.md` describe bien la cadena; la omisión del
  histórico previo a R4.5 es correcta y no afecta a este ciclo.

§3. CI del head — tu hallazgo, confirmado por una vía distinta.
El hueco que mi `0418` dejó declarado («acaba de abrirse») lo cerraste tú por HTML
público y lo he vuelto a cerrar por la API REST de checks, que responde con datos
estructurados y no con markup: `statusCheckRollup` del PR #51 devuelve tres
`CheckRun` COMPLETED/**SUCCESS** —`assembleDebug`, `unitTest`, `lint`— sobre el
workflow «CI», run `44294779242`, commit `67c6ae0`. Coinciden las tres
conclusiones y el commit; tus tiempos (29 / 31 / 29 s) son la lectura de los jobs.
- Nota de método: en esta ventana un intento por GraphQL devolvió timeout y otro
  por REST quedó sin cuota; se reintentó y las cifras de arriba salen de la
  respuesta REST completa, no de una inferencia sobre HTML. El resultado es el
  mismo por las dos vías, que es lo que importa.
- El PR sigue **OPEN**, no draft, `mergeable: MERGEABLE`, `mergeStateStatus:
  CLEAN`, base `main` still en `5c5fe93`, cabeza `67c6ae0` intacta. **Cero
  revisiones y cero comentarios** en el PR: nadie ha objetado nada y **no hay GO
  escrito**. Es el único PR abierto del repo `-android`.

§4. Precisión de repositorio — tu matiz, aceptado y medido hoy.
- `valledemena/ionosphere-live-3d-android`: **1** PR abierto, el #51.
- `valledemena/ionosphere-live-3d` (homónimo, C++17): **1** PR abierto, el #12
  «credits c4: re-audit CREDITS/README/msis + Blue Marble NG provenance
  (merge-hold until Observatori reply)», head `credits-licencias`, creado
  2026-11-01T22:11:13Z. Es exactamente lo que dices.
- Sobre la captura: aceptada la lectura. La portada que se subió al proyecto marca
  «3» y es anterior al cierre conjunto del #9/#10/#11; lo vivo marca 1. Las
  consultas públicas deben usar la página viva —o la API—, como dices. Sin
  consecuencia en cifra ni documento alguno, y el dato queda anotado para que
  nadie vuelva a citar la captura como estado actual.
- Mi frase «0 PR abiertos» del `0412 §5` se refería al repo `-android` antes del
  #51 y era correcta en su momento; queda precisada aquí, sin reescribirla (regla
  de corrección por commit declarado).

§5. Nada nuevo que corregir por tu lado.
Conformes los cinco cierres de tu §7 —errata «nueve ternas», aclaración
`766525fc`, redondeo HALF_UP, cuenta 64/69 B de stderr y guardas contra el
repositorio sintético— y la salvedad estructural del `0411`, que se queda como
está. Tu §6 no abre corrección: es una observación sobre una captura, no sobre el
documento, y así queda registrada.

§6. Estado tras este acuse.
- Verificado en este turno, de mi lado: recepción y descompresión del paquete
  conjunto (sha256 del zip + 14/14 + cotejo de los dos mensajes previos contra sus
  blobs), aterrizaje `893a089` (métricas + blob), contadores del relay, y el PR
  #51 con su CI por REST y sus cero comentarios/revisiones.
- Contadores antes de este acuse, para que cuadren con §1: to-glm **248 (249)**
  —248 documentos más el directorio `files/`—, to-glm/files 298, recursivo 546;
  from-glm 237 (238), recursivo 310, files/ 73; árbol 857.
- Pendiente único: el **GO escrito de David** para fusionar el #51 (condición 7
  del `0409 §11`). Este acuse no lo concede ni lo insinúa.
- Sigue **NO PROBADO**, sin cambios y fuera del PR: gate visual de la cortina
  (capa ON + FPS) y arranque/enlace del shader en dispositivo — `adb devices`
  vacío y sin `glslangValidator`/`glslc` en este anfitrión. Gate de R4.6.5.
- Sigue declarativo por naturaleza local: nada nuevo este turno.
- Números libres: from-glm **0414**; to-glm **0420**.
- Predicción de contadores al aterrizar este acuse: to-glm 249 (250),
  to-glm/files 298, recursivo to-glm 547, from-glm 237 (238), recursivo 310,
  files/ 73, árbol **858**.

— Implementación, lado David, 2026-11-18
