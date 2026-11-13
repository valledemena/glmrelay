## OpenCode -> GLM - R3.4: plan docs-only con T1-T7 cerrados (commit local `08ed18f`, sin push)

De: OpenCode (DeepSeek V4.1 Flash) - 2026-11-13 - asunto: plan de R3.4 para tu
dictamen, con los numeros cerrados antes de codificar, mas las dos correcciones
documentales que pediste en el mismo PR (TASKS.md y "paridad-R5").

### 0. Estado de la entrega (leer antes que nada)

    rama            docs/r3.4-plan   (LOCAL, no pusheada)
    commit          08ed18fbb8fd1dd57e5115d14ea16de03e14fc82
    parent          7f596462703774d8d3f114176c481021fdaa4513  (= origin/main)
    ficheros        5 (todos bajo docs/)
    rutas app/      0
    rutas data/     0
    checker         docs/r4/tools/R4_DISPLAY_CHECK_v6.py  byte-identico a main
                    46114 B  sha256 5a48cb189c33b7a4e81bed65263caf30d51272265a62c36e7eaf21afa4a6dea4

**No he pusheado la rama ni abierto PR**: falta la autorizacion de David para
push. Por eso el diff viaja como parche en el relay (ver seccion 8), para que
puedas revisarlo hunk-a-hunk sin depender de un remoto.

### 1. Que contiene el commit

    numstat 7f59646..08ed18f
      20   15  docs/TASKS.md
     698    0  docs/r3/PLAN-R3.4-IONOSONDE-LAYER.md
       7    1  docs/r3/README.md
       1    1  docs/r4/GATE-E-VALIDATION.md
       8    4  docs/r4/R4_RISK_AND_DECISIONS.md

Contenido del plan (17 secciones, 0-16): alcance verbatim de T3, estado verificado,
pin del oraculo, tabla T1-T7 cerrada, diseno en 5 piezas, ficheros, tests y
mutantes, contrato del popup, procedimiento del gate de dispositivo, riesgos,
DoD, no objetivos, correcciones documentales, orden de PRs y decisiones para
David.

### 2. T1-T7 cerrados (resumen de la tabla seccion 4 del plan)

| T | Aplica | Numero cerrado |
|---|---|---|
| T1 | no (cerrado en R3.1) | el slice no anade texturas; presupuesto intacto |
| T2 | si (solo `pointSize`) | default **11**, slider **3..15 step 1**, persistencia `readNumber(3,15,11)`, uniform `clamp(valor,2,30)`, tolerancia visual **<= 5%** de diametro |
| T3 | si (nucleo) | 6 casos obligatorios + 5 de la suite del web; **mismo orden de guardas** que `types.ts:393` |
| T4 | si | metodo fijo + **FPS(ON) >= 0.95 x FPS(OFF)** y techo efectivo **70 px** (`35 x min(dpr,2)`) |
| T5 | si (consumo) | `ColormapsPinsTest` ya sella 16 pines a **1e-4/canal**; `aFo` **<= 1e-9** |
| T6 | si | **4 capturas** obligatorias (T6-1..T6-4) + 1 opcional, ancladas por sha256 y firmadas por David |
| T7 | si | David firma, GLM hunk-a-hunk, merge solo David |

### 3. T3: las fronteras y los mutantes

Obligatorias: `2->2`, `30->30`, `1->2`, `31->30`, `-1->2`, `NaN->2`.
Anadidas de la suite del web: `0->2`, `11->11`, `99->30`. Derivadas: `+Inf->30`,
`-Inf->2`, `2.5->2.5`.

Mutantes (11) con el test que los mata: MUT-1 borrar la guarda `!(v>0)` (solo la
mata `NaN`), MUT-2 `v<2` a `v<3`, MUT-3 `30` a `31`, MUT-4 borrar la guarda
alta, MUT-5 `span` sin el `max(1.5, ...)`, MUT-6 `aFo` sin clamp, MUT-7 umbral de
pick `24` a `48`, MUT-8 quitar la guarda de arrastre de 6 px, MUT-9 quitar el
test de hemisferio oculto, MUT-10 uniform sin clamp, MUT-11 radio `1.012` a
`1.0`.

Declaro un **mutante equivalente**: `v<2` a `v<=2` no se puede matar (devuelve 2
en ambos casos) y no lo cuento como cobertura.

### 4. Correcciones documentales incluidas

**(a) `docs/TASKS.md` reparado.** El blob de main decodifica como UTF-8 pero es
doble codificacion. Reparacion determinista y sin perdida:

    s = blob.decode('utf-8')                 # 1605 chars, valido
    fixed = s.encode('cp1252').decode('utf-8')   # 1583 chars

No-ASCII resultante (unico): `U+00F3` x4, `U+00ED` x4, `U+2014` x3, `U+00E1` x2,
`U+00E9` x2, `U+00FA` x1, `U+2013` x1, `U+00F1` x1. Cero caracteres sustituidos
por `?`. Fichero escrito UTF-8 sin BOM, LF. Bytes 1653 -> 1947.

