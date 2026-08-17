# Second-subconstituent nullity at μ=2 — a λ=1,μ=2-specific structural fact

Round 32 of the sequence/regularity line. This completes interrupted work: the
`pattern_subconstituent_spectrum*`, `pattern_nullity_*`, `pattern_kernel_*`,
`pattern_h_parameters*` files were written (timestamps 07:19–07:47) but had NO
captures and NO report. This note re-derives and verifies them cleanly.

## Setup

Fix vertex 0 of an srg(v,k,λ,μ). The **second subconstituent** H is the induced
graph on the m = v−k−1 = k(k−λ−1)/μ non-neighbours of 0. Each outer u carries a
**pair-label** P_u = N(u)∩N(0), of size μ.

## Proven fact (this round, exact integer arithmetic) — nullity = k/2 at μ=2

For each **matched edge** {a,a′} of N(0)=7K₂ (λ=1 ⇒ N(0) is a perfect matching),
define the vector on the outer vertices by

    x^{a,a′}_u = [a ∈ P_u] − [a′ ∈ P_u].

Then **H x^{a,a′} = 0 exactly**, and the k/2 = 7 such vectors are linearly
independent. Verified:

| graph | (v,k,λ,μ) | m | nullity(H) | k/2 | all kernel | rank | non-matched fail |
|---|---|---|---|---|---|---|---|
| rook(3) | (9,4,1,2) | 4 | 2 | 2 | ✓ | 2 | 0/4 (all vanish, kernel degenerate) |
| bvls | (243,22,1,2) | 220 | 11 | 11 | ✓ | 11 | 220/220 fail |
| doily | (15,6,1,3) | 8 | 0 | 3 | ✗ | — | μ≠2: no 0-eig |
| GQ(2,4) | (27,10,1,5) | 16 | 0 | 5 | ✗ | — | μ≠2: no 0-eig |

So the kernel construction is **specific to λ=1, μ=2**: it needs N(0) to be a
matching (λ=1) and the pair-labels to be 2-sets with the μ=2 common-neighbour
count. On bvls the matched-pair span is the **whole** 0-eigenspace (non-matched
pairs all fail); on rook the kernel is small and degenerate (all six 2-subsets
vanish, only 2 independent).

## H x = 0 is verified; but the sets are NOT equal — only the counts are

(Hx)_w = Σ_{u outer, u~w} ([a~u] − [a′~u]) = |A_w| − |A′_w| where
A_w = {u outer: u~a, u~w}, A′_w = {u outer: u~a′, u~w}.

The exact check `pf_second_subconstituent_proof_check.py` proves that on bvls
**A_w ≠ A′_w as sets** (membership differs on nearly every outer w), while
**|A_w| = |A′_w| always** (every one of the 11×220 (matched-pair, outer-w)
combinations has equal cardinality, values 1 or 2). Hence (Hx)_w = 0 for every
outer w. This is exactly the empirical Hx=0; the earlier draft over-claimed
set-equality as a "closed-form proof" — retracted. A genuine proof would have to
be a cardinality/case argument, not given here; only the exact computation
stands. (For rook, Hx=0 also holds, and there all six 2-subsets vanish — the
kernel is degenerate so the matched-pair phenomenon is not observable purely
from the vector identity.)

**Consequence: nullity(H) ≥ k/2 for every srg(v,k,1,2)** — parameter-determined
at the (λ=1,μ=2) subfamily, so it holds identically on rook and bvls and would
hold on 99. **No separating power for srg(99,14,1,2); not a route.**

## Conjecture (2 data points, not parameter-proven)

nullity(H) = k/2 **exactly** (observed: rook 2, bvls 11). The lower bound is
proven, the equality is not derivable from the above. Falsifying term: a μ=2,
λ=1 SRG whose second subconstituent has nullity ≠ k/2. The μ=2 λ=1 family is
{rook, 99 (open), bvls} — only the two controls exist, so there is **no further
test case**. The concrete prediction is: *if srg(99,14,1,2) exists, its 84-vertex
second subconstituent has nullity exactly 7* (zero-eigenvalue multiplicity 7,
rank 77). This is a genuine 99-specific claim, but it is a conjecture on 2
points and cannot currently be tested or derived.

## Verdict

- The kernel-vector identity is a **proven, parameter-determined** structural fact
  (new to the catalogue, which covered triangles/coclique/distance-2/pentagons/
  hexagons/ic4/rank/SNF/s-sharing but not this). It is exact and safe to cite.
- It does **not** separate 99 from controls (holds identically on both). Only the
  nullity-=k/2 equality is a live 99-relevant conjecture, and it is weak.

## Files
- `code/out/pf_second_subconstituent_nullity.py` (+ capture) — consolidated exact verification.
- `code/out/pf_second_subconstituent_matched_only.py` (+ capture) — matched-vs-nonmatched.
- `code/out/pf_second_subconstituent_nullity.py` is the anchor.
