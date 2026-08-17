# Index — code/pattern_hunt

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_R_runs.py` | Analyzes run structure of the right-special factors R_k (constant-V runs of length 2/3) and S1(k) noise; writes code/out/s1_res.txt and vR_res.txt. |
| `check_corr_translation.py` | Tests translation-invariance of factor-set pair-correlation C(i,j); shows it holds only at k=F_n-1, refuting lag-sum reduction at general k. |
| `check_directive1.py` | Verify directive-1 pair-correlation/autocorrelation formula vs brute exact Psi at k=F_n-1 (n=2..7): brute==rot==corr==exact. |
| `check_directive1_big.py` | Extend directive-1 verification to n=2..12 (k up to 232): rotation set == brute factor set, autocorr formula == rotation Psi. |
| `check_ext_recurrence.py` | Verifies the right-extension (Sturmian) recurrence Psi(k+1)=100Psi(k)+100V(R_k)^2+20S1(k)+J(k) exactly k=1..40 against the string oracle; writes code/out/ext_recurrence.txt. |
| `check_ext_recurrence_400.py` | Verifies the mod-M right-extension recurrence and J(k)=c1(k+1) for k=1..400, plus Toeplitz probe; writes code/out/extrecur_res.txt. |
| `check_leading_counts.py` | Clean recomputation of lead-1/lead-0 factor counts (k=1..30). |
| `check_lmin.py` | Early probe: Lmin vs floor(phi^2 k) and A344953; superseded by verify_lmin_formula.py. |
| `check_toeplitz_defect.py` | Scans the pair-correlation Toeplitz defect for k=1..400: verifies |d|<=1 always and zero-defect exactly at k=F_n-1; writes code/out/topelitz_defects.txt. |
| `check_weight_dist.py` | Tabulates length-k Fibonacci subword counts by weight; confirms exactly two weights floor/ceil(k/phi^2). |
| `extract_subseqs.py` | Extract subsequences Psi mod M at k=F_m-1/F_m/F_m+1; superseded. |
| `gen_sequences.py` | Generate PE1006 integer sequences (Psi exact 1..25, Psi mod M 1..400, Lmin 1..400); writes code/out/*.txt. |
| `probe_noise.py` | Statistical probe of residue sequence (autocorr, chi2, collisions): noise-flat. |
| `push_lmin_k6764.py` | Third standalone Lmin verifier k=1..6764. |
| `verify_c1_formula.py` | Verifies c1(k)=1+floor(k/phi^2) three independent routes k=1..400; writes code/out/c1_terms.txt. |
| `verify_lmin_formula.py` | Check Lmin(k)=k+NextFib(k)-1 for k=1..2583. |
| `verify_lmin_formula_f20.py` | Primary Lmin verifier k=1..6764 via bit-mask; helper-driven from code/lib/fibword.py. |
| `verify_lmin_formula_indep.py` | Independent cross-check of Lmin formula on sampled k. |
