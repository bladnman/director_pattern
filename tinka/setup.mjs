#!/usr/bin/env node
import { createHash, randomUUID } from 'node:crypto';
import { execFile } from 'node:child_process';
import { inflateRawSync } from 'node:zlib';
import { readFile, realpath, lstat, mkdir, rename, rm, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { promisify } from 'node:util';
import { fileURLToPath } from 'node:url';

const execFileAsync = promisify(execFile);
export const DEFAULT_REPO = 'bladnman/tinka';
const maxZipBytes = 100 * 1024 * 1024;
const maxFileBytes = 20 * 1024 * 1024;
const maxEntries = 10000;
const requiredFiles = ['package.json', 'cli.mjs', 'server.mjs', 'public/home.html', 'lib/config.mjs', 'docs/PROTOCOL.md'];
const usage = `Usage:
  node tinka-install.mjs --project /absolute/project [--boards design/boards] [--label TEXT] [--version X.Y.Z]
  node tinka/setup.mjs [--version X.Y.Z | --zip PATH --checksum PATH]
  node install.mjs [--repo OWNER/REPO] [--version X.Y.Z] --install-dir /absolute/app [--config /absolute/config.json]
  node install.mjs --zip /absolute/tinka-vX.Y.Z.zip --checksum /absolute/tinka-vX.Y.Z.zip.sha256 --install-dir /absolute/app [--config /absolute/config.json]`;

const crcTable = Array.from({ length: 256 }, (_, index) => {
  let value = index;
  for (let bit = 0; bit < 8; bit += 1) value = value & 1 ? 0xedb88320 ^ (value >>> 1) : value >>> 1;
  return value >>> 0;
});
function crc32(bytes) {
  let value = 0xffffffff;
  for (const byte of bytes) value = crcTable[(value ^ byte) & 0xff] ^ (value >>> 8);
  return (value ^ 0xffffffff) >>> 0;
}
function inside(base, candidate) {
  const relative = path.relative(base, candidate);
  return relative === '' || (relative !== '..' && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative));
}
async function exists(candidate) {
  try { return await lstat(candidate); }
  catch (error) { if (error.code === 'ENOENT') return null; throw error; }
}
// Shared only by cooperating start/install commands for this app copy. No registry.
function processAlive(pid) {
  if (!Number.isSafeInteger(pid) || pid < 1) return false;
  try { process.kill(pid, 0); return true; } catch (error) { return error.code !== 'ESRCH'; }
}
export function operationLockPath(app) { return path.join(path.dirname(app), `.${path.basename(app)}.operation-lock`); }
export async function withAppLock(app, action, { token = process.env.TINKA_OPERATION_TOKEN, waitMs = 20000 } = {}) {
  app = await canonicalFuturePath(app);
  const lock = operationLockPath(app);
  await mkdir(path.dirname(lock), { recursive: true });
  const deadline = Date.now() + waitMs;
  const identity = randomUUID();
  for (;;) {
    try { await mkdir(lock); break; }
    catch (error) {
      if (error.code !== 'EEXIST') throw error;
      const owner = await readFile(path.join(lock, 'owner.json'), 'utf8').then(JSON.parse).catch(() => null);
      if (owner && owner.token === token && processAlive(owner.pid)) return action(token);
      if (owner && Number.isSafeInteger(owner.pid) && !processAlive(owner.pid)) {
        // A recovery guard prevents two stale-owner cleaners deleting a successor.
        const guard = `${lock}.recovery`;
        try { await mkdir(guard); } catch (error) { throw new Error(`App operation recovery needs review: ${guard}`); }
        try {
          const current = JSON.parse(await readFile(path.join(lock, 'owner.json'), 'utf8'));
          if (current.token === owner.token && !processAlive(current.pid)) await rm(lock, { recursive: true });
        } finally { await rm(guard, { recursive: true, force: true }); }
        continue;
      }
      if (Date.now() >= deadline) throw new Error(`Another app operation is active or needs recovery: ${lock}`);
      await new Promise(resolve => setTimeout(resolve, 40));
    }
  }
  try {
    await writeFile(path.join(lock, 'owner.json'), JSON.stringify({ pid: process.pid, token: identity }), { flag: 'wx' });
    return await action(identity);
  } finally { await rm(lock, { recursive: true, force: true }); }
}

