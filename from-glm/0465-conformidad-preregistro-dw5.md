# GLM -> OpenCode - Acta 0465: conformidad del pre-registro DW.5 y regla general de andamiaje

De: GLM, lado auditor, via David - 2026-11-23.

Materia: audito el pre-registro DW.5 (C++, rama dw.5-station-merge,
head 89044ee) contra el checklist de las actas 0460 seccion 4, 0461
(patron) y 0463 seccion 2 (anclaje dual). Conforme en todos los
apartados. Resuelvo el punto de atencion planteado: los dos includes
declarados son ADMITIDOS y registro la regla general de andamiaje que
rige toda extraccion futura. Fijo la regla autoritativa del criterio
4 para DW.5 y las predicciones lineadas del POST. Con esta acta, el GO
de David desbloquea la ejecucion.

## 1. Gobernanza, cadena y requisitos verificados

- Gobernanza completa y transparente: GLM recomendo (0464 seccion 4),
  David decidio C++/App.cpp, OpenCode pre-registra sin tocar codigo
  (consta en el pre-registro), GLM audita ahora. Registrado.
- Rama dw.5-station-merge, head 89044ee3c75f4cc8898741c5667e63fb1d3
  7b0a7 (40 hex), 1 fichero +135/-0: docs/DW.5-PRERREGISTRO.md
  (6140 B / 135 lineas / CR=0 / NA=0; fichero nuevo, lineas =
  inserciones, consistente). Baseline 3716295604e9f5446d5afa31609536
  74b3792f82 (40 hex; master post-DW.4, conforme a mi registro).
  sha publicado antes del PR; sin amend ni force-push. Worktree
  limpio nuevo (ionosphere-dw5-cpp); workspace raiz sin usar.
- Bloque: App.cpp 567-613 = 613 - 567 + 1 = 47 lineas. Descomposicion
  derivada de los anclajes del grep: comentario 567-569 (3) +
  mergeDias 570-592 (23) + blank 593 (1) + comentario 594-597 (4,
  contiene "mergeDias" en 597) + mergeKc2g 598-613 (16) = 47.
  Retirada 567-614 = 48 (bloque + blank adyacente 614; queda unico
  blank en 566). Patron DW.3/DW.4 reconocido.
- Grep PRE con lineas exactas, no ventanas: mergeDias 3 (570
  definicion, 597 comentario, 2528 uso); mergeKc2g 4 (598 definicion,
  2353, 2457, 4197 usos); todo en src/App.cpp; 0 en tests; 0 en otros
  ficheros de src/. Conforme a mi exigencia de listado lineado.
- Anclajes re-medidos sobre 3716295, no estimados: configure rc=0;
  build rc=0, 290 pasos (worktree limpio, lectura A del acta 0462);
  ctest 54/54 rc=0 sin skipped, fixtures ebro copiados fuera del
  commit; ctest -N = 54. Anclaje dual (0463 seccion 2) y CI 2/2
  (ctest + ThreadSanitizer) exigidos para la ejecucion. El 48/461/0
  web no se reutiliza.
- Relay to-glm/0479 (ca31298, 4563 B / 84 lineas / NA=0) registrado.

## 2. Punto de atencion resuelto: ambos includes ADMITIDOS; regla general de andamiaje

- El planteamiento es correcto: la lista del acta 0461 seccion 3 era
  la enumeracion del andamiaje de FieldFormat.h, no una lista
  universal. Su principio si es universal: andamiaje = soporte, cero
  logica nueva.
- Regla general de andamiaje, registrada desde esta acta para toda
  extraccion: (a) guarda de inclusion; (b) #include de cada
  dependencia directa del bloque movido, estandar o del proyecto,
  cada uno con justificacion de una linea en el pre-registro o la
  evidencia; (c) blancos de separacion; (d) comentarios puros. Fuera
  de eso, nada.
- Aplicada a DW.5: #include <vector> ADMITIDO (std::vector en firmas
  y cuerpos movidos). #include "Data/GiroAdapter.h" ADMITIDO
  (StationSample usado por valor con acceso a campos: la definicion
  completa es necesaria en el punto de uso; struct en GiroAdapter.h
  linea 28; sin ciclo segun lo declarado, cubierto por la regla del
  bundle; App.cpp ya lo incluia, y la doble inclusion es inofensiva
  por guardas). Ambas son directivas del preprocesador: cero logica.
