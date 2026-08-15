# Dirac frame formulation: the target is the frame-max of the squared truncated Dirac operator

```approach
idea: f(n) is the minimum over splits S ⊔ S^c of the maximum *diagonal* entry of
B², where B = A_n[S,S] is the Huang/Dirac operator A_n = Σ_{i≤n} γ_i compressed
to S. The exact identity deg_S(v) = ‖P_S A_n e_v‖² = (B²)_{vv} = n − ‖C^T e_v‖²
turns the combinatorial maximum degree into an operator-theoretic *frame quantity*
(max over the coordinate frame {e_v : v ∈ S}), which sits strictly between the
trace of B² (the average degree — the log-bound route) and the norm λ_max(B²)
(the spectral route — the √n bound). This is the missing middle that the
averaging obstruction in problem.md says must be found.

mechanism: A_n is the n-generator Dirac operator (Clifford: γ_i² = I, γ_iγ_j = −γ_jγ_i,
A_n = Σγ_i, hence A_n² = nI), a symmetric {0,±1} matrix whose support is exactly
E(Q_n). Split V = S ⊔ S^c and write A_n in block form

      [ B   C ]
  A = [ Cᵀ  D ]    with  B = A_n[S,S],  C = A_n[S,S^c],  D = A_n[S^c,S^c].

The top-left block of A_n² = nI gives the *supersymmetry* relation

      B² + CCᵀ = n·I_S.

For v ∈ S: (B²)_{vv} = ‖B e_v‖² = ‖P_S A_n e_v‖² = deg_S(v) (each surviving
neighbour contributes a distinct ±1 coordinate), and (CCᵀ)_{vv} = ‖Cᵀ e_v‖² =
outdeg_S(v) = #{neighbours of v outside S}. Hence

      deg_S(v) = (B²)_{vv} = n − outdeg_S(v),

and the target is the frame-max of B²:

      D(S) = max_{v∈S} (B²)_{vv} = max_{v∈S} ‖P_S A_n e_v‖² = n − min_{v∈S} outdeg_S(v).

The three operator statistics of the SAME matrix B² are now cleanly separated:
  • trace(B²)/|S| = average internal degree = 2e(S)/|S|     → the log-bound route;
  • max_{v} (B²)_{vv} = D(S)                                 → THE TARGET (frame-max);
  • λ_max(B²) = λ_max(B)² = n                                → the spectral route.
The first is an average, the third is a norm, and the problem is exactly the
frame-max in between — this is the "quantity that is itself a maximum by
construction" that problem.md requires, now expressed natively in the Dirac world.

Sharp spectral fact (sharpening the closed route): for |S| = 2^{n-1}+1, Cauchy
interlacing applied in BOTH directions gives λ_max(B) = √n exactly (not just ≥):
β_1 ≤ α_1 = √n (top eigenvalue of A_n) and β_1 ≥ α_{2^{n-1}} = √n (the
(2^n − m + 1)-th eigenvalue of A_n, with m = 2^{n-1}+1). Equivalently the
supersymmetry relation B² = nI_S − CCᵀ with CCᵀ ⪰ 0 forces λ_max(B²) ≤ n, and
interlacing forces λ_max(B²) ≥ n, so λ_max(B²) = n. The degree bound λ_max(B) ≤ D(S)
(for {0,±1} matrices supported on the edges) closes the operator chain:

      √n = λ_max(B) ≤ D(S) = max diag(B²) ≤ λ_max(B²) = n.

So the OPEN exact-value residue is the single question: for B = A_n[S,S] with
λ_max(B) fixed at √n, how small can the maximum diagonal entry of B² be pushed?
Observed f(1..5) = 1,2,2,2,3 = ceil(√n); the conjecture to attack is that the
minimum frame-max is exactly ceil(√n), i.e. there is a split with every v ∈ S
having ‖P_S A_n e_v‖² ≤ ceil(√n) (outdeg ≥ n − ceil(√n)), and none with a smaller
ceiling.

covers: reproduces `huang-signed-adjacency` (A_n² = nI, native Clifford relation),
`huang-interlacing-sqrt` (sharpened to λ_max(B) = √n exactly), and `huang-f-n-sqrt-n`
(the chain √n = λ_max(B) ≤ D(S)). Scholze's rule holds: the new frame quantity
D(S) = max diag(B²) *recovers* the spectral bound √n ≤ D(S) and additionally
locates exactly where the closed route leaves slack (the gap √n ≤ D(S) ≤ n).
It does not re-claim a lower bound; its target is the genuinely open exact value.

status: adopted
killed-by: (none — this is the adopted line; see provenance below)
provenance: the synthesis of the grounded Clifford/Dirac reformulation (correct
  algebra, A_n = Σγ_i, A_n² = nI) with the grounding finding that its *norm*
  overshoots (the minimisers are "flat", not parity-plus-one, so λ_max is the
  wrong statistic). The correction — use the diagonal/frame statistic of B², not
  the operator norm of B — is the new idea, and it is not one of the three
  original candidates. Supersedes `clifford-dirac-fermionic` (whose norm-based
  overshoot is refuted at n=4) and is orthogonal to the refuted average-type
  lines (`delsarte-krawtchouk-lp`, `entropy-degree-constrained-hardcore`).
precedent:
  - Clifford relations γ_i² = I, γ_iγ_j = −γ_jγ_i, A = Σγ_i ⇒ A² = nI: standard
    Clifford/Dirac identity; A_n = Huang's signed adjacency is verified exactly
    for n = 1..8 (sympy Integer) at code/out/huang_spectral.captured.txt.
  - Cauchy interlacing (both directions) for principal submatrices: standard; the
    sharpening λ_max(B) = √n exactly follows from α_1 = α_{2^{n-1}} = √n.
  - The degree bound λ_max(B) ≤ D(S) and the PSD fact max diag(B²) ≤ λ_max(B²):
    standard matrix facts, already in the ledger as `huang-degree-bounds-lambda`.
  - No published source states the frame identity deg_S(v) = ‖P_S A_n e_v‖² =
    (B²)_{vv} = n − ‖Cᵀe_v‖² for this problem; it is this run's own derivation,
    hand-checked here and to be machine-verified per the first-step.

first-step: (tool_builder, shell available) Reuse A_n from code/lib/huang.py.
  For n = 1..4 enumerate every admissible S (|S| = 2^{n-1}+1; sizes 2,3,5,9,
  C(16,9)=11440 at n=4 — feasible) and for each verify, with exact sympy Integer
  arithmetic: (i) λ_max(A_n[S,S]) == √n exactly; (ii) for every v ∈ S,
  (A_n[S,S]²)_{vv} == deg_S(v) == #{u∈S : u~v} (direct neighbour count) ==
  n − outdeg_S(v); (iii) B² + CCᵀ == n·I_S exactly, C = A_n[S,S^c];
  (iv) min_S max_{v∈S} (B²)_{vv} == f(n) = 1,2,2,2. Then n = 5 by the existing
  CP-SAT/ILP decision oracle to confirm the frame-max minimum == 3 == f(5), and
  extract a witness S_5; report its out-degree profile (the "flat" structure:
  outdeg ≥ n − ceil(√n) for all v). If (i)–(iv) hold, the reformulation is
  grounded and the next move is the extremal/structural question: characterise
  the splits realising max diag(B²) = ceil(√n), i.e. the constraint system
  {‖P_S A_n e_v‖² ≤ ceil(√n) for all v ∈ S, |S| = 2^{n-1}+1}.
```
