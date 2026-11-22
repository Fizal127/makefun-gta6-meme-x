// gta6-meme-x-01 entry — "Sick Day in Leonida" (Node 22, standard library only).
//
// The entry is the X post itself: the meme (meme.png) is posted on X from a
// public account with make.fun and the play code in its text, and POST.json
// names the post. This program only copies POST.json from the repository root
// to /output/POST.json, where the gate reads it. Nothing it writes is judged:
// the house reads the post itself from X (its first picture and its text).
//
// Run it the way the grader does (from the repository root):
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
  console.log(`POST.json copied to ${join(OUTPUT_DIR, 'POST.json')}`);
} catch (err) {
  console.error(`could not copy POST.json from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
