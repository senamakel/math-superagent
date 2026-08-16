# Index — scenario

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `attack_eigen_recurrence.py` | Attacks/pushes the fixed-type eigen-recurrence (fixed type t column S(d-1,t+1) is C-finite, char poly prod_{j=1}^{t+1}(x-j)) to degree 120, and confirms the Bell-total column is not C-finite. |
| `badprime_upper_bound_seq.py` | Computes log10 of the Schaub-Spivakovsky bad-prime upper bound B(n) (2411.13967 Cor 3.2) for n=3..12 via log-gamma (forming the exact integer C! is impossible). Establishes the bound's log grows super-exponentially (no polynomial/CC-recurrence); a dead end for pattern work, recorded so it is not recomputed. |
| `badprimes_criterion.py` | _(undescribed)_ |
| `check_d13.py` | Brute-force check of the scenario-count law (by-type = Stirling S(d-1,t+1), total = Bell(d-1)) at degree d=13, pushing one degree past the run's earlier d=2..8,12. Confirmed. |
| `check_d14_15.py` | Brute-force check of the scenario-count law at degrees 14 and 15. Confirmed at both (Bell(13)=27644437, Bell(14)=190899322). |
| `check_scenarios.py` | _(undescribed)_ |
| `criterion_counts_extended.py` | Computes count of distinct primes p dividing (d choose i)-1 for some i (Schaub-Spivakovsky sufficient bad-prime criterion) for d=2..40; sequence confirmed irregular, no recurrence. |
| `discrepancies_96_98.py` | Pinpoints why 96 and 98 are the only genuine discrepancies between the published open-degree list (Castryck 2012 eq 6.5) and m<=7 settled-family coverage: 98=2*7^2 covered by 2p^k; 96 has no m*p^k cover (p=2 bad for 3 and for 6). |
| `full_coverage_reconcile.py` | Reconciles n=96 and n=98 against the FULL m<=7 settled-family coverage (including 6p^k with the 53 d=6 bad primes, and 7p^k with the 127-bound). Confirms the only two inconsistent degrees under the corrected comparison are {96, 98}: 98 settled-but-listed-open, 96 open-but-unlisted. This corrects an earlier draft that declared 96 "not a discrepancy". |
| `general_law.py` | _(undescribed)_ |
| `type_columns.py` | Prints fixed-type scenario-count columns S(d-1,t+1) for d=3..16 from the exact Stirling closed form; the raw data that type_columns_check.py verifies the eigen-recurrence on. |
| `type_columns_check.py` | Verifies that for fixed type t, the scenario count S(d-1,t+1) satisfies the constant-coefficient recurrence of order t+1 with char poly prod_{j=1}^{t+1}(x-j); checks it exactly over up to 29 terms for t=0..12. Derived from the Stirling closed form, checked not merely fitted. |
| `verify_open_degrees.py` | Checks whether the published open-degree list <= 100 (Castryck 2012 eq 6.5) equals the complement of the m<=5 settled-family coverage (p^k,2p^k,3p^k,4p^k,5p^k plus bad-prime exclusions). Uses the correct set-difference comparison. The m<=5 restriction intentionally excludes 6/7 families, so 96/98 discrepancies are expected boundary artifacts (see verify_open_degrees_check.py). |
| `verify_open_degrees_check.py` | Independent harness that implements BOTH the correct open-degree comparison (pub_open == not covered) and the old buggy pub!=cov collector, with negative controls (n=16 settled, n=20, n=28 open all consistent under correct, falsely flagged under buggy). Confirms exactly two genuine discrepancies: 98 (settled but on published open list), 96 (uncovered but absent from published open list). |
