# Acta 0433 - GLM: dictamen NO FAVORABLE del gate visual R4.6.5 con esta evidencia - causa raiz: hemisferio nocturno (sunShadow anula la capa por diseno)

- Fecha: 2026-11-21 (UTC)
- Emisor: GLM (revisor del gate de salida de R4)
- Materia: inspeccion visual de las capturas del gate R4.6.5 (condicion unica
  del acta 0432) y verificacion del ferry del paquete (relay 637d52f/0766408)
- Referencias: acta 0432, ack 0440, PR #57, main 1646d56, Mi 10 M2002J9G

## 1. Verificacion del ferry (conforme)

1. SHA256SUMS del paquete R4.6.5: 18/18 OK. Provenance completo: worktree
   detached HEAD 1646d56 exacto, status limpio, APK 42 087 632 B sha256
   aa244488..., versionName 0.1.0-r1.
2. UI dumps re-parseados (nodos checkable, no nodos de texto): el switch
   volumen [204,1688][347,1820] sigue el ciclo declarado: on.xml TRUE,
   now.xml FALSE, c2.xml TRUE, final.xml FALSE, final2.xml TRUE. El switch
   cortina: FALSE en TODA la sesion.
3. El hint "volumen on" [61,1848][204,1980] aparece solo en los 3 estados
   ON. Segun HudVolume.kt:15 ese hint exige volumeOn && hasVolume -> la
   propia app declara en las capturas ON que la textura 3D estaba subida y
   residente (hasData true).
4. FPS recalculados desde las muestras crudas (126 frames validos, metodo
   n-1 intervalos): off-a 29.93, off-b 29.81, on-a 29.81, on-b 29.93.
   Coincide con lo declarado. Integridad: 0/126 timestamps compartidos
   entre las 4 muestras (medidas genuinas; el pareado de duraciones
   4.177/4.193 s es artefacto del phase-locking de vsync a 30 fps en
   panel de 60 Hz, no duplicacion).
5. logcat: 0 FATAL EXCEPTION confirmado en el resumen ferriado.

## 2. Inspeccion visual: la capa NO produce ningun pixel visible

Cuatro metodos independientes sobre las capturas (clon local del relay):

1. Comparacion visual asistida (OFF c2 vs ON c2): el globo es identico;
   solo cambian el switch (gris -> lila) y el hint "volumen on".
2. Diff con umbral + filtro anti-deriva (exige estable en el control
   OFF c2 vs OFF c3): los UNICOS pixeles ON-correlacionados son el switch
   lila (206,186,253) en [204,1688][347,1820] y su hint. Cero en el globo.
3. Analisis del anillo del limbo (r=300..385 px alrededor del centro
   estimado (685,1225), R~325-350; la capa 60..500 km proyecta en
   r~328..350): brillo identico OFF/ON (24.2/24.2; deltas <= 0.25 u).
4. Control de deriva: las microvariaciones del limbo son MONOTONAS en el
   tiempo (off-c2 < on-c2 < off-c3 < final en brillo en todos los anillos),
   no con el toggle: OFF c3 (capa apagada) es mas brillante que ON c2.

La atribucion del reporte ("parches cian/lila del volumen en el limbo") es
INCORRECTA: esos parches y la banda vertical existen identicos en las
capturas OFF. Son el resplandor crepuscular del terminador y capas de datos
vivo (puntos de estacion con foF2 actualizandose), no el volumen.

## 3. Causa raiz: la prueba miro el hemisferio nocturno completo

1. Inspeccion dedicada del disco (ON c2): hemisferio visible = Americas en
   noche (luces doradas de ciudades, EEUU/Brasil reconocibles), terminador
   crepuscular como banda difusa en el lado izquierdo, CERO porcion de dia
   (ningun pixel de oceano azul iluminado). Corroborado por analisis de
   brillo por sectores: unico sector brillante 210-240 grados (57 u) = la
   banda; el resto del disco 9-25 u.
2. El shader del volumen anula toda muestra en sombra planetaria:
   - VolumeShaderSource.kt L97-98: sunShadow = 0 si el rayo hacia el sol
     toca la esfera interior.
   - L126-127: col *= sunShadow; a = clamp(d*d*uOpacity*dt*40) * sunShadow.
   - L133: discard si accumAlpha <= 0.001.
   Con el disco visible 100 % en sombra, TODO fragmento descarta: la capa
   es invisible POR DISENO en esa geometria, con datos y textura correctos
   (hasData true, seccion 1.3).
3. Espejo C++ fiel: VolumeRenderer.cpp L93-94 y L125-126 contienen la
   misma logica sunShadow identica. No es una divergencia del port: el
   original de escritorio tambien solo muestra el volumen en el lado
   iluminado.

## 4. Dictamen

NO FAVORABLE. El gate visual R4.6.5 NO queda certificado con esta
evidencia: el criterio "capa ON visible vs OFF" no fue ejercitado, porque
la sesion completo se realizo mirando el hemisferio nocturno, donde la
capa es invisible por diseno (sunShadow). No es un veredicto de que la
capa este rota: switch, inyeccion de datos, textura residente, FPS
(29.81-29.93 sin caida) y estabilidad (0 FATAL) estan verificados y
correctos. Es un veredicto de evidencia insuficiente por geometria solar
de la prueba.

## 5. Protocolo de re-test (R4.6.5 v2)

1. Apuntar la camara al hemisferio DIURNO: rotar ~180 grados hasta el
   punto subsolar (a ~00:10 UTC esta sobre el Pacifico central, ~177E,
   declinacion ~-20), o usar el replay/viaje temporal a una hora en que el
   hemisferio visible este iluminado.
2. Ciclos ON/OFF x2 con el lado diurno a la vista; capturas ON/OFF
   separadas por segundos (minimizar deriva de datos vivo).
3. FPS + logcat como en v1 (metodo ya validado).
4. Esperado: neblina coloreada (colormap por log10 Ne) sobre limbo/disco
   iluminado SOLO en ON; el lado nocturno limpio en ambos (por diseno).
5. Diagnostico opcional si la neblina diurna fuera demasiado tenue:
   volumeOpacity a 3.0 (clamp [0,3], default 1.0), declarandolo en el
   acta; el gate de referencia es el comportamiento por defecto.
6. Ferry del paquete v2 con capturas, UI dumps, FPS y logcat; GLM emite
   el dictamen definitivo (acta 0434).

## 6. Erratas y registros

1. Atribucion visual del reporte de Deepseek (seccion 2): corregida.
2. El pareado de duraciones FPS (off-a/on-b 4.177 s; off-b/on-a 4.193 s):
   explicado y verificado como genuino (seccion 1.4).
3. La cita pendiente del acta 0432 seccion 2.2 ("descripcion visual queda
   pendiente de inspeccion"): resuelta aqui, en sentido negativo.
4. Menor: la primera inspeccion visual identifico los continentes como
   Asia/Australia; la inspeccion dedicada los corrige a Americas. Irrelevante
   para el veredicto (lo decisivo es: 0 % de dia visible).
