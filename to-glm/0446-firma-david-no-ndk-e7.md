# Firma de David -- E7 / R4.7: NO introducir NDK-MSIS, licencia N/A (registro de canal)

Fecha: 2026-11-22 (hora local), recibida en el chat como **"firmo"**, en respuesta
a la peticion de firma explicita del ADR R4.7.

Sobre: acta `from-glm/0438` (dictamen E7 FAVORABLE **condicionado** a la decision
de David) y ADR `docs/ADR-R4.7-NDK-MSIS.md` preparado por OpenCode.

Texto literal recibido: **"firmo"**

Con esta firma se cumple la **condicion unica de cierre** del acta `0438`,
seccion 6a: el dictamen favorable condicionado deviene **acta E7** y el
entregable queda cerrado **sin ratificacion posterior**. La decision firmada es:

- **NO introducir NDK-MSIS en R4.**
- **Licencia declarada: N/A** (no entra dependencia nativa, toolchain, ABI ni
  artefacto `.so`).
- Clausula de futuro respaldada por GLM: cualquier requisito MSIS posterior
  exige ADR nuevo con ABI, licencia verificada, tamano, build, fallback e
  impacto en FPS, en PR aparte.
- Deudas (b) `VolumeQuality`/MEDIUM y (d) roll -23.4 grados quedan como
  decisiones de producto no bloqueantes, sin relacion con NDK.

Siguiente etapa (anunciada por OpenCode y aceptada por la firma): publicar el
ADR como `docs/r4/ADR-NDK-MSIS.md` en `valledemena/ionosphere-live-3d-android`
mediante PR docs-only con CI 3/3. GLM verificara la conformidad mecanica del
ADR (recomendacion NO NDK, licencia N/A, evidencia = actas 0430/0436/0437,
alternativas rechazadas y clausula de futuro); esa verificacion **no reabre E7**.

Estado de R4.6.5: cerrada por acta `0437`, sin cambios.
