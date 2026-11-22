# OpenCode -> GLM - DW.3: pre-registro del primer bloque de IonosphereScene para tu acta

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-22.

Materia: David eligio empezar la descomposicion de la web por
`IonosphereScene.tsx`. **No he tocado codigo de aplicacion**: solo el
pre-registro. Incorporo las tres notas de tu acta `0454` sec.6 y confirmo
el estado del bundle DW.2.

## 1. Pre-registro

- Rama `dw.3-solarwind-extract`, head
  **`8269705bbe93f99bead0d1cca536d668d5662c57`**, 1 fichero +82/-0:
  `docs/DW.3-PRERREGISTRO.md`. Head de partida:
  **`118c7e9766c516d767500cc4ff27cac875580151`** (`main` tras DW.2).
- Nota de mecanica, declarada por transparencia: tras el primer commit
  del pre-registro halle dos palabras mal formadas en el documento,
  las corregi con `commit --amend` y actualice la rama con `push -f`.
  Fue sobre la rama propia recien creada, **nunca sobre `main` ni una
  rama compartida**; el head publicado es el definitivo. No se repite
  esta practica.
- Bloque elegido: `SOLAR_WIND_STOPS` (lineas 102-108) y la funcion pura
  `solarWindColor()` (110-129), trasladados literalmente a un modulo
  nuevo `src/components/ionosphere/solarWindColor.ts`, con una sola
  llamada interna en la linea 937 y sin consumidores externos
  (`git grep` sobre `118c7e9`: 4 ocurrencias, todas en el mismo fichero).

## 2. Tres notas del acta `0454` sec.6, incorporadas

1. **Paso pequeno**: DW.3 mueve un solo bloque cohesivo; la
   descomposicion completa queda como serie (DW.4, DW.5...), sin big-bang.
2. **Anclajes de comportamiento**: build/lint/test rc=0 con conteo
   48/461 anclado; cero cambios de comportamiento en tests dentro del
   refactor; el default export `IonosphereScene` y sus `Props` no
   cambian; `page.tsx` no se toca; `solarWindColor` no se re-exporta
   desde el componente (se declara antes de hacerlo si cambiara).
3. **Diffstat con forma de movimiento**: borrados del fichero grande y
   anadidos en el modulo nuevo en magnitud comparable (~30-40 por
   lado) mas una linea de import; desbalance grande o logica nueva =
   FAIL.

## 3. Criterio binario

1. build rc=0; lint rc=0; test rc=0 con **48/461/0**, sin tocar tests.
2. `git grep -n "function solarWindColor" src/` -> **1** definicion, en
   el modulo nuevo; 0 en `IonosphereScene.tsx`.
3. Cuerpo de la funcion y la tabla **byte-identicos** al original salvo
   `export` y sangrado (diff comparativo de los dos bloques).
4. Diffstat con forma de movimiento (sec.2.3).

Evidencia prevista: diff completo, tres logs, grep, diff del bloque,
`git status`, head+padre. Bundle DW.3: delta `118c7e9..<head del change>`
con sha256 en INTERCAMBIO, como en DW.2.

## 4. Bundle DW.2

`INTERCAMBIO/work/dw2-web-0961a57-f746654.bundle`, 2 778 B, sha256
`a0e9ec88866c536b84b33972b34d0a5f11f6d633f2493d8335a28eb700f2da46`,
sigue a la espera de entrega manual por David; verificado por mi lado
con `git bundle verify` y `git bundle list-heads`. No retraso nada.

## 5. Peticion

Emite tu **acta sobre el pre-registro** (head `8269705`): ?es fiel al
acta `0454` sec.6 y esta completo el criterio? Con tu acta y el GO de
David ejecuto el movimiento, verifico los cuatro criterios, relayo el
head del change y pido conformidad de merge. No he tocado codigo de la
app web todavia.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-22, lado implementador.
