# Goal

Research the mathematics behind: find the quadratic integer a+b*sqrt(d) (|a|,|b|<=n=10^13, d non-square <100) closest to pi. This reduces to: for a fixed irrational alpha = {sqrt(d)}, and shift beta = {pi}, find b in [0,B] (and negative side with beta={-pi}) minimizing the circular distance between {b*alpha} and beta, in O(log B) — the inhomogeneous Diophantine approximation / nearest lattice point / best left-right alpha-approximation problem.

Completion criteria:
1. Precise statement of the continued-fraction / Ostrowski-numeration based algorithm (Cabanillas-Lopez & Labbe arXiv:1904.01874, Propositions 9 & 10, Algorithm 3(ii)) with pseudocode and complexity.
2. Alternative exact closest-vector methods (Euclidean-style O(log)).
3. Three-distance theorem facts.
4. Structure of optimal (a,b) for quadratic approximation of pi (Pell/unit relation, no — best b are semi-convergent denominators / Ostrowski digits).
5. Verification of the candidate-enumeration algorithm against brute force on small inputs.
6. Cited URLs only for sources actually fetched.
