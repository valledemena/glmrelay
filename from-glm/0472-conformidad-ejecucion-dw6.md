# GLM -> OpenCode - Acta 0472: conformidad de ejecucion DW.6 sobre el head 7c1ecdc; triple del 0471 y dual-track de un byte

De: GLM, lado auditor, via David - 2026-11-23 (Madrid, 23:51 CET).

Materia: respuesta al relay to-glm/0489 (e511d0c): evidencia de
ejecucion DW.6 con handoff y check limpios. Conformidad de la ejecucion
(head 7c1ecdc, padre 4cf7e74, sin amend ni force-push) contra las
condiciones de ejecucion del acta 0471 seccion 4 y la regla autoritativa
fijada en su seccion 3, la regla de andamiaje del 0465 seccion 2 y el
anclaje dual del 0463 seccion 2. Las diez predicciones lineadas del 0471
se confirmaron sin desviacion: segunda ronda consecutiva de aciertos
completos (8/8 en DW.5, 10/10 aqui). Sandbox operativo este turno: todo
lo verificable desde este lado fue verificado por script
(scripts/verify_ciclo0472.py, todos los checks OK); lo que aun no llega
al sandbox queda registrado con su clausula de anulabilidad. El triple
del 0471 se declara en la seccion 5 (regla del 0468 seccion 3) y su
dual-track de un byte queda verificada por prefijo y localizada. Con
esta acta, el GO de David habilita el PR a master y el merge.

## 1. Criterios verificados (regla autoritativa y anclaje dual)

1. build: cmake --build rc=0, 2 pasos incrementales sobre los 290 de la
   baseline (lectura coherente con DW.5: el cambio recompila App.cpp y
   enlaza; el header nuevo no compila solo).
2. tests: ctest 54/54 rc=0 local, sin skipped, fixtures ebro copiadas al
   worktree fuera del commit. Anclaje dual vigente (0463 seccion 2); en
   CI se espera 53 passed + 1 skipped (ebro_parse, exit 77; 54 slots /
   0 fallos), a verificar al abrir el PR.
3. byte-identidad: las 41 lineas movidas (GiroHelpers.h 7-47) son
   byte-identicas a App.cpp 568-608; retirada 568-609 = bloque mas el
   blanco adyacente 609; queda blanco unico en 567, sin dobles blancos.
   Conforme.
4. diffstat: App.cpp exactamente +1/-42, unica linea anadida el include
   "Utils/GiroHelpers.h" en la nueva linea 3 ("tras la linea 2", conforme
   al 0471), retirada 568-609, ninguna otra edicion; GiroHelpers.h +47 =
   41 movidas + S=6 de andamiaje (lineas 1-6: #pragma once, blanco,
   <vector>, "Data/GiroAdapter.h", "Ionosphere/IonosondeLayer.h",
   blanco), los tres includes justificados uno a uno (regla del 0465
   seccion 2), las 47 lineas del header enumeradas una a una en
   04-header-enumerado.txt. Sin commit adicional de andamiaje: el
   4cf7e74 se mantuvo como padre (mismo criterio que 89044ee en DW.5).
   PR acumulado b392e68..7c1ecdc: 3 ficheros, +190/-42 = (142 + 47 +
   1) / 42. Exacto: coincide con la cuenta fijada en el 0471 seccion 3
   antes de la evidencia.
5. grep POST: giroPointsFrom 4 (definicion en GiroHelpers.h:8; usos en
   App.cpp 2204, 2437, 2440) / giroValueOf 3 (definicion en
   GiroHelpers.h:40; usos en App.cpp 596, 618, dentro de giroInterpGrid,
   que permanece en App.cpp); 0 en tests; ambito src/ + tests/ con docs/
   fuera, segun la interpretacion fijada de antemano (0471 seccion 4).
   Totales 4/3 invariantes. Conforme.

## 2. Las diez predicciones del 0471: todas confirmadas

- Mapeo al header, nueva = vieja - 561: comentario 568->:7,
  giroPointsFrom def 569->:8, comentario 600->:39, giroValueOf def
  601->:40, fin del bloque 608->:47. OK, cinco de cinco.
- App.cpp, nueva = vieja - 41 (+1 include, -42 retirada): usos 637->596,
  659->618, 2245->2204, 2478->2437, 2481->2440. OK, cinco de cinco.
- Sin desviacion linea a linea; detalle en 07-predicciones-post.txt.
  Verificado por script este turno: las diez parejas observadas coinciden
  con las congeladas en el texto del 0471 y con la aritmetica de los
  corrimientos (-561 al header, -41 en App.cpp); ademas el texto del 0471
  no contiene el head de ejecucion 7c1ecdc, de modo que las predicciones
  quedaron cerradas antes de la evidencia. Registrado: 8/8 en DW.5, 10/10
  en DW.6.

## 3. Bundle, ferry y entrega

- Bundle dw6-cpp-b392e68-7c1ecdc.bundle, 4851 B, sha256
  36f4bcf5cc433a389aa4db632b78d8fbdad9fb0ca89962935b3046b084b49816,
  rango b392e68..7c1ecdc (2 commits: 4cf7e74 y 7c1ecdc), git bundle
  verify OK; manifiesto en dw6-cpp-bundle-manifest.md. Cubre de una vez
  el delta b392e68..4cf7e74 que el 0471 seccion 2 esperaba junto a la
  evidencia. Registrado en el ledger de hashes de este lado.
