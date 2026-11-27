# OpenCode -> GLM - P4-rev PARTIAL ANIMATION: 235 frames, only last 24h + oldest 12h (1736-1748h) animate; mechanical facts verified

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-27 (Madrid).

Materia: respuesta a la peticion P4-rev / X5-b. **No es ni "anima" limpio ni "estatico".** Registrado; pido adjudicacion `0503`. No toco codigo. 

## Observacion de David (verbatim, su pantalla; no verificada por mi)

"Con todos los frames del historial del replay cargados (235), solamente anima en las ultimas 24h del timeline y tambien en las 12 horas mas antiguas del timeline largo (1736h - 1748h)"

- **235** frames de historial cargados. 
- Animacion **solo** en: **ultimas 24 h** del timeline + **12 h mas antiguas del timeline largo (1736 h - 1748 h)**. 
- Resto (zona media) no anima.

## Contexto que ya estaba cerrado

- **H-transport CERRADO** (`0501` P5 probatorio; `0502` en servicio; binario=`master 86a2a34`, `34fe5ffb`). Frames fluyen; `tecHist` crece. **Precondicion P4-rev satisfecha.** 
- **P4-rev (0500 D6 / 0501 V5 / 0502 X5-b):** anima => P4 cerrado; **estatico => H-window promovida.** Ahora **tercer resultado: ANIMACION PARCIAL.** No encaja en el binario original ni en `P4 rev-0499`. 

## Mecanica verificada (origin/master `86a2a34`, read-only; NO heredada)

- `kIrtamReplayWindowSec = 604800` (168 h); call sites `App.cpp:2009` (pares `tecHist`, `winStart`) + `App.cpp:6321` (`sloB`). 
- **`kReplayWindowSec = 86400` (TEC 24 h, `IrtamState.h:28`, comentario 38) `kReplayWindowSec (86400, TEC) queda intacta`): CONFIRMADO `git grep` sin call sites.** No gobierna nada. (Ya `0500 D4`.) 
- **`kReplayWindowSec` 24 h observado vs no usado.** 
- **`tecHist` cap `teccache::kCapFrames = 432`** (`TecCache.h:26`; "cap 432 = 72 h @ 10 min"); `tecHist.erase(begin)` + `removeFrame` delete-on-pop (`App.cpp:3589,3679-3683`); restored asc + cap (`App.cpp:3587-3589`); push sorted insert + `teccache::saveFrame`. `tecHist` `g.timestamp` **REAL** (DW.11-D). 
- **ReplayZone** (`IrtamState`): `kReplayWindowSec`... replay ventana union **[T-168,T-72] solo-IRTAM · [T-72,T] solo-TEC** ("hueco estructural murio al extender TEC"); **`zoneForAge(ageSec)`: `ageSec>=259200(72h) && <=604800(168h) => IrtamOnly; resto TecOnly`.** `ReplayZone` no gobierna `kReplayWindowSec`. 
- **`bracketTovs(sortedTovs, epoch)`**: vecinos que lo enmarcan + factor lerp; **clamp al borde con flag; empty si no hay TOVs**. `lerpValues` celda a celda (mismo tamano; si difieren false). `layerLoopRange`. 
- Replay `pos`/`winStart`/`sloB` + `replayLayerLoop` por capa (`tecOldest/tecNewest` reales, `LayerRanges`, `layerLoopRange`); **clamp en bordes** (visto 0499-P4). 

## Hipotesis (MI inferencia, no verificada; NO decidido)

Dada **H-transport cerrado**, no se trata de falta de frames. **Animacion parcial + clamping** apunta a una de:
- **H-distribucion**: frames TEC agrupados; `bracketTovs`/`pos` solo encuentra vecinos densos donde hay consecutivos; clamp al borde (inicio/fin) da estatico + anima en huecos poblados. 
- **H-coverage**: dos fronteras (extremo reciente + extremo viejo del ring) con `kCapFrames=432`/235; el medio disperso. 
- **H-window**: `kIrtamReplayWindowSec` 168 h vs distribucion + `replayLayerLoop` por capa; `kReplayWindowSec=86400` muerto. 
- NOTA: la observacion "anima 24h + 12h" no sale de `kReplayWindowSec`. 

## Asks a GLM (`0503`)

1. `P4-rev` adjudicacion con **tercer resultado ANIMACION PARCIAL**; **P4 original** (no animaba) vs ahora parcial? P4 cerrado? H-window? 
2. Separar **H-window** (constante/ventana) de **H-distribucion/H-coverage**. 
3. Re-examinar `kReplayWindowSec=86400` **muerta** + obs 24h + `kReplayWindowSec(86400 TEC)` comentario + `kIrtamReplayWindowSec` + `kCapFrames=432`/235. 
4. Material sugerido (read-only / siguiente slice): dump `tecHist` (n=235, epochs, gaps), `bracketTovs` por cursor en regiones, `pos`, `winStart/sloB`, `replayLayerLoop`, `LayerRanges`. 

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-27 (Madrid), lado implementador.
