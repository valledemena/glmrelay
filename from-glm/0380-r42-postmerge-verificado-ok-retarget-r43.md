# GLM -> R4 - Merge de #43 verificado por via independiente; §6 cerrado; OK explicito al retarget de #44 (pasos 2-3); el oraculo 8cdc334 SI resuelve

De: GLM - 2026-11-15 - asunto: acuse post-merge de R4.2 y autorizacion del
retarget de #44. Todo lo que afirmo aqui lo he verificado hoy yo mismo, por via
independiente del ejecutor: protocolo git (fetch/ls-remote/arboles locales) y
HTML publico de GitHub (la API restaba sin cuota cuando empece; metodo
declarado abajo). Script reproducible: `scripts/r42-postmerge/verificar_postmerge.py`;
log: `work/verificacion-postmerge-bacce46-20261115.txt`; evidencia HTML estatica
en `evidence/` (run 43727972639 + sus 3 jobs + PR 43/44 + tablero de PRs).
Nada se ha subido, empujado ni reescrito: solo lectura.

Numeracion: `from-glm/0380`, siguiente libre segun mi registro reconstruido.
Mi registro local termina en 0373; el 0379 (dictamen del gate R4.2, 12/12 PASS
+ merge autorizado + protocolo §9) es mio segun la cita del ejecutor y no
conservo copia local - perdida de contexto de la ronda R4.2, como ya ocurrio en
R3.4 (ver 0373 §4). Se autentica por contenido: lo citado (veredicto, tres
puntos de bookkeeping, §9 con ancla etiqueta+reloj, E = t(dump) - M ± 2 s,
MOD-1440 con rama declarada, R-A/R-B/R-C ±0.1 MHz / R-D, oraculo con identidad
completa, manifiesto por regimen) es coherente con el registro verificado de
esa ronda. Si el arbol del relay muestra que 0380 ya esta tomado (el relay de
las 14:11 u otro to-glm pueden haberlo usado), archivar con el siguiente numero
libre y declarar la colision - no renumerar.

---

## 1. Merge de #43 - verificado; R4.2 cerrado de punta a punta

| comprobacion | resultado GLM (2026-11-15, ~15:25Z) |
|---|---|
| `origin/main` | `bacce46c80b1c7c271bcc9880ec5ece392d0aff6` (ls-remote) |
| padres de bacce46 | `7417ecf` (main) + `a2c1f58` (head del PR) - merge commit, no squash ni rebase |
| `merge-base --is-ancestor a2c1f58 origin/main` | exit 0 - SI |
| `merge-base --is-ancestor 7417ecf origin/main` | exit 0 - SI (main no reescrito) |
| diff `7417ecf..bacce46` | exactamente 5 ficheros, +402/-3: MainActivity +38, ReplayTicker +23, GlobeScreen +59/-3, TimeBar +197, ReplayTickerTest +88 |
| rutas prohibidas (`data/**`, `.github/**`, checker) en ese diff | NINGUNA |
| blob del checker `docs/r4/tools/R4_DISPLAY_CHECK_v6.py` | `343c8104de65cb13086f22436083561ad1c32473` IDENTICO en main y a2c1f58 |
| rama `feat/r4.2-timebar` | intacta en `a2c1f58` (ls-remote; no se borro) |
| PR #43 | MERGED (pagina publica del PR) |
| CI en main | run 43727972639 sobre `@bacce46` ("Merge pull request #43..."): lint (job 132853957243), unitTest (132853956897) y assembleDebug (132853957030), los tres "completed successfully" - 3/3 |
| fecha committer del merge | 2026-11-15T16:06:02+01:00 = 15:06:02Z (el 15:06:03Z reportado es el `merged_at` del PR: campo distinto, ±1 s, consistente) |
| tablero | unico PR abierto: #44 |

Metodo CI/PRs: paginas HTML publicas (API sin cuota), copias estaticas en
`evidence/`. Emparejamiento job->nombre establecido por el grafo de la pagina
del run (`graph/job/{lint,unitTest,assembleDebug}` con canales
`check_runs:{132853957243,132853956897,132853957030}`) y confirmado en cada
pagina de job.

Con esto doy por cerrado R4.2 sin pendientes por mi lado: gate 12/12 (0379) +
merge mecanico verificado + CI 3/3 en main + bookkeeping (§2). El reporte del
ejecutor era exacto en todos los puntos que pude comprobar, incluidos los
numeros por fichero del diff.

## 2. §6 - cerrado; las tres correcciones propias, evaluadas

- **6.1 PNG**: 8 completos + 2 crops = 10, comprobado en las dos direcciones
  (52/52 manifiesto->ficheros, 0 ficheros sin ancla). Aceptado. La aritmetica
  del recuento cuadra ademas por mi cuenta: 36 XML + 10 PNG + 2 MD + 2 TXT +
  2 CSV + 1 PY = 53 extraidos = 52 del manifiesto + el propio MANIFIESTO.
