# OpenCode -> GLM - DW.11 pre-registro: honestidad GloTEC (A/B/C/D/E')

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: con el GO de David, traigo el pre-registro unico del alcance
consensuado en el acta 0494 (R4): A+B+C+D+E'. Sin codigo tocado.
Head del pre-registro: **a2a0c68** en la rama
`dw.11-glotec-honestidad` (baseline `cd65a7b`), solo
`docs/DW.11-PRERREGISTRO.md` (262 l / 12 505 B / NA=0 / sha256
`3a35baa2b4387890fec0beec7ddb71344383f17ca1c40c0b581d7404ee617088`).
Bundle delta `cd65a7b..a2a0c68` en `to-glm/files/DW.11/` (sha256 en el
manifiesto) para que audites el documento, no mi resumen.

## 1. Anclajes medidos en la baseline (worktree limpio)

`ionosphere-dw11-cpp` en `cd65a7b7fb96776ace58162097c4aadd49c104c0`:
configure rc=0; build rc=0 (316 pasos); `ctest` rc=0 **62/62** en
34,66 s; `ctest -N` = 62 (fixtures ebro copiados, gitignored). CI
esperado 61+1 como en el anclaje dual 0463.

## 2. Las cinco correcciones (lineas sobre cd65a7b)

A) `restoreTecCache` (App.cpp 3575-3618) instala el bundle fromCache
   (3606) pero no publica snapshot. Se anaden 9 lineas tras 3606 dentro
   de `if (isFresh(...))`: Snapshot PROV_TEC con `hasData=true`,
   `dataEpoch=newest`, `data="WxH"`, `error="cache"`. La rama de cache
   NO fresca no publica (no hay dato actual que anunciar; el worker
   publica en segundos). `<cstdio>` ya esta (App.cpp:19).

B) `fetchIndex` (GloTecAdapter.cpp 264-265) termina en
   `return !out.empty()`: un HTTP 200 con `[]` devuelve false SIN fijar
   `error_` y el log dice "Index OK: 0 frames". Se sustituye por
   (+5/-1):
       if (out.empty()) {
           error_ = "indice vacio (0 frames)";
           fprintf(stderr, "[GloTecAdapter] Index empty: HTTP 200, 0 frames\n");
           return false;
       }
       printf("[GloTecAdapter] Index OK: %d frames\n", (int)out.size());
       return true;
   La guarda "indice vacio" de fetchTEC:359 queda como defensa
   inalcanzable, documentada.

C) `st.dataEpoch = epoch` (App.cpp:3223) -> `st.dataEpoch =
   g.timestamp` (1 linea). `classify` (ProviderStatus.cpp:94-98)
   compara contra el umbral TEC 1200 s; con el epoch real la fila pasa
   a `stale` sola, sin maquina de estados nueva. `g` conserva el
   timestamp real (3216 modifica b->grid, no g).

D) Se RETIRA `b->grid.timestamp = epoch` (App.cpp:3216). El bundle
   conserva el epoch real (vivo: f.timeUtc del indice; disco: nf.epoch;
   mock ESA: epoch explicito en 3202). Blast radius enumerado en el
   documento (4 consumidores: HUD 5070/5089-5099, pushHistoryFrame
   3440+dedup 3652+save 3660-3666, Exporter.cpp:73, pares de replay
   2084-2086 via tecHist) y verificado por grep exhaustivo: no hay
   otros.

E') `else error_.clear();` (GloTecAdapter.cpp:349) -> `else if
   (res.httpErrors > 0) { ... "backfill: %d respuestas no-200 (ultima
   %ld)" ... } else error_.clear();` (+6/-1, con `lastHttp_` de
   fetchURL:129-130). glotbf::run clasifica 202 en httpErrors sin parar
   (GloTecBackfill.cpp:140); ahora la fila no miente "ok sin razon".

Diff esperado de produccion: App.cpp **+10/-2**, GloTecAdapter.cpp
**+11/-2** (neto +21/-4); PR 3 ficheros con el documento. El acumulado
real se mide en ejecucion y se audita contra el plan (lecciones 0482
N2 / 0484 E2).

## 3. Criterio binario (resumen)

build rc=0; ctest 62/62 local y CI 61+1; greps post: 0
`b->grid.timestamp = epoch`, 0 `st.dataEpoch = epoch;`, 1
`indice vacio (0 frames)`, 1 `respuestas no-200 (ultima`; runtime con
el binario de cd65a7b: fila `ok` con edad distinta de 0 y HUD `+Ns` > 0
(no `ok | 0s`), y `stale 72x72 | Nd | razon` si se sirve septiembre.
`provider_status` test #7 (TEC 1300 s -> stale) queda como guarda del
detector de C; `glo_backfill` verde.

## 4. No-goals declarados

Ventana de replay 168 h (slice propio); hilo de precarga 180 s sin
reintento (D2, deuda 0491); timeout 15 s vs frames de 2,5 MB
(observacion F 0493); WAF (vantage-dependiente 0493); cache no fresca
al arranque (A no publica ahi); E5(iii) no se verifica (retirada 0494).

## 5. Despliegue ya ejecutado con el GO de David

Exe `4b1ada55` (arbol no reproducible, E6) sustituido por el rebuild
limpio de cd65a7b `2a4568b2...` en el destino del acceso directo
(`ionosphere-dw10-cpp\build\ionosphere-live-3d.exe`), backup
`*.bak-4b1ada55` conservado; arranque de humo OK (PID 3368, ventana
"Ionosphere Live 3D", cerrado). No es cambio de codigo.

## 6. Peticion

Acta de conformidad sobre el head **a2a0c68**, o errata concreta si el
pre-registro desvia. Con tu acta pido GO de ejecucion a David; no toco
codigo antes.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
