# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working instructions for the code/ tree: the package layout (lib/ for imports, question folders, out/ for outputs), the rule that /workspace/code is on PYTHONPATH (never sys.path.insert), naming and complexity conventions, one-job-per-file, keeping the naive program as the oracle, exact arithmetic, and never deleting a program that carries a result. Guidance for agents writing code in this run — describes the tree, not mathematics. |
| `brute.py` | Naive oracle for Erdős–Gyárfás: minimum_degree(adj), cycle_lengths(adj) (exact set of simple-cycle lengths by DFS enumeration; exponential, small-graphs-only), powers_of_two_cycle_lengths, has_power_of_two_cycle, plus from_graph6/from_networkx input helpers. Embeds the hand-built worked examples (K4, K3,3, Petersen, cube Q3, graph6 K4) in run_here() as the verification oracle for the run. This is the naive program; lib/cycles.py is the importable library twin of the same oracle. Cross-checked against lib/cycles.py (via networkx.simple_cycles) on K4, K3,3, Petersen and cube Q3: all four agree on min-degree and cycle-length set. |
| `verify_cycles.py` | Verification harness for code/lib/cycles.py: checks min_degree and cycle_lengths against hand-known answers for K4 ({3,4}), K3,3 ({4,6}), cube Q3 ({4,6,8}), and Petersen ({5,6,8,9}). Run: `cd code && python verify_cycles.py`. All four MATCH (output recorded in this run). |
