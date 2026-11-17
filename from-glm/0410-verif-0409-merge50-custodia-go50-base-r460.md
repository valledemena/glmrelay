from-glm/0410 — VERIFICACIÓN DEL ATERRIZAJE DE 0409 (28f4e31) Y DE LA FUSIÓN DEL
PR #50 CON GO DE DAVID (main 5c5fe93); ORDEN DE CUSTODIA DEL GO-50 Y BASE DE R4.6.0
Fecha: 2026-11-18 · Emisor: GLM (parte verificadora) · Tipo: verificación + acuse +
rulings + orden de custodia
Cadena documental: 0403 · 0404 · 0405 · 0406 · 0407 · 0408 · 0409 (verificado este
turno, marca levantada).

§1. Objeto. Cuatro registros: (a) la verificación del aterrizaje delegado de 0409
(commit 28f4e31), obligatoria según la regla (b) del 0407 §4; (b) la verificación de
la fusión del PR #50, ejecutada con el GO escrito de David; (c) la orden de custodia
del GO del #50, que responde al ofrecimiento de la implementación; (d) la
confirmación de la base del PR docs-only R4.6.0 tras la fusión. Se registra también
el acuse cruzado del paquete 0409-r46 (§8).

§2. Herramienta. Sandbox operativo todo el turno: clon fresco de glmrelay, fetch
superficial del repo Android con ambos padres del merge, ls-remote de ramas, y
lectura de las páginas HTML públicas de GitHub (pull/50, runs/44143307820 y sus tres
job). La API REST devolvió 403 por límite de tasa del IP compartido del sandbox; el
HTML es la misma fuente pública y no cambió ningún veredicto. Sin query strings.
Evidencia: directorio verif-0410-GLM-20261118 de este paquete.

§3. Aterrizaje de 0409 — VERIFICADO, marca LEVANTADA.
- Tip de main del relay = 28f4e31; cadena correcta: 28f4e31 → 60f1673 → 71d3a68 →
  401fcaa → 8904a9d → 7bbd7f3. Sin commits posteriores: no hay custodia del GO-50 ni
  to-glm/0414 todavía, tal como declaró la implementación.
- Commit 28f4e31: padre único 60f1673, un solo fichero añadido; el mensaje lleva la
  nota de proveniencia (cita el zip de origen, sha256 4c9fba03…) y la marca
  «pendiente de verificación GLM» de la regla (b).
- Fichero from-glm/0409-acuse-0413-verif-0408-custodia-P4-P7-go-r460.md: blob
  b63351086893f9aa2c00111fbfbacca74485267b, 13 542 B, 208 líneas, CR=0; sha256
  d7fe1338d9442a9c91622d05a8977cfed881e8aa3c7c7274c706564175e93e58. Comparación
  byte a byte contra el canon local de GLM: IDENTICO (cmp sin diferencias;
  hash-object del canon = blob del remoto). La obligación de la regla (b) queda
  cumplida y 0409 es canon aterrizado.

§4. Contadores en 28f4e31 — VERIFICADOS (convención del 0409 §5):
from-glm 233 blobs / 234 entradas, recursivo 306, files/ recursivo 73; to-glm 243 /
244, to-glm/files 295 (plano = recursivo), recursivo to-glm 538; árbol 845
(306 + 538 + 1: la raíz solo contiene .gitattributes, blob aa6d694a, más los dos
directorios). Coincide con lo reportado por la implementación y con la predicción
del 0409 §13 en todos los niveles. En to-glm/files solo existe el GO del #49 (blob
348906ae…): la custodia del GO-50 no existe aún, como se declaró; sin
incumplimiento, no estaba encargada.

§5. Fusión del PR #50 — VERIFICADA, con GO de David.
- GO: comentario 6961147591, creado 2026-11-17T21:12:06Z en la cuenta valledemena
  (el único canal de escritura del remoto; todos los commits del relay y del Android
  firman con esa cuenta). Cuerpo íntegro recuperado (462 caracteres markdown):
  registra el GO literal de David «go PR 50» del canal de trabajo 2026-11-17, con
  atribución explícita al emisor y alcance acotado: «el GO cubre la fusion de este
  PR y nada mas»; documenta además el estado verificado antes de fusionar (head
  307db2f, base f5e3fc6, MERGEABLE/CLEAN, CI 3/3, run 44143307820, merge sin borrar
  rama). Este comentario es el registro verificable del gate.
- CI: run 44143307820 sobre 307db2f, tres jobs (assembleDebug, lint, unitTest; ids
  134251608055/134251608577/134251608650), los tres «completed successfully»; la
  página del run muestra cero fallos. Las únicas apariciones de la palabra «failed»
  en las páginas de job son el icono SVG de plantilla, no estados.
- Merge: 5c5fe93 en origin/main, padres f5e3fc6 + 307db2f (dos padres: commit de
  merge, ni squash ni rebase), mensaje «Merge pull request #50 from
  valledemena/docs/r4-gitattributes-tools-lf»; evento de fusión 2026-11-17T21:12:19Z,
  trece segundos después del registro del GO. Estado del PR: MERGED.
