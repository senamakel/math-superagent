# Refutation report — R-k-interior (and the R-one-interior handoff)

Refuter verdict on the weakened rung `R-k-interior`
(`code/refute/r-k-interior-n4-k2.p`), taking over where
`r-one-interior-refutation2.md` left off.

## Statement attacked

`R-k-interior` (research/weakened/es-conjecture.md): *For every n >= 4 and
every fixed k >= 0, every set of 2^(n-2)+1 points in general position with
at most k interior points contains n points in convex position.*

## Structural observation that dominates the refutation

**`R-k-interior` is not a genuine weakening of the conjecture.** The
conjecture ES(n) = 2^(n-2)+1 asserts that *every* set of 2^(n-2)+1 points
contains n in convex position, regardless of how many are interior. Adding
"with at most k interior points" introduces a hypothesis that, if the
conjecture is true, is *satisfied by every set* and changes nothing. So for a
fixed n, `R-k-interior` is **logically equivalent to ES(n) <= 2^(n-2)+1** for
every k:

    R-k-interior(n,k)  <=>  ES(n) <= 2^(n-2)+1.

Consequently the interior-count bound k is a red herring as far as truth goes:
the threshold does not move with k. The one regime where the trivial
hull-count argument dies (k > 2^(n-2)+1-n, i.e. fewer hull vertices than n)
is *still* covered by the full value ES(n), so it is not a first open case
of this rung — it is simply ES(n) stated in a subclass.

(What the weakened-target ladder seems to want — "admit k interior points and
induct on k" — is a *proof strategy* for the conjecture, not a separate
statement. The ladder row `R-one-interior`'s merge text already said as much;
this confirms the content belongs in `R-k-interior` and is the conjecture.)

## Machine-checked instances

Because R-k-interior(n,k) <=> ES(n) <= 2^(n-2)+1, every small n is an already
established value in this library (claim `es-exact-values`):
ES(3)=3, ES(4)=5, ES(5)=9, ES(6)=17. So **no small counterexample exists**:
a counterexample at n=4,5,6 would contradict a verified value, and n>=7 is
beyond any model search the tools can reach.

New machine check performed here, the **hardest small case of the rung**:

- **`code/refute/r-one-interior-n4.p`** (previous, n=4, k=1): SZS **Theorem**.
- **`code/refute/r-k-interior-n4-k2.p`** (this run, n=4, **k=2** — the maximum
  interior count for 5 points, so the hull is a triangle and the trivial
  hull-count argument *dies*): SZS **Theorem** from these axioms
  (points-distinct, ccw-total/total-antisymmetric per triple, ccw-cyclic,
  inside-def, interior-def via Caratheodory, at-most-two-interior,
  convex4-def via the 4-point criterion). This is exactly ES(4)=5 stated in
  its worst subclass, and the result is **proved from the axioms** — it
  agrees with the established value.

So the verdict on every small, tool-reachable instance of `R-k-interior` is
**proved**, and this is expected: they are the settled values ES(4..6).

## What would actually be falsifiable

The *first* genuinely open instance of the underlying statement is **n=7**
(ES(7) is open; the conjecture predicts 33). R-k-interior(7,k) for the hard
regime k > 33-7=26 is exactly "ES(7) <= 33", which is beyond any finite-model
search reachable here (32 order types are astronomically many; Peters–Szekeres
needed bespoke SAT for 17 points). So:

- No counterexample, and none is searched-for at full size: the search space
  for n>=7 is the order of the conjecture itself, and the tools here cannot
  touch it.
- Sizes covered: the full CC fragment at 5 points (n=4, both k=1 and k=2),
  returning SZS Theorem.

An honest note on scope: this refutation is *weaker than it looks*, because
the whole rung is equivalent to the conjecture. "Proved from these axioms for
n=4" says nothing about n>=7.

## Traps checked

- The abstract-chirotope trap (a non-realizable abstract model "refuting" a
  real statement). Not triggered: the n=4 results are SZS Theorem, and the
  established value ES(4)=5 independently rules out any real counterexample.
- Not a weakening of the axioms to hunt a model: the at-most-interior axiom
  was set at its *maximum* (k=2), which is the most hostile, not weakest,
  instance.

## Recommended next refutation target

Not `R-k-interior` k>=2 at n=5/k=5 (that is ES(5)=9, already true). The only
remaining tool-reachable refutation surface is the **sampled structural claims
about `es_construct`** (e.g. the n=8 triangular block-pattern classes,
`refute/pattern_triangular_n8_attack.py`), which are *new* claims of this
run's own, not settled values, and so genuinely falsifiable — flagged in
`r-one-interior-refutation2.md` as the most-likely-false finding.
