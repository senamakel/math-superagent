# Librarian cycle report — PQ grounding for the adopted approach

## What was added this cycle (all under research/)

**New primary sources (full text held):**
1. **A. Mohammadian & B. Tayfeh-Rezaie, "On a family of diamond-free strongly
   regular graphs", arXiv:1303.0473 (2013).**
   - Full: `research/sources/mohammadian-diamond-free-srg-ar5iv.full.md`
   - Summary + claim `diamond-free-srg-iff-pq-2602-grounding`:
     `research/summaries/mohammadian-diamond-free-srg-ar5iv.md`
   - Establishes: diamond-free SRG ⟺ PQ(s,t,μ) collinearity graph, primary
     source for the adopted `pq-2-6-2-classification` approach (which
     previously rested only on abstracts). Confirms srg(99,14,1,2) = PQ(2,6,2).
   - Bondarenko–Radchenko subfamily n∈{1,2,4} corroborated; the paper's g=k
     negative-Latin-square technique does NOT apply to 99.

2. **Christian Pech, "On highly regular strongly regular graphs", Algebraic
   Combinatorics 4 (2021) no. 5, pp. 843-878, doi 10.5802/alco.183**
   (open access).
   - Full: `research/sources/pech-highly-regular-alco.full.md`
   - Summary: `research/summaries/pech-highly-regular-alco.md`
   - Establishes: point graphs of partial quadrangles satisfy the 5-vertex
     condition (primary proof). Upgraded claim `bik-5vertex-holds-for-pq`
     from "asserted" to "sourced". Making 5-vertex a necessary condition on a
     hypothetical 99-graph.

**Claim updates:**
- `bik-5vertex-holds-for-pq`: status asserted → sourced (Pech primary in
  library), anchor extended.
- New claim `diamond-free-srg-iff-pq-2602-grounding` added.
- Both previously-open REQUESTS rows (`exact-list-prime-051a`,
  `published-mechanism-ruling-5cf8`) confirmed answered on disk by claims
  `wilbrink-order11-sourced` and `srg33-mechanism-answers-request`.

**A mis-download caught and corrected (the exact failure this role exists to
prevent):** fetched "Pech" at arXiv 2107.05747 — an UNRELATED ML paper
(SoftHebb). Files `pech-highly-regular-srg*.full.md` and their summaries are
now overwritten with CORRECTION notes pointing to the real Pech ALCO source,
so nobody reads arXiv:2107.05747 as the PQ paper. The correct Pech ALCO paper
was then downloaded from doi 10.5802/alco.183.

**Also tightened:** `sts-4vertex-two-families` note/claim now pins the exact
STS block-graph 4-vertex classification (PG(m,2) + AG(2,3), all rank-3 from
BIK §3.4) rather than the vague "two families" of the paywalled BLÖ abstract.

## Unheld / noted gaps (for REQUESTS, not urgent)
- Cameron's defining "Partial quadrangles" (1975) full text is paywalled and
  NOT held; now independently sourced via Mohammadian–Tayfeh-Rezaie's
  equivalent definition, so only needed if PQ(2,6,2) self-duality or a
  PQ-specific constraint is pursued.
- BLÖ 2012 full text remains paywalled; its exact content is now pinned by
  BIK §3.4 + Mohammadian–Tayfeh-Rezaie, so the gap is substantively closed.

## Verification note
- The PQ(2,6,2) parameter solve (s=2,t=6,μ=2 → v=99) and the diamond-free
  condition (λ+1|k, 2|14) are hand-verified arithmetic; a check script
  `code/out/check_pq_parameter_map.py` was written but NOT executed (no
  execution tool in this role) — executor should run it to confirm.
