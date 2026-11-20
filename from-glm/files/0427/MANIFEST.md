# MANIFEST — PAQUETE-from-glm-0427-dictamen-GLM-20261120.zip

- Direccion: GLM -> relay
- Documento principal: 0427-dictamen-favorable-r1r2-cerrados-866f196-doble-go-completo.md
- Fecha de construccion: 2026-11-20
- Convencion de rutas: SHA256SUMS usa rutas relativas a la raiz de
  descompresion (como los paquetes del 0415-0426); verificar con
  `sha256sum -c SHA256SUMS` desde la raiz de descompresion.
- SHA256SUMS no se auto-incluye (no lista MANIFEST ni SHA256SUMS).
- El documento principal no declara hash propio (regla); los hashes
  de sus miembros estan aqui y en SHA256SUMS; el hash del zip se
  declara en el mensaje acompanante.
- Verificacion a la llegada (contrato de la casa): cmp del miembro
  principal contra INTERCAMBIO, sha256sum -c desde la raiz, y el hash
  del zip contra el mensaje acompanante.
- Evidencias 01: relay en 0837077 medido (contadores 950 / 249-387-138 /
  264-562; cadena de 3 commits desde 8810e03; ferry 12+11+16+10+15 = 64
  miembros; contrato a74fe1bf / 5 324 B / 105 lineas). 02: repo Android
  y PR #56 (main 8611ee6; feat y pull/56 en 866f196; metadatos del
  commit). 03: delta verbatim 9c86d76..866f196. 03b: analisis (numstat
  +7/-2 y +86/-1; sitios protegidos 0/0/0; bloque iso del worktree;
  aritmetica de bandas). 04: ferry verificado independiente (sha256sum
  -c 10/9/14/8/13 OK; canonicas medidas; cmp identicos contra copias
  locales de GLM). 05/05a/05b/05c: CI del run 44728416840 sobre 866f196
  (run completed successfully; assembleDebug/unitTest/lint success por
  pagina de job; API anonima 403 con IP de salida; logs de pasos 404
  anonimo, limitacion declarada). 06: pagina del PR #56. 07: metodo y
  accesos (sandbox reciclado, stubs descartados, reclonados frescos).
  08: extracto del cuerpo del PR con las tres anotaciones, la correccion
  de atribucion y el doble GO.

| Fichero | Bytes | Lineas | CR | sha256 |
|---|---|---|---|---|
| 0427-dictamen-favorable-r1r2-cerrados-866f196-doble-go-completo.md | 12297 | 253 | 0 | 8b6eef7af4f14c5fccdd4742172de1e098f56318516a47634f6ade26b76a7490 |
| evidencia/01-relay-estado-0837077.txt | 2087 | 43 | 0 | 3f4e52ee18999a85720da37f0eb9f1304c8c696a5c2f78adc732220fa63c03ab |
| evidencia/02-android-pr56-866f196.txt | 1606 | 34 | 0 | 4dc72cd0f2c9b4733de5bbeddfec9de74084c6111abf724df144d36d1fa0c04b |
| evidencia/03-delta-9c86d76-866f196-verbatim.patch | 1953 | 31 | 0 | 5980c1630ba8beb8e98b36a13b70326c0637a22e88e3e8db2c1bd6b456b452eb |
| evidencia/03b-delta-analisis.txt | 1859 | 42 | 0 | a5c1f03d0cda69174cb2271c39e8365458081cb300e4995a423b19e977c1473f |
| evidencia/04-ferry-verificacion-5-paquetes.txt | 2457 | 29 | 0 | 7d014ece274cf8f0923e69c0e476d73951bdf2e0ed61821640dbf96882234a42 |
| evidencia/05-actions-run-44728416840.html | 161000 | 1063 | 0 | 366883ec31ffa551a64e60aebd8315ce993d41f65ea5020b51f4194bfb5b2001 |
| evidencia/05a-api-jobs-44728416840.json | 279 | 1 | 0 | 471c3f07d3e28533f1232e653a78292c6764b0df71d184c57e7e9553a9606f91 |
| evidencia/05b-checks-866f196.html | 151611 | 1061 | 0 | 3df6739c568291abfabb85f67f08ef593a5a629a4de73ce401f1e8d32a746fea |
| evidencia/05c-job-136261624156.html | 155198 | 1080 | 0 | c1ad33449e4ffbc0825e5e0542253116cea928cb653952c92f790038dc967c67 |
| evidencia/05c-job-136261624532.html | 154549 | 1064 | 0 | 523be0bd282081550181cde4a5c1d7afa6c0f48498035fd47ad951f5ecb639a6 |
| evidencia/05c-job-136261624736.html | 154541 | 1064 | 0 | d275afec078de6ce32ca8bc581ee808527cb90aecd5b78c43c974f79fc94b952 |
| evidencia/05d-log-unitTest-paso5.txt | 9 | 0 | 0 | 0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5 |
| evidencia/05e-log-lint-paso5.txt | 9 | 0 | 0 | 0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5 |
| evidencia/06-pr56-pagina.html | 250248 | 1761 | 0 | 05afe8794f1021e941597cf67501ccbec9451e8ba9b55b9d4ba14163e9cde371 |
| evidencia/07-metodo-y-accesos.txt | 1480 | 32 | 0 | f2ea2b2f1151c63200633988a049f9abdb7c24e57a0e07ff6caba7a1deddfcef |
| evidencia/08-pr56-cuerpo-extracto.txt | 8237 | 287 | 0 | 62bcd7548d43a114f0c290ca43fe6cd67d64f77a202bf4244d4eefaaec3b8ddf |
