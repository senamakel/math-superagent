# Index — code/out/verify

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_directive6_anchors.py` | Independent-verification of directive-6 anchors 34432237 (k=10^4, count 10001) and 20938836 (k=10^6, count 1000001) by the window/residue route itself: distinct length-k windows of fib_prefix(k+NextFib(k)-1) read as decimals, squares summed mod M, de-duplicated by residue pairs, count asserted k+1. Includes strict-NextFib sanity for k=3. |
| `check_phase4_anchors.py` | Independent-verification of the k=10^4 acceptance anchor: recomputes Psi(10^4) by the valid direct (psi_direct) method and compares against the directive-6 anchor 34432237 (old Phase-4 anchor 16242174 refuted, no longer a target). |
| `conjugate_christoffel_factor_sturmian-0be2e715.json` | _(undescribed)_ |
| `directive6-anchors-verified.md` | Records the in-container verification of the directive-6 acceptance anchors Psi(10^4)=34432237 and Psi(10^6)=20938836 by the window/residue route; releases the directive-10 Lean hard gate. |
| `fibonacci_sturmian_complexity-1649cd8e.json` | _(undescribed)_ |
| `fibonacci_word_sturmian_density_balance-6f1716f4.json` | _(undescribed)_ |
| `g1_factor_chain_nested-de74dba9.json` | _(undescribed)_ |
| `g1_oracle_length3-ed70ff6a.json` | _(undescribed)_ |
| `g1_sturmian_factor_structure-09b161ff.json` | _(undescribed)_ |
| `governing_factor_complexity-542ce8cd.json` | _(undescribed)_ |
| `governing_sturmian-f892cba8.json` | _(undescribed)_ |
| `governing_universal_euclidean-6e83e0b7.json` | _(undescribed)_ |
| `mechanical_word_digit_rule-f4995b0e.json` | _(undescribed)_ |
| `monoid_composition_formulas_verified-9ccd80eb.json` | _(undescribed)_ |
| `pe1006_psi_G1_sturmian_factor_structure-87f94deb.json` | _(undescribed)_ |
| `pe1006_psi_G2_mechanical_word_representation-1f79c34f.json` | _(undescribed)_ |
| `pe1006_psi_G3_telescoped_second_moment-7bd1c5f8.json` | _(undescribed)_ |
| `pe1006_psi_G4_universal_euclidean_floor_sum-7383014a.json` | _(undescribed)_ |
| `req_close_universal_euclidean-4773c60b.json` | _(undescribed)_ |
| `universal_euclidean_geometric_floor_sum-8768a07e.json` | _(undescribed)_ |
| `window_residue_route.captured.txt` | Captured output of running window_residue_route.py in-container: k=3 factor set {1,10,100,101} Psi=20302; k=10 Psi(10)=10699667 count 11; k=10^4 Psi=34432237 distinct 10001; k=10^6 Psi=20938836 distinct 1000001 in 1.2s; k=1..60 agree with brute.py. ALL CHECKS PASS = True. |
| `window_residue_route.py` | In-container verification of the directive-6 anchors by the independent sliding-window residue route. Builds prefix W of length L = k + NextFib(k) - 1 + k (NextFib strict), keeps each window's value as TWO independent sliding residues mod M=101001001 and mod M2=1000000007 via w_{r+1} = (10·w_r − y_r·10^k + y_{r+k}) mod m, dedups by the residue pair, asserts distinct count == k+1, and sums squares of distinct residues mod M = Psi(k). Reproduces Psi(3)=20302/{1,10,100,101}, Psi(10)=10699667, Psi(10^4)=34432237 (10001), Psi(10^6)=20938836 (1000001), and agrees with brute.py for k=1..60. The two-residue design fixes the single-modulus collision where distinct M-congruent factors collapse (k=10: M and 10·M both residue 0). |
