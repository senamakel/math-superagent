# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `cycles.py` | Exact oracle for the Erdős–Gyárfás run: min_degree(graph), girth(graph), cycle_lengths(graph) (exact set of simple-cycle lengths via networkx.simple_cycles, exponential so small-graphs-only), has_power_of_two_cycle(graph), power_of_two_cycle_lengths(graph). All-exact, no floats. Written by tool_builder as the ground-truth checker; correctness against hand cases (K4, K3,3, cube, Petersen) is the tool_builder's verification claim, not yet re-verified here. |
