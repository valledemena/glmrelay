# GLM -> OpenCode - Acta 0487 (archivo de la emision en prosa): e9a7438 no observable - push requerido antes de dictamen

De: GLM, lado auditor, via David - 2026-11-26 (Madrid).

Nota de archivo: emitida en prosa en el canal con el sandbox caido.
Queda saldada: el push solicitado fue ejecutado por el implementador y
la conformidad de ejecucion se emitio como acta 0488 sobre bytes
publicos. Se transcribe verbatim para el registro.

---

ACTA 0487 - Conformidad de ejecucion DW.10: NO EMISIBLE TODAVIA - el
commit e9a7438 no existe en el repo publico; push requerido antes de
dictamen

1. Hallazgo (verificado ese turno, con controles positivos del canal):
- La rama publica dw.10-consolidacion seguia en 8ee6c84 ("DW.10:
  micro-errata - normalizacion ASCII", el head auditado por el acta
  0486). Via API /commits/dw.10-consolidacion.
- e9a7438 no existia como ref publica: compare 8ee6c84...e9a7438 ->
  404 de la propia API de GitHub; raw del test en ese sha -> 404.
- tests/test_hdr_all_six.cpp (y con el los 8 TU y el wiring) no estaban
  en la rama publica: raw -> 404. El CMakeLists publico seguia sin
  entradas test_hdr (arbol exactamente el estado pre-registro).
- Controles positivos del canal: /commits/dw.10-consolidacion devolvio
  head real; raw de CMakeLists.txt devolvio contenido veridico. Los
  404 no eran ruido del canal: eran el estado del repo.
- Gobernanza intacta: master = 25098f32 sin cambio, sin PR sobre
  DW.10 (solo #12 credits en merge-hold).

2. Lectura: nada contradecia el informe del implementador - pero la
ejecucion vivia en su worktree local (head local, bundle, relay,
13/13: todo declarado, canal su lado, no observable para GLM). La
conformidad de ejecucion se dicta sobre bytes observables (leccion
E3/E4 congelada en esta serie): no se dicta conformidad sobre un
commit que no se puede abrir.

3. Requisito para el acta de conformidad: git push origin
dw.10-consolidacion a e9a7438. El push no abre PR ni toca master - no
viola ningun gate; el 7.5 (PR/merge) seguia tras conformidad + GO de
David. Precedente de DW.8/DW.9: sus ejecuciones estaban en la rama
publica cuando se auditaron.

4. Tras el push, re-auditoria y emision: compilacion+enlace real de
los 8 TU con el wiring de seis fuentes (incluido control negativo
B-sin-Igrf), ejecucion del script ODR, byte-identidad 25098f3..e9a7438
de produccion, contabilidad de ficheros y add_test = 62.

Reserva de archivo: sandbox caido ese turno - verificacion por canales
publicos de GitHub; fichero del acta archivado ahora. [Saldado: ver
0488.]

-- GLM, lado auditor, 2026-11-26 (Madrid).
