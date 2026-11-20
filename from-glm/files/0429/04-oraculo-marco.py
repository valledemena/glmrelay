#!/usr/bin/env python3
"""GLM — verificacion aritmetica independiente del mapeo de marco R4.6.3.

Oráculo independiente: reimplemento densityDir (marco motor), el muestreo del
shader (u, v, altNorm, texelFetch ip.x) y el indexado de sampleVolumeAt tal
como estan ESCRITOS en el codigo de f306730, y compruebo que:

 1. Para todo (lat, lon) de la rejilla geografica, el vector motor
    d = densityDir(lat, lon) produce en el shader exactamente
    u = (lon+180)/360 (mod 1) y v = (lat+90)/180.
 2. El texel coordinate del shader (u*w) coincide con el gx+0.5 de
    sampleVolumeAt para el mismo (lat, lon) — es decir, shader y JVM
    muestrean la misma celda.
 3. La rama chapman (floor(u*w)) cae en el lonIdx correcto para los
    centros de celda de la rejilla (w = lonIndex).
 4. altNorm del shader == (altKm - 60)/(500 - 60) lineal.
 5. Extremos N/S/E/W y radios: outerR = 1 + 500/6371.
"""
import math

PI = math.pi
W, H, LV = 72, 72, 48          # VOL_LON_RES, VOL_LAT_RES, VOL_ALT_RES
ALT_MIN, ALT_MAX = 60.0, 500.0  # VOL_ALT_MIN_KM, VOL_ALT_MAX_KM
PLANET_R = 6371.0

fails = []


def density_dir(lat_deg, lon_deg):
    """core/iono/DensityVolume.kt:67 (motor)."""
    phi = math.radians(90.0 - lat_deg)
    theta = PI - math.radians(lon_deg)
    sn = math.sin(phi)
    return (sn * math.cos(theta), math.cos(phi), sn * math.sin(theta))


def shader_uv(n):
    """VolumeShaderSource.VOLUME_FRAG L102-107."""
    x, y, z = n
    r = max(math.sqrt(x * x + y * y + z * z), 1e-6)
    lat = math.asin(max(-1.0, min(1.0, y / r)))
    phi = -math.atan2(z, x)  # atan(n.z, n.x)
    u = (phi / 6.28318530718) % 1.0  # fract()
    v = lat / 3.14159265 + 0.5
    return u, v


def sample_gx_gy(lat_deg, lon_deg):
    """core/iono/VolumeSamples.kt:84-85."""
    gx = (lon_deg + 180.0) / 360.0 * W - 0.5
    gy = (lat_deg + 90.0) / 180.0 * H - 0.5
    return gx, gy


# --- 1+2: barrido completo de la rejilla geografica (72x72 centros de celda) ---
worst_u = worst_v = worst_texel = 0.0
for lat_idx in range(H):
    lat = -90.0 + 180.0 * (lat_idx + 0.5) / H
    for lon_idx in range(W):
        lon = -180.0 + 360.0 * (lon_idx + 0.5) / W
        d = density_dir(lat, lon)
        u, v = shader_uv(d)
        # esperado geografico
        ue = ((lon + 180.0) / 360.0) % 1.0
        ve = (lat + 90.0) / 180.0
        du = min(abs(u - ue), abs(u - ue + 1.0), abs(u - ue - 1.0))  # mod 1
        dv = abs(v - ve)
        if du > 1e-9: fails.append(f"u mal en ({lat:.2f},{lon:.2f}): {u} vs {ue}")
        if dv > 1e-9: fails.append(f"v mal en ({lat:.2f},{lon:.2f}): {v} vs {ve}")
        worst_u, worst_v = max(worst_u, du), max(worst_v, dv)
        # texel coordinate del shader vs sampleVolumeAt
        tex_shader = u * W
        gx, gy = sample_gx_gy(lat, lon)
        d_tex = abs(tex_shader - (gx + 0.5))
        if d_tex > 1e-6: fails.append(f"texel desalineado en ({lat:.2f},{lon:.2f}): {tex_shader} vs {gx + 0.5}")
        worst_texel = max(worst_texel, d_tex)
