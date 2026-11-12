# PLAN R5 — GATE DEEP EXPLÍCITO — 2026-11-12 (rev. 2, enmienda GLM)

**Estado:** propuesta de plan. No ejecutado. No se ha creado ningún v6, no se
ha tocado `R4_DISPLAY_CHECK_v5.py`, no se ha modificado `main` ni la evidencia.

**Autor:** DeepSeek/Buffy (custodio INTERCAMBIO)  
**Revisión:** rev. 2 tras auditoría GLM (relay 334).  
**Contexto:** R4 cerrado en `e23b47e`; R5 es la siguiente fase.  
**Decisión de David:** preparar solo el plan, sin abrir todavía el slice.

---

## 1. Resumen ejecutivo

La propuesta inicial colocaba el gate DEEP en E2. La auditoría GLM la
enmienda con razón: **E2 solo corre en el selector E**, mientras que W11 corre
en **C/D/P/E**. Poner DEEP en E2 dejaría al selector P sin gatear la banda
DEEP, y P es precisamente el slice que movió la banda (highp: 0.23 → 0.26).

Diseño corregido:

- **W11** gatea THIN **y** DEEP:
  - THIN: `min(android) >= 3`, `min(web) >= 3`, `max|Δ_THIN| <= 2.0`.
  - DEEP: `max|Δ_DEEP| <= 2.0` en los 10 sectores.
- **E2** se queda como está: geometría + THIN absoluto `>= 3`; DEEP no se
  duplica allí.
- **Tolerancia fija en el instrumento** (`PARITY_TOL = 2.0`), no leída del
  `comp`.
- **DEEP absoluto no se gatea**: se reporta `min_android_deep` /
  `min_web_deep`.
- **Total sin cambios**: W11 sigue siendo un check; C=40, D=46, P=48, E=50.

## 2. Estado actual (verificado en el v5 original)

### 2.1 E2

`R4_DISPLAY_CHECK_v5.py`, bloque E:

- Lee `work/halo-<head7>.json`.
- Exige `capture={w:610,h:620,dpr:1}`, `n_angles=720`, `sector_deg=15`,
  `THIN=[258,278]`, `DEEP=[262,287]`, `illuminated_limb=[75,225]`.
- Gatea `delta_B_min_illuminated >= 3` (THIN).
- **No gatea DEEP**; solo lo archiva.

### 2.2 W11

- Lee `work/comp-<head7>.json`.
- Exige las mismas bandas/geometría en Android y web.
- Gatea THIN: `min(android) >= 3`, `min(web) >= 3`,
  `max|Δ_THIN| <= parity_tol`.
- **No gatea DEEP**, aunque el `comp` ya contiene
  `delta_B_deep_by_sector` en ambas plataformas.
- Hoy lee `tol = j.get("parity_tol", 2.0)`; el v6 debe **fijar** la tolerancia
  en el instrumento, no confiar en el JSON.

### 2.3 Cobertura por selector

W11 corre para C/D/P/E (índice ≥ 2). E2 solo para E. Por eso el gate DEEP
debe vivir en W11: así P —y cualquier slice que mueva la banda— queda
cubierto.

## 3. Criterio propuesto

| Elemento | Decisión |
|---|---|
| THIN absoluto | Sin cambio: `min_illuminated >= 3` |
| THIN paridad | Sin cambio: W11 `max|Δ_THIN| <= 2.0` |
| DEEP absoluto | **No gatear**; reportar mínimos Android/web |
| DEEP paridad | **Gate en W11:** `max|Δ_DEEP| <= 2.0` en 10 sectores |
| `passes_deep` | Ignorar; recalcular desde las series |
| Tolerancia | Constante `PARITY_TOL = 2.0` en el instrumento |
| Denominador | Sin cambio: C=40, D=46, P=48, E=50 |

## 4. Evidencia actual

### 4.1 E @ `24595b1` / merge `e23b47e`

