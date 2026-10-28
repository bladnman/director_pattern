import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import worker, { prefersMarkdown } from '../src/worker.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
test('ordinary browsers and wildcard clients retain HTML; only an explicit Markdown preference changes it', () => {
  for (const accept of ['', '*/*', 'text/html', 'text/html,application/xhtml+xml,*/*;q=0.8', 'text/markdown;q=0', 'text/markdown;q=.4,text/html;q=.9', 'text/markdown;q=no']) assert.equal(prefersMarkdown(accept), false, accept);
  for (const accept of ['text/markdown', 'text/markdown,text/html', 'text/markdown;q=.9,text/html;q=.5', 'TEXT/MARKDOWN; Q=1', 'text/markdown,*/*;q=.8']) assert.equal(prefersMarkdown(accept), true, accept);
});

test('root GET/HEAD negotiate the guide, preserve errors and expose cache/discovery headers', async () => {
  for (const method of ['GET', 'HEAD']) for (const markdown of [false, true]) {
    let assetPath;
    const env = { ASSETS: { fetch: async request => {
      assetPath = new URL(request.url).pathname;
      return new Response('fixture', { status: 200, headers: { 'Content-Type': 'text/html', Vary: 'Accept-Encoding' } });
    } } };
    const response = await worker.fetch(new Request('https://director.metal-sole.com/', { method, headers: { Accept: markdown ? 'text/markdown' : '*/*' } }), env);
    assert.equal(assetPath, markdown ? '/install.md' : '/');
    assert.equal(response.status, 200);
    assert.equal(response.headers.get('Vary'), 'Accept-Encoding, Accept');
    assert.match(response.headers.get('Link'), /install\.md.*text\/markdown/);
    assert.equal(response.headers.get('Content-Location'), markdown ? '/install.md' : null);
    assert.equal(await response.text(), method === 'HEAD' ? '' : 'fixture');
    if (markdown) assert.match(response.headers.get('Content-Type'), /^text\/markdown/);
  }
  const response = await worker.fetch(new Request('https://director.metal-sole.com/', { headers: { Accept: 'text/markdown' } }), { ASSETS: { fetch: async () => new Response('missing', { status: 404 }) } });
  assert.equal(response.status, 404);
});

test('non-root paths and other methods pass unchanged to assets', async () => {
  for (const [path, method] of [['/install.md', 'GET'], ['/missing', 'HEAD'], ['/', 'POST']]) {
    const request = new Request(`https://director.metal-sole.com${path}`, { method });
    const response = await worker.fetch(request, { ASSETS: { fetch: async received => {
      assert.equal(received, request);
      return new Response('fixture', { status: 404 });
    } } });
    assert.equal(response.status, 404);
    assert.equal(response.headers.get('Link'), null);
  }
});

test('copyable requests agree between the human page and agent guide', async () => {
  const html = await readFile(new URL('../public/index.html', import.meta.url), 'utf8');
  const guide = await readFile(new URL('../public/install.md', import.meta.url), 'utf8');
  const requests = [...html.matchAll(/<code id="(?:install|verify|update)-request">([^<]+)<\/code>/g)].map(match => match[1]);
  assert.equal(requests.length, 3);
  for (const request of requests) assert.ok(guide.includes(`\n${request}\n`), request);
  assert.equal(requests[0], 'Install the Director Pattern in this project: https://director.metal-sole.com');
  assert.equal(requests[2], 'Update the Director Pattern in this project from https://director.metal-sole.com');
  for (const [, anchor] of html.matchAll(/href="#([^"]+)"/g)) assert.ok(html.includes(`id="${anchor}"`), anchor);
});

test('the public front door exposes an agent guide that proceeds to canonical GitHub installation', async () => {
  const html = await readFile(new URL('../public/index.html', import.meta.url), 'utf8');
  const guide = await readFile(new URL('../public/install.md', import.meta.url), 'utf8');
  assert.match(html, /<nav[^>]*>[\s\S]*href="\/install\.md">For an agent<\/a>[\s\S]*<\/nav>/);
  assert.match(guide, /canonical GitHub installation protocol linked above/);
  assert.match(guide, /Do not send the user back\nto this website to repeat the same request/);
  assert.ok(guide.includes('https://github.com/bladnman/director_pattern/blob/main/pattern/INSTALL.md'));
  assert.ok(guide.includes('https://github.com/bladnman/director_pattern/blob/main/pattern/engine/references/UPDATES.md'));
  assert.match(guide, /exact reviewed commit/);
  assert.match(guide, /Copy only the manifest-selected payload/);
});

test('the four sparse markers and exact periodic report label agree with the source contract', async () => {
  const html = await readFile(new URL('../public/index.html', import.meta.url), 'utf8');
  const guide = await readFile(new URL('../public/install.md', import.meta.url), 'utf8');
  const contract = await readFile(new URL('../../pattern/engine/DIRECTION.md', import.meta.url), 'utf8');
  assert.deepEqual([...html.matchAll(/<dt>([^<]+)<\/dt>/g)].map(match => match[1]), ['❓', '🖐️', '🎬', '📋']);
  assert.match(html, /<h4 class="sitrep-heading">📋 SitRep<\/h4>/);
  for (const document of [html, guide, contract]) {
    assert.ok(document.includes('📋 SitRep'));
    assert.doesNotMatch(document, /\bSitrep\b/);
  }
  assert.match(guide, /do not attach it to every progress sentence/);
  assert.match(contract, /A checked Director keeps its required `🎬` response prefix/);
});

test('the public narrative names the Director and one-manager-per-outcome responsibilities without new role values or badges', async () => {
  const html = await readFile(new URL('../public/index.html', import.meta.url), 'utf8');
  const guide = await readFile(new URL('../public/install.md', import.meta.url), 'utf8');
  const llms = await readFile(new URL('../public/llms.txt', import.meta.url), 'utf8');
  const contract = await readFile(new URL('../../pattern/engine/DIRECTION.md', import.meta.url), 'utf8');
  for (const document of [html, guide, llms]) assert.match(document, /Request\s+Manager/);
  assert.match(contract, /Request Manager/);
  assert.match(contract, /A specialty[^.]*is a task within the outcome, not a reason for\s+another manager/);
  assert.match(guide, /a specialty is a task within the outcome, not a reason for\s+another manager/);
  assert.match(guide, /only `worker` and\s+`director`/);
  assert.match(guide, /maintained responsibilities, not new\s+role values/);
  assert.match(guide, /Managers and other actors use an assigned identity[^.]*never\s+the badge/);
  assert.match(html, /Managers and other actors use an assigned name[^.]*never the badge/);
  assert.match(html, /<p class="status-limit">[^<]*project Director role[^<]*managers or workers[^<]*<\/p>/);
});

test('production output contains only reviewed public assets, not installation/private state', async () => {
  execFileSync(process.execPath, ['scripts/build.mjs'], { cwd: root });
  const names = (await readdir(new URL('../dist/', import.meta.url))).sort();
  assert.deepEqual(names, ['404.html', '_headers', 'index.html', 'install.md', 'llms.txt', 'mark.svg', 'robots.txt', 'script.js', 'sitemap.xml', 'styles.css']);
  for (const name of names) {
    const value = await readFile(new URL(`../dist/${name}`, import.meta.url), 'utf8');
    assert.doesNotMatch(value, /\/Users\/|\.reference\/|setup-receipt|source-bundles|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY/);
  }
  const manifest = JSON.parse(await readFile(new URL('../../pattern/manifest.json', import.meta.url), 'utf8'));
  assert.ok([...manifest.base_files, ...manifest.tracked_files].every(file => !file.startsWith('site/')));
});
