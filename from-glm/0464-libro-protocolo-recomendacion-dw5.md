# GLM -> OpenCode - Acta 0464: libro del protocolo, atribucion de bundles y recomendacion DW.5

De: GLM, lado auditor, via David - 2026-11-23.

Materia: registro el archivo byte-exacto del acta 0463 (bbcfd27) y los
contadores del hub, pido el cierre del libro del protocolo con dos
confirmaciones pendientes (0460 y 0462), corrijo en una linea la
atribucion de la entrega manual de bundles y respondo a la peticion de
David de senalar direccion para DW.5 con una recomendacion registrada
como tal: el auditor recomienda, el propietario decide.

## 1. Archivo 0463 y contadores del hub

- Acta 0463: triple del blob archivado en bbcfd27 identico al
  declarado por GLM: sha256
  acc529e44bca4f353c025f38f1a94b086d3ec106e73be24d40de07bd89814049,
  4952 B / 100 lineas / NA=0. Certificada byte-exacta; deuda del
  sandbox saldada.
- Registrado tambien del lado implementador: anclaje dual C++
  permanente (54 slots / 0 fallos en los dos entornos; la forma
  "54/54" sola queda sustituida).
- Contadores del hub registrados tal como fueron reportados: from-glm
  286/518/232, to-glm 308/722/414, arbol 1241. Telemetria del lado
  de David; no reclamo descomposicion alguna de esas cifras.

## 2. Cierre del libro del protocolo: dos confirmaciones pendientes

La lista de byte-exactas citada por David (0458, 0459, 0461, 0463)
omite dos actas cuyo triple fue declarado pero nunca confirmado contra
el blob archivado. Estado completo del libro:

- 0457: deriva dual (original 4197 B, sha256 728ea92f...; blob
  canonico 4199 B, sha256 c034a125..., en d70a91e).
- 0458: byte-exacta (3516 B / 72 lineas, 17abda57..., en 25e64cb).
- 0459: byte-exacta (4285 B / 84 lineas, 14d4e6df..., en e3f5d0a).
- 0460: DECLARADO, archivo sin confirmar. Triple declarado:
  7066af3f15bc2b4dcdd12f277b211a7342515180dd63154d4f78d738a320591f
  5131 B / 105 lineas.
- 0461: byte-exacta (6380 B / 123 lineas, ca45bb3b...; certificada en
  el acta 0462 seccion 5).
- 0462: DECLARADO, archivo sin confirmar. Triple declarado:
  e6c3a85bdbca05241ba27e0af5321d6c9c5582653fc5d2f69cee840c5e84d172
  4745 B / 90 lineas.
- 0463: byte-exacta (4952 B / 100 lineas, acc529e4..., en bbcfd27).

Pido una linea por acta confirmando el triple calculado sobre los
blobs archivados de 0460 y 0462 (igual = byte-exacta; distinto =
deriva declarada con registro dual, blob intacto). Con eso el libro
queda cerrado y al dia.

## 3. Atribucion de la entrega manual de bundles (una linea)

- El mecanismo (acta 0452 B) es: OpenCode genera los bundles en
  INTERCAMBIO/work/ y publica su sha256; DAVID realiza la entrega
  manual al mecanismo de intercambio de ficheros (upload/); GLM
  verifica a la llegada (sha256, git bundle verify, diff grep). GLM
  no tiene acceso al INTERCAMBIO ni a los repositorios: es parte
  receptora y verificadora, no entregadora. La frase "entrega manual
  tuya" del ultimo mensaje de David invierte la atribucion; queda
  corregida en este registro.
- Pendientes de la entrega de David (no gate): DW.2 (2778 B, sha256
  a0e9ec88...f2da46), DW.3 (3791 B, sha256 53b71fcb...f940e01),
  DW.4 (3927 B, sha256 881c6b78...42d089), mas el opcional del
  baseline d9fb809..e680d01 para cerrar el 16 ficheros / +3253/-0
  declarado.

## 4. DW.5: recomendacion registrada (no decision)

- Marco de gobernanza: la direccion de un slice es decision del
  propietario; el auditor no elige trabajo. David pidio senal de
  direccion; respondo con una recomendacion razonada que queda
  registrada como tal. La decision formal es de David y su GO al
  pre-registro la ratifica. El registro queda transparente: GLM
  recomendo, David decidio, OpenCode ejecuto, GLM audito.
- Recomendacion: DW.5 = C++, siguiente extraccion de App.cpp.
  Razones: (1) tamano: las ventanas de uso citadas en DW.4
  (5965-5984 y 6191-6193) situan App.cpp en al menos 6193 lineas, un
  monolito con un solo slice hecho en esta era; (2) base de evidencia
  mas fuerte por slice: CI de dos jobs (ctest + ThreadSanitizer) y
  anclaje dual recien definido (acta 0463 seccion 2), verificacion
  automatica e independiente que el lado web no tiene; (3) el patron
  C++ acaba de consolidarse y aplicarlo de inmediato reduce deriva de
  proceso; la descomposicion web puede reanudarse en cualquier
  momento sin perdida (patron documentado en 0454 seccion 6, 0460
  seccion 4.2 y precedentes DW.1/DW.3).
- Si la direccion es C++: OpenCode propone el siguiente bloque por
  cohesion (una familia autocontenida de helpers, como FieldFormat) y
  el pre-registro lleva el checklist completo: lineas exactas,
  cierre grep por simbolo, anclaje dual re-medido, diffstat de
  movimiento con enumeracion de andamiaje (para no repetir el desliz
  k del acta 0461), evidencia byte antes/despues, bundle delta con
  sha256 y PR a master con CI 2/2.
- Alternativas, todas auditables y decision de David: (a) web:
  siguiente extraccion de IonosphereScene.tsx (ancla 48 ficheros /
  461 tests / 0 fallos); (b) higiene web: un slice de infraestructura
  que anada CI al repo web mejoraria la base de evidencia de todos
  los slices web futuros; no es refactor de movimiento y requeriria
  criterios propios en su pre-registro.

## 5. Estado

- C++: master 3716295. Web: main 9eca362. Android: aparcado en
  59f539b. Eras DW.1-DW.4 cerradas; sin conformidades abiertas.
- Mi siguiente acta: conformidad (o rechazo motivado) del
  pre-registro DW.5 que David defina.

- GLM, lado auditor, 2026-11-23.
