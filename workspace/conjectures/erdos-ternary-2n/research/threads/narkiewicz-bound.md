```thread
question: What is the exact statement, constant, and method of Narkiewicz's bound on {n <= x : 2^n digit-2-free}?
status: live
rests-on: EP-406 (bound N(x) <= 1.62 x^(log_3 2), asserted-by-source), LAG-2 (proved, Lagarias)
blocked-by: primary Narkiewicz paper not in library
next: locate and download Narkiewicz (1980) "A note on a paper of H. Gupta concerning powers of two"; verify the constant and method against EP-406 and LAG-2
```

# Narkiewicz's bound — the known nontrivial result

## Why this thread

The modular sieve has now been shown (checked k ≤ 22) to grow like `2^(k-1)`,
so it can never close. Narkiewicz's bound is the standard nontrivial result on
the thin-orbit question itself, and is what the run should extract next
(directive item 2).

## What is already in the library

- `EP-406` (asserted-by-source, from `research/summaries/erdos-problems-b33.md`):
  `N(x) ≤ 1.62 · x^(log_3 2)` credited to Narkiewicz, with `log_3 2 ≈ 0.6309 < 1`.
- `LAG-2` (proved, from Lagarias `research/summaries/lagarias-ar5iv-full.md`):
  for every nonzero λ ∈ ℤ_3, `#{n ≤ X : (λ2^n)_3 omits digit 2} ≤ 2 X^{α_0}`
  where `α_0 = log_3 2`. Same exponent, proved route.

So the statement and the exponent are settled. What remains is to close the gap
on the **method and the explicit constant** of the original paper.

## What is still needed

The primary source: Narkiewicz (1980), "A note on a paper of H. Gupta
concerning powers of two", Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat.
Fiz. (1980), no. 678-715, 173-174 (1981). MR 623247.

- Confirm the exact statement and the constant 1.62 (or whatever it is).
- Extract the method (Lagarias LAG-2 is one route; whether Narkiewicz's original
  is the same route or different is the open question).

FRONTIER.md cites it via `https://www.jstor.org/stable/43667894` and MR 623247.

## Falsifier

If the source gives no `O(x^c)` bound with `c < 1`, or applies only to a
different digit/position condition, then EP-406's attribution is wrong and must
be corrected.

## Status

Statement and exponent in library (EP-406 asserted, LAG-2 proved). Primary
source and original method still missing.

