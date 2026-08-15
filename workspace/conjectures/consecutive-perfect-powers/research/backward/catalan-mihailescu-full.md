# Backward skeleton — full proof of the Catalan conjecture

The goal, decomposed into the propositions that would give it, following the
standard (Mihailescu) structure. `research/CLAIMS.md` is currently empty
("No claims recorded yet") and `search_claims` finds no claim matching any
lemma below, so **every** lemma here is an open gap, none discharged. Each gap
states where the known solution `3^2 - 2^3 = 1` sits relative to it, because a
lemma that eliminates it is refuted, not weakened.

```skeleton
goal: The only solution of x^p - y^q = 1 in integers x, y > 0, p, q > 1 is (x, p, y, q) = (3, 2, 2, 3).
implies: >
  By G-red every solution descends to one with p and q prime. If p = q then
  x^p - y^p = 1 forces y = 0, since (y+1)^p - y^p >= 2^p - 1 >= 3 for p >= 2
  and y >= 1; excluded, so p != q. If p = 2, G-exp2-x gives (x, p, y, q)
  = (3, 2, 2, 3) and nothing else. If q = 2, G-exp2-y gives no solution (p is
  odd prime). The remaining case is p, q distinct odd primes: G-cassels gives
  q | x and p | y; G-wieferich then gives q^{p-1} = 1 (mod p^2) and
  p^{q-1} = 1 (mod q^2); G-final asserts that no such (x, y, p, q) exists.
  The cases are exhaustive, so the only solution is (3, 2, 2, 3).
status: live
rests-on: none — the claim ledger is empty and search_claims returns no matching claim.
killed-by: none
```

```gap
id: red-prime-exponents
lemma: >
  Every solution x^p - y^q = 1 with p, q > 1 yields a solution x'^{p'} - y'^{q'} = 1
  with p', q' prime: if p = a b then (x', p') = (x^a, b) preserves the equation and
  x' > 0; iterate while the exponent is composite, and likewise for q.
status: open
known-solution: unaffected — the known solution already has p = 2, q = 3 prime; the reduction is a logical transform, not a condition on solutions.
next: >
  Lean 4: formalise against Mathlib that composite exponent descends to prime
  exponent by iterated base change x -> x^a, p -> b, and report #print axioms.
  This is ~30 lines and is the formal prerequisite for every later lemma.
```

```gap
id: exp2-case-x-squared
lemma: >
  x^2 - y^q = 1 with x, y > 0, q prime has exactly the solution (x, q, y) = (3, 3, 2),
  i.e. 3^2 - 2^3 = 1.
status: open
known-solution: this lemma is the positive case — the known solution is the unique solution it asserts; it must not be stated as "no solutions".
next: >
  Elementary proof over Z: y^q = x^2 - 1 = (x-1)(x+1), gcd(x-1, x+1) divides 2;
  split on x odd/even, show one factor is a q-th power and the other is
  2^{q-1} times a q-th power, and conclude x = 3, q = 3, y = 2. Then Lean 4.
  Verify the asserted uniqueness against solutions(N) once the oracle is built.
```

```gap
id: exp2-case-y-squared
lemma: >
  x^p - y^2 = 1 with x, y > 0 and p an odd prime has no solution.
status: open
known-solution: excluded by hypothesis (q = 2), since the known solution has q = 3 — a genuine exception the lemma must state.
next: >
  Elementary proof in Z[i]: x^p = y^2 + 1 = (y+i)(y-i), gcd(y+i, y-i) divides 2,
  so for p odd both factors are p-th powers in Z[i] up to a unit; compare
  imaginary parts of (a+bi)^p = y +/- i to force b = +/-1, a = 0, hence y = 0
  (excluded). Then Lean 4. Verify "no solution with q = 2, p odd" against
  solutions(N) for small N.
```

```gap
id: cassels-divisibility
lemma: >
  If x^p - y^q = 1 with x, y > 0 and p, q distinct odd primes, then q | x and p | y.
status: open
known-solution: conclusion holds there too (3 | 3 and 2 | 2), but the hypothesis "both odd" fails since p = 2; the known solution is excluded from this lemma only by that hypothesis.
next: >
  Source Cassels (J. London Math. Soc. 35 (1960)) or a self-contained proof, and
  re-run the two valuation computations that carry it:
  v_p(x^p - 1) = 1 + v_p(x - 1) and v_q(y^q + 1) = 1 + v_q(y + 1), which force
  p | y and q | x. Verify q | x, p | y against the oracle and against (3,2,2,3).
```

```gap
id: double-wieferich
lemma: >
  If x^p - y^q = 1 with x, y > 0 and p, q distinct odd primes, then
  q^{p-1} = 1 (mod p^2) and p^{q-1} = 1 (mod q^2).
status: open
known-solution: fails there (3^1 = 3 != 1 mod 4; 2^2 = 4 != 1 mod 9) — correctly so, because p = 2 is even. This is the trap lemma: dropping the "odd primes" hypothesis makes it false at the known solution, so the hypothesis must be stated and checked.
next: >
  This is the class-group core. First concrete move (symbolic_math): factor
  (x^p - 1)/(x - 1) into cyclotomic values in Q(zeta_p), use p | y and q | x to
  force the ideal factorisation, and derive the p-adic valuation identity that
  yields q^{p-1} = 1 (mod p^2); mirror for p^{q-1} = 1 (mod q^2). Source:
  Mihailescu 2002, "Primary Cyclotomic Units and a Proof of Catalan's
  Conjecture". CAUTION: the hint in problem.md, "p^2 | y^{p-1} - 1", contradicts
  Cassels's p | y (which gives y^{p-1} = 0 mod p), so the exact form must be
  re-derived, not copied; the double-Wieferich form above is the one consistent
  with the known solution being excluded only by the odd hypothesis.
```

```gap
id: odd-prime-contradiction
lemma: >
  There do not exist distinct odd primes p, q and positive integers x, y with
  x^p - y^q = 1, q | x, p | y, q^{p-1} = 1 (mod p^2) and p^{q-1} = 1 (mod q^2).
status: open
known-solution: excluded by hypothesis (distinct odd primes; the known solution has p = 2).
next: >
  Extract the exact closing lemma of Mihailescu's proof — the short estimate that
  turns the double-Wieferich congruences plus q | x, p | y into a contradiction —
  and reduce it to a checkable inequality. Until the precise statement and proof
  are sourced, this is a research request rather than a task (see request_research
  below); afterwards it is a Lean 4 target.
```
