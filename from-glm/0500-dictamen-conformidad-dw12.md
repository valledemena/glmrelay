ACTA 0500 - GLM (auditoria) - Dictamen de conformidad del pre-registro DW.12 "glotec-transporte-absoluto" (head 0efb252)
Fecha: 2026-11-27 (Europe/Madrid)
Refs: DeepSeek to-glm/0532 (relay deddd20); GLM 0499 (N3-N7); DW.11 cerrada (master ea185d7, baseline). GLM toco cero codigo.
Vantage: contenido relayado del documento docs/DW.12-PRERREGISTRO.md (202 l / 9 764 B / NA=0 / sha256 4b3f0465...d6083, LF, ASCII) en head 0efb252, rama dw.12-glotec-transporte-absoluto, worktree ionosphere-dw12-cpp limpio. Verificaciones read-only ejecutadas por DeepSeek contra origin/master (ea185d7). GLM no tiene acceso al repo: dictamen de contenido. Estandar de la serie.

D1 - Requisitos de 0499 N6 sobre el pre-registro: verificados uno a uno.
  (i) Lineas exactas: GloTecAdapter.cpp (395 l): base https://services.swpc.noaa.gov; transport lambda l.297-304; objetivo l.300; pure f.url l.291; GLOTEC_INDEX_URL l.12. CONFORME.
  (ii) Blast radius enumerado: 1 fichero / 1 linea (l.300); cadena transport <- glotbf::run (backfillFrom) <- fetchTEC <- App.cpp:3189 / DataManager; fetchURL / glotbf::run / fetchFrame / fetchIndex / pushHistoryFrame intactos; sin cambio de firma; fetchFrame sigue sin callers y no se conecta. CONFORME con la opcion (1) endosada en 0499 N6.
  (iii) Auditoria grep N6(iii): EJECUTADA con el mejor resultado posible: git grep fetchURL( sobre src; UNICA llamada con URL relativa = GloTecAdapter.cpp:300; GLOTEC_INDEX_URL (l.12) absoluta; full (l.274) prefijada; Dias/IrtamCoeff/SdoImage/Aurora/GIRO/Kc2g/Solar*/Storm/Xray absolutas; ningun fetchURL("/ en el arbol. La clase latente de defecto es SINGLETON: la propia l.300. LISTADA, no arreglada - disciplina de alcance correcta. N6(iii) CERRADO.
  (iv) No-goals: timeout 15 s / obs F (observar CURLE 28 post-fix); E-2; ventana replay 168 h; kReplayWindowSec 86400; H-window separado; D2; cache/replay/persistencia/HUD; fetchFrame sin callers no se conecta. CONFORME.
  (v) Criterio binario: N6-v completo (sin "fallos de transporte" en el primer ciclo; >= 1 tec_*.bin con epoch del dia CONTRASTADO POR EPOCH/SHA, NO MTIME; PROV_TEC ok edad < 1200 s; tecHist crece) + habituales (build rc=0; ctest 62/62; CI 61+1 + TS; numstat; greps post; sin amend). CONFORME - la caution mtime de 0499 N6 queda embebida.
  (vi) P4 rev-0499: incluido - test de replay SOLO tras ingesta demostrada de frames frescos; anima => P4 cerrado; estatico => H-window promovida y pre-registro aparte. CONFORME.

D2 - Auditoria del mecanismo (cambio propuesto sobre l.300):
    std::string full = (!url.empty() && url[0]=='/') ? "https://services.swpc.noaa.gov" + url : url;
    fetchURL(full, body);
  (a) Guarda: prefija SOLO si url empieza por '/'; las absolutas pasan intactas (sin doble prefijo); url vacia protegida por !url.empty(). CONFORME.
  (b) Semantica C++: literal + std::string via operator+ (const char* + std::string): valido.
  (c) Contabilidad de glotbf::run intacta: el lambda sigue llamando a fetchURL igual, solo cambia el argumento; lastCurl_ / transportOk / store sin tocar. CONFORME.
  (d) Borde residual REGISTRADO (sin accion, no bloqueante): una URL relativa SIN '/' inicial pasaria intacta y fallaria igual; no se observa ninguna en el indice medido (las de frames empiezan por '/'); aceptable en slice minimo; el fallback de cache queda como hoy.

D3 - Aritmetica de lineas: EXPECTATIVA REGISTRADA para el acta de ejecucion.
  El snippet relayado renderiza 2 lineas sustituyendo 1 (=> +2/-1 en ese render); el numstat declarado es +3/-1. Causa presumida: el documento real envuelve la linea larga std::string full = ... en 2 lineas fisicas (estilo del codigo) => 3 anadidas. NO es errata de sustancia: el diff exacto vive en el doc y el acta de ejecucion debe reconciliar numstat medido (+3/-1 esperado) contra el doc, documentando cualquier desviacion (lecciones 0482 N2; precedente DW.11 +1). Un solo fichero de codigo + el doc.

D4 - Nota de auditoria 0499 N4 (kIrtamReplayWindowSec): RESUELTA por medicion.
  kIrtamReplayWindowSec = 604800 (IrtamState.h:39); call sites App.cpp:2009 (pares tecHist) + App.cpp:6321 (sloB). kReplayWindowSec = 86400 (IrtamState.h:28, comentario "TEC 24 h") SIN call sites. Conclusion: el replay de TEC esta gobernado EN EL CALL SITE por kIrtamReplayWindowSec => ventana 168 h CONFIRMADA por enumeracion de call sites, no por nombre. kReplayWindowSec es una constante muerta con comentario enganoso - candidata de limpieza en el futuro slice H-window (sin accion ahora; no-goal de DW.12). El olor a nombre senalado en 0499 N4 era correcto y queda fijado por evidencia.

D5 - Protocolo: rama desde master ea185d7; commit solo con el doc; push relay deddd20; check limpio; cero codigo tocado antes de acta y GO (GO de David para preparar el pre-registro, respetado). CONFORME.

D6 - DICTAMEN Y PETICION.
  Dictamen: pre-registro DW.12 head 0efb252 CONFORME con 0499 N6 y el estandar de la serie. Sin erratas vinculantes; una expectativa aritmetica registrada (D3) y un borde residual no bloqueante (D2-d).
  Peticion a David: GO de ejecucion. El acta de ejecucion debe traer: (1) diff real vs plan con numstat reconciliado (+3/-1 esperado); (2) criterio binario N6-v con contrastes por epoch/sha; (3) greps post; (4) ctest 62/62 local + CI 61+1 + TS; (5) material de adjudicacion P4 rev (sesion de replay SOLO tras frames frescos demostrados); (6) observacion de CURLE 28 (obs F) si ocurre.
  Predicciones falsables registradas por GLM para la ejecucion DW.12:
    P5: en el primer ciclo fresco post-fix, la razon pierde "fallos de transporte" y aparece >= 1 tec_*.bin con epoch del dia (confirmacion causal de H-transport si se cumple).
    P6: PROV_TEC pasa de stale a ok con edad < 1200 s en cuanto fluyan frames.
    P7: si aparece CURLE 28 (timeout 15 s vs ~2,5 MB) post-fix, la obs F asciende de marginal a real y se decide aparte (no-goal aqui).
    P8: (P4 rev) con frames frescos entrando: replay anima => P4 cerrado; estatico => H-window promovida a slice propio.

D7 - Canonico pendiente: acta-0499.txt (sandbox caido en su turno; texto verbatim ya entregado y archivado como transcripcion por DeepSeek). Se entrega/cita por hash en cuanto el sandbox lo permita; el 0499-VERIF seguira el procedimiento 0495/0497.

Reconocimiento: pre-registro de primera - requisitos N6 completos uno a uno, grep de clase latente con resultado singleton, la nota de auditoria N4 resuelta por call sites, y el diff esperado declarado con numstat. El estandar se mantiene.

Relay: esta acta = from-glm 0500; proximos libres to-glm 0533, from-glm 0501.
Firmado: GLM (auditor). ASCII puro.
sha256: computar al archivar (vantage DeepSeek; canonico GLM proximo turno con sandbox).
