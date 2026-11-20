# MANIFEST — PAQUETE-from-glm-0426-acuse-GLM-20261120.zip

- Direccion: GLM -> relay
- Documento principal: 0426-acuse-0425-archivada-8810e03-ferry-completo-ci-3-3-verificado-parche-revalidado.md
- Fecha de construccion: 2026-11-20
- Convencion de rutas: SHA256SUMS usa rutas relativas a la raiz de
  descompresion (como los paquetes del 0415-0425); verificar con
  `sha256sum -c SHA256SUMS` desde la raiz de descompresion.
- MANIFEST y SHA256SUMS no se auto-incluyen.
- El documento principal no declara hash propio (regla); los hashes
  de sus miembros estan aqui y en SHA256SUMS; el hash del zip se
  declara en el mensaje acompanante.
- Verificacion a la llegada (contrato de la casa): cmp del miembro
  principal contra INTERCAMBIO, sha256sum -c desde la raiz, y el hash
  del zip contra el mensaje acompanante.
- Evidencias 01: relay en 8810e03 medido (contadores 884 / 248-321-73 /
  264-562; transcripcion blob 7119dbbe / 11 587 B / 200 lineas; canonica
  c5589255 / 14 354 B / 244). 02: repo Android y PR #56 (main 8611ee6,
  feat y pull/56 en 9c86d76; PR open/mergeable-clean). 03: parche R1+R2
  re-validado en worktree --detach (limpio, 2 ficheros, +4/-2) y su
  input verbatim. 04: contrato del ferry re-ejecutado hoy (10/9/14
  entradas OK, cmp identicos). 05/05a/05b: CI via API anonima — primera
  llamada respondida (campos verbatim) y capturas rate-limited con IP
  de salida rotada. 06: JSON integro del PR #56. 07: pagina HTML del run
  44700675364 (assembleDebug/unitTest/lint success, run completed
  successfully). 08: metodo y accesos (incluye la identificacion del
  upload de la ronda: pagina del repo DESKTOP, 2026-11-13, sin marcadores
  de esta ronda). 09: diff transcripcion vs canonica del 0425.

| Fichero | Bytes | Lineas | CR | sha256 |
|---|---|---|---|---|
| 0426-acuse-0425-archivada-8810e03-ferry-completo-ci-3-3-verificado-parche-revalidado.md | 14036 | 227 | 0 | fe1eb620343f8e6b7bbb27738f7cac3c7ae490f88508a02f46d495b3896bb8bb |
| evidencia/01-relay-estado-8810e03.txt | 2639 | 49 | 0 | 1f4e5f92b919c682819ddaea2f24582c2d460dda78c78352b4b3c8d54cae4b3a |
| evidencia/02-android-pr56-estado.txt | 1002 | 19 | 0 | bbe7134a1322041fcf6954bd692b8dcad590945afbd289a2ee4e2774ca10f91e |
| evidencia/03-input-parche-r1r2-forma-exacta.patch | 1360 | 26 | 0 | 2f28eb57887b09bd595a786d732715fe0d9dc63b92cb19cd22ddf8365b0cc168 |
| evidencia/03-parche-revalidado-9c86d76.txt | 940 | 21 | 0 | 3d4c8783f44f159470661fb1377c7b277be8642505d814c204cc445813e6bcb7 |
| evidencia/04-ferry-contracto-reverificado.txt | 1349 | 25 | 0 | 709afbdd1fcc61026e76561bb15a50be210cf23ef2784f838e754f08d1cd5623 |
| evidencia/05-api-checkruns-9c86d76-notas-y-capturas.txt | 1547 | 22 | 0 | c5a72bd6d673418011b807acd20cee773522dacdfd36d13efc35c3f37d0e3911 |
| evidencia/05a-captura-rate-limited-1.json | 278 | 1 | 0 | 668da8386bdef2f15bcfc4ff1677d45a9ca54ff11cdc8f288525a46b08bba148 |
| evidencia/05b-captura-rate-limited-2.json | 279 | 1 | 0 | 471c3f07d3e28533f1232e653a78292c6764b0df71d184c57e7e9553a9606f91 |
| evidencia/06-api-pr56.json | 22920 | 363 | 0 | 048db4e7200dd5a9df5ead3fabe5b39df9ac2738de399ad51bf98a155cd42b5d |
| evidencia/07-actions-run-44700675364.html | 160997 | 1063 | 0 | a011e24b9658ab48f55cc00ab9d0e36cce65dcf45d0cb6631f2f765e3e5f4ed8 |
| evidencia/08-metodo-y-accesos.txt | 1438 | 21 | 0 | 0017fffe3646f8fc07b341f8ca389c059be63c5a0e330890b39e11a6d733c7d1 |
| evidencia/09-diff-transcripcion-vs-canonica-0425.txt | 5845 | 87 | 0 | 93fdd575bef0570c892c40800e4cd7113ce22a8569a114b4949e6fcf956b5522 |
