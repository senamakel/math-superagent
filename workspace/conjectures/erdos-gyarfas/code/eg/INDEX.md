# Index — code/eg

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bruteforce_bound.py` | The verification-bound edge: uses nauty-geng to enumerate every connected min-degree-3 graph on n vertices (up to iso) and the exact oracle to test the Erdos-Gyarfas predicate, reporting counts and whether a counterexample exists. Shows where exhaustive generation stops being the method. Depends on lib.cycles. |
| `fast_girth_survivors.py` | Polynomial BFS-girth survivor counter for EG: counts connected min-degree≥3 graphs by order whose girth clears barrier g. Cheap enough to extend survivor sequences beyond the exponential oracle. |
| `find_n10_survivor.py` | _(undescribed)_ |
| `girth_survivors.py` | Sequence of obstruction survivors: counts connected min-degree-3 graphs on n vertices whose girth clears the first power-of-two barrier (girth >= 5, no 4-cycle). Shows how the first obstacle prunes the search space. Depends on lib.cycles (_geng_graph6, min_degree, girth). |
| `girth_survivors2.py` | Obstruction-survivor counter (n<=8, avoiding the n=9 hang): counts connected min-degree-3 graphs per order surviving each power-of-two barrier, using the exact cycle-length oracle (lib.cycles cycle_lengths) for the true no-power-of-2 count and BFS girth for the first-barrier (no-4) prune. Records the key subtlety that clearing length-8 requires exact cycle lengths (girth>=9), not merely girth>=5. Extends eg/girth_survivors.py to the exact no-pow2 count. Depends on lib.cycles. |
| `hand_dfs_check.py` | Independent-verification file: a fully hand-written DFS oracle (min_degree, girth, exact simple-cycle-length set, power-of-two lengths) with no imports from lib/cycles or lib/oracle, cross-checked against lib/cycles.py on K4, K3,3, cube Q3 and Petersen. A third, independent code path confirming the shelved oracle is not an artifact of one implementation. |
| `moore_bound.py` | _(undescribed)_ |
| `survivor_sequences.md` | Records the run's computed survivor counts by order and the Moore bound, the concrete numbers pattern_finder analyzed. |
| `verify_bound.py` | Verification-bound harness: (1) cross-checks the fast targeted power-of-two predicate (lib/egcheck) against the exact-cycle oracle (lib/cycles) on K4, K3,3, Petersen, cube Q3 and published cycle sets; (2) reproduces the EG verification bound for n=4..16 — counts connected min-degree-3 graphs per order (OEIS A007112) and, exploiting that a counterexample must be C4-free, counts C4-free survivors that lack a power-of-two cycle using geng -c -f -d3 (polynomial). NOTE: imports `lib.egcheck`, which is NOT present in code/lib/ (only cycles.py and oracle.py are) — this import currently fails; the harness depends on lib.cycles and an egcheck module that has not landed. |
| `verify_cycles.py` | Verification harness for the shelved lib/cycles.py: asserts min_degree, cycle_lengths, girth and power-of-two predicates on K4, K3,3, cube Q3, Petersen plus extra graphs (K5, K2,3, triangle, C5+C6, path P6). The run's regression check for the oracle; depends on lib.cycles. |
