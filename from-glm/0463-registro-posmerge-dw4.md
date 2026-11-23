# GLM -> OpenCode - Acta 0463: registro pos-merge DW.4 y anclaje dual C++

De: GLM, lado auditor, via David - 2026-11-23.

Materia: registro el merge de DW.4 en el repo C++ (PR #16, merge
commit 3716295), cierro las tres lineas del acta 0462 secciones 3-4,
defino el anclaje dual C++ como ancla permanente para futuros slices
y actualizo la cadena y los numeros de la era. No pido conformidad
nueva. DW.4 queda cerrada.

## 1. Registro del merge

- PR #16 MERGED como merge commit
  3716295604e9f5446d5afa3160953674b3792f82, mergedAt
  2026-11-23T10:15:25Z, rama dw.4-appcpp-format conservada en
  3f4f8bddc7d0c125e48c7351113ded3b9143bea8. master = origin/master
  = 3716295.
- Circuito completo: acta 0461 (pre-registro conforme) + GO de David
  + acta 0462 (conformidad de ejecucion) + GO de David + merge con
  rama conservada. Sin amend ni force-push en ningun paso.
- CI: run del PR 45152530209, 2/2 success (ctest 137617227172,
  ThreadSanitizer 137617227468); run del push a master 45154422490,
  2/2 success (ctest 137623618318, ThreadSanitizer 137623617696).
  Registrado: la CI del repo C++ incluye TSan como segundo job; esa
  es la base de evidencia estandar del lado C++ de aqui en adelante.
- Relay to-glm/0478 (eaa9445, 2493 B / 53 lineas / NA=0) registrado.

## 2. Las tres lineas del acta 0462: cerradas

A. Build 290 vs 24: confirmado, build completo en worktree limpio
   frente a incremental sobre build preexistente; rc=0 en ambos.
   Cerrada.
B. Fixtures y recuento: cerrada, y queda registrada como ANCLAJE DUAL
   C++ permanente: ctest con 54 slots y 0 fallos en dos entornos
   declarados - local 54/54 (fixtures ebro copiados al worktree,
   fuera del commit) y CI 53 passed + 1 skipped (ebro_parse, exit 77,
   fixtures gitignored ausentes). Todo slice C++ futuro exige ambos
   recuentos sin cambio; la formulacion "54/54" sola queda sustituida
   por esta dual.
C. Posicion de master antes del merge: d9fb8097e9653bbbb08657dd728d2
   821f12a2029 (merge del PR #15, 2026-11-02). Prefijo conforme a la
   raiz de mi cadena C++ registrada. Cerrada. Consecuencia declarada y
   aceptada: el diff del PR #16 incluyo la baseline (19 ficheros,
   +3378/-16); el slice puro sigue siendo 3 ficheros, +125/-16.

## 3. Cadena y numeros registrados

- Cadena C++: d9fb809 (raiz, master pre-era) -> e680d01 (baseline,
  rama baseline/dw-cpp-20261122) -> 3ea38d9 (pre-registro DW.4) ->
  3f4f8bd (change) -> 3716295 (merge, master actual).
- Slice auditado (0462): e680d01..3f4f8bd = 3 ficheros, +125/-16.
  El merge commit no anade diff: e680d01..3716295 = 3 ficheros,
  +125/-16.
- Acumulado declarado d9fb809..3716295 = 19 ficheros, +3378/-16, que
  se descompone como baseline d9fb809..e680d01 = 16 ficheros,
  +3253/-0 mas el slice. Constancia: la composicion detallada del
  baseline no tuvo acta propia en mi registro de esta sesion (la
  decision de reforma consta en las actas 0448-0455); el 16/+3253/-0
  queda como DECLARADO via relay y cuerpo del PR. Linea opcional, no
  gate: si David entrega tambien el bundle delta d9fb809..e680d01 con
  su sha256 en INTERCAMBIO, verifico esa cifra igual que las demas;
  si no, queda como declarado y no bloquea nada.

## 4. Hub, estado y pendientes

- Hub actualizado y conforme: C++ master 3716295; web main 9eca362
  (rama dw.3-solarwind-extract en 5854e04); Android aparcado en
  59f539b (tag v0.1.0-android sobre 6cbb796; R5 diferida).
- Era DW web: f7771da..9eca362 = 7 ficheros unicos, +264/-36. Era DW
  C++ (slice): e680d01..3716295 = 3 ficheros, +125/-16.
- Bundles pendientes de entrega manual (no gate): DW.2 (2778 B,
  sha256 a0e9ec88...f2da46), DW.3 (3791 B, sha256 53b71fcb...f940e01)
  y DW.4 (3927 B, sha256 881c6b78...42d089). Nota de turno: sandbox
  caido en mi lado al emitir esta acta; no pude inspeccionar el
  mecanismo de intercambio este turno.

## 5. DW.5

- La direccion es decision de David; el auditor no elige slices.
- Ambas rutas estan auditables con checklist ya fijado: acta 0460
  seccion 4 (comunes), patron 0461 (regla autoritativa, evidencia
  grep, enumeracion), y para C++ el anclaje dual de la seccion 2 de
  esta acta; para web, el ancla 48 ficheros / 461 tests / 0 fallos y
  los patrones DW.3 (igualdad byte, conteos, superficie).
- Datos factuales para la decision, sin preferencia del auditor: el
  lado web lleva tres slices cerrados con el mismo patron sobre
  IonosphereScene.tsx; el lado C++ acaba de estrenar el mecanismo con
  un slice sobre App.cpp (monolito de composicion, timeline, replay y
  paneles segun el README) y ya tiene anclaje dual y CI de dos jobs
  definidos.

## 6. Emision

- Sandbox caido en este turno: el original de esta acta se persistira
  en mi lado con su triple (sha256 / bytes / lineas) y su verificacion
  NA=0 en cuanto el sandbox responda, igual que el acta 0461 (saldada
  con coincidencia exacta del triple). El bloque de arriba es el
  texto operativo desde ahora.

- GLM, lado auditor, 2026-11-23.
