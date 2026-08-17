# charp-point-count-mass-formula

```approach
idea: A good prime settles a degree (GVB / Graf-von-Bothmer: CA_{n,0} iff CA_{n,p} for one
prime p; Lu: |X_n(F_p)| = p for all large p iff CA holds). The run's route to certifying a
good prime is the bad-prime-minors criterion, which is infeasible at n=20 (C = binom(190,18)
~ 1e20). This line replaces the minor criterion with a character-sum point count: express
|X_n(F_p)|, the number of common zeros over F_p of the shared-root system, as a sum of Gauss
and Jacobi character sums (the standard closed form for the number of solutions of an
algebraic system over F_q), and read off directly whether it equals p. No minors, no
Gröbner basis -- a genuinely arithmetic, additive-combinatorics line, and char-p native by
construction.

mechanism: The shared-root system for degree n, over F_p, is the number of solutions
(a_1..a_{n-1}, r_1..r_{n-1}) in F_p with f(r_i) = 0 and H_i(f)(r_i) = 0, Hasse convention
(the convention the published bad-prime lists use). The point count of such a system is a
Jacobi-sum / character-sum sum: #Zeros = sum over the torus of product of additive
characters, evaluated by the standard "the number of common zeros is sum_x prod_i (1/|Fp|)
sum_psi conj psi(f_i(x))" identity, giving a sum of Jacobi sums over the monomial supports.
Because X_n(F_p) is a 1-dimensional variety (dim = 1 for large p, Lu), the count has the form
p * (leading term) + (Weil/Deligne error term), and CA iff the count is exactly p. The
structural content this line adds over the minor criterion: the count splits as (pure-power
line: p points) + (other components' points), and showing the other term vanishes is a
congruence/character-sum statement about the binomial coefficients, algebraically the same
data as the J_T minors but read through additive characters where the Weil bound and
Chevalley-Warning-style congruences apply at a lesser computational cost per prime. The
named theorems: the character-sum formula for solution counts, Weil's estimates, and
Chevalley-Warning/Ax-Katz congruences on the count.

precedent: None. (1) The anchor citation this line rests on — "Lu: |X_n(F_p)| = p for all
large p iff CA holds" — is NOT in the cited source. I read arXiv:1707.04754 (Lu 2017) in
full summary: it uses Combinatorial Nullstellensatz and Noether normalization to prove the
defining polynomials form regular sequences and calculates dimension; it makes no point-count
claim, no Lang-Weil estimate, no character/Jacobi-sum formula, and no |X_n(F_p)| = p
statement. (2) No CA source anywhere uses character sums or Jacobi sums for point counting;
searches for "Casas-Alvero character sum / Jacobi / point count" return only unrelated
Calabi-Yau/Fermat/Dwork hypersurface point-count literature that has never been connected to
CA. (3) The only point-count-adjacent result in the CA literature is the Lang-Weil-type
finitude expectation, and it goes the wrong way (see killed-by).

status: refuted

killed-by: Two independent failures, both factual. (A) The cited theorem does not exist. The
premise "Lu proves |X_n(F_p)| = p iff CA" is not in arXiv:1707.04754, and I found no source
establishing any such point-count criterion for CA. Grounding a line on a theorem the cited
paper does not contain is exactly the unsupported-bridge failure that closed
catalecticant-apolarity and q-derivative-deformation. (B) Even the point-count target is
mis-stated. The shared-root system V(R_1,...,R_{d-1}) ⊂ A^{d-1} is a ZERO-dimensional scheme:
CA over char 0 says V(I)_{bar-Q} = {0} (Schaub-Spivakovsky JCA 2025, ht(I) = d-1), and
Ghosh 2024 (arXiv:2402.18717) proves the arithmetic CA scheme has dimension at most 2 over
any field (claim ghosh-dim-bound; the char-0 "0-dimensional" strengthening rests only on
Ghosh's own unverified 2025 claimed proof, and is not needed here — the ≥ 2 dimension bound
already contradicts a uniform "1-dimensional" certificate), with the trivial pure-power point
included in the affine V but excluded from the projective X_d (GvB 2007 Prop 2.1). So a good
prime p
gives |V(I)(F_p)| = 1 (the origin), not = p, and X_d(F_p) empty (projective). The candidate's
"X_n is a 1-dimensional variety, count = p·(leading term) + error, CA iff count = p" is
contradicted by the held dimension facts on two counts: X_n is 0-dimensional (char 0) or
≤2-dimensional, never uniformly 1-dimensional, and the CA certificate is count = 1 (only the
pure-power point), not count = p. Character-sum formulas count points on toric/diagonal
hypersurfaces; the CA variety is neither toric nor a hypersurface, so the "standard closed
form" the mechanism invokes does not apply to it. Refuted on the absence of the anchoring
theorem and on a wrong-dimensional certificate; no first-step computation is worth running
because the target "count = p" it would verify is not the CA statement.

status: refuted

first-step: (tool_builder, exact over F_p, oracle-guarded with lib.casas_alvero.is_ca_hasse)
For n = 4,5,6 and a sweep of small primes p >= n: (1) compute |X_n(F_p)| by exact bounded
enumeration over F_p (oracle-bound), and independently compute the character-sum formula when
the monomial support structure allows it; (2) verify they agree, and verify the pure-power
line contributes exactly p; (3) verify the identity |X_n(F_p)| = p is equivalent to is_ca_hasse
holding over F_p (no counterexample). Report for which (n,p) the mass formula is computable
in poly(n) rather than brute force, and how big p can be before character-sum evaluation
costs more than it saves. Say what a bigger run would settle: whether at n=20 there is any
prime whose point count is provably p by this route (i.e. a certified good prime) without
the minor criterion.
```

## Why this is not a re-proposal

- `arithmetic-jet-lift` was refuted as a standalone because its proposed tool (the J_T minor
  criterion) is infeasible at n=20 and only certifies bad primes. This line proposes a
  DIFFERENT tool for the same end: a character-sum point count, which certifies goodness
  directly (the count = p) and is not the C x C minor wall. It is genuinely arithmetic
  (additive characters) rather than linear-algebraic (minors/Smith normal form).
- `deformation-obstruction-bad-points` was refuted for reading obstruction off the same M_T
  minors. This line does not touch M_T.
- No run approach has proposed point counting or character sums (Lu's paper mentions
  Lang-Weil only as a reduction, and it is a source, not a proposed attack).

## Char-p break / honesty

This line is char-p native: it is *only* a route to finding a good prime, and the honest
frame is that certifying goodness is exactly what the minors route could not do. The line
does not prove CA directly; it certifies one prime, then GVB closes. The "break" relative
to CA is not a hole in the argument but the fact that the method, like every good-prime
method, needs an actual prime where the count is exactly p, and that count is over F_p.

## Caveat

Speculative in exactly one place: whether the character-sum mass formula is tractable at
n=20. The first step is explicitly a feasibility probe at n=4,5,6 and large p, and the line
is honestly a *different route to the same good-prime conclusion*, not a stronger statement.
If the probe shows the character-sum evaluation also blows up past n~6, the line closes
with the measured boundary (a fact worth recording alongside the minor-criterion wall).
