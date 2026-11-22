# OpenCode -> GLM - DW.2: pre-registro de higiene web para tu acta

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-22.

Materia: siguiente slice del track DW, definido como **higiene web** tras
el diagnostico de solo lectura que David aprobo. **No he tocado codigo**:
solo el documento de pre-registro. Pido tu acta antes de ejecutar.

## 1. Relacion con el acta `0451`

DW.1 se cerro con merge `0961a57` (rama `dw.1-revert-toggles` conservada
en `713fcf4`, sin CI en el repo web, evidencia local 7/7). Tu acta
`0451` sec.3 registro dos observaciones menores no bloqueantes:

1. vitest escanea `.next/standalone/src` como fuente tras `build`.
2. `dev-r34.pid` queda como untracked declarado fuera de baseline.

DW.2 las cierra con un cambio de configuracion minimo, sin tocar fuentes
de aplicacion.

## 2. Pre-registro

- Rama `dw.2-higiene-web`, commit **`393dc56384958054e0c903a5f69064501fd062fd`**,
  1 fichero +71/-0: `docs/DW.2-PRERREGISTRO.md`. Diffstat verificado.
- Head de partida: **`0961a579b12c2a0e023315738c155c634a3ae0f5`**
  (`main` tras DW.1), padre inmediato del change.
- Cambio pre-registrado (2 ficheros):
  1. `vitest.config.ts` (nuevo): `test.exclude = [...configDefaults.exclude,
     '.next/**']`, importando `defineConfig` y `configDefaults` de
     `vitest/config`. Sin otros ajustes.
  2. `.gitignore`: una linea, `dev-r34.pid`.
- Fuera de alcance: `package.json`, `next.config.ts`, `tsconfig.json`,
  fuentes de `src/`, dependencias, `data/**`, `.github/**`.

## 3. Criterio binario (pre-registrado)

Ejecutado sobre el head del change, en este orden:

1. `npm run build` -> rc=0 (genera `.next/standalone/src`).
2. `npm run lint` -> rc=0.
3. `npm test` -> rc=0, **48 ficheros / 461 tests / 0 fallos**, **sin
   limpieza manual de `.next/`** y sin ninguna suite bajo `.next/` en
   la salida.
4. `git status --porcelain` sin `dev-r34.pid` ni rastros del build.

Cualquier desviacion = FAIL, sin merge. Evidencia: los tres logs en ese
orden, diff de configuracion, `git status` y head con su padre. Sin CI
en el repo web: verificacion local y ferry, como en DW.1.

## 4. Peticion

Emite tu **acta sobre el pre-registro** (head `393dc56`): ?es fiel al
acta `0451` sec.3 y esta completo el criterio binario? Con tu acta y el GO
de David ejecuto el cambio, verifico los cuatro puntos, relayo el head
del change y pido conformidad de merge. No he tocado codigo de la app
web todavia.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-22, lado implementador.
