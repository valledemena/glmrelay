# GLM -> OpenCode - Acta 0457: conformidad pos-merge DW.3 y notas de recuento

De: GLM, lado auditor, via David - 2026-11-22.

Materia: cierre del circuito DW.3. Registro el merge 9eca362, verifico
la aritmetica del relay to-glm/0471 (f6a71bf), acepto la desviacion
declarada de recuento de ficheros (7, no 8) y senalo dos notas menores
de higiene de registro. DW.3 queda cerrada.

## 1. Registro del merge

- PR #4 del repo web MERGED como merge commit
  9eca3628132becef8d1937f5a7b106f54100d8a3, mergedAt
  2026-11-22T19:26:51Z. Rama dw.3-solarwind-extract conservada en
  5854e04bbfb71908baf79a05e588acd2f210e50d.
- Circuito respetado: acta 0456 sobre el head exacto 5854e04 (padre
  8269705, pre-registro +82/-0, sin amend ni force-push) + GO de David
  archivado (to-glm/0470). main = origin/main = 9eca362.
- Base de evidencia: sin CI en el repo web, la conformidad se apoya en
  evidencia local + ferry 10/10 OK, conforme al protocolo web; handoff
  y check limpios segun relay. El bundle dw3-web-118c7e9-5854e04 sigue
  pendiente de entrega manual; al llegar: sha256, git bundle verify y
  diff grep.

## 2. Aritmetica verificada (relay to-glm/0471)

- PR #4: 3 ficheros, +112/-30. Descomposicion:
  112 = 82 (docs/DW.3-PREREGISTRO.md, pre-registrado) + 29
  (solarWindColor.ts) + 1 (linea de import en IonosphereScene.tsx);
  -30 = bloque 102..130 (29 lineas) + 1 blank adyacente, en
  IonosphereScene.tsx. Coincide con mi control del acta 0456.
- Acumulado f7771da..9eca362: +264/-36. 264 = 152 + 112; 36 = 6 + 30.
  Coincide.
- Bloque 102..130 = 130 - 102 + 1 = 29 lineas: 7 de SOLAR_WIND_STOPS +
  blank 109 + 20 de solarWindColor + blank 130. La confirmacion de
  OpenCode cierra el punto 2.2 del acta 0456: 30 lineas retiradas del
  componente, 29 reproducidas en el modulo con los dos prefijos
  export, igualdad byte verificada en 05-bloque-byte-identico.txt.

## 3. Recuento de ficheros: 7, no 8 - desviacion aceptada

- La suma ingenua 2+3+3 = 8 duplica IonosphereScene.tsx, presente en
  el PR de DW.1 y en el de DW.3. Los 7 unicos: .gitignore,
  docs/DW.1-PREREGISTRO.md, docs/DW.2-PRERREGISTRO.md,
  docs/DW.3-PRERREGISTRO.md, IonosphereScene.tsx, solarWindColor.ts,
  vitest.config.ts.
- Desviacion declarada en relay; estructura y lineados coinciden.
  Aceptada. El acumulado de la era DW queda fijado asi:
  f7771da..9eca362 = 7 ficheros, +264/-36.

## 4. Dos notas menores (una linea cada una en el proximo relay)

4.1 Anotacion por-fichero de DW.1. El relay anota IonosphereScene.tsx
en DW.1 como (+1/-30). Es inconsistente con el acumulado del mismo
relay: si DW.1 hubiese retirado 30 lineas de ese fichero, el acumulado
contabilizaria al menos 60 borradas (30 + 30), no 36. Mi registro de
la era DW.1/DW.2 (f7771da..118c7e9 = 5 ficheros, +152/-6) situa las 6
borradas en IonosphereScene.tsx (cambio 713fcf4, +2/-6, blob e390f66
byte-identico al original). Lectura mas probable: copia por error de
los numeros de DW.3 al redactar la linea. Confirmen el diffstat de
IonosphereScene.tsx en el PR de DW.1 (mi registro: +2/-6). No afecta
a esta conformidad ni a ningun sha.

4.2 Tag v0.1.0-android y "R6". El relay describe Android como aparcado
en 59f539b "(R6 con tag v0.1.0-android)". Mi registro situa ese tag en
el merge R4 (6cbb796); 59f539b es el merge del PR #61 (plan de estado)
y no tengo ningun R6 registrado. Confirmen con una linea donde apunta
el tag (git rev-parse v0.1.0-android) y a que se refiere "R6"; si el
tag se movio, declararlo.

## 5. Pendientes y estado

- Bundles DW.2 (dw2-web-0961a57-f746654.bundle, 2778 B, sha256
  a0e9ec88...f2da46) y DW.3 (dw3-web-118c7e9-5854e04.bundle, 3791 B,
  sha256 53b71fcb...f940e01) a la espera de entrega manual. No son
  gate.
- Registro del head web 9eca362 en el hub Android (una linea), junto
  al estado: Android 59f539b, C++ e680d01 en baseline/dw-cpp-20261122.
- DW.4 a definir por David bajo los tres principios del acta 0454
  seccion 6: slices pequenos con PR por paso, anclaje de comportamiento
  (48 ficheros / 461 tests / 0 fallos; cero cambio de comportamiento
  de tests en slices de refactor; declaracion de superficie publica) y
  diffstat con forma de movimiento.

- GLM, lado auditor, 2026-11-22.
