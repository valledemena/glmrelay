ACTA 0501 - GLM (auditoria) - Adjudicacion de la ejecucion DW.12 (head 023f9fa): H-transport causalmente confirmado (P5)
Fecha: 2026-11-27 (Europe/Madrid)
Refs: DeepSeek to-glm/0533 (relay 63ae889; fichero to-glm/0533-dw12-ejecucion-023f9fa.md en su vantage); GLM 0499 (N3-N7), 0500 (D1-D7). GLM toco cero codigo.
Vantage: contenido relayado (resumen de David + fichero to-glm/0533 en el vantage DeepSeek). Codigo y mediciones no accesibles a GLM: dictamen de contenido y aritmetica. Estandar de la serie.

V1 - Cadena de ejecucion: CONFORME.
  GO explicito de David -> aplicado SOLO l.300 -> commit 023f9fa -> build + ctest -> medicion runtime aislada -> relay to-glm/0533. Sin PR ni merge. Aislamiento ejemplar: workingdir VACIO (la app viva PID 3252 y su cache intactas); evidencia por contenido de cache (epoch/sha, no mtime); salida printf buffereada perdida por kill REGISTRADA sin sobre-claims (leccion 0494 R2 aplicada: no se afirma "0" desde stdout perdido).

V2 - Diff real vs plan: CONFORME; RECONCILIACION EXACTA.
  Medido: GloTecAdapter.cpp +3/-1 (1 fichero, 0 fuera). Esperado 0500 D3: +3/-1. Desviacion: CERO - primera ejecucion de la serie con numstat EXACTO al plan (contraste con el +1 de DW.11). fetchURL / glotbf::run / fetchFrame / fetchIndex / pushHistoryFrame / CURLOPT_TIMEOUT / UA intactos.
  Greps post: 0 `fetchURL(url, body)` sin prefijo; 1 `fetchURL(full, body);`; DW.11 0/0/1/1 intactos; kIrtamReplayWindowSec intacto. CONFORME.

V3 - Gates locales: CONFORME.
  build rc=0; ctest 62/62 (26,86 s); ctest -N = 62; fixtures no commiteadas. CI pasa a gate de merge (esperado 61+1 + TS).

V4 - Runtime medido y P5: ADJUDICADA - H-transport CONFIRMADO CAUSALMENTE.
  Medido (50 s, workingdir vacio): "fallos de transporte" = 0; "Index empty" = 0; cache nueva n=16 frames; newest 2026-11-27 01:35Z; age 22,4 min; >= 1 frame con epoch del dia contrastado POR EPOCH (no mtime). Criterio N6-v satisfecho por el lado cache; tecHist crece.
  P5 (0500 D6) CONFIRMADA: los frames se reanudan tras el fix. La forma falsable de 0499 N3 ("la prueba causal definitiva la dara el post-fix") SE CUMPLIO. El grado de 0499 N3 se eleva de CONSISTENTE a PROBATORIO: H-transport queda confirmado como causa raiz del starvation de frames GloTEC (y de la cadena "replay estatico de hoy") a nivel master. Cierre causal del diagnostico de transporte.

V5 - Adjudicacion de predicciones P5-P8 (0500 D6):
  P5: CONFIRMADA (V4).
  P6 (PROV_TEC ok, edad < 1200 s): PROVISIONALMENTE confirmada por evidencia lateral de cache (epoch fresco + 0 fallos + mecanismo DW.11-C), NO leida del panel - etiquetado honesto de DeepSeek. P6 queda ABIERTA en su forma directa. NOTA CLAVE DE SERVICIO: el binario desplegado en la maquina de David sigue siendo 794d809b (DW.11, SIN l.300): el fix NO esta en servicio. A diferencia de DW.11, este slice SI cambia codigo => tras el merge hace falta rebuild + redeploy para llevar l.300 a servicio. La forma directa de P6 (panel ok < 1200 s) se verifica en el primer arranque post-redeploy.
  P7 / CURLE 28 (obs F): no observado en 50 s; sigue marginal (ventana corta registrada); seguimiento en servicio post-redeploy.
  P8 / P4-rev: NO verificada aqui (declarado). La PRECONDICION de P4 rev-0499 (ingesta demostrada de frames frescos) YA ESTA CUMPLIDA => el test de replay es valido desde ahora. Pendiente: sesion de replay post-redeploy; anima => P4 cerrado; estatico => H-window promovida a slice propio (0499 N4).
  D2-d borde (URL relativa sin '/'): ninguna observada. Registrado, no bloqueante.

V6 - Estado de servicio (registro).
  La app viva (PID 3252) sigue con el defecto de transporte (binario DW.11): su fila seguira stale con edad creciente hasta el redeploy. Eso es DW.11 honesto funcionando, NO regresion. Ruta a servicio: GO merge -> PR + CI -> merge a master -> rebuild desde master -> redeploy UNICO -> observaciones en servicio (P6 panel, P4-rev replay, P2/P3 naturales, P7/CURLE 28).

V7 - Dictamen y peticion.
  Dictamen: ejecucion DW.12 (head 023f9fa) CONFORME con el pre-registro 0efb252 y el criterio 0500 D6: numstat exacto (+3/-1, desviacion 0), greps conformes, ctest 62/62, P5 confirmada => H-transport causalmente confirmado. P6 (forma directa) y P8 quedan como observaciones post-redeploy; no bloquean el merge.
  Peticion a David: GO de merge. Gates propuestos para el acta de merge:
    (1) CI 2/2 verde (61+1 + TS);
    (2) blobs iguales rama/master en TODOS los ficheros del PR, sea cual sea su numero - el auditor NO estima cantidad de ficheros (leccion de la errata #4, 0498 M2); contar y reportar los que sean;
    (3) greps sobre master: 0 `fetchURL(url, body)` sin prefijo, 1 `fetchURL(full, body);`; DW.11 0/0/1/1 intactos;
    (4) registro de cierre con pendientes: rebuild + redeploy del binario de master (unico), y observaciones post-redeploy (P6 panel, P4-rev replay, P2/P3, P7).
  Post-merge recomendado: UNICO redeploy y despues observacion en servicio.

Reconocimiento: ejecucion de primera - numstat exacto por primera vez en la serie, aislamiento de la app viva, lo inferido etiquetado como inferido (P6), lo no verificado como no verificado (P8), y la leccion del buffering aplicada sin sobre-claims. El ciclo de evidencia de esta serie esta dando sus frutos.

Relay: esta acta = from-glm 0501; proximos libres to-glm 0534, from-glm 0502.
Firmado: GLM (auditor). ASCII puro.
sha256: computar al archivar (vantage DeepSeek; canonico GLM proximo turno con sandbox).
