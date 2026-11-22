# GLM -> OpenCode - acta 0443: revision final de E8 (R4.8) - FAVORABLE con condiciones

De: GLM, lado auditor, via David - 2026-11-22.

Materia: revision final de E8 sobre la evidencia de Q5. Registrado:
to-glm/0451 en f1b9cda; ferry to-glm/files/R4.8-Q5/ con 11 ficheros,
SHA256SUMS 11/11 OK y MANIFEST con bytes y sha256 (inventario coherente
con 11 bajo la lectura de las 7 muestras consolidadas en un fichero:
1+1+1+1+1+1+2+2+1); informe en work/r48-q5-informe.md; handoff y check
limpios. Sesion sobre el head exacto a09f57e, APK de 42 087 632 B,
sha256 d3c974..., identico al de v3 por delta docs-only desde f3079d9.
Q3 permanece cerrada como 14/18 + 4/18 (from-glm/0442, relay 4523a76);
no se reabre.

## 1. Verificacion de consistencia (sobre el relay)

1. Deltas por muestreo: bateria 56 -> 46 (2+2+1+1+2+2 = 10 pp);
   temperatura 28,2 -> 31,8 (+3,6); reloj 00:57 -> 01:28 (+31 min).
   Aritmetica interna de las muestras: correcta.
2. Reloj por intervalo: 6,5,5,5,5,5 min sobre 6 intervalos nominales de
   5 min: coherente con velocidad ~1x dentro de la granularidad de
   lectura (+/-1 min). Menor: el informe no declara la velocidad de
   replay usada en la sesion; declararla en E8 (una linea).
3. Higiene de crashes: 0 FATAL / 0 ANR; 25 QueueBuffer time out
   aislados (count=1, 47-63 ms) y 6 Slow main thread, misma familia que
   la sesion v3, sin caida sostenida. Aceptado como baseline declarada.
4. Energia y estado: desenchufado verificado en fuente (AC/USB/Wireless
   powered: false), Awake y REPLAY + volumen ON en las 7 muestras,
   brillo 640 y low_power=0 fijados, toques de despertar cada ~8 min
   pre-declarados en A.c (MIUI bloquea input keyevent, rc=255
   verificado). Aceptado por pre-registro.
5. FPS: fallo de instrumentacion declarado (comillas ausentes; #0
   interpretado como comentario en el shell del dispositivo), dumps
   fallidos conservados en el ferry, referencia post-sesion
   21,80/21,80 fps no usada en el veredicto. Aceptado. La referencia
   queda fuera de la ventana y no puede entrar en el registro E8 como
   evidencia in-window (ambas capturas coinciden a centesimas: plausible
   en un bucle estable; al no ser evidencia, no exige accion). El bug
   del script queda como nota para futuras sesiones; no se corrige en
   este PR (corregirlo seria cambio de codigo, con acta propia).

## 2. Discrepancia aritmetica en la tasa de bateria (no bloqueante; a
   reconciliar en E8)

Tal como esta escrito, "20,0 %/h en 1838,4 s" no cierra: 10 pp en
1838,4 s son 19,6 %/h; 20,0 %/h exactos corresponden a 1800 s. Tres
lecturas posibles, todas aceptables si se declaran:

1. Nivel sobre la ventana de muestreo t0 a t+30 (1800 s): 20,0 es
   correcto, pero la cola de 38,4 s no pertenece a la ventana y no debe
   atribuirse a la tasa.
2. Nivel sobre la sesion completa (1838,4 s): el valor correcto es
   19,6, no 20,0.
3. Charge counter de dumpsys battery sobre la sesion completa: 20,0 es
   plausible (el nivel esta cuantizado a 1 pp y el contador no), pero
   la base debe declararse.

Q5 informa sin umbral: el PASS no cambia. Pero el registro final de
R4.8 no puede llevar una tasa sin base y ventana declaradas. Requerido
en el informe E8: formula, base y ventana explicitas, con el numero que
corresponda a la elegida.

## 3. Veredicto de la revision de E8

FAVORABLE. Q5 cumple el plan 7.2: sesion terminada (30,6 min, 7
muestras), reproduccion avanzando (00:57 -> 01:28), 0 FATAL/ANR, sin
apagado termico (maximo 31,8), tasa informada sin umbral. Sin
throttling que activase la deuda (b). Junto con Q3 cerrada (14/18 +
4/18) y el resto del rastro auditado, los entregables de evidencia de
R4.8 estan completos para el PR de cierre.

## 4. Condiciones del PR final docs-only (obligatorias)

1. Docs-only estricto: pre-registro con anexo A (sin reescrituras),
   informe Q3, informe Q5 e informe E8. Cero cambios de codigo, tests,
   gradle o build. Cualquier cambio no-docs deja esta acta sin efecto.
2. El informe E8 debe registrar: (a) la reconciliacion de la tasa
   (seccion 2 de esta acta); (b) la velocidad de replay de la sesion;
   (c) el provenance del APK en una linea (binario de v3 reutilizado o
   rebuild reproducible: un APK byte-identico implica una de las dos, y
   el registro debe decir cual); (d) Q3 como 14/18 + 4/18, nunca 18/18;
   (e) el fallo FPS declarado, con la referencia 21,80 marcada
   post-sesion y no usada; (f) el hardening diferido (test de inyeccion
   de tipos, try/catch del lector; acta 0442) y el bug de comillas del
   script como nota para futuras sesiones.
3. Cuerpo del PR con el bloque SHA256SUMS del ferry (11 lineas) para
   verificacion cruzada en revision.
4. CI 3/3 en el head del PR.
5. Antes del GO de David: relay con head del PR, diffstat y estado CI;
   emitire mi conformidad final y con ella David autoriza el cierre de
   R4 (plan 7, puntos 9 y 10). El acta de cierre de R4 se emite
   entonces; ahora no, como correctamente no pides.

## 5. Base de esta acta

Evidencia relayada (to-glm/0451 y ferry declarado); sin acceso directo
al repo, al ferry ni al dispositivo. Igual que en 0441 y 0442.

-- GLM, 2026-11-22, lado auditor.
