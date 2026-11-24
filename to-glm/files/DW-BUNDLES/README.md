# Bundles DW entregados a GLM via relay (2026-11-24 Madrid)

Cadena (acta 0452 B, cambio de actor to-glm/0486): OpenCode genera y publica
sha256; David delego la entrega en OpenCode; GLM verifica a la llegada.

Ubicacion en el relay: to-glm/files/DW-BUNDLES/

| Bundle | Bytes | sha256 |
|---|---|---|
| dw2-web-0961a57-f746654.bundle | 2778 | a0e9ec88866c536b84b33972b34d0a5f11f6d633f2493d8335a28eb700f2da46 |
| dw3-web-118c7e9-5854e04.bundle | 3791 | 53b71fcbb9fb35e5301ace24b8f056f8e569a62adf0144c605111c72cf940e01 |
| dw4-cpp-e680d01-3f4f8bd.bundle | 3927 | 881c6b781bebfcf2d42ab2e2db9971e432bb604855177464de04e0bde642d089 |
| dw5-cpp-3716295-151bd87.bundle | 4918 | dcace283f22e76db2eb0c435f06076685f2206b872129d6c6f46904056b7ca51 |
| dw0-cpp-baseline-d9fb809-e680d01.bundle | 141251 | 4e90b4a8566b8cb0fc7e0d85ead2ac10544f0b13e47028e155b12b283367a632 |
| dw6-cpp-b392e68-7c1ecdc.bundle | 4851 | 36f4bcf5cc433a389aa4db632b78d8fbdad9fb0ca89962935b3046b084b49816 |

Verificacion: `sha256sum -c SHA256SUMS` (6 entradas) y `git bundle verify <f>`.
Los cuatro DW + baseline + DW.6 suman 161516 B.
