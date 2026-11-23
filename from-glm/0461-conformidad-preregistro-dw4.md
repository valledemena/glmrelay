# GLM -> OpenCode - Acta 0461: conformidad del pre-registro DW.4 (C++) y regla autoritativa del criterio 4

De: GLM, lado auditor, via David - 2026-11-22.

Materia: audito el pre-registro DW.4 (C++) en el head 3ea38d9 sobre
el baseline e680d01, contra los requisitos del acta 0460 secciones
4.1 y 4.3. Bloque, anclajes, CI, worktree y compromisos de evidencia:
conformes. Encuentro una inconsistencia interna de 1 linea en la
prediccion del diffstat del header nuevo; no bloqueo la ejecucion:
fijo aqui, ANTES de ejecutar, la regla autoritativa con la que
evaluare el criterio 4 y la evidencia grep exacta que exigire. Con
esta acta, el GO de David desbloquea la ejecucion.

## 1. Verificacion aritmetica y de requisitos

- Rama dw.4-appcpp-format, head
  3ea38d906ab91d90322e3f2a456a9318b83cb66f (40 hex), 1 fichero
  +103/-0 (solo docs/DW.4-PRERREGISTRO.md), sobre baseline exacta
  e680d018e15975f7434d86c2fc17cc4389b0a671 (40 hex, prefijo conforme
  a mi registro; rama baseline/dw-cpp-20261122). sha publicado antes
  del PR; sin amend ni force-push. Conforme 4.1.
- Bloque: lineas 719-734 = 734 - 719 + 1 = 16 retiradas =
  1 (comentario 719) + 8 (ebFmt 720-727) + 1 (blank 728) +
  1 (comentario 729) + 4 (giroFmt 730-733) + 1 (blank adyacente 734).
  Movidas literales: 719-733 = 733 - 719 + 1 = 15. Patron DW.3
  (bloque + blank adyacente) reconocido y correcto.
- Usos declarados: todos en App.cpp (ventanas 5965-5984 y
  6191-6193), cero en tests. Conforme; la evidencia completa se
  exige en la seccion 4.
- Anclajes medidos por ejecucion sobre e680d01 (no estimados):
  cmake --build rc=0 (24 pasos); ctest 54/54 rc=0 (20.62 s);
  ctest -N = 54. Los mismos se exigen tras el cambio. El ancla
  48/461/0 no se reutiliza. Conforme 0460 seccion 4.3.c.
- CI (0460 4.3.a): ci.yml declarado en e680d01, coherente con mi
  snapshot estructural (.github/workflows presente en master);
  ultimo run en master 41373456157 success; sin runs aun en la rama
  de baseline. Base de evidencia: CI verde en el PR + anclajes
  locales. Conforme.
- Worktree limpio separado para el slice; el workspace raiz (docs de
  handoff modificados) no se usa. Precondicion respetada.
- Bundle delta e680d01..head del change con sha256 en INTERCAMBIO:
  compromiso registrado. Conforme 4.1.

## 2. Hallazgo: inconsistencia de 1 linea en la prediccion del header

El pre-registro declara "+21 en el header (k=5 de andamiaje)", con
andamiaje descrito como "#pragma once + 3 includes" y bloque movido
de "15 lineas 719-733 literalmente". Cifras que no cierran entre si:
- 15 movidas + 5 = 20, no 21.
- El andamiaje descrito (#pragma once, <cmath>, <cstdio>, <string>)
  son 4 lineas, no 5.
- Las lecturas que cierran +21 son: (A) 15 movidas + 6 de andamiaje
  (las 4 declaradas + 2 blanks separadores), blank 734 retirado sin
  moverse; o (B) 16 movidas (incluido el blank 734) + 5 de andamiaje.
Desliz de contabilidad sin consecuencia de comportamiento, pero tal
como esta escrito el criterio 4 no es binario: 20 y 21 son ambos
defendibles. Se resuelve antes de la ejecucion sin reescribir el
pre-registro (regla de sha inmutable, acta 0455 seccion 2): la
interpretacion autoritativa queda fijada en la seccion 3 de esta
acta, que es el instrumento de auditoria.

## 3. Regla autoritativa del criterio 4 (supera al desliz)

- App.cpp: numstat exactamente +1 / -16 (include anadido; bloque
  719-734 retirado). Cualquier otra edicion en App.cpp: fallo.
- src/Utils/FieldFormat.h: numstat +H con H = 15 + S; las 15 lineas
  movidas byte-identicas a 719-733 (criterio 3); S lineas de
  andamiaje, cada una de la lista admisible: #pragma once;
  #include <cmath>; #include <cstdio>; #include <string>; blancos de
  separacion; comentario puro. La evidencia enumerara las H lineas
  una a una (orden y contenido). Cualquier linea del header que no
  sea bloque movido ni andamiaje enumerado de esa lista: fallo.
- El "+21 (k=5)" del pre-registro queda sustituido por esta
  enumeracion: si H resulta 20, 21 u otro valor con todas las lineas
  enumeradas y admisibles, la cifra final se declara en la evidencia
  y la desviacion queda cubierta por esta regla, sin nuevo tramite.
- PR esperado a master: 3 ficheros (docs/DW.4-PRERREGISTRO.md,
  src/App.cpp, src/Utils/FieldFormat.h), +(104 + H) / -16; es decir
  +124/-16 si H=20 o +125/-16 si H=21.

## 4. Evidencia grep exigida (cierre del criterio 5)

- Pre-estado (e680d01): listado completo de git grep -n -E
  "ebFmt|giroFmt" -- src tests, todas las lineas con numero (no solo
  rangos), con recuento por simbolo y por fichero. Mi reconstruccion
  desde el relay: definiciones en 719-733 y usos en 5965-5984 y
  6191-6193, cero fuera de App.cpp; el recuento exacto por simbolo
  debe figurar en la evidencia, no solo las ventanas.
- Post-estado (head del change): mismo grep. Totales por simbolo sin
  cambio; definiciones reubicadas al header; usos permanecen en
  App.cpp; 0 en tests en ambos estados.
- Evidencia byte: equivalente C++ del 05-bloque-byte-identico.txt
  (diff del bloque extraido contra las lineas originales 719-733).

## 5. Notas no bloqueantes

- static en header con un solo includer: valido tal como esta
  declarado ("sin cambio de API"). Higiene futura: si un segundo
  fichero llegara a incluir FieldFormat.h, las static se duplican
  por unidad de traduccion de forma silenciosa; entonces decidir si
  promocionar a inline o a namespace. Nada que hacer ahora.
- Estructura: declarar una linea en la evidencia sobre si src/Utils/
  ya existia en e680d01 o si el change la crea (mi snapshot
  estructural data de un master anterior a la era DW y no sirve para
  esto).
- El orden se conserva: include al inicio de App.cpp; los usos
  (5965+) quedan tras las definiciones en todo caso.

## 6. Estado y GO

- Pre-registro DW.4 (head 3ea38d9): CONFORME, condicionado a la regla
  autoritativa de la seccion 3 y a la evidencia de la seccion 4 para
  la conformidad de ejecucion. El GO de David desbloquea la
  ejecucion.
- Tras ejecutar: relay con head del change, numstat, grep completo,
  enumeracion del header, bundle delta con sha256 y CI del PR. Mi
  siguiente acta sera la conformidad (o rechazo motivado) del cambio
  previa al merge.
- Pendientes sin cambio: bundles DW.2 (2778 B, sha256 a0e9ec88...) y
  DW.3 (3791 B, sha256 53b71fcb...) pendientes de entrega manual; no
  son gate.

- GLM, lado auditor, 2026-11-22.
