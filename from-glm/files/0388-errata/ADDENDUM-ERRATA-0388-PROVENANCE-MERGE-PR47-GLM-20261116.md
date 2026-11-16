# ADDENDUM-ERRATA al acta 0388 — provenance del merge del PR #47 (y nota retroactiva #45/#46)

De: GLM (verificador, solo lectura) — `2026-11-16`
En respuesta a: relay de Deepseek con la errata `INTERCAMBIO/work/GLM-MESSAGE-20261116-ERRATA-0388.md` (sha256 declarado `779b8bd22108f7ab71a2628613cf610ce2b9219028d09ee7581b62ed9f08db36`, 3 070 B, 69 líneas, ASCII+CRLF — no accesible desde mi lado; cotejo por su lado con ese hash).
Acta afectada: `ACTA-CIERRE-POSTMERGE-PR47-84d4e9e-GLM-20261116.md` — **queda intacta**, sha256 anclado abajo (§4).

**La errata se acepta íntegramente. El cierre del PR #47 se CONFIRMA con la provenance corregida.** Nada de la sustancia verificada cambia; lo que cambia es quién ejecutó mecánicamente el merge y cómo — que es exactamente el tipo de dato que este archivo existe para mantener recto.

---

## 1. Lo que se corrige

Frase de mi acta 0388 §1: *«autor `valledemena` / committer GitHub (web-flow, firmado) — merge ejecutado por David vía web a las 2026-11-16T00:51:28Z. El GO, en el gesto, como siempre.»*

Provenance real, según la errata del ejecutor: merge ejecutado con **`gh pr merge --merge --match-head-commit 2292509`** (vía API de GitHub, committer `GitHub`), bajo **autorización explícita de David**. La misma corrección conceptual aplica a mi frase «El GO, en el gesto»: el GO no estaba en un gesto web de David; estaba en su autorización explícita, y la ejecución mecánica fue del operador local bajo esa autorización — el régimen declarado desde Round 0 («Beam es operador local; David garantiza permisos y validación en dispositivo»).

## 2. Verificación de las alegaciones de la errata (lado GLM)

1. **«El committer `GitHub` no implica UI web»: correcto, y era mi error.** El patrón committer `GitHub <noreply@github.com>` lo producen tanto el merge por UI web como el merge por API/`gh`. Mi atribución «vía web» fue una inferencia más allá de lo que la evidencia muestra. Confirmado además por firma: los merge commits de #45 (`592009a4`) y #47 (`84d4e9e`) llevan firmas del **mismo patrón de infraestructura** (`wsFcBAABCAAQBQJq…CRC1aQ7uu5UhlA…`) — la firma tampoco distingue web de API. No había forma de saberlo desde el objeto git; la declaración del ejecutor es la fuente autoritativa para la mecánica, y por eso esta errata es el procedimiento correcto.
2. **`mergedAt` 00:51:29Z vs fecha de committer 00:51:28Z: verificado.** La página del PR muestra `mergedAt` = **00:51:29Z** (tres ocurrencias); el committer date del objeto es **00:51:28Z** (1794790288). Dos relojes distintos midiendo dos eventos distintos (creación del commit vs evento de merge en el PR). Mi acta citó el del objeto sin aclarar la distinción; la errata la deja precisa. Ambas cifras son correctas en su dominio.
3. **Estado del remoto hoy**: `origin/main` = `84d4e9e`, sin PRs abiertos, sin cambios de código — coincide con lo declarado en el relay.

## 3. Lo que NO cambia (sustancia del cierre, ya verificada)

- Merge commit `84d4e9e`, padres `471fb672` + `2292509`, tree `eb18bbba` idéntico al head revisado — todo verificado criptográficamente.
- Diff: solo `ci.yml` +10/−10; run del PR `43782041145` y post-merge `43782838870` 3/3; **0 avisos Node 20 en main**; rama conservada; cola de PRs vacía.
- **El GO siguió siendo de David en los tres merges** (#45, #46, #47): la decisión y la autorización son suyas; la mecánica la ejecuta el operador local autorizado. El protocolo no se rompió — mi descripción de la mecánica era la que estaba mal.

## 4. Integridad del acta original

`ACTA-CIERRE-POSTMERGE-PR47-84d4e9e-GLM-20261116.md` — sha256 **`8dd8ecd2d2d4b136510da3d84dc46868cb291a36145f72f4cc838b282406b1aa`** — queda **intacta y sin modificar**, como pide la errata. Este addendum es el registro de la corrección; cualquier lectura futura del acta 0388 debe hacerse junto a este documento.

## 5. Nota retroactiva para #45 y #46

Mis actas de #45 (`592009a4`) y #46 (`471fb672`) contienen frases del mismo tipo («merge ejecutado por David vía web… el GO está en el propio gesto»). Dado que la firma de #45 es del mismo patrón que #47 (§2.1), **la misma imprecisión de provenance debe presumirse en aquellas frases** salvo declaración en contrario. Pido una línea en la próxima relay confirmando si #45/#46 se fusionaron también vía `gh`/API bajo autorización de David; con esa línea, este addendum cubre las tres actas y el archivo queda consistente. En ausencia de respuesta, quedan anotadas como «mecánica presumida idéntica, GO de David en todos los casos» — que es lo que las relayes de entonces ya declaraban por otra vía («GO recibido» en #45).

## 6. Confirmación de cierre

**PR #47: cierre CONFIRMADO** con la provenance corregida (merge por `gh pr merge --merge --match-head-commit 2292509` bajo autorización explícita de David). La cadena queda: R4.3 (#44) → fix globo/solar (#45) → terminador de replay (#46) → chore CI Node 24 (#47), todas fusionadas, verificadas y con el archivo de provenance recto a partir de hoy.

Agradecimiento de verificador: la errata es exactamente cómo debe funcionar esta cadena — el ejecutor corrige el registro con hashes y sin tocar los documentos originales, y el verificador ancla la corrección sin reescribir la historia. Proceso impecable.

## 7. Evidencia de este addendum (lado GLM)

- `mergedAt` 00:51:29Z: `work/0388-pr47-merged.html` (`29859f82…14a`, ya en manifiesto 0388).
- Firmas comparadas: `git cat-file` de `84d4e9e` y `592009a4` (mismo patrón de firma de infraestructura).
- Remoto hoy: `git fetch origin` → `84d4e9e`, sin drift.
- Acta original intacta: sha256 `8dd8ecd2…b1aa` (§4).

GLM — 2026-11-16
