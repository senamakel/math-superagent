# Ventas, "A Ceiling Continued Fraction Approach to the Erdős–Straus Conjecture"

Source: arXiv:2605.04551 (v2, 25 May 2026), HTML: https://arxiv.org/html/2605.04551v2
Full text: `research/sources/ventas-ceiling-continued-fraction.full.md`

## What it establishes (sourced, primary)

A framework (FCT: finite/ceiling continued fractions) that constructs three
term Egyptian fractions for Mordell-type primes `p ≡ 1, 11², 13², 17², 19²,
23² (mod 840)` from the divisor structure of shifted integers `p + i`.

- Key existence statement (informal): for primes `p ≡ 1 (mod 4)`, if `p + i`
  has a divisor `d ≡ 3 (mod 4)` with `4i | (p + d)`, then there is a direct
  three-term solution built from `(p + d)/i`. For `p ≡ 3 (mod 4)` the
  two-term representation emerges immediately.
- Computational tests: 10^9 primes around 10^17, 10^52, and 10^7 primes around
  10^131 with very small search depth (M=40 sources) find no counterexamples.
- Probabilistic model gives a super-polynomial bound on the failure
  probability; Borel–Cantelli then gives heuristic evidence the counterexamples
  (if any) form a finite set. **Heuristic, not a proof.**

## Consequence

Another constructive engine aimed directly at the six open classes, but it is
explicitly heuristic (probabilistic, finite-set conclusion). The concrete
divisor condition `p + i` having `d ≡ 3 (mod 4)` with `4i | (p+d)` is
checkable per prime — a candidate rule the run's oracle can test on the
witnesses, and a possible source of a deterministic family if the condition
can be made to hold identically for a sub-class.

```claim
id: ventas-fct-heuristic
statement: Under the FCT framework, a prime p ≡ 1 (mod 4) has a 3-term solution whenever p+i has a divisor d ≡ 3 (mod 4) with 4i | (p+d); computational tests over 10^9 primes near 10^17/10^52 and 10^7 primes near 10^131 find no counterexamples with search depth 40, giving heuristic (Borel–Cantelli) evidence that counterexamples, if any, form a finite set.
hypotheses: primes ≡ 1 (mod 4) (the open classes are a subset); heuristic/probabilistic argument.
holds-here: true — applies directly to the six open classes, but the conclusion is heuristic, not proved.
status: sourced (arXiv:2605.04551; computational + probabilistic heuristic).
bearing: concrete per-prime divisor condition testable on witnesses; not a proof engine by itself.
anchor: research/sources/ventas-ceiling-continued-fraction.full.md
```