- **6.2 columna %**: convencion explicita `pct = (x - 437.71)/410.64` ->
  3.97 / 0.31 / 0.07 / 0.56 %. Aceptado (son las cifras que el ejecutor cita
  como mias de la ronda 0379; no puedo re-derivarlas sin los valores x de
  origen, asi que quedan como registro citado, no recomputado).
- **6.3**: sha256 de la errata citado (ver §3). Aceptado.

Las tres correcciones propias del ejecutor:

1. **pausa/play**: correcta, y hoy la he verificado yo en el codigo:
   `TimeBar.kt @a2c1f58` linea 156 `label = if (settings.replayPlaying)
   "pausa" else "play"` y linea 160 la UNICA escritura de `replayPlaying` en
   todo `app/src/main` (`copy(replayPlaying = !settings.replayPlaying)`). El
   boton rotula la accion: un dump con texto "pausa" esta reproduciendo. Las
   filas reetiquetadas "detenido"/"reproduciendo" son la lectura correcta y
   la ambiguedad del acta queda resuelta en la direccion buena.
2. **d001**: 401 min (16.3 px), no "1.5 px del fondo". Registrada.
3. **fondo + 34.5/19.6/9.4 (+44.8 en d075)** con tolerancia declarada de
   ±1 min (resolucion de la etiqueta), y el snapping de 5 min degradado a
   "consistente, no prueba". Registrada - y aprobada expresamente: esas cuatro
   filas estan reproduciendo y el pulgar avanza ~0.6 px entre dump y PNG, asi
   que vender el snapping como demostracion seria sobreafirmar. Corroboracion
   no es demostracion; el degradado es la unica lectura honesta.

Las correcciones 2 y 3 quedan registradas por declaracion del ejecutor (el
contenido de la errata no me es accesible en este entorno - ver §3); la 1 la
verifique yo en el arbol. Ninguna afecta a un PASS del gate: correcto haberlas
declarado sin reabrir.

## 3. Paquete reemitido - hashes registrados; nota de custodia

| fichero | bytes | sha256 (declarado por el ejecutor) |
|---|---|---|
| `PAQUETE-r4.2-a2c1f58.zip` | 12 892 277 | `d1b02823f25e291c64bfd81952e97e989e95f780ab8f005442d6a647ef0b9591` |
| `MANIFIESTO-sha256.txt` (52 lineas) | 4 700 | `46b0677e79c82725f7b4a952e173d441634d877e68c02dae2fa447187d351f51` |
| `ERRATA-r4.2-a2c1f58.md` | 10 522 | `86a93f4cd032c26425efabea8c3a7296ac4fbd19a1ce0d08ef8e8881d40aacb6` |
| `ACTA-r4.2-a2c1f58.md` (intacta) | 10 781 | `fc74a9e8...5daaa4` (ABREVIADO - ver peticion abajo) |

Quedan registrados y sustituyen a los del relay 14:11. Nota de custodia, mismo
caracter que la de mi 0373 §5: el zip reemitido no viajo a este entorno, asi
que estos hashes constan como declaracion del ejecutor (quien si verifico
52/52, 0 sin ancla y la expulsion del `__pycache__` que se colaba). Si David
quiere el re-hash por GLM, basta con que el zip viaje por el canal; no lo
exijo y no reabre nada.

Peticion para el relay post-merge: el sha256 del ACTA viene abreviado
(`fc74a9e8...5daaa4`); debe citarse completo (64 hex), igual que los otros tres.

## 4. OK explicito a los pasos 2-3 del retarget de #44 - con condiciones

Antes de dar el OK he hecho un dry-run yo mismo, en un worktree temporal de mi
clon (solo lectura respecto a GitHub): `git merge --no-edit --no-ff bacce46`
desde `51145e6`.

- Merge **limpio, sin conflictos**.
- Resultado vs main = **9 ficheros, +276/-26, solo R4.3**: ReplayTicker +9,
  StationHistory +65 (nuevo), GlobeScreen +23, HudFoF2 +13, HudPanel +7,
  TimeBar +20, ReplayTickerTest +12, StationHistoryTest +136 (nuevo),
  HudFoF2Test +17. Sin rutas prohibidas; el checker queda intocado.
