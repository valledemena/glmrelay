# MANIFEST — PAQUETE-from-glm-0423-acuse-GLM-20261120.zip

- Direccion: GLM -> relay
- Documento principal: 0423-acuse-archivo-0422-errata-contadores-go-push-r467.md
- Fecha de construccion: 2026-11-20
- Convencion de rutas: SHA256SUMS usa rutas relativas a la raiz de
  descompresion (como los paquetes del 0415-0422); verificar con
  `sha256sum -c SHA256SUMS` desde la raiz de descompresion.
- MANIFEST y SHA256SUMS no se auto-incluyen.
- El documento principal no declara hash propio (regla); los hashes
  de sus miembros estan aqui y en SHA256SUMS; el hash del zip se
  declara en el mensaje acompanante.
- Verificacion a la llegada (contrato del to-glm/0422 SS2 y
  to-glm/0423 SS7, reiterado en el acta 0423 SS7): cmp del miembro
  principal contra INTERCAMBIO, sha256sum -c desde la raiz, y el
  hash del zip contra el mensaje acompanante.
- Evidencia 06 es el script del oraculo (instrumento re-derivable de
  la evidencia 05); las demas son salidas de medicion. La evidencia
  02 es el volcado verbatim del 0422 archivado (reconstruccion de
  David) tal como vive en c30760e, para custodia.

| Fichero | Bytes | Lineas | CR | sha256 |
|---|---|---|---|---|
| 0423-acuse-archivo-0422-errata-contadores-go-push-r467.md | 15665 | 254 | 0 | dbdc636f049dd900976bb3b1aa42f8c7f1c8f7ea1ae3c8a7982f10719e08638d |
| evidencia/01-relay-estado-c30760e-contadores.txt | 1844 | 45 | 0 | 236e71685285a8bc6e1b269dcf4d0f441b1d760215c86990abd5f58f9071c9f7 |
| evidencia/02-0422-archivado-verbatim.md | 4158 | 86 | 0 | 4ba841af98e3f319a4999f5e0ba13ba7c7fc526d01c8de27e6ed12a0ac57d1b3 |
| evidencia/03-cotejo-canonical-vs-archivado.txt | 5786 | 96 | 0 | 3f713800c2c63b495c4ccee0dbfe8ff5d4a9c909077367026ccb0cb690c6a75f |
| evidencia/04-android-estado-r467-push.txt | 2495 | 38 | 0 | 8d44a8b533053edd07632fe1e60938b5e720726bb989ca595c13d0bb3b2787a1 |
| evidencia/05-oraculo-odref-bandas.txt | 1653 | 32 | 0 | e15148fd38b9f143c8d640fa8b59737e5532e2984e09db1731534bdc623f482c |
| evidencia/06-oraculo-odref.py | 4928 | 130 | 0 | 4aa3173dac84d3cb3b0cbbf1b5d7d62c69e26bc484be532685cc2dc425a3d11c |
| evidencia/07-paquete-0422-verificacion.txt | 1877 | 39 | 0 | a370f7bb764c4a365a62138200dc48e48da631e449a7bce4d54608aedeb67d68 |
| evidencia/08-metodo-y-accesos.txt | 2434 | 38 | 0 | 7d8bdb70eea3fc5e4516c616b8f77712c98726604f185aa4c9b68c9e1e04b437 |
