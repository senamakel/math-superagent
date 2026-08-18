# Simons 2008 — m-cycles for generalized Syracuse sequences (Acta Arith. 131(3) 217–254)

<!-- src: J. L. Simons, "On the (non-)existence of m-cycles for generalized Syracuse sequences", Acta Arithmetica 131(3) (2008) 217–254, DOI 10.4064/aa131-3-2. Full text: research/sources/simons-2008-generalized-syracuse.full.md (via Wayback Machine of the IMPAN free CC-BY PDF). -->

## What the source establishes

This is the author's own survey of the Simons–de Weger m-cycle method and its
extension to generalized Syracuse sequences (3x+q, px+1, px+q with
GCD(p,q)=1). The paper is not a new bound for the standard 3x+1 problem — it
recapitulates the S&dW approach (Section 2) and then generalizes it.

**Structure of the S&dW method (Section 2), stated by the author:**
an m-cycle has m local minima x_i and m local maxima; each odd number
x_0 = a_0 2^{k_0} − 1 starts an increasing subsequence of k_0 odd numbers; the
chain equation joining the i-th decreasing to the (i+1)-th increasing
subsequence is (a_i 3^{k_i} − 1)/2^{l_i} = a_{i+1} 2^{k_{i+1}} − 1; all chain
equations together form a Diophantine matrix equation in the coefficients a_i.
Existence of an m-cycle ⇔ integer solution of this system. Λ =
(K+L) log 2 − K log 3 and δ = log 3 / log 2 control the bounds.

**Key lemmas:**
- Lemma 1/2: with verification bound X0, K ≥ q_{n+1} where q_n are
  convergents of δ (generalizes the S&dW lower bound; for the standard
  problem this is the `sdw-K-corollary-11` family).
- Lemma 5: K ≥ K3(m,q) from the Rhin lower bound on Λ.
- Lemma 7/8: the 3x+q problem (5 ≤ q ≤ 97 prime) has no m-cycles for m ≤ 10
  beyond explicit hypothetical tables.
- Lemma 13: if a primitive m-cycle of px+q exists with K odd, L even
  elements, then 2^{K+L} − p^K ≡ 0 (mod q).
- Lemma 14–17: the 5x+q, 7x+q, 11x+q problems have no m-cycles for m ≤ 7
  (resp. m ≤ 4) beyond the tables.
- Lemma 18–20: 1-cycles of px+q: existence ⇔ positive integers k, l, r (r
  odd) with 2^{k+l} − p^k = q r and odd x_0 = (p^k − 2^k)/((p−2) r).
- **Lemma 23**: the inverse Collatz problem has no m-cycles for m ≤ 9 other
  than (1), (2,3), (4,6,9,7,5) and the 12-cycle (44, 66, 99, 74, 111, 83, 62,
  93, 70, 105, 79, 59).
- **Lemma 26**: if the generalized Collatz problem has an m-cycle with
  x_i > 0, then m ≥ 10.

## Relation to the standard problem

The paper's opening restates the S&dW result "non-existence of m-cycles
(m ≤ 75)" — that is the preprint-improved figure, not the published 2005
bound (m ≤ 68). For the standard 3x+1 problem the paper adds the inverse-Collatz
classification (Lemma 23) and the m ≥ 10 statement (Lemma 26); the
generalized-family lemmas (3x+q, px+q) are its original contribution.

## Claims

```claim
id: simons-2008-generalized-family
answers: text-layer-full-3ce1
statement: The Simons–de Weger m-cycle method (Diophantine chain equations, convergents of δ = log 3/log 2, Rhin/LMN lower bounds on linear forms in logarithms) extends to the 3x+q, px+1 and px+q (GCD(p,q)=1) generalized Syracuse problems: m-cycles there are excluded for small m up to explicit tables (3x+q: m ≤ 10 for 5 ≤ q ≤ 97 prime; 5x+q: m ≤ 7; 7x+q, 11x+q: m ≤ 4), and a primitive m-cycle of px+q must satisfy 2^{K+L} − p^K ≡ 0 (mod q). (Simons, Acta Arith. 131 (2008), Lemmas 7–17.)
hypotheses: generalized Syracuse maps with GCD(p,q)=1; m = number of local minima; K odd, L even elements
holds-here: true for the 3x+1 standard case as the p=3,q=1 specialization; the generalization shows the method is robust beyond the single map
evidence: proved in source (full text held)
status: proved
falsifies: a counterexample m-cycle for one of the stated generalized families contradicting the tables
```

```claim
id: simons-2008-inverse-collatz
statement: The inverse Collatz problem has no m-cycles for m ≤ 9 other than (1), (2,3), (4,6,9,7,5) and the 12-cycle (44, 66, 99, 74, 111, 83, 62, 93, 70, 105, 79, 59); if the generalized Collatz problem has an m-cycle with positive elements then m ≥ 10. (Simons, Acta Arith. 131 (2008), Lemmas 23 and 26.)
hypotheses: inverse Collatz / generalized Collatz problems as defined in the paper
holds-here: true for the inverse problem; a structural constraint on cycle shapes
evidence: proved in source (full text held)
status: proved
falsifies: an m-cycle with m ≤ 9 outside the listed four in the inverse problem
```

## Cross-check with the v1.44 preprint

The method described here matches the held preprint's machinery (chain
equations, Λ, δ, convergents, lattice reduction). The 2008 paper is the
generalized-family extension; for the standard problem the paper's "m ≤ 75"
is a citation of the preprint-improved result, so it does not change the
published-2005 baseline (m ≤ 68) recorded in the companion summary.
