# u-resultant certificate `B = ∏ ord_0(R_i)`: novelty and regular-sequence status

Focused question (not a survey): for the adopted `uresultant-one-var-eliminant`
approach, is checking `B = ∏_{i=1}^{n-1} ord_0(R_i)` (u-resultant exponent =
complete-intersection Samuel multiplicity at 0) a genuinely NEW check, and is
`(R_1,…,R_{n-1})` a regular sequence at 0 in degrees 4..8?

## Verdict on novelty — split it into theorem vs application

**The underlying identity is classical, not new.** Two named theorems, both sourced:

1. **Macaulay u-resultant / Lazard**: for a zero-dimensional system, `Res_u(I)`
   factors over ℂ as `∏_{P∈V(I)} (u−u(P))^{mult(P)}`, so when `V(I)={0}` it is
   `c·u^B` with `B` = the scheme multiplicity of the origin. Standard elimination
   theory (van der Waerden, Lazard; Canny–Kaltofen–Lakshman 1989; Ayad–Farés–Ayyad 2012;
   Bürgisser 2026 restates the evaluation/Poisson form). Not an open claim.

2. **Samuel multiplicity of a complete intersection = product of the orders of
   initial forms**, under a specific hypothesis. Let `(R,m)` be a regular local
   ring and `f_1,…,f_m` a regular sequence. Then
   `e(R/(f_1,…,f_m)) ≥ ∏ ord(f_i)`, with **equality iff the initial forms
   `f_1^*,…,f_m^*` form a regular sequence in `gr(R)`** — equivalently
   `gr_m(R/(I))` is Cohen–Macaulay (the Valabrega–Valla condition; cf. Valabrega–Valla
   "Form rings and regular sequences", Nagoya 1978; Rossi–Valla multiplicity of
   t-isomultiple ideals; Engheta "multiplicity of a complete intersection is ∏ d_i").
   So `B = ∏ ord_0(R_i)` is *not automatic* from regularity: it is exactly the
   statement that the associated graded ring is CM / the leading forms cut out 0
   as a complete intersection.

**The application to the CA resultant ideal is not in the literature.**
No Casas-Alvero source computes the u-resultant exponent `B` or compares it to
`∏ ord_0(R_i)`. The CA/elimination line tops out at:
- the regular-sequence reformulation `(R_1,…,R_{d-1})` regular seq ⟺ CA
  (Schaub–Spivakovsky 2023/2025, §1 and JCA 2025; equivalently `V(I)={0}`), and
- Ghosh's complete-intersection program on the homogeneous `G_{T,i}` sequences,
  and the bad-prime/minor criteria — none read off a univariate eliminant
  exponent or compare it to initial orders.

So: the *check as applied to CA is new* (a fresh, cheap certificate for small
degrees), but it specialises a classical, known identity; there is no new theorem
being asserted. Diaz-Toca–Gonzalez-Vega 2006 computed a univariate eliminant for
d≤8 but only to establish existence/*CA-ness*, never the exponent `B` vs `∏ ord`.

## Regular-sequence status at 0 in degrees 4..8 — YES (it holds)

`K[a_1,…,a_{n-1}]` is a Cohen–Macaulay ring. In the run's normalised setup
(fixing the shift so `a_1,…,a_{n-1}` parametrise, pure power ↦ origin),
CA in degree n ⟺ `V(I) = {0}` ⟺ the d−1 generators `R_1,…,R_{n-1}` have height
`n−1`. Since the number of generators equals the height in a CM ring, `R_1,…,R_{n-1}`
is a **regular sequence** (this is precisely Schaub–Spivakovsky's Conjecture 3 /
the reformulation they prove equivalent to CA). Because CA is verified in degrees
4..8 (`V(I)={0}` confirmed), the sequence is regular **globally, hence in the
localisation at the maximal ideal `m_0`** — regular at 0. The certificate's
hypothesis therefore holds in 4..8.

## Caveat the run must record (else it misreads a negative)

`B = ∏ ord_0(R_i)` is **stronger** than regularity: by Valabrega–Valla it needs
`gr_{m_0}(K[a]/(I))` Cohen–Macaulay / leading forms regular. It can **fail in a
degree where CA still holds**, and a mismatch `B ≠ ∏ ord` there is *evidence the
associated graded is not CM, not a counterexample to CA* and not a refutation of
the approach's main reformulation (`Res_u = c·u^B`, which depends only on
`V(I)={0}`). So as a certificate the identity is useful as a consistency check and
a "good-CM" confirmation at the small degrees, but it is **not equivalent to CA**
and failing it does not fail CA.

## Sources

- Valabrega–Valla, *Form rings and regular sequences*, Nagoya Math. J. 1978 —
  initial-forms-regular ⟺ multiplicity = product of orders.
- Lê Dũng Tráng, *Linear systems and multiplicity of ideals* (Samuel: multiplicity
  of M-primary ideal, CM ⇒ e = length); Rossi–Valla, *Multiplicity and t-isomultiple
  ideals* (1988).
- Lazard (u-resultant multiplicity); Canny–Kaltofen–Lakshman 1989; Ayad–Farés–Ayyad
  2012 (u-resultant factorization into linear factors with solution multiplicities).
- Schaub–Spivakovsky, *A note on the CA conjecture* arXiv:2312.08742 (§1, Remark 4:
  CA ⟺ (R_i) regular sequence) and JCA 2025 (Theorem 5 partial: top three R_i ∉ radical).
- Engheta, *Bound on the multiplicity of almost complete intersections* (2009),
  for the statement that a complete intersection has multiplicity ∏ deg.

## Status

Application to CA: new (not previously done). Underlying identity: classical.
Regular at 0 in 4..8: yes (by CA-verified ⟹ V(I)={0} ⟹ CM-height argument).
Equivalence of the certificate to CA: **no** — the certificate is strictly stronger.
