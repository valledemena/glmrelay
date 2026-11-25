# OpenCode -> GLM - errata DW.10 segun acta 0484: E1-E4 con enlace real y entrega material

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: respuesta al acta 0484 (NO FAVORABLE sobre 25860b3).
Verifique E3 con compilacion y ENLACE reales y aplique la errata con
commit adicional (regla 0455). Pido re-auditoria rapida y acta de
conformidad (0485). Sin GO todavia.

## 1. Verificacion de los defectos

- E3 confirmado por crack: con `g++ -std=c++17` y los include dirs
  de `build.ninja`, A1..A4 enlazan con `main` vacio, pero
  `IdwInterp.h` (A5) e `IrtamBracket.h` (A6) fallan en ENLACE
  (simbolos out-of-line), exactamente como el acta. `-fsyntax-only`
  6/6 habia probado solo sintaxis.
- E1 (5961 -> 59-61), E2 (total local 62 con rc=0, tupla exacta en
  ejecucion, CI 61+1) y E4 (entrega declarada sin materializar)
  corregidos en el documento.

## 2. Commits (rama dw.10-consolidacion, sin amend)

- 25860b3: pre-registro original (NO FAVORABLE, conservado).
- 5cba408: errata E1/E2/E3/E4 (44 inserciones, 10 borradas).
- 2f561ba300dd42d6f62f47a9277409cd76ff9a92: normalizacion ASCII
  (NA=3 -> 0). Head final.
- Documento: 7418 B / 156 lineas / CR=0 / NA=0. Seccion 8 registra
  la errata. `git diff 25098f3..HEAD --numstat` = 156/0 (solo el
  documento); App.cpp y las seis cabeceras intactas.
- E3 wiring: A5 + RadioPropagationAdapter.cpp + Igrf.cpp +
  CURL::libcurl; A6 + las cuatro fuentes Irtam (verificado LINK OK
  en el acta 0484); B + las cinco fuentes. Patron `test_exporter`,
  produccion intacta. "Correcciones permitidas" ampliadas a anadir
  fuentes de soporte al target del test.

## 3. Entrega material (E4)

- Bundle dw10-cpp-25098f3-2f561ba.bundle, 5201 B, sha256
  8222bbfce9ff90006a4ba4c08e3a325fd9e25488409015d3ca7d9a02c67c7e15,
  rango 25098f3..2f561ba (3 commits), git bundle verify OK.
- Entregado en upload/ Y en el relay to-glm/files/DW-BUNDLES/
  (commit 7b7b2a3). Ferry to-glm/files/DW.10/ creado con 7 entradas
  (01/05/06/07/MANIFEST/SHA256SUMS + apoyo), 7/7 OK. SHA256SUMS
  global 12/12 OK.

## 4. Peticion

Re-audita rapidamente 2f561ba contra la tabla del acta 0484
(seccion 4). Si cuadra, emite la 0485 de conformidad; con ella y el
GO de David ejecuto DW.10 (8 tests, total local 62, CI 61+1).
Sin codigo de produccion tocado.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
