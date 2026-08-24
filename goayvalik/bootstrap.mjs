import fs from 'node:fs';
import path from 'node:path';

const manifest = JSON.parse(fs.readFileSync(new URL('./source-manifest.json', import.meta.url), 'utf8'));
for (const [relativePath, content] of Object.entries(manifest)) {
  const target = path.resolve(process.cwd(), relativePath);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.writeFileSync(target, content, 'utf8');
}
console.log(`Materialized ${Object.keys(manifest).length} Go Ayvalık source files.`);
