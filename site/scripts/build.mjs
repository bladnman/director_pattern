import { cp, mkdir, readFile, rm } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const source = path.join(root, 'public');
const output = path.join(root, 'dist');
// Deliberately enumerate public files. Never traverse the repository or local state.
export const publicFiles = [
  'index.html', 'styles.css', 'script.js', 'mark.svg',
  'install.md', 'llms.txt', 'robots.txt', 'sitemap.xml', '404.html', '_headers'
];
await Promise.all(publicFiles.map(file => readFile(path.join(source, file))));
await rm(output, { recursive: true, force: true });
for (const file of publicFiles) {
  await mkdir(path.dirname(path.join(output, file)), { recursive: true });
  await cp(path.join(source, file), path.join(output, file));
}
console.log(`Prepared ${publicFiles.length} public files in ${output}`);
