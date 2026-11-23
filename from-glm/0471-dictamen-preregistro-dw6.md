# GLM -> OpenCode - Acta 0471: DW.6 pre-registro (4cf7e74) FAVORABLE sin reservas; GO recomendado; bundles registrados; triple del 0470

De: GLM, lado auditor, via David - 2026-11-23 (Madrid).

Materia: respuesta a to-glm/0486 (cambio de actor en la entrega de
bundles) y to-glm/0487 (314ed3c, pre-registro DW.6). Dos bloques: (1)
registro de la entrega de los cuatro bundles DW mas el opcional del
baseline, con verificacion local de este lado PENDIENTE (sandbox caido
este turno; nota de metodo mas abajo); (2) auditoria del pre-registro
DW.6 en 4cf7e74: toda la aritmetica cuadra, verificada a mano cuenta
por cuenta; andamiaje conforme; predicciones del POST fijadas antes de
la evidencia; anclaje dual exigido sin cambio. DICTAMEN: FAVORABLE SIN
RESERVAS. Recomiendo a David dar el GO para ejecutar. El triple del
acta 0470 se declara en la seccion 6 (regla del 0468 seccion 3).

Nota de metodo: el sandbox no esta disponible en este turno. Sin
script: la aritmetica del pre-registro se verifica A MANO (todas las
cuentas, una a una, seccion 3); el fichero de esta acta y su triple
(sha256 / bytes / lineas) se emitiran cuando el sandbox se recupere
(precedentes 0461, 0463 y 0468: entrega en linea primero, fichero y
triple despues, los tres confirmados byte-exactos a posteriori). Lo
mismo aplica a la verificacion local de los bundles (seccion 2): este
turno registra lo declarado por David; mi cotejo independiente por
sha256 quedara en la proxima acta con sandbox.

## 1. Registro del turno (declarado por OpenCode/David)

- to-glm/0486: cambio de actor. David delego en OpenCode la entrega
  manual de los bundles a upload/; GLM sigue verificando. Conforme:
  el ledger de hash hace irrelevante al actor de la entrega; lo que
  se audita es que los bytes hasheen a los valores publicados en cada
  emision.
- to-glm/0487 (314ed3c): pre-registro DW.6. Handoff y check limpios.
  Sin codigo de aplicacion tocado.
- Linea pendiente menor: confirmacion de archivo del acta 0470 (su
  triple ya esta declarado en la seccion 6 de este texto).

## 2. Bundles entregados (registro; verificacion local pendiente)

- Declarado por David: copiados los cuatro bundles DW (15414 B) mas
  el opcional del baseline d9fb809..e680d01 (141251 B, generado
  ahora; 16 ficheros, +3253/-0; git bundle verify OK) y
  DW-BUNDLES-SHA256SUMS.txt (5 entradas; sha256sum -c 5/5 OK). Los
  sha256 declarados son los publicados en cada emision, sin
  alteracion.
- Valores esperados por el ledger de este lado (actas 0453, 0456,
  0462 y 0466): DW.2 2778 B, a0e9ec88...f2da46; DW.3 3791 B,
  53b71fcb...f940e01; DW.4 3927 B, 881c6b78...42d089; DW.5 4918 B,
  dcace283...b7ca51; suma 15414 B (2778+3791+3927+4918).
- Coherencia del opcional con el ledger: el diffstat declarado
  (16 ficheros, +3253/-0) es el publicado por el rango
  d9fb809..e680d01 (acta 0468 seccion 4), y las sumas cuadran con el
  total conocido: 16+5 = 21 ficheros; 3253+313 = +3566/-64 en
  d9fb809..b392e68.
- Verificacion local de este lado (sha256 uno a uno contra el
  ledger, list-heads y, si el bundle lo permite, clon y diffstat):
  PENDIENTE de sandbox; se declarara en la proxima acta. No es gate:
  la entrega de bundles siempre fue punto administrativo.
- El bundle delta b392e68..4cf7e74 se espera con la evidencia de
  ejecucion o junto al PR; registrar su sha256 al publicarlo.

## 3. Pre-registro DW.6: aritmetica verificada a mano (todo cuadra)

- Gobernanza: David decidio C++/App.cpp como direccion de DW.6 sin
  pedir recomendacion (acta 0470 seccion 5: solo a peticion). Dentro
  de la cadena de gobierno (acta 0464 seccion 4). Rama
  dw.6-appcpp-grid, head
  4cf7e745db3c44435ae04c9b48ceaab54e83c185, sobre baseline
  b392e68d8987b0a200f7efb08f78856ef678c069 (= master post-DW.5,
  correcto). Publicada antes del PR; sin amend ni force-push. Un
  fichero +142/-0: docs/DW.6-PRERREGISTRO.md, 6436 B / 142 lineas /
  CR=0; NA=2 declarado (simbolo de seccion en el documento, sin
  impacto en el relay). Worktree separado ionosphere-dw6-cpp, limpio.
- Bloque: App.cpp 568..608 = 41 lineas (608-568+1 = 41); la anatomia
  declarada suma lo mismo: 1 (comentario 568) + 30 (giroPointsFrom
  569..598) + 1 (blanco 599) + 1 (comentario 600) + 8 (giroValueOf
  601..608) = 41.
- Retirada: 568..609 = 42 lineas (609-568+1), bloque mas el blanco
  adyacente 609; queda blanco unico en 567. Movimiento limpio, sin
  dobles blancos.
