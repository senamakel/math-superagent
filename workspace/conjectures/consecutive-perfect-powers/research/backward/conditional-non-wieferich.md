# Skeleton — conditional theorem: non-double-Wieferich pairs give no solution

This is the cheapest result that would count under GOAL.md's second
deliverable: a theorem for *all* odd prime exponent pairs satisfying a stated,
checkable condition. It does not wait on the deep descent; it rests only on
Cassels's divisibility theorem and the double-Wieferich refinement, both of
which are re-derivable in this workspace.

```skeleton
goal: >
  For all odd primes p, q with p^(q-1) != 1 (mod q^2) or
  q^(p-1) != 1 (mod p^2) (i.e. (p,q) is NOT a double-Wieferich pair),
  the equation x^p - y^q = 1 has no solution in integers x, y > 0.
implies: >
  Contraposition. Assume (x,p,y,q) is a solution with p,q odd primes. By
  cond-cassels, p | y and q | x. By cond-wieferich, applied to that same
  solution, p^(q-1) = 1 (mod q^2) AND q^(p-1) = 1 (mod p^2). Hence any
  solution forces (p,q) to be a double-Wieferich pair. Therefore if (p,q)
  is not a double-Wieferich pair — at least one of the two congruences
  fails — no such solution exists. The two gaps are chained
  (solution -> Cassels -> double-Wieferich), and the goal is their
  contrapositive, so the conjunction of the two lemmas is exactly the goal.
  The known solution (3,2,2,3) has p = 2 (even), so it lies outside the
  hypothesis "p,q odd primes" and is never eliminated: the theorem only
  speaks about odd-prime pairs, and the checkable condition is stated for
  odd primes only.
status: sketched
rests-on: none — research/CLAIMS.md is empty and search_claims finds no matching claim.
killed-by: none
```

```gap
id: cond-cassels
lemma: >
  If x^p - y^q = 1 with x,y > 0 and p,q distinct odd primes, then
  q | x and p | y. (Cassels, 1960.)
status: open
known-solution: conclusion happens to hold there too (3 | 3, 2 | 2), but the
  hypothesis "both odd" fails since p = 2; the lemma is silent about
  (3,2,2,3) and never claims no solution exists.
next: >
  Re-derive via the two factorisations x^p - 1 = y^q in Z[zeta_p] and
  y^q + 1 = x^p in Z[zeta_q]: in Q(zeta_p) the prime (1-zeta_p) is the
  unique ramified prime and the ideals (x - zeta_p^i) are pairwise coprime
  off it, so the q-th-power valuation of y^q forces p | v_p(y); mirror for
  q | v_q(x). symbolic_math runs the valuation computation on small odd
  (p,q); theorem_prover formalises the resulting divisibility in
  Lean/Mathlib. Cross-check against the exact-integer oracle once built.
```

```gap
id: cond-wieferich
lemma: >
  If x^p - y^q = 1 with x,y > 0 and p,q distinct odd primes, then
  q^(p-1) = 1 (mod p^2) and p^(q-1) = 1 (mod q^2).
status: open
known-solution: fails there (3^1 = 3 != 1 mod 4, 2^2 = 4 != 1 mod 9) —
  correctly, because p = 2 is even; this is the trap lemma and the odd-prime
  hypothesis is exactly what keeps the known solution outside.
next: >
  Derive from cond-cassels by the p-adic / cyclotomic-unit argument: p | y
  forces x^p = 1 (mod p^2) and a unit relation in Z[zeta_q] yields
  p^(q-1) = 1 (mod q^2); mirror for the other congruence. symbolic_math
  computes the ideal factorisation of (x^p - 1)/(x - 1) in Q(zeta_p) and
  the forced congruence; theorem_prover formalises the result. Then
  tool_builder implements check_conditions(p,q) evaluating both
  congruences by exact integer arithmetic — the direct, runnable form of
  the condition in the goal. CAUTION: the problem.md hint "p^2 |
  y^{p-1} - 1" contradicts p | y (it forces y^{p-1} = 0 mod p), so the
  exact form must be re-derived, not copied; the double-Wieferich form
  above is the one consistent with the known solution being excluded only
  by the odd-prime hypothesis.
```

## What this buys and where it stops

The conjunction of the two gaps gives the conditional theorem, which is the
precise, checkable form of GOAL.md's second deliverable:

> **If an odd-prime pair (p,q) is not a double-Wieferich pair, then
> x^p - y^q = 1 has no solution.**

The hypothesis is evaluated directly by `check_conditions(p,q)` (exact
integer arithmetic on two congruences), so the theorem covers *every*
non-double-Wieferich odd-prime pair at once — not just a searched range.

What it does **not** do: it says nothing about double-Wieferich pairs, which
exist (e.g. (83, 4871)) and are exactly where the known searches concentrate.
Closing the conjecture requires the deep descent over double-Wieferich pairs,
which is the gap `G-odd-descent` in `odd-prime-case.md` and is not part of
this skeleton.
