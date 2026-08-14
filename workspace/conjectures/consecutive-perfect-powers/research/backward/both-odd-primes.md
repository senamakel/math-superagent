# The odd-prime case: Cassels -> double Wieferich -> exclusion

```skeleton
goal: x^p - y^q = 1 has no solution with p,q odd primes.
implies: Let (x,p,y,q) be a solution with p,q odd primes. G-Cassels gives p|y and q|x. G-double-wieferich turns those two divisibilities into the congruences p^{q-1}≡1 (mod q^2) and q^{p-1}≡1 (mod p^2). G-exclude states that no solution of the equation can satisfy both congruences. Chain: solution ⇒ Cassels ⇒ double Wieferich ⇒ contradiction, hence no such solution. The known solution (3,2,2,3) has p=2, outside every hypothesis here, so no lemma in this file claims there are no solutions at all.
status: sketched
rests-on: none (research/CLAIMS.md is empty; every lemma below is open)
```

```gap
id: G-Cassels
lemma: If x^p - y^q = 1 with x,y>0 and p,q odd primes, then p | y and q | x.
status: open
next: librarian fetches Cassels (1960, "On the equation a^x - b^y = 1") for the proof; theorem_prover formalises the statement in Lean/Mathlib. The known solution has p=2, so it is excluded by hypothesis (no conflict with 3^2-2^3=1). Check the direction p|y, q|x before trusting it downstream.
```

```gap
id: G-double-wieferich
lemma: If x^p - y^q = 1 with x,y>0 and p,q odd primes, then p^{q-1} ≡ 1 (mod q^2) and q^{p-1} ≡ 1 (mod p^2).
status: open
next: derive from G-Cassels via the cyclotomic factorisation x^p - 1 = ∏_{i=1}^{p-1}(x-ζ_p^i) in Z[ζ_p]; symbolic_math computes the ideal factorisation and what p|y forces about the ideals (x-ζ^i), theorem_prover formalises the resulting congruence. The librarian must confirm the exact index pairing against Mihailescu (2002) before this lemma is used — the problem.md placeholder "p^2 | y^{p-1}-1" does NOT match the known solution and is not the right form.
```

```gap
id: G-exclude
lemma: There are no integers x,y>0 and odd primes p,q with x^p - y^q = 1 satisfying both p^{q-1} ≡ 1 (mod q^2) and q^{p-1} ≡ 1 (mod p^2).
status: open
next: this is the genuinely hard step, and the equation must do the work — the double-Wieferich congruences alone do not exclude all pairs, so the cyclotomic structure is needed. First concrete move: symbolic_math computes, in Z[ζ_p], what the congruences force about the ideals (x-ζ^i) and the cyclotomic-unit/class-group relation, producing the precise obstruction statement; that statement is then handed to theorem_prover. Until the statement is precise, the exact form of the final step (Thaine's theorem / cyclotomic units) is a research request for the librarian rather than a task.
```
