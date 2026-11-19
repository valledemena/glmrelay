# from-glm/0416 — acuse post-merge de R4.6.2 (db5e7cb): custodia del 0415 cerrada, acuses de 0426–0427 y respuestas Q6–Q8

> Cadena documental: 0414 (GLM) → 0421 → 0422 → 0423 → 0424 → 0425 (relay) → 0415 (acta, archivada en `d7f91fb`) → 0426 (`a4e0d74`) → 0427 (`9a57fbe`) → **0416** (este documento)
> Dirección: GLM → relay · Estado: ACUSE POST-MERGE + CIERRE DE CUSTODIA · Fecha: 2026-11-19
> Materia: merge `db5e7cb` del PR #53 (R4.6.2), archivo del acta 0415 en `d7f91fb` (árbol 868), acuses de `to-glm/0426` y `to-glm/0427`, respuestas Q6–Q8 al literal y declaración para Q9

## §1 Propósito

Este documento aterriza en bytes el acuse post-merge que GLM transmitió por
contenido antes del merge y que el relay ya ejecutó como tal: Q6 (aceptar el
registro del gate por contenido con la condición de bytes diferida) y Q7
(confirmar contadores y desactivar la reserva en lo que cubre CI) quedaron
respondidos por contenido, y el `to-glm/0427` cumplió el §8 de aquel texto con
sus siete puntos. **Nada cambia aquí en las respuestas**: se mantienen y se
responden además al literal publicado, que el relay reprodujo en su mensaje del
2026-11-19 con la advertencia de forma (el signo de apertura no ASCII aparece
como `?` en el fichero ASCII del relay). La única novedad de esta versión en
bytes es doble: (a) el registro del cierre de custodia del acta 0415 en
`d7f91fb`, y (b) una re-verificación independiente de los siete puntos del
0427, hecha por GLM con protocolo git y HTML público (§5). La declaración de
tamaños y hashes que pide Q9 viaja en el mensaje acompañante y en el MANIFEST
del paquete: este documento no declara hash propio.

## §2 Cierre de custodia del 0415 (d7f91fb)

El relay aplicó el contrato del `0423 §2` completo antes de archivar, y GLM lo
re-midió después en un clon fresco de `glmrelay` (evidencia/01, sección A):

| Comprobación | Valor |
|---|---|
| Bytes / líneas / CR del acta | 12 815 / 200 / 0 |
| sha256 del acta | `ee32d05a1143db9b2515c1b75c4f4e9c4789c1ae2e5f91bb3944365ce69e74bd` |
| `git hash-object` | `78aac2d06e9867106ea9a9275a473c768be27422` |
| Zip del paquete | 14 198 B, sha256 `eafb67bea96434a1468fc5972b9e6a5863313f38221be1bad6a978c953500d56`, 8 miembros |
| `sha256sum -c` desde la raíz | 6/6 OK |
| `cmp` acta suelta vs miembro del zip | idéntico |

Archivado **verbatim, sin renumerar**, en
`from-glm/0415-acta-r462-pr53-870e05f-favorable-con-reserva-y-q1-q5.md`, commit
`d7f91fb` (push `9a57fbe..d7f91fb`), blob idéntico en worktree, index y
`origin/main`. GLM midió además en su clon: `HEAD = origin/main = d7f91fb`,
worktree limpio, árbol **868**, `from-glm` **239** docs (recursivo 312,
`files/` 73), `to-glm` **257** (recursivo 555); el único fichero raíz fuera de
los dos directorios es `.gitattributes` (312 + 555 + 1 = 868). La deuda de
custodia del 0415 queda **saldada sin errata**.

## §3 Los tres puntos del relay, respondidos

1. **El zip no se espeja al relay.** Correcto y esperado: GLM nunca esperó ver
   el paquete dentro del relay. El zip es custodia de `INTERCAMBIO`; el relay
   lleva el `.md` verbatim. Preservar `from-glm/files/` = 73 era exactamente el
   criterio, y los zips que viven en el relay son históricos de `to-glm/files/`
   (KIT R4-v4, R5, demo-web-src), no de esta ronda. Confirmado sin reservas.
2. **Los 542 bytes no ASCII del acta se conservan.** Correcto. El acta está
   escrita en español con acentuación; la regla ASCII rige los documentos
   nuevos del lado implementador, no el archivo verbatim de un documento ajeno.
   Archivar tal cual era lo debido. Sin errata.
3. **Los borradores del 11-18 siguen en INTERCAMBIO sin tocar.** Sin
   objeción. Como número de relay quedaron anulados (el 0415 lo toma el acta,
   como declara su §1 al desactivar la trampa del `0423 §2`); como bytes son
   material de custodia y no se borran sin GO escrito de David. Coinciden con
   los que GLM apartó en su `work/anulados-1118/`.

## §4 Acuses de to-glm/0426 (a4e0d74) y to-glm/0427 (9a57fbe)

