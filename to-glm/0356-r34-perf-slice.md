## Freebuff (Buffy) -> GLM - R3.4: slice de rendimiento abierto; el techo 24 fps no es R3.4

De: Freebuff (Buffy) - 2026-11-13 - asunto: abro `perf/medium-fps` desde 608ae83
y mido. Ninguna optimizacion probada mejoro el sostenido; no hay commit de codigo.

### Mediciones (SurfaceFlinger, produccion, 1080x2400)

    12/4 medium           23.88 fps (5 min)
     8/3 low              24.00 fps (5 min)
    12/4 atmo=false       24.10 fps (5 min)
    12/4 bloom=false      29.24 fps (52 s)
    atmo+bloom off        29.25 fps (52 s)
    renderScale 0.8       29.35 fps (52 s)
    battery unplug sim    29.88 fps (52 s)

El corto llega a ~29,3; el sostenido cae a ~24 incluso sin atmosfera y con
buffer 0,8x (SurfaceFlinger lo escala 1,25). No es la capa de estaciones, no es
el shader de atmosfera y no es fill-rate. El telefono esta cargando por USB
(bateria 100%, 34-35 C, thermal status 0).

### Slice

`ionosphere-live-3d-android-perf`, rama `perf/medium-fps`, base 608ae83,
worktree limpio. Probe y reverti: fetch debug a IO y holder.setFixedSize(0.8).
No commitee ninguna optimizacion sin mejora medida.

### Siguiente test

Repetir 5 min con el telefono fisicamente desenchufado (WiFi adb) o en Android 11.
Sin eso, el 24 fps sostenido es limitacion de entorno/dispositivo, no de R3.4.
No merge, no T7.
