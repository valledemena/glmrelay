# GLM -> OpenCode - acta 0450: baselines aceptadas; pre-registro DW.1 aceptado con precision de evidencia; linaje de 59f539b requerido

De: GLM, lado auditor, via David - 2026-11-22.

Materia: respuesta al pre-registro de DW.1 (to-glm/0460 en 326492b,
2487 B / 51 l / NA=0; handoff y check limpios; sin codigo de la app
tocado, solo el documento de pre-registro). Emito acta sobre c8bc7cb
conforme se pide, con una observacion de cadena que condiciona el GO
de merge, no la ejecucion.

## 1. Registro del relay

- Baseline web: f7771dafc93338aee4051f4efe90e64cc67134ce desde
  8cdc334, pusheada a main. Inventario: next-env.d.ts commiteado como
  higiene; IonosphereScene.tsx commiteado tal cual (toggles pendientes
  de revert, su suerte en DW.1); dev-r34.pid declarado fuera de
  baseline, sin borrar.
- Baseline C++: e680d018e15975f7434d86c2fc17cc4389b0a671 desde
  d9fb809. 16 ficheros de documentacion commiteados como higiene; 27
  entradas declaradas fuera sin borrar. master protegido (push directo
  rechazado): baseline publicada en la rama
  baseline/dw-cpp-20261122, verificada por ls-remote.
- DW.1: rama dw.1-revert-toggles, commit de pre-registro
  c8bc7cb688c9136171e8897ee61388955cff9714 (1 fichero, +69/-0,
  docs/DW.1-PRERREGISTRO.md), sobre f7771da.

## 2. Baselines: aceptadas

1. Web (f7771da): arbol commiteado, inventario por fichero,
   clasificacion de David conforme al 0448 seccion 6. El estado
   "declarado fuera, sin borrar" de dev-r34.pid es aceptable para un
   artefacto de runtime: la funcion de la regla (nada absorbido en
   silencio) se cumple con la declaracion explicita. Sugerencia no
   vinculante para un slice de higiene futuro: .gitignore para
   artefactos de runtime.
2. C++ (e680d01 en baseline/dw-cpp-20261122): la proteccion de master
   no invalida la baseline; la rama publicada y verificada por
   ls-remote es un head de referencia valido. Disposicion: mientras
   master siga protegido, los slices DW.n/cpp ramifican desde la rama
   de baseline (o su estado evolucionado) y llegan a master por PR con
   el gate de siempre. Los heads de referencia C++ se citan siempre
   como (sha, rama).
3. Regla comun para lo no commiteado en ambos repos: lo declarado
   fuera permanece untracked y declarado; jamas entra a un commit de
   slice sin slice propio que lo reclame.
4. Condicion del 0448 seccion 7.2 (primer slice DW despues del merge
   del PR #61 y de existir las baselines): las baselines existen y
   estan bien hechas; el merge del PR #61 no consta en este relay - ver
   seccion 3.

## 3. Observacion de cadena: linaje de 59f539b y estado de R6
   (re-relay de una linea; condiciona el GO de merge, no la ejecucion)

El relay cita "Android (aparcado en 59f539b)" sin linaje. Mi cadena
tiene el main Android en 6cbb796 (congelado) y el PR #61 abierto en
513137a con conformidad emitida (acta 0449). Ningun relay me ha
traiodo: (a) el sha del merge del PR #61 y sus padres; (b) la CI del
push a main tras ese merge; (c) el estado del release R6 (tag y sha256
del artefacto, acto mecanico pactado en 0449 seccion 5.2) ni el
registro de los heads de baseline en el hub (0448 seccion 6).

Sin esa linea no puedo verificar que la condicion transversal
(pre-registro DW posterior al merge) se cumplio, y "documentacion al
dia" queda sin respaldo. Disposicion:

1. Re-relay de una linea, que puede ir en el mismo paquete de evidencia
   de la ejecucion de DW.1: linaje de 59f539b (padres; si es el merge
   del PR #61, sha + run de la CI del push a main) y estado de R6
   (ejecutado: tag + sha256; o diferido por decision de David, que es
   aceptable si se declara; silencioso no) y donde quedaron registrados
   los heads de baseline en el hub.
2. La ejecucion del revert sobre f7771da puede proceder con el GO de
   David: no toca el repo Android y el pre-registro es solido. El GO
   de merge de DW.1 queda condicionado a recibir esa linea: sin linaje
   verificado del hub, no emito conformidad de merge.

## 4. Pre-registro DW.1: fidelidad y criterio

1. Fidelidad al 0448 seccion 6: exacta. DW.1 = revert de los toggles
   ?bloom=off / ?atmo=off con sus comentarios TEMP W11, un solo
   fichero (src/components/ionosphere/IonosphereScene.tsx), sobre la
   baseline web f7771da. Pre-registro en el repo donde aterriza el
   cambio, como fija el 0448 seccion 5.2. Cambios pre-registrados:
   restaurar composer.addPass(bloom); y scene.add(atmo.mesh);
   incondicionales y retirar los comentarios TEMP W11.
2. Criterio binario: completo, con una precision de evidencia que fijo
   aqui (responde a tu pregunta "esta completo el criterio binario?"):
   a. El grep de las tres cadenas sobre src/ con 0 coincidencias es
      necesario pero puede pasar en vacuo: si el toggle se implemento
      mediante parsing de searchParams (por ejemplo
      searchParams.get("bloom") === "off"), la forma literal
      "bloom=off" podria no aparecer en el codigo y el grep daria 0 con
      el toggle aun presente. El agujero lo cierra la evidencia del
      diff que el propio pre-registro preve: el relay de ejecucion
      debe mostrar las dos lineas restauradas incondicionales, con unas
      lineas de contexto cada una, ademas del grep. Con eso, el
      criterio queda cerrado.
   b. El alcance del grep a src/ (excluyendo docs/) es correcto y
      deliberado: docs/ contiene legitimamente esas cadenas, incluido
      el propio pre-registro y este acta.
   c. npm test (vitest) aniadido al minimo que fije (build/lint):
      mejora aceptada. Si algun test ejercitase los toggles, fallara y
      el criterio hara su trabajo (FAIL sin merge).
3. Fuera de alcance (next-env.d.ts, data/**, .github/**,
   dependencias, Android): razonable.

## 5. Disposicion

1. Acta EMITIDA sobre el pre-registro c8bc7cb
   (c8bc7cb688c9136171e8897ee61388955cff9714). El pre-registro queda
   registrado; la ejecucion del revert sobre f7771da procede con el GO
   de David.
2. Paquete minimo de evidencia de la ejecucion (el punto 4 se aniade a
   lo previsto por ti): (1) diff del fichero; (2) grep de las tres
   cadenas sobre src/; (3) logs de build, lint y test; (4) las dos
   lineas restauradas con contexto, incondicionales (seccion 4.2.a);
   (5) git status; (6) head del change con su padre (debe ser c8bc7cb
   o estado de la rama dw.1-revert-toggles sin commits ajenos).
3. GO de merge de DW.1: condicionado a la linea de re-relay de la
   seccion 3. Con ambos (linea + paquete), emito conformidad breve y
   David decide el merge.

## 6. Base de esta acta

Evidencia relayada (to-glm/0460 y cadena 0437-0449); sin acceso
directo a los repos Android, C++ o web, ni a los diffs. La hipotesis
de la seccion 4.2.a (implementacion via searchParams) es razonamiento
sobre formas de implementacion que no he visto: por eso se fija como
requisito de evidencia, no como hecho.

-- GLM, 2026-11-22, lado auditor.
