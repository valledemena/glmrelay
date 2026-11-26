# OpenCode -> GLM - evidencia runtime: log sin firmas GloTEC (nueva pista)

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: David pidio verificar el binario, arrancar la app y tomar
capturas del provider status a lo largo del tiempo mientras el
copiaba el log. Te entrego la evidencia cruda para tu dictamen.

## 1. Binario verificado

- Tres ejecutables: raiz 2026-11-22 23:18 (pre-DW, sha ab178755),
  dw9 2026-11-25 14:19 (c7002ffd), dw10 2026-11-25 17:16
  (4b1ada55). Ninguno tiene metadatos FileVersion/ProductVersion.
- Arrancado el de **dw10** (`4b1ada55`, cwd=
  ionosphere-live-3d para usar la MISMA cache de 111 ficheros),
  PID 3148. Codigo de produccion identico a master cd65a7b.
- Importante: el "Build 20.19.15.5171" de la captura es la version
  del driver OpenGL de Intel (linea "OpenGL 4.6.0 - Build ..."),
  NO una version del binario de la app. No sirve para datar el
  ejecutable de David.

## 2. Capturas (t+0, 2, 4, 6 min; panel abierto)

Estado estable en las cuatro:
- GIOTEC: **off** (sin reason, sin datos)
- GIRO: degraded (fetching), 2/50 -> 10/50 st, hist 5,9 -> 19,1 h,
  backoff 2 -> 8 st, retry 20 -> 17 min
- IRTAM: degraded, "gate: <15 s desde request lgdc previo"
- Indices/Solar wind/Kp-HF/Xray/SDO/DIAS/EBRO/WSPR/ENLIL/NWS: ok
Ficheros: shot0.png .. shot4.png en AppData/Local/Temp/opencode/.

## 3. Hallazgo nuevo: log sin firmas GloTEC

`app_runtime.log` (12 311 B, 153 lineas) contiene SOLO:
- `[OK] SolarWindRiver initialized`, framebuffer MSAA fallback,
  `[Ebro]`, y mucho trafico `[LGDC ...] launch/getbest/gate-consult`.
NO contiene NI UNA de estas cadenas, que existen en el codigo:
- `[GloTecAdapter] Index OK: N frames` (GloTecAdapter.cpp:264)
- `[GloTecAdapter] Index failed:` (:229)
- `[App] TEC cache: N restored` (App.cpp:3616)
- `[App] History preload:` (:1224)
- `[App] Periodic backfill:` (:1293)
Con 6 min de ejecucion y la fila GIOTEC en off, el worker GloTEC
no produce ninguna salida observable. Esto es DISTINTO de tu E2
(indice vacio con "Index OK: 0 frames"): aqui ni siquiera aparece
"Index OK". Posibles lecturas: (a) el worker no arranca, (b) stdout
buffereado y no volcado, (c) el launch del indice esta mas adelante
en la secuencia y tarda >6 min, (d) la ruta de cache no se lee.

## 4. Peticion

Dictamina que significa la ausencia total de firmas GloTEC y si
cambia el alcance minimo A+B del acta 0491. David va a copiar su
log; si el suyo muestra las mismas firmas ausentes, tenemos la
causa comun. Sin codigo tocado.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
