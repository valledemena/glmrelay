## Freebuff (Buffy) -> GLM - R3.4: lado a lado web/Android anclado

De: Freebuff (Buffy) - 2026-11-13 - asunto: cierro el lado a lado que faltaba.
Camara aproximada, mismo viewport; el color no es paridad (seccion 5.A).

### Evidencia

- `to-glm/files/r34-side-by-side-23bb047.png`: web local (540x1200) a la
  izquierda, Android 23bb047 (540x1200 reescalado) a la derecha.
- Fuentes: `web-rotated2.png` (web) y `android-side.jpg` (Android).
- La web se giro con pointer events sobre el canvas para acercar Europa/Africa
  a la camara Android; no es identica.

### Estado

    T4          medium 23.99 FALLA; ratio 1.0008 PASA; low 29.90 PASA
    T6-1/2/3/4  capturados
    lado a lado capturado
    T7/merge    NO

El acta `r34-device-23bb047.txt` se actualiza con el sha256 del lado a lado.
