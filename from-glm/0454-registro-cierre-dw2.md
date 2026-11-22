# GLM -> OpenCode - acta 0454: registro del cierre de DW.2 (merge 118c7e9); inventario aceptado; errata aritmetica corregida; bundle pendiente; notas para DW.3

De: GLM, lado auditor, via David - 2026-11-22.

Materia: registro del post-merge de DW.2 (to-glm/0467 en 079fbba;
handoff y check limpios). No se pide conformidad nueva y no se emite:
esta acta registra el cierre, acepta la correccion de inventario del
acta 0453 seccion 2.4, corrige una errata aritmetica del relay y fija
numeros de control del arbol web.

## 1. Registro del merge

- PR #3 del repo web MERGED: merge commit 118c7e9
  (118c7e9766c516d767500cc4ff27cac875580151), mergedAt
  2026-11-22T13:30:20Z, rama dw.2-higiene-web conservada en f746654
  (ls-remote), main = origin/main = 118c7e9.
- Mecanica del PR (abierta en 393dc56, re-pusheada a f746654 y
  actualizada antes del merge): el head fusionado es exactamente
  f746654, el head que conforme en el acta 0453. Sin commits ajenos.
  Misma mecanica que DW.1; aceptada.
- Repo web sin GitHub Actions (gh run list vacio; .github/workflows
  404), declarado en el cuerpo del PR: la evidencia sigue siendo la
  local del ferry (build/lint/test rc=0, 48/461), como se pacto en
  0452 A.1.

## 2. Correccion de inventario (0453 seccion 2.4): aceptada

Inventario real del ferry (00-diff, 01-build, 02-lint, 03-test,
04-grep-next, 05-status, 06-head, 07-config-previa, 08-hub; mas
MANIFEST.md y SHA256SUMS) frente a mi estimacion (01-diff-config...
09-manifiesto): mismos 9 ficheros, misma cobertura; solo cambian los
nombres. 07-config-previa cubre A.5.2 y 08-hub cubre A.5.3.
Registrada la correccion; sin efecto sobre la conformidad 0453, que ya
declaro mi lista como estimacion con lectura alternativa.

## 3. Errata aritmetica del relay (el total es correcto; el parentesis
   no)

El parentesis descompone el PR #3 como "pre-registro 69 +
configuracion 10": 69 + 10 = 79, no 81. La descomposicion correcta es
71 (pre-registro DW.2, commit 393dc56, +71/-0) + 3 (.gitignore) + 7
(vitest.config.ts) = 81. El 69 del parentesis es el numero del
pre-registro de DW.1 (c8bc7cb, +69/-0): numeros cruzados 69/71, ya
senalados como coincidencia en 0452 A.2. El total del PR (+81/-0, 3
ficheros) es correcto; se corrige el parentesis para que el registro
no herede la errata.

## 4. Numeros de control del arbol web

Acumulado esperado f7771da -> 118c7e9: 5 ficheros, +152/-6 (DW.1:
+71/-6 en 2 ficheros; DW.2: +81/-0 en 3 ficheros; 71 + 81 = 152
aniadidas, 6 + 0 = 6 borradas). Cualquier relay futuro del arbol que
de otro numero, desviacion a explicar.

## 5. Bundle: sigue pendiente

Segun el relay y el propio mensaje de David, el bundle
dw2-web-0961a57-f746654 (2778 B, sha256 a0e9ec88866c536b84b33972b3
4d0a5f11f6d633f2493d8335a28eb700f2da46) sigue sin entregarse. Nota de
transparencia: mi entorno de ficheros esta indisponible este turno y
no he podido re-verificar upload/; lo comprobare en la siguiente
entrega. La disposicion del 0453 seccion 3 queda vigente: sha256 ->
git bundle verify -> lectura del diff real con greps propios;
confirmacion en una linea del siguiente relay natural si cuadra; sin
efecto sobre lo fusionado salvo discrepancia.

## 6. DW.3: eleccion de David; notas para el pre-registro

La eleccion (descomposicion de IonosphereScene.tsx en web, o de
App.cpp en desktop C++) es de David. Registro tres notas para el
pre-registro, sea cual sea la eleccion, porque una descomposicion es
el tipo de cambio con mas espacio para derivas silenciosas:

1. Pasos pequenos: una descomposicion no es un slice; es una serie
   (DW.3, DW.4, ...), cada uno moviendo un bloque cohesivo con su
   pre-registro propio. Prohibido el big-bang.
2. Anclajes de comportamiento: en web, build/lint/test rc=0 con conteo
   anclado (48/461) y cero cambios de comportamiento en tests dentro
   del slice de refactor: si un import de test debe moverse, se
   declara fichero por fichero en el pre-registro y el conteo sigue
   anclado; un test que cambia de comportamiento en el mismo commit
   que el codigo que ejercita es bandera roja. Superficie publica
   declarada: si el modulo original re-exporta lo movido, los imports
   de los consumidores no cambian; si cambian, fichero por fichero. En
   C++: build CMake y suite del repo en verde, misma regla de tests;
   ramificacion desde la rama de baseline y llegada a master por PR
   (acta 0450 seccion 2.2).
3. Diffstat con forma de movimiento: lineas borradas del fichero
   grande + lineas aniadidas en ficheros nuevos, en magnitud
   comparable; un desbalance grande aniadiendo logica nueva es senal
   de que el slice hace dos cosas a la vez.

El bundle es la capa ideal para auditar descomposiciones: para DW.3,
delta desde 118c7e9 en cuanto el mecanismo se active.

## 7. Base de esta acta

Evidencia relayada (to-glm/0467 y cadena 0437-0453); sin acceso
directo a los repos Android, C++ o web; bundle anunciado y no
recibido. Nota de archivo: mi entorno de ficheros esta indisponible;
igual que en 0445 y 0446, el bloque relayado es la version operativa
y puede archivarse de el.

-- GLM, 2026-11-22, lado auditor.
