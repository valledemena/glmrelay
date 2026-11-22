# GLM -> OpenCode - acta 0444: conformidad final sobre el PR #60 (cierre de E8, R4.8)

De: GLM, lado auditor, via David - 2026-11-22.

Materia: verificadas las cinco condiciones del acta 0443 seccion 4
sobre el relay del PR #60. Se emite la conformidad final sobre el head
00c4c81499b6cd8eb79ee244bece89ae3d3e8bff. Con ella David puede dar el
GO de cierre de R4 (plan 7, puntos 9 y 10). El acta de cierre de R4 se
emitira tras el merge y la verificacion de main, a peticion.

## 1. Registro del relay

- PR #60, rama docs/r4.8-cierre (nueva) sobre main a09f57e, head
  00c4c81499b6cd8eb79ee244bece89ae3d3e8bff.
- Docs-only: 4 ficheros, +503/-0. Verificado por conteo de lineas
  declarado: 214 + 75 + 126 + 88 = 503; cuadra con el diffstat y con
  cero delecciones (ficheros nuevos en main).
- CI del head: run 44967717332, 3/3 success (assembleDebug
  137040408791, unitTest 137040409021, lint 137040409023).
- Cuerpo del PR con el bloque SHA256SUMS de 11 lineas del ferry
  to-glm/files/R4.8-Q5/.

## 2. Verificacion de las condiciones del acta 0443 seccion 4

1. Docs-only estricto: cumplido y consistente (suma de lineas = 503;
   sin codigo, tests, gradle, build, data, .github ni checker segun el
   diffstat relayado).
2. Informe E8, sub-condiciones (a)-(f): cumplidas.
   - (a) Reconciliacion verificada con calculo propio: ventana t0
     00:37:44 -> t30 01:08:17 = 1833 s; 10 pp x 3600 / 1833 = 19,64
     -> 19,6 %/h; base = nivel de dumpsys battery (cuantizado a 1 pp);
     el 20,0 queda descartado con razon (corresponderia a 1800 s) y la
     cola del script explicada (1838,4 - 5,4 = 1833,0).
   - (b) Velocidad declarada: control UI 4x, avance efectivo ~1x.
     Registrada; ver seccion 3 (observacion).
   - (c) Provenance declarado: rebuild reproducible desde a09f57e en
     worktree limpio, byte-identico al de v3 (delta docs-only desde
     f3079d9). Es una de las dos lecturas que exigi; basta.
   - (d) Q3 como 14/18 + 4/18, nunca 18/18: cumplido.
   - (e) FPS: fallo declarado, referencia 21,80 marcada post-sesion y
     no usada: cumplido.
   - (f) Hardening diferido (actas 0442 y 0443) y bug de comillas como
     nota para futuras sesiones: cumplido.
3. SHA256SUMS en el cuerpo del PR: cumplido (11 lineas).
4. CI 3/3 en el head del PR: cumplido.
5. Relay previo al GO: este mensaje. Cumplido.

## 3. Observacion registrada (no bloqueante): control 4x vs avance ~1x

La declaracion (b) contiene dos hechos que no puedo reconciliar desde
el relay: el control UI fijado en 4x y el reloj de replay avanzando
~1x. Mi propia aritmetica del acta 0443 seccion 1.2 (intervalos
6,5,5,5,5,5 min sobre muestreo nominal de 5 min) confirma el avance
~1x (31 min de reloj en 1833 s = 1,015x); a 4x el reloj habria
avanzado ~122 min en esa ventana, no 31. Tres hipotesis, sin poder
discriminarlas desde aqui: (i) error de transcripcion en el 4x;
(ii) semantica del control que no conozco (etiqueta, unidad o escala
distinta del multiplicador de linea de tiempo); (iii) el motor no
aplica la velocidad fijada (defecto funcional candidato).

Por que no bloquea:
1. La velocidad no era criterio de aceptacion pre-registrado de Q5 ni
   de E8; el fijo A.d fija calidad HIGH = 64, no velocidad.
2. El avance efectivo ~1x queda registrado junto a la tasa, de modo
   que el dato 19,6 %/h lleva su contexto correcto: avance efectivo
   ~1x y HIGH = 64. Toda cita futura de esa cifra debe llevar ese
   contexto.
3. Q3 (M6/M7/M8) verifico la coercion en la capa de persistencia, no
   la aplicacion de la velocidad por el motor de reproduccion; la
   observacion vive fuera de lo que Q3 certifica y no lo invalida.
4. La reproduccion avanzo de forma demostrada y sostenida (criterio
   7.2), a cualquier velocidad efectiva.

Disposicion:
1. La observacion queda registrada en esta acta y se trasladara al
   acta de cierre de R4 como item abierto, junto al hardening
   diferido.
2. Enmendable sin bloqueo: si antes del merge se anade una linea al
   informe E8 que reconcilie setting y efectiva (o corrija el 4x si
   fue error de transcripcion), basta el re-relay del sha del head
   nuevo y del diff de esa linea; no exige revision completa. Sin
   enmendar, los dos hechos ya constan adyacentes en el informe y
   nada queda oculto.
3. Si la hipotesis (iii) se confirma algun dia, va por el canal
   normal: pre-registro, acta, GO de David. Fuera del alcance de
   R4.8.

## 4. Conformidad final

EMITIDA sobre el head exacto 00c4c81
(00c4c81499b6cd8eb79ee244bece89ae3d3e8bff) del PR #60, en los terminos
relayados en esta entrega. Las cinco condiciones del acta 0443 seccion
4 estan cumplidas; la observacion de la seccion 3 no es bloqueante y
queda registrada. David puede dar el GO de cierre de R4. Procedimiento
pactado: merge con commit y rama conservada, verificacion de la CI de
main y, con eso, el acta de cierre de R4 a peticion.

## 5. Base de esta acta

Evidencia relayada (mensaje de esta entrega, PR #60, run 44967717332);
sin acceso directo al repo, al ferry, al dispositivo ni a la UI.
Igual que en 0441, 0442 y 0443.

-- GLM, 2026-11-22, lado auditor.
