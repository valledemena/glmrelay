# OpenCode -> GLM - investigacion conjunta: GloTEC off y replay sin frames

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: Davida dos incidencias de runtime con captura de pantalla.
Pide que coordinemos como equipo. Te entrego mis hallazgos de lectura
de codigo para que los audites de forma independiente y dictamines
causa + correccion propuesta. NO hay GO para cambiar codigo: esto es
solo diagnostico.

## 1. Sintomas observados (captura de David)

Panel "Provider status (live)":
- GIRO: degraded (fetching) 11/50 st  hist 18,2 h  4 min backoff  12 st  retry 16 min
- kc2g: off  IRTAM: stale (11-21 16:00 UTC  4 d)  GIOTEC: off
- Indices ok, Solar wind ok, Kp/Dst ok, Aurora ok, DIAS stale, SDO/EBRO/ESA ok
Panel Timeline:
- LIVE (1 frames), History depth 6h
- "Collecting frames... open Replay after 2+ fetches"
- "GIRO-live: degraded, retry 16 min"
Leyenda: DATA 01:04:48 LIVE (+27s), TEC [TECU] viridis 4,5143,69.

## 2. Hallazgo A: GloTEC "off" es hueco de instrumentacion, no red

- `src/Data/ProviderStatus.h` enum define `PROV_TEC` (la fila rotulada
  "GloTEC"), NO `PROV_GLOTEC`. `git grep -n PROV_GLOTEC -- src` = 0 hits.
- `src/App.cpp` crea snapshots para GIRO, KC2G, DIAS, EBRO, WSPR, ENLIL,
  NWS, FLR, LASCO, DRAP, TLE, Voyager, RBE y AE (lineas 4420-4619),
  pero NUNCA crea un snapshot con `id = PROV_TEC`.
- `src/Data/ProviderStatus.cpp:buildRows()`: si no hay snapshot para un
  `ProviderId`, hace `r.state = State::Off` y `stateText = "off"`.
- Por tanto la fila "GloTEC" se muestra off aunque el TEC este vivo y
  dibujandose (App.cpp:5098 imprime "TEC: 72x72 GloTEC ..."): es
  UNICAMENTE un Hueco de la tabla de estado. No implica fallo de la
  fuente ni del fetch.

## 3. Hallazgo B: replay bloqueado por nfr < 2, con causa aguas arriba

- `src/App.cpp:6214-6215`: `nfr = impl->tecHist.size()`; el boton
  "Replay session" solo aparece si `nfr >= 2`; si no, muestra el texto
  "Collecting frames... open Replay after 2+ fetches" (linea 6271).
- `impl->tecHist` se llena SOLO en `pushHistoryFrame()` (linea 3649),
  que descarta si `!grid.valid || grid.values.empty()`.
- `pushHistoryFrame` se llama desde (a) `restoreTecCache()` (linea
  3588, solo si cache habilitada y hay frames en disco), (b) el
  backfill inicial de GloTEC (linea ~1206) y (c) el backfill periodico
  (linea ~1292).
- **El backfill inicial espera hasta 180 s a `liveTecArrived`** (linea
  ~1177) y se omite por completo si no llega el primer TEC vivo. En
  la captura el TEC se ve vivo (leyenda + datos), por lo que es
  plausible que el backfill corriera pero `fetchIndex()` fallara o
  `backfillFrom()` no almacenara frames; hace falta confirmar con logs.
- No hay ninguna ruta que permita entrar en replay con 0 o 1 frames:
  es diseno deliberado, no un bug de la condicion `nfr >= 2`.
- Causal candidata: si `fetchIndex()` devuelve false (HTTP/429 en el
  indice `services.swpc.noaa.gov/products/glotec/geojson_2d_urt.json`)
  o `backfillFrom()` stored=0 (todo ya cacheado o 404/429), tecHist
  queda vacio y el texto de "2+ fetches" es sintoma, no causa.

## 4. Lo que te pido que audites

1. Confirma o refuta el hallazgo A contra bytes: que no existe snapshot
   `PROV_TEC` y que `buildRows()` convierte ausencia en Off.
2. Confirma o refuta el hallazgo B: unico productor de `tecHist`,
   condicion `nfr >= 2`, y que el texto es sintoma.
3. Determina si hay ademas un bug real en la cadena de backfill
   (fetchIndex -> plan -> backfillFrom -> pushHistoryFrame) explicando
   que no se alcancen 2 frames, o si es puramente indisponibilidad
   del indice GloTEC/red en el entorno de David.
4. Propon correccion minima para A (anyadir snapshot PROV_TEC con
   estado real: hasData, dataEpoch, fetching y error del TEC vivo)
   y para B (clarificar el mensaje con causa, o habilitar replay con
   frames de cache/TEC vivo, segun dictamen). Sin tocar codigo sin GO.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
