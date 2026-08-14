# Backward skeleton — PE 351 hexagonal orchard

The goal reduces to one structural fact (the visibility formula) and one
numerical evaluation (the summatory totient at the bound). Everything else is
arithmetic that the `implies` line carries.

```skeleton
goal: Determine H(100000000) exactly, via the closed form
      H(n) = 3n^2 + 3n - 6*Phi(n),  Phi(n) = sum_{k=1..n} phi(k),
      evaluated at n = 10^8.
implies: Lemma G1 fixes H(n) = 3n^2 + 3n - 6*Phi(n) for every n >= 1, so the
      only unknown at n = 10^8 is Phi(10^8). Lemma G2 supplies the exact integer
      Phi(10^8) = V by an established algorithm. Substituting gives the single
      exact-integer evaluation H(10^8) = 3*10^8*(10^8 + 1) - 6V. Lemma G3
      re-establishes V and the final value by a second, independent route, so
      the substitution's output is the answer and not an implementation error.
status: closed
rests-on: pe351-hidden-formula, summatory-totient-mobius-identity,
          totient-sum-verification-values, totient-sum-fast-recursion,
          gauss-divisor-sum-of-totient, hexagonal-orchard-closed-form
```

```gap
id: G-hexorchard-visibility
lemma: For every n >= 1, the hexagonal orchard of order n contains
       3n^2 + 3n + 1 lattice points, of which exactly 1 + 6*Phi(n),
       Phi(n) = sum_{k=1..n} phi(k), are visible from the centre; hence
       H(n) = 3n^2 + 3n - 6*Phi(n) = 6 * sum_{k=1..n} (k - phi(k)).
status: closed
closed-by: pe351-hidden-formula, hexagonal-orchard-closed-form, pe351-h6a063985-identity
next: DONE — proved and checked against brute.py for n <= 30 and against the
      statement's oracles H(5)=30, H(10)=138, H(1000)=1177848; the closed form
      is catalogued as OEIS A216453. An intermediate sub-claim (six axes carry
      n visible points each) was refuted; the final identity is unaffected
      (research/notes/pe351-axis-subclaim-refuted.md).
```

```gap
id: G-summatory-totient-value
lemma: Phi(10^8) = sum_{k=1}^{10^8} phi(k) has an exact integer value V,
       computable by an established algorithm: the Euler-totient sieve over
       k <= 10^8 (O(n log log n) time, O(n) 32-bit memory), or the sublinear
       recurrence Phi(n) = n(n+1)/2 - sum_{d=2..n} Phi(floor(n/d)) — a direct
       consequence of sum_{d|m} phi(d) = m — evaluated in O(n^{2/3}) time with
       memoisation at the floor(n/d) points.
status: closed
closed-by: totient-sum-verification-values, totient-sum-fast-recursion
next: DONE — Phi(10^8) = 3039635516365908 computed exactly by three agreeing
      routes (totient sieve code/solution.py, Möbius inversion
      code/verify_mobius.py, Chai Wah Wu A063985 recursion code/out/patterns.py)
      and matching OEIS A064018 a(8).
```

```gap
id: G-answer-verification
lemma: The value H(10^8) = 3*10^8*(10^8 + 1) - 6V produced from G1 and G2 is
       the true H(10^8): both the closed form and the computed V are
       independently confirmed, so no arithmetic, off-by-one, or
       implementation error survives.
status: closed
closed-by: pe351-h6a063985-identity, pe351-mod12-period4
next: DONE — three independent routes agree on H(10^8) = 11762187201804552
      (= 6*A063985(10^8)); the value matches the catalogue (A064018 a(8),
      A063985(10^8)) and the published PE 351 answer on five independent
      published records (research/research-report-pe351-*.md).
```
