# Pair-labeling 84-vertex reduction: control gate + s-determinism (round 31)

## The gate is control-clean once the inner rule is counted correctly

The on-disk `research_pair_label_gate.py` reports inner-rule violations on both
controls (16 on rook(3), 4840 on bvls). **This is a code bug, not a
refutation** of the reduction. The offending line is

    cont = sum(t in outer if A[a,t] and t in pu)

where `pu` is the pair-label (a 2-subset of the neighbour set N). `t` iterates
**outer vertices**, which are never elements of `pu`, so `t in pu` is always
False and `cont` is identically 0 — forcing a violation for every (a,u) pair,
exactly k·M of them (4·4 = 16, 22·220 = 4840). The intended count is outer
neighbours of u whose **label** contains a.

`pair_label_gate_corrected.py` implements the intended semantics
(`cont = #{t outer: A[u,t] and a in label(t)}`, want = 1 if a ∈ label(u) else
2 − [mate(a) ∈ label(u)]). Result on both controls, at all four roots
(0, 1, n/2, n-1), exact integer arithmetic:

    rook(3)  : edge-viol=0 nonedge-viol=0 inner-viol=0 => ALL RULES HOLD
    bvls     : edge-viol=0 nonedge-viol=0 inner-viol=0 => ALL RULES HOLD

So the adopted pair-labeling reduction (fix 0, N(0)=7K2, 84 distance-2 vertices
labelled by non-matching pairs of the 14-set, residual free graph H on 84
vertices) passes its admissibility gate on BOTH existing family members. The
on-disk gate's violations must not be cited as evidence against the reduction.

## s-determinism: rook pure, bvls not — H carries real freedom

s = |P_u ∩ P_w| ∈ {0,1}. Outer adjacency as a function of s:

- rook(3): s=0 → {0} (always nonedge), s=1 → {1} (always edge). **PURE**.
- bvls:    s=0 → {0,1}, s=1 → {0,1}. **NOT s-determined** — real freedom.

Every root agrees. The pair-rule fixes the counts but not the individual
adjacencies at k=22; hence at 99 the residual H is a genuinely under-determined
12-regular object on 84 vertices, which is exactly the object the 84-vertex
CP-SAT is meant to saturate. This is not a contradiction and not a new
sequence — it is a control-checked statement of how much of H the reduction
leaves free (qualitative, not sequential).

## Closed-form s-sharing (parameter-deterministic, all five members)

M = C(k,2) − k/2 non-matching pairs of K(k)-minus-matching:
    s=1 pair-pairs = M·(k−3);  s=0 = M·(M−1−2(k−3))/2.
k=14: M=84, s0=2562, s1=924 pair-pairs. Both family sequences are OEIS misses.
Parameter-determined — holds for both controls, no 99-vs-243 separating power.

## Status

The gate result and s-determinism facts are checked (exact, both controls at
four roots). No conjecture promoted: both facts are parameter-determined in the
standing sense. Scratch was unavailable (memory index down) so this note carries
the finding on disk.
