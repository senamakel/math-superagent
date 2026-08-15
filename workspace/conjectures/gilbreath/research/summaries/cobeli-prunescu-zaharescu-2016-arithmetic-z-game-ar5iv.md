# Cobeli, Prunescu & Zaharescu 2016 — "A growth model based on the arithmetic Z-game"

**Full text:** `research/sources/cobeli-prunescu-zaharescu-2016-arithmetic-z-game-ar5iv.full.md`
**Source:** https://ar5iv.labs.arxiv.org/html/1511.04315 (arXiv:1511.04315 [math.NT]); journal version Chaos Solitons Fractals 91 (2016) 136–147, doi 10.1016/j.chaos.2016.05.016.

## What it is

The multiplicative companion to the 2014 Cobeli–Zaharescu game. Same atomic rule `Z(a,b)=ab/gcd(a,b)²`, applied to neighbors to grow a triangular matrix `T_𝒢`. The new ingredient: the analysis of the **west edge** (left column) of the matrix grown from ℕ\* (the positive integers) and from ℙ (its squarefree part), with a complete description of the **2-tomography** and an explicit, **fully solved** characterization of the west edge's structure near powers of 2.

## Why it is the *counterpart of Gilbreath's conjecture* (the load-bearing link)

The Z-rule is per-prime an **absolute difference of exponents**: `ν_p(Z(a,b)) = |ν_p(a) − ν_p(b)|`. So the whole game decomposes into independent **p-tomographies**, each an absolute-difference (mod-2 / Rule-90 / Pascal) evolution of the exponent rows.

> "At the exponents level, this is the counterpart of the Gilbreath's Conjecture [Guy A10], which refers to the similar process that starts with the sequence of primes ... Gilbreath's Conjecture says that the west edge of [that] triangle ... contains only ones."

In the Z-game the west edge is `W_ℕ* = 1,2,3,6,5,15,105,70,1,5,33,55,65,273,1001,…` (OEIS A222311 after sorting). The analogue of GC is:

> **Conjecture 2 (CZ 2014 §9):** the west edge of the triangle from ℕ\* contains only **squarefree** numbers (no prime-square divides any west term).

This paper proves a strong special case and the surrounding structure.

## Main results (all proved in the paper)

- **Theorem 1 + Corollary 1 (complete 2-tomography, west edge clean at powers of 2):** the 2-valuation of the west edge is exactly
  `v₂(W_ℕ*(m)) = 1 if m = 2^k (k≥1), else 0`. So on the west edge, 2 never appears with exponent ≥ 2.
- **Corollary 2 (solves a Sloane question, A222313):** there is **no 4** on the west edge of T_ℕ*. (This is the first nontrivial case of Conjecture 2.)
- **Theorem 2 (eventual periodicity of odd tomography):** for every odd prime p, the rows of `v_p(T_ℙ)` are eventually periodic, with pre-period just row 1 and period length dividing `2^{ind_p(2)} − 1`. Small periods: π₂=1, π₃=3, π₅=15, π₇=7, π₁₁=341, π₁₃=819, π₁₇=255, π₁₉=9709.
- **Theorem 3 (explicit west-edge values near powers of 2):** exact product formulas for `W_ℙ(2^g−1)`, `W_ℙ(2^g)`, `W_ℙ(2^g+1)`, with worked values W_ℙ(64)=3·7·11···61 (12 factors), W_ℙ(65)=65, W_ℙ(66)=2145, W_ℙ(256)=·37·… etc.
- **Structure:** the 2-tomography rows group into slices S_k of 2^{k−1} rows, whose nonzero cells are Pascal-mod-2 triangles P₂(2^{k−1}, t) with weights reading the "bubbled" sequence `β(w₁) = v₂` gaps — a clean Sierpinski/Rule-90 tiling.

## The mechanism (formal-power-series side)

Passing from one generation to the next = multiplying the 𝔽₂ series by `(1+X)/X`, then dropping the meromorphic part and constant term (the `Δ` projection, justified because the west edge has no left influence). This is the same `(1+X)/X` operator the run's mod-4 linearization uses modulo 2; here because the game is purely exponent-level, the mod-2 law is *exact* rather than a congruence ceiling, so the whole thing is solvable.

## Why it matters for this run

1. **A third, independent primary source for "the {0,2}/mod-2 regime is linear iff it is genuinely an exponent-level game."** The Z-game's west edge is provably structured (squarefree, no 4, explicit powers-of-2 values) precisely because each prime evolves independently by the exact mod-2 difference law. In Gilbreath the entries are *integers*, not exponents of a squarefree base, so the absolutely-difference law is only a mod-4 *congruence*, not an identity — which is exactly why GC has no such closed form. This is the cleanest available statement of why the sibling problems are solved and Gilbreath is not.
2. **Corroborates the run's proved `rule90-interior-xor` and `mod4-linearization`.** The Pascal/Rule-90 tiling, the `(1+X)^m` binomial law, and the Glaisher power-of-2 counts are here developed at length and in a primary peer-reviewed source; the same facts drive the run's {0,2}-interior analysis.
3. **Conjecture 2 (west edge squarefree) is an open analogue to Gilbreath** — of the same "left-edge stabilisation" shape — and Corollary 2 (no 4) is its proved v₂=0 refinement. It gives a second instance (besides GC) of a left-edge "all-equal" conjecture against which the run's invariants could be stress-tested: any invariant forcing the prime-triangle west edge to {1} has a counterpart forcing this west edge to {squarefree}, and here part of it is proved.
4. **Growth/self-similar vocabulary for the "block length grows" direction.** The paper is fundamentally about how a left/edge sequence grows in self-similar waves near powers of 2 — the same qualitative phenomenon as the run's measured block-length growth — in a setting where it is completely analysed. It does NOT contain a block-length-regeneration theorem (b_k is Gilbreath-specific), so `block-growth-literature-not-covered` still stands; but it is a strong structural precedent.

**Status:** sourced (full text held), peer-reviewed (Chaos Solitons Fractals 2016). West-edge values cross-checked by this run against the paper's own Table 1 and §5 examples.