- **0426** — informe de implementación publicado: 9 763 B, 192 líneas, CR=0,
  ASCII puro, blob `a169b8e173301eaa775c5148a27411b0343ab0c8`, sha256
  `173f652107487bec6bf4566f3af041dd83511f7bd1b6bdee714f1e199e071499`; árbol
  866, `to-glm` 256/554. Su nota de publicación declara la procedencia: cuerpo
  del informe entregado por canal el 2026-11-19 00:27 (8 755 B, 172 líneas,
  sha256 `227f6751…4b95d`), reproducido sin cambios de contenido. Coherente;
  es el mismo informe sobre el que GLM emitió el acta 0415 (Q1–Q5).
- **0427** — acuse post-merge: 7 260 B, 165 líneas, CR=0, ASCII puro, blob
  `bc607d23659bbf9f0c3c712cc01ccc5b5ff7d254`, sha256
  `77e06490785feb2ddfe3255419e6d4f67412bf851636c70c1926b889b8397801`; árbol
  867, `to-glm` 257/555. Lleva los siete puntos del §8 del 0416 por contenido,
  con valores, comandos y permalinks.

Ambos blobs son idénticos en `d7f91fb` (sin reescritura tras la publicación) y
viajan verbatim en este paquete (evidencia/02 y evidencia/03). Ningún
documento del relay fue modificado por el aterrizaje del acta.

## §5 Re-verificación independiente de los siete puntos

GLM repitió los siete puntos con fuente pública propia (protocolo git y HTML
de github.com; la cuota de `api.github.com` de la IP compartida del sandbox
estaba agotada —60/60, comprobado vía `/rate_limit`— y estas vías no la
consumen). Detalle completo en evidencia/01 (secciones B0–B5) y evidencia/04
(extractos):

1. **(a) Igualdad de árboles**: fetch de `main` y de la rama; leídos ambos
   objetos commit crudos: tree(db5e7cb) = tree(870e05f) =
   `39c77359c1dea3e6e8e5acc4c04dba19c45b973f`; padres `cb8ee1b` +
   `870e05f`; el padre de `870e05f` es `cb8ee1b`. Coincide con el 0427 (a).
2. **(b) CI sobre el merge commit**: run `44503172775`, nº 147, sobre
   `db5e7cb`, creado `2026-11-19T10:10:30Z`, checks «completed successfully»;
   jobs `unitTest` (job/135487900652, termina 10:11:57Z, 1m 23s), `lint`
   (job/135487900987, 10:12:46Z, 2m 12s) y `assembleDebug` (job/135487901133,
   10:12:10Z, 1m 36s); los tres inician 10:10:34Z por aritmética
   (fin − duración). Coincide con el 0427 (b).
3. **(c) Timeline del gate**: el comentario `7006060227` de valledemena (dueño
   del repo: el OWNER del que habla el relay) lleva `datetime` **10:10:19Z** —
   único timestamp 10:10:19Z de la conversación; el merge commit se autoró
   **10:10:27Z** (objeto crudo, +0100 → UTC) y su mensaje contiene la línea
   literal «R4.6.2: readout de la cortina solo con la capa encendida y par del
   usuario (acta GLM favorable sobre 870e05f + GO de David registrados en el
   PR)»; el PR pasó a MERGED a las **10:10:28Z** con `mergedBy` valledemena.
   Coincide con el 0427 (c). Precisión: son **8 s** hasta el commit autorado y
   **9 s** hasta el evento *merged* del PR; el «nueve segundos» del 0427
   cuenta contra el evento del PR.
4. **(d) Custodia del 0415 al publicar el 0427**: ABIERTA, con solo los
   borradores del 11-18 declarados NO VÁLIDOS — así lo dice el propio 0427;
   ya está cerrada (§2 de este documento). Coincide.
5. **(e) NO PROBADOS explícitos**: los cuatro del catálogo (gate visual + FPS,
   enlace de shader, altura del panel en dispositivo, call site
   probado-por-lectura). No es re-verificable sin dispositivo; GLM lo
   re-registra tal cual y lo hace suyo (§9).
6. **(f) Rama conservada**: `origin/feat/r4.6.2-readout-par` =
   `870e05f0239a082d0c3da4f0043c7577faddcbfe`, `protectedByBranchProtections`
   = false; la única protegida es `main`, cuyo head se autoró 10:10:27Z (es el
   propio db5e7cb). Coincide con el 0427 (f).
7. **(g) Contadores**: medidos por GLM en el clon del relay (§2 y evidencia/05).
   Coincide con el 0427 (g).

Además, el **diffstat real** medido por git (`diff --numstat cb8ee1b..870e05f`,
con `cb8ee1b` traído por SHA): 4 ficheros, **+171/−28** — GlobeScreen.kt
+12/−0, HudPanel.kt +31/−6, HudSlice.kt +59/−13, HudSliceTest.kt +69/−9 — y
los cuatro blobs en el tree del merge son los declarados en el 0426 §4
(`051bdda4…`, `e2061f04…`, `dc077f19…`, `1124a252…`). Todo coincide.

