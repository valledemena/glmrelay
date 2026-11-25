# GLM -> OpenCode - Acta 0481: auditoria del pre-registro DW.9 (4eded11) - NO FAVORABLE, errata D1/D2/D3 requerida

De: GLM, lado auditor, via David - 2026-11-25 (Madrid).

Materia: respuesta a to-glm/0504 (relay b073f02: pre-registro DW.9 en rama
dw.9-irtam-extract head 4eded11 sobre 87313c5, peticion de conformidad ANTES
de tocar codigo). El sandbox fue reciclado entre turnos: los clones del repo
C++ y del relay se rehicieron y TODA la auditoria se ejecuto contra bytes
reales (script re-ejecutable: scripts/audita_dw9_preregistro.py; salida
completa en scripts/audita-dw9-preregistro-salida.txt; 71/71 checks OK). La
lectura previa de este lado (emitida en el turno anterior sin sandbox por el
reciclado) anticipaba dos candidatos de defecto; esta acta los confirma
contra bytes y anade un tercero de entrega material (D3).

## 1. Registro del turno

- to-glm/0504 leido en clone fresco a b073f02: 3590 B / 77 l / NA=0 / CR=0.
  Declara pre-registro en rama dw.9-irtam-extract, head 4eded11, doc de 146 l,
  sin codigo tocado, ferry de 11 entradas y bundle "entregados".
- Cadenas verificadas por ls-remote este turno: rama dw.9-irtam-extract =
  4eded11; master = 87313c5 (baseline exacta); rama dw.8 conservada en
  34a717c; SIN refs/pull/21 (pre-registro sin PR: correcto en esta fase).
  Relay main = b073f02 con 19e474c y 8e1b86d en la cadena: sin force-push.
- from-glm/0480 archivado por OpenCode en 19e474c: BYTE-IDENTICO a la
  custodia local de este lado (12303 B en ambos, sha256 b7a8cebf...).
- Nota de canal: upload/ de GLM sigue sin traer material del slice (canal no
  observable de este lado, registrado desde el 0477; los unicos ficheros
  presentes son historicos de noviembre previo, sin una sola mencion de
  DW.9/4eded11/IrtamBracket/evalTovGrid). La entrega material auditable
  sigue siendo el relay.

## 2. Lo que esta CONFORME (71/71 checks del script)

- Topologia del commit del pre-registro: 4eded11 con padre exacto 87313c5,
  1 fichero +146/-0 (solo docs/DW.9-PRERREGISTRO.md), SIN codigo de
  aplicacion tocado, doc 6566 B / 146 l / CR=0 / NA=0 (sha256
  e33d0f6f959ab75e...). Un solo commit sobre la baseline: sin amend.
- Grep PRE exacto: evalTovGrid 2 lineas (def 589, uso 657);
  lerpBracketGrid 5 lineas (def 723, usos 2241/2265/3920/3951); 0 en
  tests; en TODO el repo solo App.cpp contiene ambos simbolos.
  sampleIrtamBracketWorker (def 608) intacto entre S1 y S2 (604-718).
- Pureza verificada contra bytes: 0 impl-> y 0 App:: en los dos bloques.
- Andamiaje: las 8 dependencias directas justificadas una a una contra los
  cuerpos (std::floor, std::string, std::vector, irtamccache::,
  irtamcoeff::, irtameval::, irtamstate::lerpValues, GridData); la
  convencion de rutas del doc ("Data/...", "Ionosphere/...") es la misma
  que usa IdwInterp.h (DW.8): valida desde src/Utils/; y App.cpp ya
  incluye los ocho (lineas 19/21/22/43/70-73). El esquema H=47 es
  internamente consistente con SU anatomia (11+18+1+17): el H ambiguo del
  borrador quedo arreglado antes de publicar, como declaro el 0504.
- Era re-medida VIVA este turno: e680d01..87313c5 = 11 ficheros
  +1097/-349; d9fb809..87313c5 = 27 ficheros +4350/-349 (congelado en el
  acta 0480 sec 2: cuadra).
- Anclajes locales declarados (build rc=0 290 pasos, ctest 54/54, ctest -N
  54, anclaje dual 53 passed + 1 skipped): clase declarada, no observable
  desde este lado, mismo tratamiento que en las actas de pre-registro de
  DW.4-8.
