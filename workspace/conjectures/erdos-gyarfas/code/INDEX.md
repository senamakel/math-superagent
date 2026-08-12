# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working instructions for the code/ tree: the package layout (lib/ for imports, question folders, out/ for outputs), the rule that /workspace/code is on PYTHONPATH (never sys.path.insert), naming and complexity conventions, one-job-per-file, keeping the naive program as the oracle, exact arithmetic, and never deleting a program that carries a result. Guidance for agents writing code in this run — describes the tree, not mathematics. |
| `brute.py` | Naive-oracle demo and worked-example harness: builds K4, K3,3, Petersen, cube Q3 by hand and prints min_degree and cycle-length set, importing the compute-core from the shelf (lib.cycles via lib.oracle) instead of carrying its own DFS copy. Verification demo, not a separate implementation. |
| `verify_cycles.py` | Verification harness for the shelved lib/cycles.py: checks min_degree and cycle_lengths on K4, K3,3, cube Q3 and Petersen against hand-known answers. Run: cd code && python verify_cycles.py. A non-importing duplicate of the oracle itself; depends on lib.cycles being right. |
