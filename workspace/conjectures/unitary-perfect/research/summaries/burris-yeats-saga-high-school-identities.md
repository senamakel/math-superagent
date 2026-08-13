<!-- source: https://math.uwaterloo.ca/~snburris/htdocs/MYWORKS/PREPRINTS/saga.pdf | converted from PDF -->

# Burris & Yeats, *The Saga of the High School Identities* (Algebra Universalis 52 (2004) 325–342; preprint held)

Full text: `research/sources/burris-yeats-saga-high-school-identities.full.md`.

## What it establishes

Survey of the equational theory of `(N, +, ×, ↑, 1)` and its finite quotients
`N_{a,k}` (integers with `a ≈ a + k`). **This is the origin text for the Higgs
prime construction** (OEIS A057447, cited by Maciejewski as [16]).

Theorem 1.1 / Proposition 1.3 (the arithmetical heart):

- Finite quotients `N_{a,k}` exist iff for all primes p: `p^e | k ⇒ e ≤ a` and
  `p | k ⇒ (p−1) | k`.
- Given `a`, define the prime sequence `Σ_a`: `p₁ = 2`, then `p_{i+1}` = the
  smallest prime `> p_i` with `(p−1) | (p₁⋯p_i)^a`. There are infinitely many
  `N_{a,k}` iff `Σ_a` is infinite.
- **`Σ₁ = (2, 3, 7, 43)` is FINITE** (exponent-1 Higgs sequence terminates).
- For `Σ₂`, about 20% of primes below 10^7 occur; enumeration cannot decide
  finiteness.
- **Conjecture 1 (Burris–Yeats):** `Σ_a` is infinite for every `a > 1`, with
  asymptotic density zero in the primes.

The 3-Higgs primes `P₃` of this run are exactly `Σ₃` (exponent-3 closure, OEIS
A057447). So the paper's empirical `Π₃(x) ≈ x^0.62` and the run's
`ford-thinness-downward-closed-primes` claim sit on top of this conjecture.

## Bearing on this problem

Fixes the *definitional origin* of 3-Higgs primes as a primary text (the run's
`hb-defs-3higgs-heven` claim previously cited only the OEIS digest). It shows
`Σ₁` finite — so the exponent cap matters: for a = 1 the greedy sequence dies at
43, while for a = 2, 3 it is conjecturally infinite. The conjecture "Σ_a
infinite with density zero" is the same phenomenon as Ford's power-saving
thinness for downward-closed prime sets, stated here 10 years earlier in
universal-algebra language. Load-bearing only as the origin/conjecture context;
it does not by itself bound anything in `H_even`.

```claim
id: burris-yeats-higgs-prime-origin
statement: Burris & Yeats define the Higgs prime sequences Sigma_a (p1 = 2,
  p_{i+1} = least prime > p_i with (p_i+1 - 1) | (p1...p_i)^a) as the
  classification invariant of finite quotients of the exponentiation algebra;
  Sigma_1 = (2,3,7,43) is finite, and they conjecture Sigma_a is infinite with
  asymptotic prime-density zero for every a > 1. The run's 3-Higgs primes P_3
  are Sigma_3.
hypotheses: none beyond the definition; the conjecture is open
holds-here: yes -- the run's P_3 is literally Sigma_3; finiteness of Sigma_1
  shows the exponent cap is essential (a=1 dies at 43, a >= 2 does not)
status: sourced (full text held); Conjecture 1 is an open conjecture, not a
  theorem
bearing: definitional origin of the 3-Higgs primes; context for the run's
  Ford-thinness claims; no direct H_even bound
anchor: research/summaries/burris-yeats-saga-high-school-identities.md
answers: origin-of-higgs-primes, whether-sigma1-finite
```