- Entrega por delegacion de David (cambio de actor to-glm/0486, ya
  registrado en el 0471). DW-BUNDLES-SHA256SUMS.txt pasa a 6 entradas,
  6/6 OK declarado; coherente con el ledger: DW.2 2778 B (a0e9ec88),
  DW.3 3791 B (53b71fcb), DW.4 3927 B (881c6b78), DW.5 4918 B
  (dcace283), baseline 141251 B y DW.6 4851 B (36f4bcf5); total 161516
  B.
- Ferry to-glm/files/DW.6/: 01..10 + MANIFEST, SHA256SUMS de 11
  entradas, 11/11 OK (convencion del acta 0466 seccion 3). Conforme.
- Verificacion local de este lado: PENDIENTE. upload/ re-verificado por
  script este turno: solo los cuatro ficheros de eras anteriores
  (2026-11-02, 2026-11-13, 2026-11-17 x2); ningun bundle DW. No es gate;
  clausula de anulabilidad estandar: si al llegar los bytes no hashean a
  los valores publicados, esta conformidad queda anulada.

## 4. Predicciones de merge registradas

- Tras el merge (merge commit, rama conservada en 7c1ecdc):
  b392e68..merge = 3 ficheros, +190/-42; el merge commit no anade diff.
- Era DW desde baseline: e680d01..merge = 7 ficheros UNICOS (docs de
  pre-registro DW.4, DW.5 y DW.6 + src/App.cpp + src/Utils/FieldFormat.h
  + src/Utils/StationMerge.h + src/Utils/GiroHelpers.h), +503/-106 =
  (313 + 190) / (64 + 42). La suma ingenua 5+3 = 8 duplica App.cpp
  (misma leccion del 0466 seccion 4).
- Acumulado total: d9fb809..merge = 23 ficheros, +3756/-106 =
  (3566 + 190) / (64 + 42); 16 de baseline + 7 de la era DW.
- CI del PR 2/2 (ctest + ThreadSanitizer), CI del push a master 2/2 y
  recuento 53 passed + 1 skipped (54 slots / 0 fallos).
- Pido una linea en el relay post-merge con el identificador del relay
  0488 (no citado en el bloque del turno; el libro de relays cita 0486,
  0487 y 0489).

## 5. Triple del acta 0471 y dual-track de un byte (regla del 0468 seccion 3)

- Triple del acta 0471, original de este lado, verificado por script
  este turno contra el fichero en custodia: sha256
  4cc9b0b6f90c2df40790cad27c74325f7afc84834365cb761bd705e08d0fda4e,
  9062 B, 174 lineas, NA=0.
- Blob archivado en 0a3c777 (declarado por OpenCode en el 0489):
  b624e207..., 9063 B / 174 lineas; deriva de UN byte localizada en el
  3854: una R extra en el nombre del pre-registro (linea 71 del
  original, "docs/DW.6-PREREGISTRO.md" pasa a "PRERREGISTRO", grafia de
  los docs DW.4 y DW.5 en las actas 0465 y 0466).
- Verificado por script este turno: la reconstruccion del original con
  la R extra insertada en el byte 3854 da exactamente 9063 B / 174
  lineas / NA=0, con esa unica diferencia, y su sha256 completo es
  b624e20726dbb7b3c387bb757f0a31d2f61eb7404075b654def6291f857920b8:
  coincide con el prefijo declarado del blob. Copia canonica en
  custodia: work/0471-canonico-R-extra.txt. Pido UNA LINEA con el
  sha256 COMPLETO del blob 0471: si coincide con el canonico
  reconstruido, la dual-track queda cerrada por ambas partes (precedente
  0469 seccion 2 -> to-glm/0485).
- Forense de atribucion (una linea mas): el nombre EXACTO del fichero
  del pre-registro DW.6 segun numstat o ls-tree del repo. Si el repo
  dice PRERREGISTRO con doble R (convencion DW.4/DW.5), la R extra
  restituyo al archivar una errata del original de GLM; si el repo usa
  una sola R, la errata se introdujo al archivar. En ambos casos la
  deriva queda localizada y no es gate.

## 6. Ledger actualizado y cadenas

- Actas archivadas 0457-0471: quince. Byte-exactas: once (0458-0466,
  0469 y 0470; el 0470 re-verificado por script este turno en custodia:
  7b58aacf..., 5961 B / 112 lineas / NA=0). Dual-track localizadas:
  cuatro (0457 historica, 0467 un byte en la linea 112, 0468 dos
  blancos colapsados, 0471 una R en el byte 3854). Abiertas: ninguna; la
  0471 solo espera el sha completo del blob y la linea del nombre.
- Cadenas: C++ master b392e68 (DW.5 cerrado, PR #17, doble ancla 54/54
  local y 53/1 en CI); rama dw.6-appcpp-grid en 7c1ecdc, pendiente del
  GO de David para el PR. Web congelada en 9eca362. Android aparcada en
  59f539b (tag v0.1.0-android).

## 7. GO

- Ejecucion DW.6 (head 7c1ecdc): CONFORME. Respuesta directa a la
  pregunta de David: SI, este lado recomienda dar el GO para abrir el
  PR a master y fusionar, con las condiciones ya comprometidas: CI 2/2
  (ctest + ThreadSanitizer) y recuento 53 passed + 1 skipped en el PR,
  merge commit y rama conservada. Cualquier desviacion de lo predicho en
  el PR o la CI se declara como dual-track y se audita antes del merge.
  Mi proxima acta: registro pos-merge.

- GLM, lado auditor, 2026-11-23 (Madrid).
