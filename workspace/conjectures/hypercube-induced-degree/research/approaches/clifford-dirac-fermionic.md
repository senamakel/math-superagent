# Clifford / Dirac operator in fermionic Fock space

```approach
idea: Place the problem in the fermionic Fock space where the signed adjacency
matrix is the Dirac operator A_n = Σ_{i=1}^n γ_i for the anticommuting Majorana
operators γ_i. Then A_n² = nI is the Clifford relation (γ_i² = I, γ_iγ_j = −γ_jγ_i),
√n is the operator norm, and D(S) is the norm of the Dirac operator compressed to
the span of S. Read the extremal structure in the occupation-number basis: the
parity classes are the even/odd fermion-number sectors, and the +1 vertex is a
single excitation.

mechanism: Identify {0,1}^n with the fermionic occupation basis; γ_i acts as
γ_i|x⟩ = (−1)^{x_1+…+x_{i−1}} |x⊕e_i⟩. Then A_n = Σγ_i is exactly Huang's signed
adjacency matrix (hand-checked for n = 2, where γ_1+γ_2 equals
[[A_1,I],[I,−A_1]]), and A_n² = nI falls out of the anticommutation relations as
a statement about fermions rather than an ad hoc signed matrix — this is the
quadratic relation that produces √n, now in its native world. The restriction
A_n[S,S] is the compression of the Dirac operator to a subspace; the
Courant–Fischer min-max principle (which subsumes Cauchy interlacing) gives
λ_max(A_n[S,S]) ≥ √n, reproducing `huang-interlacing-sqrt` in operator-theoretic
terms, satisfying Scholze's rule.

The genuinely new part is the occupation-number (fermion-number) decomposition of
an arbitrary S: its indicator 1_S carries a definite even/odd structure, and the
exact-half-plus-one condition means S is a maximal independent set (a parity
sector) plus one vertex (one excitation). Conjecture to test, clearly marked as
speculative: the truncated operator norm is forced to be exactly ceil(√n), which
would give the sharper exact statement f(n) = ceil(√n) for every n, consistent
with f(1..5) = (1,2,2,2,3), and would classify the extremal S as parity-plus-one.
This overshoots the asymptotic Θ(√n) the closed route achieved.

covers: reproduces `huang-signed-adjacency` (A_n = Σγ_i, A_n² = nI) and
`huang-interlacing-sqrt` (via Courant–Fischer), then overshoots to the exact value.

status: refuted (superseded — its correct core is carried forward in `dirac-frame-supersymmetric-split`)
killed-by: The conjectured extremal classification "S = parity class + one
  excitation" is false at n=4, settled directly from the verified exact values.
  In Q_4, a parity-plus-one set (8 even-class vertices + 1 odd vertex x) has
  x adjacent to all four of its neighbours (flipping one bit flips parity, so
  every neighbour of the odd x lies in the even class), hence the lone
  excitation has internal degree 4. So D(parity+one) = 4 at n=4, whereas
  f(4)=2 (exact, exhaustive). The optimum is attained at 2 by a 4-even/5-odd
  witness — not by any parity-plus-one set. The value conjecture f(n)=ceil(sqrt(n))
  survives (it matches f(1..5) = 1,2,2,2,3) but the stated reason for it —
  the fermion-number/occupation decomposition forcing the truncated Dirac
  norm to ceil(sqrt(n)) on parity-plus-one sets — is killed at n=4, since the
  minimisers are not parity-plus-one. As a reformulation it is a genuine and
  correct restatement of Huang's signed adjacency (A_n = sum gamma_i with
  gamma_i^2 = I, anticommuting, is verified to equal the Huang matrix; A_n^2=nI
  is Clifford's relation), so it satisfies Scholze's rule at the level of
  reproducing `huang-signed-adjacency` and `huang-interlacing-sqrt`; it just
  contributes no independent lower-bound proof and its classification
  overshoot is refuted.
precedent:
  - Clifford relations gamma_i^2 = I, gamma_i gamma_j = -gamma_j gamma_i and
    A = sum gamma_i => A^2 = n I: standard Clifford algebra identity (Dirac
    operator on n-generator Clifford algebra); the operator norm sqrt(n) is
    native to this world. Primary sources develop the technique (lattice
    fermions as spectral graphs), but the direct "A_n = Huang matrix" equality
    is this run's own hand derivation, to be sympy-verified per the file.
  - https://link.springer.com/article/10.1007/JHEP02(2022)104 (Lattice fermions
    as spectral graphs, JHEP 2022) — Dirac operator on hypercube lattices via
    spectral graph theory; supports the identification but does not report this
    problem's answer.
  - https://link.springer.com/article/10.1007/s00006-010-0206-z (Clifford
    algebra applied to Grover, ACGE 2010) — Clifford-algebraic spectral
    groundings of cube-type search.
  - https://doi.org/10.1007/JHEP11(2020)154 (Chaos on the hypercube, JHEP 2020)
    — interacting Majorana fermions on the hypercube; the Fock-space reading.
  The fermionic rephrasing is genuinely different in world (it is the native
  algebra of the matrix) but is a repackaging of the already-closed spectral
  route: it contributes the same sqrt(n) proof, no new lower bound.
refuted-at: n=4 (exact); largest speculative claim killed, rest recognised.
successor: `dirac-frame-supersymmetric-split` — keeps the correct algebra
  (A_n = Σγ_i, A_n² = nI) but replaces the refuted *norm* statistic λ_max(B)
  with the correct *frame* statistic D(S) = max_{v∈S} (B²)_{vv} = max ‖P_S A_n e_v‖²,
  which equals the actual target exactly. The overshoot of this file was using
  λ_max(B) where the problem asks for the max diagonal of B².

first-step: Verify A_n = Σ_i γ_i in the Majorana representation equals the Huang
matrix exactly for n = 1..8 (sympy Integer); then express D(S) as
max_{⟨ψ|ψ⟩=1, supp ψ ⊆ S} ⟨ψ|A_n|ψ⟩ and compute, for small n, the min-max over
fermion-number sectors to test f(n) = ceil(√n) against f(1..5).
```
