#!/usr/bin/env python3
# Ronda 0422 (GLM) — oraculo numerico del rango del proxy d en ATMO_FRAG (main 8611ee6).
# Replica el loop del raymarch del shader (AtmoShaderSource.ATMO_FRAG) con las
# constantes de AtmoShaderConstants para medir el rango real de:
#   (a) d por paso = dR + dM = (exp(-h/H_R) + exp(-h/H_M)) * dt   [lo que el 0434 declara]
#   (b) rho por punto = exp(-h/H_R) + exp(-h/H_M)                 [sin el factor dt]
#   (c) od acumulado = odR + odM a lo largo del rayo             [tercera variante]
# y a que altitudes caerian las bandas 10.5/11/11.5 bajo cada mapa.
import math

PLANET_R = 1.0
ATM_R = 1.0255
H_R = 0.0085
H_M = 0.012
BANDS = (10.5, 11.0, 11.5)


def ray_sphere(ro, rd, r):
    b = sum(ro[i] * rd[i] for i in range(3))
    c = sum(x * x for x in ro) - r * r
    h = b * b - c
    if h < 0.0:
        return -1.0
    return -b - math.sqrt(h)


def far_sphere(ro, rd, r):
    """Segunda interseccion (la del fragmento back-face del shell)."""
    b = sum(ro[i] * rd[i] for i in range(3))
    c = sum(x * x for x in ro) - r * r
    h = b * b - c
    if h < 0.0:
        return -1.0
    return -b + math.sqrt(h)


def march(D, b, usteps):
    """Un rayo con parametro de impacto b desde camara a distancia D. Devuelve
    (lista de (h, d_paso, rho_punto, od_acum) por paso, seg_len) o None."""
    ro = (0.0, 0.0, D)
    if b > D:
        return None
    theta = math.asin(b / D)
    rd = (-math.sin(theta), 0.0, -math.cos(theta))
    t0 = ray_sphere(ro, rd, ATM_R)
    if t0 < 0.0:
        return None
    t1 = ray_sphere(ro, rd, PLANET_R)  # entrada al planeta si lo golpea
    if t1 < 0.0:
        t1 = far_sphere(ro, rd, ATM_R)  # fragmento back-face: limite lejano
    seg = t1 - t0
    if seg <= 0.0:
        return None
    dt = seg / usteps
    steps = []
    od = 0.0
    for i in range(usteps):
        t = t0 + dt * (i + 0.5)
        p = [ro[j] + rd[j] * t for j in range(3)]
        h = max(math.sqrt(sum(x * x for x in p)) - PLANET_R, 0.0)
        dR = math.exp(-h / H_R) * dt
        dM = math.exp(-h / H_M) * dt
        od += dR + dM
        rho = math.exp(-h / H_R) + math.exp(-h / H_M)
        steps.append((h, dR + dM, rho, od))
    return steps, seg


def solve_band_altitudes(mapping):
    """Altitudes h donde mapping(h) cruza cada banda (biseccion)."""
    out = []
    for band in BANDS:
        lo, hi = 0.0, ATM_R - PLANET_R
        flo, fhi = mapping(lo), mapping(hi)
        if not (min(flo, fhi) <= band <= max(flo, fhi)):
            out.append(None)  # banda fuera del rango del mapa dentro de la atmosfera
            continue
        for _ in range(80):
            mid = (lo + hi) / 2.0
            fm = mapping(mid)
            if (flo - band) * (fm - band) <= 0:
                hi, fhi = mid, fm
            else:
                lo, flo = mid, fm
        out.append((lo + hi) / 2.0)
    return out


