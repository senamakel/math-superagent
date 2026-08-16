# A Forced-Structure Reduction and Verifiable Bounds for Conway's 99-Graph — summary

Source: https://arxiv.org/html/2608.11211v1 (full text at
`research/sources/forced-structure-reduction-conway99.full.md`)

**Status: unverified AI-agent preprint** (Conference for AI Scientists 2026
track). It does **not** claim to settle existence. It reports verifiable partial
results relevant to this run's live threads (`g-reduce` / forced-structure
reduction, and the `Z_7` prescribed-automorphism sub-case). Treat any number it
reports as a *lead* to reproduce, not a fact.

## What it establishes (their claims, to verify)

1. **Circulant ceiling (Prop 1, exhaustive):** no circulant on Z/99Z (14
   connection set, symmetric) satisfies more than 33/49 difference-classes,
   i.e. score 3366/4950 = 68.0%. Verified by complete enumeration over
   C(49,7) = 85,900,584 connection sets (batched FFT autocorrelation, ~100 s).
   Best set S = {±1,±2,±4,±15,±27,±36,±45}. The other abelian group of order 99
   (Z3×Z3×Z11) attains the same 33/49. A perfect circulant would be a
   (99,14,1,2) partial difference set, already known not to exist.

2. **Forced-structure reduction (Section 4) — *independently confirms the
   run's own derived-design-at-a-vertex result*:** fix vertex 0, N(0) a perfect
   matching (7K2). μ=2 forces every outer vertex to have exactly two neighbours
   in N(0) and to be in bijection with the non-matched pairs of N(0). So
   inner–outer adjacency is entirely forced; the sole unknown is the
   outer–outer graph, which is (k−2)-regular on M = C(k,2) − k/2 vertices.
   For (99,14,1,2): a **12-regular graph on 84 vertices**. Encoded for CP-SAT
   with lex-leader symmetry breaking over the group of order 2^7·7! = 645,120;
   379,987 Booleans, 761,221 constraints. Pipeline validated by recovering the
   unique srg(9,4,1,2) in milliseconds; for (99,14,1,2) it neither returns a
   graph nor exhausts (expected for an open problem). **Cross-check this
   against the run's `research/backward/derived-design-at-a-vertex.md` — the
   run has the same reduction and additionally found (checked) that the outer
   design's *collinearity graph* is not itself an srg(*,*,1,2).**

3. **Prescribed-automorphism orbit-existence encoding (Section 5):** a clean
   block-circulant/orbit model for a prescribed automorphism of order p,
   validated by re-verifying srg(9,4,1,2) (fixed-point-free Z3 and order-2 with
   one fixed point) and Paley srg(13,6,2,3) (order-3, one fixed point). Then
   attacked the genuinely open single-fixed-point **Z_7** case (minimal
   admissible order-7 action: 14 orbits of size 7 + 1 fixed vertex): CP-SAT
   returns unknown after 48h on 14 cores, neither building the graph nor
   proving infeasibility. Fixed-point-free Z_3 (33 orbits) likewise unknown
   within 1800s. Honest negative finding: off-the-shelf CP-SAT does not decide
   even these open sub-cases — a structural barrier attributed to general-
   purpose encodings, motivating specialised orbit-matrix + eigenvalue-
   interlacing machinery. **This matches the run's claims: order 7 gives Z_7
   (Cesarz-Woldar), and Z7-symmetry existence is itself open; the run's
   automorphism-orders ledger lists no Z_7 exclusion.**

4. **Heuristic frontier (Section 6):** best verified artifact 3437/4950 =
   69.43%; fourteen methods converge to 68.0–69.43%; frontier is a strict
   local optimum, not a tuning artifact. A score of 4950 *is* an
   srg(99,14,1,2); a *provable* upper bound below 4950 would be a
   non-existence proof; no such bound is claimed.

## Why it matters here

- Section 4 is the only independent published account (in this library) of the
  forced-structure reduction to a 12-regular graph on 84 vertices — the run's
  own g-reduce thread computed this reduction and its checked negative on the
  recursion, so this source supplies external confirmation (and the exact
  label-derived λ/μ conditions on the outer graph).
- Section 5 documents the empirical fate of the Z_7 prescribed-automorphism
  sub-case, which the run's automorphism thread identifies as the open rung
  (G ≅ Z_7 is not excluded).
- It is a *preprint by an AI agent*, not peer-reviewed; its exhaustive circulant
  bound and validation claims are reproducible but not yet independently checked
  in this run's `code/out/`. Log as a lead.

Claim filed: `forced-structure-reduction-conway99` (unchecked / asserted-by-
source).
