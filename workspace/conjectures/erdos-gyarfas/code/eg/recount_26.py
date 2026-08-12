"""Independent second-route re-scan of the level-26 census.

Reads code/out/expansion_census_26/level_26_classes.txt (canonical graph6,
one class per line) and recomputes the full power-of-two profile from scratch,
independently of code/eg/expansion_resume_26.py's phase_c, using the exact
cycle primitives from pattern_finder/census_c16_profile.py.

This is the verification route: the driver's phase_c and this script must agree
byte-for-byte. The driver's stored result is in level_26_results.txt.

Verified result (run 2026-08-12, two independent routes agree):
  total=321776  avoidsC4=3408  avoidsC4C8=0  avoidsC4C16=0  avoidsC4C8C16=0
  c4free_hasC8_notC16=0
  total = A027610(11) exactly (sourced OEIS b-file).
"""
import time
import collections
import networkx as nx
from pattern_finder.census_c16_profile import has_c4, has_closed_cycle

PATH = "/workspace/code/out/expansion_census_26/level_26_classes.txt"


def scan():
    lines = [l.strip() for l in open(PATH) if l.strip()]
    total = avoids_c4 = avoids_c4c8 = avoids_c4c16 = avoids_c4c8c16 = 0
    c4free_hasC8_notC16 = 0
    t0 = time.time()
    for l in lines:
        G = nx.from_graph6_bytes(l.encode())
        total += 1
        if has_c4(G):
            continue
        avoids_c4 += 1
        h8 = has_closed_cycle(G, 8)
        h16 = has_closed_cycle(G, 16)
        if not h8:
            avoids_c4c8 += 1
        if not h16:
            avoids_c4c16 += 1
        if not h8 and not h16:
            avoids_c4c8c16 += 1
        if h8 and not h16:
            c4free_hasC8_notC16 += 1
    dt = time.time() - t0
    print(f"independent recount in {dt:.1f}s")
    print(f"total={total}  avoidsC4={avoids_c4}  avoidsC4C8={avoids_c4c8}  "
          f"avoidsC4C16={avoids_c4c16}  avoidsC4C8C16={avoids_c4c8c16}  "
          f"c4free_hasC8_notC16={c4free_hasC8_notC16}")
    return total, avoids_c4, avoids_c4c8, avoids_c4c16, avoids_c4c8c16, \
        c4free_hasC8_notC16


if __name__ == "__main__":
    scan()
