# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `threshold_analysis.p` | TPTP attack encoding G3's universal inequality at the singleton a=1; find_counterexample returns CounterSatisfiable (refuted). |
| `threshold_analysis.py` | Exact brute-force oracle computing U_d(a)=max over A⊆E, |
| `threshold_analysis_finding.md` | Records the refutation of G-threshold-analysis: singleton A={a} gives |
| `threshold_shadow_brute.py` | Brute-force computation of |
| `threshold_shadow_compare.py` | Brute-force comparator of true extremal |
| `threshold_shadow_core.p` | Machine evidence for the G-threshold-shadow refutation: propositional core asserting all 8 odd vertices have <=1 neighbour in A={0000,1111}; conjecture negated, returns refuted via find_counterexample. |
| `threshold_shadow_finding.md` | Interim hand computation of the n=4,d=1,a=2 counterexample to G-threshold-shadow (A={0000,1111} beats every Hamming ball). |
| `threshold_shadow_refuted.md` | Records the refutation of G-threshold-shadow: A={0000,1111} in n=4 gives |
