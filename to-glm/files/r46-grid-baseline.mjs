#!/usr/bin/env node
/**
 * r46-grid-baseline.mjs — arnes reproducible de la medicion base de R4.6.0.
 *
 * Mide la construccion de la rejilla de perfiles del pin web 8cdc3348 SIN
 * duplicar fisica: materializa del commit pin los modulos puros del pin,
 * los empaqueta con el esbuild del propio repo web y ejecuta la cadena de
 * produccion (stations -> interpProfiles -> applyDayNight -> buildDensityVolume).
 *
 * Uso:
 *   node r46-grid-baseline.mjs <ruta-del-clon-web> [--runs N] [--warmup N]
 *
 * Requisitos: git, Node >= 20.11 (import.meta.dirname), un clon de
 * valledemena/ionosphere-live-3d-web con node_modules instalado (esbuild
 * viene como dependencia de vite).
 * No escribe en el clon: trabaja en un directorio temporal.
 *
 * Salida: un JSON por stdout (entorno, pin verificado, tiempos y memoria).
 */
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import os from "node:os";
import path from "node:path";

const PIN = "8cdc3348ab087d10dd43807af217da4e246d996d";
const FILES = {
  "src/lib/iono/profileGrid.ts": "73207e86298742c3928078660b9ee2d93e9fde33",
  "src/lib/iono/ionomath.ts": null,
  "src/lib/iono/densityVolume.ts": null,
  "src/lib/iono/layerProfile.ts": null,
};

const argv = process.argv.slice(2);
const webRoot = argv.find((a) => !a.startsWith("--"));
if (!webRoot) {
  console.error("uso: node r46-grid-baseline.mjs <ruta-del-clon-web> [--runs N] [--warmup N]");
  process.exit(2);
}
const flag = (name, dflt) => {
  const i = argv.indexOf(`--${name}`);
  return i >= 0 && argv[i + 1] ? Number(argv[i + 1]) : dflt;
};
const RUNS = flag("runs", 15);
const WARMUP = flag("warmup", 3);

function git(args, cwd) {
  return execFileSync("git", args, { cwd, encoding: "utf8", maxBuffer: 1 << 26 }).trim();
}

// 1. El clon debe contener el commit pin como objeto (no hace falta checkout).
try {
  git(["cat-file", "-e", `${PIN}^{commit}`], webRoot);
} catch {
  console.error(`ERROR: el clon no contiene el commit pin ${PIN}. Haz: git fetch --all`);
  process.exit(3);
}

// 2. Verificacion de arbol: blobs de los modulos puros en el pin.
const blobs = {};
for (const rel of Object.keys(FILES)) {
  blobs[rel] = git(["rev-parse", `${PIN}:${rel}`], webRoot);
}
const failures = Object.entries(FILES).filter(([rel, want]) => want && blobs[rel] !== want);
if (failures.length) {
  console.error(`ERROR: blob inesperado en el pin: ${JSON.stringify(failures)}`);
  process.exit(4);
}

// 3. Materializacion del subarbol del pin en un temporal (git archive + tar).
const tmp = mkdtempSync(path.join(os.tmpdir(), "r46-"));
const cleanup = () => rmSync(tmp, { recursive: true, force: true });
process.on("exit", cleanup);
// git archive a fichero + tar -x: no depende del shell ni del separador |.
const tarPath = path.join(tmp, "pin.tar");
execFileSync("git", ["archive", `--output=${tarPath}`, PIN, "src/lib/iono"], { cwd: webRoot });
execFileSync("tar", ["-xf", "pin.tar"], { cwd: tmp }); // rutas relativas: MSYS tar lee "C:" como host remoto

const entry = path.join(tmp, "entry.ts");
writeFileSync(entry, readFileSync(path.join(import.meta.dirname, "r46-entry.ts"), "utf8"));

// 4. Bundle con el esbuild del repo web (viene con vite).
const esbuildBin = path.join(webRoot, "node_modules", "esbuild", "bin", "esbuild");
if (!existsSync(esbuildBin)) {
  console.error("ERROR: falta node_modules/esbuild en el clon web (npm ci).");
  process.exit(5);
}
const outFile = path.join(tmp, "bundle.mjs");
execFileSync(process.execPath, [esbuildBin, entry, "--bundle", "--platform=node", "--format=esm", "--target=node20", `--outfile=${outFile}`, "--log-level=warning"], {
  cwd: tmp,
  stdio: ["ignore", "inherit", "inherit"],
});

// 5. Ejecucion: el bundle imprime el JSON de medicion.
const report = execFileSync(process.execPath, ["--expose-gc", outFile, String(RUNS), String(WARMUP)], {
  encoding: "utf8",
  maxBuffer: 1 << 26,
});

const meta = {
  harness: "r46-grid-baseline.mjs",
  pin: PIN,
  harness_sha256: createHash("sha256").update(readFileSync(process.argv[1])).digest("hex"),
  web_root_head: git(["rev-parse", "HEAD"], webRoot),
  web_root_status: git(["status", "--porcelain"], webRoot).length === 0 ? "limpio" : "sucio (irrelevante: se lee del pin, no del arbol de trabajo)",
  pin_blobs: blobs,
  pin_file_stats: Object.keys(FILES).map((rel) => {
    const buf = readFileSync(path.join(tmp, rel));
    return {
      path: rel,
      bytes: buf.length,
      lines: buf.toString("utf8").split("\n").length - 1,
      cr: (buf.toString("utf8").match(/\r/g) ?? []).length,
      sha256: createHash("sha256").update(buf).digest("hex"),
    };
  }),
};
console.log(JSON.stringify({ ...meta, measure: JSON.parse(report) }, null, 2));
