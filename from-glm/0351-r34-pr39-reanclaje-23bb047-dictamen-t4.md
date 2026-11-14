# GLM -> R3.4 - Re-anclaje del PR #39 a `23bb047`, cierre de P3/mutantes y dictamen sobre el gate T4/T6

De: GLM - 2026-11-14 - asunto: el PR #39 queda re-anclado y revisado en su head
nuevo; el P3.1 se cierra; los mutantes 7.2 se aceptan con MUT-10 muerto por
inspeccion; el gate T4 ejecutado no es firmable y se recomienda una escalera de
decision para David. Sin merge, sin T7.

Si David adopta este mensaje en el relay, sugerimos archivarlo como
`from-glm/0351-...` (contador unico compartido con `to-glm/`, cuyo ultimo es
0350), o con la numeracion que David prefiera.

---

## 1. Re-anclaje verificado (tercer momento extendido al head nuevo)

Todo lo siguiente fue verificado de forma independiente por GLM contra los
objetos git reales (protocolo smart HTTP) y contra el diff completo del PR:

    head            23bb04715b95a752f34eac8353ef36e0f0fdd85b
                    "R3.4: flag debug stations para el gate T4"
    cadena          608ae83 -> b6afd24 -> c5f1121 -> 23bb047  (lineal)
                    c5f1121b5b505940f757075cae5068f4b905d45b
                    b6afd24c92404a21775c395a7492acd0330d7cdd
    main            608ae834be079e3145c385ccf8ecd11767600b9c  (sin cambios)
    PR 39           OPEN, base main, rama feat/r3.4-ionosonde-layer = 23bb047
    CI              ci.yml PASS sobre la punta de la rama (badge verde);
                    el run id del 23bb047 no esta reportado -> pedirlo para 0351
    numstat         16 ficheros, +1042/-8  (recuento independiente de GLM)

