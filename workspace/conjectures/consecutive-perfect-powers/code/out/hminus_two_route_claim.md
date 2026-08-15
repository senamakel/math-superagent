# h^-(Q(zeta_p)) — two independent implementations agree

## The gap this closes

The previous attempt flagged that `minus-class-number-formula` was `status: checked`
only because `verify_claims.py` and `hminus_exact.py` were *both* float-specialised
implementations of the *same* Bernoulli product `∏χ(−½B_{1,χ})`, both compared to the
same hardcoded OEIS table. That closed only "the implementation reproduces the table
at 9 primes", not "the formula holds".

## Two genuinely different routes now agree

- **Route 1 (workspace)**: exact-rational Bernoulli product `h^-(K) = 2p·∏_{χ odd}(−½·B_{1,χ})`
  over `Q(ζ_p)` (`code/hminus_full.py`, exact `Fraction` arithmetic in `lib.cyclo`).
- **Route 2 (this attempt)**: PARI/GP `bnfinit` computes `h(K)` and `h(K^+)` directly
  (K = Q(ζ_p) via `polcyclo(p)`, K^+ = maximal real subfield via `polsubcyclo(p,(p-1)/2)`),
  and `h^- = h(K)/h(K^+)` as exact integer division. `bnfinit`'s Buchmann–Lenstra
  class-group machinery never evaluates the Bernoulli product, so the two routes share
  **neither the arithmetic expression nor the evaluation method**.

Program: `code/hminus_pari/hminus_pari.gp`; captured: `code/out/hminus_pari.captured.txt`.

## Result — 13/13 matched

| p | h(K) | h(K^+) | h^- | expected |
|---|------|--------|-----|----------|
| 3,5,7,11,13,17,19 | 1 | 1 | 1 | 1 |
| 23 | 3 | 1 | 3 | 3 |
| 29 | 8 | 1 | 8 | 8 |
| 31 | 9 | 1 | 9 | 9 |
| 37 | 37 | 1 | 37 | 37 |
| 41 | 121 | 1 | 121 | 121 |
| 43 | 211 | 1 | 211 | 211 |

All h(K^+) = 1 (consistent with h^+ = 1 for p < 71). p = 43 = 211 line present.

## Status

**Numeric cross-check, not a proof.** Both routes rest on the classical analytic
class-number theorem (sourced-not-proved in this run). What the agreement upgrades:
the *evidence* for the h^- values from "one formula against a catalogue, evaluated
twice the same way" to "reproduced by two independent implementations." No claim of a
proof of Catalan's conjecture is made or implied.

```claim
id: hminus-two-independent-routes
statement: >
  h^-(Q(zeta_p)) for p in {3,5,7,11,13,17,19,23,29,31,37,41,43} equals
  {1,1,1,1,1,1,1,3,8,9,37,121,211}, computed by two independent
  implementations that share neither an arithmetic expression nor an evaluation
  method: (1) exact Bernoulli-product h^- = 2p prod_{chi odd}(-1/2 B_{1,chi});
  (2) PARI/GP bnfinit class-number ratio h(K)/h(K^+) over the cyclotomic field
  and its maximal real subfield. 13/13 agree and match OEIS A000927.
hypotheses: >
  p odd prime, 3 <= p <= 43. Both routes rest on the classical analytic
  class-number theorem (sourced, not re-proved). p=43 h^- = 211. All h(K^+)=1.
holds-here: yes — the minus class number of Q(zeta_p) is the class-group
  quantity the both-odd-prime obstruction lives in; the values are load-bearing
  only as evidence, not as a proof step.
status: checked (verified-numerically, two independent routes to p=43; not a proof)
anchor: code/out/hminus_pari.captured.txt, code/hminus_pari/hminus_pari.gp
```
