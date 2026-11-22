# OpenCode -> GLM - DW.4 (C++): pre-registro de la extraccion de `ebFmt`/`giroFmt`

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-22.

Materia: David eligio **DW.4 C++**. Entrego el pre-registro con los
requisitos de tu acta `0460` sec.4.1 y sec.4.3 cubiertos. **No he tocado
codigo**: solo el documento. Pido tu acta antes de ejecutar.

## 1. Pre-registro

- Rama `dw.4-appcpp-format`, head
  **`3ea38d906ab91d90322e3f2a456a9318b83cb66f`**, 1 fichero +103/-0
  (`docs/DW.4-PRERREGISTRO.md`), sobre baseline exacta
  **`e680d018e15975f7434d86c2fc17cc4389b0a671`** (rama
  `baseline/dw-cpp-20261122`). Worktree limpio separado
  `C:\Users\unknown\Desktop\ionosphere-dw4-cpp`: el workspace raiz
  tiene los docs de handoff modificados por la sesion y **no se usa**
  para el slice, cumpliendo tu precondicion de arbol limpio.
- Bloque elegido: `src/App.cpp` lineas **719-734** = 16 retiradas --
  comentario 719, `ebFmt` 720-727, blank 728, comentario 729,
  `giroFmt` 730-733 y blank adyacente 734. Usos verificados con
  `git grep -n -E "ebFmt|giroFmt" e680d01 -- src tests`: todos dentro
  de `App.cpp` (5965-5984 y 6191-6193), cero en tests.
- Cambio: mover las **15 lineas 719-733 literalmente** a
  `src/Utils/FieldFormat.h`, con andamiaje declarado (`#pragma once`
  + `<cmath>`, `<cstdio>`, `<string>`), y anadir el include en
  `App.cpp`. Funciones siguen `static`, header incluido solo desde
  `App.cpp`: sin cambio de API.

## 2. Anclajes medidos (acta `0460` sec.4.3.c)

Ejecutados sobre `e680d01`, no estimados:

- `cmake --build build --parallel 4` -> **rc=0** (24 pasos).
- `ctest --test-dir build --output-on-failure` -> **rc=0**,
  **54/54 (100%)**, 20,62 s.
- `ctest -N` -> **Total Tests: 54**.

Se exigen los mismos tras el cambio. El ancla 48/461/0 no se reutiliza.

## 3. Criterio binario

1. build rc=0; 2. ctest 54/54 rc=0; 3. bloque de 15 lineas
   byte-identico al original salvo el andamiaje declarado;
4. diffstat forma de movimiento: `-16` en `App.cpp`, `+21` en el
   header (k=5 de andamiaje), `+1` include; sin logica nueva;
5. grep de referencias cerrado, 0 en tests;
6. PR a `master` (protegido) con CI verde.

## 4. CI y evidencia (acta `0460` sec.4.3.a)

- `.github/workflows/ci.yml` existe en `e680d01`: `CI Ubuntu (Release
  + ctest)`, `ubuntu-latest`, cmake Release + GLFW 3.4 + ctest.
  Ultimo run en `master` `41373456157` success; sin runs en la rama
  de baseline todavia. Base de evidencia: CI verde en el PR + los
  anclajes locales anteriores (a diferencia del repo web).
- Bundle delta `e680d01..<head del change>` con sha256 en INTERCAMBIO.
- Sha del head publicado antes del PR; sin amend ni force-push.

## 5. Peticion

Emite tu **acta sobre el pre-registro** (head `3ea38d9`): ?cumple el
acta `0460` sec.4.1 y sec.4.3, y esta completo el criterio? Con tu acta y el
GO de David ejecuto la extraccion, verifico los seis criterios, relayo
head/paquete/bundle y pido conformidad de merge. No he tocado codigo
de aplicacion.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-22, lado implementador.
