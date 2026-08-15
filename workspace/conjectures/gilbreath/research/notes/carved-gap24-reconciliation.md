# R-carved-gap24 (and its restatements) are already settled by R-lipschitz-corner

## The statement

The current weakened rung being attacked (first-failure-ladder →
`R-carved-gap24-no-first-failure`, also `R-carved-gap24` in
recharge-ladder, `R-gaps-24` in spike-propagation-ladder):

> Let A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1 − 3 = 2, and
> x_{i+1} − x_i ∈ {2,4} for all i ≥ 1 (gaps after the first all 2 or 4).
> Then there is no first failure: A_k(1) ∈ {0,2} for all k ≥ 1
> (equivalently A_k(0) = 1 for all k).

## It is already a settled theorem in this run's own machinery

The run lists `R-lipschitz-corner` (gap-lipschitz-ladder) as **settled**:

> For a 2-then-odds sequence with first even gap g_1 = 2 and
> |g_i − g_{i+1}| ≤ 2 for all i ≥ 1 (the gap sequence is 1-Lipschitz),
> A_2 is the all-{0,2} corner, hence A_k(0) = 1 for every k ≥ 1.

A `{2,4}`-support gap sequence with first gap 2 **is** 1-Lipschitz:
each |g_i − g_{i+1}| with g_i, g_{i+1} ∈ {2,4} is 0 or 2, so ≤ 2.
So every sequence in the carved-{2,4} class lies in the domain of the
settled `R-lipschitz-corner`, which already concludes A_k(0)=1 ∀k.
The run's own index even says (under `R-gaps-24`): "subsumed by
gap-lipschitz-ladder's settled R-lipschitz-corner."

## The two-line proof, made explicit

With g_1 = x_1 − 3 = 2 and g_i ∈ {2,4} for i ≥ 2:

- A_1 = (1, 2, g_2, g_3, g_4, ...): since A_0 = (2,3,5,x_2,x_3,...), the
  first difference |2−3|=1, |3−5|=2, and |x_{j−1}−x_j| = g_j for j ≥ 2.
- A_2(0) = |1−2| = 1.
- A_2(1) = |2 − g_2| ∈ {0,2} since g_2 ∈ {2,4}.
- A_2(j) = |g_j − g_{j+1}| ∈ {0,2} for every j ≥ 2, since
  g_j, g_{j+1} ∈ {2,4}.

So row 2 is the corner (1, {0,2}, {0,2}, ...). By the proved closure
`closure-0d-double-edge` (a difference of two {0,2} entries is again in
{0,2}, and |1 − c| = 1 for c ∈ {0,2}), every later row begins with 1.
Hence A_k(1) ∈ {0,2} for all k ≥ 1 and there is no first failure.

**Concrete check** — gaps (2,4,2,4): A_0=(2,3,5,9,11,15),
A_1=(1,2,4,2,4), A_2=(1,2,2,2) = the corner. ✓ hand-verified.
This is the mechanism the run has already marked proved as claim
`sweep-corner-mechanism`: "row 2 is the corner state (1,{0,2},{0,2},...)
for every continuation; the corner state is closed under absolute
differencing, so such sequences satisfy the {0,2} property for all rows."

## What this means

The index is stale: `R-carved-gap24-no-first-failure` is marked **open**
and is "the current rung — attack this one", but it is already settled by
the run's own proved `R-lipschitz-corner` (or directly by the two-line
corner argument, a genuinely weaker theorem than Lipschitz). The run
should mark it settled and move to the next difficulty (one ≥6 gap in the
{2,4} stream), not spend budget re-deriving it.

```claim
id: carved-gap24-is-r-lipschitz-corner
statement: The weakened rung R-carved-gap24 (2-then-odds with first gap 2 and all later gaps in {2,4}) is already settled: A_1 = (1, 2, g_2, g_3, ...) with g_j ∈ {2,4}; A_2 = (1, |2−g_2|, |g_2−g_3|, |g_3−g_4|, ...) = (1, {0,2}, {0,2}, ...), because |2−g_2| ∈ {0,2} and every |g_j − g_{j+1}| ∈ {0,2}. So A_2 is the all-{0,2} corner, which is closed under absolute differencing (|1−c|=1 for c ∈ {0,2}; a difference of two {0,2} entries is again in {0,2}), hence A_k(1) ∈ {0,2} for all k and there is no first failure. The class is subsumed by the settled rung R-lipschitz-corner (a {2,4}-support gap sequence with first gap 2 is 1-Lipschitz in its gaps) and by claim sweep-corner-mechanism.
hypotheses: A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1−3 = 2, and x_{i+1}−x_i ∈ {2,4} for all i ≥ 1.
holds-here: yes
status: proved (two-line corner argument: the {2,4}-support and first-gap-2 conditions force A_2 to be the {0,2} corner for every continuation; hand-checked example gaps (2,4,2,4) → A_1=(1,2,4,2,4), A_2=(1,2,2,2))
bearing: the index must not mark R-carved-gap24-no-first-failure open — it is settled by R-lipschitz-corner / sweep-corner-mechanism; the next difficulty is a gap ≥ 6 entering the {2,4} stream.
anchor: research/notes/carved-gap24-reconciliation.md; claims sweep-corner-mechanism, R-lipschitz-corner (gap-lipschitz-ladder)
contradicts: none
```
