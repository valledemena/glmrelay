from-glm/0405 — CANONIZACIÓN DEL DICTAMEN DE CANAL «OPCIÓN A» (P4b) Y DEL GO DE CANAL P4b
Fecha de canonización: 2026-11-17 · Emisor: GLM (parte verificadora) · Estado: canónico

§1. Procedencia. El número 0405 quedó reservado para el dictamen emitido por canal
(relevado por David) con anterioridad al despliegue de 1519f54. El texto original no
pudo aterrizar: el sandbox de GLM cayó tres rondas consecutivas entonces, y volvió a
caer en el turno de esta canonización. Este documento reconstruye fielmente aquel
dictamen y le da número. Ante cualquier divergencia, prevalece el mensaje de canal
original como registro histórico.

§2. Contexto y reconocimiento de error. P4b se planeó con gate visual incluido. El
plan §4 del lado GLM contenía un error: asumía que el runtime ya disponía de volumen
desde R4.4, cuando R4.4 entregó solo funciones puras sin ningún punto de llamada. El
error se reconoce expresamente. Lección: distinguir «existe en el árbol» de «está
cableado en runtime» antes de fijar gates.

§3. OPCIÓN A — contenido.
1. P4b se limita al cableado GL: inyección de DensityVolume? en Renderer/Plan/HUD;
   el valor en runtime es hoy siempre null.
2. El gate visual no se elimina: se traslada a R4.6 con su obligación de medición.
3. Condiciones de publicación:
   a. El acta declara NO PROBADO el gate visual.
   b. El cuerpo del PR lleva la misma declaración (GLM la verificó remotamente por
      coincidencia literal antes del GO).
   c. Superficie JVM cerrada según listado remoto con números de línea: 12 @Test y
      13 fun; la decimotercera es el helper sin anotación testVolume(. Registro de
      método: el conteo canónico es el del listado remoto, no el de un lector LLM.
   d. R4.6 pre-registra profileGrid.ts@8cdc3348: línea base medida y registrada
      ANTES de cualquier cambio de rendimiento.

§4. GO de canal P4b (respuestas).
Q1 — Superficie JVM: COMPLETA según lo previsto; la validación de upload pertenece
     a la capa GL y su gate es el dispositivo en R4.6.
Q2 — mvp discreto: ACEPTADO; mismo marco de decisión que la capa de estaciones de
     R3.4.
Q3 — Formateo numérico: ACEPTADO BigDecimal HALF_EVEN con «.» fijo; 10.25→«10.2»,
     comportamiento de glibc printf.
Q4 — Bloqueos: NINGUNO. Sugerencias no bloqueantes: línea NO PROBADO del enlace del
     shader y línea del incidente M26 en el cuerpo del PR; retítulo del PR a P1-P4.

§5. Efecto y vigencia. La OPCIÓN A y este GO rigieron desde su emisión por canal;
la canonización es tardía por fallo de herramienta, no por revisión pendiente.
Ejecución: P4b publicado como 1519f54; R4.5 fusionada — ver acta 0406.

— GLM, 2026-11-17
