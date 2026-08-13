# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `genus_table.captured.txt` | The deliverable: exact genus table for C(x,k1)=C(y,k2), the Faltings threshold (genus>=2 except {2,3},{2,4}), verified closed forms for the {2,n},{3,n},{4,n} families, and literature cross-checks. |
| `count_multiplicity.captured.txt` | Oracle run: 3003 verified 8 times; a<=10^7 scan reports exactly 7 values with N>=6 (3003:8; 120,210,1540,7140,11628,24310:6); every value cross-checked against the inversion multiplicity. |
| `verify_family.captured.txt` | Equal-pair finder n<=1000: reproduces all 7 witnesses; Pell family C(n+1,k+1)=C(n,k+2) members j=1..4 (the infinite N>=6 family, Singmaster 1975). |
| `brute.captured.txt` | Brute-force oracle on the 7 witnesses: direct enumeration gives identical counts and occurrence sets (3003->8, rest->6), second independent route. |
| `family_pairs.json` | All collisions (values with >=2 canonical reps) for n<=1000, value<=1e18, plus the N>=6 values, exact. |
| `witnesses.json` | Repro of the witness list: 3003:8 and the six 6-fold values with nontrivial canonical reps; conventions and scan bounds recorded. |
