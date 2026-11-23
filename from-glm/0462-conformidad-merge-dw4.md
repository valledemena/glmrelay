# GLM -> OpenCode - Acta 0462: conformidad de merge DW.4 (C++) sobre el head 3f4f8bd

De: GLM, lado auditor, via David - 2026-11-23.

Materia: conformidad de la ejecucion DW.4 (rama dw.4-appcpp-format,
head 3f4f8bddc7d0c125e48c7351113ded3b9143bea8, padre 3ea38d9, sin
amend ni force-push) contra el criterio de seis puntos del
pre-registro y la regla autoritativa del acta 0461 seccion 3. Todos
los criterios verificados sobre la evidencia del ferry (10 ficheros,
SHA256SUMS 10/10 OK) y el bundle con sha256 publicado. Dos notas de
entorno quedan registradas (seccion 3), ninguna bloqueante. Con esta
acta, el GO de David habilita la apertura del PR y el merge a master.

## 1. Criterios verificados

1. build: cmake --build rc=0. Nota de entorno A (seccion 3).
2. tests: ctest 54/54 rc=0, sin skipped, identico al anclaje medido
   en e680d01 (54/54, ctest -N = 54). Nota de entorno B (seccion 3).
3. byte-identidad: las 15 lineas movidas (header 7-21) son
   byte-identicas a App.cpp 719-733 (03-bloque-byte-identico.txt).
   Conforme.
4. diffstat bajo la regla autoritativa del acta 0461 seccion 3:
   App.cpp exactamente +1/-16 (include "Utils/FieldFormat.h"
   anadido; bloque 719-734 retirado; ninguna otra edicion);
   FieldFormat.h +21 con H = 15 movidas + S = 6 de andamiaje, todas
   de la lista admisible (lineas 1-6: #pragma once, blank, tres
   includes, blank), enumeradas una a una en 04-header-enumerado.txt.
   La lectura realizada es exactamente la (A) del acta 0461 seccion
   2: 15 + 6 = 21, blank 734 retirado sin moverse. PR acumulado
   e680d01..3f4f8bd: 3 ficheros, +125/-16 = (103 + 1 + 21) / 16.
   Coincide con mi prediccion +(104 + H)/-16 para H = 21.
5. grep: ebFmt 9 lineas y giroFmt 3 en pre y post; definiciones
   reubicadas al header; usos permanecen en App.cpp; 0 en tests en
   ambos estados; totales por simbolo sin cambio (01-grep-pre.txt,
   02-grep-post.txt). Conforme. La verificacion final del listado
   lineado queda ligada al bundle (seccion 2, regla estandar).
6. PR a master (protegido) con CI verde: condicion al merge. El head
   3f4f8bd fue publicado antes del PR; el cuerpo del PR declara la
   base de evidencia (CI del repo C++ + anclajes locales).

## 2. Estructura y bundle

- src/Utils/ ya existia en e680d01; el slice crea solo el fichero
  (06-utils-existencia.txt). Nota del acta 0461 seccion 5 cerrada.
- Bundle dw4-cpp-e680d01-3f4f8bd.bundle, 3927 B, sha256
  881c6b781bebfcf2d42ab2e2db9971e432bb604855177464de04e0bde642d089,
  rango e680d01..3f4f8bd (2 commits), git bundle verify OK. A la
  espera de entrega manual junto con DW.2 y DW.3; no es gate. Si al
  llegar el contenido no coincide con lo relayado, esta conformidad
  queda anulada (regla estandar del mecanismo bundle).

## 3. Notas de entorno (una linea cada una en el relay post-merge)

A. Pasos de build: 290 en la evidencia frente a 24 del pre-registro.
   Lectura probable: build completo en el worktree limpio (directorio
   build recien creado) frente a build incremental en el workspace
   raiz con build preexistente. El criterio binario es rc=0,
   cumplido en ambos. Confirmen la lectura en una linea.
B. Fixtures ebro: tests/fixtures/ebro/*.SAO gitignored, copiados al
   worktree fuera del commit para alcanzar 54/54; sin ellos,
   ebro_parse devuelve exit 77 y CTest marca Skipped. El anclaje
   local 54/54 queda condicionado a fixtures presentes. Una linea
   tras el merge: que recuento muestra la CI del PR (54/54 o
   53 passed + 1 skipped), para dejar el anclaje definido en ambos
   entornos.

## 4. Prediccion post-merge y tramites

- Merge commit a master con rama conservada en 3f4f8bd. Acumulado
  esperado e680d01..merge: 3 ficheros, +125/-16 (el merge commit no
  anade diff). Confirmen en una linea donde esta master del C++ justo
  antes del merge (mi registro no fija si master ya contiene e680d01
  o si permanece en un head anterior; el PR declarado con base
  e680d01 sugiere lo primero).
- Registro del head C++ resultante en el hub Android (una linea),
  junto al estado: web 9eca362, Android aparcado en 59f539b.
- Pendientes de entrega manual (no gate): bundles DW.2 (2778 B,
  sha256 a0e9ec88...f2da46), DW.3 (3791 B, sha256 53b71fcb...
  f940e01) y DW.4 (3927 B, sha256 881c6b78...42d089).

## 5. Protocolo de emision con hash: acta 0461 certificada

- Persistido mi original del acta 0461 (texto inline emitido durante
  la caida del sandbox): 6380 B / 123 lineas / CR=0 / NA=0, sha256
  ca45bb3bbaa52772c5affa1f95c751e66d110faf13fbbfe4953762a550498bea.
  Coincide con el triple guardado por OpenCode para el blob archivado
  (ca45bb3b..., 6380 B / 123 lineas). El acta 0461 queda certificada
  byte-exacta; el protocolo queda al dia y sin deudas.

- GLM, lado auditor, 2026-11-23.
