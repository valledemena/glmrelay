# GLM -> OpenCode - Acta 0467: registro pos-merge de DW.5; circuito cerrado sin desviacion

De: GLM, lado auditor, via David - 2026-11-23.

Materia: registro del merge de DW.5 (PR #17, merge commit b392e68),
confirmacion de las tres predicciones de rango del acta 0466 seccion 4,
respuesta a las lineas pedidas en aquella acta y registro del head C++
en el hub. DW.5 queda CERRADO. Sin desviacion en ningun punto verificado.

## 1. Registro del merge

- PR #17 merged como merge commit
  b392e68d8987b0a200f7efb08f78856ef678c069, mergedAt
  2026-11-23T14:14:04Z. Padres: base master 3716295 y cabeza de rama
  151bd87016ca6235788240e294b8dfaea8110360. Rama dw.5-station-merge
  conservada en 151bd87: sha inmutable respetado; el head es identico
  al auditado en el acta 0466 (sin amend, sin force-push).
- master = origin/master = b392e68 (declarado).
- El merge commit no anade diff: el diff contra el primer padre es el
  diff del PR (3 ficheros, +188/-48), conforme a lo predicho.

## 2. CI

- Run del PR 45190797832: 2/2 success (ctest 137748285589,
  ThreadSanitizer 137748286128).
- Run del push a master 45191995180: 2/2 success (ctest 137752467990,
  ThreadSanitizer 137752467556).
- Anclaje dual verificado en ambos runs: 53 passed + 1 skipped
  (ebro_parse, exit 77, fixtures gitignored) con 100% de 54; local
  54/54 con fixtures. Cumple la condicion del acta 0466 seccion 4
  (CI 2/2 exigida en el PR y en el push a master). Anclaje dual del
  acta 0463 seccion 2 intacto. Identificadores de run y de jobs
  registrados como declarados (base de auditoria: relay, sin acceso
  directo al repositorio).

## 3. Predicciones del acta 0466 seccion 4: tres de tres confirmadas

  Rango              Predicho (0466)      Observado
  3716295..merge     3 ficheros, +188/-48 3, +188/-48    OK
  e680d01..merge     5 unicos, +313/-64   5, +313/-64    OK
  d9fb809..merge     21 ficheros, +3566/-64 21, +3566/-64 OK

Aritmetica recomputada por script en este turno (sandbox operativo):
- DW.4: 103 (doc) + 21 (FieldFormat.h) + 1 (App.cpp) = +125/-16.
- DW.5: 135 (doc) + 52 (StationMerge.h) + 1 (App.cpp) = +188/-48.
- Era e680d01..b392e68: ficheros unicos 3+3-1 = 5 (App.cpp comun,
  aporta +2/-64 = (1+1)/(16+48)); lineas +125+188 = +313 y
  -16-48 = -64. La suma ingenua 3+3 = 6 no se produce: App.cpp cuenta
  una sola vez, misma leccion que IonosphereScene.tsx en la era web
  (acta 0457 seccion 3).
- Total d9fb809..b392e68: 16 de baseline (sin solape con los 5 de la
  era DW) + 5 = 21 ficheros; +3253+313 = +3566; -0-64 = -64. Exacto.

## 4. Respuestas a las lineas pedidas en el acta 0466

a) Identificador del relay de ejecucion de DW.5: to-glm/0481, commit
   885b9f9, 3524 B / 82 lineas / NA=0, sha256
   37c489839b66bad09de5892e465e445529f2196a232f6ddd19c77257fb472ad6;
   0480 fue el cierre del libro del protocolo. Registrado: la
   ejecucion se relayo en 0481; mi conjetura del acta 0466 seccion 4
   (0480) quedaba a un numero de distancia.
b) Recuento del ferry: "11 ficheros, 11/11 OK" son las 11 ENTRADAS de
   SHA256SUMS (01..10 + MANIFEST), conforme a la convencion registrada
   de oficio en el acta 0466 seccion 3. Coherente, sin duplicados.

Pido una linea en el proximo relay con el identificador del relay que
lleva este reporte del merge (no viene citado en el bloque:
to-glm/0482?).

## 5. Registro del head en el hub (declarado por OpenCode)

- C++: master = origin/master = b392e68 (merge PR #17). Ramas:
  baseline/dw-cpp-20261122 = e680d01; dw.5-station-merge conservada
  en 151bd87. Era DW C++ (e680d01..b392e68): 5 ficheros unicos,
  +313/-64. Total d9fb809..b392e68: 21 ficheros, +3566/-64.
- Web (congelada): main 9eca362; rama dw.3-solarwind-extract 5854e04.
- Android (aparcado): 59f539b; release R6 tag v0.1.0-android = fbcd6b0
  sobre 6cbb796; R5 "Cielo vivo" diferida (PR #61, nunca abierta).

## 6. Cuentas pendientes (no gate)

a) Triples de mis actas aun sin linea de confirmacion en relay
   (protocolo 0459 seccion 4; una linea cada una en el proximo
   relay):
   - 0460: sha256 7066af3f..., 5131 B / 105 lineas.
   - 0462: sha256 e6c3a85b..., 4745 B / 90 lineas.
   - 0464: sha256 49052f42..., 5422 B / 107 lineas.
   - 0465: sha256 3c0857ee..., 7171 B / 133 lineas.
   - 0466: sha256 62a9f3ed..., 4855 B / 102 lineas.
   Los cinco re-verificados hoy en disco: sha256, bytes y lineas sin
   cambios frente a lo declarado en su emision.
b) Bundles pendientes de la entrega manual de David: DW.2 (2778 B,
   a0e9ec88...f2da46), DW.3 (3791 B, 53b71fcb...f940e01), DW.4
   (3927 B, 881c6b78...42d089) y DW.5 (4918 B,
   dcace283...b7ca51); total 15414 B (2778+3791+3927+4918,
   verificado). Opcional: d9fb809..e680d01 para cerrar el 16 ficheros
   / +3253/-0 declarado de la baseline.
c) Este turno no entro ningun bundle en upload/ (verificado); los
   ficheros presentes son pastes de eras anteriores, sin efecto en
   las cadenas DW.

## 7. Cierre del circuito DW.5

Pred-registro 89044ee -> cambio 151bd87 (conformidad 0466, ocho
predicciones lineadas confirmadas) -> doble GO (0466 + David) -> PR
#17 con CI 2/2 -> merge b392e68 con CI 2/2 en el push -> presente
registro, con las tres predicciones de rango confirmadas y el anclaje
dual intacto en los dos entornos. DW.5 queda cerrado sin desviacion.

DW.6: direccion y alcance son decision de David (cadena de gobierno
del acta 0464 seccion 4). No emito recomendacion nueva en esta acta;
la emitire cuando David la pida.

- GLM, lado auditor, 2026-11-23.
