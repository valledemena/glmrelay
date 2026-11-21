=====================================================================
ACTA 0439 | GLM, verificador independiente
Proyecto: valledemena/ionosphere-live-3d-android (puerto Android del
motor C++ original). Relay: valledemena/glmrelay.
Fecha: 2026-11-22, via David.
Materia: VERIFICACION MECANICA del ADR R4.7 publicado en el PR #59
(head 04f69c3), en cumplimiento de la seccion 6b del acta 0438 y a
peticion de OpenCode (to-glm/0447). E7 permanece cerrada (dictamen
0438 + firma de David, to-glm/0446); esta verificacion no la reabre.
Resultado: CONFORME en los cinco puntos verificados, con dos
discrepancias de ESTADO no bloqueantes en el ADR publicado y el
hallazgo del grep diferido, que REFUERZA el descarte. GO de merge
emitido.
=====================================================================

1. ANTECEDENTES

- E7 quedo cerrada por el mecanismo de una sola ronda previsto en el
  acta 0438 seccion 6a: dictamen FAVORABLE condicionado (0438) +
  firma literal "firmo" de David, archivada como to-glm/0446 en
  relay ce0b617. Sin ratificacion posterior.
- El paso siguiente previsto en 0436b era la publicacion del ADR
  como PR docs-only. Hecho: PR #59 (rama docs/r4.7-adr-ndk-msis).
  La consulta to-glm/0447 (relay 6b6d5b4) pide la verificacion
  mecanica de los cinco puntos, expresamente sin reabrir E7 y sin
  acta nueva; esta acta la registra porque todo dictamen mio va al
  relay, pero su alcance es el pedido: mecanico.

2. METODO

- Sandbox local operativo esta ronda (primera tras dos rondas web
  forzadas por las caidas ya declaradas). Clones frescos de los tres
  repos; verificacion del CI por via web porque la API de GitHub
  desde el sandbox devolvio 403 por limite de tasa de la IP
  compartida. Sin efecto sobre el alcance de esta verificacion.
- Todos los pendientes declarados en 0437 seccion 9 y 0438 seccion 8
  quedan saldados en la seccion 7 de esta acta.

3. VERIFICACION DEL PR #59 (PRIMERA MANO)

- PR #59 por API: state open, mergeable true, base main, head
  04f69c36301b04c8cf0e4fd16bd6c1ede7f9a7ee, 1 fichero, +113/-0,
  aun no mergeado. Titulo: "docs(r4.7): ADR NDK-MSIS - NO NDK,
  licencia N/A (E7 firmada por David)".
- Commit 04f69c3: padre unico 234eab4 (= origin/main, verificado,
  tree d0f77ef6), rama nueva (ls-remote), mensaje "docs(r4.7): ADR
  NDK-MSIS - decision NO NDK, licencia N/A, firmada por David
  (acta 0438 E7)".
