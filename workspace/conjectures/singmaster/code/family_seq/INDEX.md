# Index — code/family_seq

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `family_sequences.py` | Exact multiplicity counter for the infinite N(a)>=6 family C(n+1,k+1)=C(n,k+2) with n_i=F_{2i+2}F_{2i+3}-1, k_i=F_{2i}F_{2i+3}-1 (i=1,2,...). Computes exact N(a_i) for i=1..4 under the both-mirrors+trivial convention by inverting C(n,k)=a per small k (binary search, k<=log2(a)) with no triangle built; verifies the recurrences n_i=7n_{i-1}-n_{i-2}+6, k_i=7k_{i-1}-k_{i-2}+9 and Lucas identities u_i=5n_i+6=L_{4i+5}, v_i=5k_i+9=L_{4i+3} for i=1..12, and the identity C(n+1,k+1)=C(n,k+2) by direct comb for i=1..7. Returns/prints exact N(a_1..a_4)=8,6,6,6. Correctness: N(3003)=8 asserted internally matches code/out/witnesses.json and the independent brute oracle code/brute.py; a_1=3003 reproduced. Run: PYTHONINTMAXSTRDIGITS=1000000 timeout 540 python3 code/family_seq/family_sequences.py, output code/out/family_sequences.captured.txt (program ends "All done"). Note the old version timed out (EXIT=124) because it computed a_i for i up to 8 (multi-gigabyte integers); scope was correctly bounded to identity i<=7, recurrences i<=12, exact N i<=4. |
