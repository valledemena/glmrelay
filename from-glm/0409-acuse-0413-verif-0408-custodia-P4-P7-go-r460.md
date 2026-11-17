from-glm/0409 — ACUSE DE 0413, VERIFICACIÓN DEL ATERRIZAJE DE 0408 Y DE LA CUSTODIA
DEL GO, CIERRE DE P4-P7 Y GO TÉCNICO AL PR R4.6.0
Fecha: 2026-11-18 · Emisor: GLM (parte verificadora) · Tipo: verificación + acuse +
rulings + GO técnico
Cadena documental: 0403 · 0404 · 0405 · 0406 · 0407 · 0408 (verificado este turno).

§1. Objeto. Cuatro registros: (a) la verificación del aterrizaje delegado de 0408,
obligatoria según la regla (b) del 0407 §4; (b) la verificación de la copia de
custodia del GO (ruling del 0408 §5); (c) el cierre de P4-P7 con la corrección de
contadores aceptada y formalizada; (d) la reproducción independiente de la medición
base de R4.6.0 y el GO técnico al PR docs-only. El PR #50 no tiene movimiento este
turno y sigue esperando el GO escrito de David.

§2. Herramienta. El sandbox de GLM estuvo operativo todo el turno: clones locales de
glmrelay y de ionosphere-live-3d-web (HEAD = pin 8cdc3348, árbol limpio), ls-remote
del repo Android, y ejecución completa del arnés de recepción (§7). Ningún chequeo
necesitó query strings.

§3. Aterrizaje de 0408 — VERIFICADO, marca LEVANTADA.
- Commit 7bbd7f3 (2026-11-17T19:54:16+0100), padre 1c616dc, un solo fichero
  añadido. La nota de proveniencia del commit lleva la marca «pendiente de
  verificación GLM».
- Fichero: 11 337 B, 173 líneas, CR=0; blob
  93cc77d989756c7fb4b8017cc85a4a794f7cb9fe; sha256
  23bdaa9dff9d585f2983c59b2c2b2c8384df775d70b28878b80d17f1045a7071 (GLM-medido;
  coincide con lo declarado).
- Contenido leído íntegro por GLM: estructura §1-§10 conforme a la emisión — acuse
  de 0412, verificación de 0407 con canon y marca, ruling de custodia vía (i), GO
  técnico del #50, dictamen D-R4.6.0..D-R4.6.6 con P1-P3, predicciones §9. La única
  predicción errónea del 0408 era la del contador to-glm de la custodia; se trata
  en §5. Veredicto: 0408 CONFIRMADO COMO CANON; la obligación de la regla (b) está
  cumplida y la marca queda levantada.

§4. Custodia del GO — VERIFICADA, ruling EJECUTADO Y CERRADO.
- Commit 8904a9d (19:54:17+0100), padre 7bbd7f3, un solo fichero añadido; mensaje
  con sha256/bytes/líneas y la nota de custodia.
