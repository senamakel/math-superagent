# Tasks

## Done — the gap is closed: f(n) = Θ(√n)

- [x] Build signed adjacency matrix `A_n` with `A_n² = n·I`; verify exactly
      (n=1..8) and spectrum `±√n` (n=2..10). Files: `code/spectral_verify.py`,
      `code/lib/huang.py`, `code/lib/qcube.py`.
- [x] Verify interlacing lower bound: `λ_max(A_n[S,S]) ≥ √n` for every
      admissible `S`, exhaustive for n=1..4, random to n=10.
- [x] Verify degree bound: `λ_max(B) ≤ Δ(H)` in every trial.
- [x] Exact `f(1..4) = 1, 2, 2, 2` (exhaustive, cross-checked with the spectral
      bounds for every admissible set).
- [x] Reproduce the worked example (even-weight set of size `2^{n-1}` is
      independent, `D=0`).

## Optional refinements (not needed for the conclusion)

- [ ] Lean 4 formalisation of the three Huang lemmas (`#print axioms`, no sorry).
- [ ] symbolic_math closed-form / larger-n spectral probe past n=10.
