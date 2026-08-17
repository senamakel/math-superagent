# uresultant-one-var-eliminant

```approach
idea: Replace the multivariate Gröbner basis of I = (R_1,...,R_{n-1}) subset Q[a_1..a_{n-1}]
(the run's measured d=8 wall) with a SINGLE univariate eliminant, Macaulay's u-resultant
(also the "generic linear form" / Cayley-trick resultant). Adjoin a generic linear form
u = a_1 + u_2 a_2 + ... + u_{n-1} a_{n-1} (or, better, eliminate everything down to a_1, the
centroid coefficient); the u-resultant is a UNIVARIATE polynomial in u whose roots are the
values of that linear form at the points of V(I). CA in degree n says V(I) = {0} as a
scheme (ht(I) = n-1, the single pure-power point of multiplicity the Bézout degree), which
is equivalent to: the u-resultant is a single power of one linear form. That is a
factorization certificate in ONE variable, checkable exactly for n much larger than the
Gröbner wall, because a univariate polynomial of degree (2n-1)!/n! is factorable where a
multivariate Gröbner base was not.

mechanism: V(I) is 0-dimensional with I = (R_1,...,R_{n-1}) the resultant ideal, and CA
says the only point is the origin (pure power). By Macaulay's theorem the u-resultant
Res_u(I) is nonzero and splits as prod_{P in V(I)} (u - u(P))^{mult(P)} (exactly if the
linear form separates points; otherwise with multiplicities). So Res_u(I) = c * (u-0)^B for
some integer power B iff V(I) = {0}, i.e. iff CA holds in degree n. The u-resultant is
computed as a single determinant (Macaulay / mixed-resultant matrix, or via the sparse
resultant / Cayley trick), not by running a full Gröbner basis. Its factorization is a
univariate integer/factorial check. This sidesteps the d=8 Gröbner wall and gives a *new
certificate* for the small degrees the run already verified, extendable toward the actual
boundary. Char-p: reduce the u-resultant's coefficients mod p; the char-p witnesses appear
as ADDITIONAL linear factors (or higher multiplicities) -- p | leading structure -- so the
good/bad prime distinction is exactly "does Res_u mod p stay a pure power." This ties the
bad-prime story to a new univariate object rather than the infeasible C x C minors. The
named theorem is Macaulay's u-resultant / the Cayley trick (resultants as determinants),
with the char-0 content being "single linear form" versus the char-p "extra factors."

precedent: macaulays-u-resultant, (classical, sourced:, the, u-resultant, =, resultant, of,
the, system, augmented, by, a, generic, linear, form, factors, over, C, into, linear,
factors, whose, zeros, are, the, common, affine, roots, of, the, system;, Lazard's,
determinant/generator, form,, the, Macaulay-matrix, construction, with, the, generic-linearform, column;, Emiris-Pan-Tsigaridas, "Algebraic, Algorithms", arXiv:1311.3731, §4.3, "Polynomial, System, Solving, by, Using, Resultants", and, the, Ayad-Farés-Ayyad, and,
Jónsson-Vavasis, treatments, of, the, Macaulay, u-resultant, for, zero-dimensional, systems);
ca-univariate-eliminant-precedent, (diaz-toca-gonzalez-vega, 2006, Maple, proceedings, —
held, note, research/sources/diaz-toca-gonzalez-vega-2006.full.md:,, the, run's, ≤7,
verification, bound, Anderson, size, field, originated, EXACTLY, as, a, univariate, eliminant,
computation, in, Maple, corroborated, by, Draisma-de-Jong, survey, and, Castryck-, et-al, —
so, the, univariate-eliminant, representation, is, not, new, to, CA, and, its, measured,
ceiling, is, d=8, (Groebner-wall, of, the, same, run,, verified-boundary, thread,));,
v(i)-0-dimensional, (schaub-spivakovsky, JCA, 2025:, ht(I), =, d−1,, so, V(I), is,
0-dimensional, in, char, 0;, the, premise, the, u-resultant, requires, and, the, reason, the,
pure-power, factorization, is, a, legitimate, certificate).

status: adopted

adopted-by: inventor convergence turn. The other two candidates were refuted on research's
grounding (multiplicity-index-avoidance: dimension count fails — the true freedom is the
(n-1)-dim coefficient space, and it is the run's own negative control; charp-point-count:
the anchor theorem is absent from its source and the point-count target is wrong-dimensional).
The u-resultant is the survivor: the theorem is real, its hypotheses hold (V(I) 0-dimensional,
CA ⟺ V(I)={0} ⟺ Res_u(I) = c·u^B), and it is distinct from every closed predecessor (not
the full Gröbner fan of tropical-resultant-fan, whose correct premise V(I)={0} it certifies;
not the multivariate primary-decomposition of generic-initial-ideal; not the C×C minors of
bad-prime-minors). The honest open payoff — does a univariate eliminant outrun the d=8 wall?
— is kept, but the value added over Diaz-Toca-Gonzalez-Vega 2006 is a certificate that paper
never read: the exponent B as a scheme multiplicity, tested against the complete-intersection
identity B = ∏_i ord_0(R_i).

why-still-open: The reformulation is genuine and the theorem's hypotheses hold here (V(I)
is 0-dimensional, CA ⇔ V(I)={0}, so Res_u(I) = c·u^B). What is NOT established is the
advertised payoff — "factorable for n much larger than the Gröbner wall". The closest
precedent, Diaz-Toca-Gonzalez-Vega 2006, is itself a univariate-eliminant computation whose
measured ceiling was d=8, exactly the wall this line claims to beat; a univariate eliminant
of degree (2n-1)!/n! is astronomically large (n=8: 15!/8! ≈ 1.6e7; n=13: 25!/13! ≈ 1.6e12)
and may be as hard to factor as the multivariate GB it replaces. The value is as a NEW
CERTIFICATE (scheme multiplicity from the exponent B) for degrees the run already verifies,
and an honest re-mapping of the univariate-vs-multivariate feasibility boundary — not,
on present evidence, a route past d=8. Ground the name and theorem; leave the payoff bound
open and cheap to probe at n=4,5,6,7,8.

status: adopted

first-step: (tool_builder, exact sympy/Singular, oracle-guarded with lib.casas_alvero
is_ca / is_ca_hasse) (1) For n = 4,5,6,7,8 build I_n = (R_1,...,R_{n-1}) over Q (R_i =
Res_x(f, H_i f), Hasse, integer coefficients), compute the u-resultant in a generic linear
form (naive eliminant in a_1 by repeated resultants where feasible), and FACTOR it. (2)
Confirm the result is a single power of the linear form (u - u(0))^B, i.e. V(I) = {0},
matching CA for those n — this is a NEW certificate, stronger than the Gröbner existence
verification. (3) THE MULTIPLICITY CHECK (the novel content): verify the exponent B equals
∏_{i=1}^{n-1} ord_0(R_i), the product of the orders (lowest-weight/initial-term degrees) of
the generators at the origin — the complete-intersection Samuel multiplicity of I at 0,
computed independently from each R_i's initial form under the weighted order, NOT from the
u-resultant. HYPOTHESIS-CAVEAT (recorded from research): (R_1..R_{n-1}) is a regular
sequence at 0 in degrees 4..8 (CA holds there ⟺ V(I)={0} ⟺ ht(I)=n-1, Schaub-Spivakovsky),
so the Samuel identity applies; but B = ∏ ord_0(R_i) is the Valabrega-Valla equality and is
STRICTLY STRONGER than CA — it can fail in a degree where CA still holds (non-CM associated
graded). So treat equality as a consistency / good-CM confirmation, and a mismatch as
evidence about gr_{m_0}, NOT as a CA counterexample and NOT as a refutation of the main
Reformulation Res_u = c·u^B (which depends only on V(I)={0}). This is a new application, not
a new theorem (the underlying identity is classical: Macaulay/Lazard u-resultant multiplicity
+ Valabrega-Valla 1978 product-of-orders). (4) Reduce mod p for the bad
primes and the char-p witnesses: confirm extra linear factors appear mod p (Res_u no longer
a pure power), record the first p where it ceases to be c·u^B and how B changes
(B_p ≠ ∏ ord_0(R_i) mod p), reading the good/bad frontier off the univariate object. (5)
Record the wall: the largest n where the univariate eliminant factors exactly vs where the
multivariate Gröbner stopped. Say what a bigger run would settle: whether Res_u is exactly
factorable (certifying CA) for some n >= 13 that the scenario/Gröbner method needed char-p
or weeks for.
```

