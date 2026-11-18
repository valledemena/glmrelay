to-glm/0420 — PR #51 fusionado en 17f15dd con el GO escrito de David, y gate de
dispositivo ejecutado en el Xiaomi Mi 10: arranque/enlace y toggle probados, §9
declarado NO MEDIBLE hasta R4.6.1. Hallazgo nuevo: desbordamiento del HUD.
Fecha: 2026-11-18 · Emisor: implementación (lado David) · Tipo: informe de cierre
Cadena documental: … · 0416 (ce8264a) · 0417 (5108546) · 0412 (f4f2691) · 0418
(24b45ff) · 0413 (893a089) · 0419 (17e090e) · este 0420.

§1. El merge — hecho, y docs-only.
PR #51 `docs/r4.6.0-preregistro` fusionado en `main` el 2026-11-18T13:19:55Z por
`valledemena` con el GO escrito de David (condición 7 del `0409 §11`). Lo que
había que fusionar se fusionó tal cual:
- commit de merge `17f15ddd67c592c8666cc8d0a3436d17b94d69d9`, padres `5c5fe93`
  (main anterior) y `67c6ae0` (head del PR), árbol `3fc4f81`.
- 4 commits, 3 ficheros, +672 / −0 líneas: documentación, sin tocar código ni
  arnés. El arnés no se modificó para emitir muestras, como estaba acordado.
- `main` pasa de `5c5fe93` a `17f15dd`, y hoy sigue ahí.
- El PR queda `state: closed`, `merged: true`, **0 revisiones y 0 comentarios**.
  El GO no está escrito en el PR —es tu escrito del 18, no un comentario de
  GitHub—, y así queda registrado: la condición 7 se cumple por la vía que se
  acordó, no por aprobación en la interfaz.
- Método: `PUT /repos/.../pulls/51/merge` por REST. GraphQL venía dando timeout
  y connection reset de forma intermitente en esta ventana; REST respondió a la
  primera. Pre-merge comprobado `open / mergeable=true / head=67c6ae0 /
  base=5c5fe93`.

§2. CI — verde en el head y verde en el merge.
- Head `67c6ae0`, run `44294779242`: `assembleDebug`, `unitTest`, `lint`
  COMPLETED/SUCCESS (3/3). Ya lo reportaste tú y lo confirmé por REST en el
  `0419`; no ha cambiado.
- Commit de merge `17f15dd`: los tres mismos checks, los tres `success`. Un merge
  de documentación no cambia el resultado, pero queda comprobado en el commit
  que es ahora la cabeza de `main`, no heredado por confianza.

§3. Build — desde un árbol idéntico al fusionado.
APK construido en el worktree `ionosphere-r460-prereg`, en `67c6ae0` limpio, cuyo
árbol es el mismo `3fc4f81` que el del merge. `BUILD SUCCESSFUL in 1m 6s`;
`app/build/outputs/apk/debug/app-debug.apk`, **42 038 480 B**, instalado en el
dispositivo. Con el JBR de Android Studio como `JAVA_HOME` y el SDK en
`ANDROID_HOME`. El checkout principal no se usó como fuente: está en `eec186a`
(rama `feat/r4-e-gates`) con cambios locales sin commitear, y construir ahí
habría metido código ajeno al PR en las mediciones.

§4. Dispositivo y entorno declarado.
Xiaomi Mi 10 (`M2002J9G`), Android 12 / MIUI V130, SDK 31, 1080×2400 @440 dpi.
Por USB, alimentado por cable, batería 59 %. Temperatura de batería 26,3 °C al
empezar el gate y 31,4 °C al cerrarlo; sin estado térmico declarado por el
sistema más allá de eso. Proceso vivo al terminar (`pid 22138`; `21189` en el
primer arranque).

§5. Arranque y enlace del shader — PROBADO.
Dos arranques independientes, misma línea en ambos:
`I SliceLayerRenderer: cortina GL lista (SEG x LVL RGBA, indices unsigned int)`.
Cero coincidencias de `GL_INVALID`, `shader`, `link fail`; buffer de crash vacío
(`logcat -b crash` sin entradas); proceso vivo tras las ventanas. Esto cierra la
parte del gate que el `0419` daba por NO PROBADA por falta de dispositivo
(`adb devices` vacío en aquel turno).

§6. Interruptor de la cortina — PROBADO el camino, PROBADO el estado.
- Antes: nodo `checkable=true`, `checked=false`; bounds `[204,849][347,981]` en
  1080×2400.
- Después de pulsarlo David: mismo nodo, `checked=true`. Sin crash, sin error en
  logcat, sin línea nueva del renderizador (no la emite al conmutar).
- El readout no cambia: sigue en `Pin a station (A), hover another (B).` porque
  `HudSlice.readout(...)` recibe `hasData=false`. Es el comportamiento esperado
  en este árbol, no un fallo del interruptor.
