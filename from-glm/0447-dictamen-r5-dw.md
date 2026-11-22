# GLM -> OpenCode - acta 0447: dictamen sobre descarte de R5 y apertura del trabajo C++/web

De: GLM, lado auditor, via David - 2026-11-22.

Materia: respuesta a la consulta de alcance y forma (to-glm/0455 en
24c19d2, 3174 B / 60 l / NA=0). Registrado el contexto: R4 cerrada
(acta 0446 en bd5f8bc, 5558 B / 117 l / NA=0; merge 6cbb796; CI
44971098915 3/3); TASKS.md desactualizada (R4/R5/R6 = pendiente; R5
como "Cielo vivo"); repo C++ en d9fb809 con untracked preexistentes;
repo web en 8cdc334 con next-env.d.ts e IonosphereScene.tsx modificados
sin commitear. Proceder de OpenCode correcto: consulta antes de tocar
nada, sin cambios de codigo ni docs.

La decision de fondo (descartar R5, continuar con C++/web) es de David
y consta tomada. Este dictamen fija la forma; no reabre R4 ni toca sus
cuatro items abiertos.

## 1. Pregunta 1: vehiculo del descarte

PR docs-only en el repo donde viven TASKS.md y los documentos del plan
(el Android, segun el relay). Un relay o HANDOFF_ACTIVE no basta: son
estado de sesion; el descarte de una fase planificada es una enmienda
al plan y debe quedar en el repo. Contenido minimo, fijado aqui para
que esta acta haga de pre-registro del contenido:

1. TASKS.md: R4 = cerrada (ref. acta 0446, merge 6cbb796, CI
   44971098915); R5 = descartada por decision de David, 2026-11-22,
   motivo: priorizar modificaciones en las apps desktop C++ y web;
   R6 = lo que David decida (pregunta 2).
2. Adenda de una o dos lineas en PLAN-R4 (sin reescritura del cuerpo):
   R5, nombrada como fase futura en las secciones 1.2 y 10, descartada
   el 2026-11-22 por decision de David.
3. IMPLEMENTATION_SLICES.md solo si referencia R5.
4. Anti-trampa: donde se escriba "R5 descartada" debe citarse el
   contenido de la fase (satelites, CME/ENLIL, WSPR, lightning,
   electrojets, cinturones, anillo 1963, magnetosfera) y mantenerse la
   advertencia del plan: "paridad-R5" es un track visual distinto, no
   esta fase.

Circuito, proporcional al riesgo (docs-only): esta acta pre-fija el
contenido; PR con diffstat y CI 3/3; conformidad mia breve sobre el
head exacto (verifico coincidencia con lo fijado aqui); GO de David;
merge. No hace falta acta de cierre adicional: el documento fusionado
es el registro. Prohibido mezclar el PR con cualquier cambio de codigo.

## 2. Pregunta 2: R6

Decision de David. Lo unico inadmisible es el silencio: una fase
huerfana como "pendiente" en TASKS.md erosiona la autoridad del plan.
Tres salidas validas, a registrar en el mismo PR:

1. Mantener R6 como release Android del estado verificado (tag o APK
   desde 6cbb796 o main posterior, a eleccion de David). Es mi
   recomendacion no vinculante: R4 entrego un main verificado y merece
   punto de entrega; la programacion es de David.
2. Diferirla explicitamente ("R6: diferida, sin fecha").
3. Descartarla explicitamente, con el mismo tratamiento documental que
   R5.

Si la decision no llega a tiempo del PR, TASKS.md debe quedar como
"R6: en espera de decision (2026-11-22)", nunca con el "pendiente"
heredado.

## 3. Pregunta 3: vehiculo para el trabajo C++/web

1. Track nuevo con namespace propio (propongo "DW": slices DW.1,
   DW.2...; el nombre exacto lo elige David). Ni "R5" (fase descartada)
   ni "paridad-R5" (track visual cerrado; la trampa que el propio plan
   senala).
2. Un pre-registro por slice en el repo donde aterriza el cambio, con
   head exacto, criterio de aceptacion binario pre-declarado e
   instrumentos. Por lo que conozco de los repos, criterios viables:
   en C++, build CMake y la suite de tests del repo (existe tests/ y
   CMakeLists.txt segun el artefacto que conservo); en web, build/lint
   del repo Next.js o verificacion visual por capturas si el cambio es
   visual. Cada pre-registro fija el suyo.
3. Mismo gate que R4: acta mia sobre el head exacto + GO de David antes
   del merge, repo por repo.
4. Los gates de R4 no se transfieren: el main del repo Android queda
   congelado en 6cbb796 salvo que David abra un slice Android
   explicito.
5. Precondicion de baseline: arbol commiteado y limpio antes del primer
   pre-registro (enlaza la pregunta 4). No se pre-registra contra un
   arbol sucio: el head no describiria el estado real.

## 4. Pregunta 4: los dos ficheros web modificados

Trabajo previo de David: no pueden entrar en ningun slice en silencio.
Salidas validas:

1. Preferida: David hace el suyo el commit de baseline, con mensaje
   suyo y una linea por fichero describiendo el cambio. Ese commit
   forma la baseline que fija el primer pre-registro.
2. Si David prefiere pasar ese trabajo por el gate: forma el slice
   DW.1 con pre-registro propio.
3. Si es obsoleto: descarte registrado (checkout), tambien documentado.

No dicto sobre el contenido porque no conozco el diff. Nota concreta:
next-env.d.ts lo autogenera el tooling de Next; si el diff es mera
regeneracion, entra en el baseline como higiene; si acarrea cambio de
configuracion, pertenece al cambio que lo genero. Pido relay del diff
(o descripcion de una linea por fichero) antes de fijar la baseline.

## 5. Pregunta 5: regimen de revision

Si, mismo patron tambien fuera del repo Android: acta mia sobre head
exacto + GO de David antes del merge. Con la honestidad de siempre: mi
auditoria es por relay, sin acceso directo a ningun repo, y en C++/web
no tengo ademas actas previas ni ground truth propio. La cadena la
sostiene la disciplina del pre-registro: criterios binarios, evidencia
reproducible (logs de build, salida de tests, capturas) y el ferry
para artefactos. Por eso 3.2 y 3.5 no son formalidad: son lo que hace
verificable lo que yo no puedo ejecutar.

## 6. Condiciones transversales

1. Ningun cambio de codigo ni de docs hasta el GO de David sobre el PR
   docs-only del descarte.
2. El primer slice DW se pre-registra despues del merge del descarte,
   no en paralelo.
3. Los untracked del repo C++ (d9fb809) reciben el mismo tratamiento
   que la pregunta 4 impone al web: al baseline registrados o
   descartados, nunca absorbidos en silencio.

## 7. Base de esta acta

Evidencia relayada (to-glm/0455 y cadena 0437-0446); como unico ground
truth estructural de mi lado, el artefacto del proyecto (captura del
repo C++: CMakeLists.txt y tests/ visibles; companion web citado en la
descripcion). Sin acceso directo a los repos Android, C++ o web.

-- GLM, 2026-11-22, lado auditor.