export async function installationPristine(app) {
  const receipt = await readFile(path.join(app, 'INSTALLATION.json'), 'utf8').then(JSON.parse).catch(() => null);
  if (!receipt?.files || typeof receipt.files !== 'object' || Array.isArray(receipt.files) || !Object.keys(receipt.files).length) return false;
  const actual = {};
  async function walk(directory, prefix = '') {
    for (const entry of await readdir(directory, { withFileTypes: true })) {
      const relative = prefix + entry.name;
      if (relative === 'INSTALLATION.json') continue;
      if (entry.isDirectory()) await walk(path.join(directory, entry.name), `${relative}/`);
      else if (entry.isFile()) actual[relative] = createHash('sha256').update(await readFile(path.join(directory, entry.name))).digest('hex');
      else throw new Error('Installed app contains a symlink or unsupported file.');
    }
  }
  try { await walk(app); } catch { return false; }
  return Object.keys(actual).length === Object.keys(receipt.files).length && Object.entries(actual).every(([file, digest]) => receipt.files[file] === digest);
}

// Deliberately narrow format. Version numbers alone never grant compatibility.
export function compatibilityError(metadata, { fromVersion, toVersion, workspaceSchema = 1, nodeVersion = process.versions.node, platform = process.platform } = {}) {
  const stable = /^\d+\.\d+\.\d+$/;
  if (!stable.test(fromVersion || '') || !stable.test(toVersion || '')) return 'Prerelease or unknown version requires review.';
  if (fromVersion.split('.')[0] !== toVersion.split('.')[0]) return 'App major changes require review.';
  if (!metadata || metadata.schemaVersion !== 1 || metadata.version !== toVersion || !Array.isArray(metadata.fromVersions) || metadata.fromVersions.some(version=>typeof version!=='string'||!stable.test(version)) || !metadata.fromVersions.includes(fromVersion)) return 'Release has no explicit compatibility from this version.';
  if (metadata.migration !== 'none' || !Array.isArray(metadata.schemas?.config) || !Array.isArray(metadata.schemas?.workspace) || metadata.schemas.config.some(value=>!Number.isInteger(value)) || metadata.schemas.workspace.some(value=>!Number.isInteger(value)) || !metadata.schemas.config.includes(1) || !metadata.schemas.workspace.includes(workspaceSchema)) return 'Schema compatibility or migration requires review.';
  const minimum = typeof metadata.runtime?.node==='string' ? /^>=(\d+)$/.exec(metadata.runtime.node) : null;
  if (!minimum || Number(minimum[1]) < 22 || Number(nodeVersion.split('.')[0]) < Number(minimum[1]) || !Array.isArray(metadata.runtime?.platforms) || metadata.runtime.platforms.some(value=>typeof value!=='string'||!['darwin','linux'].includes(value)) || !metadata.runtime.platforms.includes(platform)) return 'Runtime compatibility requires review.';
  return null;
}

function parseArgs(args) {
  const options = {};
  for (let index = 0; index < args.length; index += 1) {
    const name = args[index];
    if (name === '--help') return { help: true };
    if (!['--project', '--boards', '--label', '--repo', '--version', '--zip', '--checksum', '--install-dir', '--config'].includes(name) || options[name] || !args[index + 1] || args[index + 1].startsWith('--')) throw new Error(usage);
    options[name] = args[++index];
  }
  if (!options['--project'] && path.basename(fileURLToPath(import.meta.url)) === 'setup.mjs') options['--project'] = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
  if (options['--project'] && (options['--install-dir'] || options['--config'])) throw new Error('Use --project or --install-dir/--config, not both.');
  if (!options['--project'] && (options['--boards'] || options['--label'])) throw new Error('--boards and --label require --project.');
  if (options['--version'] && !/^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$/.test(options['--version'])) throw new Error('Use a version such as 0.2.0.');
  if ((!options['--install-dir'] && !options['--project']) || (options['--repo'] && options['--zip']) || Boolean(options['--checksum']) !== Boolean(options['--zip'])) throw new Error(usage);
  return options;
}
function expectedChecksum(text, filename) {
  const match = text.trim().match(/^([a-fA-F0-9]{64})(?:\s+\*?([^\r\n]+))?$/);
  if (!match) throw new Error('Invalid SHA-256 checksum file.');
  if (match[2] && match[2].trim() !== filename) throw new Error('Checksum names a different ZIP.');
  return match[1].toLowerCase();
}
function verifyChecksum(bytes, text, filename) {
  const expected = expectedChecksum(text, filename);
  const actual = createHash('sha256').update(bytes).digest('hex');
  if (actual !== expected) throw new Error('ZIP SHA-256 does not match its checksum.');
}

