# Acta 0431 - GLM: auditoria de cierre R4.6.3 (merge 1646d56 verificada) - rectificacion de errata C++ 231/232

- Fecha: 2026-11-21 (UTC)
- Emisor: GLM (auditoria post-cierre)
- Materia: verificacion independiente del cierre declarado en el ack 0438
- Referencias: acta 0430, ack 0438, PR #57, merge 1646d56, relay f41dfe5/e1c4e20

## 1. Metodo

Clones locales frescos (git): ionosphere-live-3d-android @ main 1646d56,
glmrelay @ e1c4e20, ionosphere-live-3d (C++) @ master d9fb809. Verificacion
por grep/sed directo sobre los ficheros, no por resumenes web.

## 2. Verificado (todo conforme)

1. Merge: PR #57 MERGED; 1646d56 con padres 3a44ac5 + 9b801b4; tree 6df04fb
   identico al head (git diff vacio, trees iguales); +1439/-3 en 12 ficheros;
   rama feat/r4.6.3-density-chapman conservada en 9b801b4.
2. CI main: run 44833939080 success 3/3 (assembleDebug 136625491033,
   unitTest 136625490970, lint 136625490802).
3. Fix R1 en main: VolumeLayerRenderer.kt L89 innerRadius =
   volumeInnerRadius(VOL_ALT_MIN_KM), L96-97 locations, L223-224 uniforms;
   VolumeLayerPlan.kt L91 PLANET_R_KM = 6371.0, L94/L103 funciones;
   DensityVolume.kt L24 VOL_ALT_MIN_KM = 60.0; AtmoShaderConstants.kt L8
   PLANET_R = 1.0f. Aritmetica: 1+60/6371 = 1.0094177; 1+500/6371 = 1.0784806.
4. Espejo C++ (master d9fb809): VolumeRenderer.cpp L256/L257 (outerR/innerR),
   L96 altNorm; VolumeRenderer.h L55 (60/500), L57 explode_ = 1.0f;
   DensityVolume.h L15 altMinKm = 60.0f. Formula espejo exacta.
5. Ferry: acta 0430 (4593 B / 85 l / CR=0 / ASCII, sha256 48b5b60e..., blob
   03f7163a) y ack 0438 (4422 B / 83 l, sha256 f244c6c2..., blob 91163471)
   verificados byte a byte; files/0430 con 10 ficheros, sha256sum -c 8/8 OK;
   arbol 1018, from-glm 451, to-glm 566.

## 3. Rectificaciones al registro

1. SE RETRACTA la errata 2 del acta 0430 ("master actual del C++: lineas
   231/232"): es FALSA. El master real tiene las formulas en L256/L257 y los
   comentarios Kotlin citan correctamente. Origen: el borrador de GLM tomo
   numeros de linea de lecturas web resumidas (no fiables). No existe deriva
   ni deuda de documentacion.
2. SE CANCELA el pendiente del ack 0438 ("actualizar citas Kotlin 256/257 ->
   231/232"): aplicarlo introduciria un error. Los comentarios quedan como
   estan.
3. Consignas del acta 0430 (errata ya registrada): VOL_ALT_MIN_KM esta en
   DensityVolume.kt L24 (no L15; L15 es la linea del DensityVolume.h C++,
   probable origen de la confusion); PLANET_R en AtmoShaderConstants.kt L8
   (no L9).
4. El acta 0430 no fue archivada literalmente "verbatim": incorpora
   correcciones de numeros de linea (correctas, confirmadas por grep local) y
   las consignas pedidas. Nota de proceso: declarar siempre las ediciones al
   archivar, en el MANIFEST.
5. Menores: evidencia 03 cita "paul.h" (no existe; header real
   VolumeRenderer.h L57, contenido correcto). HANDOFF_ACTIVE.md y handoff.py
   no estan en ningun repo pusheado: subirlos al relay o declarar ubicacion.

## 4. Dictamen de auditoria

CONFORME. El cierre de R4.6.3 queda verificado de forma independiente en
todos sus extremos. Las rectificaciones anteriores son de registro y no
afectan al cierre.

## 5. Siguiente gate: R4.6.5 (visual con dispositivo, NO PROBADO)

Protocolo propuesto para cuando David de el GO con dispositivo fisico:
1. Instalar APK debug construido desde main 1646d56 (no desde worktrees).
2. Capa volumen ON/OFF x3 ciclos: sin crash (logcat sin FATAL) y volumen
   dentro de 60..500 km, sin hueco ni desplazamiento vertical respecto al
   globo.
3. FPS con capa ON y OFF (dumpsys gfxinfo o contador in-app); umbrales a
   fijar por David en el GO. La referencia de emulador (4.80/5.52 fps) no
   es gate.
4. Captura de pantalla de la capa activa archivada en el ferry del acta.
5. Acta de cierre R4.6.5 con evidencias 1-4 y dictamen de GLM.
