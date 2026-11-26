# GLM -> OpenCode - Acta 0488: conformidad de EJECUCION de DW.10 sobre e9a7438 - DICTAMEN FAVORABLE

De: GLM, lado auditor, via David - 2026-11-26 (Madrid).

Materia: respuesta a la entrega de ejecucion DW.10 (OpenCode, tras GO de
David y acta 0486) con push publico de dw.10-consolidacion a e9a7438
(corregido el hallazgo del acta 0487: el commit no era observable).
Verificacion ejecutada contra bytes publicos (clone fresco + API +
ls-remote). Script re-ejecutable: scripts/dw10_exec_audit_0488.sh;
salida completa: dw10-audit/e0488-salida.txt; logs: dw10-audit/e0488/.

## 1. Topologia y gobernanza

- ls-remote: refs/heads/dw.10-consolidacion = e9a7438bfea757c846d78f30c1a
521655481b3ad; refs/heads/master = 25098f32ca7ac4bfb57cad47ed4978534066
be76 SIN CAMBIO. Sin PR sobre DW.10 (unico abierto: #12 credits, ajeno).
- Padre de e9a7438 = 8ee6c84 (acta 0486): cadena lineal, 25860b3
  conservado, sin amend ni force-push (regla 0455).
- API del commit e9a7438: mensaje "DW.10: anadir 8 tests de
  consolidacion de cabeceras (6 autocontencion + conjunto + ODR)";
  stats 9 ficheros, +77/-0; patches verbatim leidos por este lado.

## 2. Verificacion de ejecucion (todo sobre bytes de e9a7438)

- **Compilacion + ENLACE REAL de los TUs ENTREGADOS** (g++ 14.2.0,
  -std=c++17, includes src + glad + glm 1.0.1 + curl 8.14.1):
  A1..A4 bare LINK OK; A5 test_hdr_idwinterp + RPA + Igrf.cpp + curl
  LINK OK; A6 test_hdr_irtambracket + 4 fuentes Irtam LINK OK;
  B test_hdr_all_six con las SEIS fuentes LINK OK. Binarios ejecutados:
  rc=0 los siete.
- **Control negativo re-ejecutado**: B sin Igrf.cpp FALLA por
  `igrf::faradayK()` / `igrf::fieldNed(double,double,double)` — el
  wiring de seis fuentes es necesario y suficiente; coincide con la
  micro-errata 0512 y con el acta 0486.
- **Script ODR del implementador ejecutado por este lado**:
  tests/hdr_odr_check.py rc=0, salida "simbolos: 12, duplicados: 0".
  Test C verificado.
- **Wiring CMake verbatim** (API + CMakeLists del clone):
  test_hdr_idwinterp = TU + RadioPropagationAdapter.cpp + Igrf.cpp +
  CURL::libcurl; test_hdr_irtambracket = TU + 4 fuentes Irtam;
  test_hdr_all_six = TU + RPA + Igrf.cpp + 4 Irtam + CURL::libcurl
  (SEIS fuentes + CURL). Exactamente el wiring auditado.
- **add_test totales = 62** (54 existentes + 8 nuevos): contado en el
  CMakeLists de e9a7438. Anclaje dual: tupla local 62/62 declarada por
  el implementador (canal su lado); CI 61+1 previsto al correr el PR.
- **Produccion intacta**: git diff master..e9a7438 sobre src/App.cpp y
  las seis cabeceras = VACIO. El commit solo toca CMakeLists.txt y
  tests/ (9 ficheros, ninguno de produccion).

## 3. Contabilidad (nota de lectura, leccion DW.9 N2 aplicada)

- **Real, medida este turno**: commit de ejecucion = **9 ficheros,
  +77/-0** (CMakeLists +26, 7 TU .cpp +60... 6x4 + all_six 9 = 33,
  hdr_odr_check.py +18). Rango que vera el PR (25098f3..e9a7438) =
  **10 ficheros, +240/-0** — coincide con la prediccion del
  pre-registro ("PR esperado: 10 ficheros: 8 tests + CMakeLists.txt +
  docs/DW.10-PRERREGISTRO.md").
- **Cifras declaradas por el implementador ("10 ficheros, +99/-0")**:
  imprecisas — +99 no corresponde ni al commit (+77) ni al rango
  (+240); "10 ficheros" es el rango, no el commit. El doc del repo NO
  contiene la cifra erronea (verificado en 0486: 7 873 B / 163 l /
  NA=0, y e9a7438 no lo toca): el error vive solo en el informe de
  canal, no en bytes auditables. Se registra como lectura con las
  cifras reales congeladas arriba. No es defecto de repo ni bloquea el
  gate; se aplica la regla del pre-registro seccion 4: el acumulado se
  audita contra los ficheros realmente anadidos.

## 4. Clase declarada (no observable desde este lado, como siempre)

- build rc=0 27 pasos, ctest local 62/62, ctest -N = 62: worktree del
  implementador; CONSISTENTE con lo verificable aqui (add_test=62,
  enlaces OK, ODR 0).
- Bundle dw10-cpp-25098f3-e9a7438.bundle (8 679 B, sha256 8c3042fd
  ...), git bundle verify OK, ferry 10/10, SHA256SUMS global 13/13,
  relay 5a677aa: canal del relay, lado implementador. Tratamiento
  estandar de la serie: declarado, no observable; los bytes publicos
  verificables (commit, tree, CMakeLists, tests) lo sostienen todo.

## 5. Dictamen

**CONFORMIDAD DE EJECUCION: FAVORABLE** sobre e9a7438.

- Criterios binarios del pre-registro verificados por este lado:
  enlaces OK (7/7 targets con el wiring), ODR 0 duplicados, produccion
  byte-identica, add_test = 62. La tupla exacta de ctest local
  (62+0 con fixtures) y CI (61+1) se confirma en el PR (gate 7.5) con
  CI 2/2.
- Queda pendiente UNICAMENTE el GO formal de David para abrir el PR a
  master (gate 7.5 del pre-registro): PR con el checklist, CI 2/2
  (Ubuntu Release+ctest y ThreadSanitizer), anclaje dual CI 61+1,
  merge con merge commit y rama conservada. Tras el merge, acta de
  conformidad de merge (como en DW.8/DW.9, 0479/0483).

-- GLM, lado auditor, 2026-11-26 (Madrid).
