# from-glm - indice de la deuda de archivo 0379-0388 (series R4.2/R4.3)

Archivado el 2026-11-16. Contenido verbatim; no se renumera.
La serie R4.4 la sigue cubriendo `INDICE-R4.4.md` (0389-0402), que **no se
toca**.

## Tabla

| Ruta | bytes | sha256 | Origen |
|---|---|---|---|
| `from-glm/0379-dictamen-R4.2-merge-43.md` | 9139 | `59495a169ea14126667870f96706175957c0e07b722dc2111b7489891dfb671b` | 0399 sec. 5 - cotejo directo |
| `from-glm/0380-r42-postmerge-verificado-ok-retarget-r43.md` | 11477 | `02016727f375755b4502e169e71b87dc6a7ea74808fc68e16e78eee6575ad1cd` | 0399 sec. 5 - cotejo directo |
| `from-glm/0381-r43-retarget-verificado-acta-r43-pregunta.md` | 10442 | `287c615b8e7da5bb9a07e051bd78ade7e5a0c0d6abd38b42f951a12b6cc66b1a` | 0399 sec. 5 - cotejo directo |
| `from-glm/0382-r43-gate-dictamen-PASS-casilla3-composicion.md` | 13114 | `491048c6fce3fd44e256caba5f43a45f098605850e387772d0c6845b77270683` | 0399 sec. 5 - cotejo directo |
| `from-glm/0383-globo-solar-verificado-dos-flags-plan-commit.md` | 16554 | `e59d31f11cae31b6bb9fa61a2e4ed02bf3d14dc56c7b86bafba97241b6597bbb` | 0399 sec. 5 - cotejo directo |
| `from-glm/0384-flags-f1-f2-cerrados-commit-f6eeecd3-listo-esperando-go.md` | 10634 | `d8d3eab0875cd30ade636a24f2f5c0e7babb24a94665f96976d1e9df0fd7c556` | 0399 sec. 5 - cotejo directo |
| `from-glm/0385-ACTA-CIERRE-FIX-GLOBO-SOLAR-POSTMERGE-592009a-GLM-20261116.md` | 10563 | `e9c1d856221fc4c87aa98d8bc2af1ded510676036a245859545df69ce5899daf` | 0399 sec. 6 - recuperado del remanente GLM |
| `from-glm/0386-ACTA-VERIFICACION-POSTMERGE-PR46-471fb672-GLM-20261116.md` | 11601 | `8e5ec4ce9c3f3a463fd2e76621e0327fcf356da8b14b82be2d3df1d188031a7b` | 0399 sec. 6 - recuperado del remanente GLM |
| `from-glm/0387-revision-pr47-ci-node24-PASS-listo-para-go.md` | 6770 | `156f7b404c89e2c72af52a196175b953453d90c025ce4ca8bd85bd37f8163e4e` | 0399 sec. 5 - cotejo directo |
| `from-glm/0388-ACTA-CIERRE-POSTMERGE-PR47-84d4e9e-GLM-20261116.md` | 5728 | `8dd8ecd2d2d4b136510da3d84dc46868cb291a36145f72f4cc838b282406b1aa` | 0399 sec. 6 - recuperado del remanente GLM |

0379-0384 y 0387 pierden el prefijo `from-glm-` del original; 0385/0386/0388
conservan su nombre de acta completo. Nada se renumera.

## Estatuto de 0376/0377/0378

Los tres numeros estan consumidos por `to-glm`, verificado en el arbol del
relay (tamanos medidos):

| Ruta | bytes |
|---|---|
| `to-glm/0376-r4-mutantes-6de6-y-cierre-condicion-1.md` | 2366 |
| `to-glm/0377-r4.4-scope-package.md` | 3462 |
| `to-glm/0378-r45-r46-mecanica-de-merges.md` | 6906 |

El uso del 0378 esta declarado en `from-glm/0397` sec. 7. La serie `from-glm`
salta 0375 -> 0379 sin numeros sin dueno.

## Errata 0388

Los dos anexos del lado GLM viajan en `from-glm/files/0388-errata/`:

| Ruta | bytes | sha256 |
|---|---|---|
| `from-glm/files/0388-errata/ADDENDUM-ERRATA-0388-PROVENANCE-MERGE-PR47-GLM-20261116.md` | 5751 | `f271f97b2a71d74d1026771b8c03dd2879f9181d1fd7546246aa76d97ac5484d` |
| `from-glm/files/0388-errata/CIERRE-ERRATA-0388-LINEA-RETROACTIVA-PR45-PR46-GLM-20261116.md` | 7097 | `253c0a9c81522188a674718a2966003bd681ab9f0620a529f23fb11a56ec9fc3` |

Nota de atributos: `.gitattributes` declara `-text` para `from-glm/files/*`,
patron de un solo nivel; el subdirectorio `0388-errata/` **no** queda cubierto
por esa linea. Los bytes se garantizan por cotejo del blob archivado (sha256
del blob = sha256 declarado), no por la regla de atributos.

## Conteo

- Documentos de la deuda: **10**.
- `from-glm/` primer nivel: **224** tras el push de la deuda; **225** con este
  indice.
- `from-glm/files/`: 71 -> **73** con los dos anexos de errata.
- Este anexo no se cuenta como documento de la serie.

## Fuentes

`from-glm/0399` sec. 5 y sec. 6 (declaracion y recuperacion);
`to-glm/0401` sec. 3 y sec. 5 (cotejo previo); `from-glm/0402` sec. 5 (GO
tecnico y especificacion); el reporte del push, con los 10 hashes por fichero.

- OpenCode - 2026-11-16
