# Hwang–Janson–Tsai — Periodic minimum in the count of binomial coefficients not divisible by a prime

<!-- source: https://arxiv.org/pdf/2408.06817 | arXiv:2408.06817v1 [math.NT] 13 Aug 2024 -->

**What this establishes for SUPPLY (librarian — fills the log-periodic gap).**
This is the *primary proof* that the run's `log-periodic-oscillation-test-d47`
previously cited only from an OEIS comment. Theorem 2.2 gives, for every prime
p, the exact log-periodic representation of the summatory count of Pascal
entries not divisible by p:

```
F_p(n) = n^ρ · P(log_p n)  for all n ≥ 1,
ρ = ρ_p := log_p((p+1)/2),
P(t) = P_p(t) a continuous 1-periodic function,
P(t) = A^{1−{t}} · φ(p^{{t}−1}),   A = A_p = (p+1)/2,
```

with φ given by the explicit digit formula (2.11) and the functional
equation (2.12). For p = 2:

- F₂(n) is exactly OEIS A006046 (number of odd entries in first n rows of
  Pascal's triangle), and ρ₂ = log₂(3/2) = log₂3 − 1 = **0.58496**.
- This is precisely the exponent directive 48 names as the "natural candidate"
  for w*(n) in the run's oscillation test — A006046 is the textbook
  Pascal-mod-2 counting function carrying the `n^E · P(log₂n)` form, its
  exact exponent log₂3 on the raw cumulative, hence log₂3−1 on the
  normalized-threshold reading.

**Importance to this problem.** The run is testing whether w*(n)/n^E shows the
bounded period-1-in-log₂(n) oscillation classical to Pascal-mod-2 counting
functions (falsifier: monotone trend). This paper is the citable primary source
for that phenomenon in its exact prototype (p=2). It does **not** transfer the
result to w*(n) — that transfer is a structural analogy, decided by the run's own
tabulation — but it *grounds* the analogy in a theorem rather than an OEIS remark.

**Neither proves nor disproves SUPPLY.** Purely arithmetic-combinatorial about
Pascal parity; the fold weight wt(Φ_n h) is a different object. Status: sourced
primary, not a SUPPLY result.

**Also here.** Wilson's conjecture β_p = B_{ξ,η} settled for odd p ≤ 113
(Thm 1.1); p=2 singled out as the hardest case (Problem 1.2, no exact β₂ known).

Full text: `research/sources/hwang_janson_tsai_periodic_minimum_binomial_modp.full.md`
