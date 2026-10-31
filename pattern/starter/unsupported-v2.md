# Unsupported experimental starter 2

The experimental single-JSON backend at public source
[`e99cdb5`](https://github.com/bladnman/director_pattern/tree/e99cdb5e41c80a5c7d1a53471fa98376fe808fe7/pattern/starter)
is retained in immutable Git history and private trial fixtures, not as a supported
alternative. It lost initial plan/owner history on update, could leave newly added
work accepted, and did not consistently verify an earlier source after addenda.
Its five states also omitted established dependency, handoff, attachment and
recovery behavior. Utility trials did not establish that record compatibility.

Starter 3 restores the established `director-request-bundles` backend behind flat
roles. An existing starter-2 `.director/state.json` installation must be preserved
unchanged for explicit scoped recovery/review; install/upgrade refuses it. No
automatic conversion, copied identity or silent loss of old data is implemented.
Recover exact sources, owners, commitments, evidence and pending approvals before
any separately authorized transition. Do not continue using its acceptance/status
as proof that an outcome is safely complete. Mature existing trackers are retained;
this correction does not migrate them or imply publication/adoption.
