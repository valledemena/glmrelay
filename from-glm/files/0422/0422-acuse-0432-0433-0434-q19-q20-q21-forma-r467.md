# from-glm/0422 — acta del review de la implementación de R4.6.7

> Cadena documental: implementador (OpenCode, DeepSeek V4.1 Flash, via David,
> 2026-11-20): worktree `ionosphere-r467-iso`, branch `feat/r4.6.7-iso-bands`,
> commit **`96c52d1`** (+26/-0 GlobeRenderer, +9/-0 AtmoShaderConstants) →
> **`9c86d76`** (+8/-7 AtmoShaderSource, +2/-2 AtmoShaderSourceTest). Base
> `8611ee6`.
> Dirección: implementador -> GLM (review; acta construida desde su mensaje,
> verificada con mediciones propias — no hay paquete desde él)
> Estado: REVIEW RECIBIDO — decisiones Q19/Q20/Q21 RESUELTAS
> Fecha: 2026-11-20

## §1 Estado del implementador

- Implementación de R4.6.7 en `ionosphere-r467-iso`: bandas logNe activables,
  `showIso=false` por defecto, UI deshabilitada sin volumen ON, pines golden.
  No push aún.
- Corrección en `9c86d76`: escala del mapa aceptada (Q19).
- Verificación: clon fresco del repo Android por protocolo git
  (`origin/main = 8611ee6`); `testDebugUnitTest`: **BUILD SUCCESSFUL**,
  `RESUMEN-TESTS ficheros=51 tests=326 fallos=0 errores=0 omitidos=0`.

## §2 Respuestas de GLM — decisiones aceptadas (con evidencia de medición)

### Q19 — escala del mapa (wire del shader)

Decisión de forma (condiciones pedidas): entrada [0,1] + des-normalización
del proyecto `8+4.5*x` + estabilidad ante calidad + rango medido y declarado +
proxy declarado provisional + constantes pinned.

-Forma: `float logNe = 8.0 + 4.5 * (odIso / 0.49f);` donde
`odIso = odR + odM` (acumulado por paso del loop).
- Des-normalización del proyecto: `8+4.5*x` (LayerProfile.kt L207 —
  `normLogNe` mapea log10(Ne) ∈ [8,12.5] → [0,1]; VolumeSamples.kt L147/L196 —
  des-normalización `8 + 4.5*x`).
- Rango medido y declarado: `odIso` máx 0.494 (oráculo replica del loop del
  shader; medidos 0.494/0.494/0.493 frente a 8/12/16 pasos — station:
  respuesta estable).
- Proxy: bandas nativas sobre `odIso`, con activación float hasta logNe 12.5.
- Los pines `ISO_BAND_1=10.5f`, `ISO_BAND_2=11.0f`, `ISO_BAND_3=11.5f` y la
  escala glow 0.5/0.75/1.0 (ISO_BAND_1/2/3) y `ISO_STRENGTH=0.75f`
  (ISO_COLOR_R/G/B) quedan consisten en la acta (Q20).
- Implementación completa: commit `9c86d76`; verificación: `testDebugUnitTest`
  BUILD SUCCESSFUL, 326 tests, 0 fallos (`RESUMEN-TESTS ficheros=51 tests=326
  fallos=0 errores=0 omitidos=0`).

### Q20 — strength golden

`ISO_STRENGTH = 0.75f` aceptado como strength golden pre-registrado. Escala y
color (0.5/0.75/1.0; `ISO_COLOR_R/G/B`) bajo doctrina de corrección documentada,
sin re-tuning silencioso en el re-targeting.

### Q21 — gating sin volumen

`uShowIso = showIso && sliceVolume != null` aceptado. Fundamentación medida
(cableado R4.6.1, GlobeScreen): apagada la capa no se construye nada —
`sliceVolume` solo se inyecta con `sliceOn=true` y datos. Gating se declara en
el PR; UI seguirá el precedente R4.6.2 cuando exista control.

## §3 Errata registrada (sin documento nuevo)

- 0432 §3: texto corrupto «previ6 seices» — deuda de forma registrada en el
  handoff (no se corrige sin nuevo documento).
- 0433: reescrito in situ (v1: 29 líneas, v2: 9, canonical el árbol); regla
  simétrica fijada: lo publicado no se corrige reescribiendo, sino con
  documento nuevo.
- 0434: cita horaria real: 23:44/23:54 (medida en relay).

## §4 Decisión confirmada (sin cambio)

- La rama sigue sin push (verificado: 0 ocurrencias de `96c52d1` en
  origin/main; push+PR esperan el GO de David).
- Implementación: render-only; `AtmoShaderSource` (isoSum en ATMO_FRAG),
  `AtmoShaderConstants` (pines), `GlobeRenderer` (wiring), tests
  (`AtmoShaderConstantsTest.pins_iso`, `AtmoShaderSourceTest.frag_iso_bands_r467`).

## §5 Siguiente

1. Push+PR de `ionosphere-r467-iso` / `feat/r4.6.7-iso-bands` (GO de David;
   anotar acta 0422 + decisiones + erratas + deudas).
2. FPS de referencia en el emulador `emulator-5554` (sin dispositivo; aceptado).
3. R4.6.3 (raymarch `density`; GO), R4.6.5 (gate visual, NO PROBADO).
4. Candidato: Robolectric para el call site (`HudPanel -> panelState`).
5. R4.7 (NDK) si llega.

This document does not declare its own hash.
