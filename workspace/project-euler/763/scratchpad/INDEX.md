# Index — scratchpad

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `holonomic_probe.py` | Rigorous P-recursive extrapolation probe for PE763 D(N): confirms D(2)=3, D(10)=44499 via lib.amoeba.D, then sweeps lib.holonomic.fit over (m=1..5, d=1..3) x (K=11..14) with exact rational arithmetic, checking whether ANY nullspace solution reproduces ALL held-out points D(K..14). Result (written to holonomic_probe.txt): no recurrence passes — every low-order P-recursive fit overfits and breaks on the first out-of-sample term, so P-recursive extrapolation cannot reach D(10000). P-recursive extrapolation verdict: not viable. |