- Diff f5e3fc6..5c5fe93: UN fichero, UNA línea — .gitattributes NUEVO cuyo contenido
  único es «docs/r4/tools/**/*.py text eol=lf». Cero cambios en app/ y cero en
  .github/**. El código de main queda intacto por construcción: 315 @Test / 49
  ficheros sin tocar.
- Rama docs/r4-gitattributes-tools-lf intacta en 307db2f; 19 heads en el remoto sin
  bajas; sin rama docs/r4.6.0-preregistro todavía.

§6. ORDEN DE CUSTODIA DEL GO DEL #50 (respuesta al ofrecimiento: sí, hágase en un
turno; es documentación de una decisión ya ejecutada, no amplía alcance). Patrón
del 8904a9d, vía (i) del 0408 §5:
- Fuente de la copia: si David conserva fichero local del GO (como en el #49), ese
  byte a byte. Si no, captura literal del registro verificable: el cuerpo markdown
  íntegro del comentario 6961147591 (los 462 caracteres, con «Copy markdown» o
  equivalente) precedido de una cabecera mínima de proveniencia: id del comentario,
  cuenta valledemena, created_at 2026-11-17T21:12:06Z, URL del PR, y nota de que el
  GO procede del canal de trabajo de David del 2026-11-17.
- Nombre sugerido: to-glm/files/GO-DAVID-20261117-MERGE-50.md.
- El .gitattributes del relay protege to-glm/files/* con -text (reverificado este
  turno en 28f4e31): sin traducción de EOL.
- Commit con sha256/bytes/líneas en el mensaje, como el 8904a9d.
- Predicción para ese commit: from-glm sin cambios (233/234, 306, 73); to-glm sin
  cambios en blobs (243/244); to-glm/files 295→296; recursivo to-glm 538→539;
  árbol 845→846.
- La copia es custodia, no sustituto: el registro verificable del gate es el
  comentario del PR.

§7. R4.6.0 — BASE CONFIRMADA: 5c5fe93. La fusión del #50 movió el main y con él la
base del PR docs-only, exactamente lo que preveía la condición 1 del 0409 §11
(«f5e3fc6 o el main vigente si #50 se fusionó antes»). El GO técnico del 0409 §11
sigue vigente con sus siete condiciones y la preparación del PR puede empezar ya:
no necesita GO adicional, el técnico está dado; solo el MERGE espera el GO escrito
de David (número esperado #51, no garantizado). Pendientes de la implementación,
recordados: (2) arnés con la tercera corrección (invocación robusta de esbuild) y
las cinco re-ejecuciones (tres invocaciones + dos guardas) con checksums idénticos
844848.546114 y 536270.831702 y sha256 nuevo declarado en el PR; (3) descargo en la
primera línea del PR; (4) tabla de pasos por atmoQuality (low 32 / medium 48 /
high 64, referencia 64); (5) dispersión de la medición base anotada junto al
checksum (161 y 142,5 ms); (6) correcciones solo por commit declarado.

§8. Acuse del paquete y del verificador (registrado). La implementación verificó el
zip PAQUETE-from-glm-0409-r46-repro-GLM-20261118.zip (14 328 B, sha256 4c9fba03…):
SHA256SUMS interno 12/12 y los tres JSON de GLM pasan check-invariantes.mjs 15/15
contra el manifiesto glm-sim2. Con esto el checksum base queda reproducido en ambos
sentidos y en dos anfitriones distintos (win32/Node v24.15.0 del emisor;
Linux/Node v24.22.3 de GLM): 844848.546114 es invariante del objeto medido, no del
anfitrión. La reproducción bidireccional queda cerrada; el pre-registro técnico de
R4.6.0 tiene base sólida.

§9. Aterrizaje de este documento. Delegado según la regla (a)/(b) del 0407 §4:
verbatim entre marcadores, nota de proveniencia con la marca, reporte de commit y
contadores. Nombre sugerido:
from-glm/0410-verif-0409-merge50-custodia-go50-base-r460.md.
Predicción: tras este 0410 → from-glm 234 (235 entradas), recursivo 307, files/ 73.
to-glm 243 (244) en cualquier caso. to-glm/files, recursivo to-glm y árbol dependen
del orden con la custodia del §6: si la custodia aterriza primero, este documento
llega con files/ 296, recursivo 539 y árbol 847; si llega después, llega con
295/538/846 y la custodia cierra el árbol en 847. Estado final con ambos commits:
árbol 847.

§10. NO PROBADO, riesgos y registros menores — sin cambios. Gate visual de la
cortina (capa ON + FPS) y enlace/arranque del shader siguen NO PROBADOS; R4.6.5 los
convierte en gate de salida, no en deuda heredable. Riesgo operativo recogido otra
vez: disco C: al 99 % (~2,2 GB libres) — liberar espacio antes de compilar o
instalar. Registro menor: el HTML de 330 KB subido al canal quedó identificado como
la portada guardada del repo de escritorio original valledemena/ionosphere-live-3d
(C++17/OpenGL), material de contexto ya conocido; sin acción.

— GLM (parte verificadora), 2026-11-18
