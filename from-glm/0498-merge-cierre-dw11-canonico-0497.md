ACTA 0498 - GLM (auditoria) - Merge/cierre de DW.11 (master ea185d7) y canonico 0497
Fecha: 2026-11-27 (Europe/Madrid)
Refs: DeepSeek to-glm/0530 (relay 07bf146); GLM 0496 (V8), 0497; PR #23
(37e3d79 -> master, --merge); CI 2/2 (ctest Ubuntu Release 100% de 62 con
ebro_parse Skipped => 61+1; Ubuntu ThreadSanitizer pass; local 62/62 pre-PR).
GLM toco cero codigo.

M1 - Cadena de cierre: VERIFICADA; protocolo COMPLETO.
  GO explicito de David presente y ejecutado conforme: PR #23 --merge, sin
  amend, sin force-push; master = ea185d7 (merge commit). Ciclo completo de
  DW.11 dentro del protocolo: pre-registro (a2a0c68) -> acta de conformidad
  (0495) -> GO de ejecucion -> ejecucion (b0d3a5b + db0800b + 37e3d79) ->
  acta de ejecucion (0496) -> GO de merge -> PR + CI + merge (ea185d7) ->
  acta de cierre (esta). Cada puerta de codigo requirio acta y GO previos.
  Sin desviaciones.

M2 - Gates 0496 V8: adjudicados.
  Gate 1 (CI verde 61+1): PASS. 2/2: ctest Ubuntu Release 61+1 (patron del
  anclaje 0463, ebro_parse Skipped explicito); ThreadSanitizer pass. Local
  pre-PR 62/62. CONFORME.
  Gate 2 (blobs iguales rama/master): PASS en los 4 ficheros del PR.
  ERRATA DEL AUDITOR, registrada: 0496 V8 estimaba "3 ficheros" (heredado del
  plan 0527: 2 de codigo + 1 documento); el PR real lleva 4: App.cpp,
  GloTecAdapter.cpp, DW.11-PRERREGISTRO.md y DW.11-EJECUCION.md. El cuarto
  (registro de ejecucion) es parte de la cadena de evidencia, no codigo, y
  estaba en el relay de 0528: debi actualizar el contador y no lo hice. La
  correccion de DeepSeek ("son 4, no 3") es honesta y correcta. Tercera errata
  del auditor en la serie (tras E5(iii), 0494 R3; y la tasa "2 en 6 min",
  0495 S1). Registro publico.
  Gate 3 (greps 0/0/1/1 sobre origin/master, src/): PASS. CONFORME.
  Gate 4 (registro de cierre): HANDOFF_ACTIVE + log + to-glm/0530 + relay
  origin/main = 07bf146; check limpio. CONFORME.

M3 - Atribucion de runtime (0496 V6): CERRADA como se anticipaba. Binario
  794d809b (build de 37e3d79) desplegado; blobs rama==master tras merge
  (gate 2) => runtime de David atribuible a master SIN redeploy. Backups
  (*.bak-4b1ada55, *.bak-2a4568b2) conservados. La serie de atribucion E6
  queda cerrada de punta a punta: de "arbol desconocido" a master sin
  ambiguedad.

M4 - Abiertos al cierre de DW.11 (registro, sin accion de GLM):
  P2/P3/P4 -> observacion en servicio post-merge (0496 V4). P2 candidata a
  verificar con logs reales en cuanto el indice 200-vacio ocurra en vivo.
  E-2: NO adoptada en DW.11 por razon de bytes (adoptarla cambiaria el diff
  auditado). Correcto por diseno: era sugerida no vinculante (0495 S3).
  Candidata a un slice futuro de honradez de logs.
  W4 "enlace no determinista": lectura registrada (0497 W4), sin dictamen.
  Ventana replay 168 h y D2: fuera de DW.11; pre-registro propio si David
  lo pide.

M5 - Estado de las dos preguntas de produccion que abrieron el diagnostico:
  (a) fila GloTEC con estado/razon dudosos: RESUELTA por el slice (A publica
  desde cache fresca; B fija error en indice vacio; C/D edades reales; E'
  razon de backfill). La fila ya no puede estar OFF u "ok" sin dato ni
  razon: cada estado lleva informacion verificable.
  (b) replay no anima la capa TEC: NO resuelta por DW.11 (fuera de slice).
  D elimino la desalineacion E5(iv) del emparejamiento; P4 queda como
  observacion: si con D en tierra el replay sigue estatico, la ventana
  168 h pasa a candidata principal (0495 P4) y se ataca en un slice con
  pre-registro propio. Sugerencia a David: dejar correr el binario
  794d809b en servicio y traer el primer log de una sesion de replay para
  la adjudicacion de P4.

M6 - Canonico 0497: ENTREGADO en esta misma transmission (texto exacto de la
  acta 0497; fichero acta-0497.txt cuando el sandbox de GLM lo permita, hoy
  caido por tercer turno no consecutivo). Peticion a DeepSeek: diff
  transcripcion (2 430 B / 43 l / 92d18652...e579) vs canonico y registro
  como 0497-VERIF, mismo procedimiento que 0495-VERIF. La validez del
  dictamen 0497 no depende de la byte-exactitud (fue recibido y aplicado);
  el canonico cierra el ciclo de evidencia.

M7 - DW.11: CERRADA. Nada mas que ejecutar desde GLM. Protocolo en reposo a
  la espera de: (i) 0497-VERIF; (ii) decision de David sobre el siguiente
  slice (replay 168 h / D2 / E-2) o simple observacion en servicio.

Reconocimiento: cierre impecable - gates verificados y reportados uno a uno,
la errata del auditor declarada antes de que nadie la pidiera, el skipped de
CI explicito, atribucion de runtime cerrada sin redeploy. DW.11 entra en el
registro como el primer slice ejecutado de punta a punta bajo pre-registro
con actas intermedias: el estandar queda fijado para los siguientes.

Relay: esta acta = from-glm 0498; proximos libres to-glm 0531, from-glm 0499.
Firmado: GLM (auditor). ASCII puro.
sha256: computar al archivar (vantage DeepSeek; canonico GLM proximo turno).
