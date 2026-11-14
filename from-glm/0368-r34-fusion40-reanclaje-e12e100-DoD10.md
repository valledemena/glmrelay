# GLM -> R3.4 - Fusion #40 registrada; tercer momento re-anclado en `e12e100`; DoD 10 listo para publicar

De: GLM - 2026-11-14 - asunto: registro la fusion del PR #40 (docs-only) y
cierro mi parte pendiente del paquete R3.4. El re-anclaje del tercer momento
queda HECHO sobre `e12e100` y extendido a `main` = `52543ab`; entrego ademas el
texto final del comentario de cierre de #15 (DoD 10) en fichero aparte, listo
para publicar. Una correccion de registro: el SHA largo de `e12e100` que me
llego por chat tenia un digito erroneo; el canonico termina en `456aa6` y el
T7 publicado ya lo cita bien.

Numeracion: `from-glm/0368` si David archiva (asumo to-glm 0364/0366/0367
consumidos por las correcciones finales y los dos avisos de fusion; el ajuste
final de numeracion es suyo).

---

## 1. Fusion #40 - verificada de forma independiente

    estado      MERGED (verificado en la pagina del PR)
    titulo      "docs: cerrar R3.4 (DoD 10)"
    merge       52543abc0b0339b162c8365e416cffe55e0f0b7e  (= main actual,
                verificado en commits/main)
    head        829a730994b7c5b5f2a96e50742f4e2f46e367ea
    base        e12e100a39025ea73b23c7d55e7a13285f456aa6
    CI          run 43590444822 sobre 829a730, completado con exito
                (assembleDebug / lint / unitTest presentes en la pagina del run)
    diff        reconteo GLM linea a linea del .diff publico: 2 ficheros,
                docs/TASKS.md (+1/-1) y docs/r3/README.md (+10/-3) = +11/-4
                -- cuadra exactamente con lo declarado
    alcance     SOLO docs; sin codigo, sin data/**, sin .github/**, sin checker
    merge       con --match-head-commit segun reporte: head 829a730 firmado una
                vez, sin re-firma (efecto verificado: el head mergeado es el
                head revisado)

Contenido del diff (leido completo, nada mas que esto): la fila R3 de
TASKS.md pasa a "**cerrado 2026-11-14**" citando PR #39 merge `e12e100`, gate
T4/T6 umbral 29,5 y T7; el README de r3 cierra R3.4 con las cifras del gate
(medium desenchufado 29,52/29,54; ratio 1,0008; low 29,90; punto <=70 px),
cita acta y capturas ancladas, enlaza el T7 y anade el parrafo final "R3 -
Escena v1 queda completo... El cierre administrativo de #15 se publica
aparte". Correcto y suficiente para la mitad documental del DoD 10.

## 2. Correccion de registro - SHA largo de `e12e100`

El largo que me llego por chat decia `e12e100a...85f458aa6`. El canonico es
`e12e100a39025ea73b23c7d55e7a13285f456aa6`. Verificado por cuatro vias
independientes:

1. redirect de la pagina del commit (github.com/.../commit/e12e100);
2. campo base del PR #40;
3. resolucion en raw.githubusercontent.com (el variante `...458aa6` da 404, el
   canonico da 200);
4. el texto del T7 publicado (pull/39#issuecomment-6875951335), que ya lleva
   el largo correcto.

El corto `e12e100` usado en TASKS.md, README y T7 es correcto y no cambia. No
hay nada que tocar en GitHub. Accion unica: revisar los borradores locales
(incluido el comentario de #15 preparado en el INTERCAMBIO) por si arrastran
el variante `...458aa6`.

## 3. Re-anclaje del tercer momento - HECHO en `e12e100`

    blobs congelados en e12e100 (canonico, verificado hoy):
      docs/r3/PLAN-R3.4-IONOSONDE-LAYER.md   34657 B  sha256 10566f61c56ee066...
      docs/r4/tools/R4_DISPLAY_CHECK_v6.py    46114 B  sha256 5a48cb189c33b7a4...
    == digests fijados pre-merge; identicos a como los verifique en
       b6afd24 / c5f1121 / 23bb047

    en main = 52543abc0b0339b162c8365e416cffe55e0f0b7e: ambos ficheros
    byte-identicos a e12e100 (comparacion directa). Las fusiones #39 y #40 no
    movieron ni un byte del plan ni del checker.

    padres de e12e100: 608ae834be079e3145c385ccf8ecd11767600b9c (main/base) +
    23bb04715b95a752f34eac8353ef36e0f0fdd85b (head firmado) - estructura de
    merge exacta.

    T7 presente en #39: pull/39#issuecomment-6875951335, con el registro
    completo (acta final b662596e..., raws anclados en 2c385c3, capturas,
    nota de recomputo en 928d3e3, global 5 min ~28,7 con 28,82 declarado y
    28,68 recomputado - no decisor).

Resolucion de la pregunta pendiente: **el tercer momento queda anclado en
`e12e100`** - el commit donde el codigo de R3.4 llego a main con gate T4/T6
29,5 y T7. `52543ab` es una capa administrativa de solo documentacion que NO
desplaza el anclaje: se registra como testimonio posterior (la mitad
documental del DoD 10), no como momento de cierre. La regla que lo sostiene:
los momentos de la cadena corresponden a estados del codigo auditado, y un
diff docs-only no altera el artefacto auditado (verificado: blobs congelados
identicos, cero toques de data/workflows/checker).

Estado de docs verificado en main (post-#40): fila R3 de TASKS.md = "cerrado
2026-11-14"; README de r3 con R3.4 cerrado citando `e12e100`, umbral 29,5,
medium 29,52/29,54, ratio 1,0008, low 29,90, punto <=70 px, acta y capturas
ancladas, T7 enlazado; parrafo "R3 queda completo" con el cierre
administrativo de #15 anunciado aparte.

## 4. DoD 10 - ejecucion

DoD 10 del plan (seccion 11): "`docs/r3/README.md` actualizado y #15
actualizado con el estado real". La mitad documental esta hecha y verificada
(PR #40, main `52543ab`). Falta la mitad del tracker: **#15 sigue OPEN**
(verificado hoy en la pagina del issue).

Sobre el "publicarlo queda para ti": no tengo credenciales de escritura en el
repo, y mi disciplina en R3.4 ha sido sin push, sin merge y sin publicar por
mi parte - la ejecucion la hace el lado con credenciales, como con el T7
(texto GLM 0365, publicacion de David). Lo que si puedo hacer, y hago ahora:
entrego el **texto final del comentario de cierre** en fichero aparte
(`issue15-cierre-R3.4-COMENTARIO-FINAL-GLM-20261114.md`), actualizado al
estado post-#40, listo para publicar tal cual. Si se prefiere publicar el
borrador local del INTERCAMBIO, verificar antes dos puntos:

1. que refleje el main actual tras #40 (`52543ab`) y la fila R3 ya cerrada;
2. que el SHA largo de e12e100 sea `...456aa6`, no `...458aa6` (seccion 2).

Con el comentario publicado y el issue cerrado, R3.4 queda cerrado al 100%
(DoD 1-10) y el tracker R3 (#15) queda cerrado con la cadena completa.

## 5. Archivo de dictamenes - peticion renovada

`from-glm/` sigue terminando en 332. Pido archivar: 0351, 0353 (los dos de la
ronda pre-gate), 0360, 0363, 0365 (texto T7) y el presente (0368 si la
numeracion sigue como asumo). El rastro de auditoria del cierre los necesita.

## 6. Estado final de la cadena R3.4 (post-#40)

- Codigo: head firmado `23bb04715b95a752f34eac8353ef36e0f0fdd85b`; base
  `608ae834be079e3145c385ccf8ecd11767600b9c`; merge #39
  `e12e100a39025ea73b23c7d55e7a13285f456aa6` (padres verificados); merge #40
  `52543abc0b0339b162c8365e416cffe55e0f0b7e` (docs-only, head
  `829a730994b7c5b5f2a96e50742f4e2f46e367ea`); **main = `52543ab`**.
- CI: run `43481739755` (3/3, citado en T7) y run `43590444822` (3/3, #40).
- Gate T4/T6: umbral enmendado 29,5 (voz de David en T7); medium desenchufado
  29,52/29,54 fps; ratio ON/OFF 1,0008; low 29,90; punto <=70 px.
- Acta final `b662596e951379b2b6c985a1efd8c1c8da6e310029444101602d9c335f42b6f3`
  (nota de recomputo en relay `928d3e3`; raiz `2c385c3`).
- Raws desenchufados anclados en `2c385c3`: 270 `a73d81b2...`, 5min2
  `332f3ce7...`, resumen `e71c0f86...`.
- Capturas: t6-1 `009b2f35...`, t6-2 `f4229b1c...`, t6-3 `1c0b77e6...`,
  t6-4-pq052 `1f94e267...` (+ jr055 `d17d211d...`), lado a lado v2
  `d4f5c6dc...` (procedencia del panel certificada por GLM: identidad bit a
  bit con t6-1, from-glm/0365).
- Blobs congelados: plan `10566f61...` (34657 B), checker `5a48cb18...`
  (46114 B) - identicos en `e12e100` y en `main`.
- T7: `pull/39#issuecomment-6875951335`.
- Relay (reporte de esta ronda): `ca3ac3e`.

## 7. Lo que falta (una sola pieza + archivo)

1. [lado con credenciales] Publicar el comentario final en #15 y cerrar el
   issue (texto entregado; o borrador local verificado contra los dos puntos
   de la seccion 4).
2. [David, cuando quiera] Archivar los dictamenes (seccion 5).

Nada mas pendiente de mi parte en R3.4. Tras #15, la siguiente fase del
tablero es R4 (Tiempo y profundidad), pendiente segun TASKS.md.

GLM - 2026-11-14
