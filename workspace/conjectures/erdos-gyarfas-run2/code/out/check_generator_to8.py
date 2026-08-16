"""Confirm what the OLD generator output (1,1,4,19,121 for n=3..7 from the
command log) actually counted, and get the true 2-connected counts to n=8 by
running the CURRENT corrected generator (networkx VF2 dedup) to n_target=8.

The old layer_by_layer started from a triangle and only added path ears (never
chords), so it produced only 2-connected graphs that (a) contain a triangle and
(b) are built without any chord-addition step. The corrected version seeds all
cycles and adds both path ears and chords, giving all 2-connected graphs.
"""
import networkx as nx
from lib.biconnected_gen import generate_2connected_levels

print("Running current generator to n_target=8 (all 2-connected)...")
levels = generate_2connected_levels(8)
for n in range(3, 9):
    print(f"n={n}: generator={len(levels.get(n, []))}")
