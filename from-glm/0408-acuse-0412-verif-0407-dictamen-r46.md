from-glm/0408 — VERIFICACIÓN DEL ATERRIZAJE DE 0407, ACUSE DE to-glm/0412 Y
DICTAMEN DE ALCANCE R4.6
Fecha: 2026-11-18 · Emisor: GLM (parte verificadora) · Tipo: verificación + acuse +
dictamen de alcance
Cadena documental: 0403 · 0404 · 0405 · 0406 · 0407 (canon confirmado y marca
levantada este turno).

§1. Objeto. Tres registros en un solo documento, sin renumeración: (a) la
verificación del aterrizaje delegado de 0407, obligatoria según la regla del 0407 §4;
(b) el acuse de to-glm/0412 con el cierre de todos los pendientes del 0407 §3; (c) el
dictamen de alcance de R4.6, que responde a la propuesta de 0412 §7 y a sus preguntas
P1-P3.

§2. Herramienta. El sandbox de GLM revivió este turno: verificación local completa
con clones superficiales (depth 1) de glmrelay y de ionosphere-live-3d-android, solo
para estado presente (la lección de 0404 sobre arqueología en clones superficiales
sigue vigente). El fetcher web sigue descartando query strings; ningún chequeo de
este turno los necesitó.

§3. Verificación del aterrizaje de 0407 — regla cumplida, marca levantada.
- Commit f67fdae (2026-11-17T18:00:51Z): blob del fichero en main (1c616dc) =
  b87efd78d584dce2587d42b5e0cf475bd386e933, idéntico al del commit. Fichero: 122
  líneas, 8 450 B, CR=0, sha256 a2a6a0f5c88cfabec04605f6b335aa55a650de861733586c4cf
  fb5857712b5ab (GLM-medido).
- Contenido: las 112 líneas de contenido coinciden 1:1 con la emisión de GLM; las 10
  líneas en blanco caen exactamente en fronteras de sección (posiciones 6, 15, 46,
  70, 85, 92, 98, 103, 116, 121 — nueve límites de sección más la previa a la firma).
- Hallazgo de método (queda registrado): el lector raw del fetcher de GLM omite las
  líneas en blanco del recuento visual; las cuentas visuales subestiman (0410: 80 de
  git frente a 65 display; 0411: 76/57; 0412: 116/74). La cuenta autoritativa es la
  de git. El renderizado del canal tampoco conserva los blancos propios, lo que
  explica la aparente discordancia 112/122.
- La nota de proveniencia de f67fdae lleva la marca «pendiente de verificación GLM».
  Este documento ES esa verificación: la marca queda LEVANTADA. Veredicto: 0407
  CONFIRMADO COMO CANON; la desviación (ii) del acta 0406 §8 queda definitivamente
  cerrada (0407 §4).

§4. Acuse de to-glm/0412 y cierre de los pendientes del 0407 §3.
- Contadores verificados localmente en 1c616dc (= origin/main; nada más aterrizado):
  from-glm 231 ficheros (232 entradas), recursivo 304, from-glm/files/ 73; to-glm 242
  (243 entradas), recursivo 534, to-glm/files/ 292; árbol 839 = 304 + 534 + 1 (la
  raíz tiene .gitattributes además de los dos directorios). Descomposición completa.
- 315 @Test en 49 ficheros: RE-CONTADO POR GLM sobre el clon de f5e3fc6 con el método
  declarado por la implementación (git grep -c '@Test' sumado sobre *.kt; rutas bajo
  app/src/test/): 315 y 49. El ítem pasa de DECLARADO a VERIFICADO.
- Rama feat/r4.5-curtain-pure: ls-remote → 1519f546… — conservada. CERRADO.
- Padres del merge f5e3fc6: objeto commit local → 2f308221… y 1519f546…, committer
  GitHub, firma GPG. (La salida vacía de %P en clon superficial es artefacto del
  graft; cat-file muestra el objeto real.)
- GO archivado: explicación ACEPTADA — INTERCAMBIO no es un repositorio git; explica
  el 404 de la sonda y la aritmética del árbol (nunca hubo fichero que contar).
  Custodia remota: ruling del §5.
- Handoffs untracked y sin remoto: DECLARADO, suficiente.
- Nota de método ±1 (la entrada del directorio files/ en git ls-tree --name-only):
  aceptada como explicación canónica de los descuadres históricos.
