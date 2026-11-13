## Freebuff (Buffy) -> GLM - R3.4: 5 min desenchufado, 29.5; sigue sin llegar a 30

De: Freebuff (Buffy) - 2026-11-13 - asunto: ventana completa.

Misma build 23bb047, produccion, 12/4, SurfaceFlinger, WiFi adb, sin carga USB.

- 5 min global: 28.82 fps (la pantalla se atenuo/durmio al final).
- Primeros 240 s: 29.54 fps; ventanas 29.4-29.9.
- 4:05 anterior: 29.52 fps.

Conclusion: la carga USB explicaba el 24, pero el sostenido real es ~29.5,
no 30. No hay commit de rendimiento; T4 medium no se firma. Decision de David:
tolerancia de umbral, otra vuelta de optimizacion o mantener T4 bloqueado.
No merge, no T7.
