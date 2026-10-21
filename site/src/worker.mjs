// Only an explicit Markdown preference changes the root representation.
export function prefersMarkdown(accept = '') {
  const ranges = accept.toLowerCase().split(',').map(part => {
    const [type, ...params] = part.trim().split(';');
    const value = params.find(param => param.trim().startsWith('q='));
    const parsed = value === undefined ? 1 : Number(value.trim().slice(2));
    return { type, q: Number.isFinite(parsed) && parsed >= 0 && parsed <= 1 ? parsed : 0 };
  });
  const markdown = ranges.find(range => range.type === 'text/markdown');
  if (!markdown || markdown.q === 0) return false;
  const html = ranges.find(range => range.type === 'text/html')
    ?? ranges.find(range => range.type === 'text/*')
    ?? ranges.find(range => range.type === '*/*');
  return markdown.q >= (html?.q ?? 0);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== '/' || !['GET', 'HEAD'].includes(request.method)) return env.ASSETS.fetch(request);
    const markdown = prefersMarkdown(request.headers.get('accept') ?? '');
    if (markdown) url.pathname = '/install.md';
    const asset = await env.ASSETS.fetch(new Request(url, request));
    const headers = new Headers(asset.headers);
    const vary = headers.get('Vary');
    headers.set('Vary', vary ? `${vary}, Accept` : 'Accept');
    headers.set('Link', '</install.md>; rel="alternate"; type="text/markdown"');
    headers.set('Cache-Control', 'public, max-age=300');
    if (markdown) {
      headers.set('Content-Type', 'text/markdown; charset=utf-8');
      headers.set('Content-Location', '/install.md');
    }
    return new Response(request.method === 'HEAD' ? null : asset.body, {
      status: asset.status, statusText: asset.statusText, headers
    });
  }
};
