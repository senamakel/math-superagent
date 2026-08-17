# Librarian cycle — Cesarz–Woldar proof body acquired (2026 cycle)

## What was done this cycle

The library entering this cycle was already comprehensive (48+ sources, all
indexed, both open requests `exact-list-prime-051a` and
`published-mechanism-ruling-5cf8` closed by `answers:` claim markers). The one
documented deficiency in the automorphism tier was that **Cesarz–Woldar 2023
("On the automorphism group of a putative Conway 99-graph") was present only as
its arXiv landing page** (`cesarz-woldar-automorph-conway99.full.md` is the
abstract); claims `aut-cw-2025` and the consolidated note flagged "proof body
absent, only landing page."

## Acquisition
- **URL:** https://arxiv.org/html/2308.02978v1
- **File:** `research/sources/cesarz-woldar-automorph-conway99-body.full.md` (76,917 bytes)
- **Verified substantive:** outline shows Sec 3 (Nonexistence of an order-14
  automorphism, with the orbit/3-cycle-counting proof of Theorem 1),
  Sec 4 (Consequences of divisibility by 7: Proposition 2 — 7||G| ⟹ G ≅ Z₇ or
  Frob(21), with orbit valencies determined), Secs 5–6 (computer elimination of
  Frob(21)). Read Theorem 1's proof directly — a genuine argument, not a stub.

## What it establishes (confirms claims aut-cw-2025 / automorphism-orders-consolidated)
- No order-14 automorphism (computer-free).
- 7 | |G| ⟹ G ≅ Z₇ (priori: Z₇ or Frob(21); Frob(21) eliminated by computer).
- 2 | |G| ⟹ |G| | 6, i.e. G ∈ {Z₂, Z₆, S₃}.
- Confirms the computer-assistance distinction already recorded: (1′),(2′) are
  computer-free in published form; the Frob(21) elimination is computer-assisted.

## Indexing / record updates
- Replaced the placeholder digest with a proper summary:
  `research/summaries/cesarz-woldar-automorph-conway99-body.md`
- Added the source to `research/summaries/index.md` under the automorphism tier.
- Added the row to `research/LIBRARY-REPORT.md` source table.
- Updated the claim anchor in
  `research/notes/automorphism-orders-consolidated.md` to point at the proof body.
- Indexed the full text for local search (`index_document`).

## Memory
`remember_memory` was attempted and refused by the memory server (degraded;
documented in CONTEXT.md). The durable record lives entirely on disk — full text,
summary, index entries, and the consolidated claim note — so nothing is lost.
Do NOT retry memory until it recovers; per directive, use `read_ledger` and
`grep_workspace` instead.

## Status
Library is complete for the current attack surface. No new source acquisition is
warranted except against a **new** gap stated in `derived/REQUESTS.md` (none now
open). The three open tasks in TASKS.md are all computational gating tasks
(clique-complex homology; incidence-budget controls; pair-labeling gate), not
library gaps — out of librarian scope.