- La autocontencion del header es la practica correcta de C++: un
  header que compila solo por el orden de includes de su includer es
  fragil. Admitirlos no es una concesion; es la regla bien aplicada.
- No hace falta commit adicional: el punto queda cerrado aqui y el
  sha 89044ee se mantiene.

## 3. Regla autoritativa del criterio 4 y predicciones del POST

- src/App.cpp: numstat exactamente +1/-48. Unica linea anadida:
  #include "Utils/StationMerge.h" (tras la linea 2). Retiradas
  567-614. Cualquier otra edicion en App.cpp: fallo.
- src/Utils/StationMerge.h: numstat +52 = 47 movidas (lineas 6-52,
  byte-identicas a App.cpp 567-613) + 5 de andamiaje (lineas 1-5:
  #pragma once, blank, #include <vector>, #include
  "Data/GiroAdapter.h", blank). Las 52 enumeradas una a una en
  04-header-enumerado.txt.
- PR acumulado 3716295..head del change: 3 ficheros, +188/-48 =
  (135 + 1 + 52) / 48.
- Predicciones lineadas del POST, derivadas de los hechos declarados;
  la evidencia debe mostrarlas o explicar la desviacion linea a
  linea. Mapeo al header: nueva = vieja - 561; luego mergeDias def
  en StationMerge.h:9, comentario con mergeDias en :36, mergeKc2g def
  en :37, fin del bloque en :52. Desplazamiento en App.cpp: -47 neto
  (+1 include, -48 retirada) para todo lo posterior a 614; luego
  usos esperados en App.cpp:2306 (antes 2353), App.cpp:2410 (2457),
  App.cpp:2481 (2528) y App.cpp:4150 (4197). Totales por simbolo sin
  cambio: mergeDias 3, mergeKc2g 4; 0 en tests.

## 4. Evidencia exigida para la conformidad de ejecucion

- Ferry to-glm/files/DW.5/ (11 ficheros, SHA256SUMS 11/11 OK):
  01-grep-pre y 02-grep-post lineados completos con recuento por
  simbolo y por fichero; 03-bloque-byte-identico (47 lineas contra
  567-613); 04-header-enumerado (52 lineas con la justificacion de
  cada include); 05-numstat; 06-head; 07-build; 08-ctest; 09-status;
  MANIFEST.
- Anclaje dual re-medido tras el cambio: local 54/54 con fixtures;
  CI 53 passed + 1 skipped (ebro_parse, exit 77); 54 slots / 0
  fallos en ambos entornos.
- CI del PR 2/2 y CI del push a master 2/2 (ctest + ThreadSanitizer).
- Bundle delta 3716295..head del change con sha256 publicado y git
  bundle verify; entrega manual de David a upload/ (0452 B: OpenCode
  genera, David entrega, GLM verifica). A la llegada: sha256, verify
  y diff grep; si no coincide, conformidad anulada.

## 5. Notas

- Atribucion de bundles, sobre la linea final del turno: la cadena
  registrada (0452 B; 0464 seccion 3; seccion 5 del propio
  pre-registro) es: OpenCode genera en INTERCAMBIO/work/ -> David
  entrega manualmente a upload/ -> GLM verifica. GLM no tiene via
  para depositar ficheros en upload/: toda lectura que le asigne ese
  paso es imposible. Pendientes de la entrega de David: DW.2 (2778 B,
  sha256 a0e9ec88...f2da46), DW.3 (3791 B, 53b71fcb...f940e01),
  DW.4 (3927 B, 881c6b78...42d089) y el opcional d9fb809..e680d01
  (cierre del 16 ficheros / +3253/-0 declarado). No son gate.
- Sigue pendiente del acta 0464 seccion 2: una linea por acta con el
  triple de los blobs archivados de 0460 (declarado 7066af3f...,
  5131 B / 105 lineas) y 0462 (declarado e6c3a85b..., 4745 B / 90
  lineas).
- static con un solo includer: nota de higiene permanente del acta
  0461 seccion 5, sin accion ahora. Si un segundo fichero llega a
  incluir StationMerge.h, decidir inline o namespace.

## 6. GO

- Pre-registro DW.5 (head 89044ee): CONFORME. Con esta acta y el GO
  de David, OpenCode ejecuta el slice. Mi proxima acta: conformidad
  (o rechazo motivado) de la ejecucion, previa al PR y al merge.

- GLM, lado auditor, 2026-11-23.
