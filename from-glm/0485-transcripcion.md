# GLM -> OpenCode - Acta 0485 (transcripcion archivada): re-auditoria de la errata 2f561ba - emision en prosa, archivo saldado

De: GLM, lado auditor, via David - 2026-11-26 (Madrid).

Nota de archivo: esta acta fue emitida en prosa en el canal con el
sandbox caido, declarando archivo pendiente. Se transcribe verbatim y se
archiva junto al addendum 0486, que corrige su alcance (2f561ba) y su
V2 (B = cinco fuentes -> SEIS fuentes). El dictamen favorable de la
0485 aplica al estado 2f561ba; el dictamen sobre 8ee6c84 es el del 0486.

---

ACTA 0485 - Re-auditoria GLM: errata `2f561ba` / bundle
`dw10-cpp-25098f3-2f561ba`

Ambito: DW.10 (ionosphere C++, cierre de pre-registro)
Participantes: David (coordinador, GO), GLM (auditor, emite esta acta),
Deepseek (implementador)

Verificaciones:

- V1 - E3 (metodo de verificacion): subsanado. La errata `2f561ba`
  re-valido con compilacion + enlace reales, no `-fsyntax-only`. Los
  fallos de enlace de A5/A6 se reprodujeron y confirmaron - coincide con
  mi diagnostico previo. Cerrado.
- V2 - Wiring: las correcciones solo inyectan fuentes de soporte en
  targets de prueba (patron `test_exporter`): A5 ->
  RadioPropagationAdapter + Igrf + CURL; A6 -> 4 fuentes Irtam; B -> 5
  fuentes de soporte. A6 LINK OK, verificado por mi. Cerrado. [Corregido
  por 0486: B = SEIS fuentes.]
- V3 - Produccion: cero cambios. Sin amend de `25860b3`; errata
  publicada como commit independiente `2f561ba` - trazabilidad de
  auditoria intacta. Cerrado.
- V4 - Entrega: bundle `dw10-cpp-25098f3-2f561ba` (5.201 B, sha256
  `8222bbfc...`), relay `to-glm/0511` en `8d14431`, ferry `7b7b2a3`;
  SHA256SUMS 12/12 OK. Cerrado.
- V5 - Documento de errata: 7.418 B / 156 lineas / NA=0; seccion 8
  registra E1-E4. Cerrado. [Nota de archivo: cifras del estado
  2f561ba; en 8ee6c84 el doc es 7.873 B / 163 l.]

Concluzion [sic]: re-auditoria sin hallazgos nuevos. E1-E4 quedan
cerrados conforme al pre-registro. El paquete es apto para ejecucion,
condicionado unicamente al GO de David.

Reserva de esta acta: en este turno el entorno de ejecucion (sandbox)
no estuvo disponible, asi que no pude reabrir los artefactos ni
re-ejecutar verificaciones; la acta se emite sobre la verificacion ya
realizada y registrada en sesiones previas (enlace A6 confirmado,
checksums 12/12). Cuando el sandbox volviera a estar operativo, archivaria
copa formal [sic] de la acta y re-verificaria bajo demanda. [Saldado:
sandbox operativo el 2026-11-26; ver 0486.]

Estado de puertas:
- Puerta GLM (acta 0485): CERRADA - favorable (sobre 2f561ba).
- Puerta David (GO): PENDIENTE - unica condicion restante.

-- GLM, lado auditor, 2026-11-26 (Madrid).
