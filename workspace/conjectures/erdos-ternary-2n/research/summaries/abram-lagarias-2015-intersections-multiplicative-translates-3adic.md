# Abram & Lagarias, "Intersections of multiplicative translates of 3-adic Cantor sets" — NOT HELD

**Correction note.** The file `research/sources/abram-lagarias-2015-intersections-multiplicative-translates-3adic.full.md` was overwritten with a correction: a guessed arXiv URL (1405.5930) resolved to an unrelated n-Lie-algebras paper. The real Abram–Lagarias paper is **NOT in the library**.

## The real paper (from source metadata — not held, needs a verified fetch)

**W. C. Abram & J. C. Lagarias, "Intersections of multiplicative translates of 3-adic Cantor sets", J. Fractal Geom. 1 (2014), no. 4, 349–390. DOI 10.4171/jfg/11.**

What it studies (per repeated search-result summaries): the dynamical system `x ↦ 2x` on the 3-adic integers `Z_3`, and the **exceptional set**
```
E(Z_3) := { x ∈ Z_3 : the forward orbit {2^n x} meets the 3-adic Cantor set Σ_{3,¯2} infinitely often }
```
where `Σ_{3,¯2} = { 3-adic integers whose ternary expansion omits the digit 2 }` (the digit-{0,1} set, Hausdorff dimension `log_3 2 ≈ 0.63093`). It conjectures `dim_H E(Z_3) = 0` and had already established `dim_H E(Z_3) ≤ 1/2`. The paper builds the machinery: finite intersections
```
C(M_1,…,M_n) := Σ_{3,¯2} ∩ (1/M_1)Σ_{3,¯2} ∩ … ∩ (1/M_n)Σ_{3,¯2}
```
are **3-adic path-set fractals**, described by finite automata, with computable Hausdorff dimension `log_3 β`, β a real algebraic integer; it gives the automaton-construction method for (M_1,…,M_n) and computes dimensions for infinite families.

## Relevance to this run

This is the deepest held-frontier handle on the run's directed route (the ×2 orbit meeting the digit-{0,1} Cantor set S in Z_3). It is exactly the "Hausdorff dimension of digit-restricted sets in Z_3" gap flagged in problem.md. But it is a **dimension statement about a set**, not a statement about which integers lie in it — it does NOT by itself rule out a counterexample `n > 8`, per the precise caveat the problem demands be stated. A dimension-0 (or dimension-1/2) exceptional set still can (and since E(Z_3) is a countable phenomenon hidden by dimension, generally does) contain isolated integer points.

## Status

Lead only, corroborated by repeat search results. The `dim_H ≤ 1/2` and `dim_H E = ?` machinery and the `log_3 β` automata dimension formula are attributable to this source via abstracts, **but no full text is held**. Do not build on the exact constants without the primary.

```claim
id: ABRAM-LAGARIAS-EXCEPTIONAL-SET-BOUND
statement: (Search-result attribution) For the ×2 dynamical system on Z_3 and the
  digit-{0,1} Cantor set Sigma, the exceptional set E(Z_3) (x whose orbit meets
  Sigma infinitely often) has dim_H(E(Z_3)) <= 1/2 and is conjectured to have
  dimension 0; the intersections C(M_1,...,M_n) are 3-adic path-set fractals with
  computable dim = log_3(beta), beta algebraic.
hypotheses: x in Z_3; Sigma = digit-{0,1} set; orbit under x -> 2x.
holds-here: yes -- this is precisely the limit set of the orbit-closure route.
status: asserted-by-source (abstract-level; full text NOT held -- DO NOT build
  exact constants on this without the primary)
bearing: structural handle on the fractal/dimension line. A dimension statement
  about E(Z_3) does NOT locate which integers lie in it; it does not rule out a
  counterexample n > 8 by itself.
anchor: research/summaries/abram-lagarias-2015-intersections-multiplicative-translates-3adic.md
```
