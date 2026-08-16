# Yakubovich, *Polynomial problems of the Casas-Alvero type* (J. Classical Analysis 4(2), 2014, 103–120) — survey tying CA to Abel–Gontcharoff / Sz.-Nagy analysis

Source URL: http://files.ele-math.com/articles/jca-04-07.pdf (open access PDF; landing page is doi:10.7153/jca-04-07). Full text: `research/sources/yakubovich2014_casas-alvero-type-survey.full.md`.

A survey + new-analysis paper focused exactly where the run's adopted `root-difference-coloring` thread lives: the **Abel–Gontcharoff polynomial** representation of f, the **Sz.-Nagy identities** relating the roots of f and its derivatives, and the real-rooted case of CA. Complementary to the held Yakubovich 2013 Abel-Gontcharoff paper and 2025 validity paper.

## Claims that bear on this run

```claim
id: y2014-ab-goncharoff-ca-representation
statement: Write f in the Abel–Gontcharoff form f(z) = G_n(z) built from the nodes
  (common roots) z_0,…,z_{n−1}; then by scaling z↦αz (α>0 with |z_ν|<α^{−1}),
  CA for arbitrary common roots reduces to CA for common roots in the unit circle
  (Prop 1): the conjecture holds iff it holds on the unit circle.
hypotheses: char 0, CA-polynomial f of degree n, Abel–Gontcharoff nodes = the shared roots
holds-here: yes — this is the unit-circle reduction used to normalise common roots
status: proved-by-source (Prop 1, final section on CA-polynomials)
bearing: gives the exact normalisation the root-difference-coloring thread needs: it may
  assume the shared roots lie in the unit disc.
anchor: research/sources/yakubovich2014_casas-alvero-type-survey.full.md (Prop 1)
falsifies: a CA-polynomial whose common roots are not all in any one disc but, scaled into
  one, becomes a counterexample — Prop 1's proof rules this out.
```

```claim
id: y2014-real-rooted-ca-holds
statement: The Casas-Alvero conjecture holds for polynomials with only real roots: under
  the Abel–Gontcharoff expansion a real-rooted non-trivial CA-polynomial would force
  the sequence x_0⪰x_1⪰…⪰x_{n−1} of common roots to be stationary, contradicting Rolle
  (Prop 2, via Lemma 10 and Corollary 9). Equivalently (Cor 11): a real-rooted counterexample,
  if any, has at least 5 distinct zeros.
hypotheses: char 0, f has only real roots, {x_ν} the shared-root sequence with f^{(s+ν)}(x_ν)≠0
holds-here: yes — confirms the real-rooted case already listed in problem.md
status: proved-by-source (Prop 2, Cor 11)
bearing: the "real-rooted case known" lead becomes a held primary proof, and the
  ≥5-distinct-roots constraint is obtained for the real-rooted subcase by Rolle/Abel-Gontcharoff
  rather than by Gauss–Lucas.
anchor: research/sources/yakubovich2014_casas-alvero-type-survey.full.md (Prop 2, Cor 11)
falsifies: exhibiting a real-rooted non-trivial CA-polynomial.
```

```claim
id: y2014-sz-nagy-root-derivative-identity
statement: For f monic of degree n≥2, the Sz.-Nagy type identities (Lemma 1, eq 15) relate the
  roots of f and of its m-th derivative: n(n−1)(x_{n−1}−x_{n−2})² = r_*D² + r^*(λ^*−x_{n−1})² +
  Σ r_j(λ_j−x_{n−1})², etc., where D = |λ_{s_0}−x_{n−1}| and the r_j are multiplicities. These
  give the span/multiplicity inequalities (43), (45) constraining l(m)+l(m+1) for a real-rooted
  CA-polynomial, and Props 3–5 give explicit necessary inequalities (44), (46), (47) on span(f)
  and D that a real-rooted counterexample would have to satisfy.
hypotheses: f monic degree n≥2, real roots, shared-root structure as defined in §4
holds-here: yes — these are exactly the root/derivative sum-of-squares identities the
  root-difference-coloring thread computes.
status: proved-by-source (Lemma 1, Lemma 2; Props 3–5)
bearing: provides the exact identities (15)/(25) and the necessary inequalities for the
  real-rooted counterexample the run's thread is testing; a place to check the run's own
  Sz.-Nagy-ish verification against.
anchor: research/sources/yakubovich2014_casas-alvero-type-survey.full.md (Lemma 1–2, Props 3–5)
falsifies: a real-rooted CA-polynomial violating (44), (46), or (47).
```

```claim
id: y2014-trivial-iff-double-root-n-2
statement: A polynomial with only real roots of degree n≥2 is trivial iff its (n−2)-nd
  derivative has a double root (Cor 1); and a degree-n≥3 polynomial with ≥2 distinct roots
  whose (n−2)-nd derivative has a double root must have at least one complex root (Cor 2).
hypotheses: char 0, real roots / general f
holds-here: yes
status: proved-by-source (Cors 1–2)
bearing: a clean real-rooted obstruction: any real-rooted f with ≥2 roots and a double root in
  f^{(n−2)} would be a (forbidden) counterexample, so it must be complex.
anchor: research/sources/yakubovich2014_casas-alvero-type-survey.full.md (Cors 1–2)
```

## What it does not settle
Does not settle CA for complex (non-real) polynomials in any degree; the degree-20 open case
is untouched. The real-rooted case is already known from earlier sources; this is a proof of it
by Abel–Gontcharoff/Rolle rather than a new family of settled degrees. Props 3–5 are necessary
(not sufficient) conditions on a hypothetical real-rooted counterexample.

## Relation to the run
This is the primary source closest to the adopted `root-difference-coloring` thread: it supplies
the Abel–Gontcharoff form, the Sz.-Nagy identities, and the unit-circle reduction (Prop 1) that
the thread's verification script exercises. The held full text lets the thread check its own
identity verification against a published derivation.
