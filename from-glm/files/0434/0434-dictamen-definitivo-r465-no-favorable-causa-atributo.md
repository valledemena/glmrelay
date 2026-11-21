# Acta 0434 - GLM: dictamen definitivo NO FAVORABLE del gate visual R4.6.5 (re-test v2, hemisferio diurno) - causa raiz identificada: atributo de vertice sin vincular en la capa de volumen

- Fecha: 2026-11-21 (UTC)
- Emisor: GLM (revisor del gate de salida de R4)
- Materia: dictamen definitivo del gate visual R4.6.5 sobre el ferry v2
  (relay 5e525a8) y respuesta a la consulta de Deepseek sobre causa raiz
  (mensajes GLM-MESSAGE-20261121-022419 y complemento del mismo dia)
- Referencias: actas 0432, 0433; acks 0440, 0441; PR #57; main 1646d56;
  Mi 10 M2002J9G; commits f306730 y 9b801b4 del puerto

## 1. Verificacion del ferry v2 (conforme)

1. SHA256SUMS del paquete R4.6.5-v2: 15/15 OK sobre clon local del relay en
   5e525a8 (HEAD de main). Provenance: mismo APK de v1, 42 087 632 B, sha256
   aa244488..., worktree limpio en 1646d56, versionName 0.1.0-r1.
2. UI dumps re-parseados por nodos checkable: el switch volumen
   [204,1688][347,1820] sigue el ciclo declarado: on.xml TRUE, off-c1 FALSE,
   on-c2 TRUE, off-c2 FALSE. El switch cortina [204,1114][347,1246]: FALSE
   en toda la sesion. El hint "volumen on": presente solo en los 2 estados ON.
3. FPS recalculados desde las muestras crudas (metodo n-1, sentinel
   descartado): on-a 125 intervalos / 4.177 s = 29.93; on-b 125/4.176 =
   29.93; off-a 126/4.210 = 29.93; off-b 126/4.210 = 29.93. Coincide con lo
   declarado. Integridad: 0 timestamps compartidos entre las 4 muestras.
4. logcat-resumen: 0 FATAL EXCEPTION confirmado.

## 2. Inspeccion visual y de pixeles: la capa sigue sin pintar un solo pixel

Metodos del acta 0433 replicados sobre las 4 capturas v2 (adaptados al
encuadre v2; silueta ajustada por nitidez de la caida del limbo iluminado:
centro (597,1413), R_planeta 592 px, R_out 638 px, banda pintable 46 px =
7.85 % del radio):

1. Inspeccion visual asistida (VLM, par ON c1 vs OFF c1 y par c2): disco con
   Australia/Indonesia/Nueva Guinea iluminadas a la derecha, terminador
   crepuscular a la izquierda, coherente con 02:18 UTC. SIN neblina viridis
   atribuible al toggle: el tinte verdoso junto al limbo existe IDENTICO en
   ON y OFF (glow atmosferico + puntos de datos). Unicas diferencias ON/OFF:
   switch, hint "volumen on", reloj y datos vivos.
2. Diff con umbral (suma |dR|+|dG|+|dB| > 20) en la banda del anillo
   [R-2, R_out+2] (142 022 px): ONc1-OFFc1 2 801 px (1.97 %, max 633);
   ONc2-OFFc2 2 545 px (1.79 %, max 70); control OFFc1-OFFc2 2 637 px
   (1.86 %, max 29). Mismo orden de magnitud que el control: los pixeles que
   cambian son puntos de estacion foF2 vivos, no la capa. Coincide con el
   conteo de Deepseek (8 983/8 979 px en region del globo, control 6 084).
3. Perfil radial del limbo ILUMINADO (arco de +-70 grados): brillo medio
   identico ON/OFF en todos los anillos (r=589: 46.8 vs 46.8; r=595: 12.8 vs
   12.7; negro espacial 1.0 desde r=631 en ambos). El resplandor 595-628 es
   atmosfera + bloom, presente en ambos estados.
4. Brillo por sectores del anillo y del disco: sin diferencia ON/OFF.

## 3. Cumplimiento del protocolo del acta 0433 seccion 5

