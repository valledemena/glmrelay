=====================================================================
ACTA 0436 | GLM, verificador independiente
Proyecto: valledemena/ionosphere-live-3d-android (puerto Android del
motor C++ original). Relay: valledemena/glmrelay.
Fecha: 2026-11-21, via David.
Materia: DICTAMEN VISUAL FINAL del re-gate v3 de R4.6.5 sobre el head
f3079d9 (PR #58), contra el ferry to-glm/files/R4.6.5-v3/ y el informe
to-glm/0443 de OpenCode (DeepSeek V4.1 Flash). Incluye una errata
propia (estimacion de FPS del acta 0435) y una discrepancia menor del
contrato del ferry, ambas declaradas en el cuerpo.
=====================================================================

1. ANTECEDENTES

- Acta 0434: NO FAVORABLE definitivo. Causa raiz: binding del atributo
  de vertice ("aPos" consultado vs "aPosition" declarado) -> malla
  degenerada -> cero fragmentos. Congenito de f306730.
- Acta 0435 (archivada por David en 5cc9550; integridad verificada en
  esta ronda: 11 604 B / 224 lineas / CR=0 / ASCII): fase de codigo
  CONFORME sobre f3079d9 (fix minimo + test estatico G7c_30 verificado
  por simulacion: PASS post-fix, FAIL pre-fix; barrido repo-wide sin
  otros descuadres; CI 3/3) y autorizacion de la prueba visual v3 con
  criterio binario pre-registrado.
- to-glm/0443 (85d856a): OpenCode ejecuta la v3 y declara PASS visual
  con cuantificacion propia; ferry 20 ficheros; FPS ON ~18.7 vs OFF
  ~27.7 declarado con transparencia; 0 FATAL.

2. METODO (PRIMERA MANO, LOCAL)

- Sandbox recuperado a las 15:39Z; clon fresco del relay @ 85d856a.
  Cadena verificada: 5cc9550 (acta 0435) -> af62e50 (ferry v3) ->
  85d856a (to-glm/0443).
- Ferry: sha256sum -c sobre los 20 ficheros; lectura de MANIFEST,
  provenance, logcat-resumen, fps/resumen y dumps crudos; UI dumps
  parseados.
- Inspeccion visual VLM de las 4 capturas (2 llamadas, ON vs OFF por
  ciclo).
- Analisis de pixeles INDEPENDIENTE con centro y radio detectados por
  mi (ajuste de circunferencia sobre la propia banda viridis), 4
  metodos. Script persistido (scripts/v3_pixel_glm.py).
- Recomputo FPS por el metodo n-1 sobre los 8 dumps crudos de
  SurfaceFlinger, con filtrado del centinela INT64_MAX (script
  persistido scripts/v3_fps_recompute.py).
- Paridad de coste verificada en clones C++ (master d9fb809) y Android
  (f3079d9).

3. FERRY v3: CONTRATO Y UNA DISCREPANCIA DECLARADA

- sha256sum -c: 19/20 OK directo. UNA discrepancia:
  analisis-pixeles.txt declara 1 242 B / sha256 f4605976... pero el
  blob del relay mide 1 220 B / sha256 59467b30...
- Causa identificada y verificada de forma determinista: el repo tiene
  .gitattributes y git normalizo CRLF -> LF al subir. Re-aplicando CRLF
  al blob del relay se obtienen EXACTAMENTE 1 242 B y el sha256
  declarado f4605976... El contenido es identico byte a byte salvo los
  finales de linea (22 lineas = 22 bytes de diferencia). El "20/20 OK"
  declarado por OpenCode era honesto contra sus ficheros locales
  (Windows, CRLF); el artefacto del relay quedo en LF.
- Valoracion: no es manipulacion ni corruption; es un artefacto de
  normalizacion. NO bloquea el gate. Recomendacion para ferries
  futuros: hashear los artefactos ya normalizados (o con core.autocrlf
  off) para que el hash declarado sea el del blob del relay.
- Provenance verificado: HEAD f3079d9, padre 1646d56, numstat 6/4 +
  73/0 (coincide con mi verificacion de codigo del acta 0435), APK
  42 087 632 B sha256 d3c97413... distinto del v2 aa244488 (cmp exit
  1, offset 10 198 534), versionName 0.1.0-r1, Mi 10 / 1140a489.
- logcat-resumen: 0 FATAL declarado sobre 18 864 lineas; sin crashes
  del proceso. El logcat completo no viaja en el ferry (solo el
  resumen), igual que en v1/v2: consistente con el formato establecido.

4. INSPECCION VLM (OJOS PROPIOS, 2 CICLOS)

- Ciclo 1 (on-c1 vs off-c1): banda verde-menta/viridis pegada al limbo,
  SOLO en ON; en OFF el limbo pasa del planeta al espacio negro sin
  banda; mas brillante en el limbo iluminado (derecha/abajo-derecha,
  Atlantico/Africa); fina y nitida (~25-45 px), no un halo ancho; sin
  corrupcion ni artefactos. Diferencias accesorias coherentes con datos
  vivos (relojes, frecuencias de ionosondas actualizandose).
- Ciclo 2 (on-c2 vs off-c2): mismas cinco confirmaciones (si banda en
  ON / no banda en OFF / limbo diurno brillante / franja fina / sin
  corrupcion).

5. ANALISIS DE PIXELES INDEPENDIENTE (4 METODOS)

Geometria propia: ajuste de circunferencia sobre los pixeles viridis de
on-c1 (80 034 px) -> centro (534.7, 1238.6), radio del anillo 524.2,
radio del planeta ~501.6 (vs declarado (539,1237) R=498: diferencia
~5 px, absorbida por usar mi propia geometria en todos los metodos).

- M1 (diff por pixel, umbral max-canal > 30, banda [1.00R, 1.10R],
  162 239 px): ON-OFF ciclo 1 = 75.91%, ciclo 2 = 74.17%; control
  OFF-OFF = 1.64%. SENAL/CONTROL: 46.2x y 45.2x. Muy por encima del
  umbral pre-registrado.
- M2 (perfil radial dG = G_on - G_off por sector): limbo diurno (este)
  pico +225.6 a +226.3 en r = 1.02-1.06; a r >= 1.10 todos los
  sectores vuelven a fondo (+1 a +8). La banda existe en los cuatro
  sectores con intensidades: este +226 (dia), oeste +166, sur +105,
  norte +95.
- M3 (conteo viridis propio, G>R+8 & G>B+8 & G>90): ON c1 79 533 px
  (49.0%) y ON c2 82 192 (50.7%) frente a OFF c1 0 px y OFF c2
  2 034 px (1.25%, deriva de datos vivos/HUD, dentro del control).
- M4 (bordes al 50% del pico, sector diurno): banda en r/R
  [1.010, 1.080], grosor 7.0% del radio, pico en 1.055R, fondo a
  1.12R (+4.8). Es la banda del cascaron 60..500 km pre-registrada
  (7.85% geometrico; el cruce al 50% recorta ligeros los bordes).

OBSERVACION (corrige una frase del informe de OpenCode, no es fallo):
el informe decia "el lado nocturno permanece apagado". Mi M2 muestra
que el limbo nocturno SI tiene banda, mas debil (+95 a +166 frente a
+226 del diurno). Esto es lo fisicamente correcto: sunShadow solo
anula las muestras dentro del cono de umbra tras el terminador; las
trayectorias tangenciales de alta altitud sobre el hemisferio nocturno
siguen iluminadas. El oraculo C++ muestra el mismo comportamiento (la
inspeccion VLM del screenshot-volume.png del acta 0435: "night-side
limb shows the shell too, but fainter"). El criterio pre-registrado
nunca exijio oscuridad nocturna: exijia la franja SOLO en ON, que se
cumple (M3: OFF = 0 px en ciclo 1).

6. FPS: RECOMPUTO, ERRATA PROPIA Y FALLO DE LA CLAUSULA

- Recomputo n-1 (centinela INT64_MAX filtrado; 3 de los 8 dumps lo
  contienen): on-a 18.76, on-b 18.76, on2-a 18.67, on2-b 18.75,
  off-a 27.71, off-b 27.73, off2-a 27.63, off2-b 27.92. Media ON
  18.74 / OFF 27.75; caida 9.01 fps (32.5%). COINCIDE con lo declarado
  por OpenCode a +-0.01 fps en las 8 muestras.
- ERRATA PROPIA (acta 0435 seccion 9): estime "FPS esperado ~30 ...
  despreciable". Era un error de apreciacion: generalize el coste del
  raster de la banda (~16% del area del disco) sin costear la
  intensidad aritmetica del raymarch (64 pasos x muestreo de textura
  3D + colormap + raySphere por paso, en highp). Ademas arrastre el
  falso basamento de v2 (29.93/29.93), que medía una capa que no
  dibujaba nada. La medicion real es 18.74 fps.
- Paridad de coste verificada: C++ VolumeRenderer.h:59 steps_ = 64
  (clamp 16..256); puerto GlobeRenderer.kt:192 VolumeQuality.HIGH =
  VOL_STEPS_REF = 64 por defecto. El coste ON es el coste FIEL del
  default del oraculo; la diferencia con el C++ es el hierro (GPU de
  escritorio frente a Adreno 650 a 1080x2400).
- La clausula de FAIL "caida de FPS fuera de lo esperado" NO se
  dispara: la caida es estable (muestras dobles consistentes), sin
  FATAL, sin ANR, sin crash, con explicacion mecanica y con la palanca
  de coste declarada del slice disponible (VolumeQuality LOW 16 /
  MEDIUM 32 / HIGH 64; DoD de R4.6.3: "uSteps es el unico parametro de
  coste"). Mi estimacion era la que estaba mal, no el puerto.

7. UI DUMPS

- on-c1 y on-c2: exactamente 1 nodo checkable="true" checked="true"
  (View adyacente a la etiqueta "volumen", bounds vecinos) y hint
  "volumen on" presente.
- off-c1 y off-c2: 0 nodos checked, sin hint.
- Consistente con 2 ciclos completos y estado final OFF declarado.

8. DICTAMEN VISUAL FINAL: FAVORABLE

Sobre f3079d9, contra el criterio binario pre-registrado en el acta
0434 seccion 7 (reiterado en 0435 seccion 9):

- PASS en ambos ciclos con margen enorme: franja viridis en la banda
  pintable SOLO en ON (senal/control 46.2x y 45.2x por mi M1; OFF = 0
  pixeles viridis en el ciclo 1), banda donde el raymarch puede pintar
  ([1.010, 1.080]R medido, cascaron 7.85% pre-registrado), limbo
  diurno mas brillante, confirmado por VLM y por analisis de pixeles
  independiente con geometria propia.
- Cláusulas de FAIL: ninguna disparada. ON != OFF fuera de todo ruido;
  0 FATAL; sin crash ni ANR; la caida de FPS es real (32.5%) pero
  estable, explicada, fiel al coste del oraculo y con palanca de
  mitigacion existente (seccion 6).
- La correccion funciona exactamente como se predijo: la banda
  desaparecia por completo (atributo sin vincular) y ahora aparece
  confinada a la banda geometrica correcta.

RECOMENDACION A DAVID: GO de merge del PR #58 (head f3079d9). El
dictamen de codigo (0435) y el visual (esta acta) son favorables.

9. RECOMENDACIONES POST-MERGE (NO BLOQUEANTES)

a) Documentar el coste ON medido (~18.7 fps en Mi 10 con quality HIGH
   = 64 pasos) en la documentacion del slice o del DoD.
b) Valorar exponer el selector VolumeQuality (LOW/MEDIUM/HIGH) en la
   UI, o fijar MEDIUM por defecto, si 18.7 fps se considera pobre UX.
   Decision de producto de David; no es defecto de puerto.
c) Corregir en la documentacion la frase "lado nocturno apagado": la
   banda nocturna es mas debil pero visible (espejo del oraculo).
d) El roll de -23.4 grados de la Tierra frente al volumen sigue
   declarado como divergencia pendiente (fiel al C++, pero desplaza
   la nube ~23 grados respecto a la geografia mostrada).
e) Para ferries futuros: hashear los ficheros ya normalizados por git
   para evitar discrepancias EOL como la de analisis-pixeles.txt.

10. NOTAS DE ARCHIVO (PARA DAVID)

- Esta acta toma el numero from-glm/0436 (verificado libre). Siguiente
  to-glm libre: 0444.
- Tras el merge con tu GO, esperare el informe post-merge (merge
  commit, CI de main) para el acuse de cierre de R4.6.5, como en
  PR #57.
- Scripts de esta ronda persistidos en scripts/ del entorno de GLM:
  v3_pixel_glm.py (4 metodos) y v3_fps_recompute.py (n-1).

Firma: GLM (verificador independiente), 2026-11-21, via David.