DEEP Android:

```text
[13.97, 18.05, 21.19, 22.19, 21.31, 18.88, 13.55, 7.57, 2.89, 0.26]
```

DEEP web:

```text
[13.66, 17.70, 20.92, 21.57, 20.68, 18.37, 13.00, 7.26, 2.85, 0.32]
```

Diferencias absolutas:

```text
[0.31, 0.35, 0.27, 0.62, 0.63, 0.51, 0.55, 0.31, 0.04, 0.06]
```

`max|Δ_DEEP| = 0.63`; `min_android_deep = 0.26`; `min_web_deep = 0.32`;
THIN mínimo = 5.03.

### 4.2 Histórico

Los `comp` con DEEP completo dan paridad **0.63–0.64** en todos los cortes
válidos. El anexo C/D se apoya en:

- C @ `53a6df7`: DEEP 0.64.
- D @ `1ec6f36`: DEEP 0.64.
- P @ `a483f48`: DEEP 0.63.
- E @ `24595b1`: DEEP 0.63.

El mínimo absoluto DEEP de 0.26 en el sector 210–225° es geométricamente
esperado; un umbral absoluto tipo 3 sería un falso negativo. La paridad sí
detecta una regresión real.

## 5. Diseño del cambio v6

### 5.1 Fichero y linaje

- Crear `docs/r4/tools/R4_DISPLAY_CHECK_v6.py` (precedente:
  `docs/r4/tools/w11-metric.py`).
- Derivarlo **del v5 original**:
  `R4_DISPLAY_CHECK_v5.py`, sha256
  `ba4332979840d2893bd28e694ca5c8f03e39cc81ad8c149bcd1e6212daa89f00`.
- **No** derivarlo de la reconstrucción `2f14ae8b…`: difiere en el bloque P0
  (más laxo) y no es base canónica.
- Mantener el v5 intacto.

### 5.2 Cambio en W11

En el bloque W11, tras validar THIN, añadir:

```python
PARITY_TOL = 2.0  # fijada en el instrumento

da = caps["android"].get("delta_B_deep_by_sector") or []
dw = caps["web"].get("delta_B_deep_by_sector") or []
deep_ok = False
deep_det = "DEEP ausente"
if len(da) == len(dw) == 10:
    dd = [abs(x - y) for x, y in zip(da, dw)]
    deep_ok = max(dd) <= PARITY_TOL
    deep_det = (f"DEEP parity {max(dd):.2f} <= {PARITY_TOL}; "
                f"min and/web {min(da):.2f}/{min(dw):.2f}")

cp_ok = (min(a) >= 3 and min(w) >= 3
         and max(diffs) <= PARITY_TOL and deep_ok)
cp_det = (f"THIN min and={min(a):.2f}/web={min(w):.2f}; "
          f"max|diff|={max(diffs):.2f} <= {PARITY_TOL}; {deep_det}")
```

Reglas:

- Si `comp` no tiene DEEP Android/web, W11 **falla cerrado**.
- Si `comp.parity_tol` existe y no es 2.0, **falla cerrado** (no se confía en
  el JSON).
- No se lee `passes_deep`; se recalcula.
- E2 no cambia.

### 5.3 Qué NO se toca

- E2: THIN absoluto y geometría, sin DEEP.
- E1/E3, S1–S10, A, B, C, W1–W10, K, P1: sin cambios.
- `w11-metric.py`: sin cambios (sha256 `b3794c49…`).
- `app/src/main`: 0 rutas.
- No se re-captura en dispositivo; los `comp` existentes ya tienen DEEP.

## 6. Regresión

El v6 debe reproducir estos seis resultados, con el detalle nuevo solo en W11:

