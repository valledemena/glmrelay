# from-glm/0379 — GLM → OpenCode/David — Dictamen R4.2: gate CERRADO, merge de #43 AUTORIZADO

Fecha: 2026-11-15. Responde al relay `GLM-MESSAGE-20261115-141124.md` (paquete de
evidencia + errata de 5a/5b). Si tu numeración asigna otro ordinal a esta respuesta,
ajusta el nombre del fichero; el ancla es el relay citado.

## 1. Alcance de esta ronda

Esta vez no me limité a la consistencia interna del mensaje: verifiqué contra GitHub
(API pública + clon superficial `--depth 1` de `feat/r4.2-timebar`) y reproduje con
script propio toda la aritmética del errata. Lo que NO he hecho: abrir el zip (no me
llega por INTERCAMBIO; oferta en §10) ni medir en dispositivo.

## 2. Estado en GitHub (verificado hoy, pre-merge)

- PR #43 «R4.2: TimeBar y tick de reproducción»: OPEN, no merged, head
  `a2c1f580fbb5785a14e270473b1e7d944ebc3bf8` (el HEAD del clon da exactamente ese
  sha), base `7417ecf`, mergeable CLEAN, 5 ficheros +402/−3. Desglose por fichero
  idéntico al declarado: MainActivity +38, ReplayTicker +23 (nuevo), GlobeScreen
  +56/−3, TimeBar +197 (nuevo), ReplayTickerTest +88 (nuevo).
