# Frontier verification — librarian close-out (attempt 3)

Status: library CLOSED by directive 18 (48 sources on disk, ROOT.md passes the
phase-1 exit test). This note records the one librarian action this cycle.

## What was verified (live searches, 2026 cycle)

The two frontier rows that cite each other and looked suspiciously recent are
REAL arXiv identifiers and ALREADY on disk. Neither is an invented-identifier
artifact:

- `arXiv:2604.23037` — Ali Keramatipour, "Approaching the Conway-99 problem
  using SAT solvers" (Cambridge MPhil thesis, dated 24 Apr 2026). Held as
  `research/sources/keramatipour-sat-conway99.full.md` (+ `-body`).
  Confirmed by live exa_search and by the source header
  (`arXiv:2604.23037v1 [cs.LO]`).
- `arXiv:1707.08047` — Zehavi & de Oliveir, "Not Conway's 99-Graph Problem"
  (2017). Held as `research/sources/zehavi-oliveira-not-conway-99.full.md`.

Phillips 2026 "Comprehensive Study of Clique Graphs..." (arXiv:2605.22867) is
also already held (`phillips-2026-clique-triangle-graphs.full.md`).

## The one genuinely-absent candidate, and why it was NOT fetched

Guseinov, "Five New Results on Conway's 99-Graph Problem" (Figshare
DOI 10.6084/m9.figshare.23732622.v1, 2023). Unrefereed, 0 citations. Triage
(read_sources, not download) verdict: not an authoritative source; no live open
gate is blocked on it; library is closed. Recorded as a lead only.

Its claim 5 (independence number alpha >= 10) is ALREADY integrated in the
library: claim `lou-murin-alpha22-block-design-reduction` states
`10 <= alpha <= 22 (lower bound from Guseinov, in-library)`.

Its claim 1 (a putative Conway 99-graph is NOT a subgraph of srg(243,22,1,2)
BvLS) is NOT held anywhere. If a live argument ever needs to rule BvLS in or out
as an ambient host to search inside for the 99-graph, this is the claim to
independently verify (it is unverified here; a subgraph-containment question is
computable only against an actual 99-graph or by a separate embedding argument,
neither of which exists).

## Conclusion

No new source acquired this cycle: the library already covers the recent
literature; the frontier is valid; the requests on disk are resumption artifacts
already answered by claims (srg33 dies on multiplicity integrality — claim
`integrality-five-members`; the automorphism prime-order list is consolidated in
claim `automorphism-orders-consolidated`). Nothing further to gather against a
closed library with no open acquisition gap.