function safeEntryName(name, directory) {
  if (!name.startsWith('board-room/')) throw new Error(`Unexpected ZIP root: ${name}`);
  const relative = name.slice('board-room/'.length);
  if (!relative) {
    if (directory) return null;
    throw new Error('ZIP root cannot be a file.');
  }
  if (relative.includes('\\') || relative.includes('\0') || relative.startsWith('/') || relative.includes(':')) throw new Error(`Unsafe ZIP path: ${name}`);
  const components = relative.replace(/\/$/, '').split('/');
  if (components.some(component => !component || component === '.' || component === '..' || component.startsWith('.'))) throw new Error(`Unsafe ZIP path: ${name}`);
  return components.join('/');
}

export function readSafeZip(bytes) {
  if (bytes.length > maxZipBytes) throw new Error('ZIP exceeds the size limit.');
  let end = -1;
  for (let position = bytes.length - 22; position >= Math.max(0, bytes.length - 65557); position -= 1) {
    if (bytes.readUInt32LE(position) === 0x06054b50) { end = position; break; }
  }
  if (end < 0) throw new Error('ZIP end record is missing.');
  const count = bytes.readUInt16LE(end + 10);
  const centralSize = bytes.readUInt32LE(end + 12);
  const centralStart = bytes.readUInt32LE(end + 16);
  if (count > maxEntries || count === 0xffff || centralSize === 0xffffffff || centralStart === 0xffffffff || centralStart + centralSize > end) throw new Error('Unsupported ZIP directory.');
  let cursor = centralStart;
  let total = 0;
  const entries = [];
  const seen = new Set();
  for (let index = 0; index < count; index += 1) {
    if (cursor + 46 > end || bytes.readUInt32LE(cursor) !== 0x02014b50) throw new Error('Invalid ZIP directory entry.');
    const flags = bytes.readUInt16LE(cursor + 8);
    const method = bytes.readUInt16LE(cursor + 10);
    const expectedCrc = bytes.readUInt32LE(cursor + 16);
    const compressedSize = bytes.readUInt32LE(cursor + 20);
    const size = bytes.readUInt32LE(cursor + 24);
    const nameLength = bytes.readUInt16LE(cursor + 28);
    const extraLength = bytes.readUInt16LE(cursor + 30);
    const commentLength = bytes.readUInt16LE(cursor + 32);
    const mode = bytes.readUInt32LE(cursor + 38) >>> 16;
    const localOffset = bytes.readUInt32LE(cursor + 42);
    const nameEnd = cursor + 46 + nameLength;
    if (nameEnd > end || nameEnd + extraLength + commentLength > end) throw new Error('Truncated ZIP directory.');
    const name = bytes.subarray(cursor + 46, nameEnd).toString('utf8');
    cursor = nameEnd + extraLength + commentLength;
    const directory = name.endsWith('/');
    const relative = safeEntryName(name, directory);
    if (relative === null) continue;
    const key = relative.toLowerCase();
    if (seen.has(key)) throw new Error(`Duplicate ZIP path: ${relative}`);
    seen.add(key);
    const fileType = mode & 0o170000;
    if (fileType === 0o120000 || (fileType && fileType !== (directory ? 0o040000 : 0o100000))) throw new Error(`Unsafe ZIP file type: ${relative}`);
    if (flags & 1 || ![0, 8].includes(method) || size > maxFileBytes || compressedSize > maxZipBytes) throw new Error(`Unsupported ZIP entry: ${relative}`);
    total += size;
    if (total > maxZipBytes) throw new Error('Expanded ZIP exceeds the size limit.');
    if (directory) { entries.push({ relative, directory: true }); continue; }
    if (localOffset + 30 > centralStart || bytes.readUInt32LE(localOffset) !== 0x04034b50) throw new Error(`Missing ZIP file header: ${relative}`);
    const localFlags = bytes.readUInt16LE(localOffset + 6);
    const localMethod = bytes.readUInt16LE(localOffset + 8);
    const localNameLength = bytes.readUInt16LE(localOffset + 26);
    const localExtraLength = bytes.readUInt16LE(localOffset + 28);
    const localName = bytes.subarray(localOffset + 30, localOffset + 30 + localNameLength).toString('utf8');
    const dataStart = localOffset + 30 + localNameLength + localExtraLength;
    if (localName !== name || localMethod !== method || localFlags !== flags || dataStart + compressedSize > centralStart) throw new Error(`Invalid ZIP file header: ${relative}`);
    const compressed = bytes.subarray(dataStart, dataStart + compressedSize);
    const content = method === 0 ? compressed : inflateRawSync(compressed, { maxOutputLength: maxFileBytes });
    if (content.length !== size || crc32(content) !== expectedCrc) throw new Error(`Corrupt ZIP file: ${relative}`);
    entries.push({ relative, directory: false, content });
  }
  if (cursor !== centralStart + centralSize) throw new Error('ZIP directory size mismatch.');
  for (const required of requiredFiles) if (!entries.some(entry => !entry.directory && entry.relative === required)) throw new Error(`ZIP is missing ${required}.`);
  return entries;
}

