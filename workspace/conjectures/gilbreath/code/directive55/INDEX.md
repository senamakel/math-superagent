# Index — code/directive55

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `alt_indep_route.py` | Second independent route confirming alternating-2/4 ν₂=O(1) (nu2=1 at n to 5000) while w~n/2, using lib.rightdiag.incremental_diagonals (a different O(N^2) construction) instead of the rows-clip triangle. Rules out a generator/suffix-convention artifact. |
| `alt_trend_check.py` | Traces ν₂/w at increasing n (to 10000) for alternating-2/4, 2,2,4,2,4, all-gaps-4, consecutive-odds, showing the structured families' transfer ratio genuinely decays to 0 (nu2=O(1)). |
| `nu2_transfer_characterize.py` | Directive-55 main: for a 2-then-odds q computes triangle, right diagonal δ(q_n), ν₂ (both conventions), w(n); reproduces constant-gap refutation (consecutive-odds ν₂=0/1 O(1) while w=n-2), measures min ν₂/w and ν₂/n over primes and structured families, evaluates non-degeneracy hypotheses H_a..H_e. Oracle reproduces problem.md A_1..A_3; ν₂ cross-checks vs lib.rightdiag. Exact ints, O(M) memory. |
| `verify_findings.py` | Independent verification of Directive-55 findings: ν₂ (both conventions) matches lib.rightdiag.cycle_and_nu2 on primes (n=50..1000, 6/6 match); hand-checked alternating-2/4 n=10 triangle showing both bit values present yet nu2=O(1). |
| `verify_success.py` | Confirms the alternating-2/4 and 2,2,4,2,4 families are SUCCESSFUL 2-then-odds sequences (leading A_k(0)=1) to depth 3000, with ν₂=O(1) (1 and 2) while w~n/2. Establishes these are genuine counterexamples to any listed H restoring the transfer, not degenerate/non-successful. |
