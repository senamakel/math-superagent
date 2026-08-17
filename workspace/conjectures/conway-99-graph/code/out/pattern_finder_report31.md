# Pattern-finder report — round 31: the 84-vertex pair-labeling gate (control-clean) and the s-determinism census

## What this round did

Ran the adopted 84-vertex pair-labeling reduction's admissibility gate on both
controls, found the on-disk gate's inner-rule "16/4840 violations" to be a code
bug, fixed it, and confirmed **ALL rules hold on both controls at all roots**.
Then quantified how much of the residual outer graph H is forced: H is
**s-determined** on rook(3) but **not** on BvLS, so the reduction leaves genuine
free structure at the 84-vertex (k=14) object rather than collapsing to a unique
candidate.

## Results (exact integer arithmetic)

### 1. The pair-labeling gate passes on both controls once the inner rule is counted correctly

On-disk `research_pair_label_gate.py` reported `inner-viol=16` (rook, k=4,
4 outer) and `inner-viol=4840` (bvls, k=22, 220 outer) at every root. Inspection
found the count bug: `cont = sum(t in outer if A[a,t] and t in pu)` with `pu`
the **pair-label** (a 2-subset of the neighbour set N). `t` is an **outer
vertex**, which is never an element of `pu`, so `t in pu` is always False and
`cont` is identically 0 — forcing a violation on every (a,u) pair: exactly
`k·M` of them (4·4=16, 22·220=4840). The intended count is outer vertices
adjacent to `u` **whose label contains `a`**.

`pair_label_gate_corrected.py` (intended semantics) reports, on rook(3) and
bvls_graph(), at every root (0, 1, n/2, n-1):

    edge-viol=0 nonedge-viol=0 inner-viol=0 => ALL RULES HOLD

So the adopted 84-vertex pair-labeling reduction is **control-safe**: its
edge/nonedge/inner pair-rules reproduce the true outer graphs of both existing
family members exactly. The on-disk gate's "16/4840 VIOLATIONS" was a
non-result (bug), and must not be cited as a failure of the reduction.
Capture: `code/out/pair_label_gate_corrected.captured.txt`.

### 2. Outer graph H is s-determined on rook(3), not on BvLS

Let s = |P_u ∩ P_w| ∈ {0,1} for two outer vertices (no two non-matching pairs
share 2 elements). Question: is outer adjacency a **pure function of s**?

| control | s=0 adjacencies present | s=1 adjacencies present | s-determined? |
|---|---|---|---|
| rook(3), k=4, M=4 | {0} | {1} | **PURE** (edge ⇔ s=1) |
| bvls, k=22, M=220 | {0,1} | {0,1} | **NOT** (real freedom) |

Every root agrees. rook(3)'s H is so small it is fully s-determined (s=0 →
nonedge, s=1 → edge, matching the observed densities 0% and 100%). bvls's H is
definitively **not** s-determined: pairs sharing 0 elements are sometimes
adjacent, sometimes not, and likewise for s=1 (so the pair-rule forces the
counts but not the individual adjacencies — the residual H carries genuinely
free structure). By the reduction this free structure is what must be saturated
at 99 too; the rule is a constraint, not a unique-specification. This is the
first clean, control-checked statement of how much of H the reduction leaves
free. Capture: `code/out/pair_label_census.captured.txt`,
`code/out/pair_label_sdetermined.captured.txt`.

### 3. Closed-form s-sharing of the non-matching pairs (exact, all five members)

For K(k) minus a perfect matching, M = C(k,2) − k/2 non-matching pairs, the
unordered pair-pair counts by s = |P∩P'| are:

    s=1: M·(k−3)
    s=0: M·(M−1−2(k−3))/2

Exact for every feasible k (4,14,22,112,994), checked against the identity
s0+s1 = M(M−1)/2:

| k | M | s=0 pair-pairs | s=1 pair-pairs |
|---|---|---|---|
| 4 | 4 | 2 | 4 |
| 14 | 84 | 2562 | 924 |
| 22 | 220 | 19910 | 4180 |
| 112 | 6160 | 18298280 | 671440 |
| 994 | 493024 | 121047498992 | 488586784 |

At k=14 (the 99-graph object) there are 84 non-matching pairs — labelled,
3586 unordered pair-relations total of which 924 have s=1 and 2562 have s=0.
OEIS lookups on the family sequences `[4,84,220,6160,493024]` and
`[2,2562,19910,18298280,121047498992]` both return **no match** (distinct
misses, recorded — no external closed form to surface).

## Verdict (sequence line)

This round did not turn up any new integer sequence with separating power for
srg(99,14,1,2): the s-sharing counts and the "free" outer-adjacency degrees are
parameter-deterministic (they follow from (n,k) and the pair-labeling alone),
so they hold identically for rook(3) and BvLS and cannot distinguish 99 from
them — confirming the standing catalogue verdict (rounds 1–30) that every
sequence this run produces is parameter-determined, an OEIS miss, or a
mechanism trace. What is genuinely new this round is *qualitative, not
sequential*: (a) the on-disk gate's inner-rule failure is a bug and the
reduction is control-clean; (b) H carries real unforced freedom (not s-
determined) at the 84-vertex object, so the 84-vertex CP-SAT that saturates it
has genuine (not trivial) search content. No structural conjecture is being
promoted out of the scratch, because the two s-determinism facts survive their
controls but are parameter-determined in the standing sense.

## Files

- `code/out/pair_label_gate_corrected.py` / `.captured.txt` — control-clean gate.
- `code/out/pair_label_census.py` / `.captured.txt` — H degree/density by s.
- `code/out/pair_label_sdetermined.py` / `.captured.txt` — s-determinism + closed-form s-sharing.
