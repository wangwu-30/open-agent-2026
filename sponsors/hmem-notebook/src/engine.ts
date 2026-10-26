// Official H-MEM reference, installed at the revision pinned in package.json.
// Runtime imports come only from vendor/hmem; no alternate engine fallback.

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import type { HMEM } from "../vendor/hmem/src/index.ts";

const here = path.dirname(fileURLToPath(import.meta.url));
const entry = path.join(here, "..", "vendor", "hmem", "src", "index.ts");

export interface LoadedEngine {
  HMEM: typeof HMEM;
  source: string;
}

export async function loadHMEM(): Promise<LoadedEngine> {
  if (fs.existsSync(entry)) {
    const mod = await import(pathToFileURL(entry).href);
    return { HMEM: mod.HMEM, source: "vendor/hmem (official Meterless H-MEM reference)" };
  }
  console.error("H-MEM engine not found. Run the setup step first:\n\n  npm run setup\n");
  console.error("(It vendors the reference implementation into vendor/hmem via degit.)");
  process.exit(1);
}
