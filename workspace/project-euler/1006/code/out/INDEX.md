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
| `lmin.txt` | k, Lmin(k) minimal prefix length containing all k+1 distinct length-k factors, for k=1..400; written by code/pattern_hunt/gen_sequences.py. |
| `psi_exact.txt` | k, Psi(k) exact big-int for k=1..25; written by code/pattern_hunt/gen_sequences.py. |
| `psi_residues.txt` | k, Psi(k) mod 101001001 for k=1..400; written by code/pattern_hunt/gen_sequences.py. |