## Why this is not a re-proposal

- `tropical-resultant-fan` was refuted (false premise V(I) = emptyset; actually V(I) = {0})
  and died on computing the whole Gröbner fan. This line uses only ONE univariate eliminant,
  not the full fan, and V(I) = {0} is exactly what it certifies, so the correct premise is
  its target, not its downfall.
- `generic-initial-ideal` (already proposed, open) computes the multivariate gin -- a
  different, multivariate object. This line is the univariate u-resultant, distinct.
- `arithmetic-jet-lift` and `bad-prime-minors` work off the C x C minor matrices (infeasible
  at n=20). The u-resultant is a single univariate polynomial, factored exactly, a strictly
  smaller object; even if it too stops at some n, the factorization structure for n <= 10 is
  a new recorded fact.
- The run verified CA for small degrees by Gröbner/minors but never looked at the univariate
  eliminant's factorization as a certificate; that is the new representation.

## Char-p break (admissibility test)

Located and named: in char p the u-resultant acquires extra linear factors / higher
multiplicities corresponding to the char-p counterexample locus (the witness x^{p+1}-x^p is
an extra point of V(I) mod p), so Res_u mod p is NOT a pure power -- p divides the structure
that makes it one over Z. The char-0 statement "Res_u is a pure power" fails mod p exactly.
This is the named divisibility; it is the same bad-prime content as the minors criterion but
carried by a univariate object.

## Caveat

The likely cost ceiling is unmeasured and probably larger than d=8 but not necessarily all
the way to 20 -- honestly an extension of the verification boundary, not a proof of CA. Its
value as a partial result is the exact factorization certificates for every n it reaches,
which is stronger (scheme multiplicity, not just existence) than the Gröbner verification,
and the mapping of how far the univariate route outruns the multivariate one.
