#!/usr/bin/env python3
# Ronda 0423 (GLM) — oraculo de alcance de bandas para la formula implementada
# del R4.6.7 (declarada por David, commit 9c86d76, sin push):
#   float logNe = 8.0 + 4.5 * (odIso / 0.49f);   odIso = odR + odM (acumulado)
# Replica el mismo barrido del oraculo 0422-evidencia-05 (camara D en
# {2.0, 2.5, 3.3, 4.5} radios, parametro de impacto b en [0, 1.03] a paso
# 0.001, uSteps 8/12/16, limite lejano = back-face del shell) y responde:
#   1. Rango real de odIso (re-derivado; debe reproducir 0.49412/0.49361/0.49343).
#   2. Donde caen los pines 10.5/11.0/11.5 en unidades odIso y normalizadas.
#   3. Entrada maxima odIso/0.49 y logNe maximo resultante por calidad.
#   4. Margen de alcance de la banda mas alta contra el maximo por calidad.
# Aritmetica propia sobre constantes publicas de main (AtmoShaderConstants,
# blob 62f5f6c9): no ejecuta el shader ni depende de GPU.
import math

PLANET_R = 1.0
ATM_R = 1.0255
H_R = 0.0085
H_M = 0.012
BANDS = (10.5, 11.0, 11.5)
LOGNE_LO, LOGNE_SPAN = 8.0, 4.5   # des-normalizacion del proyecto: 8 + 4.5*x
OD_REF = 0.49                     # referencia declarada en 9c86d76
DS = (2.0, 2.5, 3.3, 4.5)         # OrbitCamera INITIAL_DISTANCE = 3.3


def ray_sphere(ro, rd, r):
    b = sum(ro[i] * rd[i] for i in range(3))
    c = sum(x * x for x in ro) - r * r
    h = b * b - c
    if h < 0.0:
        return -1.0
    return -b - math.sqrt(h)


def far_sphere(ro, rd, r):
    b = sum(ro[i] * rd[i] for i in range(3))
    c = sum(x * x for x in ro) - r * r
    h = b * b - c
    if h < 0.0:
        return -1.0
    return -b + math.sqrt(h)


def od_final(D, b, usteps):
    """odR + odM acumulado al final del rayo con parametro de impacto b."""
    ro = (0.0, 0.0, D)
    if b > D:
        return None
    theta = math.asin(b / D)
    rd = (-math.sin(theta), 0.0, -math.cos(theta))
    t0 = ray_sphere(ro, rd, ATM_R)
    if t0 < 0.0:
        return None
    t1 = ray_sphere(ro, rd, PLANET_R)
    if t1 < 0.0:
        t1 = far_sphere(ro, rd, ATM_R)
    seg = t1 - t0
    if seg <= 0.0:
        return None
    dt = seg / usteps
    od = 0.0
    for i in range(usteps):
        t = t0 + dt * (i + 0.5)
        p = [ro[j] + rd[j] * t for j in range(3)]
        h = max(math.sqrt(sum(x * x for x in p)) - PLANET_R, 0.0)
        od += (math.exp(-h / H_R) + math.exp(-h / H_M)) * dt
    return od


print("ORACULO 0423 — alcance de bandas del mapa implementado del R4.6.7")
print("Formula declarada (9c86d76): logNe = 8.0 + 4.5 * (odIso / 0.49f)")
print("Constantes: PLANET_R=1.0 ATM_R=1.0255 H_R=0.0085 H_M=0.012 "
      "(AtmoShaderConstants, blob 62f5f6c9)")
print("Barrido: D en {2.0, 2.5, 3.3, 4.5}, b en [0, 1.03] paso 0.001, "
      "uSteps 8/12/16 (STEPS_MIN/DEFAULT/MAX).")
print()

# [1] rango de odIso re-derivado
maxima = {}
for usteps in (8, 12, 16):
    best, where = 0.0, None
    for D in DS:
        b = 0.0
        while b <= 1.03 + 1e-9:
            v = od_final(D, b, usteps)
            if v is not None and v > best:
                best, where = v, (D, round(b, 3))
            b += 0.001
    maxima[usteps] = best
    print(f"[1] uSteps={usteps:2d}: max odIso = {best:.5f} "
          f"(D={where[0]}, b={where[1]})")
print()

# [2] pines en unidades normalizadas y odIso
print("[2] posicion de los pines bajo el mapa declarado:")
for band in BANDS:
    x = (band - LOGNE_LO) / LOGNE_SPAN
    od_need = OD_REF * x
    print(f"    banda {band}: x = {x:.5f}  ->  odIso necesario = {od_need:.5f}")
print()

# [3] entrada maxima y logNe maximo por calidad (sin clamp conocido)
print(f"[3] entrada maxima = max odIso / {OD_REF} y logNe maximo = "
      f"8 + 4.5 * entrada:")
for usteps in (8, 12, 16):
    ent = maxima[usteps] / OD_REF
    logne = LOGNE_LO + LOGNE_SPAN * ent
    print(f"    uSteps={usteps:2d}: entrada max = {ent:.5f} "
          f"(+{(ent - 1.0) * 100:.2f}% sobre 1.0)  logNe max = {logne:.4f}")
print(f"    tope del rango del proyecto (LayerProfile): logNe = "
      f"{LOGNE_LO + LOGNE_SPAN}")
print()

# [4] margen de la banda mas alta contra el maximo por calidad
top_need = OD_REF * (max(BANDS) - LOGNE_LO) / LOGNE_SPAN
print(f"[4] banda mas alta {max(BANDS)}: odIso necesario = {top_need:.5f}")
for usteps in (8, 12, 16):
    marg = maxima[usteps] - top_need
    print(f"    uSteps={usteps:2d}: margen = {marg:.5f} "
          f"({'ALCANZA' if marg > 0 else 'NO ALCANZA'})")
print()

# [5] referencia que cerraria la entrada en 1.0 exacto
print("[5] para entrada <= 1.0 estricta se necesita OD_REF >= max odIso:")
for usteps in (8, 12, 16):
    print(f"    uSteps={usteps:2d}: OD_REF >= {maxima[usteps]:.5f}")
print(f"    declarado: OD_REF = {OD_REF} -> sobrepaso de entrada "
      f"{(maxima[8] / OD_REF - 1.0) * 100:.2f}% en el rayo rasante extremo;")
print("    ningun pin vive por encima de 11.5, asi que el sobrepaso no toca")
print("    banda alguna: es forma (entrada fuera de [0,1] por <1%), no sustancia.")