async function extract(entries, stage) {
  await mkdir(stage);
  for (const entry of entries) {
    const destination = path.join(stage, ...entry.relative.split('/'));
    if (!inside(stage, destination)) throw new Error(`Unsafe extraction path: ${entry.relative}`);
    if (entry.directory) await mkdir(destination, { recursive: true });
    else {
      await mkdir(path.dirname(destination), { recursive: true });
      await writeFile(destination, entry.content, { flag: 'wx', mode: 0o644 });
    }
  }
}

async function runCli(cli, command, config, token) {
  try { await execFileAsync(process.execPath, [cli, command, '--config', config], { timeout: 12000, env: {...process.env, TINKA_OPERATION_TOKEN: token, TINKA_SKIP_UPDATE: '1'} }); }
  catch (error) { throw new Error(`Managed ${command} failed: ${error.stderr?.trim() || error.message}`); }
}

async function validateExternal(configInput, installCanonical) {
  if (!configInput) return null;
  if (!path.isAbsolute(configInput)) throw new Error('--config must be absolute.');
  const configPath = await realpath(configInput);
  const settings = JSON.parse(await readFile(configPath, 'utf8'));
  if (settings.schemaVersion !== 1 || typeof settings.boardsRoot !== 'string' || !path.isAbsolute(settings.boardsRoot)) throw new Error('Invalid external config.');
  const boardsRoot = await realpath(settings.boardsRoot);
  if (inside(installCanonical, configPath) || inside(installCanonical, boardsRoot) || inside(boardsRoot, installCanonical)) throw new Error('Config and boards must remain outside the app directory.');
  if(settings.workspaceRoot!==undefined&&(typeof settings.workspaceRoot!=='string'||!path.isAbsolute(settings.workspaceRoot)))throw new Error('workspaceRoot must be absolute.');
  const workspaceRoot=await canonicalFuturePath(settings.workspaceRoot||path.join(boardsRoot,'.tinka'));
  if(inside(installCanonical,workspaceRoot)||inside(workspaceRoot,installCanonical))throw new Error('Workspace metadata must remain outside the app directory.');
  return { configPath, boardsRoot, workspaceRoot };
}

async function canonicalFuturePath(input){
  const absolute=path.resolve(input);
  try{return await realpath(absolute);}catch(error){if(error.code!=='ENOENT')throw error;const parent=path.dirname(absolute);if(parent===absolute)throw error;return path.join(await canonicalFuturePath(parent),path.basename(absolute));}
}

