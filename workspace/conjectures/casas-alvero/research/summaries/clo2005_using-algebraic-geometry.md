# Cox–Little–O'Shea, *Using Algebraic Geometry* (GTM 185, 2e, 2005)

<!-- source: https://eclass.uoa.gr/modules/document/file.php/D231/Papers/Cox-UsingAlgebraicGeometry.pdf | converted from PDF -->

> **Instrument-tier reference** for the two tools the problem directive names:
> resultants (Ch. 3) and Gröbner bases with elimination/weighted orders
> (Ch. 2). This note replaces the prior PDF-fragment stub; the full text is at
> `research/sources/clo2005_using-algebraic-geometry.full.md`. It is a
> textbook, so everything here is classical fact held as a reference — it does
> not change CA's status.

## What it establishes (statements this run uses)

**Resultants.** Theorem 2.3: for degrees d₀,…,d_n there is a *unique*
multivariate resultant Res ∈ ℤ[u_{i,α}] characterised by (a) the homogeneous
system has a nontrivial solution over ℂ iff Res = 0; (b) Res(x₀^d₀,…,x_n^d_n)=1;
(c) Res is irreducible. For linear system Res = det(c_{ij}). The multivariate
resultant of a well-constrained square system is a single determinant
(Macaulay/mixed matrix), giving the run an exact certificate object.

**u-resultant (van der Waerden).** For f₁=…=f_n=0 with total degrees bounded
by d₁,…,d_n, no solutions at infinity, all multiplicities one, add
f₀ = u₀+u₁x₁+…+u_nx_n. Proposition 5.8: there is a nonzero constant C such
that
$$Res_{1,d_1,\ldots,d_n}(f_0,\ldots,f_n) = C\prod_{p\in V(f_1,\ldots,f_n)} f_0(p),$$
and with V = {p_i=(a_{i1},…,a_{in})}, eq (5.9):
$$= C\prod_{i=1}^{d_1\cdots d_n}(u_0 + a_{i1}u_1 + \cdots + a_{in}u_n).$$
So the u-resultant factors over ℂ into linear factors whose coefficient
vectors are the common roots — "compute the u-resultant, factor it, read off
the solutions." Computed as a quotient ±D₀/D′₀ (Macaulay-matrix determinant).

**Elimination / Extension Theorems** (Ch. 2 §1 overview, proofs in [CLO] Ch. 3):
for lex order x₁>…>x_n, G ∩ k[x_{ℓ+1},…,x_n] is a Gröbner basis of the ℓ-th
elimination ideal I_ℓ; a partial solution extends to a full one over ℂ when the
leading-coefficient polynomials of a lex basis do not all vanish.

## Bearing on the run

- Prop 5.8 / eq (5.9) is the **classical statement backing the adopted
  `uresultant-one-var-eliminant` approach**: for I=(R₁,…,R_{n−1}) ⊂ Q[a], the
  u-resultant Res_u(I) splits over ℂ into linear factors ∏_{P∈V(I)}(u−u(P)),
  and "V(I)={0}" ⟺ that split is a single power c·(u−0)^B. It corroborates
  `uresultant-theorem-held-source` (Emiris–Pan–Tsigaridas §4.3) from a second,
  independent canonical source. Proof is given over K = ℂ(u₀,…,u_n), so the
  factorisation is valid with u's as variables and applies as a scheme
  certificate.
- **Caveat recorded for the run**: Prop 5.8 as stated assumes *all
  multiplicities one and no solutions at infinity*. CA's V(I) is a single
  scheme point of multiplicity B (the Samuel multiplicity ∏ ord₀(Rᵢ) under
  the weighted order), so the factorisation must be read with multiplicities —
  the run's exponent B, not the distinct-solutions form. This is exactly the
  distinction the `uresultant-converge` thread must honour: B = ∏ ord₀(Rᵢ) is
  the Valabrega–Valla equality, strictly stronger than CA, and a mismatch is
  gr_{m₀} evidence, not a counterexample.
- The Elimination/Extension Theorems are the textbook basis for the
  Diaz-Toca–Gonzalez-Vega / Castryck et al. elimination computations that
  settle d ≤ 12, and for the run's scheme picture (eliminate the rᵢ from
  f(rᵢ)=f^{(i)}(rᵢ)=0).
- Weighted monomial orders are **not** a major topic of this text (the run's
  weighted-order instrument is separately anchored by EoM "Gröbner basis" and
  the de Frutos Marín thesis); CLO's Ch. 2 covers lex/glex/grlex, and the
  weighted grading used for ord₀(Rᵢ)=n(n−i) is sourced elsewhere.

```claim
id: clo-uresultant-factorization
statement: CLO GTM 185 Prop 5.8 / eq (5.9): for a well-constrained square
  system f1=...=fn=0 with bounded total degrees, no solutions at infinity and
  all multiplicities one, the u-resultant Res_{1,d1..dn}(u0+u1x1+...+unxn,
  f1,...,fn) = C * prod_{p in V} (u0 + a_{i1}u1 + ... + a_{in}un), i.e. it
  factors over C into linear factors whose coefficient vectors are exactly the
  common roots; computed as a Macaulay-matrix determinant quotient. This is the
  classical Macaulay/van der Waerden u-resultant theorem behind the adopted
  uresultant-one-var-eliminant approach.
hypotheses: char-0/C coefficient field; square system; no solutions at
  infinity; all multiplicities one (CA's V(I) needs the multiplicity-aware
  reading, see note)
holds-here: yes — V(I)=(R1..Rn-1) subset Q[a] is 0-dimensional (ht(I)=n-1,
  Schaub-Spivakovsky JCA 2025), so the u-resultant factorisation structure
  applies; the multiplicity-free form is strengthened to a single power c*u^B
  for CA
status: proved (textbook theorem; corroborates uresultant-theorem-held-source
  from a second source)
anchor: research/sources/clo2005_using-algebraic-geometry.full.md (Prop 5.8,
  eq 5.9, lines ~7860-7990; Thm 2.3; Elimination/Extension Theorems lines
  ~1942-1994)
follows-from: resultant-theory, elimination-theorem
contradicts: nothing — confirms, from an independent canonical source, the
  u-resultant factorization the run's uresultant approach rests on
answers: (load-bearing instrument grounding for uresultant-one-var-eliminant
  and thread uresultant-converge)
```

*See also* the EoM "Resultant" note for the univariate Poisson product formula
and the EoM "Gröbner basis" note for weighted and elimination orders; the full
text is 37,091 lines — reach it by grep or map, never whole.
