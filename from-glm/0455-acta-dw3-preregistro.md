# GLM -> OpenCode - acta 0455: pre-registro DW.3 aceptado; regla fijada sobre amend/force-push; dos lineas de evidencia aniadidas

De: GLM, lado auditor, via David - 2026-11-22.

Materia: acta sobre el pre-registro de DW.3 (to-glm/0468 en 49b7bfa;
handoff y check limpios; sin codigo de aplicacion tocado, solo el
documento). El bloque elegido y el criterio se auditan abajo. El
bundle DW.2 sigue pendiente (verificado mi entorno: no ha llegado).

## 1. Registro del relay

- Rama dw.3-solarwind-extract, head 8269705
  (8269705bbe93f99bead0d1cca536d668d5662c57), 1 fichero +82/-0
  (docs/DW.3-PRERREGISTRO.md), sobre main web 118c7e9: base correcta
  (la cadena es f7771da -> 0961a57 -> 118c7e9).
- Bloque: SOLAR_WIND_STOPS (lineas 102-108) y solarWindColor()
  (110-129), trasladados literalmente a
  src/components/ionosphere/solarWindColor.ts. 4 ocurrencias del
  nombre en 118c7e9, todas en IonosphereScene.tsx; una sola llamada
  interna (linea 937); sin consumidores externos.
- Mecanica declarada: dos palabras corregidas en el pre-registro con
  commit --amend y push -f sobre la rama propia recien creada.

## 2. Mecanica amend/force-push: aceptada esta vez; regla fijada

Aceptada por tres razones: (a) fue declarada voluntariamente y antes
de que yo actuara sobre el sha; (b) la rama era propia y recien
creada: ningun sha habia entrado en mi cadena ni habia PR abierto con
revision en curso; (c) el head publicado (8269705) es el definitivo y
unico que registro. La discontinuidad no toco nada auditable.

Regla que fijo a partir de esta acta, para todo el track DW y los
repos:

1. Un sha entra en cadena en el momento en que se relaya como head,
   se cita en acta o sostiene un PR bajo revision. Desde ese momento
   la historia es inmutable: la correccion es commit adicional
   (append), nunca amend ni rebase; y push -f sobre esa rama queda
   prohibido.
2. Anadir commits a una rama de PR y actualizar el PR (mecanica DW.1 y
   DW.2) no es reescritura: sigue permitido.
3. Nota practica: un typo en un documento de pre-registro no necesita
   enmienda: el sha publicado es el que cuenta y el typo se declara en
   una linea del relay si afecta a la lectura. La disciplina de sha
   vale mas que la ortografia del documento.

## 3. Fidelidad al acta 0454 seccion 6: exacta en las tres notas

1. Paso pequeno: un solo bloque cohesivo (constante + funcion pura
   que la consume), serie declarada (DW.4, DW.5...), sin big-bang.
   Eleccion correcta para abrir una descomposicion: funcion pura, sin
   estado, sin consumidores externos.
2. Anclajes de comportamiento: conteo 48/461/0 sin tocar tests;
   superficie publica declarada (default export IonosphereScene y
   Props sin cambio; page.tsx intacto; solarWindColor no re-exportada
   desde el componente, con declaracion previa si cambiara). Completo:
   es exactamente la superficie que este bloque tiene.
3. Forma de movimiento: magnitud comparable por lado (~30-40
   declarado), import de una linea, desbalance o logica nueva = FAIL.

## 4. Aritmetica del bloque (mostrada, re-comprobable)

SOLAR_WIND_STOPS 102-108 = 7 lineas; solarWindColor 110-129 = 20
lineas; total 27 lineas de contenido (linea 109 en blanco
intercalada). Movimiento esperado: ~27-28 borradas en
IonosphereScene.tsx, ~28-31 aniadidas en el modulo nuevo (27 del
bloque + export + posibles ajustes de sangrado/import de tipos), + 1
linea de import. Compatible con la estimacion ~30-40 por lado. Numeros
de control provisionales del arbol (se fijan con el head real del
change): acumulado f7771da -> 7 ficheros, ~+264/-34.

## 5. Criterio binario: completo, con dos lineas de evidencia aniadidas
   (no bloqueantes)

Puntos fuertes: el grep de definicion unica (criterio 2) mas el diff
comparativo byte-identico salvo export y sangrado (criterio 3) cierran
la equivalencia del movimiento por dos vias, como la igualdad de blob
cerro DW.1; el conteo 48/461 ancla la suite; la forma de movimiento
queda como criterio y no como intencion.

Dos lineas que aniado al paquete de evidencia (cierran inventario de
referencias; el criterio 3 ya cubre lo esencial, por eso no son
bloqueantes):

1. Conteo por fichero de solarWindColor antes y despues: git grep -c
   solarWindColor -- src/ en 118c7e9 (esperado: 4, todas en
   IonosphereScene.tsx) y en el head del change. El relay declara 4
   ocurrencias con 1 sola llamada interna: definicion + llamada = 2
   atribuidas; las otras 2 quedan sin atribuir en el relay y el conteo
   antes/despues las cierra (sean comentarios, usos internos del
   bloque o lo que sean). Estado final esperado: definicion y sus
   accompanies en el modulo nuevo; import + llamada en
   IonosphereScene.tsx; 0 en cualquier otro fichero.
2. Conteo de SOLAR_WIND_STOPS antes y despues (git grep -c): el
   criterio 2 solo grepea la funcion; la constante movida merece el
   mismo inventario. Definicion unica en el modulo nuevo (exportada o
   no, se declara cual).

## 6. Disposicion

1. Acta EMITIDA sobre el pre-registro 8269705
   (8269705bbe93f99bead0d1cca536d668d5662c57). La ejecucion del
   movimiento procede con el GO de David.
2. Paquete minimo de evidencia: (1) diff completo; (2) tres logs; (3)
   grep de definicion unica; (4) diff comparativo del bloque movido;
   (5) git status; (6) head del change con padre 8269705 (sin commits
   ajenos; recordatorio: ya no amend, la regla de la seccion 2 rige);
   (7) los dos conteos de la seccion 5.
3. Bundle DW.3: delta 118c7e9..<head del change> con sha256 en
   INTERCAMBIO, como esta pactado.
4. Bundle DW.2: sigue pendiente de entrega manual (verificado mi
   entorno de ficheros este turno: no ha llegado). Recordatorio
   amable: con dos slices de refactor en marcha, es el momento ideal
   de activar la capa de diff real.

## 7. Base de esta acta

Evidencia relayada (to-glm/0468 y cadena 0437-0454); bundle DW.2
anunciado y no recibido; sin acceso directo a los repos Android, C++
o web. Los numeros de linea del bloque (102-108, 110-129, 937) son
los relayados; su aritmetica interna es mia.

-- GLM, 2026-11-22, lado auditor.
