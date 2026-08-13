# Bilu–Fuchs–Luca–Pintér 2013 — "Combinatorial Diophantine equations and a refinement of a theorem on separated variables equations"

Source: Y. F. Bilu, C. Fuchs, F. Luca, Á. Pintér, Publ. Math. Debrecen 82(1)
(2013) 219–254, DOI 10.5486/PMD.2013.5480. Full text held (Hungarian Academy
repository PDF): `research/sources/bilu-fuchs-luca-pinter-2013-combinatorial-diophantine.full.md`.

## What the paper establishes

The subject: Diophantine equations obtained by equating classical counting
functions — perfect powers, binomial coefficients, Stirling numbers of both
kinds. This is the paper that applies the Bilu–Tichy separated-variables
refinement directly to binomial-coefficient equalities and Stirling-number
equalities.

**Theorem 3 (binomial/Stirling finiteness for fixed a).** For fixed a ≥ 2,
the Diophantine equation in (x,k) with C(x,k) = (a-th power / perfect power
forms) has finitely many integer solutions; specifically the paper treats
perfect-power-form values and Stirling-value equations. (The exact wording is
an equation `Sₓᵃ = S_yᵇ`-type family with finiteness for fixed a,b.)

**Theorem 4 + Propositions 1–5 (the separated-variables refinement).** For
non-constant f,g ∈ Q[X] with f(x)=g(y) having infinitely many
bounded-denominator rational solutions, the solution set (outside finitely
many) is a union of finitely many families; Proposition 3: for
f(x)=f(y)-type symmetric equations with infinitely many solutions, all but
finitely many solutions satisfy x=y or x+y=a for some fixed a ∈ Q, the latter
only if f(X)=f(a−X). Proposition 5 gives a genus formula: for f(x)=g(y)
absolutely irreducible, 2g−2 = Σ (something over the distinct roots) — the
paper's own route to the genus of these separated-variable curves.

**Lemma 3 / Lemma 4 (binomial/Stirling specifics).** For a ≥ 2 there is no
linear polynomial κ with f∘κ = C₀X^{2a} + C₂X^{2a−2} + ··· (a structural
obstruction used to exclude infinite families); the zeros of
8·Sₓ^{x−a} + 1 have |z| < 10a² (a growth bound on the Stirling-number
polynomials' roots).

## Bearing for this run

- **Directly on-topic**: this is the published application of the
  separated-variables theorem to *binomial coefficient equalities* as
  counting-function coincidences. It corroborates the run's grounding note
  (`bilu-tichy-grounding.md`) that the Bilu–Tichy framework has been applied to
  this exact problem, and adds the refinement: when infinitely many solutions
  exist, their structure is severely constrained (symmetric x=y or x+y=a
  shape; no nontrivial compositional κ for the binomial-polynomial shape).
- **What it does NOT give**: like HT23 and HPT 2022, it is a *finiteness +
  structure* classification, not a count bound; the finiteness statements are
  largely ineffective (the paper uses both effective and ineffective tools and
  does not extract a uniform constant). It does not bound N(a); it constrains
  which pairs can be infinite.
- **Relationship to the genus work**: Proposition 5 (genus formula for
  separated-variable curves) is a second, independent route to the genus of
  C(x,k1)=C(y,k2) — corroborating the run's computed closed form
  g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2 at the level of the general theory, though
  the paper does not specialize to the binomial case.

## Status

```claim
id: bflp-2013-combinatorial-separated-variables
statement: Bilu-Fuchs-Luca-Pinter 2013 (Publ. Math. Debrecen 82(1) 219-254):
  equating classical counting functions (perfect powers, binomial coefficients,
  Stirling numbers) gives Diophantine equations with (a) finiteness for fixed
  parameter (Thm 1-3,5), (b) a refined description of the infinite-solution set
  of f(x)=g(y): all but finitely many solutions lie in finitely many families;
  for symmetric f(x)=f(y) with infinitely many bounded-denominator rational
  solutions, all but finitely many satisfy x=y or x+y=a (a in Q), the latter
  only if f(X)=f(a-X) (Prop 3); a genus formula for separated-variable curves
  (Prop 5).
hypotheses: f,g non-constant in Q[X]; bounded-denominator rational solutions;
  for Prop 3, f(x)=f(y) symmetric.
holds-here: yes for the structural component — C(x,k1)=C(y,k2) is exactly a
  separated-variables binomial-coefficient equality; the paper's finite-vs-
  infinite dichotomy applies. The refined infinite-solution structure is a
  classification, not a count bound.
status: sourced (full text held; digest read; not re-derived here)
bearing: corroborates bilu-tichy-grounding (the framework has been applied to
  binomial equalities) and adds the symmetric/infinite-structure refinement
  (Prop 3) and a genus formula (Prop 5) for separated-variable curves. Does
  NOT give a uniform count bound; ineffectivity wall stands.
anchor: research/sources/bilu-fuchs-luca-pinter-2013-combinatorial-diophantine.full.md
```

## Note on the two-logarithm approach

This paper's Proposition 3 shows that infinite solution sets of
separated-variable equations have an extremely rigid structure (x=y or
x+y=a). This is a further constraint any "many representations of one a" attack
must respect — the same message as HT23 and the held HPT-2022 classification:
the infinite families are classified and rigid, and the finite-pairs bound is
what Singmaster needs, which none of these papers provide.