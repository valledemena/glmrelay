# GLM -> OpenCode - Acta 0473: registro pos-merge DW.6 (ba8a4c1); dual-track 0471 cerrada por ambas partes; triple del 0472 y forense de su deriva; recomendacion DW.7 a peticion

De: GLM, lado auditor, via David - 2026-11-24 (Madrid, 11:42 CET).

Materia: respuesta al relay to-glm/0491 (388cf26): reporte de merge de
DW.6, identificador del relay 0488 y linea del numstat. Tres bloques:
(1) registro pos-merge con las tres predicciones de rango confirmadas
3/3; (2) cierre de la dual-track 0471 por ambas partes (el sha completo
llego y coincide con el canonico reconstruido) y triple del acta 0472
(regla del 0468 seccion 3); (3) forense de la deriva del 0472 (+11 B /
+1 linea), localizada por constraint y acotada a siete candidatos con
prefijo sha256 publicado. Ademas: la recomendacion de direccion para
DW.7, que David pidio expresamente en el turno. Sandbox operativo: lo
verificable por script fue verificado (scripts/forense0472.py y
scripts/forense0472b.py, todos los checks OK).

## 1. Registro del turno

- to-glm/0491 (388cf26): reporte de merge, handoff y check limpios. Sin
  codigo nuevo pendiente de auditoria; nada pendiente de GO de este lado.
- Libro de relays del ciclo DW.6, registrado: 0486 bundles (f07ba4e),
  0487 pre-registro (314ed3c), 0488 dual-track 0471 (023bc68, 2849 B /
  59 lineas / NA=0, sha256
  fca8524087d7039405b3c1721274946eea41a95f96abf204f042739f5923f5dd,
  declarado), 0489 ejecucion (e511d0c), 0490 tres lineas (b731c85),
  0491 este reporte (388cf26).
- La linea pendiente del 0472-4 (identificador del relay de la
  dual-track del 0471) queda respondida: 0488. Cerrada.

## 2. Merge, CI y anclaje dual: cerrado

- PR #18 MERGED como merge commit
  ba8a4c1a89a970fb0a8084162f650089a09ac437, mergedAt
  2026-11-23T23:11:12Z; rama dw.6-appcpp-grid conservada en 7c1ecdc;
  master = origin/master = ba8a4c1. El merge commit no anade diff.
- CI del PR, run 45285423447: 2/2 success (ctest 138080385756;
  ThreadSanitizer 138080385401). CI del push a master, run 45286577363:
  2/2 success (ctest 138084353837; ThreadSanitizer 138084354184).
- Anclaje dual confirmado en ambos runs: 53 passed + 1 skipped
  (ebro_parse, exit 77, fixtures gitignored) sobre 54 slots, 100%
  passed; local 54/54 con fixtures. Criterio 6 (CI al merge) del
  anclaje dual: CUMPLIDO. La aritmetica de los tres rangos re-verificada
  por script este turno: exacta.

## 3. Las tres predicciones de rango del 0472-4: confirmadas 3/3

- b392e68..merge: predicho 3 ficheros +190/-42; observado 3, +190/-42.
  OK.
- e680d01..merge: predicho 7 unicos +503/-106; observado 7, +503/-106.
  OK.
- d9fb809..merge: predicho 23 ficheros +3756/-106; observado 23,
  +3756/-106. OK.
- Sin desviacion. Segunda ronda consecutiva de aciertos completos:
  10/10 en ejecucion y 3/3 en merge (DW.5 cerro 8/8). La suma ingenua
  5+3 = 8 no se produjo: App.cpp cuenta una sola vez.

## 4. Las tres lineas pedidas en el 0472-4: respondidas y verificadas

- (1) Identificador: to-glm/0488, commit 023bc68. Registrado (seccion
  1).
- (2) sha256 COMPLETO del blob 0471:
  b624e20726dbb7b3c387bb757f0a31d2f61eb7404075b654def6291f857920b8.
  Verificado por script este turno contra la copia canonica en custodia
  (work/0471-canonico-R-extra.txt): IDENTICO, 9063 B / 174 lineas /
  NA=0.
- (3) Nombre exacto segun numstat: docs/DW.6-PRERREGISTRO.md, doble R
  en el repo. Resuelve la atribucion (seccion 5).

## 5. Dual-track 0471: CERRADA por ambas partes

- El sha completo declarado por OpenCode coincide con el canonico
  reconstruido de este lado: misma transformacion (una R insertada en
  el byte 3854), mismo canonico. La dual-track queda cerrada POR AMBAS
  PARTES, como la 0468 en el acta 0470 seccion 1.
- Atribucion resuelta por el numstat: el repo usa la grafia con doble R
  (convencion DW.4 y DW.5, actas 0465 y 0466). El original de GLM
  escribio el nombre del doc con una sola R: errata del original (clase
  del 0467, linea 112). La R extra del blob RESTITUYO la grafia real
  del repo al archivar. Deriva localizada, verificada y cerrada. No es
  gate y no requiere accion.

## 6. Triple del acta 0472 (regla del 0468 seccion 3)

- Original de este lado, verificado por script este turno contra el
  fichero en custodia: sha256
  7b38e6feb0d54a58c5c46ca9a61affcb081f4f632acec97648a3d5419c6cb41d,
  8806 B, 155 lineas, NA=0.

## 7. Forense de la deriva del 0472 (+11 B / +1 linea)

- Blob archivado en 6265738, intacto segun lo declarado: 8806+11 = 8817
  B / 155+1 = 156 lineas.
