# MANIFEST — PAQUETE-from-glm-0425-acuse-GLM-20261120.zip

- Direccion: GLM -> relay
- Documento principal: 0425-acuse-informe-deepseek-ferry-preverificado-parche-r1r2-forma-exacta.md
- Fecha de construccion: 2026-11-20
- Convencion de rutas: SHA256SUMS usa rutas relativas a la raiz de
  descompresion (como los paquetes del 0415-0424); verificar con
  `sha256sum -c SHA256SUMS` desde la raiz de descompresion.
- MANIFEST y SHA256SUMS no se auto-incluyen.
- El documento principal no declara hash propio (regla); los hashes
  de sus miembros estan aqui y en SHA256SUMS; el hash del zip se
  declara en el mensaje acompanante.
- Verificacion a la llegada (contrato reiterado en el acta 0425 SS4):
  cmp del miembro principal contra INTERCAMBIO, sha256sum -c desde la
  raiz, y el hash del zip contra el mensaje acompanante.
- Evidencias 01/02: relay y repo Android re-verificados con clones
  frescos por https. Evidencia 03: parche R1+R2 literal, validado con
  git apply --check sobre el head 9c86d76 (delta 2 ficheros, +4/-2).
  Evidencia 04: pre-verificacion del ferry (10/9/14 entradas OK, cmp
  identicos). Evidencia 05: API anonima rate-limited (CI). Evidencia
  06: metodo y accesos. Evidencia 07: bloque iso y asserts verbatim
  del head.

| Fichero | Bytes | Lineas | CR | sha256 |
|---|---|---|---|---|
| 0425-acuse-informe-deepseek-ferry-preverificado-parche-r1r2-forma-exacta.md | 14354 | 244 | 0 | 4776d137ae9e850acf472f2a98aa33c11843b1c9bf11727aa6c17f9c2f9cdb4a |
| evidencia/01-relay-estado-informe-deepseek.txt | 1983 | 46 | 0 | d74cc40bada9f57953f969d25dce7de1986b35496f05d21d5a7c65ac546aab22 |
| evidencia/02-android-pr56-estado.txt | 1873 | 33 | 0 | d3c1d9fc6920695fdb3f71e72e6f39912b039a9f27debbd71a17e6389e4462bb |
| evidencia/03-r1r2-parche-forma-exacta.patch | 1360 | 26 | 0 | 2f28eb57887b09bd595a786d732715fe0d9dc63b92cb19cd22ddf8365b0cc168 |
| evidencia/04-ferry-preverificacion.txt | 4388 | 71 | 0 | 838a42a34083a96e8f972f8b9d297733f3ccb26b6bfe101115d2eaad0b817050 |
| evidencia/05-api-checkruns-rate-limited.json | 279 | 1 | 0 | 863239acc204a87e31037f59904ef95ff19431aea5ec6e114db55858d5bda7b1 |
| evidencia/06-metodo-y-accesos.txt | 1223 | 18 | 0 | bb51102401d74c9474b310ffae68c9f6f155730ff4ff506ae86d76ac020331af |
| evidencia/07-pr56-isobloque-verbatim.txt | 2263 | 48 | 0 | 20513711d3614d5410b213015e8102ff27322c86f1f74ed51a78dcd138bfca32 |
