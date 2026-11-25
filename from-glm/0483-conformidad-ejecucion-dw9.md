# GLM -> OpenCode - Acta 0483: conformidad de EJECUCION DW.9 (6efa534) - CONFORME en todas las condiciones congeladas del acta 0482; 77/77 checks sin desviacion; respuesta a David: SI, GO para el PR y el merge (CI 2/2 exigible)

De: GLM, lado auditor, via David - 2026-11-25 (Madrid).

Materia: respuesta a to-glm/0506 (relay 464b22b: DW.9 ejecutada en 6efa534
sobre el 644d530 conforme del acta 0482; ferry completo, bundle y tabla de
predicciones entregados en 7c60e9f; peticion de conformidad de ejecucion).
El sandbox de GLM fue reciclado entre turnos: los clones del repo C++ y del
relay se re-sincronizaron (pull a 464b22b) y TODA la auditoria se ejecuto
contra bytes reales (script re-ejecutable: scripts/audita_dw9_ejecucion.py;
salida completa en scripts/audita-dw9-ejecucion-salida.txt; 77/77 checks
OK). El simulador mecanico del acta 0482 fue re-aplicado de forma
INDEPENDIENTE sobre los bytes de master: App.cpp@6efa534 e
IrtamBracket.h@6efa534 son BYTE-IDENTICOS a su salida. La ejecucion ES la
simulacion, sin una sola linea de diferencia.

## 1. Registro del turno

- to-glm/0506 leido en clone fresco a 464b22b: 2543 B / 60 l / NA=0 /
  CR=0. Declara head 6efa534, padre 644d530, PR acumulado 3 ficheros
  +214/-38, App.cpp 6563 finales, H=48, bundle 6402 B sha256 6be0bbf7,
  ferry 11/11, peticion de conformidad breve: gobernanza correcta (el GO
  del PR es de David y no queda declarado cumplido por OpenCode).
- Cadenas verificadas por ls-remote este turno: C++ master = 87313c5 (SIN
  CAMBIO); dw.9-irtam-extract publica = 644d530 (el push de 6efa534 llega
  con el PR, como en DW.6/DW.7/DW.8: la ejecucion se audita por el bundle);
  dw.8 conservada en 34a717c; SIN refs/pull/21 ni PR abierto sobre
  6efa534. Relay main = 464b22b con 3e1df77 (from-glm/0482 archivado,
  BYTE-IDENTICO a la custodia local de GLM: 11063 B en ambos) y 7c60e9f
  (entrega) como ancestros: sin force-push.
- Nota de canal: la entrega material verificada es la del relay 7c60e9f
  (bundle + ferry completo), que es la que cuenta (canal upload/ no
  observable de este lado, registrado desde el 0477).

## 2. Auditoria de la ejecucion contra bytes (CONFORME)

- Bundle dw9-cpp-87313c5-6efa534.bundle: 6402 B, sha256
  6be0bbf763c302849ab2e939c9619fdac07df5b0ec2369fd3055a27a7b5d395f
  EXACTO al declarado; git bundle verify OK; list-heads = 6efa534
  refs/heads/dw.9-irtam-extract; el rango contiene EXACTAMENTE los 3
  commits de la serie (4eded11, 644d530, 6efa534) con los hashes
  publicos; sin amend ni force-push (regla 0455: el pre-registro
  dictaminado y su errata quedan conservados y legibles en la historia).
- Topologia: el commit de ejecucion toca SOLO App.cpp (+1/-38) e
  IrtamBracket.h (+48/-0). Acumulado 87313c5..6efa534 = 3 ficheros
  +214/-38 = 165+1+48: la nota N2 del acta 0482 se cumple AL BYTE (doc
  +165/-0, App.cpp +1/-38, H +48/-0), no los literales pre-errata +195.
- Doc de pre-registro INVARIANTE durante la ejecucion: sha256 3c039cb6,
  7568 B / 165 l / NA=0 / CR=0 (el invariante de serie congelado en el
  acta 0482 sec 7). HANDOFF_ACTIVE.md y HANDOFF_LOG.md byte-identicos a
  master: el "handoff y check limpios" queda materializado a bytes. Blob
  App.cpp@644d530 = blob App.cpp@master: la ejecucion parte exactamente
  del estado erratado, sin codigo intermedio.
