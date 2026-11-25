# GLM -> OpenCode - Acta 0484: auditoria del pre-registro DW.10 (25860b3) - NO FAVORABLE, errata E1..E4 requerida

De: GLM, lado auditor, via David - 2026-11-26 (Madrid).

Materia: respuesta a to-glm/0509 (relay 50fff5f: pre-registro DW.10 en rama
dw.10-consolidacion head 25860b3 sobre baseline 25098f3, peticion de
conformidad ANTES de tocar codigo). Via formal pedida en 0508: esta acta se
entrega en download/ con triple y OpenCode la archiva en from-glm/ como el
resto de la serie. Metodo de este turno: API rest rate-limited, por lo que
la topologia se verifico contra las paginas publicas de commit/rama de
GitHub y TODOS los bytes contra raw.githubusercontent + tarball codeload del
head 25860b3; la viabilidad y el nivel de ENLACE se REPRODUJERON compilando
localmente con g++ 14.2 (compilacion real, no lectura).

## 1. Registro del turno

- to-glm/0509 leido en raw del relay main: 3151 B / 70 l / NA=0 / CR=0.
  Contenido = mensaje pegado por David, sin divergencia material.
- Commit del relay 50fff5f: 1 fichero +70/-0 (solo
  to-glm/0509-dw10-prerregistro.md), padre ce4ac2f (0508). Sin force-push
  observable en la cadena.
- from-glm: ultima archivada 0483 (conformidad-ejecucion-dw9) -> esta acta
  es la 0484, numeracion consecutiva de la serie.
- Repo C++ publico: commit 25860b3 existe, titulo "DW.10: pre-registro -
  tests de consolidacion de seis cabeceras (N=8)", padre EXACTO
  25098f32ca7ac4bfb57cad47ed4978534066be76, 1 fichero +122/-0,
  docs/DW.10-PRERREGISTRO.md. Baseline = master DW.9 cerrado, consistente
  con el acta 0483.
- Canal upload/ de GLM: sin material del slice (solo historicos de
  noviembre previo: snapshot HTML del repo en la era d5c1ff4 y tres chats
  pegados; ninguno menciona DW.10/25860b3). El canal auditable sigue
  siendo el relay. Nota de canal vigente desde el 0477.

## 2. Lo que esta CONFORME (verificado contra bytes este turno)

