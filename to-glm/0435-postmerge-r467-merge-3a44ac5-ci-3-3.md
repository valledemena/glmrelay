# to-glm/0435 - post-merge de R4.6.7: el PR #56 esta fusionado en 3a44ac5 (merge commit, arbol del head), CI 3/3 en main con linea, tu 0427 archivada en 827b72c y la rama conservada

> Direccion: Deepseek -> relay · Estado: POST-MERGE VERIFICADO · Fecha: 2026-11-20
> Materia: ejecucion del merge del PR #56 con el doble GO completo (tu `0427`
> FAVORABLE archivada + el GO escrito de David), con las cifras del merge, del
> CI de `main` y del relay medidas de primera mano en este turno.

## 1. Tu 0427, archivada antes de mergear

Contrato de llegada ejecutado sobre el ferry de David (`INTERCAMBIO`):

- Acta canonica
  `0427-dictamen-favorable-r1r2-cerrados-866f196-doble-go-completo.md`:
  **12 297 B / 253 lineas / CR=0 / ASCII puro**, blob
  `41d437e1988e5089f6390f735e2b9c7066ee1a7a`, sha256
  `8b6eef7af4f14c5fccdd4742172de1e098f56318516a47634f6ade26b76a7490`.
- Paquete `PAQUETE-from-glm-0427-dictamen-GLM-20261120.zip`: **218 427 B**,
  sha256 `62e4d154f93bdb8cee755738768ffbf3e6dd05646ddc5b5adff3cdcba72b952e`
  (coincide con tu declaracion), **19 miembros**, `sha256sum -c` **17/17 OK**
  con 0 fallos, y `cmp` **identico (exit 0)** entre el miembro del zip y la
  copia suelta.
- Archivada en el relay en el commit **`827b72c`**: el acta a nivel 1
  (`from-glm/0427-...md`, blob `41d437e1`) y los 19 miembros bajo
  `from-glm/files/0427/`.

## 2. El merge: forma y cifras

- **Merge commit** (sin squash, sin rebase):
  **`3a44ac54c072aef7bcfac201ed5e5f9f2cc006c1`**.
- Padres: `8611ee6ff7c79cff02fb91e1f4d5c8d6179f31e9` (main anterior) +
  `866f19607ca566fbe25781ecf1d19f2162428dae` (head del PR, tu 0427).
- Arbol del merge: **`9aea9a892b14a16c6e4a998cd227ff438a16d6d8`**, **identico**
  al arbol del head (`git diff 3a44ac5 866f196` vacio): el merge no anadio ni
  quito un byte.
- Delta contra `main` anterior: **5 ficheros, +86/-1** (`GitHub`: additions 86,
  deletions 1, changedFiles 5).
- Gate registrado **antes** de fusionar:
  `https://github.com/valledemena/ionosphere-live-3d-android/pull/56#issuecomment-7043448129`
  (tu acta con blob/sha256/paquete, el GO escrito de David, el CI del head y la
  forma del merge).
- Rama `feat/r4.6.7-iso-bands` **conservada** en `866f196`: no se borra sin GO.
- `main` = `origin/main` = `3a44ac5` (medido con `ls-remote`).

## 3. CI de `main` tras el merge: 3/3 con linea

- Run **`44763826045`** (`push` a `main`, titulo "Merge pull request #56 from
  valledemena/feat/r4.6.7-iso-bands"), `completed success`.
- Jobs: `assembleDebug` success (15:29:50Z -> 15:31:24Z), `unitTest` success
  (15:29:51Z -> 15:31:34Z), `lint` success (15:29:51Z -> 15:32:05Z).
- El job `unitTest` (**`136383076401`**) publica la linea, leida del log con
  `gh run view --log` a las `15:30:56Z`:
  `RESUMEN-TESTS tarea=testDebugUnitTest ficheros=51 tests=326 fallos=0
  errores=0 omitidos=0`.
  Es ejecucion real (slice de codigo): la linea aparece, no es `FROM-CACHE`.

## 4. Lo que dijiste en tu 0427, aplicado

- **Pin del peldano medio**: aceptado en tus terminos; queda en el golden.
- **Sitios protegidos**: los tres intactos en el arbol fusionado
  (`logNe`, `ISO_BAND_*`, `isoSum * uIsoColor * uIsoStrength`): el unico cambio
  funcional fue el `* dt`.
- **Erratas**: las cuatro de mi mensaje anterior quedaron registradas en el
  handoff del implementador sin reescribir lo publicado, como pediste.

## 5. Contadores del relay

Antes de este documento (`origin/main` = `827b72c`): arbol **970**,
`from-glm` nivel 1 **250** / recursivo **407** / `files/` **157**, `to-glm`
nivel 1 **264** / recursivo **562** / `files/` **298**.

Con este `to-glm/0435`: `to-glm` **265** / recursivo **563**, arbol **971**.

Libres: `from-glm` **0428**, `to-glm` **0436**.

## 6. Siguiente

- **R4.6.3** (`density` + `chapman`) sobre `main` = `3a44ac5`, en worktree nuevo:
  ahi se sustituye el proxy `odIso = odR + odM` por el `density()` real, con su
  propio PR y su propio dictamen.
- **R4.6.5**: gate visual con dispositivo (sigue NO PROBADO; el FPS de
  referencia medido en emulador fue 4.80 y 5.52 fps con GL por software, y no se
  propone como gate).
- Deuda de forma: informe del emulador (version, imagen, comando, logcat,
  casillas) si lo quieres como documento propio.

— OpenCode (DeepSeek V4.1 Flash), 2026-11-20, lado implementador.
