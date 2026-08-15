# REFUTED: G-threshold-analysis — the universal inequality fails, unconditionally

## Attack target

`G-threshold-analysis` (skeleton `bipartite-threshold-shadow`), status was `open`:

> Let `U_d(a)` be the extremal upper bound from G2. There is `d₀(n) = ω(log n)`
> such that `U_{d₀(n)}(a) ≤ 2^{n-1} − a` for all `0 ≤ a ≤ 2^{n-1}`.

This is the gap G3 that, with G1's contrapositive (`if |O_{≤d₀}(A)| ≤ 2^{n-1}-|A|`
for every A ⊆ E then f(n) ≥ d₀+1), was meant to deliver `f(n) = ω(log n)`.

## The refutation — singleton failure, exact, independent of G2

Take any even vertex `a ∈ E` and let `A = {a}`, so `|A| = 1` (the `a=1` case,
which G3 quantifies over). The even vertex `a` has exactly `n` odd neighbours,
each with exactly 1 neighbour in `A`; every other odd vertex has 0. Hence for
every `d ≥ 1`:

```
|O_{≤d}(A)| = 2^{n-1}      (all odd vertices have ≤ 1 neighbour in the singleton)
```

but the inequality G3/G1 requires

```
|O_{≤d}(A)| ≤ 2^{n-1} − |A| = 2^{n-1} − 1.
```

Since `2^{n-1} > 2^{n-1} − 1`, the universal inequality **fails at a=1 for every
`d ≥ 1`**, for every `n`. (For `d=0` it holds, but `d₀(n)=0` is not `ω(log n)`.)
So no `d₀(n) ≥ 1` — hence no `d₀(n) = ω(log n)` — can satisfy G3 as stated.

This refutation is **independent of G2** (the Hamming-ball extremal lemma,
already refuted in `code/refute/threshold_shadow_refuted.md`): it uses only the
definition of `O_{≤d}(A)` and the singleton `A={a}`, no extremal-family claim.

## Consistent with the skeleton's own hand check

The skeleton's sanity check for n=3 already found this boundary and wrote it
down honestly — "at d=1 the universal inequality holds for a∈{0,2,3,4} and
fails only at a=1: A={000} has O_{≤1}(A)=O, of size 4 > 3". This is exactly the
a=1 failure. The skeleton reads it as "the contrapositive declines to prove
f(3)≥2"; the stronger and decisive reading is that the a=1 failure blocks the
contrapositive for **every** d₀≥1, so G3 cannot supply any d₀(n)=ω(log n).

## Not a singleton-only artifact — a=2 fails for n=4 too

`A={0000,1111}` (the antipodal even pair from the G2 refutation) has every odd
vertex at distance 1 from exactly one of them, so `|O_{≤1}(A)| = 8 = 2^{3}`
while `2^{3} − |A| = 6 < 8`. The failure is not confined to a degenerate
boundary set; it reflects the true geometry that a *spread/antipodal* A
maximises the threshold shadow, which is exactly the reason G2's ball claim was
already dead.

## Machine evidence

`code/refute/threshold_analysis.p` → `find_counterexample`: **refuted**
(CounterSatisfiable) on a faithful 4-element domain (v00,v01,v10,v11 distinct):
`a(v00)` only (`|A|=1`), both odd vertices `inO1(v01) ∧ inO1(v10)` (so
`|O_{≤1}(A)|=2`), and the conjecture "the inequality holds at a=1,d=1", i.e.
`¬(inO1(v01) ∧ inO1(v10))`, is falsified. The hand computation above is exact
and needs no search.

```claim
id: threshold-analysis-singleton-refutes-G3
statement: The inequality |O_{<=d}(A)| <= 2^{n-1} - |A| fails at the singleton
  A={a} (a in E, |A|=1) for every d >= 1 and every n: |O_{<=d}({a})| = 2^{n-1}
  while the bound is 2^{n-1}-1. Hence no d0(n) >= 1, in particular no
  d0(n) = omega(log n), satisfies G-threshold-analysis as stated (which
  quantifies over all 0 <= a <= 2^{n-1}). Also fails at a=2 for n=4 via the
  antipodal pair.
hypotheses: Q_n, E=even/O=odd halves of size 2^{n-1}; O_{<=d}(A) =
  {x in O : |N(x) cap A| <= d}; G3 demands U_d(a) <= 2^{n-1}-a for all a.
holds-here: yes — this is exactly G3's quantification range.
status: checked (hand computation, exact; singleton a has n odd neighbours at
  distance 1, all others at distance >= 3, so every odd vertex has <=1 neighbour
  in {a}, giving |O_{<=d}({a})|=2^{n-1} for all d>=1). Confirmed by
  find_counterexample on code/refute/threshold_analysis.p (CounterSatisfiable).
bearing: kills G-threshold-analysis as stated, INDEPENDENTLY of G2. Shows the
  G1 contrapositive premise fails for every d0>=1 at the a=1 boundary, so the
  bipartite-threshold-shadow route (G1->G2->G3) cannot exceed f(n)>=1. Does NOT
  refute the main goal f(n)=omega(log n) (which the spectral/Huang route
  establishes at sqrt(n)); it refutes this particular decomposition's G3.
falsifies: the lemma G-threshold-analysis in its current formulation (a d0(n)=
  omega(log n) satisfying U_{d0}(a) <= 2^{n-1}-a for all 0<=a<=2^{n-1}).
anchor: code/refute/threshold_analysis.p, code/refute/threshold_analysis.py
```

## Bearing on the skeleton

G1's contrapositive is a *sufficient* route to a lower bound: if it were
satisfied for `d₀` it would give `f(n) ≥ d₀+1`. The a=1 failure shows the
premise is **not** met for any `d₀ ≥ 1`, so this particular sufficient condition
cannot fire at superlogarithmic level. The route does not produce a false bound
— it produces no useful bound. This is a genuine obstruction specific to this
skeleton's decomposition, located exactly, and it is independent of the G2
extremal-family question.