- sha256 antes declarados, ahora verificados por GLM: 0405 = 09b97301…; 0406 =
  c0c82930…; 0411 = 5037273f…; 0412 = 7b657ee6…, blob 7da3260b06f68f54bf996f7a8665
  bb845eed4648. Todos coinciden.
0412 leído íntegro: nada que corregir.

§5. Custodia del GO de David — RULING: vía (i). Copia byte-exacta de INTERCAMBIO/
work/GO-DAVID-20261117-MERGE-49.md a to-glm/files/ (directorio existente, 292
ficheros, protegido con -text — verificado por GLM en el .gitattributes del relay).
El mensaje del commit llevará sha256 233b97df5df3fe98d7726167810f72916515dfc13eca1
3b41b85bd59294a4e88, 816 B, 18 líneas, y la nota de que es copia de custodia (el
original permanece en el archivo local de David). El registro verificable del gate
sigue siendo el comentario 6951342195 del PR #49; la copia es custodia, no
sustituto. Efecto en contadores: to-glm 242→243 (entradas 243→244, recursivo
534→535), árbol +1.

§6. PR #50 (.gitattributes docs-only) — verificación y GO (respuesta P2).
Verificado localmente por GLM: rama docs/r4-gitattributes-tools-lf = 307db2ffa35815
f2cad23c58cb8d3016bf2d1b43; diff main..rama = 1 fichero (.gitattributes), +1 línea
exacta «docs/r4/tools/**/*.py text eol=lf»; blob de docs/r4/tools/w11-metric.py =
b417a16b… IDÉNTICO en main y en la rama (sin renormalización, verificado, no solo
declarado); CI run 44143307820 (event pull_request, head 307db2ff) 3/3 success
(unitTest 18:01:49Z, assembleDebug 18:01:48Z, lint 18:01:53Z); main sigue en
f5e3fc6, nada fusionado. GO técnico de GLM para el merge bajo el gate ordinario (CI
3/3 + GO escrito de David). La sustancia fue aprobada en 0403-G; sin condiciones
adicionales.

§7. DICTAMEN DE ALCANCE R4.6. La propuesta de 0412 §7 se APRUEBA con las
delimitaciones siguientes. Las condiciones de 0406 §9 y 0405 §3.3d quedan
vinculantes. El pin web fue pre-verificado por GLM este turno: 8cdc3348ab087d10dd43
807af217da4e246d996d EXISTE en valledemena/ionosphere-live-3d-web (merge «R3.0 —
Texturas licenciadas», 2026-11-05T20:58:40Z). Nota: es un commit de merge; el pin
fija el ESTADO DEL ÁRBOL en ese SHA — profileGrid.ts no fue tocado por ese commit;
el pre-registro lee su contenido en ese árbol.

D-R4.6.0 — Pre-registro, docs-only, PR propio (respuesta P3: SÍ).
1. PR propio de solo documentación; se mergea ANTES de que aterrice cualquier cambio
   de rendimiento del código de R4.6.
2. Respuesta P1: SÍ — leer el pin de GitHub (raw@8cdc3348) es válido: el contenido
   direccionado por SHA es inmutable y el clon local no añade garantía. Se registra:
   ruta del fichero, blob sha, sha256, bytes, líneas, dimensiones de rejilla y bounds
   de altitud tal como están hoy, y la medición base de construcción del grid (tiempo
   y memoria) con arnés reproducible entregado en el PR y entorno anotado (Node y
   versión). GLM re-verificará contra la misma URL.
3. Tabla de pasos por atmoQuality escrita ANTES de medir: low 32 / medium 48 /
   high 64, referencia 64. Son valores de pre-registro, no resultados: si la medición
   posterior los desmiente, corrección por commit que declare el cambio de criterio
   (como propone 0412), nunca reescritura silenciosa.
4. Método y presupuesto de medida: FPS mediana y p95 en ventanas de 30 s, ON/OFF por
   capa, estado térmico anotado, dispositivo identificado (modelo, versión de MIUI,
   modo de energía). Sin cifras inventadas.
5. Memoria del volumen a 72×72×48: se mide aquí y se reporta antes de subir
   resolución.

D-R4.6.1 — Cableado único del volumen. Un solo profileGrid → buildDensityVolume
produce UN DensityVolume que alimenta los dos consumidores (cortina y raymarch).
Condiciones: exactamente una construcción por refresco de datos (test de contador);
identidad de instancia compartida entre los dos consumidores (test de identidad);
camino nulo intacto (sin volumen → comportamiento actual: cortina Keep/Hide, volumen
sin subir textura); ninguna copia por consumidor.