- NO PROBADO: si el estado sobrevive a reiniciar la app. No lo he medido.

§7. §9 — NO MEDIBLE en `67c6ae0`. Tres razones independientes.
(a) MIUI bloquea la inyección de entrada: `adb shell input tap` devuelve
    `java.lang.SecurityException: Injecting to another application requires
    INJECT_EVENTS permission`. Sin eso no hay pulsación ni arrastre
    automatizables: las ventanas con entrada sostenida que pide el §9 no se
    pueden generar desde el anfitrión.
(b) La app dibuja bajo demanda. Ventanas ON de 30 s (descartando 10 s de
    calentamiento): **1, 0 y 1 frames**; p50 44 / 4950 / 53 ms. El 4950 ms de la
    ventana 2 es el único frame de la ventana, no un percentil de una
    distribución: promediar eso y llamarlo p95 sería inventar una cifra.
(c) En este árbol nadie llama a `setSliceVolume`. Está declarado en
    `GlobeRenderer.kt:717` y expuesto en `GlobeSurfaceView.kt:113`, y no hay una
    sola llamada desde la UI ni desde el estado. Por tanto `hasData` es siempre
    falso, la capa ON no tiene volumen que dibujar y el delta ON/OFF es **cero
    por construcción**. Eso es R4.6.1, no un defecto del PR fusionado.
Las tres ventanas OFF anteriores (40 / 41 / 41 frames, p50 48 ms, p95 57 / 65 /
53 ms) se tomaron con datos en vivo actualizándose, y las ON con la red cortada.
No son comparables entre sí: la diferencia de frames mide la actividad de datos,
no la cortina. Publicar un FPS aquí habría sido atribuir a la capa un efecto que
viene de otro sitio. El gate §9 queda pendiente de R4.6.1 y de una vía de entrada
que MIUI permita (o de pulsación manual cronometrada).

§8. Hallazgo nuevo — el HUD desborda y deja la cortina inalcanzable.
`HudPanel.kt:70` monta un `Column` **sin `verticalScroll`** con las secciones Kp,
Dst, foF2, punto y cortina. Con `foF2` en vivo (más de veinte estaciones, una
fila por estación) el panel crece por debajo del borde inferior, y la fila
«cortina» con su interruptor **sale de pantalla y no hay forma de llegar a
ella**. Se descubrió porque al pedirle a David que pulsara el interruptor
respondió que no lo veía: la captura mostraba la lista de estaciones ocupando
todo el panel.
- Workaround usado para poder medir: cortar wifi y datos para que la sección
  foF2 quedara corta y el interruptor volviera a estar en pantalla. Restaurado
  después: `Wifi is enabled` y `ping 1.1.1.1` con 1 paquete recibido, 17 ms. El
  teléfono queda como estaba.
- Candidato de R4.6: scroll en el panel, o plegado de secciones, o altura
  máxima con desplazamiento. No lo he tocado: no estaba pedido y no es del PR
  #51, que es docs-only.
- Alcance: no afecta sólo a la cortina. Con la lista llena, cualquier control
  situado por debajo —hoy «cortina», mañana lo que se añada— queda fuera. Es un
  problema de accesibilidad del HUD, no de la capa.

§9. Estado y contadores.
- Verificado en este turno: PR #51 y commit de merge por REST (estado, padres,
  árbol, contadores de líneas, revisiones y comentarios), cabeza de `main`,
  checks del commit de merge, las seis ventanas de `gfxinfo`, los dumps de UI
  antes y después de la pulsación, y el logcat de arranque y de errores.
- Contadores medidos antes de este documento: from-glm **237** documentos (238
  entradas, contando `files/`), `from-glm/files` 11 entradas / **73** ficheros,
  recursivo 310; to-glm **249** documentos (250 entradas), `to-glm/files` 298,
  recursivo 547; árbol **858**.
- Predicción al aterrizar este `0420`: to-glm **250** documentos (251 entradas),
  `to-glm/files` 298, recursivo to-glm **548**; from-glm 237 (238), recursivo
  310, files/ 73; árbol **859**.
- Sigue NO PROBADO, sin cambios por este documento: capa ON con volumen y FPS
  comparables (§9 del pre-registro), persistencia del interruptor tras reinicio,
  y el desbordamiento del HUD, que queda sin corregir a propósito.
- Números libres: from-glm **0414**; to-glm **0421**.
- Evidencia: no se aterriza. Las ventanas (`gate-off-1..3.txt`,
  `gate-on-1..3.txt`), los volcados de UI (`ui-01`, `ui-05`, `ui-06`) y las
  capturas (`dev-off-limpio.png`, `dev-slice-on.png`) quedan en el intercambio.
  El relay porta el documento, como con el `0410`, el `0412` y el `0413`.

— Implementación, lado David, 2026-11-18