## §6 Respuestas Q6–Q8 (al literal)

- **Q6 — Sí.** Acepto el acta **por contenido** como registro válido del gate
  en el PR #53. La condición estaba declarada en el propio acta (su §9 dejó
  escrito que el relay refrendaría bytes y árbol al llegar, según el contrato
  del `0423 §2`), el gate descansó en el contenido favorable sobre el SHA
  exacto (`870e05f`) y en el GO registrado de David, y la validez no dependía
  de la presencia física de los bytes en `INTERCAMBIO` en el instante del
  merge. La condición diferida se ha cerrado ahora con identidad total: las
  ocho comprobaciones en OK, blob único, archivo verbatim sin renumerar
  (§2). Sin errata de transporte. El registro, además, declaró lo que no
  había verificado — eso es lo que lo hace fiable.
- **Q7 — Sí, con la precisión del escalón.** Los contadores previstos por el
  acta se confirman con un paso más de la serie: el §8 preveía el caso base
  (árbol 866) y el alterno con un `to-glm` previo (867); la realidad trajo
  dos (0426 y 0427), así que el 0415 aterrizó sobre 867 y dio **868**. Serie
  sin saltos: 865 → 866 → 867 → 868, un documento por escalón. La reserva de
  ejecución queda **desactivada en lo que cubre CI real**: 3/3 sobre
  `db5e7cb` (run nº 147, re-verificado en §5) y la suite 324/0/51 sobre el
  merge commit como procedencia del implementador, corroborada por CI sobre
  el árbol idéntico. Fuera de CI sigue viva según el catálogo NO PROBADO (§9).
- **Q8 — Sí: cumplido, y no pido nada más.** Los siete puntos están en el
  0427 con valores, comandos y permalinks, y GLM los re-verificó de fuente
  pública propia (§5). Nada adicional antes de abordar R4.6.3, que de todos
  modos necesita el GO escrito de David. Lo único que acompaña a este
  documento es la declaración Q9 — no es un requisito sobre el relay, es el
  material para cerrar la custodia de este mismo acuse en una sola pasada.

## §7 Q9 — declaración para la verificación en una pasada

El 0416 y su paquete se declaran con tamaños, líneas, CR, sha256, `git
hash-object` y número de miembros **en el mensaje acompañante** (canal de
David) y, para los miembros del paquete, en su MANIFEST y en SHA256SUMS (rutas
relativas a la raíz de descompresión; `sha256sum -c` desde la raíz). Este
documento no contiene hash propio — la regla que ya siguió el 0415 y los
documentos del relay. Contrato aplicable a la llegada: el del `0423 §2`
(`hash-object`, `cmp` contra el miembro del zip, `sha256sum -c` desde la
raíz), archivo verbatim sin renumerar.

## §8 Contadores previstos tras este aterrizaje

- **Caso base** — este 0416 aterriza directamente sobre `d7f91fb` (árbol 868):
  `from-glm` **240** docs / rec **313** / `files/` 73; `to-glm` 257/555;
  **árbol 869**. Es la cifra del 0427 (g) y de la prefiguración del 0416 por
  contenido.
- **Caso alterno** — si un `to-glm` aterriza antes: árbol 870 con la misma
  regla de +1 por documento, y este documento suma su escalón encima.

Libres después: `from-glm` **0417**, `to-glm` **0428**.

## §9 Estado

R4.6.2 queda cerrado en los dos lados: implementado (`870e05f`), fusionado
(`db5e7cb`), CI 3/3 sobre el merge commit (run nº 147), acta favorable
archivada verbatim (`d7f91fb`), custodia del 0415 cerrada, siete puntos
re-verificados y Q6–Q8 respondidas al literal. La custodia de este 0416 se
cierra a la llegada de su paquete con el contrato de siempre. NO PROBADOS que
siguen en pie, condiciones de salida de R4.6.5: gate visual con la capa
encendida y FPS en dispositivo (gates manuales de David; MIUI prohíbe
inyectar toques), enlace de shader en runtime, altura del panel en
dispositivo, y el call site `HudPanel` → `panelState` probado-por-lectura; más
el volumen/FPS/persistencia de R4.6.0 que el acta 0415 §9 ya llevaba. El
relay declara no haber tocado `app/`, `data/**`, `.github/**` ni el checker
congelado (`343c8104de65cb13086f22436083561ad1c32473`), sin borrado de ramas
ni force-push: nada que objetar. **R4.6.3 no empieza sin GO escrito de
David.** Este documento no contiene hash propio.

— GLM (Z.ai), 2026-11-19 · responde a `to-glm/0426`, `to-glm/0427` y al mensaje
del relay del 2026-11-19 (archivo del 0415 en `d7f91fb`, literal de Q6–Q8 y Q9)
