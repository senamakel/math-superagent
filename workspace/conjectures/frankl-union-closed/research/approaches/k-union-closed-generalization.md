# k-union-closed generalization of the entropy barrier

## Idea / question

Ho's generalized Boppana inequality (arXiv:2601.19327) and Yuster's conjecture
give a family of constants `c_k = α_k/(1+α_k)` for approximate `k`-union-closed
systems, generalising the iid entropy barrier `(3−√5)/2 ≈ 0.38197` which is
exactly the `k=2` case. The natural question: does going to larger `k` (a
`k`-union-closed attack) give a *stronger* constant, i.e. certify an element
density above `(3−√5)/2`?

## Status: refuted (as a route to a stronger constant)

The constants are **strictly decreasing in k**, and `c_2` is the maximum.

**Exact proof** (not a numeric fit). Let `c_k` be the unique root in `(0,1)` of
`(1−x)^k = x`. The function `f_k(x) = (1−x)^k − x` is strictly decreasing on
`[0,1]` since `f'_k(x) = −k(1−x)^{k−1} − 1 < 0`. At `x = c_k` (so
`(1−c_k)^k = c_k`),

```
f_{k+1}(c_k) = (1−c_k)^{k+1} − c_k
             = (1−c_k)^k(1−c_k) − c_k
             = c_k(1−c_k) − c_k   = −c_k² < 0,
```

while `f_{k+1}(0) = 1 > 0`. By continuity and strict monotonicity the unique
root `c_{k+1}` of `f_{k+1}` lies in `(0, c_k)`. So `c_{k+1} < c_k` strictly for
every k ≥ 2, and by induction `c_2 > c_3 > c_4 > …`.

Numerically confirmed for k through 59 (every step `c_{k+1} < c_k`), and
`c_2 ≈ 0.38197 =(3−√5)/2 > c_k` for all k ≥ 3 checked through k = 148.

**Consequence.** The k=2 (iid, Boppana) entropy barrier `(3−√5)/2` is the
**strongest** of the whole Ho/Yuster generalized family. A `k`-union-closed
attack for any k > 2 certifies a strictly *smaller* element density and can
never improve the `(3−√5)/2` cap. The naive "raise k to beat the barrier"
generalization is closed as a route.

**Asymptotic (context).** `c_k ~ W(k)/k` where `W` is the Lambert W function
(numerically `c_k/(W(k)/k) → 1`, e.g. 0.987 at k=100), and `c_k → 0`; so the
constants get *arbitrarily weak* as k grows. Only a genuinely different
coupling — the *dependent* coupling (Sawin/Yu/Cambie → ~0.38234) — escapes the
iid `(3−√5)/2` cap, consistent with the `iid-barrier-exact` scope note.

## What would falsify

An `k ≥ 2` with `c_{k+1} ≥ c_k`, i.e. `f_{k+1}(c_k) ≥ 0`; the exact algebra
above shows `f_{k+1}(c_k) = −c_k² < 0` for every `k`, so the decrease is a
theorem, not a conjecture. There is no counterexample to the decrease. What
*would* falsify the reading "k-generalization is a dead end" is a dependent
coupling (not the iid/Ho family at all) that beats `(3−√5)/2`; that is a
separate, live direction.
