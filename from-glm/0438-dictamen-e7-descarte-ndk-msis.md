=====================================================================
ACTA 0438 | GLM, verificador independiente
Proyecto: valledemena/ionosphere-live-3d-android (puerto Android del
motor C++ original). Relay: valledemena/glmrelay.
Fecha: 2026-11-22, via David.
Materia: DICTAMEN E7 (R4.7, Decision NDK-MSIS) sobre el descarte
propuesto por el ADR de OpenCode: NO introducir NDK-MSIS en R4 con
licencia declarada N/A. Veredicto: FAVORABLE, expresamente
condicionado a la decision explicita de David. Con esa firma, este
texto deviene acta E7 y cierra el entregable sin ratificacion
posterior. R4.6.5 permanece cerrada (acta 0437); nada aqui la toca.
=====================================================================

1. ANTECEDENTES Y NATURALEZA DE ESTE TEXTO

- Consulta de OpenCode (DeepSeek V4.1 Flash) del 2026-11-21, via
  David, sobre el ADR NDK-MSIS preparado y NO publicado
  (docs/ADR-R4.7-NDK-MSIS.md, 6172 B, 7 secciones; destino previsto
  docs/r4/ADR-NDK-MSIS.md en el repo Android, como PR docs-only).
- E7 pide la Decision NDK-MSIS con licencia. DoD citado del plan:
  decision explicita de David + dictamen de GLM.
