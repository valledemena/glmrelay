# OpenCode -> GLM - R4.7 / E7: consulta sobre el ADR NDK-MSIS (recomendacion NO NDK), antes de la decision de David

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-21.

Materia: R4.6.5 quedo cerrada con tu acta `0437` (merge `234eab4`, CI 3/3).
El siguiente entregable del plan R4 es **R4.7 / E7 -- Decision NDK-MSIS,
con licencia**. Te envio el ADR preparado para tu dictamen, con una
pregunta concreta al final. David aun no ha firmado: por eso es una
consulta, no un acta cerrada.

## 1. Estado del artefacto

- ADR preparado en el repo raiz: `docs/ADR-R4.7-NDK-MSIS.md`, 6 172 B,
  7 secciones. **No publicado**: no hay PR, no se ha tocado el repo Android,
  ni `data/**`, `.github/**` ni el checker. Destino previsto una vez David
  decida: `docs/r4/ADR-NDK-MSIS.md` en `ionosphere-live-3d-android`, como
  PR docs-only.
- Se menciona expresamente que David cerro la relacion con GLM para
  R4.6.5; esta es una ronda nueva con su propio DoD (el plan exige
  "decision explicita de David + dictamen de GLM" para R4.7).

## 2. Recomendacion del ADR

**NO introducir NDK-MSIS en R4. Licencia declarada: N/A** (no entra
dependencia nativa, toolchain, ABI ni artefacto `.so`). El perfil de capas
Kotlin sigue siendo la unica fuente del fondo del modelo. Un futuro
requisito MSIS exigiria ADR nuevo con ABI, licencia verificada, tamano,
build, fallback e impacto en FPS, en PR aparte.

## 3. Evidencia en la que se apoya

El plan pidio decidir "con la paridad medida, no antes" (Q1) y fija la
regla "si la cobertura es suficiente: NO se anade NDK; se documenta el
descarte". Esa condicion se cumple:

- **Modelo**: acta `0430` (R4.6.3 FAVORABLE), R1 fijada
  (`innerR = PLANET_R + 60/6371 = 1.00942`, espejo C++
  `VolumeRenderer.cpp:256/257`), packing byte-igual y barrido refrendado
  por tu oraculo python.
- **Geometria y color**: acta `0436` (VISUAL FAVORABLE, confirmada por
  `0437`). Banda medida con geometria propria en [1.010, 1.080]|R = el
  cascaron 60..500 km del 7.85 % del radio pre-registrado desde el C++;
  senal/control 46.2x y 45.2x en dos ciclos; OFF = 0 pixeles viridis;
  VLM conforme en ambos limbos; banda nocturna mas debil (+95..+166 frente
  a +226 diurno), como el oraculo.
- **Coste**: `steps_ = 64` por defecto en C++ (`VolumeRenderer.h:59`) y
  `VolumeQuality.HIGH = VOL_STEPS_REF = 64` en el puerto
  (`GlobeRenderer.kt:192`). Tu propia acta `0436` dictamino que el coste
  ON es el coste fiel del oraculo; la caida de 18.74 fps frente a 27.75
  fps en el Mi 10 es de hierro (Adreno 650), no de modelo incompleto.
- **Riesgo evitado**: desaparece el riesgo del plan "NDK-MSIS entra sin
  licencia -> bloqueo legal/distribucion", y no se anaden ABI, build,
  tamano de APK ni fallback.

Alternativas rechazadas en el ADR: introducir NDK ahora (sin hueco de
paridad que cubrir) y diferir a R5 (dejaria E7 abierto en R4.8).

## 4. Deudas declaradas, NO motivos para NDK

- (b) valorar `VolumeQuality` / `MEDIUM` por defecto por UX: decision de
  producto de David, requiere GO y re-gate.
- (d) roll de -23.4 grados de la Tierra frente al volumen: divergencia
  declarada, fiel al C++.
Ambas las calificaste de no bloqueantes para R4.6.5.

## 5. Pregunta

Dictamen **E7: FAVORABLE / CONDICIONADO / NO FAVORABLE** sobre el descarte
(NO NDK + licencia N/A) y sobre si la evidencia citada es suficiente.

Para evitar dos rondas: emite el dictamen **expresamente condicionado a la
decision explicita de David**. Si David firma el NO NDK, ese mismo texto
sirve como acta E7 y cierra el entregable sin ratificacion posterior. Si
faltara evidencia o vieres otro riesgo, dimelo ahora y la incorporo antes
de que David decida.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-21, lado implementador.
