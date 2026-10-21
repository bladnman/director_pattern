# Director Pattern website

Intended public URL: https://director.metal-sole.com/
Agent entrypoint: https://director.metal-sole.com/install.md

This is the public introduction, outside the installable `pattern/` payload.
The canonical contracts and install/update protocols remain in the public GitHub
package. The website summarizes them and links there; it is not an installer.
Visitors paste requests into their existing project agent, rather than a terminal.
The browser cannot inspect a local project or claim an installation is present.
Install and update requests use `https://director.metal-sole.com` as the public
front door. A visible **For an agent** link opens `install.md`; that guide directs
authorized work straight to the canonical GitHub package and exact reviewed SHA.
It must not ask an agent to return to the website and repeat the same request.

## Build and background preview

Requires Node.js 22+. The existing Wrangler CLI handles Worker preview/publishing.
No runtime packages, backend, accounts, analytics, external fonts, or trackers.

```sh
cd site
npm test
npm run build
npm run dev
```

The build copies exactly ten allowlisted files from `public/` into disposable
`dist/`. It never traverses the source repository, `.director/`, or `.reference/`.
Keep private receipts, screenshots, browser fixtures, and raw source evidence out
of this directory. `dist/`, logs, and local Wrangler cache are ignored.
Stop only the preview/browser processes started for this site's checks.

## Publication and rollback

Preparation is local until a publication receipt confirms a deployment.
Source pushes do not publish. When publication is authorized, use the existing
Wrangler login and `npm run deploy` to deploy Worker `director-pattern-site`.
The configuration has no routes: attach only `director.metal-sole.com` as this
Worker's custom domain as a separate scoped action. Leave sibling domains,
other Workers and zone-wide policies intact. No credential belongs in source.

Before publication: run tests/build, inspect the exact `dist/` list, then use
headless desktop (1440), phone (390), and small-phone (320) checks for overflow,
navigation, all three copy buttons, denied-clipboard selection, reduced motion,
and keyboard operation. Keep QA artifacts outside the repository. Compare
the page with current contracts, especially setup/status and update claims.

After publication: verify normal DNS/TLS, HTML and explicit Markdown root
responses, HEAD, `install.md`, `llms.txt`, asset bytes, and missing/private-path
404s. Check ordinary agent clients as well as a browser. Do not assume a shared
edge policy is necessary; diagnose any specific failure before changing a
hostname-scoped rule. Record the actual deployment/version and verified URL.

Record `wrangler deployments list --name director-pattern-site`. Roll back to a
known-good version with `wrangler rollback VERSION_ID --name director-pattern-site`
or deploy its reviewed source revision. A first launch has no prior site version;
record that limit. Domain removal is separate from a code rollback.

## Agent discovery

The page visibly links `install.md`, with HTML and HTTP alternate links.
`llms.txt` indexes the guide and canonical package. Root clients explicitly
preferring `text/markdown` receive the guide; browsers and wildcard clients
receive HTML. Both vary on Accept. These conventions help discovery, without
promising automatic installation or version detection.

## Presentation and boundaries

A warm neutral page with a restrained rust accent introduces the Director, a
Request Manager (one per complete outcome, directing specialists), and the shared
recorder with a diagram and one labeled illustrative request.
Installation, checking setup, and manual updates each have a copyable request.
Tracked/lean options and existing tracker preservation stay visible. The status
example explains the four sparse markers and the **📋 SitRep** report heading
without claiming activity. That heading belongs to periodic report blocks, while
the checked project Director retains its `🎬` response prefix; managers and other
actors use assigned identities. The page names the adoption prerequisites (role
index, model/effort mapping, recorder route, identity roster) and that an update
leaves those project-owned mappings in place.
The site makes no adoption, performance, customer, or behavioral guarantees.

## Local verification

After the Director / Request Manager revision, all eight site contract cases pass.
A quick headless look at 1440, 760, 390 and 320 pixels found no horizontal
overflow and a readable diagram. The copy-button, keyboard, denied-clipboard,
reduced-motion, JavaScript-disabled, Worker and independent-review checks in the
next paragraph describe the earlier director/worker revision and are not re-run
for this one.

Earlier revision, October 17, 2026: seven site contract cases passed. All 30
repository tests passed at the initial launch; the unchanged helper is outside this
website revision. The production build contains ten allowlisted files. Background
headless checks at 1440, 390 and 320 pixels verify all three exact copy requests,
keyboard activation and denied-clipboard selection, visible anchor navigation,
reduced-motion rendering and no horizontal overflow. The page loads without script
errors, failed requests or external asset requests. Installation text and
navigation remain available with JavaScript disabled. Local Worker checks verify
HTML/Markdown negotiation, HEAD, the guide's content type and a private-path 404.
An independent review checked contract accuracy, role-first setup checks, privacy
and publication scope. These local results do not establish deployment, adoption,
or agent behavior.
