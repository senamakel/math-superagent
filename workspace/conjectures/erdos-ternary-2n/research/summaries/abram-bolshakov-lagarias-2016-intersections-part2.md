# Abram, Bolshakov & Lagarias, "Intersections of Multiplicative Translates of 3-Adic Cantor Sets II: Two Infinite Families"

Source: arXiv:1508.05967 (2015), published Experimental Mathematics (2016), DOI 10.1080/10586458.2016.1205532. Full text: `research/sources/abram-bolshakov-lagarias-2016-intersections-part2.full.md`. **Verified correct** (this is the real Cantor-set paper; an earlier guessed-URL fetch of arXiv:1508.05075 stored a Mont-Blanc HPC report and was overwritten with a correction note).

## Setup — exactly this run's fractal/dimension line

`Σ_{3,¯2} ⊂ Z_3` is the 3-adic Cantor set: 3-adic integers whose ternary expansion omits the digit 2 (the digit-{0,1} set), Hausdorff dimension `log_3 2 ≈ 0.63093`. The paper studies finite intersections of **multiplicative translates**:
```
C(M_1,…,M_n) := Σ_{3,¯2} ∩ (1/M_1)Σ_{3,¯2} ∩ … ∩ (1/M_n)Σ_{3,¯2},   1 ≤ M_1 < … < M_n integers.
```
The motivating object is the discrete dynamical system `x ↦ 2x` on `Z_3` and its **exceptional set**
```
E(Z_3) := { x ∈ Z_3 : the forward orbit {2^n x} meets Σ_{3,¯2} infinitely often }.
```

## What it establishes

- **Conjecture 1.2 (Exceptional Set Conjecture):** `dim_H(E(Z_3)) = 0`. The paper gives the machinery toward upper bounds.
- The sets `C(1, M)` are **3-adic path-set fractals**: their points' 3-adic expansions are labelled paths in a **finite automaton**, and the Hausdorff dimension is exactly `log_3 β` for β a real algebraic integer, computable from the automaton (spectral radius of its adjacency matrix).
- Two infinite families `P_k = 2·3^k + 1` and `Q_k = 3^{2k} − 3^k + 1` are worked out in full (Theorem 2.1–2.6): explicit automata, vertex counts, and Hausdorff dimensions.
- **Corollary 2.7 — the headline for this run:** `Γ* ≤ log_3 φ ≈ 0.438018`, φ = (1+√5)/2 the golden ratio. This is an improved upper bound toward the Exceptional Set Conjecture, sharpening the earlier `dim_H(E(Z_3)) ≤ 1/2`.
- **Proposition 3.2:** a right-resolving path-set presentation gives a computable Hausdorff dimension formula; **Proposition 3.4**: n-interleaving of a path set is a path set with explicit presentation growth; **Corollary 3.7**: interleaving preserves Hausdorff dimension.

## What it does NOT do — precise scope (the trap the problem warns about)

`dim_H(E(Z_3)) ≤ log_3 φ` is a **statement about the Hausdorff dimension of a set**, not a statement about which integers lie in it. `E(Z_3)` is a set of 3-adic points whose orbit hits `Σ` infinitely often; its dimension can be 0 or small while still containing, potentially, isolated points — and the powers-of-2 question is exactly whether `E` contains the specific point `1` (whose orbit is `{2^n}`) at all. A dimension bound says nothing by itself about whether `1 ∈ E(Z_3)` (equivalently whether infinitely many `2^n` are digit-{0,1}), and nothing about whether **some** `2^n` (even finitely many, i.e. the conjecture) is in `Σ`. So this is powerful structural background for the fractal line, not a proof route by itself.

## Method worth borrowing

The whole approach is **finite automata / path sets that describe the 3-adic digit expansions of points in `C(1,M)`**. This is the same symbolic-dynamics-on-the-3-adic-digits machinery the run's directed route ("symbolic invariant / automaton / transducer statistic") is pointed at — the intersection `C(1,2)` contains exactly the 3-adic limits relevant to `x ↦ 2x`, and its automaton is a concrete finite object to hunt an invariant on. Any transferable here is: the digit-{0,1} membership is a sofic/path-set condition, and its dimension is a computable spectral-radius quantity.

## Status

Sourced and verified — full primary text held under `research/sources/abram-bolshakov-lagarias-2016-intersections-part2.full.md`.

```claim
id: ABL-II-EXCEPTIONAL-SET-BOUND-PRIMARY
statement: (Corollary 2.7) The nesting constant Gamma* satisfies Gamma* <=
  log_3(phi) ~ 0.438018, phi the golden ratio. This is an upper bound toward the
  Exceptional Set Conjecture dim_H(E(Z_3)) = 0, where E(Z_3) = {x in Z_3 : the
  x->2x orbit meets the digit-{0,1} Cantor set Sigma infinitely often}.
hypotheses: x in Z_3; Sigma = 3-adic Cantor set (ternary digits in {0,1}).
holds-here: yes -- E(Z_3) is the limit set of the run's orbit-closure route;
  dim_H(E) <= log_3 phi < 1/2.
status: asserted-by-source (held primary, arXiv:1508.05967, Cor 2.7; proof in
  the paper, not re-derived here).
bearing: the fractal/dimension line's sharpest bound. It is a dimension bound
  on a set, NOT a statement about which integers lie in it (1 in E(Z_3) <=>
  infinitely many 2^n in Sigma; and even finitely many 2^n in Sigma is the
  unconquered question). Does not rule out a counterexample n>8 by itself.
anchor: research/sources/abram-bolshakov-lagarias-2016-intersections-part2.full.md
```

```claim
id: ABL-PATH-SET-DIMENSION-METHOD
statement: (Prop 3.2, 3.4, 3.7) The sets C(1,M) = Sigma ∩ (1/M)Sigma are
  3-adic path-set fractals whose points' 3-adic expansions are infinite labelled
  paths in a finite automaton; their Hausdorff dimension is exactly log_3(beta),
  beta a real algebraic integer = spectral radius of the automaton's adjacency
  matrix. n-interleaving of a path set is a path set with preserved Hausdorff
  dimension.
hypotheses: right-resolving path-set presentation.
holds-here: yes -- the finite automata on the 3-adic digits of C(1,M) are the
  concrete objects for the transducer/invariant route; dimension is a computable
  spectral-radius quantity.
status: asserted-by-source (held primary).
bearing: the method handle for the symbolic/automaton route. C(1,2) is the
  relevant intersection for x->2x; its automaton is a finite object to hunt an
  invariant on.
anchor: research/sources/abram-bolshakov-lagarias-2016-intersections-part2.full.md
```
