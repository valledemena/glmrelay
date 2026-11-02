# Mobile (Android) baseline — Round 0 coordination (para GLM)

Circulacion via este relay. No hay acceso a GLM (credenciales ni cuenta), por lo que GLM lee este fichero y escribe la respuesta como `from-glm/0333-mobile-r1-...md`.

## Contexto
- Proyecto desktop: ionosphere-live-3d (C++17/CMake, OpenGL 4.0).
- Proyecto web (referencia): ionosphere-live-3d-web (Next 16 + React 19 + Three.js WebGL).
- Nuevo repo movil: https://github.com/valledemena/ionosphere-live-3d-android (`docs/r0`, Issue #1 abierto; docs de baseline existen).
- Sistema operativo target: Android (David: Xiaomi Mi 10 Lite 5G, API 30, Adreno 620, 6GB; target mínimo sugerido por GLM: API 26).

## Lo que GLM ya propuso en el R0 (del archivo GLM_R0_RESPONSE)
- Kotlin nativo + Compose + renderer custom (OpenGL ES 3.1).
- Schema-first con schemas + codegen kotlinx para Android y tipos TS para web.
- Llamadas directas (sin backend web obligatorio). Web es referencia.
- Slices: R0-R6, v1 usable R1/R2.
- Degradation semantica que viene del desktop (off/degraded/failed).
- Diferir Ebro FTP hasta late slices (permiso pendiente).
- Puertas de verificacion como las del desktop: hunk-a-hunk + seam + mutantes antes del merge.
- Licencia GPL-3.

## Tarea de GLM (R1)
Responder por este mismo relay con archivos en `from-glm/0333-mobile-r1-...md` (y anexar si hace falta).

1. Arquitectura y rendering
- Confirmar OpenGL ES 3.1 y render propio (no RN/r3f, no SceneView salvo glTF).
- Propuesta de layer manager / scene graph equivalente al de C++ y web.
- Budget de memoria: textura de 5400x2700 DOWNSCALEASTCI y fallback/backoff en 2k.
- Cómo portar el volumen ionosférico (textura 3D/blending/mesh) a ES 3.1.

2. Datos y cadena de fuentes
- Endpoint contract: beans IA, ionosondes, satellites, solar image, space weather, AE, Dst, voyager, WSPR. Mirror desktop/web.
- Caching con Room/WorkManager, cadencias: foreground 5min, background 15-30min, manual refresh.
- Degradación: honest off/degraded/failed; no invented data.

3. Tests portables y contract gates
- Golden fixtures para parse (JSON Schema, web tests as spec, JUnit local).
- CI en GitHub Actions: assemble + unit + lint, smoke con emulator GL ES.
- Peticion de GLM concreta: indicar qué matriz de hardware (API 26+, 2GB RAM minimum, GPU variantes).

4. Slices (añade estimados de esfuerzo si posible)
- R0 scaffolding
- R1 renderer bootstrap + 60fps on mid-range
- R2 normal contract freeze
- R3 data + degradation
- R4 offline cold start
- R5 gates + AAB

5. Reserva de assets y texturas:
- Cost at runtime, fallback, telemetry minima.

6. Ownership y flujo OK-2:
- Verbo exacto antes de merge (hunk-a-hunk PROMISED-vs-DELIVERED, seam, mutantes).
- GLM responde; David decide merge; Beam ejecuta.

Giras recomendadas:
- `src/lib/iono` de web.
- `Ionosphere/LayerProfile` y adapters de C++.
- CREDITS/de offensive-defense license pattern.

A la espera de GLM.
