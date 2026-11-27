# OpenCode -> GLM - P10 DUMP read-only: H-distribucion CONFIRMADA; n=236; IrtamOnly(72-168h)=0; single gap 1711h; clusters Sep15 12.5h + Nov26 ~24.8h; timeline 1748h

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-27 (Madrid).

Materia: `Q5`/`P10`. Dump READ-ONLY sobre `cache/tec_*.bin` (workingdir `ionosphere-live-3d`, app parada; NO instrumentacion commiteada, sin codigo). Peticion adjudicacion `0504`. 

## Medido (read-only; `tecHist` == cache restaurado + push/save; app `tecHist`=235 de David, disco n=236)

- `n_disco_tec = 236` (~235 app). oldest `2026-09-15 05:55Z`, newest `2026-11-27 01:55Z`, `timeline_span=1748.0 h`, edad vieja `1748.7h`, reciente `40.9min`. 
- **Bandas de zona (`zoneForAge`, age vs now):**
  - `TecOnly_reciente (<72h)`: **161**
  - `IrtamOnly (72-168h)`: **0**  <== **banda media 72-168h VACIA**
  - `TecOnly_viejo (>168h)`: **75**
- Por mes `Sep=75 Nov=161`; **Sep todo el 09-15 (75 consecutivos @10min = ~12.5h denso); Nov 11-26=149 (+24.8h denso) + 11-27=12.**
- **Huecos >1h: n=1:** `Sep15 18:33 -> Nov26 01:55` **1711.4 h**. (Dentro de cada cluster, sin huecos >1h; el resto contiguo @10min.) 

## P10 adjudicacion (compuesta) - comprobado

- (i) cluster Sep ~75 ~12.5h zona vieja que anima (`TecOnly_viejo` + contiguo): **SI** (75 sep-15; borde 1736-1748h ~ fin del cluster).
- (ii) medio ~Sep16->Nov26 vacio: **SI** (unico hueco 1711h; `IrtamOnly`=0; medio sin TEC).
- (iii) cluster reciente denso ~==24h animando: **SI** (`TecOnly_reciente`=161; denso nov-26 ~24.8h + nov-27; observado `ultimas24h`).
=> **`H-distribucion` CONFIRMADA por datos; `F-parcial` cerrado-por-diseño-y-datos.** (no refutada Q3-d).

## Consistencia con diseno

- `kIrtamReplayWindowSec=168h` + `zoneForAge 72/168` + `ReplayZone` `[T-168,T-72] IRTAM-only / [T-72,T] TEC-only` + densidad + `bracketTovs` clamp. `kReplayWindowSec=86400` muerta. `kCapFrames=432` no vinculante (236<432).
- **`IrtamOnly` vacio en TEC + zona muerta `kReplayWindowSec` + banda 72-168h sin TEC** = medio estatico; anima en `TecOnly` con datos. `P9` converge ~72h rodante. 
- `n` app=235 vs disco=236 (+1 runtime). 

## Q6 (mi eleccion "lo que creas mas conveniente")

**Acepto** comportamiento actual = diseno + datos; **F-parcial cerrado; serie replay termina.** No abro slice ni mas cobertura. `P9` self-converge; reabrir SOLO si `P10` refutado. (`Q6-2` `72h TecOnly` + `backfill extent` no necesario ahora.)

## Asks `0504`

1. `P10` adjudicar (datos). 2. `H-distribucion` confirmado? `F-parcial` cerrado? 3. `P9` registrar; `kReplayWindowSec` higiene nota. 

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-27 (Madrid), lado implementador.
