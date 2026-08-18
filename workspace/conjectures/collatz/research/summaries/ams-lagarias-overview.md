# Lagarias, *The 3x+1 Problem: An Overview*

<!-- source: https://www.ams.org/bookstore/pspdf/mbk-78-prev.pdf -->

Lagarias defines the classical Collatz map C(n)=3n+1 for odd n and n/2 for even n, and the accelerated map T(n)=(3n+1)/2 for odd n and n/2 for even n. Iteration of T omits the forced halving after an odd C-step. The conjecture is that every positive orbit reaches the trivial cycle; the problem remains open.

The overview records historical world records, including (at its publication date) verification below 20·2^58, exclusion of nontrivial cycles below specified period/odd-term thresholds, density results, and Diophantine-approximation approaches. These are historical, not current records. It emphasizes the central difficulty: pseudorandom dependence of successive accelerated iterates and the possibility of computationally complex behavior. It distinguishes rigorous theorems, heuristic stochastic models, and finite computation.

```claim
id: lagarias-map-reduction
statement: The accelerated map T agrees with C on even inputs and with C^2 on odd inputs; hence reaching the trivial cycle for T is equivalent to reaching it for C.
hypotheses: positive integer input and the definitions above.
holds-here: yes.
evidence: Lagarias overview, cited source.
status: asserted-by-source.
falsifies: direct calculation showing the stated relation fails for an odd or even input.
```