| Ref | Selector | v5 | v6 esperado | DEEP |
|---|---|---|---|---|
| `24595b1` | E | 50/50 | **50/50** | 0.63 |
| `e23b47e` | E | 48/50 | **48/50** | 0.63 |
| `a483f48` | P | 48/48 | **48/48** | 0.63 |
| `e23b47e` | P | 44/48 | **44/48** | 0.63 |
| `53a6df7` | C | 40/40 | **40/40** | 0.64 |
| `1ec6f36` | D | 46/46 | **46/46** | 0.64 |

Criterio:

- Las líneas de todos los checks distintos de W11 deben ser idénticas.
- W11 debe seguir PASS en los seis cortes.
- Cualquier cambio de total es un fallo del v6.
- `eec186a` (E2 1.74) puede añadirse como falsación si su evidencia está
  disponible; no es obligatorio para el 6/6.

## 7. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| DEEP fuera de P | Gate en W11, que corre C/D/P/E |
| `comp` sin DEEP web | W11 falla cerrado |
| `passes_deep` heredado | Ignorarlo; recalcular |
| Tolerancia leída del JSON | Constante `PARITY_TOL=2.0`; rechazar si difiere |
| DEEP absoluto 0.26 | No gatear absoluto; solo paridad |
| Deriva del instrumento | v6 separado; v5 intacto |
| Copia laxa de P0 | Derivar del original `ba433297…` |
| Cambio de denominador | W11 sigue siendo un check |
| Referencia web distinta | Exigir el mismo `comp`/`reference_sha256` |

## 8. Pasos de ejecución (cuando David abra R5)

1. Congelar el v5 original y registrar su sha256.
2. Crear v6 por copia; cambiar solo versión/docstring y W11.
3. Fijar `PARITY_TOL=2.0`; añadir DEEP parity y fallo cerrado.
4. Ejecutar la regresión 6/6 y diff de salidas contra v5.
5. Verificar `app/src/main` = 0 rutas y medidor intacto.
6. Actualizar documentación R5 y registro de decisiones.
7. Empaquetar evidencia con `SHA256SUMS` nativo.
8. PR docs/tooling, CI 3/3, auditoría GLM y dictamen.
9. Solo después, decidir si se re-mide en dispositivo (no necesario).

## 9. Criterios de aceptación

- [ ] v6 deriva del v5 original `ba433297…`; v5 no se modifica.
- [ ] W11 exige THIN `>= 3` y DEEP paridad `<= 2.0`.
- [ ] E2 sigue solo con THIN absoluto.
- [ ] Tolerancia fija en el instrumento, no leída del comp.
- [ ] Totales C/D/P/E sin cambio (40/46/48/50).
- [ ] Regresión 6/6 exacta (salvo detalle W11).
- [ ] `app/src/main` = 0 rutas; medidor `b3794c49…` intacto.
- [ ] DEEP Android y web presentes; fallo cerrado si falta.
- [ ] Paquete con `SHA256SUMS` y CI del SHA exacto.

## 10. No objetivos

- No tocar el render ni el pase de atmósfera.
- No introducir umbral absoluto DEEP.
- No cambiar THIN ni la tolerancia 2.0.
- No duplicar DEEP en E2.
- No re-capturar en dispositivo salvo evidencia faltante.
- No fusionar ni abrir PR en esta fase de plan.

## 11. Decisiones pendientes de David

1. Confirmar **W11** como ubicación del gate DEEP (enmienda GLM).
2. Confirmar **DEEP paridad 2.0** con tolerancia fija.
3. Confirmar **regresión 4/4 + anexo C/D**.
4. Confirmar path `docs/r4/tools/R4_DISPLAY_CHECK_v6.py`.
5. Autorizar el depósito del plan y, después, la apertura de R5.

---

**Conclusión:** el gate DEEP es pequeño, pero debe vivir en W11 para cubrir P y
cualquier slice que mueva la banda. El plan lo aísla en un v6 derivado del
original, con tolerancia fija, fallo cerrado y regresión 6/6. La decisión de
abrir R5 sigue siendo de David.
