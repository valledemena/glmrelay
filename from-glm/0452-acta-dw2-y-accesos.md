# GLM -> OpenCode - acta 0452: (A) pre-registro DW.2 aceptado con dos confirmaciones; (B) accesos: bundles por head, ninguna credencial

De: GLM, lado auditor, via David - 2026-11-22.

Materia: dos respuestas en una entrega. (A) Acta sobre el pre-registro
DW.2 (to-glm/0464 en e218790, 2504 B / 58 l / NA=0). (B) Respuesta a
la consulta de accesos a los repos privados (to-glm/0465 en d749b0b,
3512 B / 69 l / NA=0). En (A) no hay codigo tocado, solo el documento;
en (B) no hay credencial creada, solo consulta. Ambas constancias
correctas.

## A. DW.2: pre-registro de higiene web

### A.1 Registro

- Rama dw.2-higiene-web, commit 393dc56
  (393dc56384958054e0c903a5f69064501fd062fd), 1 fichero +71/-0
  (docs/DW.2-PRERREGISTRO.md), sobre main web 0961a57.
- Constancia del cierre de DW.1: merge 0961a57, rama conservada en
  713fcf4, sin CI en el repo web (declarado; la conformidad 0451 se
  sustento en evidencia local + ferry 7/7, y asi queda entendido para
  todo el track web mientras no exista CI).
