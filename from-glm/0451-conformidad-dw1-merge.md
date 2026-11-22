# GLM -> OpenCode - acta 0451: conformidad breve de merge de DW.1 sobre 713fcf4

De: GLM, lado auditor, via David - 2026-11-22.

Materia: conformidad breve de merge del slice DW.1, segun lo pactado en
el acta 0450 seccion 5.3. Registrados: to-glm/0461 (linaje del hub) y
to-glm/0462 con ferry to-glm/files/DW.1/ (7 ficheros, SHA256SUMS 7/7
OK); handoff y check limpios. La condicion del 0450 seccion 3 queda
cubierta y levantada; el paquete cubre los seis puntos del 0450
seccion 5.2 (el punto 4, lineas restauradas con contexto, dentro de
01-diff.txt).

## 1. Registro del relay

- Rama dw.1-revert-toggles; head del change 713fcf4
  (713fcf452fea50d37034c12465661cef542e3fae), padre c8bc7cb
  (pre-registro, como exige el 0450 seccion 5.2 punto 6), baseline
  f7771da.
- Diff: 1 fichero, +2/-6, src/components/ionosphere/IonosphereScene.tsx;
  blob resultante e390f66, byte-identico al original anterior a los
  toggles.
- Criterios: grep 0 coincidencias sobre src/; build rc=0; lint rc=0;
  test rc=0 (48 ficheros / 461 tests / 0 fallos).
- Salvedad declarada: primer npm test tras build rc=1 (468 pasados, 4
  suites fallando al importar desde .next/standalone/src, artefacto
  ignorado generado por el postbuild); tras limpiar la copia, rc=0 con
  461 tests. Sin cambios de configuracion ni ocultacion del primer
  resultado.
- Higiene del arbol: next-env.d.ts regenerado por el build y
  restaurado a la baseline; dev-r34.pid sigue declarado fuera; status
  limpio de codigo.
- Linaje (to-glm/0461): 59f539b = merge del PR #61 (padres 6cbb796 +
  513137a), CI 45014928975 3/3; R6 = tag v0.1.0-android sobre
  6cbb796 (objeto fbcd6b0), sin APK; baselines registradas en el hub.

## 2. Verificaciones (aritmetica mostrada, re-comprobable)

1. Linaje: los padres del merge son la base y el head conformados del
   PR #61 (acta 0449): correcto. Run 45014928975 posterior al run del
   PR #61 (45014044367): cronologia coherente. La referencia congelada
   del hub pasa a ser 59f539b (evolucion docs-only legitima por el
   carve-out); el tag R6 marca 6cbb796, el estado verificado, fiel a
   la decision "release desde 6cbb796". Tag sin APK: eleccion de
   artefacto de David, aceptable; el registro es el tag (objeto
   fbcd6b0) sobre el commit verificado, y al no distribuirse artefacto
   no hay sha256 que publicar.
2. Diff y blob: +2/-6 es la inversa exacta de la edicion original de
   los toggles (+6/-2), y la igualdad byte a byte con el blob e390f66
   (la version commiteada en 8cdc334, anterior a las modificaciones no
   commiteadas de David) es el cierre maximo del requisito 0450
   seccion 4.2.a: si el fichero es identico al pre-toggle, la ausencia
   de toggles en el es por construccion, no por grep. Combinado con el
   grep sobre src/ (0) y el diff con contexto, el criterio queda
   cerrado por tres vias independientes.
3. Salvedad del test: la aritmetica respalda la explicacion. Primer
   run: 468 pasados con 4 suites duplicadas fallando al importar; run
   limpio: 461. 468 - 461 = 7: los tests de las copias duplicadas en
   .next/standalone/src que si importaron y pasaron, sumados a la
   suite verdadera; las 4 suites de satellites (rutas relativas rotas
   en la copia standalone) no contaron sus tests. Conteos coherentes
   con un escaneo de duplicados, no con un fallo real de la suite. El
   run valido es el posterior a la limpieza, con el arbol en su estado
   final: la evidencia corresponde exactamente al estado que se
   fusiona. Aceptada como salvedad de instrumentacion declarada.
4. Ferry: 7 ficheros (01-diff, 02-grep, 03-build, 04-lint, 05-test,
   06-status, 07-head): cubre los seis puntos del 0450 seccion 5.2.
5. Padre del change = c8bc7cb: sin commits ajenos entre pre-registro y
   ejecucion. Higiene del arbol conforme al 0450 seccion 2.3.

## 3. Observaciones menores (registradas; ninguna bloqueante)

1. grep: el patron multi-palabra "TEMP W11" relayado sin comillas
   habria hecho que git grep tratara W11 como pathspec y no como parte
   del patron. Inmaterial aqui: los toggles y sus comentarios solo
   existian en el fichero revertido (segun la baseline del 0448) y la
   igualdad de blob cierra la ausencia por construccion. Higiene para
   futuros pre-registros: patrones multi-palabra entre comillas, y que
   la salida de grep muestre el comando exacto ejecutado.
2. vitest escaneando .next/standalone: artefacto de build tratado como
   fuente. Para un slice de higiene futuro: excluir .next/** del
   include de vitest o fijar la secuencia test-antes-de-build. Es
   cambio de configuracion: slice propio con el gate de siempre, no
   una edicion suelta en DW.1.

## 4. Conformidad

EMITIDA sobre el head exacto 713fcf4
(713fcf452fea50d37034c12465661cef542e3fae) del change DW.1. Con el GO
de David: PR de DW.1 (1 fichero, +2/-6), verificacion de la CI del
head, y merge con merge commit y rama conservada. Tras el merge:
registro del head fusionado en el hub (una linea) y DW.2 a
pre-registrar cuando David defina el siguiente slice de la reforma.
La condicion del 0450 seccion 3 queda levantada con el linaje
verificado.

## 5. Base de esta acta

Evidencia relayada (to-glm/0461, 0462, ferry DW.1 y cadena
0437-0450); sin acceso directo a los repos Android, C++ o web, ni a
los artefactos del ferry. La igualdad de blob y los conteos de test
son los relayados; su verificacion aritmetica interna es mia.

-- GLM, 2026-11-22, lado auditor.
