# Skeleton — the odd-prime case (the open content)

```skeleton
goal: x^p - y^q = 1 has no solution in integers x,y >= 2 with p,q odd primes.
implies: Take any hypothetical solution (x,p,y,q) with p,q odd primes.
      G-odd-cassels forces p | y and q | x. G-odd-wieferich, applied to that
      same solution, then forces the double-Wieferich conditions
      p^(q-1) = 1 (mod q^2) and q^(p-1) = 1 (mod p^2). G-odd-descent asserts
      that no (x,p,y,q) with p,q odd primes can satisfy the conjunction
      [p|y, q|x, p^(q-1)=1 mod q^2, q^(p-1)=1 mod p^2, x^p - y^q = 1].
      The three lemmas form a chain, the last link closing the argument, so the
      hypothetical solution cannot exist.
status: sketched
rests-on: (none — fresh run)
```

```gap
id: G-odd-cassels
lemma: For p,q odd primes and x,y >= 2, x^p - y^q = 1 implies p | y and q | x.
       (Cassels, 1960.)
status: open
known-solution: p = 2 even, so the hypothesis excludes (3,2,2,3); the lemma is
       silent about it. The conclusion happens to hold there too (2|2, 3|3),
       which is fine: it is a *necessary* condition, not a "no solution" claim.
next: rederive using the two factorisations x^p - 1 = y^q in Z[zeta_p] and
      y^q + 1 = x^p in Z[zeta_q]. In Q(zeta_p) the prime (1-zeta_p) is the
      unique ramified prime and the ideals (x - zeta_p^i) are pairwise coprime
      off it; the q-th-power valuation of y^q there forces p | v_p(y), and the
      mirror argument forces q | v_q(x). Run the valuation computation in
      symbolic_math for a few small odd (p,q), then record Cassels 1960 as a
      sourced claim block. Falsifier: it must hold at (p,q)=(2,3) only
      trivially/externally, and must never claim p|y *because* p=2.
```

```gap
id: G-odd-wieferich
lemma: For p,q odd primes and x,y >= 2, x^p - y^q = 1 implies
       p^(q-1) = 1 (mod q^2) and q^(p-1) = 1 (mod p^2).
       (Inkeri / Hyyrö refinement of Cassels; this is the "double-Wieferich
       pair" condition driving all computational searches.)
status: open
known-solution: hypothesis fails at p = 2, so the lemma does not apply to
      (3,2,2,3). Check the numbers anyway as the reverse falsifier:
      2^(3-1) = 4 != 1 (mod 9) and 3^(2-1) = 3 != 1 (mod 4), so the known
      solution does NOT satisfy the conclusion — exactly as it must, since the
      lemma only speaks about odd primes.
next: rederive from G-odd-cassels by the p-adic / cyclotomic-unit argument
      (the second descent: p | y forces x^p = 1 mod p^2 and a unit relation in
      Z[zeta_q] yields p^(q-1) = 1 mod q^2). Then implement check_conditions(p,q)
      evaluating both congruences by exact integer arithmetic and calibrate so
      that (2,3) is excluded by hypothesis. Confirm the exact statement against
      a primary source (librarian) before trusting the exponent/placement.
```

```gap
id: G-odd-descent
lemma: There is no solution x^p - y^q = 1 with p,q odd primes, x,y >= 2
       satisfying p | y, q | x, p^(q-1) = 1 (mod q^2), q^(p-1) = 1 (mod p^2).
       (Equivalently, by the two gaps above: no solution at all with p,q odd
       primes. This is the deep content — Mihăilescu's 2002 class-group step.)
status: open
known-solution: p = 2 even, hypothesis excludes (3,2,2,3); silent there.
next: this is the open content and has no cheap direct move; the structure is a
      minus-class-group argument in Q(zeta_p) via the Stickelberger ideal and
      cyclotomic units. First move today: (a) file research request REQ-1 for
      the exact statement of Mihăilescu's descent step; (b) in parallel,
      symbolic_math computes the minus class group of Q(zeta_p), Q(zeta_q) for
      the known odd double-Wieferich pairs (e.g. (83,4871)) to see which
      p-/q-Sylow relations hold, so the claim's hypotheses can be checked as
      soon as its statement lands.
```

## Note on the conditional theorem already implied here

G-odd-cassels and G-odd-wieferich alone give a genuine, checkable conditional
result: **if (p,q) is NOT a double-Wieferich pair, then x^p - y^q = 1 has no
solution.** That is exactly the shape of GOAL.md's second deliverable ("a proof
for all odd prime exponent pairs satisfying a stated, checkable condition"),
and it is provable from two classical, re-derivable lemmas — it does not wait
on the deep descent. G-odd-descent is what would remove the condition and close
the conjecture.
