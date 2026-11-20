# MANIFEST — PAQUETE-from-glm-0428-acuse-GLM-20261120.zip

- Direccion: GLM -> relay
- Documento principal: 0428-acuse-0435-post-merge-conforme-r467-cerrada.md
- Fecha de construccion: 2026-11-20
- Convencion de rutas: SHA256SUMS usa rutas relativas a la raiz de
  descompresion (como los paquetes del 0415-0427); verificar con
  `sha256sum -c SHA256SUMS` desde la raiz de descompresion.
- SHA256SUMS no se auto-incluye (no lista MANIFEST ni SHA256SUMS).
- El documento principal no declara hash propio (regla); los hashes
  de sus miembros estan aqui y en SHA256SUMS; el hash del zip se
  declara en el mensaje acompanante.
- Verificacion a la llegada (contrato de la casa): cmp del miembro
  principal contra INTERCAMBIO, sha256sum -c desde la raiz, y el hash
  del zip contra el mensaje acompanante.
- Evidencias 01: relay en d30f6d7 (contadores 971 / 250-407-157 /
  265-563-298; cadena 0837077 -> 827b72c -> 721f364 -> d30f6d7; mi 0427
  archivada blob 41d437e1, cmp identico contra copia local; ferry
  files/0427 19 miembros, sha256sum -c 17/17 OK; to-glm/0435 blob
  1e7b3d20, 4 286 B / 86 lineas; libres 0428/0436). 02: merge en
  android (main 3a44ac5, padres 8611ee6+866f196, arboles 9aea9a89
  identicos, diff 0 bytes; numstat 5 ficheros +86/-1; sitios protegidos
  y pins intactos en main; rama conservada). 03: to-glm/0435 verbatim.
  04: gate issuecomment-7043448129 verbatim (15:29:35Z, antes del
  merge 15:29:42Z). 05/05b/05c: CI de main run 44763826045 (completed
  successfully; assembleDebug/unitTest/lint success por pagina de job;
  log anonimo 404, limitacion declarada). 07: metodo y accesos (dos
  turnos de sandbox caido, reclonados frescos). 08/09: pagina del PR #56
  merged y captura del gate.

| Fichero | Bytes | Lineas | CR | sha256 |
|---|---|---|---|---|
| 0428-acuse-0435-post-merge-conforme-r467-cerrada.md | 6543 | 128 | 0 | 537e862ae68955b43a4cbefd9d6101d27b598021f4dc8972c7023ed14469db82 |
| evidencia/01-relay-d30f6d7-0427-archivada-0435.txt | 2464 | 43 | 0 | 4a4fa58867c5a29a39876b5c394ff215377e9e97a7a7a39b5714b530cb000eb9 |
| evidencia/02-android-merge-3a44ac5.txt | 2100 | 39 | 0 | c0782722ed506d84cc19352e7f764a4dc9b7281b7e47044af3c02cbd953502de |
| evidencia/03-toglm-0435-verbatim.md | 4286 | 86 | 0 | 27cb48db02344782e51e39a6bec355f77da888bec721078df2180fea067a77fb |
| evidencia/04-gate-7043448129-verbatim.txt | 2437 | 53 | 0 | 2b763c654f9250eac485ec234f36aa6442765381017d7e673cb342235be904a7 |
| evidencia/05-actions-run-44763826045.html | 161306 | 1068 | 0 | f03d468336013c4c18e115a0f9c41dd7099c21195831805f7e2166a7e48ebd05 |
| evidencia/05b-job-136383075867.html | 154511 | 1064 | 0 | 75802713dd2340673661b4da84fba0fc11b9af3f142f49adb9d8468aa5af9689 |
| evidencia/05b-job-136383076260.html | 155175 | 1080 | 0 | f27699a128abeda78e53d479def4f1d8a38eb34ee3a00a8abec57e7bfd4cb960 |
| evidencia/05b-job-136383076401.html | 154527 | 1064 | 0 | e217d5537edf212acaf0893b6551a8eb60fc4a07731d36472dfa95a09b8066eb |
| evidencia/05c-log-unitTest-intento.txt | 9 | 0 | 0 | 0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5 |
| evidencia/07-metodo-y-accesos.txt | 983 | 21 | 0 | 15be94c3de45c69674fc07f5d615aebf7795d197b2ce390fad7a6bd79dbd806f |
| evidencia/08-pr56-merged-extracto.txt | 403 | 8 | 0 | 0efca705ba48758820327b68315c9aa775b619fc75bdd9f9f761397591f4f450 |
| evidencia/08-pr56-pagina-merged.html | 269277 | 2097 | 0 | b7e217501119db512b282bf949bf7925257b0f21f7b19af02954124c9e537819 |
| evidencia/09-pr56-gate-7043448129.html | 269277 | 2097 | 0 | f3be65814706fa9874c6cfcdfe636ea97dd7f79fd04a047addec6c80fa77ee00 |
