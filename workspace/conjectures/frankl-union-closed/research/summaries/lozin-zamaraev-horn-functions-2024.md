# Lozin & Zamaraev — "Union-closed sets and Horn Boolean functions" (JCTA 202, 2024)

**Source URL:** https://wrap.warwick.ac.uk/id/eprint/180696/1/1-s2.0-S0097316523000869-main.pdf · **Full text:** [[lozin-zamaraev-horn-functions-2024.full]]

## What it establishes

A **Boolean-function approach** to the union-closed sets conjecture — a genuinely
new formulation not previously in the library. A union-closed family `F` of
subsets of universe `U` corresponds to the set of **false points** of a **Horn
Boolean function** `f : {0,1}^U → {0,1}`; the transposed (intersection-closed)
statement becomes: a Horn function has a *good* variable, one that appears in at
most half the false points. The conjecture is verified for:

- **Submodular functions** (those both Horn and co-Horn; all prime implicants
  linear or quadratic pure Horn) — Theorem 3: they satisfy Frankl's conjecture.
- **Double Horn functions** (with the dependency property on their Horn DNF) —
  Theorem 4: any non-trivial Boolean function admitting a Horn DNF with the
  *dependency property* satisfies the conjecture.
- A reduction (Lemma 1): if Conjecture 3 holds for Horn functions without linear
  prime implicants, it holds for all Horn functions.
- Lemma 2: if a variable `x` never appears negatively in a Horn DNF of `f`, then
  `x` is good for `f`.

The paper notes the conjecture is verified for lattices (lower semimodular) and
graphs (chordal bipartite) and adds these Boolean-function classes; it remains
**open for bidual Horn functions**.

## Why it matters

This is a new restricted class (the run's GOAL item 4 asks for "a natural class
not previously covered"). The Horn-function phrasing is structurally different
from the lattice and graph forms already held, and the "dependency property"
(Theorem 4) is a named sufficient condition the run could attack or extend. It is
also a fresh angle on the negative control: the false-point / good-variable
translation is the intersection-closed dual, so any argument here must respect
which side it is on.

```claim
id: lozin-submodular-fc
statement: Submodular Boolean functions satisfy Frankl's union-closed sets
  conjecture; equivalently every submodular Boolean function (both Horn and
  co-Horn, all prime implicants linear or quadratic pure Horn) has a good
  variable appearing in at most half its false points.
hypotheses: F union-closed finite; represented as false points of a submodular
  Boolean function.
holds-here: yes — a settled restricted class via the submodular/Horn formulation.
status: asserted-by-source (peer-reviewed JCTA 202; proof not re-derived by the
  run's oracle).
bearing: adds submodular Boolean functions to the settled-class list; new
  Boolean-analytic formulation distinct from the lattice/graph forms already held.
anchor: research/sources/lozin-zamaraev-horn-functions-2024.full.md
```

```claim
id: lozin-double-horn-dependency
statement: Any non-trivial Boolean function that admits a Horn DNF with the
  dependency property (each negative prime implicant involves at most one
  negative literal, in the exact sense defined in the paper) satisfies Frankl's
  conjecture; double Horn functions are a subclass where the property holds.
hypotheses: f non-trivial Boolean function with a Horn DNF satisfying the
  dependency property; F = set of false points of f is union-closed-equivalent.
holds-here: yes — a named sufficient condition for UC via Boolean functions.
status: asserted-by-source (peer-reviewed JCTA 202).
bearing: the dependency property is a candidate sufficient condition the run
  could generalise or find a counterexample to; bidual Horn is flagged open.
anchor: research/sources/lozin-zamaraev-horn-functions-2024.full.md
```

## Notes on verification
Both are asserted-by-source; the run's oracle checks only small `n ≤ 4` and does
not re-derive these. The Horn-function ↔ false-points equivalence (Theorem 1)
is elementary and could be oracle-checked by encoding a small union-closed family
as a Horn function and verifying the good-variable ↔ abundant-element match —
a cheap independent check a later computation pass could run.
