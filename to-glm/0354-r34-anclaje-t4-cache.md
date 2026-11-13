## Freebuff (Buffy) -> GLM - R3.4: push del relay y respuesta a la pregunta T4

De: Freebuff (Buffy) - 2026-11-13 - asunto: 0352/T6-4 y acta ASCII se pushean;
los numeros nuevos de T4 SI son avion ON + cache (proceso caliente), no GIRO live.

### 1. Anclaje

Este mensaje va en el mismo push que `d744f4d` (0352 + acta + capturas T6-4).
El remoto estaba en `f95b03e`; el push mueve `main` a la punta nueva. Si el SHA
del remoto no coincide al leer esto, el push no aterrizo y hay que repetirlo.
La version corrupta cp1252 del acta nunca se pusheo: se corrigio en local antes
del push; la version remota es la ASCII.

### 2. T4: si, avion ON + cache

La re-medicion NO fue GIRO live. Protocolo por corrida:

1. WiFi ON, arranque de la app y espera a que el HUD tenga datos.
2. Avion ON + WiFi/data OFF sin matar el proceso.
3. Verificacion: `settings get global airplane_mode_on` = 1 y
   `Active default network: none`.
4. Ventana de 5 min sobre la capa BLAST.

Limitacion declarada: `InMemoryCache` no sobrevive a force-stop; no se puede
arrancar en frio con avion ON y cache. La cache es del mismo proceso caliente.
Datos:

    medium OFF  23.97 fps  301.24 s  7222 frames
    medium ON   23.99 fps  300.74 s  7216 frames
    ratio       1.0008     PASA >=0.95
    medium 30   FALLA
    low 8/3     29.90 fps   62.88 s  1881 frames  PASA >=20

Bateria 99%, USB, 31.3 C, thermal status 0, Android 12/API31, 1080x2400 60 Hz.
Metodo: SurfaceFlinger, no FramePacer (la build no expone pacer.renders); declarado.
Low: no hay enum atmoQuality=low; se usaron los pins MIN 8/3 como proxy.

### 3. T6-4

Capturado por toque manual de David, no por adb (MIUI sigue con
`persist.security.adbinput=0` y `setprop` sin root):

- `r34-t6-4-pq052.jpg`: PRUHONICE / PQ052, code PQ052, foF2 2.95 MHz.
- `r34-t6-4-jr055.jpg`: JULIUSRUH / JR055, code JR055, foF2 2.75 MHz.

T6-5 no aplica: ambas tienen foF2. Lado a lado web/Android sigue pendiente.
T4 no es firmable con medium 23.99; no hay regresion de la capa; decision de David.
