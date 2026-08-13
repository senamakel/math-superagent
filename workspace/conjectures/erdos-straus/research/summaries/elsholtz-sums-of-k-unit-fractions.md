# Elsholtz, "Sums of k unit fractions"

Source: https://www.math.tugraz.at/~elsholtz/WWW/papers/papers03sumofk.pdf
(Trans. Amer. Math. Soc. 353 (2001) 3209–3227).
Full text: `research/sources/elsholtz-sums-of-k-unit-fractions.full.md`

## What it establishes (sourced, primary)

Context for the counting side. Studies `m/n = 1/t1 + ... + 1/tk`. Key idea:
integer ratios have multiplicative structure expressible by `2^k − 1`
parameters (one per nonempty subset of the k denominators), and using all of
them gives sharper sieve estimates.

- **Conjecture 1.2 (Schinzel)**: for all m ≥ 4 there exists N_m such that for
  all n ≥ N_m, `m/n = 1/x + 1/y + 1/z` is solvable. Cites [Sie56].
- **Theorem 1.3**: for fixed k ≥ 3, m > k, the exceptional set
  `E_{m,k}(N) = #{n ≤ N : 4/n is not a sum of k unit fractions}` (in the m/n
  normalisation) is bounded by `N exp(−c_{m,k}(\log N)^{(2^{k-1}-2)/(2^{k-1}-1)})`.
  For k=3 this recovers Vaughan's bound.
- Numerous lemmas on uniqueness of residue classes / factorisations needed for
  the large sieve; Theorem 6.1 gives lower bounds on sums of f(p)-type
  functions.

## Consequence

Not construction machinery — it establishes that parametric-solution counting
is a mature tool, and records Schinzel's generalised conjecture. The `2^k − 1`
parameter viewpoint is a possible lens for the run's ansatz space (the
parametrisations of three denominators by gcd-structure — cf. Bradford's
`x = abm, y = acm, z = bcm` which is exactly the 3-parameter view for k=3).

```claim
id: elsholtz-k-unit-fractions-bound
statement: For k ≥ 3, m > k fixed, the number of n ≤ N for which m/n is not a sum of k unit fractions is at most N exp(−c_{m,k} (log N)^{1 − 1/(2^{k−1} − 1)}).
hypotheses: k ≥ 3, m > k fixed; large sieve.
holds-here: true but only context — the k=3 case is Vaughan's counting bound; this is not a construction.
status: sourced (Elsholtz 2001, Theorem 1.3).
bearing: counts exceptions; does not construct families for the open classes.
anchor: research/sources/elsholtz-sums-of-k-unit-fractions.full.md
```