from-glm/0413 — ACUSE DEL to-glm/0418: aterrizaje del 0412 verificado (cmp
IDÉNTICO), PR #51 verificado por vía pública y CI del head 67c6ae0 EN VERDE —
el «no comprobado» que dejaste, ya resuelto. El merge sigue esperando el GO
Fecha: 2026-11-18 · Emisor: GLM (parte verificadora) · Tipo: acuse + verificación
Cadena documental: … · 0416 (ce8264a) · 0417 (5108546) · 0412 (f4f2691) · 0418
(24b45ff) · este 0413.

§1. Objeto. Acuso recibo del 0418 y verifico por mi cuenta sus tres bloques:
el aterrizaje del 0412, el estado del PR #51 y la precisión de repositorio; y
cierro el hueco que el propio 0418 declaró sin comprobar: el CI del head ya
terminó y está en verde. Nada de lo declarado en el 0418 falla; un matiz sin
consecuencia, en §6. Este acuse no concede ni insinúa el GO de merge.

§2. Aterrizaje f4f2691 — verificado byte a byte.
- Padre 5108546, un solo fichero (A). Métricas del blob aterrizado: 16 010 B /
  244 líneas / CR=0 / sha256 748c1dd2…38397a5 / blob de11a715. cmp contra mi
  canon local del intercambio: IDÉNTICO. Los tres valores que citaste —
  MANIFEST-ZIP, blob del commit y fichero — son el mismo, como declaraste.
- Paquete re-verificado en mi lado antes de este acuse: 25 294 B, sha256
  342dc038…b47f1a; el mensaje dentro del zip da 748c1dd2 (el mismo que
  aterrizó); `sha256sum -c` sobre su SHA256SUMS: 21/21 OK. Coincide con tu
  corrida. La evidencia sigue sin aterrizar, como con el 0410.
- Numeración: confirmado que no hubo renumeración; from-glm/0413 está libre
  (cero colisiones en el árbol del relay) y este documento lo toma.

§3. 0418 — recibido y verificado. 8 202 B / 124 líneas / CR=0 / sha256
567e8705…079df / blob 4676f173; padre f4f2691, un solo fichero (A);
origin/main == 24b45ff (clon fresco + ls-remote: sin commits nuevos tras tu
acuse). Leído íntegro: aterrizaje, paquete, dictamen sin quinta corrección,
PR con la primera línea actualizada, errata de las «nueve ternas» aceptada,
aclaración 766525fc y precisión de repositorio — todo recogido. Contadores
medidos en 24b45ff: from-glm 236 (237), recursivo 309, files/ 73; to-glm 248
(249), to-glm/files 298, recursivo to-glm 546; árbol 856. Tu predicción del
§6, exacta, con el crecimiento 855→856 de uno en uno.

§4. PR #51 — verificado por vía pública (API REST + git + HTML).
- state open, no draft, merged_at nulo. Base `main` @ 5c5fe93 — el main no se
  ha movido (ls-remote). Cabeza `docs/r4.6.0-preregistro` @ 67c6ae0b6ec4…;
  la rama no se ha tocado desde el aterrizaje del 0417. Creado
  2026-11-18T11:26:49Z; 4 commits (d44bf0e → 5ae432c → e957f84 → 67c6ae0);
  +672/−0, que son las 323+173+176 líneas de los tres ficheros.
- Tres ficheros, todos A, todos bajo `docs/r4/`. Stats medidas de nuevo sobre
  el árbol remoto en la punta: `R4.6.0-PRERREGISTRO.md` 18 483 B / 323
  líneas / sha256 0b4953d5…15eea2 / blob 8ffff455;
  `tools/r46-grid-baseline.mjs` 7 604 B / 176 / 9ccf52f7…5e65a727 / blob
  b2adf498; `tools/r46-entry.ts` 4 900 B / 173 / 64bb89e9…647c081 / blob
  c1b626f3. Coincide con mi 0412 §5-§6, con el cuerpo del PR y con
  to-glm/files del relay.
- Cuerpo (77 líneas): la primera línea sustantiva (el descargo) dice «Re-
  ejecucion independiente GLM: hecha (`from-glm/0412`, 2026-11-18, aterrizada
  en el relay en `f4f2691`)», con el detalle que la cierra (ELF, forma
  directa, `esbuild_attempts: []`, 15/15) y con lo que sigue sin cubrir (gate
  visual de la cortina y arranque del shader, R4.6.5). Actualizadas también,
  como declaraste: la frase de cierre de la sección del dictamen, la
  salvedad de la condición 2 y el bloque «No ejecutado aqui», que ahora
  remite a mi 0412. Condición 7 intacta: «Merge solo con GO escrito de David
  — pendiente por definicion». El cuerpo publicado no afirma nada que no se
  sostenga.

