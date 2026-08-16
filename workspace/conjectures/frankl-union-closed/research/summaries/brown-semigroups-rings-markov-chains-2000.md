# Brown, "Semigroups, rings, and Markov chains" (2000)

Source: https://arxiv.org/pdf/math/0006145 (Kenneth S. Brown, 2000; adapted from
the 1998 paper "Semigroups, Rings, and Markov Chains" and a 1996
arXiv:math.RT/9610001). Full text:
`research/sources/brown-semigroups-rings-markov-chains-2000.full.md`.

## What this source is

The canonical ring-theoretic treatment of random walks on **left-regular bands**
(LRBs). A left-regular band (LRB) is a finite semigroup in which every element is
idempotent and every element acts as a left zero on its product (a simplified
form of the semigroup governing random walks). The associated **support lattice**
L — the lattice of joins of elements — is where all the structure lives. The
paper generalises Bidigare–Hanlon–Rockmore's theory of random walks on
hyperplane chamber sets.

## Why it matters here (the adopted Möbius-algebra approach)

The run's adopted approach (`research/approaches/mobius-algebra-join-irreducibles.md`)
works in the **Möbius algebra** `C[L, ∨]` of a lattice — the semigroup algebra of
the join-semilattice `(L, ∨)`, with product `x·y = x∨y` — and uses the primitive
orthogonal idempotents
`e_a = Σ_{b≥a} μ(a,b)·b`
(only `b ≥ a` contribute). This is **exactly Brown's equation (16)**:

```
e_X = Σ_{Y≥X} μ(X,Y)·Y      (16)
```

The paper proves (Theorem 3, Bidigare; and the surrounding text at lines
1180–1220): the `e_X` (X ∈ L) form a **basis of kL consisting of pairwise
orthogonal primitive idempotents** (`e_X² = e_X`, `e_X e_Y = 0` for `X≠Y`), and
the map `φ: kL → functions on L`, `φ(X) = Σ_{Y≥X} δ_Y`, is the Möbius-inversion
isomorphism. In `C[L,∨]` the semigroup algebra is split semisimple — it is
(isomorphic to) a product of `|L|` copies of `C` — and the `e_a` are its
primitive idempotents, giving `x = Σ_{b≥x} e_b` by Möbius inversion.

This is the **primary source** the run needs to ground the claim that the
idempotent expansion and the semisimplicity of `C[L,∨]` are standard and
correct. The run had previously verified the expansion numerically in
`code/out/mobius_algebra_check.py` but had no source for it; it now has one.

```claim
id: brown-idempotent-expansion
statement: In the Möbius (semigroup) algebra of a (semi)lattice L, the elements
  e_X = Σ_{Y≥X} μ(X,Y)·Y (X ∈ L) form a basis of pairwise orthogonal primitive
  idempotents: e_X² = e_X, e_X e_Y = 0 for X ≠ Y. Consequently the algebra is
  split semisimple (a product of |L| copies of the field), and by Möbius
  inversion every basis element x expands as x = Σ_{b≥x} e_b — into exactly
  |↑x| of the idempotents.
hypotheses: L a finite lattice (or meet/join semilattice), field of
  characteristic 0; μ the Möbius function of L. Product is the join.
holds-here: true — this is the exact construction used in the adopted
  mobius-algebra approach.
status: sourced (Brown 2000, eq. 16, pp. 20–21)
bearing: grounds the two "checkable facts" the Möbius-algebra approach rests on:
  dim(left ideal L·a) = |↑a| and basis element a populates exactly |↑a| of the
  |L| primitive idempotents. Poonen's lattice form of Frankl then reads: some
  join-irreducible j is at most half-populated in the idempotent decomposition.
anchor: research/sources/brown-semigroups-rings-markov-chains-2000.full.md
  lines 1180–1220 (eq. 16); verified computationally in
  code/out/mobius_algebra_check.py.
```

## The rest of the paper (context, not directly used)

Theorems 0–7 establish that the transition matrix of an LRB random walk is
diagonalizable, give its eigenvalues `λ_X` and multiplicities, and identify the
primitive idempotents of the walk algebra `R[w]` (grouped by eigenvalue in the
non-generic case). Applications: random walks on maximal chains of a
distributive lattice, matroid walks, q-analogues of the Tsetlin library. These
are not used by this run.

## What it implies for this run

- The semisimplicity / idempotent-basis fact the mobius-algebra approach relies
  on is now **sourced and primary** (Brown, not Knop).
- It does **not** by itself prove the forcing step ("the join-irreducibles
  cannot all be >½-populated"): that remains the open hinge, with no precedent
  found either in Brown or in Bouchard (who works in the same lattice
  formulation but not through the idempotent basis).
