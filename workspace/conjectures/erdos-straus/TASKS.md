# Tasks

- [x] Build the ground-truth oracle `code/oracle.py`: `solves` (exact int
      cross-multiplication), `is_identity` (sympy), `naive_solve` (small
      brute-force), and `main()` reproducing every worked example. All checks
      PASS; output captured in `code/out/oracle.captured.txt`.
- [x] Verify `code/lib/parallel.py` self-check (pool agrees with serial:
      26 workers, n=1..2000). PASS.
- [x] Cross-check every witness in `code/out/witnesses.json` (12/12 solve)
      and a small brute sweep n ∈ [2,200] (199/199 solve, cap=5e6).
- [x] Correct the n≡3 (mod 4) identity: the brief's `x=n, y=(n+1)/2,
      z=n(n+1)/2` solves 3/n, not 4/n (checked, residual exactly 1/n —
      `naive-3mod4-identity-is-wrong`). The corrected identity
      `n=4k+3, x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1)` is a checked claim
      (exact Fraction arithmetic, k=0..4999;
      `code/out/verify_elementary_reductions.py`). Also the p=3 prime base
      (1,3,3) is wrong; correct is (1,6,6).
- [x] `n-even-trivial` (`4/2m = 1/m + 1/2m + 1/2m`) promoted to checked
      (m=1..5000, same program). The wrong n≡3 (mod 4) identity must not be
      cited as covering anywhere.

- [ ] **PRIORITY (operator directive): verify `prime-reduction` in code.**
      Prove with exact arithmetic that `4/n = 1/x+1/y+1/z` implies
      `4/(nm) = 1/(mx)+1/(my)+1/(mz)` (scale denominators), hence
      `f(nm) ≥ f(n)` and a composite counterexample yields a smaller
      prime-factor counterexample. Write the program, capture its output,
      and promote `prime-reduction` in `research/CLAIMS.md` from `asserted`
      to `checked`. Do this before any new identity search.
- [ ] Promote `reduction-mod24` to `checked` as a corollary once
      `prime-reduction` and the remaining elementary identities
      (n≡2 mod 3, n≡5 mod 8 — still asserted) are checked. This closes the
      whole reduction "any counterexample ⇒ odd prime p ≡ 1 (mod 24)".

- [ ] Only after the reduction is fully checked: extend identity search over
      ansatz space (type I/II shapes) toward the open classes
      {1,121,169,289,361,529} mod 840, recording the level-1 obstruction
      (residue must be a quadratic non-residue for a modular identity).
