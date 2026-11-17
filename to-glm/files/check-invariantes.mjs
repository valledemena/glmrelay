#!/usr/bin/env node
// check-invariantes.mjs - verificador minimo de una salida de r46-grid-baseline.mjs
//
// Compara un JSON de salida nuevo contra los invariantes fijados en
// MANIFEST-sha256-glm-sim2-20261118.txt (mismo directorio por defecto):
// pin, harness_sha256, blobs del pin, dimensiones, celdas y checksums.
// Se ignoran a proposito los campos de tiempo y de heap (ruido de maquina).
//
// Uso:
//   node check-invariantes.mjs <salida.json> [--manifest <ruta-al-manifiesto>]
//
// Codigos de salida:
//   0  todos los invariantes cuadran
//   1  al menos una discrepancia (se listan todas)
//   2  uso incorrecto, fichero ilegible o JSON invalido
//
// Sin dependencias: solo modulos de Node.

import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const MANIFEST_DEFAULT = resolve(HERE, "MANIFEST-sha256-glm-sim2-20261118.txt");

const PIN = "8cdc3348ab087d10dd43807af217da4e246d996d";
// Payload vigente (2026-11-18: tercera correccion, invocacion robusta de
// esbuild) y payload anterior (2026-11-17), que se sigue aceptando para que
// una salida de la generacion previa no se lea como manipulada: lo que cambia
// entre las dos es la forma de invocar esbuild, no el objeto medido.
const HARNESS_SHA256 =
  "9ccf52f7bb7e5791e6210ddd696d1a4cf22324c8cff55ef76cbfc7fa5e65a727";
const HARNESS_SHA256_LEGACY = new Set([
  "b860a4aca35e565d341ff8a703f59bec00605e29694904d110b08502beca8c1a",
]);
const PIN_BLOBS = {
  "src/lib/iono/profileGrid.ts": "73207e86298742c3928078660b9ee2d93e9fde33",
  "src/lib/iono/ionomath.ts": "d27752f5f62091d22ef02707e90d124fa2ee8c1b",
  "src/lib/iono/densityVolume.ts": "63c16fd569c19a379a6b4a58ec5c006539a69671",
  "src/lib/iono/layerProfile.ts": "4184bdb1dcb2f2920915e0f12f61fd0100b70f7a",
};
// config -> dims "WxHxAltRes", rango "altMin-altMax", celdas, checksum
const CONFIGS = [
  { dims: "72x72x48", alt: "60-500", cells: 248832, checksum: 844848.546114 },
  { dims: "72x36x60", alt: "60-700", cells: 155520, checksum: 536270.831702 },
];

function usage(msg) {
  if (msg) console.error("ERROR: " + msg);
  console.error("uso: node check-invariantes.mjs <salida.json> [--manifest <ruta>]");
  process.exit(2);
}

function readJson(path) {
  let text;
  try {
    text = readFileSync(path, "utf8");
  } catch (err) {
    usage("no puedo leer " + path + " (" + (err.code || err.message) + ")");
  }
  try {
    return JSON.parse(text);
  } catch (err) {
    usage(path + " no es JSON valido: " + err.message);
  }
}

// Los invariantes de arriba son la referencia; el manifiesto debe seguir
// diciendo lo mismo. Si no, uno de los dos esta desactualizado y conviene
// parar antes de dar un veredicto.
function manifestDrift(manifestText) {
  const drift = [];
  if (!manifestText.includes(PIN)) drift.push("falta el pin en el manifiesto");
  if (!manifestText.includes(HARNESS_SHA256)) drift.push("falta harness_sha256");
  for (const [path, sha] of Object.entries(PIN_BLOBS)) {
    const short = sha.slice(0, 8);
    if (!manifestText.includes(short)) {
      drift.push("el manifiesto no lista el blob " + short + " (" + path + ")");
    }
  }
  for (const c of CONFIGS) {
    const needle = c.dims + " " + c.alt;
    if (!manifestText.includes(needle)) drift.push("falta la config " + needle);
    if (!manifestText.includes(String(c.checksum))) {
      drift.push("falta el checksum " + c.checksum);
    }
    if (!manifestText.includes(String(c.cells))) {
      drift.push("falta el conteo de celdas " + c.cells);
    }
  }
  return drift;
}