- Cambio previsto: vitest.config.ts nuevo con
  test.exclude = [...configDefaults.exclude, '.next/**'] y una linea
  dev-r34.pid en .gitignore. Fuera de alcance: package.json,
  next.config.ts, tsconfig.json, src/, dependencias, data/**,
  .github/**.

### A.2 Aritmetica de control

Acumulado esperado del merge DW.1 (f7771da -> 0961a57): 2 ficheros,
+71/-6 (pre-registro 69 + change 2 aniadidas; 0 + 6 borradas). Si un
relay futuro del arbol web diera otro numero, seria desviacion a
explicar. El +71/-0 del pre-registro DW.2 es coincidencia numerica
con ese acumulado; sin relacion.

### A.3 Fidelidad al acta 0451 seccion 3

Exacta en los dos extremos:

1. Exclusion de .next/** del escaneo de vitest como slice propio de
   configuracion con el gate de siempre: literalmente lo que la
   observacion 0451 seccion 3.2 disponia.
2. .gitignore para dev-r34.pid: la sugerencia no vinculante del 0450
   seccion 2.1, asumida como slice.

### A.4 Criterio binario: completo

Puntos fuertes verificados:

1. El orden build -> lint -> test SIN limpieza manual de .next/
   reproduce exactamente el escenario de la salvedad DW.1 y obliga al
   fix a trabajar en condiciones reales, no en un arbol barrido a
   mano.
2. El conteo 48 ficheros / 461 tests ancla la suite verdadera: los 7
   tests duplicados de la copia standalone no deben reaparecer.
3. La exigencia de cero suites bajo .next/ en la salida cierra
   empiricamente el riesgo de forma del glob (A.5.1).
4. El status final limpio mantiene la higiene del arbol: si el build
   toca next-env.d.ts, se restaura a la baseline antes del status
   (practica DW.1); y dev-r34.pid pasa a ignorado, desapareciendo del
   porcelain por efecto del propio .gitignore que este slice aniade.

### A.5 Precisiones no bloqueantes

1. Forma del glob: '.next/**' cubre el .next raiz; '**/.next/**'
   cubriria tambien apariciones anidadas. Eleccion de David; el cierre
   empirico del criterio (cero suites bajo .next con build ejecutado)
   hace la forma inmaterial para PASS.
2. vitest.config.ts nuevo: si existiese configuracion previa de test
   (bloque test en vite.config.ts u otra), vitest.config.ts tiene
   prioridad y la sustituira en silencio. La guarda es el conteo
   48/461: una config pisada moveria los numeros y daria FAIL. Pido
   una linea en el paquete de evidencia confirmando que no se pisa
   config previa de test (o declarando cual es).
3. Registro del head fusionado DW.1 (0961a57) en el hub, una linea
   (0451 seccion 4): no consta su confirmacion en este relay. Una
   linea en el paquete la cierra (o declarar que ya esta hecho).

### A.6 Disposicion

1. Acta EMITIDA sobre el pre-registro 393dc56
   (393dc56384958054e0c903a5f69064501fd062fd). La ejecucion procede
   con el GO de David.
2. Paquete minimo de evidencia: (1) diff de los dos ficheros de
   configuracion; (2) los tres logs en el orden del criterio; (3)
   conteo de suites demostrando ausencia de .next/; (4) git status
   final; (5) head del change con padre 393dc56 (sin commits ajenos);
   (6) las lineas de A.5.2 y A.5.3.
3. Con el paquete, conformidad breve; el merge es decision de David.
   Sin CI en el repo web, la conformidad se basa en evidencia local +
   ferry, como en DW.1.

## B. Consulta de accesos (to-glm/0465): bundles por head; ninguna credencial

### B.1 Decision

Opcion 4: paquetes offline por head exacto (git bundle), con el sha256
del bundle publicado en INTERCAMBIO en la misma entrega, y el relay
como registro permanente. Ninguna credencial: ni deploy key, ni PAT,
ni colaborador externo. En particular, no genero pares de claves para
deploy keys: el privado seria custodia de credencial de mi lado, y
declino esa custodia.

### B.2 Razones (declaradas con honestidad)

1. No existe canal seguro de entrega hacia mi. Mis unicos canales son
   este chat y mi entorno de ficheros; ambos son reposo en
   infraestructura compartida y reciclable. Un archivo cifrado cuya
   clave viaja por el mismo canal es ofuscacion, no seguridad. Un
   secreto entregado a mi seria un secreto en reposo que no puedo
   custodiar, rotar ni proteger de forma verificable.
2. Minimo privilegio real: un bundle no tiene scope que abusar, no
   requiere revocacion, es exacto por construccion al head que audito
   y caduca solo.
3. La garantia central de este protocolo nunca fue mi acceso vivo:
   fue la disciplina del pre-registro (criterios binarios, evidencia
   reproducible, ferry, GO de David). Cambiar la base probatoria a
   mitad del track no mejora esa garantia y si introduce una
   componente nueva y sin auditar: mi propia custodia de secretos.

### B.3 Uso declarado del bundle

1. Leer diffs y blobs en el head exacto: cerrar la brecha que declare
   en 0449 seccion 3 (verificar coincidencia contra el diff real, no
   contra el mapeo transcripto).
2. Verificar diffstats, conteos de lineas y estado del arbol.
3. Ejecutar yo mismo los greps de criterio sobre el arbol exacto:
   verificacion independiente, no lectura de logs ajenos.
4. No necesito: API de CI ni listado de PRs (siguen por relay,
   transcritos, como hasta ahora); reproducir builds o tests (la CI
   cubre build/test donde existe, y mi entorno no reproduce su stack
   con fidelidad que sume valor probatorio).

### B.4 Repos y cadencia

1. Mientras dure el track DW: bundle por head bajo auditoria de web y
   de C++. Delta desde el ultimo head que haya auditado
   (git bundle create <fichero> <prev>..<head>) para mantenerlo ligero;
   el repo C++ lleva textures y capturas que un bundle completo
   engordaria sin necesidad.
2. Hub Android: bundle solo cuando haya un PR docs bajo revision
   (habria sido util para el #61); en rutina, relay.
3. Entrega por el mecanismo de ficheros del proyecto (como llego el
   artefacto del repo C++ que conservo). Yo verifico sha256 contra lo
   publicado en INTERCAMBIO y git bundle verify antes de usar el
   paquete.

### B.5 Efecto en las actas

Cuando use un bundle, la seccion "Base de esta acta" pasara a declarar
"relay + bundle verificado (sha256 ..., head ...)". Sin efecto
retroactivo sobre 0437-0451. Y el limite, dicho claro: el bundle
reduce pero no elimina la confianza en el relay (el ancla sigue siendo
el GO de David y los hashes publicados); lo que elimina es mi
dependencia de la transcripcion de diffs y greps.

### B.6 Si algun dia hace falta acceso vivo

Se reconsulta, con David decidiendo. Mi recomendacion seguira siendo
no crear la credencial mientras el bundle cubra la necesidad; y si se
crea para otro proposito, que nunca se comparta conmigo por ningun
canal.

## C. Base de esta acta

Evidencia relayada (to-glm/0464, 0465 y cadena 0437-0451); sin acceso
directo a los repos Android, C++ o web. El artefacto del proyecto
(captura del repo C++) sigue siendo mi unico ground truth estructural.

-- GLM, 2026-11-22, lado auditor.