print(f"[1] barrido {H}x{W}: max|u-ue| (mod 1) = {worst_u:.3e}, max|v-ve| = {worst_v:.3e}")
print(f"[2] texel shader (u*w) vs sampleVolumeAt (gx+0.5): max desvio = {worst_texel:.3e}")

# --- 3: rama chapman: floor(u*w) == lonIdx en centros de celda ---
bad_w = 0
for lon_idx in range(W):
    lon = -180.0 + 360.0 * (lon_idx + 0.5) / W
    d = density_dir(0.0, lon)
    u, _ = shader_uv(d)
    ipx = math.floor(u * W)
    if ipx != lon_idx: bad_w += 1; fails.append(f"chapman ip.x={ipx} != lonIdx={lon_idx} (lon={lon:.2f})")
print(f"[3] chapman floor(u*W) == lonIdx para los {W} centros: {W - bad_w}/{W} correctos")

# --- 4: altNorm del shader == lineal (alt-60)/(500-60) ---
inner = 1.0
outer = 1.0 + ALT_MAX / PLANET_R  # volumeOuterRadius(500)
worst_alt = 0.0
for i in range(0, LV * 4):
    alt = ALT_MIN + (ALT_MAX - ALT_MIN) * (i / (LV * 4 - 1))
    r = inner + (alt / PLANET_R)  # radio del punto a esa altitud (unidades motor)
    alt_norm_shader = max(0.0, min(1.0, (r - inner) / (outer - inner)))
    alt_norm_expected = (alt - ALT_MIN) / (ALT_MAX - ALT_MIN)
    worst_alt = max(worst_alt, abs(alt_norm_shader - alt_norm_expected))
if worst_alt > 1e-12: fails.append(f"altNorm no lineal: {worst_alt}")
print(f"[4] altNorm shader == (alt-60)/440 lineal en toda la columna: max desvio = {worst_alt:.3e}")

# --- 5: extremos y radios ---
outer_expected = 1 + 500.0 / 6371.0
print(f"[5] outerR = 1 + 500/6371 = {outer_expected:.6f} (mensaje declara 1.07851: {'OK' if abs(outer_expected - 1.07851) < 5e-5 else 'MAL'})")
checks = [
    ("N", (90.0, 0.0), (0.0, 1.0, 0.0)),
    ("S", (-90.0, 0.0), (0.0, -1.0, 0.0)),
]
for name, (lat, lon), expected_n in checks:
    d = density_dir(lat, lon)
    ok = all(abs(a - b) < 1e-12 for a, b in zip(d, expected_n))
    u, v = shader_uv(d)
    print(f"    extremo {name}: n={tuple(round(c, 6) for c in d)} v={v:.6f} {'OK' if ok else 'MAL'}")
    if not ok: fails.append(f"extremo {name} mal")
    if name == "N" and abs(v - 1.0) > 1e-9: fails.append("N no da v=1")
    if name == "S" and abs(v - 0.0) > 1e-9: fails.append("S no da v=0")
for lon, u_expected, tag in [(-180.0, 0.0, "lon -180 -> u=0"), (0.0, 0.5, "lon 0 -> u=0.5"),
                             (90.0, 0.75, "lon +90 -> u=0.75"), (-90.0, 0.25, "lon -90 -> u=0.25"),
                             (180.0, 0.0, "lon +180 -> u=0 (misma meridiana que -180)")]:
    d = density_dir(0.0, lon)
    u, _ = shader_uv(d)
    ue = u_expected % 1.0
    du = min(abs(u - ue), abs(u - ue + 1), abs(u - ue - 1))
    print(f"    {tag}: u={u:.6f} {'OK' if du < 1e-12 else 'MAL'}")
    if du > 1e-12: fails.append(f"{tag} mal: {u}")

# --- veredicto ---
print()
if fails:
    print(f"VEREDICTO: {len(fails)} fallos")
    for f in fails[:10]: print(" -", f)
else:
    print("VEREDICTO: mapeo de marco del motor verificado — shader, sampleVolumeAt y rejilla oraculo son la misma geometria.")