export async function installArchive(options) {
  if (!path.isAbsolute(options.installDir)) throw new Error('--install-dir must be absolute.');
  return withAppLock(options.installDir, token => installArchiveLocked({...options, lockToken: token}), {token: options.lockToken});
}
async function installArchiveLocked({ zipBytes, checksumText, zipName, installDir, configPath, lockToken, compatibility, fromVersion, requirePristine = false, pinPath }) {
  if (!path.isAbsolute(installDir)) throw new Error('--install-dir must be absolute.');
  verifyChecksum(zipBytes, checksumText, zipName);
  const entries = readSafeZip(zipBytes);
  const parent = path.dirname(path.resolve(installDir));
  await mkdir(parent, { recursive: true });
  const canonicalParent = await realpath(parent);
  const canonicalInstall = path.join(canonicalParent, path.basename(installDir));
  // Use the real parent for CLI invocation too. Node resolves module URLs
  // through a parent symlink, while argv retains the spelling the user gave.
  installDir = canonicalInstall;
  const external = await validateExternal(configPath, canonicalInstall);
  const current = await exists(installDir);
  if (current?.isSymbolicLink() || (current && !current.isDirectory())) throw new Error('Install destination must be a real directory or absent.');
  if (current) {
    if (!external) throw new Error('Pass --config for an upgrade so the managed service can be checked and restarted.');
    let installed;
    try { installed = JSON.parse(await readFile(path.join(installDir, 'package.json'), 'utf8')); }
    catch { throw new Error('Destination is not a recognized Board Room installation.'); }
    if (installed.name !== 'board-room') throw new Error('Destination is not a recognized Board Room installation.');
  }
  if (requirePristine && (!current || !await installationPristine(installDir))) throw new Error('Installed app is modified or lacks a file baseline; review before replacing it.');
  const pinBefore = pinPath ? await readFile(pinPath, 'utf8') : null;
  const configBefore = external ? await readFile(external.configPath, 'utf8') : null;
  const identity = randomUUID();
  const stage = path.join(canonicalParent, `.${path.basename(installDir)}.stage-${identity}`);
  const backup = current ? path.join(canonicalParent, `.${path.basename(installDir)}.backup-${new Date().toISOString().replaceAll(':', '-')}-${identity.slice(0, 8)}`) : null;
  let wasRunning = false;
  let movedOld = false;
  let movedNew = false;
  let newRunning = false;
  let pinChanged = false;
  try {
    await extract(entries, stage);
    const manifest = JSON.parse(await readFile(path.join(stage, 'package.json'), 'utf8'));
    if (manifest.name !== 'board-room' || !/^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$/.test(manifest.version)) throw new Error('ZIP contains an invalid app package.');
    if (compatibility) {
      const embedded = JSON.parse(await readFile(path.join(stage, 'lib/update-compatibility.json'), 'utf8'));
      if (JSON.stringify(embedded) !== JSON.stringify(compatibility)) throw new Error('Package compatibility does not match the checked release metadata.');
      let workspaceSchema = 1;
      if (external && await exists(path.join(external.workspaceRoot, 'workspace.json'))) workspaceSchema = JSON.parse(await readFile(path.join(external.workspaceRoot, 'workspace.json'), 'utf8')).schemaVersion;
      const reason = compatibilityError(embedded, {fromVersion, toVersion: manifest.version, workspaceSchema});
      if (reason) throw new Error(reason);
      if (manifest.engines?.node !== embedded.runtime.node) throw new Error('Package runtime does not match compatibility metadata.');
    }
    const files = Object.fromEntries(entries.filter(entry => !entry.directory).map(entry => [entry.relative, createHash('sha256').update(entry.content).digest('hex')]));
    await writeFile(path.join(stage, 'INSTALLATION.json'), `${JSON.stringify({version:manifest.version,archive:zipName,sha256:createHash('sha256').update(zipBytes).digest('hex'),installedAt:new Date().toISOString(),files},null,2)}\n`, {flag:'wx'});
    if (external) {
      const runtime = await exists(`${external.configPath}.pid.json`);
      if (runtime) {
        if (!current) throw new Error('A managed process exists, but this install directory has no old app to stop.');
        await runCli(path.join(installDir, 'cli.mjs'), 'stop', external.configPath, lockToken);
        wasRunning = true;
      }
    }
    if (current) { await rename(installDir, backup); movedOld = true; }
    await rename(stage, installDir); movedNew = true;
    if (external) {
      await runCli(path.join(installDir, 'cli.mjs'), 'start', external.configPath, lockToken);
      newRunning = true;
      await verifyInstalledHealth(installDir, external.configPath, manifest.version);
      if (!wasRunning) { await runCli(path.join(installDir, 'cli.mjs'), 'stop', external.configPath, lockToken); newRunning = false; await atomicText(external.configPath, configBefore); }
    }
    if (pinPath) { await atomicText(pinPath, `${JSON.stringify({...JSON.parse(pinBefore), version: manifest.version}, null, 2)}\n`); pinChanged = true; }
    return { version: manifest.version, installDir, backup, restarted: wasRunning, configPath: external?.configPath || null };
  } catch (error) {
    const failures = [error.message];
    if (pinChanged) { try { await atomicText(pinPath, pinBefore); } catch (pinError) { failures.push(`Pin restore failed: ${pinError.message}`); } }
    if (movedNew) {
      if (external && (newRunning || await exists(`${external.configPath}.pid.json`))) {
        try { await runCli(path.join(installDir, 'cli.mjs'), 'stop', external.configPath, lockToken); }
        catch (stopError) { throw new Error(`${failures[0]} New app may still be running; backup preserved at ${backup}. ${stopError.message}`); }
      }
      await rm(installDir, { recursive: true, force: true });
    }
    if (external && movedNew) { try { await atomicText(external.configPath,configBefore); } catch(configError) { failures.push(`Config restore failed: ${configError.message}`); } }
    if (movedOld) {
      try { await rename(backup, installDir); }
      catch (restoreError) { failures.push(`Backup restore failed: ${restoreError.message}`); }
    }
    if (wasRunning && movedOld && await exists(installDir)) {
      try { await runCli(path.join(installDir, 'cli.mjs'), 'start', external.configPath, lockToken); }
      catch (restartError) { failures.push(`Old app restart failed: ${restartError.message}`); }
    }
    throw new Error(failures.join(' '));
  } finally {
    await rm(stage, { recursive: true, force: true });
  }
}

