# Tasks

- [x] Build the ground-truth oracle `code/oracle.py`: `solves` (exact int
      cross-multiplication), `is_identity` (sympy), `naive_solve` (small
      brute-force), and `main()` reproducing every worked example. All checks
      PASS; output captured in `code/out/oracle.captured.txt`.
- [x] Verify `code/lib/parallel.py` self-check (pool agrees with serial:
      26 workers, n=1..2000). PASS.
- [x] Cross-check every witness in `code/out/witnesses.json` (12/12 solve)
      and a small brute sweep n ∈ [2,200] (199/199 solve, cap=5e6).
- [x] Correct two errors in the brief discovered by the oracle:
      (1) the n≡3 (mod 4) identity (brief gives 3/n; correct is
      `1/((n+1)/4)+1/(n(n+1)/2)+1/(n(n+1)/2)`, from Elsholtz–Tao Type II);
      (2) the p=3 prime base (1,3,3) is wrong, correct is (1,6,6).

- [ ] Next concrete step toward the conjecture: extend identity search over
      ansatz space (type I/II shapes) toward the open classes
      {1,121,169,289,361,529} mod 840, recording the level-1 obstruction
      (residue must be a quadratic non-residue for a modular identity).
