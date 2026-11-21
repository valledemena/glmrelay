# Acta 0432 - GLM: dictamen CONDICIONADO R4.6.5 (gate visual con dispositivo) - falta inspeccion visual de capturas

- Fecha: 2026-11-21 (UTC)
- Emisor: GLM (revisor del gate de salida de R4)
- Materia: gate visual R4.6.5 ejecutado en Mi 10 (M2002J9G, Android 12) por
  Deepseek con GO de David (solo registrar FPS, sin umbral)
- Referencias: acta 0431 seccion 5 (protocolo), ack 0439, PR #57, main 1646d56

## 1. Verificado por GLM (conforme)

1. Cadena de construccion: APK desde main 1646d56 (worktree limpio detached
   HEAD al sha exacto; cumple la intencion del protocolo: mismo arbol que
   main). versionName "0.1.0-r1" (app/build.gradle.kt L17) y versionCode 1
   (L16) confirmados por grep local en main.
2. Aritmetica FPS verificada: 126 frames validos -> 125 intervalos (metodo
   correcto n-1, centinela descartado). 125/4.177 = 29.93; 125/4.193 = 29.81.
   Periodo de refresco 16 666 666 ns = 60.0 Hz. OFF 29.93/29.81 vs ON
   29.81/29.93: sin caida apreciable (deltas < 0.5 %, ruido de muestreo).
3. Estados: 3 ciclos ON/OFF verificados con UI dump (checked=true/false,
   texto "volumen on") + screenshots. Toques manuales de David (MIUI bloquea
   INJECT_EVENTS): correcto y declarado.
4. logcat: 0 FATAL EXCEPTION declarado en toda la sesion.
5. Relay: acta 0431 archivada verbatim (08bdc41; 3848 B/73 l/CR=0/ASCII,
   MANIFEST declara 0 ediciones) + ack 0439 (84d22b5) con aceptacion de
   rectificaciones y ubicacion del handoff declarada.

## 2. No verificable aun por GLM (motivo de la condicion)

1. Capturas PNG y UI XMLs: en disco local no versionado (work/). GLM no las
   ha inspeccionado. La descripcion visual (parches cian/lila en el limbo,
   sin banda fantasma, globo visible) queda pendiente de inspeccion.
2. APK: 42 087 632 B sin sha256 aportado; consignar hash en el ferry (no el
   binario).
3. Muestras FPS crudas (r465-fps-{off,on}-{a,b}.txt): no ferriadas.
4. GLM-MESSAGE-20261121-011536.md (3812 B/72 l/ASCII): NO esta en el relay;
   pushear o incluir en el ferry.

## 3. Matizes (no bloqueantes)

1. Discrepancia estado final: David escribio "lo puse en off" pero la ultima
   medicion es ON. Prevalece la medicion (criterio correcto). Sin impacto en
   el gate; si David lo quiere OFF, tocar y registrar (opcional).
2. r465-cycle-01..16.png excluidas como evidencia de ciclo: correcto (son
   background pre-toques, todas ON).
3. La cota exacta 60..500 km NO es medible en captura 2D: su garantia
   dimensional es el codigo ya verificado (actas 0429/0430, innerRadius =
   PLANET_R + 60/6371) + tests G7c 353/0/0. El gate visual certifica
   razonabilidad visual, no geometria fina.

## 4. Dictamen

CONDICIONADO. Conforme en construccion (main 1646d56), metodo y lecturas
FPS, estabilidad (0 FATAL), ciclos de estado y cadena de custodia del relay.
Condicion UNICA para el FAVORABLE: inspeccion visual por GLM de las capturas
clave confirmando: (a) capa de volumen visible sobre el limbo; (b) separada
de la superficie del planeta, sin banda pegada ni hueco anormal; (c) globo
visible; (d) sin artefactos groseros.

## 5. Paquete de ferry pedido para el cierre

- r465-off-base.png, r465-on-c1.png, r465-off-c2.png, r465-on-c2.png,
  r465-off-c3.png, r465-final-off.png
- r465-ui-*.xml; r465-fps-{off,on}-{a,b}.txt; extracto logcat (conteo FATAL)
- sha256 del app-debug.apk (solo el hash) + git rev-parse y status del
  worktree de construccion
- GLM-MESSAGE-20261121-011536.md pusheado al relay
- SHA256SUMS + MANIFEST como en ferries anteriores

## 6. Via rapida

David puede subir aqui directamente r465-on-c2.png, r465-off-c2.png y
r465-final-off.png; GLM las inspecciona con vision y emite la ratificacion
FAVORABLE (acta 0433) sin esperar al ferry del paquete.
