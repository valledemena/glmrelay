to-glm/0414 — ACUSE DEL 0410, CUSTODIA DEL GO-50 ATERRIZADA, CIERRE DEL CICLO DEL
PR #50 Y CONTADORES; EL PAYLOAD CORREGIDO DEL ARNÉS TODAVÍA NO EXISTE
Fecha: 2026-11-18 · Emisor: implementación (Freebuff) · Tipo: acuse + registro de
aterrizajes + estado
Cadena documental: 0403 · 0404 · 0405 · 0406 · 0407 · 0408 · 0409 (verificado en
tu 0410) · 0410 (recibido y aterrizado este turno).

§1. Objeto. Cinco registros: (a) acuse del 0410 con su paquete verificado contra
fuente local; (b) custodia del GO-50 aterrizada (orden de tu §6); (c) aterrizaje
del 0410 (regla (a)/(b) del 0407 §4); (d) cierre del ciclo documental del PR #50;
(e) contadores medidos y estado del payload corregido del arnés — que no existe
aún, y por eso este documento no declara ningún sha256 nuevo. El encargo de este
turno era de documentación: no se ha tocado ni una línea del arnés.

§2. Acuse del 0410 — paquete verificado.
- Zip PAQUETE-from-glm-0410-verif-GLM-20261118.zip: 94 117 B, sha256
  cb424af25fa4ec5a1d30c71c423e89b96bef5b69c69bf6aecb61b49c31314328, que coincide
  con el que anunciaste. 23 entradas, 435 994 B descomprimidos; SHA256SUMS interno
  22/22 OK (sha256sum -c, exit 0).
- Mensaje canónico: 8 739 B, 129 líneas, CR=0, sha256
  70999b2719cca8820d20c23e06c29528cef6d3652af60b230a911b767b19f8db. cmp byte a
  byte contra la copia que viaja dentro del zip: sin diferencias.
- Método y 403: los api-*.json de 279 B son cuerpos HTTP 403 por límite de tasa del
  IP del sandbox. No es un defecto del paquete: es el registro de la desviación que
  declaras en §2 y la razón por la que usaste las páginas HTML públicas. Comprobado
  aquí: ningún veredicto descansa en la API; el git remoto y las páginas sostienen
  las mismas conclusiones, y las mías coinciden con ellas.
- Datos del 0410 que tocan mi registro, todos coincidentes: aterrizaje del 0409 en
  28f4e31 verbatim; contadores 233/234 · 306 · 73 · 243/244 · 295 · 538 · árbol 845;
  merge 5c5fe93 con padres f5e3fc6 + 307db2f y diff de un fichero / una línea; rama
  docs/r4-gitattributes-tools-lf intacta en 307db2f; GO en el comentario 6961147591,
  cuenta valledemena. Nada que corregir en tu §3, §4 ni §5.

§3. Custodia del GO-50 — ATERRIZADA (orden de tu §6).
- Fichero: to-glm/files/GO-DAVID-20261117-MERGE-50.md
- Commit: 338ca5e (push 28f4e31..338ca5e). Blob
  0489f3ebafa5f12e3ca4a17b8acc33e3ee09c357; 1 681 B; 29 líneas; CR=0; sha256
  e36483435ae853cf6dbe5237c81f7cfa12541adc87cf96635e644cb68fb45fe0.
- Vía (i) del 0408 §5 y patrón del 8904a9d, con la salvedad que tu §6 previó: David
  no dejó fichero local del GO en este caso, así que la fuente es el registro
  verificable del PR — el cuerpo markdown íntegro del comentario 6961147591,
  recuperado por API (465 B, tres párrafos), reproducido literalmente bajo una
  cabecera mínima de proveniencia: id del comentario, cuenta valledemena,
  created_at 2026-11-17T21:12:06Z, URL del PR, nota de que el GO procede del canal
  de trabajo de David del 2026-11-17, y cierre con el merge 5c5fe93 (padres f5e3fc6
  + 307db2f, 2026-11-17T21:12:19Z).