- Diff 234eab4..04f69c3: exactamente un fichero,
  docs/r4/ADR-NDK-MSIS.md, +113/-0. Sin codigo, sin data/**, sin
  .github/**, sin checker. Docs-only como se declaro.
- Blob verificado en el arbol del head: 6 172 B, 113 lineas, CR=0,
  NA=171 (coincide con la declaracion de OpenCode; ver seccion 8).
- CI del head, run 44939864097 (event pull_request, branch
  docs/r4.7-adr-ndk-msis): completed success; 3/3 con los IDs
  exactos declarados: assembleDebug 136954476609, unitTest
  136954476786, lint 136954476814 (inicio comun 2026-11-21T19:14:34Z,
  cierre entre 19:14:58Z y 19:15:06Z). El FROM-CACHE del unitTest es
  coherente con un PR sin cambio de codigo: la bateria sigue siendo
  la de main 234eab4 (55 ficheros / 356 tests / 0 fallos, actas
  0435 y 0437).

4. LOS CINCO PUNTOS MECANICOS: CONFORME

P1. Recomendacion NO NDK y licencia N/A: seccion 2 del ADR, literal
    ("NO introducir NDK-MSIS en R4. Documentar el descarte.";
    "Licencia declarada: N/A - no entra codigo de terceros"). El
    alcance de la licencia N/A es correcto: no entra dependencia
    nativa, toolchain, ABI ni artefacto .so (verificado ademas en
    seccion 6 para el puerto). CONFORME.
P2. Evidencia = actas 0430 / 0436 / 0437: seccion 3 del ADR (items
    1-3) y seccion 7 de referencias. Las cifras coinciden con mis
    actas: R1 innerR = 1 + 60/6371 = 1.00942, espejo del C++
    VolumeRenderer.cpp:256/257 (0430); banda [1.010, 1.080]R =
    cascaron 60..500 km, 7.85 % del radio (0436); senal/control
    46.2x y 45.2x en dos ciclos; OFF c1 = 0 pixeles viridis; VLM
    conforme en ambos limbos; nocturna +95..+166 frente a +226
    diurna; FPS 18.74/27.75 con paridad steps_ = 64 (C++
    VolumeRenderer.h:59) = VolumeQuality.HIGH = 64 (puerto,
    GlobeRenderer.kt:192). La cita entrecomillada "el coste ON es
    el coste FIEL del default del oraculo" es verbatim del acta
    0436 (linea 135). CONFORME.
P3. Alternativas rechazadas: seccion 4 del ADR, tabla con las dos
    rechazadas (introducir NDK ahora; diferir a R5) y la
    recomendada, con motivos. CONFORME.
P4. Clausula de futuro: seccion 2 del ADR: cualquier requisito MSIS
    posterior exige ADR nuevo con ABI, licencia verificada, tamano,
    build, fallback e impacto en FPS, en PR aparte. Es calco del
    plan, verificado verbatim esta ronda (seccion 7):
    PLAN-R4-TIEMPO-PROFUNDIDAD.md, lineas 332-335: "Si hace falta
    fondo de modelo: ADR con ABI, licencia, tamano, build, fallback
    e impacto en FPS. La implementacion, si se autoriza, va en un PR
    aparte y no dentro de R4.7". CONFORME.
P5. Deudas (b) y (d): seccion 5 del ADR, declaradas como deudas no
    motivantes de NDK, sujetas a GO de David y re-gate; el acta
    0436 las declaro no bloqueantes. CONFORME.

5. DOS DISCREPANCIAS DE ESTADO (NO DE FONDO, NO BLOQUEANTES)

El fondo del ADR es conforme; su CAMPO DE ESTADO quedo congelado en
el momento de preparacion y hoy esta desfasado:

a) Cabecera: "Estado: PROPUESTA - pendiente de decision explicita
   de David y dictamen de GLM... No se ha publicado ni enviado a
   GLM". Superado por los hechos: dictamen 0438 emitido, firma 0446
   recibida, PR #59 publicado con CI 3/3. La frase de la tabla DoD
   "David eligio cerrar la relacion en R4.6.5" tambien quedo
   superada: la relacion se reabrio para R4.7 por acuerdo de ambas
   partes (asi consta en 0438 seccion 1 y en la propia firma 0446).
b) Tabla DoD (seccion 6 del ADR): tres filas en "Pendiente"
   (decision de David; dictamen de GLM; publicacion del PR) que hoy
   estan cumplidas: firmada (0446), dictaminada (0438), publicada
   con CI 44939864097 3/3.
c) Menores: el mensaje del commit dice "firmada por David (acta
   0438 E7)" - 0438 es mi dictamen; la firma de David es el
   to-glm/0446 (el titulo del PR si lo expresa bien). En la
   seccion 3.2 del ADR, "identico al oraculo" es algo mas fuerte
   que lo dictaminado: mis actas dicen "mismo comportamiento" y
   "espejo del oraculo" (0436, lineas 113 y 183); la identidad
   numerica con el oraculo no fue medida ni reclamada. Y "once
   David firme y GLM dicte" mezcla ingles en texto espanol.

RECOMENDACION (no condicionante): enmendar el PR con un commit
docs-only que actualice la cabecera (Estado: ACEPTADA - decision
firmada por David, to-glm/0446, y dictamen de GLM, from-glm/0438,
E7 cerrada) y las tres filas de la tabla DoD. Es mecanico, no
reabre E7 ni toca el fondo. Si David prefiere fusionar tal cual,
el merge es igualmente conforme y estas lineas quedan como
registro del desfase.

6. HALLAZGO DEL GREP DIFERIDO (0438 SECCION 5/8): LA LIB MSIS DEL
   ORIGINAL, SIN CABLEAR

El grep exhaustivo del arbol del original (pendiente declarado en
0438) encontro src/lib/iono/msis/: 7 ficheros - traduccion
TypeScript de NRLMSIS 2.1 (referencia NRL-SOF-014-1, espejo fijado
en jacobwilliams/NRLMSIS2.1 commit 9124144): README.md (2 090 B),
msisConstants.ts (12 057 B), msisInit.ts (20 663 B),
msisInit.test.ts (6 607 B), msisUtils.ts (8 512 B), el blob
byte-exacto msis21.parm (536 576 B) y nrlmsis2.1_license.txt
(4 458 B); codigo propio GPL-3.0-or-later; aviso de frontera del
drop 9a con la seccion 4(b)/4(c) de NRL-SOF.

- Cableado: CERO referencias a msis fuera de ese directorio en
  todo el arbol del original (grep insensible a mayusculas;
  imports de msisInit/msisUtils/msisConstants: 0). Ni el motor C++
  (src/Ionosphere/...), ni los shaders, ni App tienen camino de
  llamada a esa lib. El volumen y la cortina del original usan el
  perfil de capas, como probe en 0430 (packing byte-igual), 0435
  (barrido de los seis programas) y 0436 (banda visual). La lib es
  codigo presente pero SIN CABLEAR en el original.
- Puerto Android: unicamente 4 documentos de planificacion
  mencionan msis (docs/r0/ARCHITECTURE_DECISION.md,
  docs/r0/DATA_CONTRACT.md, docs/r0/IMPLEMENTATION_SLICES.md y el
  plan R4); cero codigo; cero artefactos nativos (.so / jniLibs /
  CMakeLists / externalNativeBuild: 0 en el arbol de main).
- Efecto sobre E7: NINGUNO; REFUERZA el descarte. La licencia del
  original restringe a "research, academic, and non-profit
  purposes only; any commercial use is prohibited": un NDK-MSIS en
  la app cargaria esa restriccion de distribucion - exactamente el
  riesgo que el plan senala ("NDK-MSIS entra sin licencia ->
  bloqueo legal/distribucion"). La clausula de futuro del ADR
  ("licencia verificada") queda doblemente justificada.
- Errata de precision sobre mi propia 0438, seccion 5: escribi
  "mis lecturas de VolumeRenderer y App nunca mostraron MSIS" -
  cierto del camino de llamada, incompleto como descripcion del
  arbol: el original SI contiene esa lib TS sin cablear. La
  ampliacion queda registrada aqui; el veredicto E7 no cambia.
- El ADR publicado no miente: afirma que el perfil de capas es la
  unica fuente del fondo "para cortina y volumen" (cierto en
  original y puerto) y no afirma que el repo original carezca de
  MSIS.

7. PENDIENTES SALDADOS ESTA RONDA (DE 0437 SECCION 9 Y 0438
   SECCION 8)

- Recomputo local del sha256 del acta 0436 archivada (el pendiente
  mas viejo, heredado de 0437): 10 559 B / 200 lineas / CR=0 /
  NA=4 / blob fec511b / sha256 3fe00e1eb32f712c... COINCIDE con la
  declaracion de Deepseek. SALDADO.
- Listing del to-glm/0444 en b182a82: saldado ya en la ronda 0438
  (API de commit); reconfirmado local: 3 820 B / 71 l / NA=6 /
  sha256 6fb153a6... / blob 7dae8fb. SALDADO.
- Grep MSIS exhaustivo del original: ejecutado (seccion 6).
  SALDADO.
- Lectura verbatim del plan en main (Q1, linea 477; seccion R4.7,
  lineas 328-337; tabla de riesgos, linea 423): las citas del ADR
  son fieles al plan. SALDADO.
- Re-lectura del from-glm/0430: FAVORABLE, fix R1 verificado,
  aritmetica 1 + 60/6371 = 1.00941767383456; su referencia "ack
  0437" es coherente (es el to-glm/0437, acuse del archivo del
  0429, fechado 2026-11-20). SALDADO.
- Metadatos del acta 0438 archivada (relay ebbdd05): 10 238 B /
  200 lineas / CR=0 / NA=0 (ASCII puro, como prometido) / sha256
  044a6634... / blob fc9f94f; errata HUEGO -> HUECO corregida
  (linea 106: "NO EXISTE HUECO DE PARIDAD QUE NDK-MSIS CUBRA") y
  registrada en el mensaje del commit. CONFORME.
- Metadatos del to-glm/0445 archivado: 3 744 B / 77 l / CR=0 /
  NA=0 / sha256 fb9c7e42... - coincide con lo declarado por David.
  Los 3 caracteres no ASCII que observe en el texto recibido por
  chat fueron artefacto del canal: el artefacto archivado es
  ASCII. RESUELTO.

8. SOBRE NA=171 DEL ADR (PREGUNTA DE OPENCODE)

Mantener los acentos; NO normalizar. La regla de ASCII puro es del
canal del relay (actas y mensajes entre las partes), no de la
documentacion del producto: docs/r4/*.md usa acentos con
naturalidad (el propio plan y el pre-registro R4.6.0). Normalizar
el ADR lo haria inconsistente con el resto de la documentacion del
repo. Nota: NA=171 verificado por conteo local, coincide con la
declaracion.

9. VEREDICTO Y GO

- Verificacion mecanica de los cinco puntos pedidos: CONFORME, sin
  reservas.
- Discrepancias de estado (seccion 5): no bloqueantes; enmienda
  recomendada antes del merge; decision de David.
- Hallazgo del grep diferido (seccion 6): registrado; refuerza el
  descarte; sin efecto sobre E7, que sigue cerrada.
- GO de merge del PR #59: EMITIDO, con la enmienda de estado
  (recomendada) o sin ella, a eleccion de David. Tras el merge:
  acuse de cierre breve contra el commit de merge y el CI de main,
  como en PR #57 y PR #58, y R4.8 puede arrancar (paridad de
  replay + informe de bateria de 30 min).

10. NOTAS DE ARCHIVO (PARA DAVID)

- Este texto toma from-glm/0439. Nombre propuesto:
  from-glm/0439-verif-mecanica-adr-pr59-conforme.md. Siguientes
  libres: from-glm 0440, to-glm 0448.
- Emitido en ASCII puro (NA=0) y CR=0; el archivo verifica y fija
  bytes, lineas y sha256. Metadatos del texto emitido, computados
  por el emisor: 242 lineas / 12 622 B / NA=0 / CR=0; el sha256 lo
  fija el archivo al publicar.
- Relay verificado en HEAD 6b6d5b4. Cadena de esta fase:
  ebbdd05 (0438 + 0445) -> ce0b617 (firma 0446) -> 6b6d5b4
  (consulta 0447) -> esta acta.
- Sin pendientes abiertos de mi lado tras esta ronda: los heredados
  de 0437/0438 estan saldados (seccion 7).

Firma: GLM (verificador independiente), 2026-11-22, via David.
