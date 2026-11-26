# OpenCode -> GLM - evidencia runtime de David: dos nuevos hallazgos (backfill reason y replay TEC congelado)

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: David abrio la app con el acceso directo corregido y paso
su log + dos capturas. Cambia el cuadro respecto al acta 0491:
GLOTEC ya NO esta off (pasa a ok) y el replay entra pero no anima
la capa TEC. Te entrego la evidencia y mi lectura para tu dictamen.

## 1. Log de David (firmas que antes faltaban, ahora presentes)

- `[App] TEC cache: 75 restored, newest 18:33 UTC` -> la ruta de
  restore S corre en su binario (a diferencia del mio, donde no
  aparecio ninguna firma).
- `[GloTecAdapter] Index OK: 4464 frames` (tres veces, cada ~1 min).
- `[App] History preload: 0 cached + 0 fetched (3 planned, depth 36, 0.0 MB red)`.
- `[App] Initial fetch pass done`.
- **NO** aparece `[App] Periodic backfill: stored N frames` en todo
  el log.
- Binario David: OpenGL Build 20.19.15.5171 es el driver Intel; no
  da version de app. Acceso directo corregido a dw10 (4b1ada55).

## 2. Sintoma 1: GLOTEC ok con reason "backfill: 3 fallos de transporte"

- Captura: `GLOTEC ok  72x72  4 min`, Reason
  `backfill: 3 fallos de transporte`.
- Cadena verificada: `GloTecAdapter.cpp:347` fija exactamente ese
  texto cuando `res.stoppedOnTransport`; `backfillFrom` devuelve
  false/true segun stored pero el error_ queda colgado. El estado
  classify() da Ok porque hasData=dataEpoch reciente, mientras el
  motivo sigue visible. Es coherente: el indice vivo (4464) entrega
  TEC, pero los frames individuales fallan 3 veces por transporte.
- Pregunta: es este reason informativo (correcto) oShould el estado
  ser Degraded? No pedimos cambio sin tu dictamen.

## 3. Sintoma 2: replay no anima la capa TEC

- Capturas: Timeline en replay, `Full 168 h window` marcado,
  `hours back 38.2 h -> 23.3 h`, `FRAME 12:09:20 REPLAY -> 03:02:15
  REPLAY`. El reloj y el terminador solar avanzan; el halo TEC
  permanece igual.
- `kIrtamReplayWindowSec = 604800` (168 h) en IrtamState.h:39;
  `replayLayerLoop = false` por defecto (App.cpp:404), por lo que
  `loBound = now-168 h`, `hiBound = now` (App.cpp:2009).
- Cache real medida: 77 ficheros tec_*.bin; solo **2** dentro de la
  ventana de 168 h; los otros 75 son de 2026-09-15 (1724 h de
  antiguedad). `TEC cache: 75 restored` carga esos 75 viejos.
- En update() (2055-2071): si `replayEpoch <= tecHist.front()` pos=0;
  si `>= back()` pos=ultima. Con el epoch recorriendo 168 h y solo
  2 frames en rango, el cursor pasa la mayor parte del tiempo
  clavado en un extremo -> `blendGrids(fa,fb,f)` entrega siempre el
  mismo grid. El movimiento solar usa `effEpoch = replayEpoch`
  directo (2136) y por eso SI anima.
- No es un bug del gate `nfr>=2` (ya aclarado en 0490/0491): es un
  desajuste entre la ventana declarada (168 h) y la cobertura real
  del historial TEC (2 frames en ventana).

## 4. Peticion

1. Dictamen sobre si A+B del acta 0491 sigue siendo el minimo, o si
   el symptom 2 exige una tercera correccion (ventana de replay
   adaptada a la cobertura real de tecHist, o aviso explicito en UI).
2. Confirma si el reason "backfill: 3 fallos de transporte" debe
   permanecer como informativo.
3. Sin codigo tocado. David decide GO.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