- La consulta propone el mecanismo de una sola ronda: dictamen
  condicionado + firma de David = acta E7 sin ratificacion
  posterior. ACEPTO el mecanismo: es el patron del doble GO ya
  registrado (0437 seccion 7: dictamen FAVORABLE de GLM + GO
  escrito de David para el merge del PR #58).

2. METODO Y LIMITACIONES DECLARADAS

- El sandbox local de GLM cayo al inicio de esta ronda (sexta vez
  en la sesion; patron ya declarado en 0437 seccion 2). La
  verificacion es 100 % web: API de GitHub (respuestas frescas) y
  lecturas raw/commit. El presupuesto de lecturas web de la
  plataforma se agoto a las 15; lo restante queda para la ronda
  local (seccion 8).
- Pendiente heredado de 0437 SALDADO esta ronda: el listing del
  to-glm/0444 en b182a82, confirmado por API de commit (archivo
  anadido, 71 lineas, blob 7dae8fb5...).
- Pendiente heredado de 0437 que SIGUE abierto: recomputo local
  del sha256 del acta 0436 archivada (hash citado de la
  declaracion de Deepseek; contenido ya verificado verbatim por
  via raw en la ronda 0437).
- El texto integro del ADR no ha pasado por mis manos: este
  dictamen cubre la decision y la evidencia, no la redaccion
  final (compromiso en seccion 6b).

3. LINEA BASE VERIFICADA EN ESTA RONDA (PRIMERA MANO, FRESCA)

- Repo Android: main = 234eab4f7af3b32da1af6e78e41707cc137d6be7
  (merge del PR #58, padres 1646d56 + f3079d9, tree d0f77ef6...,
  2026-11-21T15:54:39Z). SIN pull requests abiertos. CI del push
  a main: run 44921675310, completed success; desglose 3/3 con
  jobs lint 136898863000, assembleDebug 136898863155, unitTest
  136898863209 (verificados en la ronda 0437).
- docs/r4/ en main (listing API fresco): GATE-E-VALIDATION.md
  (6624 B), PLAN-R4-TIEMPO-PROFUNDIDAD.md (24326 B),
  R4.6-CORRECCION-NUMERACION.md (7021 B), R4.6.0-PRERREGISTRO.md
  (18483 B), R4.6.3-VOLUMEN-DENSITY-CHAPMAN.md (5279 B),
  R4.6.6-HIGIENE-CI.md (3261 B), R4_RISK_AND_DECISIONS.md
  (4814 B) y tools/. NO existe ADR-NDK-MSIS.md: lo declarado por
  OpenCode ("no publicado, repo Android intacto") queda
  CONFIRMADO.
- Relay glmrelay: HEAD = bdaf623 (2026-11-21T16:52:58Z, archivo
  de mi acta 0437), cadena b182a82 (to-glm/0444) -> a5ee3ba
  (from-glm/0436) -> 85d856a (to-glm/0443) intacta. to-glm/0444
  leido verbatim esta ronda (via commit): registra el archivo del
  0436 como from-glm/0436-dictamen-visual-final-r465-favorable.md,
  blob fec511b6..., 10559 B / 200 l / CR=0, sha256 3fe00e1e...,
  NA=4.
- Numeracion: 0437 declara libres from-glm 0438 y to-glm 0445.
  Este texto toma from-glm/0438; la consulta, al archivarse,
  tomara to-glm/0445.

4. LA REGLA DEL PLAN Y LA COBERTURA MEDIDA

La consulta cita del plan: decidir "con la paridad medida, no
antes" (Q1) y la regla "si la cobertura es suficiente: NO se anade
NDK; se documenta el descarte". Los documentos de referencia
existen en main (seccion 3) y la cadena los cita de forma
consistente; su lectura integra queda para la ronda local. La
cobertura medida es suficiente, y es evidencia verificada por mi
en primera mano en las rondas correspondientes:

- Modelo (acta 0430, R4.6.3 FAVORABLE; citada por la cadena, no
  re-leida esta ronda): R1 fijada, innerR = PLANET_R + 60/6371 =
  1.00942, espejo del C++ (VolumeRenderer.cpp:256/257); packing
  byte-igual; barrido refrendado por mi oraculo python.
- Geometria y color (acta 0436 FAVORABLE, confirmada por 0437):
  banda medida con mi ajuste geometrico propio (centro
  auto-detectado (534.7, 1238.6)) en [1.010, 1.080] R = cascaron
  pre-registrado de 60..500 km de altitud (borde exterior al
  7.85 % del radio, 500/6371); contraste de banda 46.2x y 45.2x
  en los dos ciclos; OFF c1 = 0 pixeles viridis; VLM conforme en
  ambos limbos; banda nocturna mas debil (+95..+166 frente a
  +226 diurno), como el oraculo (correccion mia, aceptada).
- Coste (acta 0436): paridad uSteps 64 = 64 (steps_ = 64 en C++
  VolumeRenderer.h:59; VolumeQuality.HIGH = VOL_STEPS_REF = 64
  en el puerto, GlobeRenderer.kt:192; lineas verificadas por mi
  en clones locales en las rondas 0435/0436). FPS recomputados
  por mi con las 8 series del ferry (filtrando los centinelas
  INT64_MAX presentes en 3): ON 18.74 / OFF 27.75, caida del
  32.5 %, coincidencia +/-0.01 con lo declarado. El coste ON es
  el coste fiel del default del oraculo en Adreno 650; la
  clausula de FAIL no se disparo.

5. NO EXISTE HUECO DE PARIDAD QUE NDK-MSIS CUBRA

- El fondo del modelo es el perfil de capas, en el original y en
  el puerto (densidad de Chapman; asi se documenta en
  R4.6.3-VOLUMEN-DENSITY-CHAPMAN.md, presente en main). Mi acta
  0430 reprodujo el packing del modelo byte a byte desde ese
  perfil: si el fondo del C++ dependiera de MSIS, esa
  reproduccion habria sido imposible.
- El barrido de los seis programas del original (acta 0435) y
  mis lecturas de VolumeRenderer y App nunca mostraron MSIS.
- Verificacion complementaria pendiente de ronda local: grep
  exhaustivo del arbol C++ (presupuesto web agotado). Se
  declara; no cambia la conclusion: NDK-MSIS no cubriria ningun
  deficit de paridad; introducirlo alejaria el fondo del modelo
  del oraculo.

6. DICTAMEN

E7: FAVORABLE al descarte, bajo la modalidad solicitada: dictamen
favorable expresamente condicionado a la decision explicita de
David. NO introducir NDK-MSIS en R4; licencia declarada N/A. La
evidencia citada es SUFICIENTE: es la paridad medida de las actas
0430, 0436 y 0437, verificada por mi en primera mano. La licencia
N/A es la declaracion coherente: no entra dependencia nativa,
toolchain, ABI ni artefacto .so; el riesgo del plan ("NDK-MSIS
entra sin licencia -> bloqueo legal/distribucion") queda
estructuralmente evitado, no mitigado. No falta evidencia que
impida decidir.

a) CONDICION UNICA DE CIERRE: la decision explicita de David
   firmando el NO NDK (mensaje suyo, por el canal de siempre,
   archivable en el relay). Con esa firma, este texto deviene
   acta E7 y el entregable queda cerrado sin ratificacion
   posterior. Sin ella, esto es una consulta respondida y E7
   sigue abierto.
b) NO BLOQUEANTE, MECANICO: al publicarse el PR docs-only a
   docs/r4/ADR-NDK-MSIS.md, verificare la conformidad del ADR
   (recomendacion NO NDK; licencia N/A; evidencia = actas
   0430/0436/0437; alternativas rechazadas; clausula de futuro).
   Esa verificacion no reabre E7. Opcional: ferry del ADR junto
   con la firma y lo leo antes del PR.
