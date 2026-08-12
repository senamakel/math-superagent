"""Cross-check fast has_c4/has_c8 vs lib.cycle_oracle on the census classes.

For every class at every level reached, assert fast has_c4 == (4 in oracle),
and on C4-free classes assert fast has_c8 == (8 in oracle). This is what
establishes the fast checker is correct before it runs at full size.
"""
import sys
import networkx as nx
sys.argv  # noqa
from eg.expansion_census_fast import has_c4, has_c8
from lib.cycle_oracle import oracle


def check_level(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    bad = 0
    for c in lines:
        H = nx.from_graph6_bytes(c.encode())
        lens = set(oracle(H)[1])
        if has_c4(H) != (4 in lens):
            print(f"C4 MISMATCH on {c}: fast={has_c4(H)} oracle={4 in lens}")
            bad += 1
        if 4 not in lens:
            if has_c8(H) != (8 in lens):
                print(f"C8 MISMATCH on {c}: fast={has_c8(H)} oracle={8 in lens}")
                bad += 1
    print(f"{path}: {len(lines)} graphs, {bad} mismatches")
    return bad


if __name__ == "__main__":
    total = 0
    for n in range(6, 25, 2):
        import os
        p = f"/workspace/code/out/expansion_census/level_{n}.canon"
        if os.path.exists(p):
            total += check_level(p)
    print("TOTAL MISMATCHES:", total)