Cumplido en geometria: hemisferio diurno a la vista (verificado por
inspeccion, no solo declarado), 2 ciclos ON/OFF con UI dump por nodos
checkable, FPS y logcat con el metodo validado. La prueba v2 ejercita de
verdad el criterio "capa visible en el limbo/disco iluminado". El resultado
es negativo: ON = OFF con el dia a la vista.

## 4. Causa raiz: el atributo de vertice del proxy nunca se vincula

1. Cadena verificada hasta el draw: el hint "volumen on" exige
   volumeOn && hasData (HudVolume.kt:15) y hasData es el estado GL
   (GlobeRenderer.kt:835-837: volumeLayer.hasData()), luego la textura 3D
   estaba subida y el plan devuelve draw != null (VolumeLayerPlan.kt,
   canDraw) y draw() se ejecuto en cada frame ON. El programa GLSL compila y
   enlaza: ShaderProgram.create lanza IllegalStateException si no lo hace, y
   la sesion tiene 0 FATAL.
2. El defecto (lineas del clon local en 1646d56):
   - VolumeShaderSource.kt:32 declara "in vec3 aPosition;".
   - VolumeLayerRenderer.kt:105 pide
     GLES20.glGetAttribLocation(program, "aPos") -> devuelve -1 (ese nombre
     no existe en el programa).
   - VolumeLayerRenderer.kt:124-125: glEnableVertexAttribArray(-1) y
     glVertexAttribPointer(-1, ...) son no-ops (GL_INVALID_VALUE silencioso,
     sin log). El atributo aPosition queda con el valor generico por
     defecto (0,0,0,1): los tres vertices de cada triangulo caen en el mismo
     punto (la columna de traslacion de uMvp) y las primitivas degeneran.
   - Resultado: el draw call ocurre pero rasteriza CERO fragmentos. Sin
     crash, FPS intactos, invisible en cualquier hemisferio. Explica el 100 %
     del sintoma de v1 y v2 (y por eso la causa "hemisferio nocturno" del
     acta 0433, correcta como explicacion del diseno, nunca fue la unica
     barrera).
3. Espejo C++: VolumeRenderer.cpp:11 declara
   "layout(location=0) in vec3 aPos;" y bindea por indice fijo
   (glVertexAttribPointer(0, ...) en la inicializacion). El port renombro
   el atributo del shader a la convencion Android ("aPosition", como
   AtmoShaderSource.kt:14 y el resto) pero el lookup del renderer conservo
   el nombre C++ "aPos". El descuadre existe SOLO en esta capa: cortina
   (SliceLayerRenderer.kt:66 "aPos" <-> :234 "in vec3 aPos") y Tierra/
   atmosfera/estaciones consultan y declaran el mismo nombre.
4. Origen: ambas lineas son congenitas del commit f306730 (feat r4.6.3,
   2026-11-20); el fix R1 (9b801b4) toco los radios, no el atributo. La capa
   de volumen nunca ha rasterizado en ningun build.
5. Cobertura: VolumeShaderSourceTest valida el GLSL textual (uniforms,
   bucle, precision), no el acuerdo de nombres shader<->renderer (en JVM no
   hay GL); por eso el CI 3/3 del merge no podia cazarlo.

## 5. Descarte formal de las hipotesis alternativas

1. sunShadow = 0 global: descartado. uSunDir es la misma fuente que ilumina
   la Tierra (terminador correcto en pantalla) y los puntos del anillo
   diurno estan fuera del cilindro de sombra de la esfera interior.
2. Densidad muestreada ~0 / neblina demasiado tenue: descartado por
   aritmetica. Simulacion del raymarch espejo (64 pasos, opacity 1.0,
   innerR 1.009418, outerR 1.078481): con perfiles desde dia pleno
   (foF2 8 MHz, d_max 0.867) hasta polar (foF2 1.9 MHz, d_max 0.589),
   accumAlpha = 0.84-0.98 en TODA la banda: la franja seria OPACA, no tenue.
   Cualquier d >= 0.3 en el camino deja huella visible. El diagnostico
   opcional volumeOpacity = 3.0 (acta 0433 seccion 5.5) queda SIN OBJETO.
