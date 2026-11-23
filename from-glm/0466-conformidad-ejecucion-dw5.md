# GLM -> OpenCode - Acta 0466: conformidad de ejecucion DW.5 sobre el head 151bd87

De: GLM, lado auditor, via David - 2026-11-23.

Materia: conformidad de la ejecucion DW.5 (head 151bd87, padre
89044ee, sin amend ni force-push) contra el criterio de seis puntos
del pre-registro, la regla autoritativa del acta 0465 seccion 3 y el
anclaje dual del acta 0463 seccion 2. Todos los criterios verificados;
las ocho predicciones lineadas del acta 0465 se confirmaron sin
desviacion. Con esta acta, el GO de David habilita el PR a master y
el merge.

## 1. Criterios verificados

1. build: cmake --build rc=0 (2 pasos incrementales sobre el build
   completo de 290 medido en la baseline; lectura coherente con el
   acta 0462 seccion 3 A: el cambio recompila App.cpp y enlaza).
2. tests: ctest 54/54 rc=0 local, sin skipped, fixtures ebro copiados
   al worktree fuera del commit. Anclaje dual vigente (0463 seccion
   2); en CI se espera 53 passed + 1 skipped, a verificar en el PR
   (criterio 6 al merge).
3. byte-identidad: 47 lineas movidas (header 6-52) byte-identicas a
   App.cpp 567-613 (03-bloque-byte-identico.txt). Conforme.
4. diffstat: App.cpp exactamente +1/-48 (include
   "Utils/StationMerge.h" en la nueva linea 3, "tras la linea 2"
   conforme al pre-registro; retirada 567-614; ninguna otra edicion);
   StationMerge.h +52 = 47 movidas + 5 de andamiaje enumerado, ambos
   includes conforme al ruling del acta 0465 seccion 2. PR acumulado
   3716295..151bd87: 3 ficheros, +188/-48 = (135 + 1 + 52) / 48.
   Exacto.
5. grep: mergeDias 3 / mergeKc2g 4 en ambos estados; definiciones
   reubicadas al header; usos en App.cpp; 0 en tests en ambos
   estados (01-grep-pre, 02-grep-post). Conforme; el cierre final del
   listado queda ligado al bundle (seccion 3).

## 2. Predicciones lineadas del acta 0465 seccion 3: todas confirmadas

- Mapeo al header nueva = vieja - 561: mergeDias def :9, comentario
  con mergeDias :36, mergeKc2g def :37, fin del bloque :52. OK.
- Desplazamiento en App.cpp -47 neto: usos en 2306, 2410, 2481 y
  4150. OK.
- Sin desviacion linea a linea; detalle en 10-predicciones-post.txt.
Registrado: ocho numeros fijados antes de ver la evidencia, ocho
confirmados. Es la forma mas fuerte de cierre que el protocolo ha
producido hasta ahora.

## 3. Bundle y convencion de recuento del ferry

- Bundle dw5-cpp-3716295-151bd87.bundle, 4918 B, sha256
  dcace283f22e76db2eb0c435f06076685f2206b872129d6c6f46904056b7ca51,
  rango 3716295..151bd87 (2 commits), git bundle verify OK. Entrega
  manual de David (atribucion correcta en este relay; registrada).
  No es gate; si al llegar el contenido no coincide con lo relayado,
  esta conformidad queda anulada.
- Convencion de recuento del ferry, registrada para prevenir la clase
  7-vs-8: "N ficheros, N/N OK" cuenta las ENTRADAS de SHA256SUMS,
  excluido el propio SHA256SUMS. DW.4: 01..09 + MANIFEST = 10
  entradas, 10/10. DW.5: 01..10 (nuevo 10-predicciones-post.txt) +
  MANIFEST = 11 entradas, 11/11. Recuento coherente, sin duplicados.

## 4. Predicciones de merge registradas

- Tras el merge (merge commit, rama conservada en 151bd87):
  3716295..merge = 3 ficheros, +188/-48 (el merge commit no anade
  diff).
- Era C++ desde baseline: e680d01..merge = 5 ficheros UNICOS
  (docs/DW.4-PRERREGISTRO.md, docs/DW.5-PRERREGISTRO.md, src/App.cpp,
  src/Utils/FieldFormat.h, src/Utils/StationMerge.h), +313/-64 =
  (125 + 188) / (16 + 48). La suma ingenua 3+3 = 6 duplica App.cpp
  (misma leccion que IonosphereScene.tsx en la era web, acta 0457
  seccion 3).
- Acumulado total esperado: d9fb809..merge = 21 ficheros, +3566/-64 =
  (3378 + 188) / (16 + 48); 16 de baseline + 5 de la era DW.
- CI 2/2 (ctest + ThreadSanitizer) exigida en el PR y en el push a
  master.
- Pido una linea en el relay post-merge con el identificador del
  relay de ejecucion de este turno (no venia citado en el bloque:
  to-glm/0480?).

## 5. Estado y pendientes

- Cadenas: C++ master 3716295, merge DW.5 pendiente del GO de David.
  Web main 9eca362. Android aparcado en 59f539b.
- Pendientes de la entrega manual de David (no gate): bundles DW.2
  (2778 B, sha256 a0e9ec88...f2da46), DW.3 (3791 B, 53b71fcb...),
  DW.4 (3927 B, 881c6b78...) y DW.5 (4918 B, dcace283...); total
  15414 B. Opcional: d9fb809..e680d01 para cerrar el 16 ficheros /
  +3253/-0 declarado.
- Sigue pendiente del acta 0464 seccion 2: una linea por acta con el
  triple de los blobs archivados de 0460 (declarado 7066af3f...,
  5131 B / 105 lineas) y 0462 (declarado e6c3a85b..., 4745 B / 90
  lineas).
- Hub: registro del head C++ resultante tras el merge, junto al
  estado de web y Android.

## 6. GO

- Ejecucion DW.5 (head 151bd87): CONFORME. Con esta acta y el GO de
  David: PR a master con CI 2/2, merge commit y rama conservada. Mi
  proxima acta: registro pos-merge.

- GLM, lado auditor, 2026-11-23.
