# GLM -> R3.4 - Cierre de #15 verificado; DoD 1-10 completo; R3 cerrado

De: GLM - 2026-11-14 - asunto: acuso el cierre del tracker #15 (DoD 10) y lo
verifico de forma independiente contra GitHub. Todo cuadra: issue cerrado,
comentario publicado con el texto entregado, SHAs canonicos, main y relay como
fue reportado. R3.4 y R3 quedan cerrados al 100% (DoD 1-10). No queda nada
pendiente de mi parte en R3; este acuse es el ultimo eslabon del rastro GLM de
la fase.

Numeracion: `from-glm/0372` si David archiva (to-glm llego a 0371 con el aviso
del cierre, anclado en el relay `769a1c9`; asumo 0369/0370 consumidos por la
revision de SHA y el aviso previo a la publicacion, que no llevan commit relay
propio; el ajuste final de numeracion es suyo, como siempre).

---

## 1. Verificacion del cierre (todo verificado hoy, post-cierre)

    Issue #15    CLOSED, state_reason "completed", closed_at
                 2026-11-14T12:47:31Z - coincide con el reporte al segundo
    Comentario   6877477627, creado 2026-11-14T12:47:29Z (2 s antes del
                 cierre), en issues/15#issuecomment-6877477627
    Texto        el comentario publicado es el fichero entregado por GLM
                 (issue15-cierre-R3.4-COMENTARIO-FINAL-GLM-20261114.md);
                 verificado por muestreo directo del cuerpo: titulo, linea
                 R3.4 con ambos merges, DoD 9 y 10, rastro from-glm
                 0351/0353/0360/0363/0365/0368 y el cierre firmado
                 "Cierro el tracker. - David (valledemena)"
    SHA en el    e12e100a39025ea73b23c7d55e7a13285f456aa6 - canonico
    comentario   (...456aa6); coincide ademas con el merge_commit_sha del
                 PR #39 devuelto por la API
    PR #39       merged 2026-11-14T10:31:19Z, merge_commit_sha
                 e12e100a39025ea73b23c7d55e7a13285f456aa6, base main
    PR #40       "docs: cerrar R3.4 (DoD 10)", merged 2026-11-14T12:20:21Z,
                 merge_commit_sha 52543abc0b0339b162c8365e416cffe55e0f0b7e,
                 base main
    main         refs/heads/main = 52543abc0b0339b162c8365e416cffe55e0f0b7e
    Relay        769a1c96eb1d12a75fb63c631c354a0f642730a4 a las
                 2026-11-14T12:47:46Z (15 s despues del cierre), mensaje
                 "r34: #15 cerrado; DoD 10 completo", anade
                 to-glm/0371-r34-issue15-cerrado.md

La secuencia temporal del dia cuadra completa en el relay (commits con
timestamp verificados): 7de57e8 07:07:19Z (acta final + lado a lado v2),
2c385c3 09:16:37Z (raws desenchufados + prueba de procedencia v2), 928d3e3
10:28:46Z (nota de recomputo), 8ec3096 10:32:56Z (T7 firmado + #39 mergeado),
1b8dc80 10:37:52Z (T7 final alineada con GLM 0365), ca3ac3e 12:20:56Z (#40
mergeado), 769a1c9 12:47:46Z (#15 cerrado). Siete anclas, ninguna fuera de
sitio; el cierre esta anclado 15 s despues de ejecutado.

## 2. Nota de metodo - sondeo rancio detectado y descartado

Mis dos primeros sondeos (issue #15 y commits/main) devolvieron estado rancio
de una capa de cache intermedia de mi herramienta de lectura: el issue "open"
y main apuntando a un commit del 2026-11-12. Descartado re-consultando con
claves nuevas y endpoints alternativos (refs/heads/main, pulls/39, pulls/40,
consulta directa del issue): el estado fresco es el de la seccion 1 y coincide
con el reporte del lado con credenciales. Lo registro porque el metodo forma
parte del rastro: esta acta se verifica sobre el estado fresco, no sobre el
rancio.

## 3. Variante ...458aa6 - registro cerrado

La variante erronea nunca llego a GitHub: el comentario publicado cita el
canonico ...456aa6 (verificado en el cuerpo del comentario y contra el
merge_commit_sha del PR #39). La variante vive unicamente en el dictamen 0368,
donde se explica la correccion, y en el chat que la transporto. Nada que
corregir en el repo. El punto queda cerrado.

## 4. Estado final de la cadena R3.4 / R3 (registro de cierre)

- Codigo: head firmado `23bb04715b95a752f34eac8353ef36e0f0fdd85b`; merge #39
  `e12e100a39025ea73b23c7d55e7a13285f456aa6` (anclaje del tercer momento);
  merge #40 `52543abc0b0339b162c8365e416cffe55e0f0b7e` (docs-only, +11/-4,
  head `829a730` con --match-head-commit); **main = `52543ab`**.
- CI: run `43481739755` (3/3, #39) y run `43590444822` (3/3, #40).
- Gate T4/T6: umbral enmendado 29,5 (David, 2026-11-13, anclado en el T7);
  medium desenchufado 29,52/29,54 fps (WiFi adb); ratio ON/OFF 1,0008; low
  29,90 (peor ventana 62,88 s); punto <=70 px (driver 1..1023).
- Acta final `b662596e951379b2b6c985a1efd8c1c8da6e310029444101602d9c335f42b6f3`;
  raws desenchufados anclados en `2c385c3` (270 `a73d81b2...`, 5min2
  `332f3ce7...`, resumen `e71c0f86...`); nota de recomputo en `928d3e3`.
- Capturas: t6-1 `009b2f35...`, t6-2 `f4229b1c...`, t6-3 `1c0b77e6...`,
  t6-4-pq052 `1f94e267...` (+ jr055 `d17d211d...`), lado a lado v2
  `d4f5c6dc...` (procedencia del panel certificada por GLM: identidad bit a
  bit con t6-1, 0365).
- Blobs congelados: plan `10566f61...` (34657 B), checker `5a48cb18...`
  (46114 B) - identicos en `e12e100` y en `main`.
- T7: `pull/39#issuecomment-6875951335`.
- Tracker: #15 CLOSED 2026-11-14T12:47:31Z, comentario de cierre
  `6877477627`, relay `769a1c9`.
- DoD 1-10: completo (la tabla item a item queda publicada en el comentario
  de cierre de #15; no la repito aqui).

## 5. Archivo de dictamenes - peticion final

`from-glm/` seguia terminando en 332 segun mi ultima verificacion directa (no
he podido releer el directorio en esta ronda). Pido archivar, si aun no lo
estan: 0351, 0353, 0360, 0363, 0365 (texto T7), 0368 y el presente (0372).
El rastro de auditoria del cierre de R3 los necesita; el comentario publicado
ya los cita por numero.

## 6. Cierre de mi participacion en R3

Sin push, sin merge, sin publicar por mi parte en toda la fase - como ha sido
desde R0. Mi parte en R3 termina aqui: el texto de cierre, el re-anclaje del
tercer momento y los acuses estan entregados y verificados. La siguiente fase
del tablero es R4 (Tiempo y profundidad), pendiente segun TASKS.md; cuando el
lado ejecutor abra esa conversacion, GLM esta a la orden.

GLM - 2026-11-14
