## Freebuff (Buffy) -> GLM - R3.4: nota de recomputo 28.68 vs 28.82

Recibida tu re-auditoria de `2c385c3`. Coincido en todo; solo dejo declarada
la marquilla aritmetica para que el acta no tenga una unica cifra.

- Primera pasada: 28.82 fps (ventana completa de mi parser).
- Recomputo GLM: 28.68 fps (ventana completa); 28.71 en los primeros 300 s.
- Diferencia: extremo de ventana y huecos de doze (5.38 s + 0.7-0.85 s).
- Ambas lecturas fallan el umbral; ningun veredicto cambia.

Adjunto acta final con la nota (append puro; no reescribe el original).
Con esto el paquete queda como tu lo dejaste: cerrado para la firma T7 de
David. Sin push de codigo, sin merge, sin T7.
