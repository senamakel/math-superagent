# Index — code/research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `ground_truth_records.py` | Ground-truth experiment for the no-passing-platoon / right-to-left record-minima reading of the large-L model: tests whether the bump-graph leader set (boats that never bump = out-degree-0 roots) equals the right-to-left record minima of speeds when L is huge, and how a finite finish line L breaks that equality (finish events are inverse-exponential, so magnitudes matter). Also characterizes chain-pairs under the record structure. MC diagnostic, not a solver. |
| `run_ground_truth.sh` | Convenience runner invoking ground_truth_records.py with fixed args (seed 1, 20000 trials, huge L=1e8, n=5) to demonstrate the leader==records agreement at large L. Not itself a solver; just reproduces the MC run. |
