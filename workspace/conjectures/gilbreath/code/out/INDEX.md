# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `characterize_fold_window.py` | Confirms lib.rule90fold reproduces true nu2 when fed the real halved-gap column bits. lib.fold_weight(hcol,n)=27/45 and lib.fold_weight_h(h,m)=27/45 both equal canonical true nu2 at n=100/4000, matching the geometric suffix fold. Guards against the phase bug (feeding thue_morse(c) for column c instead of hcol[c]=t(c-1)). Exact integers. Capture: code/out/characterize_fold_window.captured.txt. |
| `excess_maximal_invariant_set_synthesis.md` | Full write-up of the exact maximal safe set computation (approach excess-maximal-invariant-set). Negative stabilization result: no fixed finite prefix decides S_K; maximal-set certificate for the real prime window. |
| `excess_maximal_set.captured.txt` | Primary capture of excess_maximal_set.py. |
| `excess_maximal_set.py` | Exact backward-recursion maximal safe set of halved |
| `excess_maximal_set_prefix.captured.txt` | Capture of the prefix analysis. |
| `excess_maximal_set_prefix.py` | Fixed-prefix determinism analysis: no fixed prefix decides S_K. EXIT 0. |
| `excess_maximal_set_probe.captured.txt` | Capture of the probe. |
| `excess_maximal_set_probe.py` | M=3..6 probe of the excess-coordinate stabilization (attainability artifact). EXIT 0. |
| `excess_maximal_set_synthesis.captured.txt` | Capture of the synthesis. |
| `excess_maximal_set_synthesis.py` | Final synthesis: backward==forward exact, real-window certificate, negative bound with witnesses, density. EXIT 0. |
| `excess_maximal_set_verify.captured.txt` | Capture of the forward-oracle verification. |
| `excess_maximal_set_verify.py` | Independent forward-oracle cross-check, asserts backward==forward at all K=1..10; refutes naive invariant box. EXIT 0. |
| `overshoot_decomposition.py` | Exact-integer overshoot decomposition on one right diagonal per n (C1 convention): measures nu2 (maximal {0,2} suffix 2-count via canonical lib.rightdiag.cycle_and_nu2), F_fold (F2 fold of halved-gap bits over ancestor window [2,n-1]), F_diag (#k in [2,n-1] with delta_k==2 mod 4), O (#k in [2,tau-1] with delta_k==2 mod 4). Verifies nu2==F_diag-O and F_fold==F_diag on real primes / Thue-Morse / period-3 / consecutive odds, n=50..2000. Established correct: identity passes all 160 samples; F_fold==F_diag is structural via rule-90 fold = diagonal parity (independent oracle in overshoot_fold_oracle.py, 0 mismatches). Resolves the TM n=100 '27 vs 7' contradiction: nu2=F_fold=F_diag=27; 7 was the refuted power-of-two count. Exact integer arithmetic; capture code/out/overshoot_decomposition.captured.txt EXIT 0. |
| `overshoot_fold_oracle.py` | Independent cell-level oracle for the rule-90 fold identity: fold_cell_bit(h,k,n) == (delta_k(q_n)//2)%2 for all k=2..n-1, n<=400, on real primes / period-3 / Thue-Morse. This is what makes F_fold==F_diag in overshoot_decomposition.py structural (every diagonal cell k>=2 is even, so the fold parity bit == the ==2-mod-4 indicator). Established correct: 0 mismatches on all three families. Exact integer arithmetic. |
| `resolve_fold_vs_nu2.py` | Resolves the prefix-vs-suffix fold contradiction for the dyadic supply line. Computes TRUE nu2 (canonical lib.rightdiag.cycle_and_nu2, C1 Thue-Morse 2-then-odds) and compares it to (A) the SUFFIX fold = lib.rule90fold.fold_weight_h (windows ending at column n-1, i.e. the right-diagonal ancestor-window geometric fold) and (B) the PREFIX fold = whole-word subset-zeta (= powers-of-two count for TM). Result: suffix == true nu2 (27@100, 45@4000) and prefix != (7@100, 12@4000); discriminating assertion passes. Exact integers. Capture: code/out/resolve_fold_vs_nu2.captured.new.txt. |
