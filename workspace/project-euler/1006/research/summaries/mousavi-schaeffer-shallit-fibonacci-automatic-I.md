# Mousavi, Schaeffer, Shallit — "Decision algorithms for Fibonacci-automatic words, I: Basic results" (RAIRO ITA 50 (2016) 39-66)

<!-- source: https://cs.uwaterloo.ca/~shallit/Papers/part1.pdf (author preprint) -->

## What this source establishes

A decision procedure over **Fibonacci (Zeckendorf) representations**: any first-order
proposition about the Fibonacci word `f = 01001010...` (fixed point of `0->01, 1->0`)
formulated with indexing, addition, and comparisons is decidable by converting it into a
finite automaton. The paper then mechanically re-proves (and improves) ~31 known results
about `f`. Those directly relevant to PE1006's factor structure:

- **Theorem 18 (right-special factor).** The unique special factor of length `n` is
  `f[0..n-1]^R` (the reverse of the length-n prefix of `f`). This is exactly the
  right-special factor `R(k)` in the run's state recurrence (`PE1006-extension-formula`),
  giving it an explicit closed form: the reverse of the length-k prefix of `f`.
- **Theorem 19.** Every nonempty factor `w` of `f` has least period a Fibonacci number
  `F_n (n>=2)`, and each such period occurs. (Periods of the Fibonacci-word factors.)
- **Theorem 6/8.** All squares in `f` are of order `F_n`; cubes of order `F_n`, `n>=4`.
- **Theorem 27.** The critical exponent of `f` is `2 + (1+sqrt5)/2`.
- **Theorem 13.** Palindromic factors: exactly one palindromic factor of length `n` if
  `n` even, two if `n` odd.
- **Theorem 14.** The length-n prefix `f[0..n-1]` is a palindrome iff `n = F_i - 2`, `i>=3`.

## Relevance to this problem

- **Fixes the right-special factor** `R(k) = f[0..k-1]^R` (reverse prefix), the exact
  quantity the sum-of-squares state recurrence (`PE1006-extension-formula`) needs and
  whose evolution must be closed to evaluate `Psi(k)` in poly(log k).
- **Confirms the factor/complexity structure** (subword complexity `k+1`, unique
  right-special factor) that the solver derives from. The paper's results are computed
  mechanically, so they are independently verified in the literature, but the paper does
  NOT supply a closed form for `Psi(k)` itself — that remains the run's task.

## What it does NOT settle

The paper gives no formula for the sum of squares `Psi(k)`; it gives structural facts
(periods, special factors, palindromes) that a closed form or recurrence on `Psi(k)`
can use. The decision procedure is effective but not a poly(log k) evaluation of a
specific arithmetic quantity at `k = 10^18`.

## Full text

[[mousavi-schaeffer-shallit-fibonacci-automatic-I.full]]

```claim
id: PE1006-rightspecial-reverse-prefix
statement: The unique right-special length-n factor of the Fibonacci word f is R(n) = f[0..n-1]^R, the reverse of the length-n prefix of f (MSS Thm 18). Also: every nonempty factor of f has least period a Fibonacci number (Thm 19), and the length-n prefix is a palindrome iff n = F_i - 2 (Thm 14).
hypotheses: f = 01001010... fixed point of 0->01, 1->0 (the problem's Fibonacci word).
holds-here: yes — the solver's state recurrence (PE1006-extension-formula) names the unique right-special factor R(k); this source fixes it explicitly as the reversed length-k prefix.
status: sourced (proved mechanically in MSS 2016)
bearing: identifies R(k) in the Psi(k) state evolution, a load-bearing quantity for any closed recurrence on Psi(k); not itself the closed form for Psi(k).
anchor: research/summaries/mousavi-schaeffer-shallit-fibonacci-automatic-I.md
```