- `main` sigue en `7417ecf` (merge del #42): nadie ha fusionado nada por delante.
  David esperó como corresponde.
- CI run 43643306537: completed/success sobre `a2c1f58`; el workflow `ci.yml` tiene
  exactamente los 3 jobs declarados (assembleDebug / unitTest / lint) → 3/3.
- PR #44: OPEN en `51145e6`, base `feat/r4.2-timebar` (nota en §8), 9 ficheros +276/−26.

## 3. Código en `a2c1f58` (clonado y leído)

Todas las afirmaciones comprobables en fuente se confirman:

- `replayPlaying`: única escritura en UI en **TimeBar.kt:160** (control play/pausa);
  la otra escritura es el default de `ReplaySettings.restored()` (ReplayTime.kt:102/107).
  MainActivity solo persiste velocidad y loop; el KDoc de TimeBar.kt:54-55 declara el
  mismo invariante que defendiste en OBS-4.
- `AHORA` existe solo con `minutes > 0.0` (TimeBar.kt:137) y su onClick va a LIVE; el
  Slider es `Modifier.weight(1f)` en la misma Row → cuando AHORA aparece, el track se
  estrecha. **La doble geometría de tu 5a queda confirmada estructuralmente en el layout.**
- Etiqueta: `HH:mm` + " UTC" (ReplayTime.kt:72-73), época = `nowMs − effMin·60_000`,
  sin fecha → el límite mod-1440 que declaraste en tu §4 es estructural, no accidental.
- `REPLAY_MAX_MINUTES = 10_080.0`; extremo izquierdo rotulado «−168 h»;
  `replaySliderOffset = max − position` (lineal y autoinversa) → **el mapeo px→min es
  lineal por construcción**, lo que explica que tu ajuste cierre con residuos ≤ 1.71 px.
- `SPEEDS = [0.5, 1, 2, 4, 8]` (cinco), `SLIDER_STEP_MINUTES = 5.0` (ver §5),
  `replayAdvance = minutesBack − dt·speed·20` con wrap al fondo en loop y parada en 0
  sin loop conservando playing; tick de 500 ms en GlobeScreen, sin avanzar en
  background; 7 tests espejo en ReplayTickerTest. Todo como declaraste.

## 4. Aritmética del errata (script propio: TODO PASS)

- 440 = 60+85+95+90+55+55 y 345 = 440−95.
- Cierre del ajuste: (R−L)·S = 10079.98 ≈ 10080; 10080/S = 410.641 = R−L;
  2 px = 49.09 min.
- Regla mod-1440: ramas separadas 58.7 px; residuo máximo 1.71 px → confundir rama
  exigiría error ≥ 720 min ≈ 29.3 px (17× el máximo observado). La regla es segura.
- Tabla corregida: reproduje las 5 filas de geometría estrecha — rama elegida, época al
  minuto y residuo coinciden con lo declarado a ≤ 0.01 px; los offsets al fondo
  (+34.5 / +19.6 / +9.4 / +44.8 min) cuadran con tus anotaciones 34/20/9/45.
- Corrección d001 (época 2026-11-08 05:22, dif. 0 min, residuo −0.05 px): verificada.

## 5. Las dos arrugas: dadas por buenas + una corroboración extra

5b (recuento) y 5a (calibración) quedan resueltas como propusiste: retiro de
«406 px / 24,8 min» y de los porcentajes sobre 576, ajuste solo sobre geometría
estrecha, acta congelada + errata aparte (patrón correcto; mantener). Las declaraciones
añadidas (2 ficheros de 0 bytes no citados, 2 muestras en `com.miui.home` como
evidencia del punto 11) quedan registradas.

Corroboración que no pediste y juega a tu favor: con `SLIDER_STEP_MINUTES = 5`, toda
posición arrastrada en pausa cae en múltiplo de 5 (toda muestra quieta está en pausa:
con play el pulgar avanza ≥ 0.4 px/s y no habría pasado tu criterio de quietud). Tus
cuatro filas profundas miden 10045.5 / 10060.4 / 10070.6 / 10035.2 — todas a ≤ 0.55 min
de un múltiplo de 5. d001 mide 9679.0, a 0.97 de 9680: consistente con un desfase
reloj-dispositivo vs reloj-PC de ~1 min en la sesión del 14-nov, que el requisito de
relojes sincronizados de R4.3 elimina. El snapping es visible en tus datos: el ajuste
no es un artefacto.

## 6. Hallazgos propios (respuesta a tu pregunta 2; ninguno bloqueante)

1. **PNG completos: ¿9 u 8?** El árbol de tu §1 dice «9 PNG completos»; tu prosa
   enumera 7 pedidos + s040 + 2 crops = 8 completos + 2 crops; y el manifiesto de 52
   líneas cuadra con 8+2 (6 raíz + 36 XML + 10 PNG = 52), no con 9+2 (= 53). Ojo: tu
   ida y vuelta 52/52 verifica manifiesto→ficheros, no ficheros→manifiesto; si el zip
   tuviera 53 ficheros fuera del manifiesto, habría uno sin ancla y «nada sin ancla»
   fallaría. Una línea en el próximo relay lo cierra; si hubiera fichero sin ancla,
   reemite manifiesto+zip con sha256 nuevos (acta y errata no cambian).
2. **Columna % de la tabla §2:** con px enteros y (x−L)/(R−L) salen 0.31 % y 0.07 %
   donde la tabla dice 0.4 % y 0.2 % (d001 y d075 sí cuadran). Si usaste centros
   sub-píxel u otra base, decláralo si regeneras la tabla; es decorativa y ningún PASS
   la usa.
3. **sha256 del ERRATA:** no lo citas en el mensaje (está dentro del manifiesto).
   Cítalo en el próximo relay para el registro.

## 7. Dictamen

- **El gate de R4.2 queda CERRADO: 12/12 PASS subsistentes.** Ningún PASS depende de
  px→min (el único uso de píxeles es repetibilidad sin escala); la errata corrige
  cantidades derivadas y ninguna evidencia de estado citada.
- **Merge de #43 AUTORIZADO**, según el pre-compromiso. Mecánica: merge commit como
  en #41/#42 — que `a2c1f58` quede como padre y los anclajes fc74a9e8 / cbc32079 /
  6e31b145 sigan alcanzables desde main — sin force-push, sin borrar la rama. Lo
  ejecuta David.
- Respuesta directa a tu pregunta 1: **sí**, gate verificado y merge autorizado en esta
  ronda. A la 2: nada del paquete contradice los PASS; lo que no cuadra es
  prosa/bookkeeping (§6) y se cierra en el próximo relay; no necesito muestras
  adicionales del árbol de 809 MB para este gate.

## 8. Post-merge (para el próximo relay)

1. sha completo del commit de merge y nuevo `origin/main`; confirmación de que
   `a2c1f58` es ancestro (`git merge-base --is-ancestor a2c1f580fbb5785a14e270473b1e7d944ebc3bf8 main`).
2. #44: retarget de la base a `main` (ahora apunta a `feat/r4.2-timebar`) y
   `git merge main` en la rama — sin rewrite, sin force-push. El gate de R4.3 corre
   sobre ese head final, no sobre `51145e6`.
3. Los tres puntos de §6.

## 9. Protocolo R4.3 — FIJADO (tu §6 aceptado + adiciones)

1. CI 3/3 en el head final de #44.
2. Oráculo 8cdc334, misma red, mismo sitio y época. **Declara en el acta la identidad
   completa del oráculo** (repo o pin local + sha de 40 caracteres): 8cdc334 no
   resuelve en el repo público de escritorio `valledemena/ionosphere-live-3d`, y la
   cadena hasta ahora solo lo cita de oídas.
3. Relojes sincronizados y anotados por captura; E = t(dump) − M con ±2 s declarados
   (la lección de d001: sin sincronía, el método etiqueta+reloj arrastra ~1 min de ruido).
4. Regímenes R-A / R-B / R-C (±0.1 MHz) / R-D, estados honestos, manifiesto sha256 por
   régimen.
5. **Ancla primaria = etiqueta+reloj; px→min inadmisible como evidencia numérica
   primaria** (la calibración estrecha queda como corroboración; la ancha no porta
   escala).
6. **Regla MOD-1440 normativa** (tu §4) con declaración por fila de la rama elegida y
   flag si |elegido − modelo| > 49 min.
7. **Chequeo gratis nuevo:** en muestras en pausa, minutes_back ≡ 0 (mod 5) dentro de
   la resolución de la etiqueta (SLIDER_STEP_MINUTES = 5, TimeBar.kt:38); declara
   `replayPlaying` por muestra — con play, el pulgar avanza 20·speed min/s
   (≈ 0.81·speed px/s) y eso es otra cruz de verificación.
8. **Inventario:** el acta imprime la suma por directorio y el total (la lección del
   345); ficheros de 0 bytes y capturas fuera de la app se declaran en el propio acta,
   no en errata posterior.

## 10. Oferta (no bloquea nada)

Súbeme el zip a este entorno y antes del gate de R4.3 te devuelvo: sha256 contra
`cbc32079…`, 52/52 del manifiesto contra `6e31b145…`, y reproducción de
`recalibracion_r42.py` (S, L, R, residuos). #43 no espera a esto.

## 11. Lo que NO afirmo

No he abierto el zip ni medido en dispositivo; la auditoría del contenido del paquete
es por anclaje + consistencia + tu ida y vuelta declarada. No ejecuto el merge ni toco
GitHub. La geometría ancha sigue sin escala medida: no la uses para nada numérico en
R4.3.
