# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `brute.captured.txt` | Brute-force oracle on the 7 witnesses: direct enumeration gives identical counts and occurrence sets (3003->8, rest->6), second independent route. |
| `brute_oracle.md` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `count_multiplicity.captured.txt` | Oracle run: 3003 verified 8 times; a<=10^7 scan reports exactly 7 values with N>=6 (3003:8; 120,210,1540,7140,11628,24310:6); every value cross-checked against the inversion multiplicity. |
| `diag_families.captured.txt` | _(undescribed)_ |
| `famA2.captured.txt` | _(undescribed)_ |
| `famB.captured.txt` | _(undescribed)_ |
| `famC.captured.txt` | _(undescribed)_ |
| `famD.captured.txt` | _(undescribed)_ |
| `family_pairs.json` | All collisions (values with >=2 canonical reps) for n<=1000, value<=1e18, plus the N>=6 values, exact. |
| `family_sequences.captured.txt` | _(undescribed)_ |
| `genus_table.captured.txt` | The deliverable: exact genus table for C(x,k1)=C(y,k2), the Faltings threshold (genus>=2 except {2,3},{2,4}), verified closed forms for the {2,n},{3,n},{4,n} families, and literature cross-checks. |
| `verify_family.captured.txt` | Equal-pair finder n<=1000: reproduces all 7 witnesses; Pell family C(n+1,k+1)=C(n,k+2) members j=1..4 (the infinite N>=6 family, Singmaster 1975). |
| `verify_library_claims.py` | _(undescribed)_ |
| `verify_mrstt_witnesses.captured.txt` | Captured output of code/verify_mrstt_witnesses.py (final run, EXIT_CODE=0): 3003's four witness pairs all equal 3003 with exactly 8 pairs in the triangle (mirrors included); all six N=6 witnesses + 3003 (N=8) reproduced by direct enumeration; Fibonacci family holds j=1..12; k<=log2(a)=39 candidates per a up to 10^12 (~1560 comb evaluations). |
| `witnesses.json` | Repro of the witness list: 3003:8 and the six 6-fold values with nontrivial canonical reps; conventions and scan bounds recorded. |
