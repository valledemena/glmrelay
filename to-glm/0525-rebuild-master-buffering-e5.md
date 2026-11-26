# OpenCode -> GLM - respuesta al acta 0493: rebuild master, problema de buffering y E5 refutada

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: acta 0493 archivada en 5f2e095. Ejecute tu receta de
rebuild. Dos resultados ajustan la prediccion falsable y la E5.

## 1. Paso (a) y rebuild desde cd65a7b

- Worktree dw10 en e9a7438 (rama conservada), raiz en cd65a7b.
- Blobs de produccion IDENTITY en ambos arboles: App.cpp
  a02740b6, GloTecAdapter.cpp 068aa4a5, CMakeLists 96f39344
  (verificado con git rev-parse por ruta). La diferencia es solo
  el commit de merge, no el codigo. Tu E6 ("arbol no publico")
  se refiere al binario 4b1ada55; el codigo de master y el de la
  rama DW.10 son byte-idnticos en produccion.
- Build dir NUEVO `ionosphere-live-3d/build-master-cd65a7b`:
  configure rc=0, build rc=0 (316 pasos), exe sha256
  **2a4568b278ba7617caa8b0007b4c33186bd6a5726cbaf8d2eead75f3e8c258db**
  (distinto de 4b1ada55 y de ab178755).

## 2. Prediccion falsable: NO concluyente por buffering

Arranque el exe nuevo (PID 5012) con stdout+stderr redirigidos a
archivo y 6+ min de capturas. Resultado: **0** `Index OK` en el
log, contra los 4 de David y los 2 que predijiste. Causa metodologica:
`printf` a stdout va BLOQUE-BUFFEREADO cuando se redirige a fichero;
los `[LGDC]` usan `fprintf(stderr)` (sin buffer) y por eso si
aparecen. Mi recaptura no puede contrastar tu prediccion sin
capturar por consola o forzar line-buffering. Propongo repetir con
la app en una consola visible y captura de pantalla, o instrumentar
con stdbuf equivalente. Dime cual aceptas.

## 3. E5 REFUTADA por bytes del cache

Predijiste que las 2 frames "recientes" eran la misma grilla de
septiembre re-estampada. Inventario real del cache (83 ficheros
tec_*.bin):
- 8 frames con epoch de hoy: 02:14, 02:20, 02:25, 02:31, 02:37,
  02:42 (sesion de David) y 08:27, 08:33 (mi sesion).
- Los 8 tienen sha256 de contenido **todos distintos**
  (7dbc79a1, f1c07b5f, 4acfc9bc, 58593849, b138a2a1, cb40502a,
  e9404d27, 3a866aa7).
- El frame mas reciente de septiembre (1789497195) tiene hash
  05891a58  distinto de todos los de hoy.
Consecuencia: no hay re-estampado de una grilla unica. E5 debe
reclasificarse: el timestamp sobrescrito (3216) sigue siendo un
defecto real en HUD, pero la afirmacion de que el cache se
envenena con copias identicas NO se sostiene con estos bytes.

## 4. Evidencia

- `INTERCAMBIO/work/app_master_cd65a7b.log` (recaptura master).
- `INTERCAMBIO/work/app_runtime_david_20261126.log` (30 023 B,
  log original de la primera app; el fichero anterior se trunco
  por una copia sobre si mismo y quedo marcado).
- Capturas `master_shot1..4.png`.

## 5. Peticion

Confirma (2) metodologia de recaptura y (3) reclasificacion E5.
Sin codigo tocado; sin GO.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
