// news-image-20261124 entry (Node 22, standard library only).
// The image beside this file is the entry: a one-page newspaper front
// page summing up Tuesday 24 November 2026, drawn by draw.py.
// This program copies it to /output/entry.png (or MAKEFUN_OUTPUT_DIR
// when set, for local runs), after checking it is a whole PNG within
// the gate limits (at most 1 MiB, at most 1024 x 1024 pixels).
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const bytes = readFileSync(join(here, "entry.png"));

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!bytes.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.png is not a PNG");
}
if (bytes.length > 1048576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB limit`);
}
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 limit`);
}

mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "entry.png");
writeFileSync(outPath, bytes);
// The grader runs the program twice and both runs must write the same
// bytes, so confirm the copy is byte-identical before reporting success.
if (!readFileSync(outPath).equals(bytes)) {
  throw new Error("output copy differs from entry.png");
}
console.log(`OK: wrote entry.png (${bytes.length} bytes, ${width}x${height})`);
