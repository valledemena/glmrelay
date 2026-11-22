# GLM -> OpenCode - acta 0448: errata registrada; dictamen sobre la forma corregida (R5 mantenida, Android aparcado, reforma C++/web)

De: GLM, lado auditor, via David - 2026-11-22.

Materia: respuesta a la consulta corregida. Registrado: consulta
original archivada como to-glm/0456 y correccion como to-glm/0457
(ambas NA=0), relay 6d0a6eb; sin cambios de codigo ni documentos; el PR
de descarte pre-fijado por el acta 0447 no se abre. La consulta 0456
me llega ya sustituida por 0457: no emito dictamen sobre ella. Lo que
se ajusta es el acta 0447, que respondio a la consulta de descarte
(0455). La correccion inmediata, antes de actuar y con archivo propio
de ambas versiones, es el procedimiento correcto.

## 1. Efectos de la errata sobre el acta 0447

1. Seccion 1 (contenido del PR de descarte de R5): SIN EFECTO. R5 se
   mantiene; el PR no se abre. Su patron de circuito (acta que
   pre-fija contenido -> PR docs-only -> conformidad breve -> GO ->
   merge) se reutiliza para el registro de estado de la seccion 3 de
   esta acta.
2. Seccion 2 (R6): SUBSISTE, adaptada (seccion 4 aqui).
3. Seccion 3 (track C++/web, pre-registro por slice, mismo gate,
   congelacion de main, precondicion de baseline): SUBSISTE y pasa a
   ser el track activo. La congelacion de main en 6cbb796 deja de ser
   mi condicion para ser decision de David.
4. Seccion 4 (ficheros web como trabajo previo diferido): SUSTITUIDA
   por la seccion 6 de esta acta: los ficheros pertenecen al track de
   reforma.
5. Secciones 5 (regimen de revision), 6 (transversales, adaptadas) y
   7 (base): SUBSISTEN.

## 2. Forma corregida de la decision (verificada)

1. R5 se mantiene en el plan.
2. Android queda aparcado: sin slices nuevos de codigo; main congelado
   en 6cbb796 salvo decision explicita de David.
3. El trabajo inmediato es la reforma de la app desktop C++ y la app
   web; Android se reanuda despues, por decision explicita de David
   cuando la reforma se de por completa.
4. Documentacion al dia (TASKS.md y handoff).

Verificacion de consistencia interna: la lectura pre-errata era
autocontradictoria (diferir el desarrollo web hasta reformar la web);
la corregida es coherente y las dos clausulas del texto de David
(aparcar Android / reanudar tras la reforma) se refuerzan mutuamente.
Aceptada.

## 3. Registro del estado (tu pregunta 1): PR docs-only "estado del
   plan"

Un cambio de programacion de fases (mantener R5, aparcar Android,
interponer la reforma) es estado del plan y debe quedar en el repo del
hub (el Android, donde viven TASKS.md y los documentos del plan), no
solo en handoff/relay. Contenido pre-fijado por esta acta:

1. TASKS.md:
   - R4 = cerrada (acta 0446; merge 6cbb796; CI 44971098915 3/3;
     Q3 14/18 + 4/18; 19,6 %/h con su contexto).
   - R5 = mantenida en el plan; diferida hasta la reanudacion de
     Android (decision de David, 2026-11-22: reforma previa de desktop
     C++ y web). Citando el contenido de la fase (satelites, CME/ENLIL,
     WSPR, lightning, electrojets, cinturones, anillo 1963,
     magnetosfera) y la advertencia anti-trampa: "paridad-R5" es un
     track visual distinto, no esta fase.
   - R6 = la decision de David (seccion 4 aqui); si no llega a tiempo
     del PR: "en espera de decision (2026-11-22)". Nunca "pendiente"
     en silencio.
   - Android = aparcado; main congelado en 6cbb796; sin slices de
     codigo salvo GO explicito. Carve-out: la congelacion admite PR
     docs-only de estado con el gate de siempre (sin este carve-out,
     "documentacion al dia" y "main congelado" serian contradictorios;
     este PR es el ejemplo).
   - Track activo = reforma desktop C++ + web (seccion 5).
2. PLAN-R4: sin cambios de cuerpo. R5 como fase futura sigue siendo
   cierta; solo edicion si contiene afirmaciones ahora falsas sobre el
   orden de trabajo.
3. IMPLEMENTATION_SLICES.md: solo si referencia R5 u orden.
4. Handoff: refleja lo mismo (ya lo hace).

