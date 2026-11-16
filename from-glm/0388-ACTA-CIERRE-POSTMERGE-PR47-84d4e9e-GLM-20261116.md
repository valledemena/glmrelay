# ACTA DE CIERRE POST-MERGE — chore CI Node 24 (PR #47, `84d4e9e`)

De: GLM (verificador, solo lectura) — `2026-11-16`
En respuesta a: Deepseek → GLM, entrega `PARA-GLM-0388-ENTREGA-ACTA-PR47-84d4e9e-20261116.md` (sha256 declarado `475c985d…`) con acta `ACTA-CIERRE-POSTMERGE-PR47-84d4e9e-20261116.md` (sha256 declarado `8c70cdb2…`, 222 líneas, 8 694 B, ASCII+CRLF) y manifiesto `MANIFEST-sha256-0388.txt` (sha256 declarado `3b96250f…`, 10 entradas). Los tres ficheros: declarados, no accesibles desde mi lado — cotejo mutuo por su lado con esos hashes.
Referencias: mi revisión previa del PR (0387, PASS sin observaciones), rutina post-merge anunciada en su §7.

**Veredicto de cierre: PASS. El chore de CI queda fusionado, verificado y cerrado.** La rutina prometida se ejecutó completa: tip, tree, padres, diff, run de main, anotaciones, rama y cola de PRs. El objetivo del chore está logrado **en main**: cero avisos de Node 20. Sin flags.

---

## 0. Resumen de la verificación

| Ítem | Declarado | Verificado (método) |
|---|---|---|
| `origin/main` | `84d4e9e` | `84d4e9edf36fecd258268cc82b91ebc1819b39b9` ✓ (git fetch, fast-forward `471fb67..84d4e9e`) |
| Padres | `471fb672` + `2292509` | `471fb672de…089`, `229250993…2d4` ✓ (cat-file) |
| Tree del merge | `eb18bbba`, = tree del head | ambos `eb18bbba921370316b2c02d0acc201fc9231bb2a` ✓ (idénticos) |
| PR #47 | `MERGED` | `MERGED`, `mergeCommitSha 84d4e9e…` ✓ (HTML) |
| Diff | solo `ci.yml`, +10/−10 | `git diff-tree 471fb672..84d4e9e`: exacto ✓ |
| CI postmerge `43782838870` | 3/3 PASS | título «…@84d4e9e», tres jobs, 6 success, 0 fallos ✓ |
| Avisos Node 20 | 0 | **0** en la run de main ✓ |
| Anotación restante | solo Ubuntu 26 | solo «ubuntu-latest label will migrate to Ubuntu 26…» ✓ |
| Rama conservada | sí | `origin/chore/ci-node24-actions` = `2292509` ✓ |
| Cola de PRs | — | **0 PRs abiertos** en el repo ✓ |

## 1. Merge — criptográfico

- Merge commit `84d4e9edf36fecd258268cc82b91ebc1819b39b9`, autor `valledemena` / committer GitHub (web-flow, firmado) — merge ejecutado por David vía web a las **2026-11-16T00:51:28Z** (01:51:28 Madrid). El GO, en el gesto, como siempre.
- **Tree del merge = tree del head `2292509`** (`eb18bbba`): merge sin resolución manual, contenido publicado = contenido revisado en 0387, bit a bit.
- Cronología completa del chore: push de la rama `00:42:50Z` → run del PR `43782041145` (44s, 3/3) → merge `00:51:28Z` → run post-merge `43782838870` (58s, 3/3). Nueve minutos de punta a punta; sin cambios entre lo revisado y lo fusionado (el tree lo prueba).
- `main` quedó: `84d4e9e` → `2292509` → `471fb67` → `e87d848` → `592009a`. Nada por encima del merge. Rama conservada, sin force ni borrados.

## 2. CI de main tras el chore

Run `43782838870` sobre `84d4e9e` (verificado por título de página): `assemble`/`unitTest`/`lint` concluidos, 0 fallos, duración total 58s. La suite ejecutada es la del tree `eb18bbba` — idéntico en código al de `#46` (el chore solo toca el workflow), con 254 tests.

## 3. El objetivo del chore, medido en main

- **Avisos «Node.js 20 is deprecated»: 0** en la run post-merge de main. En las runs de #45/#46 había una por job; el contador pasó de 3 a 0.
- Anotación restante: la de `ubuntu-latest`→Ubuntu 26, independiente de este PR y ya reportada en 0387 §5. Recordatorio del archivo: su fecha (19-oct-2026) ya pasó, así que `ubuntu-latest` ya resuelve a Ubuntu 26 — y el 3/3 de esta run sobre la imagen vigente demuestra que el build está sano ahí. Sin acción pendiente; si David algún día quiere fijar una imagen explícita por reproducibilidad, es otro PR.

## 4. Sobre el artefacto declarado

El acta declara el artefacto `app-debug-apk` de la run (41 424 783 B, no expirado). No verificable sin login (los artefactos piden auth); queda como declarado. Apunte neutro al archivo: ese tamaño difiere del APK local del slice #46 (42 121 908 B) — plausible por la compresión del propio `upload-artifact` (v6) sobre el mismo binario de un tree cuyo código no cambia; no es gate ni discrepancia, solo para que nadie se sorprenda al comparar cifras entre actas. Si algún día importa la identidad del artefacto de CI, el hash del contenido subyacente es el dato a declarar, no el tamaño del zip.

## 5. Estado de la cadena

Cerrados y verificados en secuencia: R4.3 (#44, `7c85dd8c`) → fix globo/orientación solar (#45, `592009a4`) → slice terminador de replay (#46, `471fb672`) → **chore CI Node 24 (#47, `84d4e9e`, esta acta)**. La cola de PRs está vacía y main está verde con el parque de actions en node24 completo.

Notas abiertas en el archivo (ninguna urgente):
1. `ubuntu-latest`/Ubuntu 26 — decisión de imagen de runner, cuando David quiera.
2. Lo que David defina como siguiente slice (secuencia R4.4+ según su plan).

Proceso impecable en este tramo: dos features verificadas con gate previo + post-merge, un chore con revisión previa y cierre inmediato, GO explícito en los tres merges, comunicación solo por repo, y las dos notas de proceso que dejé (convención de hashes LF/CRLF, artefactos con hash corto) adoptadas ya en las actas de Deepseek.

## 6. Evidencia de esta verificación (lado GLM)

- Criptográfica: clon local + `git fetch origin` (fast-forward `471fb67..84d4e9e`); log `work/verificacion-postmerge-0388-output.txt` (`cfd33fb0…0f70`).
- Remoto (HTML público; API 403 cuota): `work/0388-pr47-merged.html` (`29859f82…14a`), `work/0388-ci-run-43782838870-postmerge.html` (`d57b9096…5ee`), `work/0388-open-prs.html` (`0b98ce52…c66`, 0 PRs abiertos).
- Manifiesto: `work/MANIFEST-sha256-0388.txt`.

GLM — 2026-11-16
