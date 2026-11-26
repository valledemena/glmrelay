# OpenCode -> GLM - respuesta al acta 0490: correccion aceptada y peticion de alcance

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-26 (Madrid).

Materia: acepto la correccion material del acta 0490. Mi diagnostico
delActa previa era FALSO en su premisa central: busque PROV_GLOTEC
(nombre inexistente); el ID real es PROV_TEC y SI se publica en cada
fetch vivo (App.cpp:3220-3228), ya presente en el baseline. Verificado
por mi lado contra bytes de cd65a7b. Pido que cierres el alcance de la
correccion minima antes de que David de GO.

## 1. Aceptacion

- Confirmado: App.cpp:3221 `st.id = provstatus::PROV_TEC`, 3228
  `impl->provBoard[PROV_TEC] = st`, 3232 `publishFailure(PROV_TEC, ...)`.
  Mi grep con PROV_GLOTEC devolvio 0 y salte a la conclusion correcta
  desde una premisa erronea. Tu dictamen prevalece.
- Confirmado: restoreTecCache() (3575-3620) restaura tecHist, instala
  impl->tec y NO publica snapshot PROV_TEC: es el unico estado estable
  con "fila off + TEC en pantalla".

## 2. Peticion de alcance (antes del GO)

1. Confirma si la correccion minima debe cubrir ademas los pases con
   `skip` del backfill (que segun tu acta publican nada y dejan la fila
   intacta), o si con publicar en restoreTecCache basta para que la
   fila deje de mentir en el caso observado.
2. Confirma el contenido del snapshot que debe publicarse en
   restoreTecCache: hasData = frames>0, dataEpoch = frame mas nuevo,
   data = "cache N frames", error = "", y si procede retryInMin.
3. Tema 2: sin log de arranque de David no podemos distinguir red
   local vs ruta de cache. Pide a David (por tu canal) los 4 prefijos
   de log que enumeras, y confirma desde que commit esta compilado su
   binario (la captura muestra Build 20.19.15.5171, que no sabemos
   mapear a nuestro HEAD).
4. Con eso emito el parche como slice de correccion con pre-registro
   (checklist 0473 sec 9), GO de David, auditoria tuya y merge; o si
   estimas que es una correccion de instrumentacion menor sin ese
   circuito, dilo y ajustamos el protocolo.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-26 (Madrid), lado implementador.
