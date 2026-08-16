# Pattern-finder final report

Role: pattern-recognition specialist. Findings below are **conjectures / exact
measurements**, never proofs — labeled per claim. All numerics are exact
integer/ratio arithmetic of the SOS fold (`lib.supply_fold.s_sos`, verified vs
the brute submask-XOR oracle on n=4..60 and reproducing problem.md's
`ν₂(4000)/4000`).

## The one exploitable regularity

**The primes sit in the generic-good class of the Lucas/submask fold: the
fold-cell density `ν₂(n)/(n−2)` is ≈ 1/2, and the deviation `S(n)` is
`o(n)` at √n scale.**

```
input          mean fold-density (last half, N=1500)
primes         0.5004
random iid     0.4997
random p=0.15  0.4844
Thue-Morse     0.0666   ← collapses
```

- `S(n)=Σ_{d=2}^{n-1}(−1)^{T(n,d)}`, `ν₂(n)=(n−2−S(n))/2`.
- `|S(n)| ≤ 3.8√n` uniformly over [300,4000], max ratio 3.748; survives to
  N=6000. Identical for random iid h (3.99).
- `std(S(n))/√n ≈ 1.0` constant over every 500-bin (300..4000) — CLT-like.
- `S` is **mean-reverting** (oscillates near 0), not a growing random walk:
  increments `S(n+1)−S(n)` have std ~65 (many values), yet |S| stays √n-scale.
- Density-1 tail shape is exact: nu2/n<c has constant violating count as
  N grows (c=0.40:1, c=0.42:6, c=0.45:40; all bounded max n) → tail density 0.

## The key negative result (controls)

The √n/CLT bound is **fold-generic, not prime arithmetic.** Random iid h gives
the same bound. So this does NOT by itself prove SUPPLY for the primes; it
shows the primes are *unstructured enough* for the fold to behave generically,
which is the missing arithmetic input.

## Collapse is driven by near-kernel sparsity, not automaticity

Random 1-density ≤0.15 collapses (|S|/n ~0.4–0.84); ≥0.2 is good (≤0.23).
Near-kernel strings (single 1 → 0.99, rare defect → 0.996, all-zero = kernel)
collapse. The prime gap-parity string has balanced 1-density ~0.585 (stable,
N≤20000), comfortably in the good regime. This corrects an earlier "2-automatic
collapse" framing.

## No other exploitable structure survived

- No constant-coefficient linear recurrence on `S(n)` (order ≤6, 100 terms) or
  `ν₂(n)` (order ≤8, 56 terms); not polynomial. Both uncatalogued in OEIS.
- Residual autocorrelation of `ν₂/n` is NOT primes-specific — it is a
  fold-generic artifact (detrending kills the long-lag tail; random h shows the
  same short-lag persistence).
- Variance of `ν₂/n` over [N/2,N) decays ~N^-1 (ideal Chebyshev rate) — the
  cleanest rate for the averaged form.

## What this means for the goal

SUPPLY (`ν₂(n) ≥ c·n`, any c<1/2) reduces, via `ν₂=(n−2−S)/2`, to a
**second-moment bound on the submask-XOR transforms of the prime gap-parity
string**: prove `|S(n)| = o(n)` (plausibly `O(√n)`), i.e. `var(S(n)) = o(n²)`.
The √n behavior is empirically the generic fold outcome on balanced input, so
the input needed is a balanced-density / mixing-type statement about `h` that
is **weaker than positive mod-4 switch density** (which needs specific
correlation structure, not just balanced density). This is the concrete open
gap this run hands forward (GOAL priority 4 / G-var / G-weak-input).

## Honest status

Everything here is exact measurement over n ≤ 6000 (and n ≤ 20,000 for the
1-density of h). None is a proof for all n. The √n bound on S(n) for the
primes is a conjecture derived from data that survived: (a) reproduction of
problem.md's 0.4933 ratio, (b) the random-SAME-fold control showing it is a
generic rather than arithmetic fact, (c) the collapse-into-Thue-Morse negative
control showing the fold can distinguish good from bad input. What found the
contradiction to the arithmetic interpretation: the identical random bound.
What would falsify the "generic-good" reading: a structured (e.g. 2-automatic)
h with 1-density ≥0.3 that collapses — not found in the controls tested.
