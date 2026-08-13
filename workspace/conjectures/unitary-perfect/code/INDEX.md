# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive exact oracle for unitary perfect numbers: factors n by trial division, computes sigma_star(n) = prod_{p^a||n}(p^a+1) in exact integers, decides is_unitary_perfect(n) := sigma_star(n)==2n. Also reports the product identity prod(1+1/p^a)==2 and the 2-adic budget identity sum v2(p^e+1)==a+1. Verified against all five known unitary perfect numbers (6,60,90,87360, fifth) and the negative controls 12,28 in code/out/brute_oracle.captured.txt. This is the deliberately-slow oracle; it is not meant for search. |
