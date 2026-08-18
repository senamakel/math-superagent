# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Lmin-formula-verified-6764.md` | Record of the verification: Lmin(k)=k+NextFib(k)-1 holds with 0 mismatches for k=1..6764, by three independent exact-integer programs; table of the 7 requested k-values. |
| `PE1006-verification.md` | Naive-oracle verification notes for PE1006 (Psi values and factor counts); companion to brute_oracle_results.md. |
| `README.md` | Workspace convention: what belongs in code/out (captured program output, not descriptions of programs), and how a computed result earns a claim block in derived/CLAIMS.md. |
| `brute_oracle_results.md` | Verified output of code/brute.py: Psi(3)=20302, Psi(10) mod 101001001=10699667, factor counts k+1 for k=1..20, full Psi(1..20) table; records the 2k-prefix sufficiency bug fix (bound 4k+8). |
| `c1_terms.txt` | c1(k) = number of distinct length-k Fibonacci subwords starting with '1', k=1..400, from verify_c1_formula.py; should equal 1+floor(k/phi^2). |
| `check_slope.captured.txt` | _(undescribed)_ |
| `check_slope.py` | Decisive slope check for the mechanical-word modelling of PE1006: verifies that slope 1/phi^2 (rational F(n-2)/F(n)) reproduces the problem's factor set at k=1..8 while the directive's literal slope F(n-1)/F(n) ~ 0.618 does not. For tool_builder to run; expected output is slope 34/89 and 1/phi^2 matching the brute oracle at every k, slope 55/89 and 1/phi failing at k=3. |
| `commands.log` | Appended verbatim log of every shell command run in this workspace and its stdout/stderr; the run's execution record. |
| `counts.txt` | k, number of distinct length-k factors harvested from a long prefix, OK/MISMATCH; written by code/pattern_hunt/gen_sequences.py, all OK. |
| `dj_mod.txt` | _(undescribed)_ |
| `dj_raw.txt` | _(undescribed)_ |
| `ext_recurrence.txt` | _(undescribed)_ |
| `extrecur_res.txt` | _(undescribed)_ |
| `lean_goal_statements.md` | Records the two top-level PE1006 Lean statements (G3 telescoped-v identity and psi_mech_reduction / pe1006_answer_active), their kernel status (compiles with declared sorry gaps), and the coefficient argument for the telescoping. |
| `lmin.txt` | k, Lmin(k) minimal prefix length containing all k+1 distinct length-k factors, for k=1..400; written by code/pattern_hunt/gen_sequences.py. |
| `mech_psi.captured.txt` | _(undescribed)_ |
| `psi_exact.txt` | k, Psi(k) exact big-int for k=1..25; written by code/pattern_hunt/gen_sequences.py. |
| `psi_residues.txt` | k, Psi(k) mod 101001001 for k=1..400; written by code/pattern_hunt/gen_sequences.py. |
| `r_runs_wythoff.txt` | Output of verify_R_runs_wythoff.py: run starts s_j=floor(j*phi^2), lengths histogram, Wythoff/zero-padding/S1-containment/J=Psi-recurrence verdicts, first 25 runs for k=1..3000. |
| `s1_exact.txt` | Exact values of S1(k)=sum V(w) over w in F_k with w*'1' in F_{k+1} (right-extension ones sum), k=1..3000, from verify_R_runs_wythoff.py. |
| `s1_res.txt` | _(undescribed)_ |
| `solution_checks.md` | _(undescribed)_ |
| `topelitz_defects.txt` | _(undescribed)_ |
| `ueuclid_main.captured.txt` | In-container __main__ run of code/lib/ueuclid.py (this cycle): ALL MONOID TESTS PASSED — acceptance 1-3 30/30 random (ueuclid == ueuclid_direct on S0/S1/S2/dR/dU), acceptance 2 (S1 at z=1 vs plain floor_sum) 30/30, deterministic 6/6, ue0 acceptance 30/30 (0-indexed wrapper vs literal loop), large-n ueuclid(514229,3,1346269,10^18,10^-1) dU=381966011250351898 == (514229*10^18+3)//1346269 in 0.29 ms. Convention is 1-INDEXED (t=1..n, weight z^(t-1); O(log) recursion verbatim fhq/LOJ138/OI-wiki). Supersedes the earlier 65-FAIL capture (0/30, caused by ueuclid_direct/docstring using 0-indexed while the recursion is 1-indexed — resolved by rewriting the oracle/docstring to 1-indexed and adding the 0-indexed ue0 wrapper). |
| `ueuclid_tests.captured.txt` | Stale: captured output of the OLD ueuclid_tests.py harness (an earlier module API), 20/20 ALL PASS — NOT evidence about current code/lib/ueuclid.py. Its source harness was deleted (stale, imported absent names); the current module runs its own __main__. |
| `vR_exact.txt` | Exact decimal values V(R_k) of the right-special factors R_k, k=1..3000, from verify_R_runs_wythoff.py. |
| `vR_res.txt` | _(undescribed)_ |
| `vr_rungaps.txt` | _(undescribed)_ |
| `vr_runvals.txt` | _(undescribed)_ |