- Header: H=47 = 41 movidas + S=6 (pragma, blanco, <vector>,
  GiroAdapter.h, IonosondeLayer.h, blanco); las 41 ocupan 7..47
  (47-7+1 = 41). Cada include justificado uno a uno; App.cpp ya los
  incluye (lineas 18, 45, 52); guardas sin ciclo; static conservado
  con un unico includer. Andamiaje conforme a la regla del acta 0465
  seccion 2.
- App.cpp: +1/-42 exacto (include tras linea 2). PR esperado desde
  b392e68: 3 ficheros, +190/-42 = 142 (doc) + 47 (header) + 1
  (include). Cuenta exacta.
- Grep PRE coherente: giroPointsFrom en 4 lineas (569 def; 2245,
  2478, 2481 usos); giroValueOf en 3 (601 def; 637 y 659 usos dentro
  de giroInterpGrid, que permanece en App.cpp); 0 en tests; 0 en
  otros ficheros de src/.
- Predicciones del POST (fijadas ANTES de la evidencia): cuadran una
  por una. Header: nueva = vieja - 561 en las cinco anclas (568->7,
  569->8, 600->39, 601->40, 608->47), corrimiento uniforme y
  consistente con el bloque en 7..47. App.cpp: nueva = vieja - 41
  (= +1 del include - 42 de la retirada) en los cinco usos (637->596,
  659->618, 2245->2204, 2478->2437, 2481->2440). Totales POST 4/3
  invariantes (definiciones al header en :8 y :40; usos en App.cpp),
  0 en tests.
- Anclajes re-medidos sobre la baseline: configure rc=0; build rc=0
  (290 pasos); ctest 54/54 rc=0; ctest -N = 54 (fixtures ebro
  gitignored copiados al worktree, fuera del commit). Anclaje dual
  del acta 0463 seccion 2 exigido SIN cambio: local 54/54 con
  fixtures y CI 53 passed + 1 skipped (ebro_parse, exit 77; 54
  slots / 0 fallos). CI del repo 2/2 (ctest y ThreadSanitizer), en
  el PR y en el push. No se reutiliza el ancla web 48/461/0.
  Conforme.

## 4. Dictamen sobre 4cf7e74 y condiciones de ejecucion

- DICTAMEN: FAVORABLE SIN RESERVAS. El pre-registro cumple la
  disciplina completa: gobierno registrado, rama publicada antes del
  PR, movimiento literal planificado, andamiaje justificado linea a
  linea, predicciones congeladas antes de la evidencia (disciplina
  DW.5, acta 0466: 8/8 aciertos), anclas re-medidas y doble ancla
  exigida.
- Recomiendo a David: dar el GO para ejecutar.
- Condiciones de ejecucion (ya comprometidas en el pre-registro; se
  listan para la acta de ejecucion): (a) bloque movido byte
  identico; (b) evidencia con tabla prediccion/observado completa
  (ferry to-glm/files/DW.6/: 10 numerados + MANIFEST + SHA256SUMS de
  11 entradas, convencion acta 0466 seccion 3); (c) App.cpp +1/-42
  exacto y PR 3 ficheros +190/-42; (d) anclaje dual sin cambio y CI
  2/2; (e) sin amend ni force-push; (f) cualquier desviacion de lo
  predicho se declara como dual-track y se audita antes del GO de
  merge.
- Interpretacion fijada de antemano (evita pseudo-dual-tracks): el
  grep POST se emite con ambito src/ + tests/; docs/ queda fuera
  (el propio pre-registro nombra los helpers y no es codigo). Con
  ese ambito, los totales 4/3 deben salir exactos.

## 5. Puntos que este lado NO ha verificado aun (transparencia)

- Bundles entregados: cotejo local por sha256 y diffstat del
  baseline (seccion 2): pendiente de sandbox, proxima acta.
- Lineas base reales de App.cpp (568..608, usos, includes en
  18/45/52): este lado no tiene acceso directo al repo; se auditaran
  contra la evidencia del ferry (prediccion/observado), como en
  DW.5.
- Fichero y triple de esta acta 0471: tras la recuperacion del
  sandbox (nota de metodo).
- Sugerencia menor (no gate): NA=0 tambien en los documentos del
  repo (el pre-registro declara NA=2 por un simbolo de seccion)
  simplificaria los cotejos futuros.

## 6. Triple del acta 0470, declarado en este texto (regla del 0468 seccion 3)

- Acta 0470 (emitida el turno anterior: conformidad 0485, ledger
  completo): sha256
  7b58aacf20d5d90121ec039d9d73770ac2d6bf0c6ad3898fe91eeec0fad77f70,
  5961 B, 112 lineas, NA=0, compuesta sin blancos entre vinetas y
  fechada por Madrid.

## 7. Estado y pendientes

- C++ master b392e68; rama dw.6-appcpp-grid en 4cf7e74 (solo el doc
  del pre-registro). Web congelada en 9eca362. Android 59f539b.
- GO pendiente: el de David para EJECUTAR DW.6 (recomendacion de
  este lado: darlo). Despues: acta de ejecucion con la tabla
  prediccion/observado y GO de merge.
- Pendientes administrativos: confirmacion de archivo del acta
  0470; verificacion local de los bundles; fichero y triple del
  0471; bundle delta b392e68..4cf7e74 al publicarse.

## 8. Cierre

Respuesta directa a la pregunta de David: SI, este lado recomienda
dar el GO para ejecutar DW.6 tal como esta pre-registrado. La proxima
acta GLM sera la de ejecucion o la de verificacion local de bundles,
lo que llegue primero.

- GLM, lado auditor, 2026-11-23 (Madrid).
