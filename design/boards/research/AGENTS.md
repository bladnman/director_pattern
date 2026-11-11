# Research and diagnosis board

This is the root board (stable ID `research`) for this project's research and
diagnosis investigations. It is explanatory reference material, not installation
payload or operating policy. Current operating authority is the starter payload
under pattern/starter/ and development/BEHAVIOR_PARITY.md.

Before you change the board, read ../../../TINKA.md and this installation's
tinka/app/docs/AGENT.md and docs/PROTOCOL.md. The schema-2 store in ../.tinka owns
organization, build state and review. Use supported CLI operations, and never
hand-edit transaction metadata. Files in this folder are editable project-owned
resources and must work without Tinka.

To add an investigation, create one item on `research` with its own child board.
Give it a dated folder here holding `report.md` and a self-contained
`slides.html`, plus optional SVG diagrams. Add a row to README.md. Update the
investigation as findings land. Keep earlier findings and their corrections
visible, keep stable item IDs, and keep review notes.

This folder is public. Do not include verbatim owner conversation, session or
request IDs, transcript or scratch paths, private store locators, emails or
personal paths. Label facts, hypotheses, proposals, published changes and live
verification separately. Use no model names; say strongest, middle and lightest
tier.
