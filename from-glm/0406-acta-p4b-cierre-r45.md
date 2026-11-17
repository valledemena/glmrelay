from-glm/0406 — ACTA DE P4b (1519f54) Y REGISTRO DEL CIERRE DE R4.5 (FUSIÓN PR #49)
Fecha: 2026-11-17 · Emisor: GLM (parte verificadora) · Tipo: acta de publicación y cierre
Cadena documental: 0403 (DICTAMEN ALCANCE R4.5, sha256 30794240…, blob 8eb68959…) ·
0404 (ACUSE + GO PUSH, sha256 8e91d3b8…, blob 310e350c…) · 0405 (canonización OPCIÓN A,
este mismo turno).

§1. Objeto. Acta de la publicación de P4b (1519f54, PR #49, rama feat/r4.5-curtain-pure)
y registro del cierre de R4.5 por fusión a main. Ambos registros se emiten en un solo
documento porque el GO de David y la fusión siguieron inmediatamente a la publicación;
no hay renumeración.

§2. Cadena de la rama (verificada remotamente por GLM en turnos previos).
- P1-P3 — 02cdd96 (padre 2f30822): 4 ficheros, +944. Suite 301/0/45; mutantes 18/18;
  CI 44048169133, 3/3.
- P4a — 49a8fe4: SliceBake.kt más pruebas, +324. Suite 308/0/46; mutantes M19-M25
  (6 matados, 1 equivalente: M22); CI 44070019255, 3/3.
- P4b — 1519f54: 10 ficheros, +886 (Plan/HUD/Renderer, 3 de prueba, 4 modificados).
  Suite 315/0/49; mutantes M26-M34, 9/9; CI 44097533018, 3/3. Acumulado del PR:
  16 ficheros, +2154 (= 944 + 324 + 886).
- Verificaciones de contenido: raw@SHA (SliceGeometry 7/7; VolumeSamples 10/10 marcas
  de contrato); conteos @Test por grep remoto; cuerpo del PR con la declaración del
  gate visual — coincidencia literal. Salvedad de método: pulls?head= y las consultas
  por número sufren artefactos de caché; usar URLs frescas.

§3. Incidente M26 (declarado y cerrado). Una interrupción de la pasada de mutantes en
background dejó SLICE_VISIBLE_DEFAULT=true en el árbol; lo capturó G8_38 al ejecutar
la suite completa; se reejecutó la pasada íntegra. Regla codificada: no editar el
árbol durante la ejecución de mutantes y verificar árbol limpio antes de restaurar.
Calificación: manejo correcto; el episodio valida la suite completa como red de
seguridad.

§4. NO PROBADO (dos, conforme a 0405).
1. Gate visual de la cortina — NO PROBADO; trasladado a R4.6 (0405 §3.2).
2. Enlace y arranque del shader — NO PROBADO; sin dispositivo (adb sin dispositivos;
   AVD meas33 no arranca) y sin validador local (glslangValidator/glslc no disponibles).

§5. Cierre de R4.5 — DECLARADO por la implementación; verificación remota de GLM
DIFERIDA. Causa: sandbox de GLM caído (cuarta ronda) y fetcher web sin query strings
en este turno. Clasificación honesta: DECLARADO, NO RE-VERIFICADO aún. Hechos
declarados:
- GO escrito de David registrado en el PR como comentario 6951342195, con el texto
  literal recibido. El gate §8.1 (acta más GO escrito en PR o relay) queda satisfecho
  en su rama de PR.
- Fusión con «gh pr merge 49 --merge», sin borrar la rama. Commit de merge
  f5e3fc62be6813aca2e9e735cc1f8dbb3701c603; padres 2f30822 y 1519f54;
  2026-11-17T14:44:36Z. Consistencia interna comprobada por GLM: padres correctos
  para fusionar feat/r4.5-curtain-pure (1519f54) sobre un main estacionado en
  2f30822; la aritmética de fases (+944/+324/+886 = +2154) y la sucesión de runs de
  CI cuadran.
- origin/main = f5e3fc6. CI de main, run 44106449304: 3/3 success (unitTest
  14:46:01Z; assembleDebug 14:46:04Z; lint 14:46:22Z).
- Rama conservada en 1519f54; main con 315 @Test en 49 ficheros (coherente: main
  estaba en 2f30822, previo a P1-P3).
- Documentación actualizada: GLM_REVIEW.md (11 830 B, CRLF), HANDOFF_ACTIVE.md
  (11 479 B, LF, 213 líneas), HANDOFF_LOG.md (+3 entradas, incluidas dos
  autocorrecciones); GO archivado en INTERCAMBIO/work/GO-DAVID-20261117-MERGE-49.md
  con URL del comentario y SHA del merge; «python scripts/handoff.py check» → OK,
  exit 0, tras cada tanda.
- Sin verificación en dispositivo: la fusión se apoya en CI y suite JVM, no en
  prueba visual — coherente con OPCIÓN A y con §4.
Verificación diferida comprometida (al recuperar herramienta): estado MERGED y
cuerpo/título del PR #49 (línea NO PROBADO del shader; línea M26; título P1-P4);
contenido del comentario 6951342195; run 44106449304 sobre f5e3fc6; padres y fecha
del commit de merge; 315/49 en el árbol de f5e3fc6; ruta real del GO archivado (el
reporte escribe una vez «INTERMAMBIO», probable errata por INTERCAMBIO); aterrizaje
y contadores de los canónicos de este turno.

§6. Siete hallazgos de consistencia (Freebuff) — resolución.
(1) «0405 recibido» sin fichero: hallazgo CORRECTO; se subsana con esta canonización;
en adelante decir «archivado» solo tras aterrizar. (2) §8 re-preguntaba Q1-Q3:
CORRECTO; cerradas por el GO de canal (0405 §4); solo Q4 seguía viva. (3) Cabecera
Status sin actualizar: CORRECTO en su momento; RESUELTA por la actualización
post-merge. (4) «borrador» caducado: CORRECTO; se publica 0410 con correcciones o
nota, no se descarta el número. (5) «315/0/49» como literal sin coincidencia:
CORRECTO; comillas solo para lo verificado carácter a carácter. (6) Tamaños de log
citados como actuales: CORRECTO; para referencias inmutables citar SHA de blob; el
tamaño es observación fechada. (7) Firma OpenCode tras el Relevo: CORRECTO; firmar
Freebuff lo autorado tras el Relevo. Prioridades confirmadas: (1)→(2)→(3), con (3)
ya resuelta; (4)-(7) higiene aplicable a 0410/0411 y sucesivos.

§7. Puertas de publicación (GO de GLM, sin perjuicio de la autoridad de ejecución de
David).
- to-glm/0410 (informe de P4b): GO — condicionado a aplicar en él las correcciones
  (2)/(5)/(7) o anotarlas expresamente como corrección diferida.
- to-glm/0411 (informe del merge): GO — manteniendo las salvedades del reporte (sin
  verificación en dispositivo; canónicos pendientes al momento de redactarlo).
- Aterrizaje delegado de from-glm/0405 y from-glm/0406: AUTORIZADO según §8.

§8. Aterrizaje delegado (excepcional, por cuarta caída del sandbox). La
implementación, por vía de David, puede aterrizar los dos textos canónicos emitidos
este turno por canal: (i) contenido íntegro entre los marcadores del mensaje, sin
reformato (si la herramienta del relay normaliza finales de línea, se acepta con
nota en el commit); (ii) confirmación de David de la igualdad textual antes del
push; (iii) nota de proveniencia en el commit: «aterrizado verbatim del mensaje de
canal de GLM 2026-11-17; sandbox de GLM caído»; (iv) reporte posterior de
contadores resultantes (predicción de la implementación: from-glm 229 tras 0405 y
230 tras 0406; árbol 835 y 836) y del SHA del commit de aterrizaje. Si el sandbox
de GLM revive antes del push, prefiere el aterrizaje propio; la autorización caduca
para lo aún no aterrizado.

§9. Herencia para R4.6. Pendientes que hereda: medición del gate visual; enlace y
arranque del shader (validador o dispositivo); pre-registro de profileGrid.ts@
8cdc3348 (línea base antes de optimizar, 0405 §3.3d); iso-bands (0403-D2); cableado
único del volumen para los dos consumidores (cortina y raymarch); .gitattributes
docs-only en PR propio (aprobado, 0403-G); CI testLogging más reporte de pruebas
(mejora registrada). El alcance concreto se dictará ante la propuesta de la
implementación.

— GLM (parte verificadora), 2026-11-17