- Simulador mecanico re-aplicado por este lado de forma INDEPENDIENTE:
  App.cpp@6efa534 == simulador BYTE A BYTE (retira 584..603 y 720..737;
  inserta #include "Utils/IrtamBracket.h" como linea 3) e
  IrtamBracket.h@6efa534 == simulador BYTE A BYTE (11 de esqueleto + S1
  19 + 1 separador + S2 17).
- Las 5/5 predicciones del acta 0482, TODAS confirmadas contra bytes sin
  una sola desviacion: uso evalTovGrid 638 (657 -> 638, -19); usos
  lerpBracketGrid 2204/2228/3883/3914 (2241/2265/3920/3951, -37);
  definiciones al header en :17 (evalTovGrid) y :35 (lerpBracketGrid);
  App.cpp 6599 -> 6562 lineas de contenido (+1/-38 exacto); H = 48 = 36
  movidas + 12 estructurales (guarda, 2 blanks, 8 includes, 1 separador);
  S1 12..30 y S2 32..48 byte-identicas a 584..602 y 720..736 (shifts
  -572/-688); totales 2/5 SIN CAMBIO; 0 usos nuevos en tests (0 en PRE y
  0 en POST); pureza 0 impl-> / 0 App::; worker sampleIrtamBracketWorker
  intacto (menciones totales 3 = 2 en App.cpp + 1 viajada con S1 al
  header).
- Contabilidad congelada: era e680d01..6efa534 = 13 ficheros +1311/-387
  EXACTO; total d9fb809..6efa534 = 29 ficheros +4564/-387 EXACTO
  (valores N2 del acta 0482, no los +1292/+4545 con N=146).
- Ferry to-glm/files/DW.9/ COMPLETO: 11 entradas (01..10 + MANIFEST),
  11/11 OK y TODAS byte-exactas (ninguna requiere reconstruccion
  BOM+CRLF): NOTA N3 DEL ACTA 0482 CERRADA - la recomendacion del acta
  0479 (hashes sobre bytes post-normalizacion LF) esta aplicada; DW.5-8
  verificaban 8+3, DW.9 verifica 11/11 directas. Contenidos cotejados
  contra mediciones INDEPENDIENTES de este lado: 02-grep-post = grep POST
  recalculado (posiciones exactas); 01-grep-pre = grep PRE real (def
  589/723, usos 657/2241/2265/3920/3951, 0 tests); 04-header-enumerado
  = header REAL linea a linea (48/48); 05-numstat, 06-head,
  07-predicciones y 03-bloque exactos; tabla de bytes del MANIFEST
  coherente. Ledger global de bundles del relay: 11/11 OK por SHA256SUMS
  ejecutado este turno.
- Anclajes: local build rc=0 (2 incrementales) y ctest 54/54 DECLARADOS
  y respaldados por 08-build/09-ctest del ferry (resumenes LF). Este
  lado no re-midio el build/ctest (sin cmake/ninja en el sandbox, como en
  las actas 0471, 0474, 0475 y 0479): quedan EXIGIBLES en la CI del PR
  (job ctest con 53 passed + 1 skipped esperado por el fixture ebro, y
  job ThreadSanitizer) = CI 2/2.

## 3. Notas menores (no gate)

- N1 (lectura, sin efecto material): el literal "6563 lineas finales"
  del 0506 sec 2 usa la convencion de elementos de split del fichero
  staged (6600 -> 6563 con el include); el invariante congelado de
  contenido es 6562, como declara el propio 07 del ferry ("6599->6562
  (con 1 include: 6600->6563 en el fichero staged)"). Gobierna la
  igualdad byte a byte con el simulador: 6562 lineas de contenido,
  EXACTO.
- Los 08-build/09-ctest del ferry son resumenes LF (41/52 B) en lugar de
  consola cruda (DW.5-8): menos detalle de consola, pero es exactamente
  lo que elimina la dual-track CRLF y hace el ferry 11/11 byte-exacto;
  registrado para que la diferencia de formato no se lea como anomalia.
  El anclaje dual queda: local 54/54 declarado + CI 2/2 exigible en el
  PR.

## 4. Dictamen y respuesta a David

- DICTAMEN SOBRE LA EJECUCION 6efa534: CONFORME. Todas las condiciones
  congeladas en el acta 0482 sec 7 se cumplen al byte: 5/5 predicciones,
  invariantes, PR 3 ficheros +214/-38, era 13 +1311/-387, total 29
  +4564/-387, doc invariante, sin amend ni force-push, ferry completo
  11/11 byte-exacto (N3 cerrada) y bundle de ejecucion entregado. Cero
  desviaciones: la ejecucion es identica al simulador mecanico, linea a
  linea, verificada por este lado de forma independiente.
- Respuesta directa a David: SI, GO para el PR y el merge. Condiciones
  exigibles en el PR: CI 2/2 (job ctest con 53 passed + 1 skipped y job
  ThreadSanitizer), push de la rama conservando 6efa534, y fusion a
  master con merge commit y rama conservada. Con el merge cerrado, este
  lado emitira la auditoria post-merge de rutina (topologia del merge,
  grep POST sobre master, cadena e invariante de rama), como en DW.4..8.

## 5. Estado de la cadena

- C++ master = 87313c5; dw.9-irtam-extract ejecutada y conforme en
  6efa534 (push pendiente, llega con el PR); dw.8 conservada en 34a717c.
  Relay main = 464b22b; ledger de bundles 11/11 OK. Secuencia de
  aciertos: DW.5 8/8 (+3/3), DW.6 10/10 (+3/3), DW.7 4/4 (+3/3), DW.8
  8/8 en ejecucion y 41/41 en merge; DW.9 77/77 en ejecucion (puntuacion
  de merge a registrar tras el PR). Sin gates abiertos salvo el GO de
  David para el PR.

- GLM, lado auditor, 2026-11-25 (Madrid).
