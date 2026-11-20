# Acta 0430 - GLM: dictamen FAVORABLE R4.6.3 / PR #57 (head 9b801b4) - fix R1 innerRadius verificado

- Fecha: 2026-11-21 (UTC)
- Emisor: GLM (revisor del slice)
- Repositorio: valledemena/ionosphere-live-3d-android
- Slice: R4.6.3 raymarch del volumen Ne(h) density + Chapman
- Referencias: acta 0429 (dictamen condicionado, head f306730), ack 0437, PR #57, CI run 44823314882

## 1. Antecedentes

El acta 0429 condiciono el cierre del slice R4.6.3 al fix R1: el radio interior
del proxy del volumen debe calcularse como volumeInnerRadius(VOL_ALT_MIN_KM),
espejo del C++ VolumeRenderer.cpp (innerR = 1 + (altMinKm_/6371)*explode_,
explode_ = 1.0), de forma que el shader mapee altNorm = (r - uInnerR)/(uOuterR -
uInnerR) en [0,1] = alt 60..500 km sin desplazamiento vertical (pines G7c_10/11/12).

## 2. Verificacion realizada (2026-11-21, via API publica de GitHub)

1. PR #57: state=open, mergeable=true, merged=false, head sha
   9b801b4d7db14b48fc1102f36305587ef67d10ef, rama feat/r4.6.3-density-chapman,
   base main, 12 ficheros, +1439/-3. Coincide con el relay de Deepseek.
2. Fix R1 presente en el head (lectura directa del codigo):
   - VolumeLayerRenderer.kt L80: val outerRadius: Float = volumeOuterRadius(VOL_ALT_MAX_KM)
   - VolumeLayerRenderer.kt L89: val innerRadius: Float = volumeInnerRadius(VOL_ALT_MIN_KM)
   - VolumeLayerRenderer.kt L96-97: uInnerR/uOuterR (locations);
     L223-224: glUniform1f(uInnerR, innerRadius) / glUniform1f(uOuterR, outerRadius)
   - VolumeLayerPlan.kt L91: const val PLANET_R_KM = 6371.0
   - VolumeLayerPlan.kt L94-95: volumeOuterRadius(altMaxKm) = PLANET_R + altMaxKm/6371
   - VolumeLayerPlan.kt L103-104: volumeInnerRadius(altMinKm) = PLANET_R + altMinKm/6371
   - Doc comments del diff citan el espejo C++ y el mapeo altNorm [0,1] =
     alt 60..500 km (G7c_10).
3. Espejo C++ verificado en ionosphere-live-3d (master),
   src/Ionosphere/VolumeRenderer.cpp:
   - L256: float outerR = 1.0f + (altMaxKm_ / 6371.0f) * explode_;
   - L257: float innerR = 1.0f + (altMinKm_ / 6371.0f) * explode_;
   - L86 (shader): float altNorm = clamp((r - u_innerR)/(u_outerR - u_innerR),
     0.0, 1.0);
   La formula coincide exactamente con la implementacion Kotlin.
4. CI del head: run 44823314882 (event pull_request, head 9b801b4)
   completed/success, 3/3 jobs success: assembleDebug (136589457552),
   unitTest (136589457838), lint (136589458062).
5. Aritmetica: innerRadius = 1 + 60/6371 = 1.00941767383456 (aprox 1.00942);
   outerRadius = 1 + 500/6371 = 1.07848061528802 (aprox 1.07848).

## 3. Erratas y observaciones (no bloqueantes)

1. El relay de Deepseek cita "log del job 136531605890" para el run 44823314882;
   ese job no existe en dicho run. Los jobs reales del head son 136589457552 /
   136589457838 / 136589458062. El id citado pertenece presumiblemente al run
   anterior (44806450830, head f306730). El exito del job unitTest del head
   9b801b4 queda verificado via API.
2. Deriva de linea en el espejo C++: los comentarios Kotlin citan
   VolumeRenderer.cpp:256/257; en master actual del C++ las lineas son 231/232
   (formula identica). Actualizar la cita en commit de documentacion posterior;
   no requiere re-review.
3. Literales a consignar al archivar (verificacion de cortesia, NO condicionan
   el dictamen; estan corroborados por doc comments, tests G7c y relay):
   - VOL_ALT_MIN_KM = 60.0 (core/iono/DensityVolume.kt, linea 15)
   - AtmoShaderConstants.PLANET_R = 1.0f (render/AtmoShaderConstants.kt, linea 9)
   - Re-verificar aritmetica con: python3 -c "print(1+60/6371, 1+500/6371)"

## 4. Dictamen

FAVORABLE. El fix R1 exigido en el acta 0429 esta implementado en el head
9b801b4d7db14b48fc1102f36305587ef67d10ef, verificado por lectura directa del
codigo y de su espejo C++, con CI 3/3 verde en el head. Quedan levantadas las
condiciones del acta 0429 para el cierre del slice R4.6.3.

## 5. Condiciones de merge

- Merge con commit de merge (sin squash); rama feat/r4.6.3-density-chapman
  conservada.
- Pin del head: --match-head-commit 9b801b4d7db14b48fc1102f36305587ef67d10ef.
- Go de David ya dado.
- Comando: gh pr merge 57 --repo valledemena/ionosphere-live-3d-android
  --merge --match-head-commit 9b801b4d7db14b48fc1102f36305587ef67d10ef

## 6. Pendientes y siguiente slice

- Archivar esta acta como
  from-glm/0430-dictamen-favorable-r463-pr57-9b801b4-r1-innerradius.md
  (ASCII, CR=0) y consignar en el archivo las citas literales de
  VOL_ALT_MIN_KM y AtmoShaderConstants.PLANET_R (fichero + linea exactos)
  mas la aritmetica con python3.
- R4.6.5: gate visual con dispositivo fisico (NO PROBADO).
