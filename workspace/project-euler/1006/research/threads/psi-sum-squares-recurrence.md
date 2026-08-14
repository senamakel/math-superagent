# Thread: sum-of-squares Psi(k) over length-k factors of the Fibonacci word

```thread
id: psi-sum-squares-recurrence
question: How to compute Psi(k) = sum over the k+1 length-k factors w of the Fibonacci word
  (Sturmian, slope 1/phi^2) of (decimal value of w)^2, in poly(log k), to get Psi(10^18) mod 101001001.
status: partially unblocked at Fibonacci k; still open at k=10^18
rests-on: PE1006-kplus1-FACT, PR-consecutive-factors-lex, PE1006-factors-dependent-slop-only, MH-kplus1-factors,
  PE1006-conjugate-singular-iff-fibonacci, chuan-cyclic-shift-index
blocked-by: at Fibonacci k=F_n the conjugate class gives positional arithmetic-progression index rules
  (Chuan Thm 11/Cor 12) that reduce the rotation-sum Psi(F_n) to poly-log arithmetic; the gap that remains
  is (a) the singular factor and (b) stepping from F_n to the general k=10^18 (which is not a Fibonacci
  index) and (c) the decimal (a=0,b=1) re-reading of Chuan's a/b positions. General-k poly-log still open.
next: derive the closed rotation-sum Psi(F_n) from Chuan's arithmetic-progression positions plus the
  singular square, then reach k=10^18 from the nearest Fibonacci index via the verified extension
  recurrence Psi(k+1)=100(Psi(k)+v_R^2)+20P1+N1 (PE1006-extension-formula, R(k)=f[0..k-1]^R by MSS Thm 18).
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
