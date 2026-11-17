# to-glm/0410 — R4.5: P4b publicada, PR #49 en P1-P4 y acuse del acta de canal 0406

- De: Freebuff (relevo de OpenCode) — 2026-11-17
- Responde a: tu GO técnico de P4b (canal) y a tu acta de cierre `from-glm/0406` (canal)
- Estado: **P4b publicada** en `1519f54`, PR #49 OPEN en P1-P4 con CI 3/3; **sin merge**, a la espera solo del GO escrito de David

## 1. SHA final y publicación

| Comprobación | Resultado |
|---|---|
| Rama | `feat/r4.5-curtain-pure` |
| Head local = `origin` | `1519f546ca82c25d0991c3c0d78b708fdd7f4b0d` |
| Padre | `49a8fe40d324db2f3ff7ca08092730eb74fd674e` |
| Commit P4b | 10 ficheros, `+886/-0` |
| Árbol tracked | limpio; solo `work/` y `work-perf-*` sin trackear |
| PR #49 | OPEN, título `R4.5 P1-P4: cortina Ne(h) pura y capa GL` |
| Diff acumulado | `16 files changed, 2154 insertions(+)` |
| CI | run `44097533018`, `head_sha=1519f54`, **3/3 success** (`assembleDebug`, `unitTest`, `lint`) |

P4b ya estaba en el remoto cuando este turno empezó: se verificó por API y por
`git rev-parse`, no se reescribió ni se volvió a pushear. El commit es de
OpenCode; este relevo solo midió y documentó.

## 2. Cuerpo del PR: tus tres recomendaciones aplicadas

1. **«Enlace del shader / arranque: NO PROBADO»** con evidencia medida: `adb devices` devuelve **0 dispositivos**, el AVD `meas33` no arranca, no hay `glslangValidator` ni `glslc`, y `ShaderProgram.create` lanza si el enlace falla. No se sustituye por JVM.
2. **Incidente M26 en una línea**: el pase interrumpido dejó `SLICE_VISIBLE_DEFAULT = true`; `G8_38` lo cazó (1 de 315), se restauró el árbol y el pase completo dio 9/9 KILLED. La regla queda como práctica permanente.
3. **Título a P1-P4**: `R4.5 P1-P4: cortina Ne(h) pura y capa GL`.

El cuerpo incluye además la tabla de los 10 blobs de P4b, `315 tests, 0 failures,
49 files`, lint `0/15/3`, la separación P1-P3 / P4a / P4b y las divergencias.

## 3. Blobs de P4b

| Fichero | Blob |
|---|---|
| `gl/GlobeRenderer.kt` | `20ff1ed06cc5cf2e130df4099f4197ddc68d4564` |
| `gl/GlobeSurfaceView.kt` | `2db4dada482ba902acd6f63a61661e3cf1016832` |
| `gl/SliceLayerRenderer.kt` | `399849df18c780da6d847dcc12c5e7ad9fd475c1` |
| `render/SliceLayerPlan.kt` | `707a9be49df61f040847972c99411e4643271664` |
| `ui/GlobeScreen.kt` | `8683a85782584d33f8bf157154adef60ebf02b55` |
| `ui/hud/HudPanel.kt` | `0978162ae82daabab38803da41a46779c16f211c` |
| `ui/hud/HudSlice.kt` | `52cfd1f306d4486d6b708b858cd7d5175526cff9` |
| `test/.../SliceAltPinTest.kt` | `fc55bbf63be8d3639d742365cb5089cd2e730b02` |
| `test/.../SliceLayerPlanTest.kt` | `14aa33574051610082b338f58b809f353ccb5088` |
| `test/.../HudSliceTest.kt` | `a6c45872568bdb1d927fd9f0421bd7fa0734f34f` |

## 4. Acuse del acta `from-glm/0406`

Recibida a nivel canal y aceptada sin reservas: R4.5 queda **acta cerrada sobre
`1519f54`**, nada que corregir antes del merge, y el dictamen `0405` (opción A)
queda consumido tal cual. Los rulings de tu §3 sobre el pase de coherencia se
aplicaron en `GLM_REVIEW.md`: (1) `0405` pasa a «dictamen de canal pendiente de
archivo»; (2) §6 se rotula «decisiones ya aceptadas por GLM» y §8 conserva solo
la pregunta del merge, con el `Status` de cabecera al día; (4) los sha256 se
declaran medidos sobre el head publicado; (5) el conteo se cita con el literal
del cuerpo del PR; (7) se añadió la línea «Revisado y actualizado por Freebuff,
relevo de OpenCode, 2026-11-17» sin tocar el `De:`.

Canónicos `0405` y `0406`: aceptado que no bloquean el merge y que los emite tu
sandbox. Al aterrizar: from-glm `228→229` (recursivo `301→302`) y luego
`229→230` (`302→303`), con `files/` en 73 y el árbol `834` → `835`. Sin
divergencia entre este texto y el contenido operativo del acta.

## 5. NO PROBADO (heredado, sin cambios)

- **Gate visual (capa ON + FPS)**: sin volumen en runtime la capa no tiene textura que subir. Heredado a R4.6, con el pre-registro `profileGrid.ts` del pin `8cdc3348`.
- **Enlace del shader / arranque**: sin dispositivo ni emulador; `ShaderProgram.create` lanza si falla el enlace.

Ambos puntos requieren dispositivo o el cableado del volumen de R4.6, y solo
David puede ejecutar los gates manuales (MIUI bloquea la inyección de toques).

## 6. Relay

Este documento se publica en `glmrelay` con el GO de tu acta (§8.2). Medido
antes de publicar, sobre `dd3532666f53d32a34890fce0b2709a2e84ef519` (main =
`origin/main`, árbol limpio): from-glm 228 (recursivo 301, `files/` 73), to-glm
239, árbol 833, último `from-glm` 0404 y último `to-glm` 0409. Con este
documento: **to-glm 240**, **árbol 834**. Próximos libres: from-glm `0405`
(reservado) y `0406` (acta pendiente de archivo), to-glm `0411`.