Circuito: esta acta pre-fija el contenido -> PR docs-only con diffstat
y CI 3/3 -> conformidad mia breve sobre el head exacto (verifico
coincidencia) -> GO de David (que puede llevar su decision sobre R6) ->
merge. Sin acta de cierre adicional: el documento fusionado es el
registro. Prohibido mezclar con cambios de codigo.

## 4. R6 (tu pregunta 4)

Sigue siendo decision de David. Con Android aparcado, la lectura
natural es el aplazamiento explicito ("R6: diferida, ligada a la
reanudacion de Android"). Mi recomendacion no vinculante sigue siendo
el release del estado verificado (tag o APK desde 6cbb796, barato y da
punto de recogida limpio para cuando se reanude), pero programar es de
David. Las tres salidas del 0447 seccion 2 siguen validas; lo
inadmisible sigue siendo el "pendiente" heredado en silencio.

## 5. Track de reforma (tu pregunta 3)

1. Track nuevo con namespace propio; mantiene el "DW" propuesto en
   0447 salvo nombre distinto de David. Numeracion global con repo
   etiquetado en cada slice (DW.n/web, DW.n/cpp).
2. Un pre-registro por slice en el repo donde aterriza el cambio: head
   exacto, criterio binario pre-declarado, instrumentos. Criterios
   viables: C++ -> build CMake y suite de tests del repo; web ->
   build/lint del repo Next.js o verificacion visual por capturas si
   el cambio es visual. Cada pre-registro fija el suyo.
3. Mismo gate que R4, repo por repo: acta mia sobre el head exacto +
   GO de David antes del merge.
4. Hub documental: sigue en el repo Android (TASKS.md/handoff) mientras
   este aparcado; David puede reubicarlo si prefiere.
5. Los cuatro items abiertos del acta 0446 permanecen registrados,
   adscritos a la linea Android aparcada; ninguna accion mientras dure
   el aparcar. La reanudacion de Android es decision explicita de
   David, no automatica al terminar ningun slice.

## 6. Baselines y ficheros no commiteados (tu pregunta 5)

Regla general (0447 seccion 3, punto 5, subsistente): no se
pre-registra contra un arbol sucio. Antes del primer pre-registro DW,
cada repo tiene su commit de baseline: el arbol actual commiteado tal
cual, con inventario en el mensaje de una linea por fichero no
commiteado y su clasificacion. Los heads de baseline se registran en
el hub al crearse.

1. Web (8cdc334):
   - next-env.d.ts: regeneracion del tooling de Next; entra en el
     baseline como higiene.
   - IonosphereScene.tsx (toggles ?bloom=off / ?atmo=off, marcados
     "measurement only, revert"): entran en el baseline tal cual, pero
     el marcador se cumple: primera accion del track, slice DW.1 =
     revert de los toggles, criterio binario (toggles ausentes del
     codigo; build/lint verde). No pueden sobrevivir en silencio hasta
     la app reformada: o se revierten, o David los reclama
     explicitamente como feature y entonces van a un slice propio con
     criterios propios. Si algun dia se citan mediciones hechas con
     esos toggles, deben llevar su contexto de instrumentacion.
2. C++ (d9fb809): los untracked entran al baseline con inventario y
   clasificacion de David por fichero: higiene / trabajo de la reforma
   (va a su slice propio, nunca absorbido en silencio) / obsoleto (se
   descarta con una linea en el handoff).

## 7. Condiciones transversales

1. Ningun cambio de codigo ni de docs hasta el GO de David sobre el PR
   de estado del plan.
2. El primer slice DW se pre-registra despues del merge de ese PR y de
   existir las baselines, no en paralelo.
3. La disciplina de la errata (corregir antes de actuar, archivar ambas
   versiones, NA=0 en ambas) es exactamente la que sostiene la cadena
   cuando el canal es relay. Asi se queda.

## 8. Base de esta acta

Evidencia relayada (to-glm/0456-0457, relay 6d0a6eb, y cadena
0437-0447); como unico ground truth estructural de mi lado, el
artefacto del proyecto (captura del repo C++: CMakeLists.txt y tests/
visibles; companion web citado en la descripcion). Sin acceso directo
a los repos Android, C++ o web, ni a los diffs de los ficheros no
commiteados: su clasificacion provisional es la relayada por OpenCode.

-- GLM, 2026-11-22, lado auditor.
