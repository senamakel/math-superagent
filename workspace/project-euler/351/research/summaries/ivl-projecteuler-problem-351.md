# IVL Project Euler 351 — "Hexagonal Orchards" (solution write-up, 25% difficulty)

Source: https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-351 — full text at
`research/sources/ivl-projecteuler-problem-351.full.md`
[[ivl-projecteuler-problem-351.full]]

## What this source establishes

A public solution write-up for PE 351 (author anonymous, IVL collection). Read
in full this session.

**The method (identical to this run's).** Consider one sixth of the hexagon and
multiply by 6. In one sector, the points of the n-th layer represent the angles
x/n, 1 ≤ x ≤ n; a point is hidden iff gcd(x, n) > 1 (the fraction x/n is not
reduced, so a closer point with the same angle exists). On layer n, φ(n) of the
n points have gcd(x,n) = 1, so n − φ(n) are hidden; hence

    H(n) = 6·Σ_{i=1..n}(i − φ(i)) = 6·(n(n+1)/2 − Φ(n)).

**The computation.** The author first evaluated the summatory totient with a
Möbius sieve (~85 s), then implemented "algorithm 6" of the official PE 351
overview PDF (a sublinear Totient Summatory Function evaluation) and dropped the
runtime to ~1 s, adding it to his `mathslib` Python package
(`mathslib.numtheory.mobius_k_sieve`).

## What it implies for this run

A second independent public confirmation (with Brumme) that the six-sector /
φ-per-layer derivation and the closed form H(n) = 6·(T(n) − Φ(n)) are the
standard solution, and that the sublinear Φ-evaluation is the standard fast
route. The page does not print the final integer H(10⁸), so it is not an answer
source; it corroborates `hexagonal-orchard-closed-form` and the
`summatory-totient-mobius-identity` route (the same Möbius identity the run's
`verify_mobius.py` uses). It also corroborates the optional fourth route
(`research/approaches/dirichlet-hyperbola-gauss-2-3.md`, Θ(n^{2/3})): the
official overview's "algorithm 6" is that same floor-grouped summatory-totient
evaluation.

```claim
id: pe351-ivl-standard-method
statement: A second public PE 351 write-up (IVL) uses the same six-sector derivation:
layer n has n points with angles x/n, hidden iff gcd(x,n) > 1, so
H(n) = 6*sum_{i<=n}(i - phi(i)) = 6*(n(n+1)/2 - Phi(n)); it evaluates Phi with a
Mobius sieve and then with the overview PDF's sublinear totient-summatory algorithm 6.
hypotheses: n >= 1; sixfold symmetry of the hexagon; gcd criterion.
holds-here: yes — same problem definition; the identity matches this run's
brute.py at n = 5, 10, 1000.
status: asserted (independent corroboration of the already checked closed form;
the page prints no final integer).
bearing: corroborates hexagonal-orchard-closed-form and the sublinear-Phi route
as the standard method; no new computation needed.
anchor: research/summaries/ivl-projecteuler-problem-351.md
```

## Hypotheses

n ≥ 1; the six-triangle symmetry and the gcd-per-layer criterion. Hold here
(verified by brute.py and the identity at n = 5, 10, 1000).

## Claims

None new — corroborates `hexagonal-orchard-closed-form`,
`summatory-totient-mobius-identity`, and the sublinear Φ route already claimed
from OEIS A216453, Brown arXiv:2506.07386, and Brumme. Added
`pe351-ivl-standard-method` (asserted) to record the corroboration with its
URL.