def main():
    print("ORACULO 04 — rango del proxy d en ATMO_FRAG (main 8611ee6) para Q19")
    print("Constantes: PLANET_R=1.0 ATM_R=1.0255 H_R=0.0085 H_M=0.012 "
          "(AtmoShaderConstants.kt, blob 62f5f6c9)")
    print("Camara: OrbitCamera INITIAL_DISTANCE=3.3; se barre D y el parametro de")
    print("impacto b (0..1.03) para cubrir disco y limbo. uSteps 8/12/16 = STEPS_MIN/DEFAULT/STEPS_MAX.")
    print()
    print("== [A] d por paso (lo implementado: d = dR + dM con dt) ==")
    for usteps in (8, 12, 16):
        glob_max = 0.0
        where = None
        for D in (2.0, 2.5, 3.3, 4.5):
            b = 0.0
            while b <= 1.03:
                r = march(D, b, usteps)
                if r:
                    for (h, d, rho, od) in r[0]:
                        if d > glob_max:
                            glob_max = d
                            where = (D, b, h)
                b += 0.001
        logne_max = 10.0 + 4.5 * glob_max
        print(f"  uSteps={usteps:2d}: max d por paso = {glob_max:.5f} "
              f"(D={where[0]}, b={where[1]:.3f}, h={where[2]:.5f})")
        print(f"            logNe = 10.0 + 4.5*d alcanza como maximo {logne_max:.3f}")
        for band in BANDS:
            d_req = (band - 10.0) / 4.5
            print(f"            banda {band}: requiere d = {d_req:.4f} -> "
                  f"{'ALCANZABLE' if d_req <= glob_max else 'FUERA DE RANGO'}")
    print()
    print("== [B] rho por punto (sin dt): exp(-h/H_R) + exp(-h/H_M) ==")
    rho_top = math.exp(-(ATM_R - PLANET_R) / H_R) + math.exp(-(ATM_R - PLANET_R) / H_M)
    print(f"  rho en h=0 (superficie): {2.0:.5f}")
    print(f"  rho en h={ATM_R - PLANET_R:.4f} (tope atmosferico, 162 km): {rho_top:.5f}")
    print(f"  rango real de rho dentro de la atmosfera: [{rho_top:.5f}, 2.0]")
    for band in BANDS:
        rho_req = (band - 10.0) / 4.5
        print(f"  banda {band}: requiere rho = {rho_req:.4f} -> "
              f"{'dentro' if rho_top <= rho_req <= 2.0 else 'FUERA (por encima del tope)'}")
    print()
    print("== [C] od acumulado (odR + odM) al final del rayo ==")
    for usteps in (8, 12, 16):
        glob_max = 0.0
        for D in (2.0, 2.5, 3.3, 4.5):
            b = 0.0
            while b <= 1.03:
                r = march(D, b, usteps)
                if r and r[0]:
                    glob_max = max(glob_max, r[0][-1][3])
                b += 0.001
        print(f"  uSteps={usteps:2d}: max od acumulado = {glob_max:.5f} -> "
              f"logNe max = {10.0 + 4.5 * glob_max:.3f}")
    print()
    print("== [D] la alternativa del 0434: log2(10.0 + 100.0 * d) ==")
    # con d por paso en [0, ~0.11]: log2(10+100d) en [3.32, 5.21]; con rho en [0.169,2]:
    print(f"  con d por paso (max ~0.1136 a 8 pasos): log2(10+100d) <= "
          f"{math.log2(10 + 100 * 0.1136):.3f}")
    print(f"  con rho por punto (max 2.0): log2(10+100*rho) <= {math.log2(10 + 100 * 2.0):.3f}")
    print("  Las bandas 10.5/11/11.5 quedan a distancias de orden 5-10 unidades:")
    for band in BANDS:
        print(f"    banda {band}: requiere 10+100x = 2^{band:.1f} = {2 ** band:.3e} -> "
              f"x = {(2 ** band - 10) / 100:.3e}")
    print("  -> base equivocada (logNe es log10) y rango inalcanzable: rechazada,")
    print("     como propuso el propio 0434; aqui con la medicion que lo cierra.")
    print()
    print("== [E] altitudes de banda bajo cada mapa (biseccion sobre h) ==")
    m_lin_d = lambda h: 10.0  # el mapa lineal sobre d por paso NO es funcion de h sola
    print("  (a) 10.0 + 4.5*d_paso: d depende de dt=segLen/uSteps (geometria+calidad);")
    print("      no es un campo: las bandas se mueven con la calidad y la geometria.")
    rho_map = lambda h: 10.0 + 4.5 * (math.exp(-h / H_R) + math.exp(-h / H_M))
    alts = solve_band_altitudes(rho_map)
    print("  (b) 10.0 + 4.5*rho(h) (sin dt, campo de altitud):")
    for band, h in zip(BANDS, alts):
        if h is None:
            print(f"      banda {band}: fuera del rango dentro de la atmosfera")
        else:
            print(f"      banda {band}: h = {h:.5f} ({h * 6371:.1f} km)")
    print()
    print("== [F] lectura para Q19 ==")
    print("  1. El 0434 declara 'd en [0,1] aprox'. Medido: d por paso <= 0.1136")
    print("     (uSteps=8, rayo rasante) y <= 0.0757 con los 12 pasos por defecto.")
    print("     La declaracion es falsa por un factor ~9-13x.")
    print("  2. Con el mapa implementado (10.0+4.5*d): a calidad por defecto NINGUNA")
    print("     banda es alcanzable (logNe max ~10.34); a 8 pasos solo la banda 10.5")
    print("     en el paso mas denso de un rayo rasante. Las bandas 11 y 11.5 no se")
    print("     alcanzan en ninguna calidad: la maquinaria iso seria codigo muerto.")
    print("  3. Ademas d lleva el factor dt: el umbral efectivo de cada banda se")
    print("     mueve con uSteps (calidad) y con la geometria del rayo — las bandas")
    print("     no serian superficies fijas sino artefactos de muestreo.")
    print("  4. Sin dt (rho por punto): las bandas 11 y 11.5 caen dentro del rango")
    print("     (cascarones de altitud) pero la 10.5 queda por encima del tope")
    print("     atmosferico. El mapa lineal 10+4.5*rho tampoco coloca las tres.")
    print("  5. ConCLUSION: el mapa debe re-escalarse (condiciones en el acta):")
    print("     entrada por punto sin dt, las tres bandas dentro del rango medido,")
    print("     y el mapa declarado como provisional a la espera de R4.6.3.")


if __name__ == "__main__":
    main()
