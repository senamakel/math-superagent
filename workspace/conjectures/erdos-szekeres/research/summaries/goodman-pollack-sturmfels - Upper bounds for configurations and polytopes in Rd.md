# Goodman–Pollack–Sturmfels, "Upper bounds for configurations and polytopes in R^d"

<!-- source: https://dl.acm.org/doi/10.1007/BF02187696 | full text at
     research/sources/goodman-pollack-sturmfels - Upper bounds for configurations and polytopes in Rd.full.md -->

**Publication.** J. E. Goodman, R. Pollack, and B. Sturmfels, *Discrete & Computational Geometry*
(1990), DOI 10.1007/BF02187696 (also STOC 1989).

## The main theorem — order-type enumeration is astronomically out of reach

**Theorem (Goodman–Pollack–Sturmfels).** The number of *realizable order types* of simple
(no-three-collinear) configurations of $n$ points in $\mathbb{R}^d$ is at most
$n^{d(d+1)n}$. The number of labeled combinatorial types of simple configurations is at most
$n^{2d^2 n}$.

In the plane, $d=2$, this gives at most $n^{6n}$ realizable order types of $n$-point sets.

**Corollary (the quantitative reason enumeration is hopeless here).** At the open case
$n=32$ (the ES(7) bound $2^{5}+1=33$): at most $32^{192}$ realizable order types. No
enumeration over all 32-point order types can ever settle ES(7). This is the fact behind the
problem statement's "the order-type count at 32 points is astronomically beyond any search."

Also: at most $n^{d(d+1)n}$ combinatorially distinct labeled simplicial polytopes with $n$
vertices in $\mathbb{R}^d$, improving the previous $n^{c n d/2}$.

## Why it matters for this problem

The run works over order types (rank-3 chirotopes / oriented matroids). Two consequences:

1. **Enumeration is not a method at n=32.** Any computational attack on ES(7) must be a
   SAT/CP-SAT encoding over *orientation variables with transitivity axioms*, not a search
   over the order-type database (which only reaches small $n$ — Aichholzer et al. cover $n\le10$).
   This is exactly the Balko–Valtr / Scheucher / Dumitru route the library already holds.

2. **Realizability is the obstacle.** $n^{6n}$ counts *realizable* order types; the abstract
   chirotopes are far more numerous and most are NOT realizable. Realizability of an order
   type (stretchability of its pseudoline arrangement) is $\exists\mathbb{R}$-complete
   (Shor 1991; Kim–de Mesmay–Miltzow arXiv:2301.03221). So an abstract-chirotope upper bound
   is stronger than the geometric conjecture and may be false — exactly what Balko–Valtr found
   (their counterexamples are non-pseudolinear / unrealizable abstract colorings).

## claim block

```claim
id: order-type-count-enumeration-hopeless
statement: The number of realizable order types of simple n-point configurations in the plane is at most n^{6n} = 32^{192} at n=32, so exhaustive enumeration over all 32-point order types is astronomically infeasible; the ES(7) case cannot be settled by brute force over order types.
hypotheses: simple (no-three-collinear) planar point configurations, up to order type.
holds-here: true — this is the exact setting of the ES conjecture (general position = simple order type).
status: proved (Goodman–Pollack–Sturmfels, DCG 1990, DOI 10.1007/BF02187696).
bearing: justifies the mandatory SAT/CP-SAT-over-orientation-variables route and rules out order-type enumeration as a method at n=32; contextualizes that only n≤10 order types are catalogued (Aichholzer et al.).
anchor: research/sources/goodman-pollack-sturmfels - Upper bounds for configurations and polytopes in Rd.full.md
```

```claim
id: realizability-etr-complete
statement: Deciding whether an abstract order type (chirotope, oriented matroid of rank 3) is realizable by real planar points is ∃R-complete (equivalent to stretchability of pseudoline arrangements); abstract chirotopes are far more numerous than realizable ones and a combinatorial upper bound over all abstract order types is stronger than the geometric conjecture and may be false.
hypotheses: rank-3 oriented matroids / abstract order types; realizability by points in R^2.
holds-here: true — the ES conjecture is about REALIZABLE point sets, so the pseudolinearity/4-tuple-realizability constraint is essential in any encoding.
status: proved/sourced (Shor 1991; Kim–de Mesmay–Miltzow arXiv:2301.03221; corroborated by Balko–Valtr's non-pseudolinear counterexamples).
bearing: any SAT/CP-SAT or chirotope upper-bound argument must encode 4-tuple realizability, or it proves something false; the Balko–Valtr counterexamples live in the unrealizable abstract space.
anchor: research/sources/fox-pach-sudakov-suk - ES-type theorems for monotone paths and convex bodies - PLMS 2012.full.md (hypergraph setting); research/sources/goodman-pollack-sturmfels ... full.md
```
