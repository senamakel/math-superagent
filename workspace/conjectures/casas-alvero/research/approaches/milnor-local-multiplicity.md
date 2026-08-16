# Approach: local Milnor/intersection multiplicity certificate (refuted)

Proposed: certify CA at the one point it forces (`x^n`) by the local intersection
multiplicity / Milnor number of the complete intersection `(R_1,…,R_{n−1})`,
computed from initial forms alone. Refuted at convergence.

```approach
idea: Milnor-fibration / intersection-multiplicity certificate. CA ⟺ the ideal
      (R_1,…,R_{n−1}) is (a_1,…,a_{n−1})-primary of the expected Bézout
      multiplicity; a local degree μ = dim_C C{a}/(R_1,…,R_{n−1}) equal to
      ∏_i deg R_i, certified from the initial forms, proves CA for that degree.
mechanism: The local degree μ is a topological invariant (Milnor number, link of
      the singularity) computable from the leading/initial forms of the R_i with
      weight w(a_j) = j, w(x) = 1 — a local regularity certificate requiring
      only the top graded piece, not a full Gröbner basis.
status: refuted
killed-by: Not a change of representation — it is the complete-intersection /
      regular-sequence reformulation the run already adopts. Ghosh 2024
      (arXiv:2402.18717, held) already reduces CA to: the homogeneous forms
      G_{T,i} form a regular sequence / the scheme is a complete intersection,
      and Schaub–Spivakovsky (arXiv:2411.13967 Thm 3.1, held) already turned
      exactly that regularity into an integer test (the minors J_T whose prime
      divisors are the bad primes). That integer test *is* the adopted
      arithmetic-jet-lift approach's engine. Wrapping it as a Milnor number over
      ℂ adds no algebraic handle: the ℂ-only topology (local link, Artin–Milnor,
      μ = ∏ μ_i) is the very part that must break in char p, while the
      characteristic-free regular-sequence content is already owned by the
      G_{T,i}/J_T machinery. Its own file conceded the risk: if a single weight
      w fails, it degrades toward the refuted tropical-resultant-fan — and the
      single weight is exactly what Ghosh's homogeneous (unweighted) G_{T,i}
      reformulation avoids.
first-step: superseded — see research/approaches/root-difference-coloring.md.
precedent: ghosh-complete-intersection, bad-prime-minors-criterion (both held).
speculative: none retained.
```
