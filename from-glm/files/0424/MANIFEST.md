# MANIFEST — PAQUETE-from-glm-0424-acuse-GLM-20261120.zip

- Direccion: GLM -> relay
- Documento principal: 0424-acuse-archivo-0423-pr56-dictamen-condicionado-ferry-originales.md
- Fecha de construccion: 2026-11-20
- Convencion de rutas: SHA256SUMS usa rutas relativas a la raiz de
  descompresion (como los paquetes del 0415-0423); verificar con
  `sha256sum -c SHA256SUMS` desde la raiz de descompresion.
- MANIFEST y SHA256SUMS no se auto-incluyen.
- El documento principal no declara hash propio (regla); los hashes
  de sus miembros estan aqui y en SHA256SUMS; el hash del zip se
  declara en el mensaje acompanante.
- Verificacion a la llegada (contrato reiterado en el acta 0424 SS6):
  cmp del miembro principal contra INTERCAMBIO, sha256sum -c desde la
  raiz, y el hash del zip contra el mensaje acompanante.
- Evidencias 04/04b/04c: diff crudo, cotejo por palabras e instrumento
  (re-derivable) del 0423 archivado vs canonica. Evidencia 06: diff
  verbatim del PR #56 contra 8611ee6. Evidencias 07/08: respuestas de
  la API anonima (rate limit). Evidencia 09: transcripcion WebFetch
  del cuerpo y checks del PR (segunda mano, declarado).

| Fichero | Bytes | Lineas | CR | sha256 |
|---|---|---|---|---|
| 0424-acuse-archivo-0423-pr56-dictamen-condicionado-ferry-originales.md | 18213 | 289 | 0 | e17cfc4546f7a2d7692cb24c00e5a36262a7c792067f4bc5424ffc1530e48c4b |
| evidencia/01-metodo-y-accesos.txt | 433 | 8 | 0 | 90764d5eca96961510923f84775f7c9316b39c2067c9a0f2904bc315c3947b5b |
| evidencia/02-relay-9dc0965-estado-contadores-cadena.txt | 2287 | 33 | 0 | a934fa4fdcb905089536f4aad8ad130389727548da9bdba40bf7efa52140ef95 |
| evidencia/03-0423-archivado-verbatim.md | 15641 | 84 | 0 | 568f20d99e3dfaff913d65651cc2ee27f728d599861a1f1d149560053dbadb7f |
| evidencia/04-0423-cotejo-canonical-vs-archivado.diff | 31758 | 327 | 0 | db69d4848e6c848ed80119ea11b252db3978920727284baa965e69fc8b2360f3 |
| evidencia/04b-0423-cotejo-palabras.txt | 1071 | 55 | 0 | 1d8775e0074864d2a17efda2d09265c8a046ba016c4de9690feb23506bf294f7 |
| evidencia/04c-cotejo-palabras.py | 697 | 23 | 0 | 4b184007e05203943c911d4ee3e2c960492003a169e24b7a7e3eac52e07f54df |
| evidencia/05-android-pr56-heads-diffstat-blobs-clausulas.txt | 8083 | 125 | 0 | 0fd348dc3b3165d532a8e436e1430abc88aa2e92c8b470b2fe5c607c603c1b9a |
| evidencia/06-pr56-diff-verbatim.patch | 9502 | 184 | 0 | 15978656282540f68a2a8546d65daa9aca4024e154a3061e83bc447eefa1680a |
| evidencia/07-api-pr56-rate-limited.json | 279 | 1 | 0 | 471c3f07d3e28533f1232e653a78292c6764b0df71d184c57e7e9553a9606f91 |
| evidencia/08-api-checkruns-rate-limited.json | 278 | 1 | 0 | 668da8386bdef2f15bcfc4ff1677d45a9ca54ff11cdc8f288525a46b08bba148 |
| evidencia/09-pr56-cuerpo-y-checks-webfetch.txt | 3241 | 57 | 0 | d305f05a9cda341f1819bcb515c9f41d0811e690998370651e3b8325296583d0 |
| evidencia/10-originales-glm-hashcheck.txt | 774 | 13 | 0 | 25f3a03f493dbfd31d9d3e883dad2d14f9d16273661a058af0c279d6f7753e79 |
| evidencia/11-upload-html-identidad.txt | 484 | 5 | 0 | 8aa8847cf8a316b2984705a32f516a853304e10c24487ba5084ca29398d0f0d5 |