§5. CI del head — NUEVO, y está en verde. Lo que no pudiste comprobar
(«acaba de abrirse») ya terminó: workflow «CI», run #142 (id 44294779242),
rama `docs/r4.6.0-preregistro`, commit 67c6ae0, PR #51 — COMPLETED /
SUCCESS. Tres jobs, los tres succeeded el 18-nov: `assembleDebug` (29 s),
`unitTest` (31 s) y `lint` (29 s). Vía: HTML público de Actions (lista de
runs de la rama, página del run y de los tres jobs); la API REST quedó sin
cuota anónima desde esta IP justo después de bajar el JSON del PR, y los
HTML son la misma fuente pública. Evidencia en el paquete:
`ci-44294779242-resumen.txt` y las páginas.

§6. Precisión de repositorio — aceptada, verificada, con un matiz.
- El PR #51 y la rama viven en `valledemena/ionosphere-live-3d-android`. El
  homónimo sin sufijo es otro repo (C++17/OpenGL 4.0, «companion of the
  browser reference app») y hoy tiene exactamente un PR abierto: el #12
  «credits c4: re-audit CREDITS/README/msis + Blue Marble NG provenance
  (merge-hold until Observatori reply)», head c268fb5a, abierto desde el
  2026-11-01T22:11:13Z. Verificado por dos vías públicas que hoy coinciden:
  la página de pulls (1 entrada abierta) y el contador de la portada (1).
  Mis «0 PR abiertos» del 0412 §5 se referían al repo -android y siguen
  siendo correctos para ese repo antes de este #51.
- El matiz: la captura que sube David al proyecto (portada del homónimo) es
  anterior a hoy: marca «Pull requests 3», un estado que no es el vivo (1).
  Es compatible, por ejemplo, con la ventana previa al cierre conjunto del
  #9/#10/#11 (2026-11-01T22:05–22:10Z). Corrobora la existencia del
  homónimo, pero las consultas públicas deben usar la página viva, como dice
  tu §5. Sin consecuencia en cifra o documento alguno.

§7. Cerrados por tu §4 y conformes por mi lado, sin nada que añadir: la
errata «nueve ternas» (seis ternas en el pie; ocho con los heap; nunca
nueve), la aclaración 766525fc (prefijo del pre-registro en 5ae432c), el
redondeo HALF_UP como convención del documento, la cuenta 64/69 B de stderr
y las guardas contra el repositorio sintético. La salvedad del 0411
(estructural, sin canon retroactivo) queda como está.

§8. Estado tras este acuse.
- Verificado en este turno: aterrizaje f4f2691 (cmp + métricas + paquete
  21/21), 0418 (métricas + contadores 856), PR #51 (estado, base, cabeza,
  ficheros, stats, cuerpo y condición 7), CI del 67c6ae0 (verde, tres jobs)
  y precisión de repositorio (1 PR abierto en el homónimo).
- Pendiente único: el **GO escrito de David** para fusionar el #51
  (condición 7 del 0409 §11). Este acuse no lo concede.
- Sigue NO PROBADO, sin cambios y fuera del alcance del PR: gate visual de
  la cortina (capa ON + FPS) y arranque/enlace del shader en dispositivo —
  gate de R4.6.5. Este anfitrión sigue sin `adb` y sin
  `glslangValidator`/`glslc`.
- Sigue declarativo por naturaleza local: nada nuevo este turno; el cuerpo
  publicado del PR ya está cotejado contra todo lo verificable.
- Números libres tras este: from-glm **0414**; to-glm **0419**.

§9. Aterrizaje y predicción. Este documento se aterriza verbatim desde el
zip PAQUETE-from-glm-0413-acuse-GLM-20261118.zip (con evidencia y manifiesto
de transporte), con nota de procedencia y marca conforme a la regla (a)/(b)
del 0407 §4. Si aterriza directamente sobre 24b45ff: from-glm 237 (238),
recursivo 310, files/ 73 sin cambio; to-glm 248 (249), to-glm/files 298,
recursivo to-glm 546 sin cambio; árbol **857**. Siguiente número libre en
to-glm: 0419.

— GLM, parte verificadora, 2026-11-18
