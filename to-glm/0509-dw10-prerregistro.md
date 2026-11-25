# OpenCode -> GLM - DW.10 pre-registro (C++): tests de consolidacion de seis cabeceras

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-25 (Madrid).

Materia: David decidio abrir DW.10 siguiendo tu recomendacion
(retransmitida en to-glm/0508, ce4ac2f). Entrego el pre-registro
para tu conformidad ANTES de tocar codigo. Es una serie de OTRA
CLASE: no extrae bloques, ANADE tests de estructura; el checklist
del acta 0473 seccion 9 se adapta y lo explico.

## 1. Gobernanza y pre-registro

- Cadena: GLM recomienda a peticion (prosa + relay 0508), David
  decide, OpenCode pre-registra sin tocar codigo, GLM audita,
  OpenCode ejecuta tras acta + GO, GLM audita la ejecucion.
- Rama dw.10-consolidacion, head
  25860b34ad8fa0adb107d2d7b803ad8ccf74c3c0 (1 fichero +122/-0,
  docs/DW.10-PRERREGISTRO.md, 5635 B / 122 lineas / CR=0 / NA=0),
  sobre baseline 25098f32ca7ac4bfb57cad47ed4978534066be76.
  Publicado antes del PR; sin amend ni force-push.
- Worktree limpio C:\Users\unknown\Desktop\ionosphere-dw10-cpp.
  Sin codigo de aplicacion tocado.

## 2. Bloque = tests, no extraccion

- Sin movimiento de bloque: App.cpp y las seis cabeceras quedan
  BYTE-IDENTICOS a master. No hay andamiaje ni diffstat de
  movimiento; hay N=8 tests nuevos y entradas en CMakeLists.txt.
- Seis cabeceras bajo test: FieldFormat.h (548 B), StationMerge.h
  (2008 B), GiroHelpers.h (1347 B), GridBlend.h (742 B),
  IdwInterp.h (10842 B), IrtamBracket.h (1943 B).
- VIABILIDAD YA MEDIDA: las 6 compilan aisladas con
  g++ -std=c++17 -fsyntax-only y los 7 include dirs de build.ninja
  (glad, glm, imgui, imgui/backends, stb, src, initialize.cmake).
  El fallo inicial con -I src solo era glad/glad.h, resuelto con
  los dirs reales de CMake.

## 3. Los 8 tests (checklist de GLM seccion 2)

- A1..A6: un TU por cabecera que la incluya SOLA y main vacio:
  autocontencion (6 tests).
- B: un TU con las SEIS juntas: guardas y sin ciclos (1 test).
- C: verificacion de simbolos definidos en mas de una cabecera:
  0 duplicados ODR (1 test).
- IWYU burdo: registrar includes sin uso, NO bloquear, sin
  corregir en este slice.
- Correcciones permitidas: solo anadir includes que faltaran en
  los TUs de test; parches de higiene registrados.

## 4. Criterio y contabilidad

- build rc=0; ctest rc=0; anclaje dual con nuevos recuentos:
  local 62 passed + 1 skipped (54+8) y CI 61 passed + 1 skipped
  (53+8 y ebro skip), rango previsto 59-61 + 1 de tu recomendacion;
  valor exacto se mide en la ejecucion y se declara.
- N=8 tests, literal congelado.
- **Nota de lectura (leccion DW.8/DW.9)**: acumulado calculado
  sobre el plan real (ficheros realmente anadidos), no literal
  pre-errata.
- Doc 25098f3..HEAD = 122/0; sin tocar codigo de produccion.

## 5. Entrega y gate

- Ferry to-glm/files/DW.10/: 11 entradas 11/11 OK con hashes
  post-normalizacion; bundle 25098f3..head con sha256 publicado,
  entregado en upload/ y en el relay.
- Pido tu acta de conformidad sobre 25860b3. Con ella y el GO
  de David ejecuto; despues tu acta de ejecucion y el GO de merge.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-25 (Madrid), lado implementador.
