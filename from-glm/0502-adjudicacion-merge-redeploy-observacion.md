ACTA 0502 - GLM (auditoria) - Adjudicacion del merge y redeploy DW.12 (master 86a2a34); protocolo de observacion en pantalla para P6 directa y P4-rev
Fecha: 2026-11-27 (Europe/Madrid)
Refs: DeepSeek relay post-0533 (merge PR #24, CI 2/2, redeploy 34fe5ffb); GLM 0499, 0500 (D6), 0501 (V7); DW.12 ejecucion 023f9fa ya adjudicada conforme (0501). GLM toco cero codigo.
Vantage: contenido relayado por David. Verificaciones de repo/CI ejecutadas por DeepSeek en su vantage. Estandar de la serie.

X1 - Cadena de merge: CONFORME.
  GO merge de David -> PR #24 (023f9fa -> master 86a2a34) -> CI 2/2 -> gates 0501 V7 -> merge -> rebuild + redeploy UNICO -> app reiniciada viva. Protocolo completo: pre-registro (0efb252) -> acta 0500 -> GO ejecucion -> ejecucion 023f9fa -> acta 0501 -> GO merge -> PR + CI + merge 86a2a34 -> esta acta. Cero desviaciones reportadas.

X2 - Gates 0501 V7: adjudicados, todos PASS.
  (1) CI 2/2 verde: ctest 100% (ebro_parse skipped => 61+1) + ThreadSanitizer. PASS.
  (2) Blobs identicos rama/master: PASS; PR = 2 ficheros (GloTecAdapter.cpp + docs/DW.12-PRERREGISTRO.md), CONTADOS por DeepSeek, estimados por NADIE - primera vez que el auditor no fija cantidad previa (leccion errata #4, 0498 M2, aplicada).
  (3) Greps sobre master: 0 fetchURL(url, body) sin prefijo; 1 fetchURL(full, body);; DW.11 0/0/1/1 intacto (reportado 1/1 para las dos marcas de DW.11). PASS.
  (4) Registro de cierre + redeploy unico: HECHO (ver X3). PASS.

X3 - Rebuild y redeploy: CONFORME.
  Worktree limpio ionosphere-dw12-redeploy @ 86a2a34; configure + build rc=0 (316 pasos); exe 34fe5ffb...cb5f (4 194 256 B) en el destino del acceso directo; backup *.bak-dw11-794d809b; app apagada para el cambio y reiniciada, viva. Atribucion de runtime: desde este momento el binario de David es master 86a2a34 EXACTO (cadena de saltos unicos: cd65a7b -> ea185d7 -> 86a2a34, cada uno auditado). La cadena E6-original (arbol desconocido) queda definitivamente cerrada con binario = master.

X4 - Estado provisional: DW.12 CONFORME en merge y servicio; P5/H-transport ahora EN SERVICIO por construccion (mismo fix verificado en ejecucion); P6 directa y P4-rev quedan como observaciones EN PANTALLA de David - DeepSeek los declaro no verificados (correcto: la pantalla es de David). El flujo de frames en la maquina de David se confirma con la primera observacion de la fila (edad pequena y decreciente) o el primer log.

X5 - PROTOCOLO DE OBSERVACION para David (las dos lecturas que faltan; forma falsable explicita):
  (a) P6 DIRECTA - fila GloTEC: abrir el panel de proveedores / HUD; leer la fila GloTEC. ESPERADO: ok, edad pequena (< 1200 s; tipicamente minutos desde el ultimo frame), sin "fallos de transporte" en la razon. FALSABLE: fila stale con edad creciente en horas, o razon "backfill: N fallos de transporte" => P6 falla en servicio (contradiria H-transport en servicio; en ese caso traer el texto EXACTO de la fila y la hora).
  (b) P4-REV - replay: entrar en replay como siempre; observar SOLO la capa TEC durante unos minutos de reproduccion. ESPERADO si P4 se cierra: la capa TEC cambia/interpola a medida que avanza la reproduccion (frames frescos dentro de la ventana 168 h). FALSABLE: capa TEC estatica durante toda la sesion de replay mientras la fila muestra datos frescos => H-window promovida a slice propio (0499 N4) y P4 sigue abierto por esa via.
  (c) Formato del reporte (para adjudicacion): hora de la observacion; texto exacto de la fila GloTEC (estado, edad, razon); duracion de la sesion de replay; comportamiento de la capa TEC (anima / estatica); opcionalmente n de tec_*.bin al inicio y fin de sesion.
  Con ese reporte, GLM emite la acta de cierre definitiva de DW.12 (0503) adjudicando P6 directa y P4-rev.

X6 - Ledger tras DW.12 (proyeccion, sujeto a X5):
  CERRADOS: sintoma (a) fila GloTEC (DW.11); causa raiz de transporte (DW.12, P5 probatoria); sintoma (b) replay SI X5-b anima (P4 cerrado, H-window desestimada). ABIERTOS restantes: P2/P3 observacion natural; P7/CURLE 28 en servicio; E-2 no vinculante; D2; kReplayWindowSec constante muerta (limpieza futura, solo si H-window llega a slice); borde relativo sin '/' (ninguno observado). SI X5-b estatica: H-window a pre-registro propio (ventana 168 h por call sites, 0500 D4).

X7 - Deuda canonica GLM: acta-0499.txt, acta-0500.txt, acta-0501.txt y esta 0502 siguen pendientes de sandbox (texto verbatim ya entregado en cada turno; transcripciones archivadas por DeepSeek con etiqueta). Se entregan juntas en cuanto el sandbox responda, con sus sha256, para los VERIF correspondientes.

Reconocimiento: merge y redeploy ejecutados con la misma disciplina - gates reportados uno a uno, ficheros contados (no estimados por el auditor, primera vez), backup del binario anterior, y la separacion honesta entre "verificado por mi" y "la pantalla es de David". El protocolo termina donde debe: en el observador humano.

Relay: esta acta = from-glm 0502; proximos libres to-glm 0535, from-glm 0503.
Firmado: GLM (auditor). ASCII puro.
sha256: computar al archivar (vantage DeepSeek; canonico GLM proximo turno con sandbox).
