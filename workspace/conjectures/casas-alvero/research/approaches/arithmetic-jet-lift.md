# Approach: obstruction-to-lifting = good-prime existence (synthesis)

Refined at convergence. The original proposal attacked CA through Buium's
p-derivations as the lift-obstruction theory. The lift-obstruction *framing*
survives; the p-derivation machinery is demoted, because the literature hands
us a strictly better tool for exactly this obstruction: the integer minors
`J_T` whose prime divisors are the bad primes. The adopted approach is the
synthesis of the two, and it is what research's actual content plus the
lift-obstruction reformulation jointly point at.

```approach
idea: One good prime settles a degree (GVB reduction mod p), so CA_{n,0} is
       equivalent to the existence of a prime p that is good for n. A prime is
       good iff p ∤ J_T for every scenario T, where J_T is the gcd of the C×C
       minors of the scenario matrix M_T (the regular-sequence determinant
       obstruction). Equivalently, CA_{n,0} ⟺ J(n) := ∏_T J_T ≠ 0: a single
       integer, uniformly defined from n, whose prime divisors are exactly the
       bad primes and whose nonvanishing is exactly CA over ℚ̄. The "obstruction
       to lifting a char-p witness" from the original jet-lift proposal is the
       p-adic reading of this same integer: v_p(J(n)) > 0 is the witness fibre
       (the non-liftability datum), and the bad prime p is the fibre over
       Spec 𝔽_p where the regular sequence degenerates.
mechanism: The resultants R_i (one per derivative) hit the Gröbner wall at
       d = 8 over ℚ, so conjecture-as-ideal-membership is infeasible to decide
       directly. The scenario/regular-sequence reformulation replaces the n−1
       resultants by n−1 homogeneous forms per scenario whose regularity is a
       determinant nonvanishing — and, decisively, the reduction-mod-p theorem
       collapses "CA over ℚ̄" to "find one good prime", which never requires a
       single Gröbner basis over ℚ. The char-0 content is exactly the statement
       J(n) ≠ 0 as an integer; the char-p falsehood is exactly p | J(n), and
       the witnesses x^{p+1} − x^p live in the resulting non-regular locus. This
       is the cleanest possible answer to the workspace's admissibility test:
       the char-p break is a named integer divisibility, not an after-the-fact
       search.
first-step: For n = 20 (smallest open degree), compute the exact certified-bad
       prime list from the binomial criterion (p | ((20 choose i) − 1) for some
       i, gmpy2, exact). That part is DONE — the 18 certified-bad primes
       {2,3,5,7,11,13,17,19,37,67,89,103,109,113,173,419,1223,15269} with
       candidates starting at 23 (research/notes/badprimes-criterion-n4-n20.md).
       The second part — testing candidate primes for GOODNESS by the minors
       criterion mod p — is now known INFEASIBLE: the minor criterion has a hard
       computational wall at n=6 (C=1365, D=2751, ~185 core-s/rank; full sweep
       ~2.2e5 core-hours), and at n=20 it is C = binomial(190,18) ~ 1e20, far
       past that wall (claim minors-criterion-feasibility-boundary, checked
       this attempt, code/n5/feasibility_boundary.py). So at n=20 the minors/
       rank route can certify BAD primes (via the sufficient binomial criterion)
       but can NEVER certify GOOD. Deliverable revised: a certified-bad list for
       n = 20 (held) and the honest frontier statement that goodness at n=20 is
       not reachable by the minor/rank criterion; any route to a good prime at
       n=20 must use a different method (e.g. scenario reduction of a type that
       shrinks C, or an analytic bound), which is an open sub-problem recorded
       in the Gaps below with this infeasibility as the obstruction it must beat.
charp-break: v_p(J(n)) > 0. In char p the integer J(n) is read as 0, the
       regular sequence degenerates, and the witness appears; there is no ring ℤ
       to carry the "some prime avoids the finite set of divisors" step. The
       one-directional reduction (char-0 counterexample ⟹ char-p witness) is
       the only char-0-only step, and it is exactly where J(n) ≠ 0 is used.
status: refuted
killed-by: non-distinct as a standalone attack — its engine (the J_T minor
      criterion, p bad ⟺ p | J_T) is the determinant form of the Ghosh scenario
      machinery that root-difference-coloring now renders explicit; the adopted
      line keeps the J_T criterion as its engine and provenance. Independently,
      the "find one good prime" reduction is not executable at the target: at
      n=20 the minors are C = binom(190,18) ≈ 1e20 (measured infeasible), and the
      sufficient binomial criterion certifies BAD primes only, never GOOD. Folded
      into research/approaches/root-difference-coloring.md.
precedent: gvb-lift (one good prime settles degree n), bad-prime-minors-criterion
       (p bad ⟺ p | J_T for some T), bad-prime-criterion (p | ((n choose i)−1)
       ⟹ bad), G-reformulation-equivalence + G-macaulay-rank (CA ⟺ all G_T
       regular ⟺ all J_T ≠ 0), computational-boundary (Gröbner wall d = 8 over
       ℚ). The equivalence CA_{n,0} ⟺ ∃ good prime ⟺ J(n) ≠ 0 is the synthesis:
       each ingredient is sourced, the assembly is this approach's own claim and
       must be re-verified computationally at n = 20 before it is relied on.
```