Filas corregidas: **R1** ("siguiente - Issue #2" -> cerrado) y **R3** ("R3.2
pendiente" -> "R3.0-R3.3 cerrados 2026-11-07; R3.4 pendiente (plan ...)").
Anadido un aviso de nomenclatura fases vs tracks.

**(b) "paridad-R5".** 5 lineas: 4 en `R4_RISK_AND_DECISIONS.md` (L5, L21, L32,
L33) y 1 en `GATE-E-VALIDATION.md` (L113). Numstat `8 4` y `1 1`; ninguna otra
linea se toca. **No he tocado el checker congelado**, que tiene 7 menciones a
"R5": renombrar dentro romperia la cadena de hashes. El glosario vive en
`docs/r3/README.md` y `docs/TASKS.md`, fuera del instrumento.

**D4** queda declarado **sin dueno** (su "R5 backlog" era el track). No lo
reasigno en este PR: propongo R6 o slice dedicado y lo dejo como decision de
David.

### 5. Hallazgos de la verificacion que corrigen supuestos previos

Los pongo porque contradicen lo que se dijo en rondas anteriores:

1. El grid de fo del web es **72x36 = 2592** muestras (`GRID_W/GRID_H` en
   `builders.ts:26-27`), no 60x60. El rango robusto de color de las estaciones
   sale de ese grid, no de las foF2.
2. **`GL_PROGRAM_POINT_SIZE` no existe en GLES.** Verificado contra
   `android.jar` de `android-35`: ausente en `GLES20`, `GLES30`, `GLES31` y
   `GLES32`; `GL_ALIASED_POINT_SIZE_RANGE` si esta (en `GLES20`, heredada por
   `GLES30`). Un `glEnable(GL_PROGRAM_POINT_SIZE)` habria sido un no-op
   silencioso; el riesgo real es no escribir `gl_PointSize` en alguna rama.
3. **`ColormapsPinsTest`** ya existe en main: 16 pines generados ejecutando
   `src/lib/iono/colormaps.ts` en `8cdc334`, tolerancia **1e-4/canal** (mas
   estricta que el 1/255 del contrato T5).
4. En el web, **`uHasData` y `uHighlight` nunca se actualizan** (unica
   asignacion: los inicializadores de `builders.ts:322-323`). La rama gris y el
   alpha 0.45 son codigo muerto: una estacion sin `foF2` se pinta con el cmap en
   `t=0`, alpha 0.95. El plan **replica el comportamiento efectivo** y pone la
   honestidad en el popup, no en el color del punto. "Arreglar" el web seria una
   divergencia con dictamen propio.
5. El `IonosondeAdapter` **ya esta en produccion** (`MainActivity.kt:77` ->
   `HudStore.kt:152` como `fof2Source`). El render no necesita camino de red
   nuevo: consume `HudStore.fof2()`. Eso hace C1 verificable por diff.

### 6. Lo que NO he hecho

- **No hay CI**: el commit es docs-only, no hay codigo que compilar y no hay run
  que ensenar. No lo presento como verde.
- **No he pusheado** la rama android ni abierto PR (falta autorizacion).
- **No hay gate de dispositivo**: no existe render todavia.
- No he tocado `data/**`, `app/**`, `.github/**` ni el checker.

### 7. Preguntas concretas para tu dictamen

1. Los numeros T1-T7 de la tabla, seccion 4 del plan, como pre-registro del
   slice: en particular **T4** (regresion 0.95 + techo 70 px) y **T2** (<= 5% de
   diametro). Son los dos que me he inventado yo; el resto los hereda del
   contrato o los he medido.
2. Aceptas que **no se reclame paridad de color** en R3.4 (formula identica,
   muestra distinta) hasta que exista el grid de fo del shell.
3. Aceptas el **contrato del popup** (seccion 8) tal cual: campos de
   `IonosondeStation`/`IonosondeData`, badge STALE, `Outcome.Cached` con edad,
   `Failure` sin puntos, y prohibicion de rellenar `foF2`/`muf3000`.
4. Aceptas la **reparacion de TASKS.md** y el **renombrado paridad-R5** con el
   checker intacto (7 menciones sin tocar).
5. **D4**: R6 o slice dedicado. No bloquea R3.4.
6. Algo del **reparto de PRs** (seccion 14) o de los **mutantes** (seccion 7.2)
   que quieras cambiar antes de que se escriba codigo.

### 8. Hashes y artefactos del relay

    to-glm/files/PLAN-R3.4-IONOSONDE-LAYER-20261113.md
      33262 B  sha256 45efac97cb432105d1d0d90d5fa426d8aaccdc54749ef263efd192320126127a
      ASCII puro, sin BOM, LF alineado con el blob de git (byte-identico)

    to-glm/files/r34-plan-08ed18f.patch
      42748 B  sha256 ec12ed34d300ae13be3d3a1d887701fb7d5987ea7818d9f75eac91c0d9f8abed
      git format-patch -1 08ed18f (parche completo del commit)

Si el patch y el plan no cuadran con el commit `08ed18f`, gana el commit: el
plan que revisas es el del parche.

**Resumen en una linea**: el plan cierra T1-T7 antes de codificar, declara las
tres decisiones que no pueden quedar a la implementacion (rango de color sin
grid, popup sin oraculo, techo de punto del driver), repara TASKS.md y renombra
el track de paridad sin tocar el instrumento congelado.
