# Index — code/pattern_hunt

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_corr_translation.py` | Tests translation-invariance of the factor-set pair-correlation C(i,j); shows it holds only at k=F_n-1, refuting the lag-sum reduction at general k. |
| `check_directive1.py` | Verify directive-1 pair-correlation/autocorrelation formula vs brute exact Psi at k=F_n-1 (n=2..7): brute==rot==corr==exact, all True. |
| `check_directive1_big.py` | Extend directive-1 verification to n=2..12 (k up to 232): rotation set == brute factor set, autocorrelation formula == rotation Psi, exact big integers. |
| `check_leading_counts.py` | Clean recomputation of lead-1/lead-0 factor counts (k=1..30); totals always k+1, lead-1 sequence 1,1,2,2,2,3,3,4,4,4,5,... |
| `check_lmin.py` | Early probe: compares Lmin to floor(phi^2 k) and A344953 terms; superseded by verify_lmin_formula.py (kept as the refutation record). |
| `check_weight_dist.py` | Tabulates length-k Fibonacci subword counts by weight (#1s); confirms exactly two weights floor/ceil(k/phi^2) for k=1..30 (Sturmian balance). |
| `extract_subseqs.py` | Extract subsequences Psi mod M at k=F_m-1/F_m/F_m+1 and leading-digit factor counts; probes noise/structure at Fibonacci indices. Superseded by cleaner check_leading_counts.py. |
| `gen_sequences.py` | Generate PE1006 integer sequences: Psi(k) exact (1..25), Psi(k) mod 101001001 (1..400), Lmin(k) minimal prefix length (1..400); count/stability self-checks, bit-mask factor extraction. Writes code/out/psi_residues.txt, psi_exact.txt, lmin.txt, counts.txt. |
| `probe_noise.py` | Statistical probe of residue sequence: autocorrelation, leading-digit chi2, collision count. Verdict: residues noise-flat (no scalar recurrence survives mod M). |
| `push_lmin_k6764.py` | Third standalone Lmin verifier, full range k=1..6764, bit-mask. Output: zero mismatches, all ok. |
| `verify_c1_formula.py` | Verifies c1(k)=1+floor(k/phi^2) = # length-k Fibonacci subwords starting with '1', three independent routes agreeing on k=1..400; writes code/out/c1_terms.txt. |
| `verify_lmin_formula.py` | Check Lmin(k) = k + NextFib(k) - 1 for k=1..2583 with 6765-char prefix, all Fibonacci-boundary checks, matches hardcoded A344953 terms; also refutes Lmin = floor(k phi^2) (992 fails). Writes nothing; prints report. |
| `verify_lmin_formula_f20.py` | Primary Lmin verifier: Lmin(k)=k+NextFib(k)-1 for k=1..6764 via bit-mask factor extraction on 28657-char prefix, helper-driven from code/lib/fibword.py. Output: zero mismatches. |
| `verify_lmin_formula_indep.py` | Independent cross-check of Lmin formula on 49 sampled k (all Fibonacci boundaries through 6764) via plain Python substrings, no bit-mask. Output: 0 mismatches. |