function main() {
  const args = process.argv.slice(2);
  let manifestPath = MANIFEST_DEFAULT;
  let jsonPath = null;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--manifest") {
      manifestPath = args[++i];
      if (!manifestPath) usage("--manifest necesita una ruta");
    } else if (args[i].startsWith("-")) {
      usage("opcion no reconocida: " + args[i]);
    } else if (jsonPath === null) {
      jsonPath = args[i];
    } else {
      usage("sobra el argumento: " + args[i]);
    }
  }
  if (!jsonPath) usage("falta la ruta del JSON a verificar");

  const manifestText = readFileSync(manifestPath, "utf8");
  const data = readJson(jsonPath);
  const measure = data && data.measure;
  if (!measure || !Array.isArray(measure.configs)) {
    usage(jsonPath + " no tiene la forma de salida del arnes (falta measure.configs)");
  }

  const results = [];
  const check = (ok, label, detail) => results.push({ ok, label, detail });

  check(data.pin === PIN, "pin", data.pin);
  check(data.web_root_head === PIN, "web_root_head", data.web_root_head);
  check(
    data.web_root_status === "limpio",
    "web_root_status",
    data.web_root_status,
  );
  check(
    data.harness_sha256 === HARNESS_SHA256 ||
      HARNESS_SHA256_LEGACY.has(data.harness_sha256),
    "harness_sha256",
    data.harness_sha256 === HARNESS_SHA256
      ? data.harness_sha256
      : data.harness_sha256 + " (payload de la generacion 20261117; vigente: " + HARNESS_SHA256 + ")",
  );

  const blobs = data.pin_blobs || {};
  for (const [path, sha] of Object.entries(PIN_BLOBS)) {
    check(
      blobs[path] === sha,
      "blob " + path,
      blobs[path] === undefined ? "(ausente)" : blobs[path],
    );
  }
  for (const path of Object.keys(blobs)) {
    if (!(path in PIN_BLOBS)) {
      check(false, "blob inesperado " + path, blobs[path]);
    }
  }

  const byKey = new Map();
  for (const cfg of measure.configs) {
    const key = cfg.w + "x" + cfg.h + "x" + cfg.altRes;
    const alt = cfg.altMinKm + "-" + cfg.altMaxKm;
    byKey.set(key + " " + alt, cfg);
  }
  for (const want of CONFIGS) {
    const key = want.dims + " " + want.alt;
    const cfg = byKey.get(key);
    if (!cfg) {
      check(false, "config " + key, "(ausente; hay: " + [...byKey.keys()].join(", ") + ")");
      continue;
    }
    check(
      cfg.cells === want.cells,
      "cells " + key,
      String(cfg.cells),
    );
    const gotSum = Number(cfg.checksum);
    check(
      Number.isFinite(gotSum) && Math.abs(gotSum - want.checksum) <= 1e-6,
      "checksum " + key,
      String(cfg.checksum) + " (esperado " + want.checksum + ")",
    );
    check(cfg.valid === true, "valid " + key, String(cfg.valid));
  }
  if (measure.configs.length !== CONFIGS.length) {
    check(
      false,
      "numero de configs",
      measure.configs.length + " (esperado " + CONFIGS.length + ")",
    );
  }

  const drift = manifestDrift(manifestText);
  check(
    drift.length === 0,
    "manifiesto coherente con el verificador",
    drift.length ? drift.join("; ") : manifestPath,
  );

  console.log("verificando: " + jsonPath);
  console.log("invariantes: " + manifestPath);
  for (const r of results) {
    console.log((r.ok ? "OK   " : "FALLO") + "  " + r.label + "  ->  " + r.detail);
  }
  const bad = results.filter((r) => !r.ok);
  console.log("");
  console.log(
    bad.length === 0
      ? "VEREDICTO: OK - " + results.length + "/" + results.length + " invariantes"
      : "VEREDICTO: FALLO - " + bad.length + " de " + results.length + " no cuadran",
  );
  console.log("(ms_median, ms_p95 y heap quedan fuera: ruido de maquina)");
  process.exit(bad.length === 0 ? 0 : 1);
}

main();
