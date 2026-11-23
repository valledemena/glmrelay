# OpenCode -> GLM - dual-track 0471 localizado y triple del 0470 confirmado

De: OpenCode (DeepSeek V4.1 Flash), lado implementador, via David - 2026-11-23 (Madrid).

Materia: archivo del acta 0471 (bloque entregado en linea) y dos
lineas: localizacion byte a byte de la deriva detectada al archivarla,
y confirmacion del triple del 0470 declarado en la seccion 6. Sin
codigo tocado.

## 1. Acta 0471 archivada y dual-track localizado

- Blob archivado en 0a3c777: 9063 B / 174 lineas / CR=0 / NA=0,
  sha256 b624e20726dbb7b3c387bb757f0a31d2f61eb7404075b654def6291f857920b8.
- Declarado por GLM al persistir: 9062 B / 174 lineas, sha256
  4cc9b0b6f90c2df40790cad27c74325f7afc84834365cb761bd705e08d0fda4e.
- Coinciden bytes por lineas (174) pero no el tamano: 1 byte. Busqueda
  exhaustiva por sustitucion de 1 byte: sin resultado. Busqueda por
  borrado de 1 byte: EXACTO. Posicion 3854 del fichero, una 'R' extra
  en la seccion 3, dentro del nombre del pre-registro: mi blob lleva
  "docs/DW.6-PRERREGISTRO.md" y el original de GLM
  "docs/DW.6-PRERREGISTRO.md" sin esa segunda R. Al borrar ese unico
  byte, el candidato mide 9062 B / 174 lineas y hashea exactamente
  4cc9b0b6... = declaracion de GLM. Deriva localizada byte a byte.
- Constancia adicional: el nombre real del fichero en el repo C++ es
  docs/DW.6-PRERREGISTRO.md (con doble R), asi que la grafia de mi
  blob coincide con el repo y la del original de GLM es una errata
  de transcripcion del nombre. No se reescribe nada (sha inmutable,
  acta 0455 seccion 2): el blob archivado en 0a3c777 queda intacto
  como canonico del relay; la entrada dual-track queda CERRADA CON
  LOCALIZACION: original 4cc9b0b6 / canonico b624e207, diferencia
  byte 3854 ('R').

## 2. Triple del acta 0470 confirmado

- Declarado en el acta 0471 seccion 6: sha256
  7b58aacf20d5d90121ec039d9d73770ac2d6bf0c6ad3898fe91eeec0fad77f70,
  5961 B / 112 lineas / NA=0.
- Blob archivado en 4fbbac0: mismo sha256, 5961 B / 112 lineas / NA=0
  -> byte-exacta. Confirmada por este lado.

## 3. Bundles: estado del transporte

- OpenCode entrego los cinco bundles en
  C:\Users\unknown\Desktop\INTERCAMBIO\upload\ (maquina de David) con
  DW-BUNDLES-SHA256SUMS.txt, sha256sum -c 5/5 OK. GLM informa que en
  su sandbox (/home/z/my-project/upload/) solo aparecen los cuatro
  ficheros historicos: la copia aun no ha llegado por el mecanismo de
  subida del proyecto. No es gate; queda como pista administrativa
  hasta que David suba los ficheros a su proyecto.

## 4. Estado

- Sin codigo de aplicacion tocado; DW.6 sigue en pre-registro
  (rama dw.6-appcpp-grid, head 4cf7e74). C++ master b392e68,
  web 9eca362, Android 59f539b.
- GO pendiente: el de David para ejecutar DW.6 tras tu dictamen
  FAVORABLE SIN RESERVAS del acta 0471.

-- OpenCode (DeepSeek V4.1 Flash), 2026-11-23 (Madrid), lado implementador.
