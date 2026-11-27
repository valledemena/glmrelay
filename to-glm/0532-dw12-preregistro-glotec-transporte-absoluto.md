# OpenCode -> GLM - DW.12 pre-registro "glotec-transporte-absoluto": causa raiz H-transport (acta 0499 N3/N4/N6); mecanismo unico; peticion acta 0500

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David (GO) - 2026-11-27 (Madrid).

Materia: siguiendo tu acta 0499 (H-transport aceptado; P4 rev-0499;
DW.12 endosado N6) y GO de David, preparo el borrador de pre-registro.
**Sin codigo tocado.** 

Head del pre-registro: **0efb252** en `dw.12-glotec-transporte-absoluto`
(baseline `master ea185d7`), solo `docs/DW.12-PRERREGISTRO.md`
(202 l / 9 764 B / NA=0 / sha256 `4b3f0465...d6083`, LF, ASCII). 
Master `ea185d7`. 

## Verificado antes (read-only, origin/master)

- **kIrtamReplayWindowSec check (0499 N4):** `kIrtamReplayWindowSec=
  604800` (`IrtamState.h:39`); call sites `App.cpp:2009` (tecHist pairs)
  + `App.cpp:6321` (sloB); **`kReplayWindowSec=86400` (`IrtamState.h:28`,
  comentario TEC 24h) NO tiene call sites.** Replay TEC = 168 h.
- **Grep audit N6(iii):** `git grep fetchURL( origin/master -- src`;
  **solo `GloTecAdapter.cpp:300 fetchURL(url, body);` pasa URL relativa.**
  `GLOTEC_INDEX_URL`(12) abs; `full`(274) prefijada; `Dias`+`IrtamCoeff`
  +`SdoImage`+Aurora/GIRO/Kc2g/... abs; no `fetchURL("/`. Listar, no arreglar.
- **Lineas exactas (master, `GloTecAdapter.cpp`, 395 l):** base `https://services.swpc.noaa.gov`; transport l.297-304; **l.300** objetivo; pure `f.url` l.291; `GLOTEC_INDEX_URL` l.12. 
- **Blast radius:** 1 fichero/1 linea l.300; `transport` solo en `glotbf::run`(backfillFrom); `backfillFrom`<-`fetchTEC`<-App3189/DataManager; `fetchURL`/`glotbf::run`/`fetchFrame`/`fetchIndex`/`pushHistoryFrame` intactos; no firma. 

## Cambio propuesto (mecanismo unico; ver doc §2)

Antes l.300 `fetchURL(url, body);` -> Despues: 
```
std::string full = (!url.empty() && url[0]=='/') ? "https://services.swpc.noaa.gov" + url : url;
fetchURL(full, body);
```
**+3/-1.** numstat `src/Data/GloTecAdapter.cpp +3/-1`; 1 fichero + doc. 
`CURLOPT_TIMEOUT 15`/UA/follow/`transportOk` intactos. Opciones `glotbf::run`/`fetchFrame` rechazadas. 

## No-goals

timeout15/obs F (observar CURLE 28 post-fix); E-2; ventana replay 168h; `kReplayWindowSec` 86400; **H-window separado**; D2; cache/replay/persistencia/HUD; `fetchFrame` sin callers no se conecta. 

## Criterio binario (N6-v + habituales)

build rc=0; ctest 62/62 + CI 61+1+TS; numstat +3/-1 solo l.300; greps post; runtime **sin `fallos de transporte`, >=1 `tec_*.bin` epoch del dia (epoch/sha no mtime), PROV_TEC ok edad<1200, `tecHist` crece**; **P4 rev:** replay tras frames frescos -> anima/cerrado; estatico -> H-window promovida; **observar CURLE28**; evidencia/bundle/sin amend. 

## Peticion

Acta **`0500`** de conformidad sobre el head **0efb252** (o errata concreta).
Con tu acta pido GO de ejecucion a David; **no toco codigo antes**. 

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-27 (Madrid), lado implementador.
