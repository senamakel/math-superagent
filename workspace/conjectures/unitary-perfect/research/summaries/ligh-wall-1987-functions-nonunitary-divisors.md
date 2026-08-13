<!-- source: https://www.fq.math.ca/Scanned/25-4/ligh.pdf | converted from PDF -->

# Ligh & Wall 1987, *Functions of Non-Unitary Divisors*, Fib. Quart. 25(4):333–338

Full text: `research/sources/ligh-wall-1987-functions-nonunitary-divisors.full.md`.

## What it establishes

Study of "non-unitary" divisors: `d` is non-unitary if `gcd(d, n/d) > 1`.
The authors decompose `n = n* · n#` where `n*` is the largest squarefree
unitary divisor (the "squarefree part") and `n#` the "powerful part" — the same
squarefree/powerful split that underlies Graham's 1989 theorem for UPNs.

- **Thm 1:** if `2^p − 1` is prime then `2^p (2^p − 1)` is *non-unitary perfect*
  (σ#(n) = n). Conjecture 1: n is non-unitary perfect iff `4 × (even perfect)`.
  Conjecture 2: infinitely many k-fold non-unitary perfect numbers.
- **Thm 2 + Conjecture 3:** non-unitary *subperfect* iff `n = 18` or `n = p²`.
- **Thm 7:** if `Σ_{d non-unitary} φ#(d) = n` for `n > 1` then `n#` is divisible
  by at least **two distinct primes** (proof: `σ(n)/n = p` forces a
  contradiction for `n# = p^e`).

## Bearing on this problem

Adjacent divisor-class classification from the same family as the run's
Wall/Cohen/Subbarao sources. Its value is structural context, not a tool for
`H_even`: the `n = n*·n#` decomposition is the same lens Graham used to prove
"UPN with squarefree odd part ⇒ {6,60,87360}", and Theorem 7's "powerful part
needs ≥ 2 distinct primes" is the non-unitary analogue of Graham's
"repeated odd kernel" conclusion. No new constraint on unitary perfect numbers
or `H_even` follows from it directly.

```claim
id: ligh-wall1987-nonunitary-perfect-construction
statement: If 2^p - 1 is prime then 2^p(2^p - 1) is non-unitary perfect
  (sum of proper non-unitary divisors equals the number); the authors
  conjecture every non-unitary perfect number is 4 times an even perfect
  number, verified below 10^6 (no other examples).
hypotheses: p prime with 2^p - 1 prime
holds-here: yes — true theorem, but about the NON-unitary divisor class, which
  is not the unitary class of this problem; kept as adjacent-class context only
status: sourced (primary text held)
bearing: confirms 6, 60, 90 are not special to one divisor theory; the
  squarefree/powerful split used here is the same one behind Graham 1989
anchor: research/summaries/ligh-wall-1987-functions-nonunitary-divisors.md
```