Congelados intactos en `23bb047` (identicos byte a byte al main fusionado):

    docs/r3/PLAN-R3.4-IONOSONDE-LAYER.md   34657 B  sha256 10566f61...
                                           (git blob sha1 08570501...)
    docs/r4/tools/R4_DISPLAY_CHECK_v6.py   46114 B  sha256 5a48cb18...
                                           (git blob sha1 343c8104...)
    data/**, .github/**, AndroidManifest    sin toques

Nota de registro: los digests historicos de GLM eran **sha256 planos**
(`10566f61`/`5a48cb18`), no git blob sha1. Se anotan ambos aqui para que
ninguna verificacion futura tropiece con la ambiguedad.

Reconciliacion de numstat: la declaracion de 0350 para `c5f1121`
(15 ficheros, +1032/-7) + el delta de `23bb047` (GlobeRenderer +13/-11
brutos = +4/-1 netos; MeasureConfig +6/-0) = **16 ficheros, +1042/-8**
exacto. La contabilidad de Freebuff cuadra al numero.

La pagina del PR renderiza cache obsoleto (b6afd24, 1 commit, 15 ficheros);
es cosmetico, se refrescara solo. El ref git refs/pull/39/head = 23bb047 es
la verdad en vivo.

## 2. Deltas hunk-a-hunk

### 2.1 `c5f1121` - P3.1 (foF2 +Inf)

`stationFoValues`: guarda `f == null || !(f > 0.0)` con clamp posterior
`coerceIn(0f, 1f)`. Espejo exacto de `builders.ts:305`
(`f && f > 0 ? Math.min(1, Math.max(0, (f - fMin) / (fMax - fMin || 1))) : 0`):

- `+Inf` -> 1 (el clamp lo lleva al techo), `-Inf` -> 0, `NaN` -> 0
  (la comparacion es falsa), `null` -> 0.
- Test anadido con `POSITIVE_INFINITY`/`NEGATIVE_INFINITY` en la fixture.
- `stationColorRange` queda fuera del cambio: +Inf no desplaza percentiles.

**P3.1 CERRADO.** Veredicto: CONFORME.

### 2.2 `23bb047` - flag debug `stations`

- `MeasureConfig`: `stations: Boolean = true` (default); clave ausente -> true;
  tipo no booleano -> config invalida (null). Consistente con la dureza
  existente de `bloom`/`atmo`.
- `GlobeRenderer`: `stationsEnabled = measure?.stations ?: true`; envuelve
  draw + `processPickRequest` en `if (stationsEnabled)`; linea de log
  extendida. Produccion (sin measure.json) identica: default true.
- El OFF se salta tambien el sondeo de pick: sesgo **conservador** para el
  ratio (favorece al OFF, en contra de la capa). El ratio paso de todos modos.

Veredicto: CONFORME. **Desviacion a declarar**: `MeasureConfig.kt` no esta en
el §6 del plan (mismo tratamiento que GlobeScreen/HudPanel/TASKS en 0350).
Ademas 0350 decia "el gate debe correr sobre c5f1121": correrlo sobre
`23bb047` es aceptable (el toggle es solo del camino de medicion y la
produccion no cambia), pero 0351 debe decirlo.

## 3. Mutantes 7.2

Tabla de 0350 = tabla del plan rev c (incluidas mis erratas: MUT-2 con killer
unico `2.5 -> 2.5`, MUT-5 asertando el rango devuelto). Ningun mutante
commiteado. Aceptado como registro medido localmente por el ejecutor.

**MUT-10 muerto por inspeccion - CONFIRMADO por GLM en `23bb047`:**

- call site: `pointSize = stationPointSizeClamp(rawPointSize)` en
  `GlobeRenderer` (el clamp SI se aplica donde se envia el uniforme);
- vertex shader `StationPointsRenderer.kt:210`:
  `gl_PointSize = min(sizePx, uMaxPointSize);` - escritura incondicional
  (riesgo 10.2 cerrado en todas las ramas);
- techo: `maxPointSize = min(driverMax, 70f)` (L69) + consulta y log de
  `GL_ALIASED_POINT_SIZE_RANGE` (L67/L72) - riesgo 10.1 cerrado;
- T6-2/T6-3 (3 vs 15) aportan la evidencia visual diferencial.

No hace falta re-ejecutar la matriz sobre `23bb047`: el delta solo envuelve el
call site en un `if` default-true y no toca ningun objetivo de mutante.

**P3.2 CERRADO** (registro). **P3.3**: no insisto; quedese como cosmética
registrada. No vale un head nuevo.

## 4. Gate de dispositivo ejecutado sobre `23bb047`: lectura del contrato

### 4.1 Entorno (§9.1) vs ejecutado

| Cláusula | Plan | Ejecutado | Estado |
|---|---|---|---|
| Dispositivo | Mi 10 Lite 5G | M2002J9G (es EL equipo fijado) | OK |
| OS | Android 11 / API 30 | Android 12 / API 31 | DESVIACION |
| Bateria | 50% | 94% | DESVIACION (benigna) |
| Avion | ON, datos cache | OFF, GIRO live | DESVIACION |
| Termica | declarada | 31,3 C, status 0 | OK |
| Ventanas | 5 min | 297,03 s / 298,62 s (99,0/99,5%) | OK |
| Metodo FPS | `FramePacer` | timestamps de capa SurfaceFlinger | DESVIACION (mas objetivo, pero no es el fijado) |

### 4.2 Medidas (§9.2)

| Medida | Umbral | Resultado | Veredicto |
|---|---|---|---|
| FPS medium ON | >= 30 | 24,16 (298,62 s) | NO PASA |
| FPS medium OFF | >= 30 | 23,86 (297,03 s) | NO PASA |
| Ratio ON/OFF | >= 0,95 | 1,0126 | PASA |
| Piso low (worst 60 s) | >= 20 | **no medida** | INCOMPLETO |
| Diametro <= 70 px | <= 70 y en rango driver | techo 70 px, driver 1..1023 | PASA (codigo + log) |

Lectura tecnica: la app marca 30 fps (`Rotation.TARGET_FPS = 30`, FramePacer
sobre la rejilla de vsync); presentar 24 fps = perder ~20% de las ranuras.
El deficit es **atribuible a la linea base**: el OFF falla identico, el ratio
1,013 (con sesgo conservador) prueba que la capa R3.4 es neutra en rendimiento.
La condicion live (avion OFF) fue exactamente lo que §9.1 queria excluir y
nunca se excluyo.

### 4.3 Capturas (§9.3)

- T6-1: tomada con camara de medida; el contrato dice literalmente
  "camara por defecto" -> **repetir obligatorio**. Es barato: modo produccion,
  pointSize 11, sin tocar nada; la rotacion automatica del globo termina
  metiendo una estacion en encuadre; se captura ese frame. No hace falta
  inyeccion de input.
- T6-2 / T6-3: conformes (3 y 15, HUD de confirmation).
- T6-4: bloqueado por MIUI (`INJECT_EVENTS`). Requiere a David: toggle
  "Depuracion USB (Ajustes de seguridad)" + reinicio/reconexion, o toque
  manual del punto. El popup debe verse con `code` visible.
- Lado a lado web vs Android (camara aproximada, sin paridad de color):
  **falta**.

### 4.4 Registro

El acta y los PNG existen solo en el disco del ejecutor. Antes de T7 deben
subirse al relay (`to-glm/files/` + mensaje 0351 con sha256). El nombre
`r34-device-23bb047.txt` ya cumple §9.4.

## 5. Dictamen sobre la decision T4 (la firma es de David)

**El gate tal como se ejecuto no es firmable**: falla el medium en ON y OFF,
falta el piso low, y el entorno y el metodo se desvian de §9.1/§9.2 sin
enmienda autorizada. Pero la evidencia tambien dice que el fallo no es de
R3.4. Escalera recomendada:

1. **Antes de cualquier decision**: repetir la bateria §9.2 completa (ON, OFF,
   ratio, **piso low incluido**) en las condiciones literalmente alcanzables
   sobre Android 12: **avion ON + datos cacheados** (el plan ya lo anticipaba
   via Outcome.Cached), bateria declarada. No requiere codigo ni head nuevo.
   Si el medium entonces pasa, T4 queda firmable con UNA sola desviacion
   declarada (el OS), y David decide si la acepta.
2. Si aun asi falla: David elige. Recomendacion de GLM: **aceptar la
   desviacion de entorno y re-alcance** - el medium pasa a condicion previa
   de la plataforma (el OFF lo falla igual), el ratio y el techo quedan como
   clausulas vinculantes (ambas pasan) - y abrir un **slice de rendimiento
   dedicado** (docs-only, con sus propios gates) si el 30 fps importa en
   Android 12. Alternativas: downgrade a Android 11 para un T4 literal (riesgo
   no recomendable en un telefono de uso) o mantener R3.4 bloqueado por una
   condicion que el slice no causa (tampoco recomendado).
3. **No** bajar el umbral para pasar: eso corrompe el gate.
4. **No** un head de rendimiento dentro de R3.4: §12 lo excluye ("no
   reescritura de GlobeRenderer ni del pase de atmosfera") y el deficit
   preexiste al slice.

## 6. Checklist antes de T7 (responsable)

- [ ] 0351 en el relay: head 23bb047 como head del gate, desviacion
      MeasureConfig (§6), desviaciones de entorno/metodo, run id del CI del
      23bb047, resultados completos (ejecutor).
- [ ] Re-medicion §9.2 con avion + cache (incl. piso low) y acta actualizada
      sobre 23bb047 (ejecutor).
- [ ] T6-1 re-tomada: produccion, camara por defecto, pointSize 11 (ejecutor).
- [ ] Captura lado a lado web vs Android (ejecutor).
- [ ] Acta + t6-*.png en to-glm/files/ con sha256 (ejecutor).
- [ ] T6-4: desbloquear input o toque manual; popup con code visible (David).
- [ ] Decision T4 segun escalera (David).
- [ ] Re-anclaje final de GLM si aparece head nuevo (GLM).
- [ ] Firma "gate R3.4 OK" + sha256 en el PR y merge (solo David).

Mientras el checklist no cierre, no hay merge ni T7.

GLM - 2026-11-14
