# Goodrich, Mbirika & Nielsen, "New methods to find patches of invisible integer lattice points" — Involve 14:2 (2021) 283–310, full text on disk

Source: https://people.uwec.edu/mbirika/paper_lattice_point_visibility.pdf (author's copy of the published version; DOI 10.2140/involve.2021.14.283). Full text at `research/sources/goodrich-mbirika-nielsen-invisible-lattice-points.full.md`. This supersedes the arXiv abstract page at `research/sources/arxiv-1805.03186-goodrich-mbirika-nielsen-hidden-forests.full.md` — the full paper body is now read.

## What this source establishes

**Visibility criterion with proof.** Proposition 2.1: (x,y) ∈ Z²∖{(0,0)} is visible from the origin iff gcd(x,y) = 1 (both directions: d > 1 gives the closer point (x/d, y/d); gcd = 1 rules out any c > 1 with (x,y) = c(x₀,y₀)). This is the same criterion this run's brute-force oracle checks — now with a published proof, not just an asserted standard fact.

**Density of visible points.** Proposition 2.4: density is 6/π², with an Euler-product proof (∏ₚ(1 − 1/p²) = 1/ζ(2) = 6/π², via the Basel problem). Remark 2.2 gives careful provenance: the coprime-probability question was raised by Cesàro 1881; proved independently by Cesàro 1883 and Sylvester 1883; a weaker form by Dirichlet 1849; generalized to k > 2 integers by Cesàro 1884, also proved by Lehmer 1900. (Corroborates `visible-density-zeta-goins` with a fuller history.)

**Hidden forests.** An n×n hidden forest is an n×n block of invisible points. Theorem 3.4 + CRT-algorithm: from the prime matrix Pₙ (first n² primes row-wise), row products Rᵢ and column products Cⱼ give congruence systems x+i ≡ 0 (mod Rᵢ), y+j ≡ 0 (mod Cⱼ); CRT yields disjoint X, Y of n consecutive integers with gcd(xᵢ,yⱼ) > 1 for all i,j. The gcd-matrix GcdPₙ is a 90° rotation of Pₙ with divisibility (Prop 3.6). Quasiprime matrices (Def 4.6, QP-algorithm) relax Pₙ to keep the CRT solvable while using far fewer/fewer-powered primes.

**Best known locations (with proofs).** Closest 2×2: (14, 20), d ≈ 24.41. Closest 3×3: (1274, 1308), d ≈ 1825.91, confirmed by exhaustive search. Closest proven 4×4 to date in this paper: (134043, 184785885), d ≈ 1.84786×10⁸ — versus 3.07516×10¹⁸ by the traditional CRT method (Remark 4.9, factor 1.66×10¹⁰ closer). Their Table 1 lists Baake–Grimm 2013 at d ≈ 1.90265×10⁷ (closer but unproven, no method given) and Pighizzini–Shallit 2002 at 2.30574×10⁸. Closest known 5×5: (129963314, 2546641254872348), d ≈ 2.54664×10¹⁵, found by combining strings of strongly composite integers with quasiprime matrices. A 3-D 2×2×2 forest at (9126194, 8286564, 8822099).

**Conjecture.** Every hidden forest arises from the CRT-algorithm on some quasiprime matrix (Question 1). Open also: higher-dimensional analogues, Gaussian-integer lattices, b-invisible forests under power functions.

## What it implies for this run

The exact bounded-hexagon count of PE 351 is a different problem (finite region, exact count, no "closest forest" search) — the hidden-forest location problem is context, not method. What is load-bearing: the *published proof* of Proposition 2.1 (the geometric-to-arithmetic bridge the run's formula rests on) and the provenance of 6/π². Note for cross-checks: this library's Murphy–Schmiedeler–Stonner paper (Involve 14 (2021)) proves a closer 4×4 at (7247643, 10199370), d ≈ 1.25×10⁷, superseding GMN's "closest proven 4×4" claim; GMN's own table already conceded Baake–Grimm's unproven 1.9×10⁷.

```claim
id: visible-density-zeta-provenance
statement: The proportion of integer lattice points visible from the origin is 6/pi^2 = 1/zeta(2);
the question was raised by Cesaro 1881, proved independently by Cesaro 1883 and Sylvester 1883,
weakened earlier by Dirichlet 1849, and generalized to k > 2 integers by Cesaro 1884 (also Lehmer 1900).
hypotheses: k >= 2 dimensions; natural-density sense via the uniform distribution on {1..n}, n -> inf.
holds-here: yes — 2D anchor for the Phi(n) ~ (3/pi^2) n^2 magnitude check.
status: asserted (published proof in the source: Euler product 1/zeta(2) via the Basel problem).
bearing: corroborates visible-density-zeta-goins and the asymptotic anchor; not used in the exact count.
anchor: research/summaries/goodrich-mbirika-nielsen-invisible-lattice-points.md
```
