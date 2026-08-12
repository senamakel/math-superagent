# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `BFILE_CHECK.md` | Independent PE241 verification report: the OEIS A159907 b-file route. Lists all 22 hemiperfect terms <= 10^18 with per-term abundancy verification (all confirmed 2*sigma/n = odd int), the exact total 482316491800641154, the first excluded term (index 23), and the (not-performed, RUN_LOG absent) DFS cross-check section. |
| `bfile_check.py` | Independent PE241 verification: reads the A159907 b-file, extracts all terms <= 1e18 (terms 1..22), verifies each term's abundancy 2*sigma(n)/n is an odd integer by exact trial-division sigma, sums them exactly, and cross-checks against the DFS RUN_LOG if present. Writes code/BFILE_CHECK.md. |
| `brute.py` | Oracle brute force for PE241: sieve spf up to N, recover sigma(n), keep n with 2*sigma(n)/n an odd integer, print n, sigma, p(n) reduced, k=(2p-1)/2. Confirmed sigma(6)=12. For N=10^7 (5.52s) finds n: 2(k=1), 24(k=2), 4320, 4680, 26208 (k=3), 8910720 (k=4); reconfirms 2,24,4320,4680,26208 for the smaller range; sum <= 10^7 = 8945954. |
| `check_2adic_approach.py` | _(undescribed)_ |
| `check_structure.py` | _(undescribed)_ |
| `check_structure_fast.py` | _(undescribed)_ |
| `classify_terms.py` | _(undescribed)_ |
| `count_signatures.py` | Counts exponent signatures (integer partitions, nonincreasing exponents) whose minimal prime assignment stays under a bound; tests feasibility of the signature-first approach. |
| `crosscheck_oeis.py` | _(undescribed)_ |
| `dbg_dfs.py` | _(undescribed)_ |
| `dfs_corrected.py` | _(undescribed)_ |
| `diag_26208.py` | _(undescribed)_ |
| `factors22.py` | _(undescribed)_ |
| `hemiperfect_dfs.py` | Reference implementation of the forced-denominator cancellation DFS for hemiperfect numbers <= 10^18 (template; not executed in this environment — no shell available). Validates the recursion described in the report. |
| `maxab.py` | _(undescribed)_ |
| `pattern_relations.py` | _(undescribed)_ |
| `perk_seqs.py` | Stores the per-abundancy-k subsequences of the 22 known hemiperfects (K2,K3,K4,K5) for the sequence tools. All show no polynomial/recurrence structure. |
| `quotients.py` | _(undescribed)_ |
| `run_count_signatures.py` | _(undescribed)_ |
| `seqgen.py` | _(undescribed)_ |
| `seqsieve.py` | _(undescribed)_ |
| `solution.py` | _(undescribed)_ |
| `sum_answer.py` | _(undescribed)_ |
| `sum_in_range.py` | _(undescribed)_ |
| `trace_dfs.py` | _(undescribed)_ |
| `trace_fixed.py` | _(undescribed)_ |
| `verify_2adic.py` | _(undescribed)_ |
