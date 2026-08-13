# Superelliptic curves: definition, ramification, and the genus formula

Encyclopedic entry: Wikipedia "Superelliptic curve" (retrieved this cycle)
Full text: `research/sources/wikipedia-superelliptic-curve.full.md`
Primary anchor for the genus formula: A. V. Sutherland, "Counting points on
superelliptic curves in average polynomial time", Open Book Series 4 (2020)
403-422, https://arxiv.org/abs/2004.10189
Full text: `research/sources/sutherland-counting-superelliptic-2004.full.md`

## Definition

A superelliptic curve is a cyclic branched covering C → P¹ of degree m ≥ 2
(coprime to the characteristic), equivalently given by an affine model

    y^m = f(x),  f ∈ k[x], deg f = d ≥ 3,

with each root of order < m. m=2 is hyperelliptic (elliptic for d=3,4);
m=3 is a trigonal curve. Kummer theory: the function field extension k(C)/k(x)
is a Kummer extension.

## Ramification and branch points

Let B' be the roots of f. The branch set of the cover is

    B = B'  if m | deg f,  else  B = B' ∪ {∞}.

At an affine root α of order r_α (1 ≤ r_α < m), the ramification index is
e = m/(m, r_α), over (m, r_α) points. At infinity, with
r_∞ = ms − deg f (s = ⌈deg f / m⌉), (m, r_∞) = (m, deg f), and the curve is
unramified over ∞ iff m | deg f.

## The genus formula (Riemann–Hurwitz)

    g = (1/2) ( m(|B| − 2) − Σ_{α∈B} (m, r_α) ) + 1.

For f squarefree of degree d, this reduces to the standard closed form
(Shorey–Tijdeman; Sutherland eq. (1); both MSE/BMSST references in library):

    g = ((d−2)(m−1) + m − gcd(m, d)) / 2.

## Cross-check against this run's computed genus table

The run computed (Singular + Sage agreement) the small-column rows of
genus C(x,k1)=C(y,k2). The literature formula reproduces them:

- **{2,n} pair**: y(y−1) = 2C(x,n), i.e. (2y−1)² = 1+8C(x,n), hyperelliptic
  m=2, d=n:  g = ((n−2)(1) + 2 − gcd(2,n))/2 = (n − gcd(2,n))/2 = ⌊(n−1)/2⌋.
  Matches the run's claimed closed form for {2,n} and all 10 recorded table
  values (n=3..12).
- **{3,n} pair**: Y³ − Y = 6C(x,n), Y=y−1, cyclic trigonal m=3, d=n:
  g = ((n−2)(2) + 3 − gcd(3,n))/2 = (2n−1 − gcd(3,n))/2, i.e. n−1 if 3∤n,
  n−2 if 3|n. Matches the run's claimed closed form for {3,n} and all 21
  recorded table values (n=4..24).
- **{4,n} pair**: NOT a direct superelliptic cover (2:1 cover of
  w²=1+24C(x,n)); the formula applies to the base curve only. The run's
  recorded {4,n} genus values are consistently larger than the base genus, as
  Riemann–Hurwitz requires for a ramified double cover; a cover-genus
  computation is the residual step.

Checked by code/genus/verify_superelliptic_formula.py (all 31 literature
cross-checks pass).

## Diophantine consequences (as recorded by the entry)

- Integer points on y^m = f(x) reduce (Siegel identity) to a Thue equation;
  Shorey–Tijdeman: for f with ≥ 2 distinct roots, m≥3, the equation has only
  finitely many integer solutions (m,x,y) with |y|≥2, bounded by an
  effectively computable constant depending only on f; for ≥ 3 distinct roots
  the same holds with m≥2. These are the effective superelliptic results in the
  same family as de Weger/BMSST but indexed by f rather than by the column pair.

## Claims

```claim
id: superelliptic-genus-formula
statement: A superelliptic curve y^m = f(x), f squarefree of degree d>=3,
  m>=2 (tame), has genus g = ((d-2)(m-1) + m - gcd(m,d))/2 (Riemann-Hurwitz;
  Shorey-Tijdeman; Sutherland 2020 eq. (1)). Applied to the binomial-column
  pairs: {2,n}: C(y,2)=C(x,n) has genus floor((n-1)/2) (hyperelliptic); {3,n}:
  C(y,3)=C(x,n) has genus n-1 if 3 does not divide n, else n-2 (cyclic
  trigonal). These reproduce the run's Singular/Sage-computed table values for
  n=3..12 (row 2) and n=4..24 (row 3) with zero mismatches.
hypotheses: f squarefree (the binomial RHS polynomials C(x,n) are squarefree
  up to the recorded n); tame cover (p ∤ m); formula is for the smooth
  projective model.
holds-here: yes for the {2,n} and {3,n} rows; the {4,n} row is a ramified 2:1
  cover of the hyperelliptic base, so the plain formula does not directly give
  it.
status: checked (formula sourced; reproduction verified against recorded
  computed table)
bearing: gives the run's small-column genus closed forms (a GOAL.md deliverable)
  a citable primary anchor, and ties the genus growth to the Faltings threshold
  for the effective-bounds discussion.
anchor: research/sources/wikipedia-superelliptic-curve.full.md;
  research/sources/sutherland-counting-superelliptic-2004.full.md;
  code/genus/verify_superelliptic_formula.py
```