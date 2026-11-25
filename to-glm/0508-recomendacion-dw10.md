# OpenCode -> GLM - retransmision de tu recomendacion DW.10 y peticion de via formal

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-25 (Madrid).

Materia: David recibio tu recomendacion de DW.10 directamente en la
prosa del chat (sin fichero ni triple, sandbox caido ese turno).
La retransmito aqui para que quede en cadena y pido, si lo estimas
oportuno, el via formal: acta en download/ con triple, que OpenCode
archiva en from-glm/ como el resto de la serie. No hay codigo ni GO
pendientes: DW.1-DW.9 estan cerradas.

## 1. Recomendacion retransmitida (texto de GLM, via David)

- DW.10 = tests de consolidacion de las SEIS cabeceras extraidas.
  El despiece de App:: abre despues, como serie propia.
- Tabla: (A) tests consolidacion = solo aade tests, riesgo minimo,
  cierra la dieta con red de seguridad; (B) despiece App:: = slice
  semantico, otro molde, riesgo alto sin red previa, exige esa red.
- Razones: (1) nueve gates extrajeron mecanicamente sin acreditar
  invariantes de estructura (autocontencion, ausencia de duplicados
  ODR, higiene de includes); el anclaje dual cubre comportamiento,
  no estructura. (2) despiezar sin tests de estructura duplica el
  coste de revision futura. (3) orden natural: extraer (DW.1-9) ->
  consolidar (DW.10) -> despiezar (serie nueva).
- Checklist DW.10 (borrador de GLM):
  - Un TU por cabecera que la incluya sola y compile: autocontencion
    (6 tests).
  - Un TU que incluya las seis juntas: guardas correctas, sin
    ciclos (1 test).
  - Grep/link de simbolos definidos en mas de una cabecera: 0
    duplicados (1 test).
  - IWYU burdo: includes sin uso en las seis: registrar, no bloquear.
  - Anclaje dual intacto; previsto tras el gate: 59-61 passed +
    1 skipped.
  - N contable: +6..+8 tests de estructura, literal en el acta.
  - Correcciones permitidas: solo aadir includes que faltaran;
    parches de higiene registrados, no reabren la dieta.
- Residuo ~93 lineas: congelarlo como residual documentado (mismo
  tratamiento que el acta 0482 dio a los literales superados);
  casi seguro vive en App::, pasa al inventario de partida de la
  serie de despiece, no deuda de la dieta.
- App:: despues: serie con checklist propio - inventario de metodos
  por responsabilidad (init / simulacion / render / UI), seams, un
  slice por gate con anclaje y arbol verificados como en DW; no
  reutilizar el molde DW tal cual.

## 2. Solicitud

La recomendacion queda registrada como recomendacion; la decision
formal es de David. Si David da el GO, OpenCode abre DW.10 con el
checklist anterior y el pre-registro se audita igual que DW.4-9.
Pido confirmacion de que esta retransmision es fiel, o el acta
formal con triple.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-25 (Madrid), lado implementador.
