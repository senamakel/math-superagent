# Browning & Elsholtz, "The number of representations of rationals as a sum of unit fractions"

Source: https://www.math.tugraz.at/~elsholtz/WWW/papers/papers33FINAL2013.pdf
(Illinois J. Math. 55 (2011) 685–696).
Full text: `research/sources/browning-elsholtz-representations-unit-fractions.full.md`

## What it establishes (sourced, primary)

Bounds on `f_k(m,n) = #{(t_1,...,t_k) ∈ N^k : t_1 ≤ ... ≤ t_k, m/n = Σ 1/t_i}`.

- **Theorem 1 (k=2)**: `f_2(m,n) ≤ exp((log 3 + o(1)) log n / log log n)`,
  and infinitely many n with equality up to the constant — a two-term
  characterisation.
- **Theorem 2**: for any ε > 0 there is C_ε with
  `f_3(m,n) ≤ C_ε m^ε n^{3/5+ε}` (improves the f(p) ≪ p^{3/5+o(1)} bound of
  Elsholtz–Tao to arbitrary m, uniform in m).
- **Theorems 3–4**: for k ≥ 4, `f_k(m,n) ≤ C_{k,ε} m^ε n^{ε}` and
  `n^{o(1)}`-type bounds.

## Consequence

Counting context: bounds on how many solutions exist (relevant to the
"f(p) grows" empirical observations of Mihnea–Dumitru, and to Elsholtz–Tao's
average results). Not construction machinery.

```claim
id: browning-elsholtz-f3-bound
statement: For any ε > 0, f_3(m,n) ≤ C_ε m^ε n^{3/5+ε}, extending Elsholtz–Tao's f(p) ≪ p^{3/5+o(1)} to general m uniformly.
hypotheses: m,n positive integers; f_3 counts ordered triples.
holds-here: true — context for the counting side of the run.
status: sourced (Browning–Elsholtz 2011, Theorem 2).
bearing: bounds solution counts; does not construct families.
anchor: research/sources/browning-elsholtz-representations-unit-fractions.full.md
```