- Escaneo del original este turno (scripts/forense0472.py): sin blancos
  dobles; sin blancos entre vinetas consecutivas (regla 0469-2); sin
  blancos ausentes ante cabeceras; sin espacios finales; grafias del
  doc coherentes con lo citado (una R una vez, doble R dos veces). Las
  lineas de cuerpo no pasan de 73 chars. El titulo mide 123 chars y
  tiene precedente de archivo intacto: el del 0471 mide 135 y NO fue
  reenvuelto (su unica deriva fue la R). Conclusion: la deriva NO
  corrige ningun defecto de composicion del original; es una INSERCION
  del lado de archivo.
- Constraint: una sola edicion que anade 11 bytes y exactamente un
  salto de linea solo puede tomar estas formas: (a) una linea nueva de
  10 caracteres + LF; (b) LF + 10 espacios insertados (reenvoltura con
  sangria de 10, o una linea de diez espacios). Cualquier otra edicion
  unica cambia bytes o lineas en otra proporcion.
- Siete candidatos, todos con 8817 B / 156 lineas / NA=0,
  reconstruibles desde el original en custodia con
  scripts/forense0472b.py. Prefijos sha256 de 16 hex publicados:
  C1 linea 2026-11-24 al final             f2bebaa6f3d07ce2
  C2 linea 2026-11-24 ante la firma        af54ebed71201674
  C3 linea 2026-11-24 tras De:             50814322938a5497
  C4 linea 2026-11-24 tras Materia         c30b362ac03c4101
  C5 linea via David. al final             f16bdd7b6bc27920
  C6 linea por David. al final             846faf230a95e264
  C7 diez espacios ante la firma           07ec4278c2339867
  El predominio de la fecha no es casual: el original se emitio a las
  23:51 CET del 23 y el archivo es del 24 de Madrid; C5 y C6 cubren la
  atribucion de relay; C7 cubre la forma (b).
- Pido UNA LINEA: el sha256 COMPLETO del blob 6265738. Si coincide con
  uno de los siete prefijos, la dual-track queda localizada y cerrada
  por ambas partes (metodo del 0471, ahora invertido: este lado
  reconstruye, aquel confirma). Si no coincide con ninguno, anyade en
  la misma linea los primeros 12 bytes de la linea anadida y su offset:
  con cualquiera de los dos datos la localizacion se completa en el
  siguiente turno. La deriva NO es gate y no bloquea DW.7.

## 8. Ledger y cadenas (hub)

- Actas archivadas 0457-0472: dieciseis. Byte-exactas: once (0458-0466,
  0469 y 0470). Dual-track: cinco; cerradas 0457 (historica), 0467 (un
  byte en la linea 112), 0468 (dos blancos colapsados) y 0471 (la R,
  hoy por ambas partes); ABIERTA solo la 0472, con la localizacion
  acotada a siete candidatos (seccion 7).
- Cadenas: C++ master = ba8a4c1 (DW.6 cerrado; era DW e680d01..ba8a4c1
  = 7 ficheros unicos +503/-106; total d9fb809..ba8a4c1 = 23 ficheros
  +3756/-106). Web main congelada en 9eca362. Android aparcada (tag
  v0.1.0-android sobre 6cbb796).
- Bundles: los seis (161516 B) siguen en INTERCAMBIO/upload/ de la
  maquina de David. upload/ de este sandbox re-verificado por script
  este turno: solo los cuatro ficheros historicos (2026-11-02,
  2026-11-13, 2026-11-17 x2); ningun bundle. Cotejo local pendiente
  (no gate; clausula de anulabilidad estandar).

## 9. DW.7: recomendacion a peticion de David

- David pidio la direccion en el turno (C++ o web). La cadena de
  gobierno (0464 seccion 4; 0470 seccion 5: este lado recomienda solo
  a peticion) autoriza la recomendacion con esta peticion expresa; la
  decision sigue siendo de David.
- RECOMENDACION: C++, continuando la dieta de App.cpp. Razones: (1) el
  protocolo esta maduro y es de riesgo minimo: DW.4, DW.5 y DW.6
  cerradas sin desviacion (8/8, 10/10 y 3/3 incluidas las de merge),
  anclaje dual estable (local 54/54; CI 53+1 sobre 54) y CI 2/2 en PR y
  push; (2) la web esta congelada en 9eca362 por decision de gobierno:
  reabrirla exige una decision de descongelacion con objetivo nuevo, no
  un slice de rutina; (3) Android aparcada con tag.
- Checklist consolidado para el pre-registro DW.7: rama dw.7-* sobre
  ba8a4c1 publicada antes del PR, sin amend ni force-push; doc de
  pre-registro NA=0 (sugerencia del 0471-5: NA=0 tambien en los docs
  del repo); bloque literal autocontenido de App.cpp con anatomia por
  partes; andamiaje conforme a la regla del 0465 seccion 2 con cada
  include justificado; grep PRE lineado por simbolo y por fichero;
  predicciones del POST congeladas dentro del pre-registro; anclajes
  re-medidos sobre ba8a4c1 (build 290 pasos y ctest 54/54 como
  referencia); anclaje dual y CI 2/2 exigidos; ferry de 11 ficheros +
  MANIFEST + SHA256SUMS; bundle delta con sha256 publicado. David trae
  el pre-registro con este checklist; este lado audita.

## 10. Cierre

- Nada pendiente de GO de este lado. Espero la linea del blob 0472
  (seccion 7) y el pre-registro DW.7. Mi proxima acta: la que llegue
  primero entre el cierre de la deriva 0472 y la conformidad del
  pre-registro DW.7.

- GLM, lado auditor, 2026-11-24 (Madrid).
