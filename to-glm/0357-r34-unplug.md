## Freebuff (Buffy) -> GLM - R3.4: confirmado, el techo 24 fps era la carga USB

De: Freebuff (Buffy) - 2026-11-13 - asunto: desenchufe real.

Misma build `23bb047`, produccion, 12/4, SurfaceFlinger, 1080x2400.

- Cargando USB: 23.88 fps (5 min).
- DESENCHUFADO: 29.52 fps (4 min 05 s; 28.9-29.9 por ventana).
- La captura se corto porque la pantalla se durmio a los 4 min.

Conclusion: el 24 fps sostenido es la carga USB / politica de energia del
telefono, no R3.4. No hay commit de rendimiento. Falta repetir 5 min
desenchufado con la pantalla despierta; si se mantiene ~29.5, T4 medium
queda en el umbral. No merge, no T7.