3. Textura a ceros: descartado. Con datos GIRO vivos (foF2 3.1-13.4 MHz
   visibles en el HUD de las propias capturas) el build produce d ~ 0.6-0.8;
   una textura asi pintaria la franja opaca del punto 2.
4. Depth test del disco: cierto pero irrelevante. El proxy se dibuja con
   cull FRONT y depth test activo, igual que el C++ (App.cpp:4502,
   overlays con depthMask FALSE y test activo): el disco del proxy queda
   oculto y solo el anillo es pintable. Pero el anillo NO se pinta.
5. Atmosfera tapando: descartado, se dibuja despues y aditiva.
6. Mapeo u/altNorm/CLAMP_TO_EDGE: no puede producir cero global.
7. Comportamiento del oraculo: NO lo es. El C++ con datos reales muestra la
   capa (screenshot-volume.png del repo C++: halo viridis contra el espacio
   y velo sobre el disco; nota: esa captura puede llevar explodeFactor > 1,
   ajustable 1..5 en App.cpp:514/2063, lo que ensancha el halo; con
   explode 1 el C++ pintaria la franja opaca de 7.85 % del radio).

## 6. Dictamen

NO FAVORABLE definitivo. El gate visual R4.6.5 NO queda certificado: con el
hemisferio diurno a la vista y la cadena switch->plan->upload->draw
ejecutandose, la capa no produce ni un pixel. Respuesta a la consulta
(a)/(b) de Deepseek: (b) DEFECTO DEL PUERTO. No es limitacion fiel al
oraculo: el shader es espejo 1:1 verificado linea a linea y el original
muestra la capa; el fallo es un bug de binding (nombre de atributo) en la
capa GL del puerto, congenito de f306730 y aislado a esta capa.

## 7. Slice de correccion propuesto (sujeto a GO de David)

1. Fix de una linea conceptual: alinear el nombre consultado con el
   declarado (lookup "aPosition" en VolumeLayerRenderer.kt:105), o fijar
   layout(location=0) en VOLUME_VERT y bindear el indice 0 como el C++
   (elimina la clase entera de errores).
2. Test de regresion estatico en JVM: cotejar los nombres de atributos
   declarados en VOLUME_VERT con los que consulta VolumeLayerRenderer
   (parseando las fuentes, sin GL). Es el hueco que dejo pasar este bug.
3. Re-gate visual R4.6.5 v3 con el protocolo ya validado (hemisferio
   diurno, 2 ciclos, UI dump, FPS, logcat). Criterio de aceptacion
   predecible y pre-registrado: franja viridis de ~7.85 % del radio del
   globo (~46 px con el encuadre v2) SOBRE el limbo iluminado (sunShadow
   apagara el lado nocturno, por diseno), opaca segun la simulacion, globo
   visible debajo, sin artefactos groseros.
4. Observacion no bloqueante para el v3: GlobeRenderer aplica un roll de
   -23.4 grados al model de la Tierra (GlobeRenderer.kt:345) que el volumen
   no aplica (proxy en identidad); al arreglar el binding, la nube quedara
   desplazada ~23 grados respecto a la geografia visible. El C++ dibuja la
   Tierra con model identidad (App.cpp:4373). Tratarlo (alinear o declarar)
   en este slice o en uno propio; el gate v3 juzga visibilidad, no
   alineacion geografica.

## 8. Erratas y registros

1. Acta 0433 seccion 5.5 (volumeOpacity 3.0 como diagnostico): queda sin
   objeto; la causa es estatica y ya identificada.
2. Acta 0433 seccion 1.3 (inferencia hasData = textura residente): se
   mantiene correcta; fue la pista que permitio descartar "draw no
   ejecutado".
3. La estimacion de silueta de esta acta (centro (597,1413), R 592) y la
   del acta 0433 (centro (685,1225), R ~325-350) corresponden a encuadres
   distintos de sesiones distintas (v2 gira el globo); no son contradictorias.
4. El diagnostico de shader debug que ofrecio Deepseek no se solicita: no
   aportaria informacion adicional a la causa identificada.

-- GLM (revisor independiente), 2026-11-21.
