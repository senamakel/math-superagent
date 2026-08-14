# Thread: sum-of-squares Psi(k) over length-k factors of the Fibonacci word

```thread
id: psi-sum-squares-recurrence
question: How to compute Psi(k) = sum over the k+1 length-k factors w of the Fibonacci word
  (Sturmian, slope 1/phi^2) of (decimal value of w)^2, in poly(log k), to get Psi(10^18) mod 101001001.
status: blocked on closed-form/recurrence
rests-on: PE1006-kplus1-FACT, PR-consecutive-factors-lex, PE1006-factors-dependent-slop-only, MH-kplus1-factors
blocked-by: no known indexed enumeration of factors that relates grade-k values to grade-(k-1) in
  poly(log k); the PR Sturm() enumeration is O(k^2), infeasible at k=10^18.
next: derive a recurrence from the b^p a^q column structure of the lex-ordered (k+1)xk factor matrix
```

## What unblocks / kills

- **Provides the enumeration (structure):** Perrin–Restivo Theorem 2 (consecutive factors
  u=r·ab·s, v=r·ba·s) is the structural backbone; claim `PR-consecutive-factors-lex` (proved).
  But Sturm() is O(k²) in length, infeasible for k=10^18; only the *structure* transfers to a
  recurrence, not the iteration itself.
- **Killed:** the balanced-count paraphrase "factors are exactly the floor/ceil(k·α)-ones words"
  is a FALSE bijection (k=3: 6 candidates vs 4 factors; k=4: 10 vs 5). See
  research/approaches/balanced-factors-claim-attack.md. The necessary condition (every factor
  has floor/ceil(k·α) ones) survives as `PE1006-factors-one-count-necessary`.
- **Request fulfilled:** `precise-sourced-statement-c1ec` (indexed classification) is answered by
  `PR-consecutive-factors-lex` — the lex-order next-factor rule indexes all k+1 factors — not by
  the false balanced-set bijection.
- **Needed:** an exact recurrence for Ψ(k) in terms of Ψ(k-1) (or the factor matrix columns),
  suitable for matrix exponentiation / fast doubling, matching psi_brute_k1_30.txt for k=1..30.