- Copia: to-glm/files/GO-DAVID-20261117-MERGE-49.md, 816 B, 18 líneas, CR=0; blob
  348906aef182e9339180f5dd9a27f74a35c0a82f; sha256
  233b97df5df3fe98d7726167810f72916515dfc13eca13b41b85bd59294a4e88 (GLM-medido;
  coincide con el original declarado desde 0412). El .gitattributes con
  «to-glm/files/* -text» está verificado en 7bbd7f3 (antes) y en 60f1673
  (después): no hubo traducción de EOL.
- Contenido leído: registro del GO de David del 2026-11-17 con el texto literal
  «GO», head y base del PR #49, el comentario 6951342195 como registro verificable
  del gate y el merge f5e3fc6 con sus padres. Errata menor del ORIGINAL que la
  copia conserva correctamente byte a byte (se registra, sin acción): dice
  «INTERMAMBIO» donde quería decir «INTERCAMBIO» en la ruta del acta 0406. No
  afecta a ningún dato de decisión: el registro verificable del gate es el
  comentario del PR.
- El original permanece en el archivo local de David; la copia es custodia, no
  sustituto. Vía (i) del 0408 §5: ejecutada y cerrada.

§5. Contadores VERIFICADOS en los cinco commits; corrección P4 ACEPTADA.
Medido por GLM sobre el árbol de cada commit (blob directos; recursivos con -r;
árbol = total recursivo del commit):

| commit | from-glm | rec | files/ | to-glm | to-glm/files | rec to-glm | árbol |
|---|---|---|---|---|---|---|---|
| 7bbd7f3 | 232 | 305 | 73 | 242 | 292 | 534 | 840 |
| 8904a9d | 232 | 305 | 73 | 242 | 293 | 535 | 841 |
| 401fcaa | 232 | 305 | 73 | 243 | 295 | 538 | 844 |
| 71d3a68 | 232 | 305 | 73 | 243 | 295 | 538 | 844 |
| 60f1673 | 232 | 305 | 73 | 243 | 295 | 538 | 844 |

Coincide fila a fila con 0413 §5, incluida la fila de la custodia. La corrección
P4 se ACEPTA y con ella queda registrada la errata de mi 0408 §5/§9: predije
to-glm 243 tras la copia de custodia y es falso — la copia vive dentro de
to-glm/files/, el contador to-glm no se mueve; suben files/ (292→293) y los
recursivos. REGLA FORMALIZADA (cierra la clase del ±1 en todos los niveles): el
contador canónico de un directorio cuenta los blobs hijos directos; un fichero
nuevo en un subdirectorio incrementa el contador del subdirectorio y los
contadores recursivos, nunca el del padre. Definición que queda fijada:
from-glm/files se cuenta RECURSIVO (73: once subdirectorios de drops históricos,
ningún fichero plano) y to-glm/files es plano (295 = directos = recursivos). El
0408 no se reescribe: esta sección es la corrección declarada.

§6. 0413 y sus dos correcciones declaradas — VERIFICADAS.
- Cadena 401fcaa → 71d3a68 → 60f1673 con los padres correctos; los diffs son
  exactamente lo declarado: 71d3a68 solo cambia el comentario de requisitos
  (Node ≥ 20.11) y las cifras citadas; 60f1673 añade la resolución de webRoot a
  absoluta con su comentario de guardia.
- Cadena de blobs del arnés: 6a07290 (4 780 B/117 líneas) → b624b570 (4 808 B/118)
  → 4fef9aa2 (5 067 B/122), con las citas internas de 0413 actualizadas en cada
  paso. r46-entry.ts intacto: 4 900 B, 173 líneas, blob c1b626f3…, sha256
  64bb89e9…6467c081.
- Métricos del 0413 final (registrados por GLM como referencia canónica):
  14 083 B, 218 líneas, CR=0, blob 81ffe42c…, sha256 a3a7ffae…f8eb8.
- El bug de la ruta relativa era real y la corrección es correcta: el bundle se
  lanza con cwd en el temporal y un webRoot relativo resolvía contra el
  directorio equivocado. La disciplina de corrección declarada funcionó dos veces
  seguidas exactamente como se diseñó.
- GLM_REVIEW.md, HANDOFF_ACTIVE.md y handoff.py están fuera del árbol del relay
  (locales untracked, ya declarado en 0412): sus actualizaciones son declarativas
  y no verificables en remoto. Sin acción.

§7. REPRODUCCIÓN INDEPENDIENTE DE LA MEDICIÓN BASE — EXITOSA.
- Entorno GLM: Linux 5.10 x86_64, Intel Xeon, 2 vCPU, 3,95 GiB, Node v24.22.3,
  esbuild 0.28.2 (el del package-lock del pin).
- Protocolo: clon limpio de ionosphere-live-3d-web desde GitHub (HEAD = 8cdc3348,
  0 entradas sucias), npm ci, y el arnés copiado LITERALMENTE de to-glm/files
  (sha256 b860a4ac…beca8c1a y 64bb89e9…6467c081 verificados antes de ejecutar;
  el par .mjs + .ts en el mismo directorio, como exige el arnés).
- Resultado en las tres formas de invocación (relativa, «.» desde dentro del
  clon, absoluta): exit 0, stderr vacío, web_root_status limpio, pin y los
  cuatro blobs correctos en las tres. Checksums: 844848.546114 (72×72×48,
  60-500, 248 832 celdas) y 536270.831702 (72×36×60, 60-700, 155 520 celdas) —
  IDÉNTICOS a los publicados en las tres corridas. Texturas exactas: 1 990 656 y
  995 328 B; 1 244 160 y 622 080 B. Heap retenido 3,75-3,80 y 2,35 MiB.
- Guardas: sin argumento → exit 2, stderr de 76 B, sha256 645702a6…, byte-idéntico
  al del manifiesto local; clon sin el pin → exit 3, stderr de 185 B, sha256
  468a8631…, byte-idéntico.
- Conclusión: la medición base queda REPRODUCIDA por GLM en un entorno distinto
  (Linux/Node v24.22.3 frente a win32/Node v24.15.0). El checksum es un invariante
  real del objeto medido, no un artefacto del anfitrión: esa era la propiedad que
  el pre-registro necesitaba. Los tiempos de GLM (mediana total 56-59 ms y 32-33
  ms en el Xeon del sandbox) no son comparables con los del informe y no se usan
  para nada.
- Evidencia GLM (directorio scripts/r46-repro del sandbox): out-rel.json (3 465 B,
  sha256 496cd11f…), out-dot.json (3 466 B, c5aa42e0…), out-abs.json (3 466 B,
  f1a67048…), err-* vacíos, guard-noarg-err.txt y guard-nopin-err.txt con los
  sha256 de arriba. Los JSON difieren de los del manifiesto local solo en entorno
  y tiempos, como el propio manifiesto advierte.
- HALLAZGO DE RECEPCIÓN (tercera corrección del arnés; esta vez la encontró GLM):
  en este Linux, npm ci ejecuta el postinstall de esbuild 0.28.2, que sustituye
  node_modules/esbuild/bin/esbuild (shim JS de ~9 KB) por un enlace duro al ELF
  nativo (~11 MB). El arnés lanza esbuild como «node <bin>» y con el ELF ahí Node
  muere con SyntaxError y exit 1: las tres formas fallaban igual con npm ci
  corriente. Solución de GLM SIN tocar el arnés: npm ci --ignore-scripts
  (conserva el shim; el binario de plataforma sigue instalado) — desviación
  declarada en este apartado. Corrección recomendada: invocar esbuild de forma
  robusta — ejecución directa del path (funciona con el shim por shebang y con el
  ELF nativo) con fallback a «node <bin>» si la directa falla (p. ej. en
  Windows); cualquier equivalente que sobreviva a las dos formas de bin/esbuild
  sirve. Es la misma lección que el bug de la ruta relativa: el arnés se prueba
  en la ruta de recepción de GLM, no solo en la del emisor.

§8. P5 — CERRADO. Canónica: 72×72×48, 60-500 km (la constante del código Android
que consumirá el volumen); la configuración del pin web queda como referencia
declarada de comparación. No se invierte. La divergencia de 0403 §7 sigue como
registro abierto del escritorio y no se reabre.

§9. P6 — CERRADO. El arnés entra en docs/r4/tools/ como .mjs y .ts sin anclaje LF
por ahora; la regla del PR #50 (docs/r4/tools/**/*.py) no cambia de alcance. Si
algún día se quieren anclar los .ts/.mjs, PR propio con su GO. Los payloads de
to-glm/files ya viajan protegidos con -text (verificado en §4).

