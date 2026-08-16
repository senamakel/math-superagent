# Bárány & Valtr, "A Positive Fraction Erdős–Szekeres Theorem"

<!-- source: https://www.renyi.hu/~barany/cikkek/72.pdf | full text at research/sources/barany-valtr-A-positive-fraction-ES-theorem.full.md -->

**Publication.** I. Bárány and P. Valtr, *Discrete & Computational Geometry* 19(3) (1998) 335–342. DOI 10.1007/PL00009350. Author copy (renyi.hu) in the library.

**Why it matters.** This is the load-bearing ingredient of Suk's 2016/17 breakthrough upper bound ES(n) ≤ 2^{n+o(n)} (also in library). Suk uses the positive-fraction / partitioned ES machinery to find a cup or cap with positively-dense support regions, then a Dilworth-type partial order forces the convex polygon. It is the reason the base-4 cup/cap bound was beaten in the exponent.

## Statements (asserted-by-source, proofs in text)

**Positive-fraction ES theorem (Theorem 1).** For every integer k ≥ 4 there is a constant c_k > 0 such that every sufficiently large finite set X ⊂ R² in general position contains k subsets Y_1,…,Y_k with |Y_i| ≥ c_k|X| such that **every transversal** {y_1,…,y_k}, y_i ∈ Y_i, is in convex position.

**Same-Type Lemma (Theorem 2, the main tool).** For every d, m there is c(d,m)>0: given finite sets X_1,…,X_m ⊂ R^d with X_1∪…∪X_m in general position, there are subsets Y_i ⊆ X_i with |Y_i| ≥ c(d,m)|X_i| such that all transversals have the **same (order) type** — equivalently the signs of every d+1-subset determinant agree (order-type stability).

Two m-tuples have the same type iff the orientations (signs of det) of all m choose d+1 simplices agree — i.e. same chirotope/orientation table.

**Corollaries.** Positive-fraction Radon theorem, positive-fraction Tverberg theorem; measure-theoretic generalizations.

**Direct consequences collected in the paper.** Theorem 1 for k=4 (Nielsen); Solymosi's weaker version (a length-ck·n sequence whose every k consecutive members are in convex position). Also connects to convex n-clusterings (partitioned ES theorem, Pór–Valtr 2002 — see the Tóth–Valtr survey in the library).

## claim block (for CLAIMS.md)
```claim
id: barany-valtr-positive-fraction
statement: For every k ≥ 4 there is c_k > 0 such that every sufficiently large planar general-position set X contains k subsets Y_1,…,Y_k with |Y_i| ≥ c_k|X| whose every transversal is in convex position (positive-fraction ES theorem). Its engine is the Same-Type Lemma: from given sets X_1,…,X_m in general position one can find c(d,m)|X_i|-size subsets whose every transversal has the same order type.
hypotheses: planar (for Thm 1); general position; d-dimensional analogies hold (Same-Type Lemma).
holds-here: true, and it is exactly what lets Suk's proof beat the 4^n cup/cap base — a genuinely load-bearing ingredient of the modern asymptotic bound.
status: proved (peer-reviewed DCG 1998, full proof in text; not independently re-derived here).
bearing: this is the fracture the run's exact-conjecture attempt must contend with on the upper-bound side. It produces a convex-position subset whose support regions carry a positive fraction, but its constants are hopelessly loose for an exact 2^{n-2}+1 bound; an exact proof needs a structural (stability/uniqueness) argument instead — matches GOAL's advice that counting cannot see uniqueness.
anchor: research/sources/barany-valtr-A-positive-fraction-ES-theorem.full.md
```
