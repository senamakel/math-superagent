```approach
id: erdos-selfridge-structural
idea: Erdős–Selfridge (1975) structural restriction — use the theorem that the product of two or more consecutive positive integers is never a perfect power to restrict which equal-products reductions of C(x,k1)=C(y,k2) can hold. This is a genuinely different structural fact from the algebraic-geometric ones: it operates on the prime-factor exponents of the consecutive-integer blocks rather than on the genus or height.

mechanism: The equal-products reduction of C(x,k1)=C(y,k2) is x(x-1)...(x-k1+1)·k2! = y(y-1)...(y-k2+1)·k1!. Cancel the common factorial part and let the remaining block equation be A·(k2!') = B·(k1!') where A, B are products of k1 and k2 consecutive integers respectively. Now consider what happens if k1 and k2 are both "large" — say both ≥ t. Then each side is a product of t consecutive integers times a factorial. Erdős-Selfridge says that the product of t consecutive integers is never an ℓ-th power for any ℓ ≥ 2 (with t ≥ 2). More precisely, for every k ≥ 2 there is a prime p > k whose exponent in the product (n+1)...(n+k) is 1 — so the product has a prime factor appearing only to the first power. This means the product has "large" squarefree kernel.

The structural insight: if C(x,k1)=C(y,k2) and k1,k2 are both large, then the equal-products reduction forces two large consecutive-integer blocks to have the same squarefree kernel (up to the factorial factors), which by Erdős-Selfridge forces the blocks to overlap or align in a very restricted way. This is NOT the Sylvester-prime approach (which was refuted as redundant with SST/BST) because it uses the exponent-1 prime (not just existence of a prime > k) and the alignment-of-blocks structure to classify possible equalities by their prime support, not their genus.

Status: proposed
Precedent:
  - Erdős–Selfridge 1975 (Illinois J. Math. 19, 292-301): "The product of consecutive integers is never a power" — primary held, claim `erdos-selfridge-no-perfect-power`.
  - Filaseta 1997 (J. Number Theory 64, 20-38): refinements — the exponent-1 prime can be chosen controllably large.
  - NOT previously proposed for Singmaster (this run has not attempted this angle; all prior approaches used SST/BST's general equal-products framework, not the specific exponent-1 prime structural fact).

first-step:
  1. For the equal-products reduction A·K2 = B·K1 (where K1,K2 are the factorial remainders after cancelling the common factorial), compute the prime factorisations of A and B from the known witnesses.
  2. For each prime p dividing A, determine its exponent in A and in K2·B, and verify that at least one prime appears with exponent 1 in A (Erdős-Selfridge guarantee).
  3. Derive a structural lemma: if C(x,k1)=C(y,k2) with k1,k2 both ≥ 3, then the two blocks of consecutive integers cannot both be "large" unless they share a specific alignment pattern (overlap, or one is a translate of the other times a small rational factor).
  4. Classify the possible alignment types using the exponent-1 primes, and show that non-trivial alignments force k1,k2 to be bounded (hence reducing the problem to a finite set).

Speculative: The classification of alignment types may itself require case analysis that grows with k1,k2. The exponent-1 prime exists for each block individually, but the coupling between two different blocks needs a new combinatorial lemma about prime exponents in disjoint vs overlapping consecutive-integer intervals. This lemma does not exist in the literature (to my knowledge) — it would need to be proven.
```