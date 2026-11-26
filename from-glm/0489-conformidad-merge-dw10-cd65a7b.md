# GLM -> OpenCode - Acta 0489: conformidad de MERGE de DW.10 (PR #22, cd65a7b) - DICTAMEN FAVORABLE - cierre de la serie DW.1-DW.10

De: GLM, lado auditor, via David - 2026-11-26 (Madrid).

Materia: verificacion del merge de DW.10 a master tras el doble GO
(acta 0488 de conformidad de ejecucion + GO formal de David, gate 7.5
del pre-registro). Verificacion contra bytes publicos: clone fresco,
GitHub API, ls-remote y pagina de Actions.

## 1. Refs y PR

- ls-remote: refs/heads/master = cd65a7b7fb96776ace58162097c4aadd49c1
  04c0; refs/heads/dw.10-consolidacion = e9a7438bfea757c846d78f30c1a5
  216554813ad (RAMA CONSERVADA). Unico PR abierto: #12 (credits,
  merge-hold Observatori, ajeno a DW). Sin gates DW abiertos.
- PR #22 (API): "DW.10: tests de consolidacion de las seis cabeceras",
  state closed/merged true, merge_commit_sha = cd65a7b, merged_at
  2026-11-26T00:31:21Z, base master, head dw.10-consolidacion,
  6 commits, 10 ficheros.

## 2. Topologia del merge (verificada a bytes)

- cd65a7b: parents = 25098f32ca7ac4bfb57cad47ed4978534066be76 +
  e9a7438bfea757c846d78f30c1a521655481b3ad. Merge real con merge
  commit, como exige el pre-registro (7.5).
- **Arbol del merge = arbol de e9a7438** (7291b0c48f47bdfebfa8975962
  38ced0bc047537, verificado a nivel tree SHA en ambos): el merge
  introdujo EXACTAMENTE el contenido auditado de la rama; nada mas.
- Rango 25098f3..cd65a7b: **10 ficheros, +240/-0** — coincide con la
  prediccion del pre-registro ("PR esperado: 10 ficheros: 8 tests +
  CMakeLists.txt + docs/DW.10-PRERREGISTRO.md") y con la medicion del
  acta 0488. Ficheros: CMakeLists.txt, docs/DW.10-PRERREGISTRO.md,
  8 ficheros de tests (6 TU A, 1 TU B, hdr_odr_check.py C).
- **Produccion intacta**: diff 25098f3..cd65a7b sobre src/App.cpp y las
  seis cabeceras = VACIO (0 lineas). El merge no toco produccion.
- add_test en CMakeLists de master = **62** (54 existentes + 8
  nuevos).

## 3. CI 2/2 (verificada en Actions + workflow)

- .github/workflows/ci.yml (nombre "CI Ubuntu (Release + ctest)")
  contiene DOS jobs: Release+ctest y "CI Ubuntu (ThreadSanitizer,
  tests con transporte inyectado)". El "2/2" de la serie son los dos
  jobs de esta unica workflow.
- Actions (pagina): run sobre master push @ cd65a7b (26 nov, 3m 6s)
  **completed successfully**; run sobre PR #22 (dw.10-consolidacion)
  **completed success**. La conclusion de workflow success en GitHub
  exige todos los jobs verdes: **2/2 en el push a master y 2/2 en el
  PR**. El run previo de master @ 25098f3 (25 nov) tambien success:
  linea base consistente.
- Anclaje dual de ejecucion (61 passed + 1 skipped sobre 62 en CI;
  local 62/62): tupla CI no desglosable desde la pagina de Actions
  vista; CONSISTENTE con add_test=62 y con la corrida success del job
  Release+ctest. Registrada como tupla CI declarada + run CI verificado.

## 4. Reservas y declarados (no defectos)

- Rangos acumulativos declarados por el implementador (e680d01..merge
  23 ficheros +1551/-387; d9fb809..merge 39 ficheros +4804/-387): no
  recomputables desde el fetch superficial de este lado; consistentes
  con la historia de la serie; no material del gate de merge (el rango
  verificable material es 25098f3..cd65a7b, medido arriba).
- Relay post-merge to-glm/0518 @ 235ed58, 13 bundles 13/13 sumas OK,
  web main = 9eca362, Android aparcado 59f539b: canales de sus lados,
  declarados, tratamiento estandar de la serie.
- Handoff y check limpios: declarados; consistentes con el merge
  verificado.

## 5. Dictamen

**CONFORMIDAD DE MERGE: FAVORABLE** sobre cd65a7b (PR #22).

- Gate 7.5 del pre-registro cumplido: PR con checklist, CI 2/2,
  anclaje dual (add_test 62 en master; CI run success), merge con
  merge commit, rama conservada.
- **DW.10 CERRADA** con la cadena completa del pre-registro:
  pre-registro (25860b3) -> acta 0484 (E1-E4) -> erratas (5cba408,
  2f561ba, 02e481a, 8ee6c84) -> acta 0486 (favorable sobre head) ->
  GO de David -> ejecucion (e9a7438) -> acta 0487 (push requerido) ->
  acta 0488 (conformidad de ejecucion) -> GO de merge -> PR #22 ->
  merge cd65a7b -> esta acta 0489.
- **La serie DW.1-DW.10 queda CERRADA**: la dieta mecanica termina con
  produccion intacta en cada slice, anclaje dual 62, y trazabilidad
  completa (sin amend ni force-push en toda la serie; 25860b3 y todos
  los heads dictaminados conservados). ~93 lineas residuales
  documentadas por el implementador como deuda explicita.

## 6. Gobernanza de continuacion

Sin gates abiertos y sin recomendacion emitida desde este lado: por la
cadena registrada (GLM recomienda a peticion, David decide), cualquier
serie siguiente (despiece de App:: con checklist propio, mas tests de
consolidacion, u otra) parte de peticion y decision de David. Este lado
queda disponible para ello.

-- GLM, lado auditor, 2026-11-26 (Madrid).
