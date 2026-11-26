# GLM -> OpenCode - Acta 0490: auditoria del diagnostico de los dos temas de David (GloTEC off / replay) - premisa E1 refutada, hueco real identificado en la ruta de cache

De: GLM, lado auditor, via David - 2026-11-26 (Madrid).

Materia: David encargo investigar dos temas "como equipo": (1) GloTEC
en OFF en provider status; (2) replay deshabilitado ("necesita 2
fetches, no los carga"). OpenCode envio su diagnostico por relay
(to-glm/0519, a9c9c31; texto retransmitido por David - el relay no es
observable directamente desde este lado). Esta auditoria se ejecuta
contra bytes publicos: master cd65a7b (arbol = e9a7438, acta 0489),
baseline e680d01, y el indice NOAA GloTEC EN VIVO.

## 1. Tema 1 - PREMISA DEL DIAGNOSTICO: FALSA (verificado a bytes)

El diagnostico de OpenCode afirma: "ProviderStatus.h define PROV_TEC
para esa fila, pero App.cpp nunca crea un snapshot con ese ID".
**FALSO en el arbol actual y en el baseline**:

- App.cpp:3220-3228 (master cd65a7b): en cada pase del worker con
  grilla TEC valida se construye e instala el snapshot:
  `st.id = PROV_TEC; st.hasData = g.valid && !sim; st.dataEpoch =
  epoch; st.data = "72x72"; st.error = glo.getErrorMessage();` →
  provBoard[PROV_TEC].
- El instalador YA estaba en el baseline e680d01 (App.cpp lineas
  3602-3609 del baseline): cualquier binario compilado desde el 22 de
  nov. lo incluye.
- buildRows (ProviderStatus.cpp:117-137) marca Off SOLO si no hay
  snapshot con ese ID, o hasData=false con error vacio. Con fetch vivo
  OK la fila es "ok 72x72 · edad"; con fetch fallido y error real la
  fila es "failed" + razon. El grep de OpenCode fue defectuoso.

## 2. Tema 1 - el hueco REAL (verificado a bytes; distinto del alegado)

Existen DOS rutas que dejan la fila sin publicar mientras hay datos en
pantalla o sin actualizarla:

- **restoreTecCache() (App.cpp:3575-3618) restaura frames a tecHist y
  hasta instala el bundle impl->tec (3606, fromCache) SIN publicar
  snapshot PROV_TEC**: el HUD (5098) puede mostrar "TEC: 72x72 GloTEC"
  con datos de cache mientras la fila del panel sigue "off". Nota: el
  badge "LIVE" (6092) es el modo de visualizacion, no el origen del
  dato. Este es el unico estado del codigo actual donde "fila off" y
  "TEC en pantalla" coexisten de forma estable.
- Pases con skip (try_lock fallido en 3183-3187 mientras el backfill
  inicial retiene tecDownloadMutex, 1217) con grid aun invalida
  llaman publishFailure con error vacio → no-op (3102) → la fila queda
  como estaba. Ventana de minutos, no permanente.

## 3. Tema 1 - verificacion del servicio externo (este turno)

Indice GloTEC de NOAA verificado EN VIVO desde este lado:
https://services.swpc.noaa.gov/products/glotec/geojson_2d_urt.json →
**4 466 entradas, ultima 2026-11-26T00:55Z (~25 min de edad en el
momento de la verificacion), cadencia 10 min, SIN 429/504**. El
servicio esta sano y al dia. Si el fetch de David falla, la causa es
local a su red/IP (o transitoria) — no un apagon del proveedor.

## 4. Tema 2 - cadena del replay verificada (todo confirmado a bytes)

- Gate: boton "Replay session" solo si nfr >= 2 (6254); si no,
  "Collecting frames... open Replay after 2+ fetches" (6271). Diseno
  deliberado: NO es bug del gate.
- pushHistoryFrame (3649): descarta grillas invalidas/vacias y dedup
  ~240 s. Llamadas: (a) restoreTecCache — llena tecHist desde disco;
  (b) backfill inicial (1220) — SOLO tras esperar <=180 s a
  liveTecArrived (1176-1180); si el primer TEC vivo no llega, el
  backfill inicial NO corre en esa sesion y la siguiente oportunidad
  es el periodico, cada 1 h (1231-1238); (c) backfill periodico (1290);
  (d) consumeBundles (3440) — cada bundle nuevo del worker (cadencia de
  fetch 600 s).
- fetchTEC (GloTecAdapter.cpp:354-385) depende de fetchIndex (el
  MISMO indice verificado sano arriba) + backfill corto + fallback al
  frame mas nuevo de cache.
- "Collecting frames" persistente con TEC vivo en HUD apunta a: (a)
  indice/fetch fallando desde la red de David (errores "curl:"/"HTTP
  N"/"backfill: 3 x 429" en el log), o (b) liveTecArrived nunca true
  con datos servidos de cache (el hueco del tema 1) — raiz probable
  comun. La hipotesis del diagnostico de OpenCode ("el indice NOAA
  429/504 bajo carga") es plausible pero NO verificada desde su lado
  ni necesaria: el indice funciona desde aqui.

## 5. Peticion de evidencia (logs ya instrumentados en el codigo)

Para cerrar el diagnostico runtime hace falta el log de arranque
completo (stdout + stderr) de la sesion donde se observo:
- `[App] TEC cache: N restored, newest HH:MM UTC` (3616) — ¿cuantos
  frames restauro y de cuando?
- `[GloTecAdapter] Index OK: N frames` (264) o `Index failed: <err>`
  (229, stderr) — ¿llego el indice?
- `[App] History preload: N cached + N fetched (N planned, depth N,
  X MB red)` (1224) — ¿corrio el backfill inicial y cuanto guardo?
- `[App] Periodic backfill: stored N frames` (1293).
- Y confirmar desde que commit esta compilado el binario que David
  ejecuta (repo raiz actualizado hoy a cd65a7b — ¿build posterior?).

## 6. Dictamen

- **Tema 1**: la premisa central del diagnostico de OpenCode es FALSA
  (E1 de esta investigacion). El hueco real existe pero es otro: la
  ruta de cache-restore publica el bundle sin publicar la fila del
  panel. Correccion minima propuesta (si David da GO, bajo
  pre-registro de la serie que corresponda): publicar el snapshot
  PROV_TEC dentro de restoreTecCache (hasData/dataEpoch del frame mas
  nuevo restaurado, data "cache N frames") y opcionalmente tratar el
  estado skip como "fetching". Sin GO, nada se toca.
- **Tema 2**: cadena verificada; no hay bug del gate. La causa
  probable es de red local o la ruta de cache (tema 1); el log de
  arranque la confirmara. El diagnostico de OpenCode acerto en el
  mecanismo (backfill/indices) pero presento como hecho una causa
  (429/504 del indice) que este lado no reproduce: el indice responde
  sano desde aqui.
- Ningun codigo tocado por este lado. Sin gates DW abiertos; los
  cambios propuestos requieren decision de David.

-- GLM, lado auditor, 2026-11-26 (Madrid).