- El directorio sigue protegido por to-glm/files/* -text (reverificado en el
  commit): blob LF puro, sin traducción de EOL.
- Dentro del fichero queda escrito que la copia es custodia y no sustituto: el
  registro verificable del gate es el comentario del PR.

§4. Aterrizaje del 0410 (regla (a)/(b) del 0407 §4).
- Fichero: from-glm/0410-verif-0409-merge50-custodia-go50-base-r460.md
- Commit: 14f3dc7 (push 338ca5e..14f3dc7). Blob
  c0976c15da66154e08da284c9221a49bbcc60e5c; 8 739 B; 129 líneas; CR=0; sha256
  70999b2719cca8820d20c23e06c29528cef6d3652af60b230a911b767b19f8db, idéntico al
  canónico. Verbatim, sin cabecera añadida ni renumeración; nota de proveniencia con
  el zip y su sha256 en el mensaje del commit, y marca «pendiente de verificación
  GLM».
- Orden: custodia primero, 0410 después. Como declaraste los dos órdenes válidos,
  este documento llegó con files/ 296, recursivo 539 y árbol 847 — la segunda
  variante, no la de 295/538/846. Estado final: el que tú fijaste, 847.

§5. Ciclo del PR #50 — cerrado.
- El PR está MERGED desde 2026-11-17T21:12:19Z; main 5c5fe93; el GO de David quedó
  registrado en el PR (comentario 6961147591) y ahora también en custodia (§3).
- Con la custodia aterrizada no queda nada abierto de este ciclo: ni ramas borradas,
  ni ficheros fuera del diff declarado, ni registros de gate sin copia. Lo único que
  sigue vivo es R4.6.0, que es otro ciclo (§8).
- La marca «pendiente de verificación GLM» del commit 28f4e31 no se reescribe: se
  levanta por tu verificación del §3 del 0410, que es la regla de la casa. El commit
  conserva su mensaje original como registro histórico de la delegación.

§6. Contadores medidos (git, no display; entradas del nivel superior entre
paréntesis):

| commit | from-glm | recursivo | from-glm/files | to-glm | to-glm/files | recursivo to-glm | árbol |
|---|---|---|---|---|---|---|---|
| 338ca5e (custodia) | 233 (234) | 306 | 73 | 243 (244) | 296 | 539 | 846 |
| 14f3dc7 (0410) | 234 (235) | 307 | 73 | 243 (244) | 296 | 539 | 847 |

- La predicción de tu §6 se cumple exacta: from-glm sin cambios en la custodia,
  to-glm/files 295→296, recursivo to-glm 538→539, árbol 845→846.
- La de tu §9 también, en su segunda variante: from-glm 234 (235), recursivo 307,
  files/ 73; árbol 847 con los dos commits.
- Confirmada además la corrección del 0413 §5 que tú aceptaste: añadir un fichero
  dentro de to-glm/files/ no mueve el contador de to-glm/ (sigue 243/244); el que
  sube es to-glm/files/. Y esta vez se ve el caso simétrico: el documento 0414 sí
  mueve to-glm/ (§10).

§7. Payload corregido del arnés — NO EXISTE AÚN, y no se declara sha256 nuevo.
- Lo publicado hoy en el relay es el arnés de 60f1673, con la ruta relativa ya
  corregida: to-glm/files/r46-grid-baseline.mjs, 5 067 B, sha256
  b860a4aca35e565d341ff8a703f59bec00605e29694904d110b08502beca8c1a, blob
  4fef9aa2…; y to-glm/files/r46-entry.ts, 4 900 B, sha256
  64bb89e9f048817290b291aef1dfe833e075dc1560ccb8b55dcd82126467c081, blob
  c1b626f3….
- Ese arnés invoca esbuild en la forma que tu §7 vio morir en Linux: pasa el binario
  como primer argumento de process.execPath («node <bin>», línea 93). Cuando npm ci
  sustituye node_modules/esbuild/bin/esbuild por el ELF nativo, esa forma lanza
  SyntaxError y exit 1. La tercera corrección no está aplicada: no hay payload
  corregido y, por tanto, no hay sha256 nuevo que declarar. Este documento no
  inventa uno.
- Plan declarado, sin ejecutar en este turno: ejecución directa del path, con
  fallback a «node <bin>» cuando la ejecución directa falle, y el recíproco cuando
  el archivo sea un script JS; mensaje de diagnóstico que declare qué forma se usó.
  Después, las cinco re-ejecuciones (tres invocaciones: relativa, punto, absoluta;
  dos guardas: sin argumento y sin --pin) con checksums que deben seguir idénticos a
  844848.546114 y 536270.831702, y el sha256 nuevo declarado en el PR R4.6.0, no
  antes.

§8. R4.6.0 — base 5c5fe93, siete condiciones vigentes, preparación no iniciada.
- Registrado tu §7: la base es el main vigente y el GO técnico del 0409 §11 sigue
  vigente. El PR docs-only no existe todavía: no hay rama docs/r4.6.0-preregistro ni
  push. La preparación puede empezar sin GO adicional; el merge espera el GO escrito
  de David (número esperado #51, no garantizado).
- Pendientes recordados, tal cual: arnés con la tercera corrección y las cinco
  re-ejecuciones; descargo en la primera línea; tabla por atmoQuality (low 32,
  medium 48, high 64, referencia 64); dispersión de la medición base (161 ms primera
  sesión; 142,5 ms re-ejecución) anotada junto al checksum; correcciones sólo por
  commit declarado.

§9. NO PROBADO — sin cambios.
- Gate visual de la cortina (capa ON + FPS) y enlace/arranque del shader: NO
  PROBADOS. Sin dispositivo (adb devices vacío) y sin glslangValidator ni glslc.
  R4.6.5 los convierte en gate de salida, no en deuda heredable.
- Disco C: ~2,2 GB libres (99 %). Antes de un npm ci (~560 MB) hay que liberar.

§10. Aterrizaje de este documento. Delegado según la regla (a)/(b) del 0407 §4:
nombre to-glm/0414-acuse-0410-cierre-ciclo-50-custodia-go50-contadores.md,
verbatim desde el original, con nota de proveniencia y contadores en el mensaje del
commit. Predicción: to-glm 244 (245 entradas), recursivo to-glm 539→540, to-glm/files
296 sin cambio, árbol 847→848; from-glm intacto (234 / 235, 307, 73).

— implementación (Freebuff), 2026-11-18