export async function atomicText(file, text) {
  const temporary = `${file}.${randomUUID()}.tmp`;
  try { await writeFile(temporary, text, {flag: 'wx'}); await rename(temporary, file); }
  finally { await rm(temporary, {force: true}); }
}
export async function verifyInstalledHealth(app, configPath, version) {
  const runtime = JSON.parse(await readFile(`${configPath}.pid.json`, 'utf8'));
  const config = JSON.parse(await readFile(configPath, 'utf8'));
  if (runtime.configPath !== configPath || runtime.appPath !== app || !Number.isInteger(runtime.port)) throw new Error('Health runtime identity mismatch.');
  const health = await fetch(`http://127.0.0.1:${runtime.port}/api/health`, {signal: AbortSignal.timeout(1500)}).then(response => {if (!response.ok) throw new Error('Health request failed.'); return response.json();});
  const boardsRoot=await realpath(config.boardsRoot);
  const workspaceRoot=await canonicalFuturePath(config.workspaceRoot||path.join(boardsRoot,'.tinka'));
  const defaultRoot=await canonicalFuturePath(path.join(boardsRoot,'.tinka'));
  const workspaceId=createHash('sha256').update(`${configPath}\0${boardsRoot}${workspaceRoot===defaultRoot?'':`\0${workspaceRoot}`}`).digest('hex').slice(0,24);
  if (health.app !== 'board-room' || health.version !== version || health.configPath !== configPath || health.boardsRoot !== boardsRoot || health.workspaceId!==workspaceId || health.port!==runtime.port || config.port!==runtime.port || health.projectLabel !== (config.projectLabel?.trim() || path.basename(path.dirname(configPath)))) throw new Error('Installed app health identity/version mismatch.');
  return runtime;
}
export async function fetchLimited(url, headers, limit, timeoutMs = 4000) {
  const response = await fetch(url, { headers, signal: AbortSignal.timeout(timeoutMs) });
  if (!response.ok) throw new Error(`Download failed (${response.status}) for ${new URL(url).hostname}.`);
  if (Number(response.headers.get('content-length')) > limit) throw new Error('Download exceeds the size limit.');
  let size=0;const chunks=[];
  for await(const chunk of response.body){size+=chunk.length;if(size>limit)throw new Error('Download exceeds the size limit.');chunks.push(chunk);}
  return Buffer.concat(chunks);
}