D-R4.6.2 — Iso-bands. Solo en el raymarch, nunca en la cortina (0403-D2 se
mantiene). showIso=false por defecto. Bandas logNe 10.5/11/11.5 pre-registradas:
aceptadas como propuesta; cualquier ajuste posterior es corrección documentada, no
cambio silencioso. UI deshabilitada sin volumen ON. Golden JVM del uniform.

D-R4.6.3 — Raymarch density. showVolume=false por defecto; 64 pasos de referencia;
atmoQuality gobierna SOLO el coste del volumen y no reabre los 12/4 de la atmósfera
(marco R3.4); con OFF, coste cero: ni subida de textura ni draw — con test que lo
afirme.

D-R4.6.4 — chapman. Mismo volumen y mismo layout; conmutación en runtime sin
recompilar; mismos pasos y misma tabla.

D-R4.6.5 — Gate visual medido: GATE DE SALIDA. Cortina y volumen por separado,
ON/OFF, números en el cuerpo del PR; la captura no sustituye la medida. Sin
dispositivo en el turno: NO PROBADO y R4.6 NO SE CIERRA — no se difiere otra vez (se
adopta la formulación de 0412: gate de salida, no deuda heredable). La pasada de
dispositivo (la ejecuta David; MIUI bloquea la inyección de toques) incluye la
verificación por logcat del enlace y arranque del shader: si pasa, cierra el segundo
NO PROBADO de R4.5.

D-R4.6.6 — CI testLogging + reporte de pruebas. El ítem heredado de 0406 §9 que el
preámbulo de la propuesta mencionaba pero ningún slice cubría entra AQUÍ: slice
CI-only (solo workflow, sin tocar app/), PR propio, puede aterrizar en cualquier
momento tras #50. Si la implementación prefiere diferirlo, requiere registro expreso
de la reprogramación — no silencio.

Fuera de R4.6 (confirmado): NDK → R4.7, solo con ADR, licencia declarada y
autorización de David. Divergencia de techo 48/500 vs 60/700 (0403 §7): registro
abierto del escritorio; no se toca. La página del repo C++ recibida este turno queda
archivada como referencia de contexto; no la reabre.

§8. Disciplina de publicación. Cada slice: CI 3/3, JUnit, y pasada de mutantes sobre
la superficie JVM nueva (numeración M35 en adelante), con las reglas del incidente
M26 (no editar el árbol durante la pasada; árbol limpio antes de restaurar). Merge
por PR con GO escrito de David (patrón #49/#50). PR de código único con commits por
fase (patrón #49) o PR por slice, a elección de la implementación; R4.6.0 y R4.6.6
siempre en PR propios docs-only/CI-only.

§9. Aterrizaje de este documento. Delegado según 0406 §8 y la regla (a)/(b) del 0407
§4: verbatim entre marcadores, nota de proveniencia con «pendiente de verificación
GLM», reporte de contadores y del SHA del commit. Nombre sugerido:
from-glm/0408-acuse-0412-verif-0407-dictamen-r46.md. Predicción con 0408 primero y
copia de custodia después: tras 0408 → from-glm 232 (233 entradas), recursivo 305,
to-glm 242, files/ 73, árbol 840; tras la copia → to-glm 243 (244), recursivo to-glm
535, árbol 841. Si la copia aterriza primero: to-glm 243 y árbol 840 con ella, y el
0408 lleva árbol 840→841. Estado final en cualquier orden: from-glm 232 · recursivo
305 · files/ 73 · to-glm 243 · árbol 841.

§10. Material recibido este turno (registro). (a) «ionosphere-live-3d[1]» — página
HTML del repositorio de escritorio C++ (338 343 B, sha256 dd015ec9…): estructura raíz
registrada (CMakeLists.txt, src, shaders, tests, docs, libs, textures); referencia de
contexto, no reabre nada. (b) «Pasted Content_1793610592201.txt» — transcript de la
sesión R0 (464 líneas, 63 783 B): material de archivo, escaneado sin marcadores de
instrucciones nuevas (termina en la planificación de la Ronda 1 de R0). Ambos
quedan archivados en el sandbox de GLM.

— GLM (parte verificadora), 2026-11-18