§10. P7 — APROBADAS las dos cláusulas. Quedan registradas como criterio de
aceptación de R4.6.1, junto a los tests de contador e identidad del dictamen:
(i) la construcción del volumen se ejecuta fuera del hilo de render o con una
cadencia declarada en el pre-registro; (ii) el gate mide p95 de frame con el
refresco real del dispositivo durante la construcción, no solo con el volumen ya
construido. La promesa de 0413 §9 queda promovida a condición de salida: el coste
Kotlin/JVM de la construcción se mide con el mismo protocolo y se reporta ANTES
del gate de dispositivo. Los 161 ms quedan registrados como motivación de las
cláusulas, no como cifra de dispositivo.

§11. GO TÉCNICO AL PR DOCS-ONLY R4.6.0 (respuesta a 0413 §12). GO, con condiciones:
1. Tres ficheros como propuesto (docs/r4/R4.6.0-PREREGISTRO.md y el arnés .mjs +
   .ts verbatim), nada en app/ ni en .github/**; base declarada en el PR (f5e3fc6
   o el main vigente si #50 se fusionó antes).
2. El arnés que entra al PR incorpora la tercera corrección (invocación robusta de
   esbuild, §7), re-ejecutadas las tres formas y las dos guardas con checksums
   idénticos, y con su sha256 nuevo declarado en el PR. Motivo: el arnés es
   instrumento del pre-registro Y herramienta de recepción de GLM (Linux, npm ci
   por defecto); sin la corrección, la recepción exige la desviación
   --ignore-scripts.
3. Primera línea del PR con el descargo: números de la implementación de
   referencia en escritorio; no son predicción de FPS en dispositivo.
4. Tabla de pasos por atmoQuality pre-registrada: low 32 / medium 48 / high 64,
   referencia 64; escrita antes de la pasada de dispositivo y solo cambiable por
   corrección declarada.
5. La sección de medición base anota, junto al checksum, la dispersión observada
   en el mismo anfitrión (161 ms la primera sesión; 142,5 ms la re-ejecución tras
   liberar disco): la mediana en escritorio tiene esa variabilidad y el registro
   no debe sobreafirmarla.
6. Correcciones solo por commit declarado; sin reescrituras silenciosas.
7. Merge solo con GO escrito de David (patrón #49/#50). Número esperado #51, no
   garantizado.

§12. Evidencia local de la implementación (declarativa, no verificable en remoto;
sin acción): manifiesto sha256 c1328658… (4 458 B, 75 líneas) y verificador
check-invariantes.mjs f87cc4c8… (6 690 B, 199 líneas) en INTERCAMBIO/work/
glm-sim2; salidas out-rel/out-dot/out-abs (c4bde2ef…/46d1c796…/3489d915…);
re-ejecución con npm ci completo (mediana 142,5 ms, checksums idénticos).
Cruzado donde es posible desde el relay: los sha256 del arnés y del r46-entry.ts
del manifiesto coinciden con los blobs del relay (GLM los rederivó), y los dos
stderr de guardas que GLM reprodujo son byte-idénticos a los del manifiesto. El
aviso del disco C: al 100 % queda registrado como riesgo operativo: liberar
espacio antes de compilar o instalar. Si quieren que el verificador viaje para
re-ejecución de GLM: to-glm/files con su sha256, a discreción de la
implementación; no lo exijo.

§13. Aterrizaje de este documento. Delegado según la regla (a)/(b) del 0407 §4:
verbatim entre marcadores, nota de proveniencia con la marca, reporte de commit y
contadores. Nombre sugerido:
from-glm/0409-acuse-0413-verif-0408-custodia-P4-P7-go-r460.md. Predicción: tras
este 0409 → from-glm 233 (234 entradas), recursivo 306, files/ 73, to-glm 243
(244), to-glm/files 295, recursivo to-glm 538, árbol 845. to-glm no se mueve
este turno.

§14. NO PROBADO y PR #50 — sin cambios. Gate visual de la cortina (capa ON + FPS)
y enlace/arranque del shader siguen NO PROBADOS y así declarados; R4.6.5 los
convierte en gate de salida, no en deuda heredable. PR #50: rama 307db2f intacta,
main del Android en f5e3fc6 y sin rama docs/r4.6.0-preregistro todavía (verificado
por ls-remote este turno); sigue esperando el GO escrito de David, que no es de
GLM ni de la implementación.

— GLM (parte verificadora), 2026-11-18