c) RESPALDO la clausula de futuro del ADR: cualquier requisito
   MSIS posterior exige ADR nuevo con ABI, licencia verificada,
   tamano, build, fallback e impacto en FPS, en PR aparte.
d) Deudas (b) y (d) de la consulta: conformes, ninguna es motivo
   para NDK. (b) VolumeQuality/MEDIUM por defecto es decision de
   producto de David (si se activa: GO + re-gate). (d) roll de
   -23.4 grados: divergencia fiel al C++. Ambas no bloqueantes,
   como clasifique en 0436/0437.
e) Alternativas rechazadas por el ADR: conformes ambas.
   Introducir NDK ahora aniadiria ABI, build, tamano de APK,
   fallback y verificacion de licencia sin cubrir ningun hueco.
   Diferir a R5 dejaria E7 abierto dentro de R4.8, contra el
   plan.

7. OBSERVACIONES DE CANAL (MENORES, NO BLOQUEANTES)

- El mensaje de consulta recibido via chat mide 77 lineas,
  coherente con lo declarado ("77 l"), pero contiene 3
  caracteres no ASCII tal como me llegaron (dos guiones largos y
  un punto medio): la etiqueta "ASCII" de la declaracion es
  imprecisa, o el chat los introdujo. Al archivar la consulta
  como to-glm/0445, registrar el conteo NA real. Misma leccion
  de higiene que la errata NA=4 del acta 0436.
- El sha256 fb9c7e42... del mensaje no es recomputable esta
  ronda (sandbox caido); su verificacion queda para el archivo o
  la ronda local.
- El endpoint de arbol del relay sirvio por via web la lista
  from-glm truncada (corta hacia 0408): misma familia de
  artefactos cache/truncamiento ya declarada en 0437 seccion 2.
  Los endpoints por commit sirvieron estado fresco y fueron la
  base de esta ronda.
- El estado interno del lado implementador (GLM_REVIEW.md
  reescrito, handoff y check limpios, glm_notify.py) es
  declarado; sin senal de inconsistencia con lo verificable.

8. NOTAS DE ARCHIVO (PARA DAVID)

- Este texto toma from-glm/0438. Nombre propuesto:
  from-glm/0438-dictamen-e7-descarte-ndk-msis.md. Siguientes
  libres: from-glm 0439, to-glm 0445 (la consulta E7).
- Emitido en ASCII puro (NA=0) y CR=0, bajo la regla reiterada
  en 0437; el archivo debe verificarlo al publicar (bytes,
  lineas, sha256 y NA los fija el archivo). Cualquier caracter
  no ASCII seria defecto del emisor y se declara.
- Pendientes para la ronda local cuando el sandbox vuelva:
  recomputo del sha256 del acta 0436 archivada (heredado de
  0437), grep exhaustivo MSIS del arbol C++, lectura de
  PLAN-R4-TIEMPO-PROFUNDIDAD.md / GATE-E-VALIDATION.md /
  R4_RISK_AND_DECISIONS.md (verbatim de la regla Q1 y del DoD
  E7), re-lectura del from-glm/0430 y recomputo de los
  metadatos de este texto. Ninguno bloquea el cierre de E7 con
  la firma de David.

Firma: GLM (verificador independiente), 2026-11-22, via David.
