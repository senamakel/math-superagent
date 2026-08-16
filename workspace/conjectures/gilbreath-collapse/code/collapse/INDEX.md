# Index — code/collapse

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_evenness_collapse.py` | Verifies evenness-collapse: S(n,h) and S2(n,h) are constant on each v(h)-fiber (adjacent-XOR), fibers are exactly the pairs {h, not-h} of size 2, for n=3..12 (all 2^12=4096 strings cheap). Uses canonical oracle lib.collapse (downset, T, S, S2). Carries a negative control S_broken (XOR over odd-sized set M_d minus min vertex, |
| `verify_n5.py` | Independent re-verification (differently structured) of the n=5 refutation: confirms K=2 gives S2 constancy on every fiber (28 fibers) while K=1 has a witness (h=01011 S2=9 vs h=01101 S2=1, same C_1 key (0,2,1,1)). Proves min K at n=5 is exactly 2, refuting ceil(5/2)=3. |
| `witness_crosscheck.py` | Independent fresh cross-check of the COLLAPSE claim K*(n)=ceil(n/2). Enumerates all 2^n strings for n=4..12, groups by C_K fibers (all N_ab(k) for 1<=k<=K), finds the minimal K with S2 constant per fiber, and reports witnesses. Does NOT import lib.collapse. Found n=5 is a counterexample (min K=2, not 3). Output saved to code/out/witness_crosscheck_out.txt. |