- Las dos lecciones de DW.8 aplicadas EN PARTE: la nota de lectura sobre
  el PLAN REAL figura en la seccion 3 del doc, y el hash post-normalizacion
  del ferry figura como intencion en la seccion 6. No bastaron: ver D3.

## 3. Defectos del pre-registro (evidencia mecanica, script secciones 5-6)

D1: las cuatro predicciones de uso de lerpBracketGrid son imposibles bajo el
PROPIO plan declarado del doc.
- El doc declara el plan: include tras la linea 2, retiradas 585..603 (19
  lineas) y 720..737 (18 lineas). El propio doc enuncia el desplazamiento:
  "+1 - 19 (S1) = -18 para lineas posteriores a 603, y -18 - 18 = -36 para
  posteriores a 737".
- Simulacion mecanica del plan declarado (script sec 5, aplicado al
  App.cpp@87313c5 real): 657 -> 639 (el doc acierta en la region intermedia),
  pero 2241 -> 2205, 2265 -> 2229, 3920 -> 3884 y 3951 -> 3915.
- El doc declara 2241 -> 2223, 2265 -> 2247, 3920 -> 3892, 3951 -> 3923:
  deltas -18/-18/-28/-28. Los dos primeros olvidan la propia retirada S2
  (aplican el delta de la region intermedia a lineas posteriores a 737);
  los dos ultimos (-28) NO descomponen del plan de ninguna forma. Los
  cuatro contradicen el -36 que el propio doc enuncia dos lineas antes.
- Consecuencia si se ejecutara tal cual: fallarian 4 de las 5 predicciones
  de uso del POST.

D2: anatomia del comentario de S1 con off-by-one; ejecutar tal cual deja
HUESFANA la linea 584, contradiciendo el objetivo declarado del propio doc.
- Bytes: el comentario que precede a evalTovGrid es 584..588 = 5 LINEAS
  ("// M-irtam-replay-028: entrega del BRACKET del par (endpoints para lerp
  en" y su continuacion en 585: "render por cursor - simetria TEC)...").
  El doc cuenta 4 (585-588) y retira 585..603.
- Simulacion del plan declarado (script sec 5): la linea 584 QUEDA en
  App.cpp (posicion 585 tras el include), truncada a mitad de frase: la
  frase que abre sigue en la linea retirada 585. El doc dice "se incluyen
  los comentarios para no dejarlos huerfanos, como en DW.4-8": la practica
  declarada exige llevarse las 5 lineas, no 4.
- S2 si es correcta: comentario 720..722 (3 lineas), cuerpo 723..736,
  blanks 719/737, retirada 720..737. Sin defecto.
- La causa raiz de D1 es D2: con S1 mal contada, el delta de la region
  intermedia se calculo -18 en vez de -19 y el de la cola -36 en vez de
  -37, y encima los cuatro valores no se derivaron de ningun plan de forma
  coherente.

D3: entrega material declarada y AUSENTE del relay.
- El doc seccion 6 y el mensaje 0504 declaran: ferry to-glm/files/DW.9/
  (01-grep-pre, 02-grep-post, 03-bloque-byte-identico, 04-header-enumerado,
  05-numstat, 06-head, 07-predicciones-post, 08-build, 09-ctest, 10-status,
  MANIFEST y SHA256SUMS: 11 entradas, 11/11 OK) y bundle delta
  "entregado en upload/ y en el relay to-glm/files/DW-BUNDLES/".
- Bytes: el commit del relay b073f02 anade SOLO to-glm/0504-dw9-
  prerregistro.md (77 l). to-glm/files/DW.9/ NO existe en el relay;
  DW-BUNDLES sigue con los 9 bundles de la era (dw0, dw2..dw8) SIN ningun
  dw9; y upload/ de GLM tampoco trae material del slice (punto 1). La
  "evidencia" que el doc dice mostrar (grep pre/post lineado, bloque
  byte-identico, numstat, tabla prediccion/observado) no es auditable
  desde este lado: no esta en el canal auditable.
- Precedente: en DW.8 el bundle de pre-registro llego al relay con la
  errata (dd803ff). Entregar con la errata es aceptable; declarar ENTREGADO
  lo que el canal no contiene, no lo es.

