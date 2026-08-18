# Lu 2026 — Bautin certificate spec (ancillary reproducibility file)

Source: `research/sources/lu-h14-3-spec-bautin.full.md` [[lu-h14-3-spec-bautin.full]] — from `https://arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/specifications/bautin.md` (plain text).

## What the source establishes

A machine-readable specification inside Lu's ancillary `h14_3_reproducibility/`
bundle, describing the computer-assisted part of the H¹⁴₃ proof:

- Claims: `lem:h14-center-bautin-ideal` and `lem:center-word-domains`.
- Manuscript locations: Theorem `thm:part-ii-center-ideal` and Appendix
  `app:center-bautin`.
- Scripts: `certificates/verify_h14_center_basis.py`,
  `verify_bautin_recurrence.py`, `verify_h14_center_bautin.py`,
  `verify_h14_center_global_domains.py`.
- Contains the finite mathematical alphabet/recurrence, physical-exhaustiveness
  statement, exact machine predicate, human-proof remainder, SHA-256, and
  reproduction commands.

## What it implies here

This is the **verification spec** for the part of Lu's claim this run has
independently checked: the Bautin-recurrence core. This run's clean-room
re-derivation (`code/bautin/verify_lu_core.py` → `code/out/lu_core.captured.txt`,
"ALL CLEAN-ROOM CHECKS PASS") covers the bridge identities, Darboux cofactors,
the degree-4 obstruction `8L4 = AC+CD+2DF−EF`, and the degree-6 equality
`192·L6 + P30 = 0`, independently of Lu's own `verify_bautin_recurrence.py`
(which `code/lyap_audit.py` byte-level reconstructs, also PASS). The two bundle
scripts are **now HELD** (fifth-pass addendum):
`verify_h14_center_bautin.py` and `verify_h14_center_global_domains.py` are in
`research/sources/` (see summaries
[[lu-h14-3-verify-center-bautin.py]] and [[lu-h14-3-verify-center-global-domains.py]],
claim `lu-h14-3-bundle-scripts-now-held`) — but **NOT yet re-executed** in this
workspace, so their focal-value/centre-barrier rows (U(0)=1/48,
both-centre-components, global-domain barriers) remain **asserted-by-source**
until a clean-room capture upgrades them to `checked`.

Evidence class: sourced-held (spec text); the claims it specifies are
**asserted-by-source**, with the algebraic core independently verified here.
See `research/notes/lu-finite-core-verified.md` and thread `lu-h14-3-verification`.