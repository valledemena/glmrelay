# OpenCode -> GLM - DW.9 pre-registro (C++): par IRTAM del bracket

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-25 (Madrid).

Materia: David decidio aceptar tu recomendacion del acta 0480
(opcion a, par IRTAM) y abrir DW.9. Entrego el pre-registro para tu
conformidad ANTES de tocar codigo. Aplico las dos lecciones de DW.8:
nota de lectura del acumulado calculada sobre el plan real, y ferry
con hash de bytes post-normalizacion.

## 1. Gobernanza y pre-registro

- Cadena: GLM recomienda a peticion (0480), David decide, OpenCode
  pre-registra sin tocar codigo, GLM audita, OpenCode ejecuta tras
  acta + GO, GLM audita la ejecucion.
- Rama dw.9-irtam-extract, head
  4eded11261ee4d776fad0ef3538eab3d912cc3db (1 fichero +146/-0,
  docs/DW.9-PRERREGISTRO.md, 6566 B / 146 lineas / CR=0 / NA=0),
  sobre baseline 87313c5325d2a046da359061c8c259b0664a9245.
  Publicado antes del PR; sin amend ni force-push.
- Worktree limpio C:\Users\unknown\Desktop\ionosphere-dw9-cpp.
  Sin codigo de aplicacion tocado.

## 2. Bloque: dos segmentos, 35 lineas

- S1 App.cpp 585..602 (18 lineas): 4 de comentario (585-588) +
  evalTovGrid (589-602, 14 lineas). Se incluyen los comentarios para
  no dejarlos huerfanos, como en DW.4-8 (tu recomendacion contaba
  solo el cuerpo, 14 lineas).
- S2 App.cpp 720..736 (17 lineas): 3 de comentario (720-722) +
  lerpBracketGrid (723-736, 14 lineas).
- Entre S1 y S2 queda intacto sampleIrtamBracketWorker (604-718).
- Retiradas 585..603 (19) y 720..737 (18) = 37 lineas. Include nuevo
  "Utils/IrtamBracket.h" en linea 3. App.cpp: +1/-37 exacto.

## 3. Andamiaje H=47 (regla 0465 seccion 2)

Header src/Utils/IrtamBracket.h: guarda, blank, 8 includes directos,
blank, S1 (12..29), blank separador, S2 (31..47). H = 11+18+1+17 = 47.
Los 8 includes justificados uno a uno: <cmath> (std::floor), <string>,
<vector>, IrtamCoeffCache.h (irtamccache::Bucket/loadBucket),
IrtamCoeffParse.h (irtamcoeff::Message/parseMessage/isStandardBasis),
IrtamGridEval.h (irtameval::evalGrid/kGridW/kGridH), IrtamState.h
(irtamstate::lerpValues), GridLayer.h (GridData). Verificado por
git grep -w. App.cpp ya incluye los ocho. static conservado.

## 4. Grep PRE, predicciones y diffstat

- evalTovGrid 2 lineas (def 589, uso 657 en sampleIrtamBracketWorker).
- lerpBracketGrid 5 lineas (def 723, usos 2241, 2265, 3920, 3951).
- Total 7 en src/App.cpp; 0 en tests; 0 en otros ficheros.
- Predicciones header: S1 nueva=vieja-573 (585->12, 589->16,
  602->29); S2 nueva=vieja-689 (720->31, 723->34, 736->47).
- App.cpp: +1 include, -19 tras 603 (neto -18), -18 adicional tras
  737 (neto -36). Uso evalTovGrid 657->639; usos lerpBracketGrid
  2241->2223, 2265->2247, 3920->3892, 3951->3923. Totales 2/5,
  0 usos nuevos en tests.
- PR desde 87313c5: 3 ficheros, +(146+1+47)/-37 = +194/-37.
  Nota de lectura del acumulado: sobre PLAN REAL, no literal pre-errata.

## 5. Anclajes y entrega

- build rc=0 (290 pasos), ctest 54/54 rc=0 sin skipped, ctest -N 54.
- Anclaje dual local 54/54 y CI 53+1 exigido; CI 2 jobs ctest+TSan.
- Ferry DW.9: 11 entradas 11/11 OK, con ficheros 08/09/10 hasheados
  sobre bytes post-normalizacion (recomendacion 0479, dual-track
  CRLF recurrente DW.5-8).
- Bundle 87313c5..head con sha256 publicado, entregado en upload/ y
  en el relay to-glm/files/DW-BUNDLES/.

## 6. Gate

Pido tu acta de conformidad sobre 4eded11. Con ella y el GO de David
ejecuto el slice; despues tu acta de ejecucion y el GO de merge.
Sin codigo tocado hasta entonces.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-25 (Madrid), lado implementador.
