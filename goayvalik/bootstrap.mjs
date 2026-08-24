import fs from 'node:fs';
import path from 'node:path';

const dir = new URL('.', import.meta.url);
const chunkNames = fs.readdirSync(dir)
  .filter((name) => /^source-\d+\.b64$/.test(name))
  .sort();

if (!chunkNames.length) {
  throw new Error('Go Ayvalık source manifest chunks are missing.');
}

const manifestJson = Buffer.concat(
  chunkNames.map((name) => Buffer.from(fs.readFileSync(new URL(name, dir), 'utf8'), 'base64'))
).toString('utf8');

const manifest = JSON.parse(manifestJson);
for (const [relativePath, content] of Object.entries(manifest)) {
  const target = path.resolve(process.cwd(), relativePath);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.writeFileSync(target, content, 'utf8');
}
console.log(`Materialized ${Object.keys(manifest).length} Go Ayvalık source files.`);
