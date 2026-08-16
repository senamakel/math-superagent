# Abram & Lagarias, "p-Adic path set fractals and arithmetic" — HELD IN FULL

Source: arXiv:1210.2478 (2012; J. Fractal Geom. 1 (2014) no.1, 45–81).
Full text: `research/sources/abram-lagarias-padic-path-set-fractals.full.md`
(83 KB, converted from the arXiv PDF — this is a *primary* text, the
foundational paper of the p-adic path-set-fractal theory that the run's ×2/×3
orbit-closure route uses).

## What it establishes (proved in the paper)

The class `C(Z_p)` of **p-adic path set fractals**: closed subsets of `Z_p`
whose p-adic expansions are the infinite label sequences of paths in a finite
labeled automaton `(G, v_0)` starting at a distinguished initial vertex. Main
theorems, all proved here:

- **Theorem 1.1 (Hausdorff dimension).** For `Y ∈ C(Z_p)` with standard
  presentation `Y = (f̅_p, G, v_0)`, the Hausdorff dimension `d_H(Y)` is
  computable; it is the matrix dimension of the construction matrix of the
  graph (the `α ≥ 0` with spectral radius of the `α`-power matrix equal to 1).
- **Theorem 1.2 / 1.4 (arithmetic closure).** `C(Z_p)` is closed under p-adic
  *addition* of p-integral rationals `r ∈ Q ∩ Z_p` and under *multiplication* by
  p-integral rationals — the result is again a p-adic path set fractal, with
  computable presentation.
- **Theorem 1.3 (Minkowski sum).** The set-valued (Minkowski) sum of two
  p-adic path set fractals is again one.
- **Theorem 2.10.** `C_G(Z_p) = C(Z_p)`: p-adic path set fractals are exactly
  the objects of p-adic geometric graph-directed constructions.

These are **purely p-adic phenomena** — analogous closure under real addition /
multiplication does not hold for real graph-directed fractals.

## Why it matters here

The 3-adic Cantor set `Σ_{3,¯2}` (ternary digits in {0,1}, omitting 2) — the
digit-restricted set `S` of problem.md — is a p-adic path set fractal. So under
`x ↦ 2x` the orbit-closure approach is: the sets
`C(M_1,…,M_n) = Σ ∩ (1/M_1)Σ ∩ … ∩ (1/M_n)Σ` (points whose ×2 orbit and its
first n multiples all land in the digit-{0,1} set) are path-set fractals with
computable Hausdorff dimension `log_3 β`. This is the machinery behind
Abram–Lagarias Part I (JFG 2014 no.4) and the `dim_H E(Z_3) ≤ log_3 φ` bound.

**Caveat (must be stated):** a dimension statement about the set `E(Z_3)` of
orbit points is *not* a statement about which integers `n` have `2^n` in the
digit set. A dimension-`< 1` (or dimension-0, if the conjecture holds)
exceptional set can still contain isolated integer points. The p-adic
path-set machinery computes *dimensions* of digit-restricted sets; it does not
by itself find or rule out a specific counterexample `n > 8`.

```claim
id: ABRAM-LAGARIAS-PADIC-PATHSET-CLOSURE
statement: The class C(Z_p) of p-adic path set fractals is closed under p-adic
  addition and multiplication by p-integral rationals and under Minkowski
  addition; each member has computable Hausdorff dimension equal to the matrix
  dimension of its construction matrix. C_G(Z_p) = C(Z_p).
hypotheses: finite labeled automaton presentations (G, v0); p-adic expansions
  as path labels; p-integral rational scalars.
holds-here: yes -- supplies the automaton/dimension machinery for the 3-adic
  Cantor (digit-{0,1}) set under multiplication by 2 in Z_3.
status: proved in the primary source.
bearing: structural handle on the orbit-closure route: digit-restricted sets
  under x->2x are path-set fractals with computable dimension. A dimension
  statement locates the fractal structure, NOT which integers lie in the set;
  it does not by itself rule out a counterexample n>8.
anchor: research/sources/abram-lagarias-padic-path-set-fractals.full.md
```

## Status

Primary source, held in full, foundational for the p-adic path-set-fractal
method. Its closure theorems and dimension formula are the theory the
Abram–Lagarias exceptional-set bounds rest on.