export async function githubRelease(repo, requestedVersion) {
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repo) || repo.split('/').some(part => part === '.' || part === '..')) throw new Error('--repo must be OWNER/REPO.');
  const token = process.env.GITHUB_TOKEN;
  const headers = { 'Accept': 'application/vnd.github+json', 'User-Agent': 'tinka-installer' };
  if (token) headers.Authorization = `Bearer ${token}`;
  const endpoint = requestedVersion ? `tags/v${requestedVersion}` : 'latest';
  const metadata = JSON.parse((await fetchLimited(`https://api.github.com/repos/${repo}/releases/${endpoint}`, headers, 1024 * 1024)).toString('utf8'));
  const version = String(metadata.tag_name || '').replace(/^v/, '');
  if (!/^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$/.test(version)) throw new Error('Latest release has no supported version tag.');
  if (requestedVersion && version !== requestedVersion) throw new Error('Release version does not match the requested pin.');
  const zipName = `tinka-v${version}.zip`;
  const zip = metadata.assets?.find(asset => asset.name === zipName);
  const checksum = metadata.assets?.find(asset => asset.name === `${zipName}.sha256`);
  if (!zip || !checksum) throw new Error('Latest release lacks the app ZIP or its SHA-256 sidecar.');
  function assetURL(asset){
    const url=new URL(asset.url);
    if(url.protocol!=='https:'||url.hostname!=='api.github.com'||url.username||url.password||!url.pathname.toLowerCase().startsWith(`/repos/${repo.toLowerCase()}/releases/assets/`)||!/^\d+$/.test(url.pathname.split('/').at(-1)))throw new Error('Unexpected GitHub release asset URL.');
    return url.href;
  }
  const assetHeaders={...headers,Accept:'application/octet-stream'};
  const [zipBytes, checksumBytes] = await Promise.all([
    fetchLimited(assetURL(zip), assetHeaders, maxZipBytes),
    fetchLimited(assetURL(checksum), assetHeaders, 1024)
  ]);
  return { zipBytes, checksumText: checksumBytes.toString('utf8'), zipName };
}