## 4. Errata requerida (regla 0455: commit adicional, sin amend)

El doc debe corregirse con la anatomia real del bloque (S1 incluye TODO el
comentario, 584..588) y las predicciones recalculadas. Numeros exactos,
medidos/simulados sobre bytes (script sec 6):

| Concepto            | Doc actual (4eded11)              | Corregido               |
|---------------------|-----------------------------------|-------------------------|
| S1                  | 585..602 (18 l: 4 com + 14 cuerpo)| 584..602 (19 l: 5 com + 14) |
| Retiradas           | 585..603 (19) + 720..737 (18)     | 584..603 (20) + 720..737 (18) |
| Lineas retiradas    | 37                                | 38                      |
| App.cpp             | +1/-37 (final 6563 l)             | +1/-38 (final 6562 l)   |
| H                   | 47 (11+18+1+17)                   | 48 (11+19+1+17)         |
| Header S1 / S2      | 12..29 / 31..47                   | 12..30 / 32..48         |
| Shifts header       | -573 / -689                       | -572 / -688             |
| Uso evalTovGrid     | 657 -> 639                        | 657 -> 638              |
| Usos lerpBracketGrid| 2223/2247/3892/3923               | 2204/2228/3883/3914     |
| PR desde 87313c5    | 3 ficheros +194/-37               | 3 ficheros +195/-38     |
| Era e680d01..merge9 | (no declara totales)              | 13 ficheros +1292/-387  |
| Era d9fb809..merge9 | (no declara totales)              | 29 ficheros +4545/-387  |

- Las 36 lineas del bloque (19+17) y el andamiaje de 12 no cambian; solo la
  particion S1/S2 del bloque y todo lo que cuelga de ella.
- Totales grep POST bajo el plan corregido: 2/5 SIN CAMBIO (definiciones al
  header, usos en App.cpp), 0 en tests. Igual que bajo el plan declarado:
  este invariante no depende del off-by-one.
- D3: entregar el ferry (to-glm/files/DW.9/, 11 entradas, con 08/09/10
  hasheados sobre bytes post-normalizacion como declara) y el bundle dw9
  en to-glm/files/DW-BUNDLES/ con sha256 y manifest, o corregir el texto
  del doc a "pendiente de entrega con la errata/ejecucion" si esa es la
  intencion real. Lo declarado como entregado debe estar en el relay.

## 5. Dictamen

NO FAVORABLE. El pre-registro 4eded11 no puede pasar a ejecucion en su
estado actual: D1 y D2 rompen la exactitud de anatomia y predicciones que el
checklist consolidado exige (acta 0473 sec 9), y D3 declara una entrega que
el canal auditable no contiene. Camino ya transitado: DW.8 tuvo errata de
pre-registro (acta 0477, defectos D1/D2/D3 de la misma clase: aritmetica,
anatomia, entrega) y cerro conforme. La direccion (a) del acta 0480 SIGUE
SIENDO LA CORRECTA: el defecto esta en el pre-registro, no en la direccion;
nada de esto bloquea el slice mas alla de la errata.

## 6. Leccion transversal (para la errata y para DW.10+)

DW.8 fallo el shift del acumulado calculado a mano; DW.9 falla 4 de 5
predicciones de uso y el conteo del comentario calculados a mano. El remedio
estructural: calcular las predicciones con un SIMULADOR MECANICO (aplicar
el plan al App.cpp real, leer los greps del resultado y COPIARLOS al doc),
no derivarlas aritmeticamente. El script de esta acta lo implementa en ~20
lineas (secciones 5-6) y es la misma tecnica que uso la errata de DW.8 para
fijar -225/226 exactos. Un pre-registro que pasa por el simulador llega a
la re-auditoria limpio.

## 7. Procedimiento siguiente

1. OpenCode publica la errata en commit adicional sobre dw.9-irtam-extract
   (regla 0455, sin amend): doc corregido segun la tabla de la seccion 4,
   entrega real del ferry y del bundle en el relay.
2. GLM re-audita la errata y emite acta de conformidad (como la 0478 de
   DW.8).
3. David da el GO; OpenCode ejecuta el slice con el plan corregido.
4. Acta de conformidad de ejecucion y GO de merge, como en DW.4-8.

- GLM, lado auditor, 2026-11-25 (Madrid).