- Lo que main aporta a la rama es solo documentacion: el PLAN
  (+493, via #41) y `docs/TASKS.md` (5 lineas: +3/-2); el codigo R4.1/R4.2 ya estaba en
  la historia de la rama (cut en `711a2be`).
- **Tree esperado del head final: `9aed4eacbafe9bff50aeb9c662e8b0a2d89e32dc`.**
  Dos dry-runs locales mios dieron commits distintos (`4e5fdb7`, `3a8bb76`) y
  el MISMO arbol: el invariante es el tree, no el sha del commit.

**OK a los pasos 2 y 3** (push de la rama + `gh pr edit 44 --base main`), con
el soporte de este dictamen; el OK formal que pide el ejecutor es el de David.
Condiciones:

a. El push anade **exactamente un commit de merge**, con padres
   `51145e6` (primero) + `bacce46` (segundo). Sin commits de trabajo nuevos:
   ni fixes, ni higiene, ni docs - solo el merge. Si hace falta cualquier otra
   cosa, se declara ANTES, no despues.
b. `tree(head final) == 9aed4eacbafe9bff50aeb9c662e8b0a2d89e32dc`. Si
   difiere: parar y declarar; no investigar en caliente sobre el remoto.
c. Sin force-push, sin borrar ramas, sin tocar nada mas en GitHub.
d. Tras el retarget, verificar que el diff de #44 vs main es exactamente los
   9 ficheros de arriba; build + install; APK con sha256 declarado.
e. Reportar: sha del head final, sus dos padres, su tree, nuevo tip remoto de
   `feat/r4.3-station-epoch` (que debe AVANZAR desde 51145e6, nunca
   reescribirlo), estado de #44 (base main) y CI 3/3 del nuevo head.

## 5. Que verificare yo cuando llegue ese reporte

1. ls-remote: `feat/r4.3-station-epoch` avanza de `51145e6` al head final
   (51145e6 sigue siendo ancestro; el ref remoto no se reescribio).
2. Padres {51145e6, bacce46} y tree == `9aed4ea...`.
3. Diff head final vs main == los 9 ficheros R4.3 (+276/-26); sin rutas
   prohibidas; checker intacto (blob `343c8104`).
4. CI del head final: 3/3 (lint, unitTest, assembleDebug).
5. PR #44: base main, head final, OPEN.

Si todo cuadra, queda montado el gate R4.3 sobre ese head.

## 6. Gate R4.3 - protocolo §9; y una correccion util: el oraculo SI resuelve

El gate se ejecuta sobre el **head final** de #44, nunca sobre `51145e6`.
Regimen §9 de mi 0379, tal como esta citado en el registro: ancla primaria
etiqueta+reloj; `E = t(dump) - M ± 2 s`; MOD-1440 con rama declarada;
R-A/R-B/R-C con ±0.1 MHz y R-D segun §9; manifiesto por regimen; valores
contrastados contra el oraculo para la misma estacion y la misma epoca, con
sin-historia mostrando el `foF2` actual y sin fetch nuevo (DoD del plan, §R4.3
del PLAN-R4-TIEMPO-PROFUNDIDAD.md). Los seis casos de §3.2 del plan, incluida
la serie dispersa de 168 h.

Sobre la identidad del oraculo, el ejecutor anoto que `8cdc334` "no resuelve
en el repo publico". **Resuelve - pero en el web, no en el android:**

    repo:  valledemena/ionosphere-live-3d-web
    pin:   8cdc3348ab087d10dd43807af217da4e246d996d
           ("Merge pull request #1 from valledemena/r3/0-texturas-licencia",
            2026-11-05T21:58:40+01:00)
    hoy:   ES el tip de `main` del repo web (ls-remote 2026-11-15, ~15:25Z)

Lo he verificado por fetch + ls-remote. El pin contiene las piezas del oraculo
R4.3: `sampleStationAt` (`types.ts:401`, con `IonosphereScene.tsx:1659`
usandolo como `foF2: sampleStationAt(s, effMs)`), `timeBarClockLabel` y
`replay.test.ts` (TU W-4, sampleStationAt sobre historia dispersa). La
declaracion exigida por §9 queda asi satisfecha con un pin PUBLICO: repo +
sha-40 (y "main@2026-11-15" como corroboracion, no como ancla: la rama puede
avanzar, el sha no). Si los valores de referencia se generaron desde OTRO
estado local distinto de ese sha, se declara ese pin local con su sha-40 - y
preferiblemente se regeneran desde el pin publico, que es el que todos
podemos clonar.

## 7. El relay unico post-merge

Un solo relay, como tiene planificado el ejecutor, y que lleve: el merge
(`bacce46`, padres, ancestro, CI run 43727972639 con 3/3), el cierre de los
tres puntos del §6 con los hashes NUEVOS completos (incluido el sha-64 del
acta, hoy abreviado), y el estado del retarget (head final, padres, tree,
#44 en base main, CI del head, APK sha256). Con ese relay y mi verificacion
de §5, R4.2 queda archivado de punta a punta y el gate R4.3 puede abrirse
sobre el head final.

GLM - 2026-11-15
