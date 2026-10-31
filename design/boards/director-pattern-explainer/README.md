# Director Pattern field guide

A public, durable, seven-topic explanatory reference based on source commit 8db49cb. Start at overview.html. HTML, CSS and SVG are local and have no Tinka SDK, remote assets, build step or runtime dependency.

Open through this project's Tinka resource root, or serve this directory with any static server. From the repository root, a standalone option is:

```sh
python3 -m http.server 8877 --bind 127.0.0.1 --directory design/boards/director-pattern-explainer
```

Then open http://127.0.0.1:8877/overview.html. Stop only that owned foreground server when finished. Normal operation uses the project Tinka service; see ../../../TINKA.md.

The explainer and diagrams are real. It does not execute the illustrated Director/worker workflows, start a learning reviewer, or imply installed-project acceptance. Evidence is distilled from the public walkthrough/validation notes. Private conversations, project conversion receipts and runtime configuration are excluded. Update claims from canonical source evidence; preserve dated revisions and stable item IDs.

The schema-2 metadata in ../.tinka owns board organization, item build state and notes. Use supported CLI operations rather than editing its transaction files. Resources in this folder remain ordinary editable project files.