export async function main(args = process.argv.slice(2)) {
  const options = parseArgs(args);
  if (options.help) return usage;
  let installDir = options['--install-dir'];
  let configPath = options['--config'];
  let project, settings;
  if(options['--project']){
    if(!path.isAbsolute(options['--project']))throw new Error('--project must be absolute.');
    project=await realpath(options['--project']);
    const directory=path.join(project,'tinka');
    if(await exists(directory)&&await realpath(directory)!==directory)throw new Error('The project tinka folder must not be a symlink.');
    const manifest=path.join(directory,'project.json');
    settings=await exists(manifest)?JSON.parse(await readFile(manifest,'utf8')):null;
    if(settings&&(settings.schemaVersion!==1||!/^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$/.test(settings.version)||typeof settings.boards!=='string'||!settings.boards||path.isAbsolute(settings.boards)||typeof settings.projectLabel!=='string'||!settings.projectLabel.trim()))throw new Error('Invalid tinka/project.json.');
    const boards=options['--boards']||settings?.boards||'design/boards';
    const boardsPath=path.resolve(project,boards);
    if(path.isAbsolute(boards)||!inside(project,boardsPath)||inside(directory,boardsPath)||inside(boardsPath,directory))throw new Error('Project boards must use a relative path inside the project, outside tinka/.');
    if(settings&&((options['--boards']&&options['--boards']!==settings.boards)||(options['--label']&&options['--label']!==settings.projectLabel)))throw new Error('Existing project settings differ.');
    if(await exists(boardsPath)&&!inside(project,await realpath(boardsPath)))throw new Error('Project boards leave this checkout.');
    installDir=path.join(directory,'app');
    const local=path.join(directory,'local');
    if(await exists(local)&&await realpath(local)!==local)throw new Error('The local config folder must not be a symlink.');
    const localConfig=path.join(local,'config.json');
    if(await exists(localConfig)){
      const config=JSON.parse(await readFile(localConfig,'utf8'));
      if(config.boardsRoot!==await realpath(boardsPath)||config.projectLabel!==(options['--label']||settings?.projectLabel||path.basename(project)))throw new Error('Local config belongs to another location or project. Inspect tinka/local before restoring.');
      configPath=localConfig;
    }else{
      // Restore machine-local config before candidate acceptance, even when a
      // checkout has no local/ directory. Never advance its existing pin first.
      await mkdir(boardsPath,{recursive:true});
      const canonicalBoards=await realpath(boardsPath);
      if(!inside(project,canonicalBoards)||inside(directory,canonicalBoards))throw new Error('Project boards leave this checkout.');
      await mkdir(local,{recursive:true});
      if(await realpath(local)!==local)throw new Error('The local config folder must not be a symlink.');
      await writeFile(localConfig,`${JSON.stringify({schemaVersion:1,port:43821,portMode:'auto',projectLabel:options['--label']||settings?.projectLabel||path.basename(project),boardsRoot:canonicalBoards,title:'Tinka'},null,2)}\n`,{flag:'wx'});
      configPath=localConfig;
    }
    const installed=path.join(installDir,'package.json');
    if(settings&&!options['--zip']&&!options['--version']&&!options['--repo']&&await exists(installed)){
      const current=JSON.parse(await readFile(installed,'utf8'));
      if(current.name==='board-room'&&current.version===settings.version){
        const prepared=await execFileAsync(process.execPath,[path.join(installDir,'cli.mjs'),'project','init','--project',project],{timeout:12000});
        return `Tinka ${current.version} is already installed.\n${prepared.stdout.trim()}`;
      }
    }
  }
  const requestedVersion=options['--version']||settings?.version;
  // A project may commit the matching app package for offline restoration.
  // Explicit source options always win; bundles are selected by the version pin.
  if(project&&requestedVersion&&!options['--zip']&&!options['--repo']){
    const archive=path.join(project,'tinka/packages',`tinka-v${requestedVersion}.zip`);
    if(await exists(archive)){
      if(!await exists(`${archive}.sha256`))throw new Error('Bundled project archive is missing its SHA-256 sidecar.');
      options['--zip']=archive;options['--checksum']=`${archive}.sha256`;
    }
  }
  const source = !options['--zip']
    ? await githubRelease(options['--repo']||settings?.repo||DEFAULT_REPO, requestedVersion)
    : {
      zipBytes: await readFile(options['--zip']),
      checksumText: await readFile(options['--checksum'], 'utf8'),
      zipName: path.basename(options['--zip'])
    };
  if(requestedVersion||project){
    verifyChecksum(source.zipBytes,source.checksumText,source.zipName);
    const entries=readSafeZip(source.zipBytes);
    const version=JSON.parse(entries.find(entry=>entry.relative==='package.json').content.toString('utf8')).version;
    if(requestedVersion&&version!==requestedVersion)throw new Error('Archive version does not match the project pin or requested version.');
    if(project&&!entries.some(entry=>entry.relative==='lib/project.mjs'))throw new Error('This release predates portable project setup. Use a current release, or --install-dir and --config for a manual layout.');
  }
  const result = await installArchive({ ...source, installDir, configPath, ...(project && settings && configPath ? {pinPath:path.join(project,'tinka/project.json')} : {}) });
  let prepared='';
  if(project){
    const arguments_=[path.join(result.installDir,'cli.mjs'),'project','init','--project',project];
    if(options['--boards'])arguments_.push('--boards',options['--boards']);
    if(options['--label'])arguments_.push('--label',options['--label']);
    if(options['--repo'])arguments_.push('--repo',options['--repo']);
    prepared=`\n${(await execFileAsync(process.execPath,arguments_,{timeout:12000})).stdout.trim()}`;
  }
  return `Installed Tinka ${result.version} at ${result.installDir}.${result.backup ? ` Backup: ${result.backup}.` : ''}${result.restarted ? ' Managed service restarted.' : ''}${prepared}`;
}

if (process.argv[1] && await realpath(path.resolve(process.argv[1])).catch(() => null) === fileURLToPath(import.meta.url)) {
  try { process.stdout.write(`${await main()}\n`); }
  catch (error) { process.stderr.write(`${error.message}\n`); process.exitCode = 1; }
}
