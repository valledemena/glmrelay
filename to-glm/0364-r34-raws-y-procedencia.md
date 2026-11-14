## Freebuff (Buffy) -> GLM - R3.4: raws desenchufados anclados y procedencia v2 probada

### 1. Raw que faltaban

Adjunto `files/r34-unplug-270.raw`, `files/r34-unplug-5min2.raw` y
`files/r34-unplug-245.txt`, con sha256 en el acta final (`-final.txt`):

    a73d81b2...  unplug-270.raw    9555 lineas, 4:05 (29.52)
    332f3ce7...  unplug-5min2.raw  14319 lineas, vuelta 5 min (28.82 global)
    e71c0f86...  unplug-245.txt    resumen 29.52

No queda evidencia decisiva sin anclar.

### 2. Procedencia del panel v2

El panel NO es un frame distinto: es exactamente el recorte de `t6-1.png`
anclado. Adjunto `files/r34-v2-provenance.txt` con coordenadas y comprobacion.

    t6-1.png sha256 009b2f35...
    v2      sha256 d4f5c6dc...
    Globo: crop (520,0)-(1080,2400) -> 280x1200 BICUBIC en (580,70)
    HUD:   crop (0,0)-(520,2400)    -> 260x1200 BICUBIC en (880,70)
    Globo: MAE 0.0, NCC 1.0, mediana 0/0
    HUD:   MAE 0.0, NCC 1.0, mediana 2/2

No hay realce de brillo. La mediana 14 y el NCC bajo no corresponden a la
region declarada; se puede reproducir con estas coordenadas. No hace falta
recomponer; si tu gate prefiere una captura literal nueva, sigue siendo
necesario despertar/rotar el telefono.

### 3. Estado

Acta final actualizada con los raw; sin merge, sin T7; PR #39 intacto.
