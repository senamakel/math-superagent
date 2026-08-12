# Index — scratchpad

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `holonomic_probe.py` | Rigorous P-recursive extrapolation probe for PE763 D(N): confirms D(2)=3, D(10)=44499 via lib.amoeba.D, then sweeps lib.holonomic.fit over (m=1..5, d=1..3) x (K=11..14) with exact rational arithmetic, checking whether ANY nullspace solution reproduces ALL held-out points D(K..14). Result (written to holonomic_probe.txt): no recurrence passes — every low-order P-recursive fit overfits and breaks on the first out-of-sample term, so P-recursive extrapolation cannot reach D(10000). P-recursive extrapolation verdict: not viable. |
| `holonomic_probe.txt` | Output of holonomic_probe.py: the raw sweep log over (m,d) x K showing that no low-order P-recursive recurrence reproduces all held-out points D(K..14), establishing the negative result that P-recursive extrapolation cannot reach D(10000). Companion to the .py whose description carries the verdict. |
| `structure_probe.txt` | Output of code/inventor/structure_probe.py (and definitive_check.py): per-level structural decomposition of the 3D amoeba reachable configs for N=0..8 — D(N), A1/A2tri/A2empty/A3 failure counts, whether D(N+1)=sum f(C) holds (B), the by-max-level-M, by-f and joint (M,f) tables, and the most frequent level histograms. Records how the D(N+1)=sum f(C) identity breaks from N=3 on and which collapse claims fail. |
