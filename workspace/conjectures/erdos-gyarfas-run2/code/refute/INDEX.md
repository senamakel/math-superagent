# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `heawood_8cycle.p` | TPTP encoding of the Heawood graph (exact Fano incidences as axioms) with the conjecture "contains an 8-cycle", used to probe the danger case of settled rung R-delta3-n16-three-targets. |
| `heawood_n16.py` | Refutation probe for settled rung R-delta3-n16-three-targets: checks whether the Heawood graph (smallest cubic girth-6 graph, n=14) and Petersen have an 8-cycle, which would falsify the n<=16 claim if absent. |
| `n12_counterexample.p` | TPTP counterexample model search for the n<=12 rung R-delta3-n12-small-target, restricted to its only danger case (girth-5 graph on 12 vertices): min-degree-3 graph on v0..v11, conjecture that it has a 4- or 8-cycle. A refuting model is a real counterexample. |
| `n16_counterexample.p` | TPTP counterexample model search for the settled rung R-delta3-n16-three-targets: axioms say edge is a symmetric irreflexive min-degree-3 graph on 16 vertices, conjecture says it contains a 4/8/16-cycle. A model refuting the conjecture would be a real counterexample proving the rung false. |
| `n16_girth6_danger.p` | Placeholder documenting that the girth-6 no-C8 danger on 15/16 vertices is a 16-vertex model search the solver cannot decide; reasoning lives in refute_report.md. |
| `petersen_8cycle.p` | Second independent mechanism (find_counterexample) verifying the oracle's claim that the Petersen graph has an 8-cycle, pinning the graph exactly and conjecturing 8-cycle existence. |
| `refute_report.md` | Refuter's report on attacking the asserted-settled rungs R-delta3-n12-small-target and R-delta3-n16-three-targets: structural Moore-bound reduction to the girth-5/girth-6 8-cycle danger cases, the hand-checked Heawood 8-cycle, the Petersen confirmation, what the find_counterexample searches returned, and the honest verdict that "settled" exceeds the run's current machine evidence. |