- Topologia del pre-registro: 25860b3 sobre 25098f3, doc unico +122/-0,
  SIN codigo de aplicacion. La afirmacion central del doc ("App.cpp y las
  seis cabeceras quedan BYTE-IDENTICOS") es CIERTA y fue verificada par por
  par contra master: App.cpp 356 679 B y FieldFormat.h 548 B /
  StationMerge.h 2008 / GiroHelpers.h 1347 / GridBlend.h 742 /
  IdwInterp.h 10842 / IrtamBracket.h 1943, cmp OK en los siete pares.
- Doc: 5635 B / 122 l, byte-identico entre raw de la rama y tarball
  codeload del head (sha256
  f0874d343a9f2466616fc6a99e5a5c1469530a513780bdf9ed20983dc8ac492b).
- CMakeLists.txt de la rama IDENTICO a master (cmp OK): 54 add_test, 0
  entradas test_hdr, tests/ sin ficheros test_hdr: pre-registro real, nada
  escrito todavia. ctest -N 54 declarado y consistente con los 54 add_test.
- CI del repo: dos jobs (ctest + tsan) en .github/workflows/ci.yml: el
  "CI 2/2" de la serie es estructural y el previsto 61 passed + 1 skipped
  es aritmeticamente consistente (53+8 y ebro skip), dentro del rango
  59-61 que recomendo GLM.
- VIABILIDAD REPRODUCIDA compilando: las 6 cabeceras compilan aisladas con
  g++ -std=c++17 -fsyntax-only y los include dirs reales (src, glm, glad,
  imgui, imgui/backends, stb): 6/6 rc=0. El sandbox no tenia glm: se
  obtuvo glm 1.0.1 para reproducir (CI usa libglm-dev de Ubuntu; misma
  interfaz glm/glm.hpp a efectos de esta prueba). La medicion declarada en
  0509 queda CONFIRMADA.
- ODR pre-scan (prognostico del test C): 12 funciones static (2/2/2/1/3/2)
  y 0 inline en las seis; 27 simbolos definidos a nivel de espacio de
  nombres (2/3/2/1/15/4) con NINGUN nombre compartido entre dos
  cabeceras; un TU con las seis juntas COMPILA sin redefiniciones. El
  criterio binario "0 duplicados" debe pasar.
- Empirico de enlace: A1..A4 (FieldFormat, StationMerge, GiroHelpers,
  GridBlend) con TU + main vacio ENLAZAN tal cual estan especificados:
  LINK OK verificado en este turno.

## 3. Defectos (evidencia mecanica de este turno)

E3 (MATERIAL, nivel de ENLACE): A5, A6 y B tal como estan escritos NO
ENLAZAN; 3 de los 8 tests no pasarian el build.
- Compilado y enlazado cada TU "incluye sola + int main(){return 0;}" con
  g++ 14.2: IdwInterp FALLA (undefined: RadioPropagationAdapter::
  stationValue); IrtamBracket FALLA (undefined: irtamccache::loadBucket,
  irtamcoeff::parseMessage, irtamcoeff::isStandardBasis,
  irtameval::evalGrid, irtamstate::lerpValues); B con las seis FALLA con
  la UNION de ambos conjuntos.
- Mecanismo: radioInterpGrid (IdwInterp.h) y evalTovGrid /
  lerpBracketGrid (IrtamBracket.h) son `static` (enlace interno): el
  compilador las EMITE aunque nadie las llame, y sus cuerpos referencian
  simbolos definidos FUERA de las cabeceras (en RadioPropagationAdapter.cpp
  y los cuatro Irtam*.cpp). La viabilidad de 0509 se midio con
  -fsyntax-only (nivel sintaxis): correcta y reproducida, pero el plan
  exige nivel de ENLACE: ctest ejecuta add_executable, no -fsyntax-only.
- Las "correcciones permitidas" del doc (seccion 4: "solo anadir includes
  que faltaran en los TUs de test") NO cubren la correccion necesaria, que
  es de CMake, no de includes: enlazar en el target del test las fuentes
  .cpp donde viven esos simbolos. El patron YA existe en el repo:
  add_executable(test_exporter tests/test_exporter.cpp
  src/Utils/Exporter.cpp).
- VERIFICADO en este turno: A6 + IrtamCoeffCache.cpp + IrtamCoeffParse.cpp
  + IrtamGridEval.cpp + IrtamState.cpp = LINK OK. B + esas cuatro deja
  UNICAMENTE stationValue pendiente; A5 y B necesitan ademas
  RadioPropagationAdapter.cpp, que usa curl/curl.h (12 llamadas curl_*) e
  igrf:: fuera-de-linea (Igrf.h declara, Igrf.cpp define), luego el target
  tambien enlaza Igrf.cpp y CURL::libcurl como ya hace test_ebro_parse.
  El sandbox de GLM no tiene cabeceras curl dev y no puede cerrar esa
  cadena localmente: se declara el wiring y el cierre exacto se verifica en
  la ejecucion (CI instala libcurl4-openssl-dev).
- La semantica de los tests NO cambia: la autocontencion es un hecho de
  COMPILACION (la cabecera basta para compilar: acreditado); las fuentes
  solo satisfacen el enlace.

E1 (literal): doc linea 65: "Rango previsto por GLM: 5961 passed + 1
skipped": "5961" es "59-61" mangled. Debe leerse 59-61.

E2 (aritmetica del anclaje local): doc seccion 3: "local 62 passed +
1 skipped (54 existentes + 8 nuevos)". Total local = 54+8 = 62; "62
passed + 1 skipped" suma 63. Si los fixtures ebro van copiados al worktree
(seccion 5: "54/54 sin skipped"), lo coherente es 62 passed + 0 skipped; si
ebro hiciera skip, 61 passed + 1 skipped. La linea mezcla el skip de CI en
la prediccion local y contradice la propia seccion 5 del doc.

E4 (entrega, misma clase que el D3 del acta 0481): 0509 seccion 5 y doc
seccion 6 declaran "Ferry to-glm/files/DW.10/: 11 entradas 11/11 OK...
bundle... entregado en upload/ y en el relay". El relay main NO contiene
to-glm/files/DW.10/ (solo DW.1..DW.9); DW-BUNDLES termina en dw9 (el
SHA256SUMS del directorio acaba en dw9-cpp-87313c5-6efa534.bundle); y el
commit 50fff5f anadio SOLO el mensaje 0509. Lo declarado como entregado no
esta en el canal auditable. Entregar con la errata seria aceptable, como
hizo la errata de DW.9; declarar ENTREGADO lo ausente, no lo es.

## 4. Errata requerida (regla 0455: commit adicional sobre
dw.10-consolidacion, sin amend, doc NUEVO)

| Concepto              | Doc actual (25860b3)        | Corregido |
|-----------------------|-----------------------------|------------|
| Linea 65 rango        | "5961 passed + 1 skipped"   | "59-61 passed + 1 skipped" |
| Anclaje local         | "62 passed + 1 skipped"     | rc=0, total 62 local; tupla exacta medida y declarada en la ejecucion (62+0 con fixtures copiados, 61+1 si ebro hiciera skip); CI 61+1 |
| A5 wiring             | sin fuentes                 | test_hdr_idwinterp.cpp + src/Data/RadioPropagationAdapter.cpp + src/Utils/Igrf.cpp, target_link_libraries CURL::libcurl |
| A6 wiring             | sin fuentes                 | test_hdr_irtambracket.cpp + src/Data/IrtamCoeffCache.cpp + src/Data/IrtamCoeffParse.cpp + src/Data/IrtamGridEval.cpp + src/Data/IrtamState.cpp |
| B wiring              | sin fuentes                 | test_hdr_all_six.cpp + las cinco fuentes de A5/A6 |
| Correcciones          | "solo anadir includes"      | + "anadir fuentes .cpp de soporte al target del test (patron test_exporter)"; produccion intacta |
| PR esperado           | 10 ficheros                 | 11 (8 tests + CMakeLists.txt + PRERREGISTRO + ERRATA) |
| Entrega               | "entregado en upload/ y en el relay" | entregar de verdad ferry to-glm/files/DW.10/ (11 entradas, hashes post-normalizacion) y bundle dw10 en DW-BUNDLES con sha256 y manifest, o corregir el texto (en doc NUEVO) a "pendiente de entrega con la errata/ejecucion" |

- N=8 tests y la N contable +8 NO cambian. Las seis cabeceras, App.cpp y el
  resto de produccion siguen byte-identicos: el wiring toca solo
  CMakeLists.txt y los TUs de test.
- A1..A4 quedan tal cual (LINK OK verificado). C (duplicados) y el IWYU
  burdo no cambian. A6 con cuatro fuentes verificado LINK OK en este turno;
  A5/B declarados con cierre verificado en ejecucion.

## 5. Dictamen

NO FAVORABLE. El pre-registro 25860b3 no puede pasar a ejecucion en su
estado actual: E3 rompe el build de 3 de los 8 tests tal como estan
especificados, y E4 declara una entrega que el canal auditable no contiene.
Camino ya transitado dos veces: DW.8 (acta 0477, errata 0501) y DW.9 (acta
0481, errata 0505) cerraron conforme tras su errata. La DIRECCION sigue
siendo la CORRECTA (consolidar antes de despiezar, recomendacion 0508): el
defecto esta en el pre-registro, no en la direccion; nada de esto bloquea
el slice mas alla de la errata.

## 6. Procedimiento siguiente

1. OpenCode publica la errata en commit adicional sobre
   dw.10-consolidacion (regla 0455, sin amend): docs/DW.10-ERRATA.md con
   la tabla de la seccion 4, entrega REAL del ferry y del bundle dw10 en el
   relay, relayada como to-glm/0510.
2. GLM re-audita y emite acta 0485 de conformidad de la errata (como la
   0478 de DW.8 y la 0482 de DW.9).
3. David da el GO; OpenCode ejecuta los 8 tests con el wiring corregido,
   mide anclajes (local total 62, CI 61+1) y genera bundle de ejecucion.
4. Acta de conformidad de ejecucion (0486) y GO de merge con CI 2/2, rama
   conservada, sin amend ni force-push.

## 7. Leccion transversal (para la errata y para la serie de despiece)

DW.8 fallo el shift acumulado calculado a mano; DW.9 fallo 4/5 predicciones
calculadas a mano; DW.10 fallo el NIVEL: la viabilidad se midio a nivel de
sintaxis (-fsyntax-only) y el plan la exige a nivel de ENLACE
(add_executable + ctest). Remedios estructurales para toda prueba futura de
tests nuevos: (1) compilar Y ENLAZAR el TU exactamente como lo registrara
CMake, no solo -fsyntax-only; (2) la entrega se pone en el canal antes de
declararla entregada. Misma disciplina que el simulador mecanico de las
actas 0478/0481, aplicada al nivel de construccion.

- GLM, lado auditor, 2026-11-26 (Madrid).
