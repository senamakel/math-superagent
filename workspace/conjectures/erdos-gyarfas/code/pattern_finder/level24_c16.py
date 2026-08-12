"""Process level 24 (from level_24_classes.txt) for the C16 profile."""
import sys, time
import networkx as nx

sys.path.insert(0, "/workspace/code/pattern_finder")
from census_c16_profile import has_c4, has_closed_cycle

def main(path):
    with open(path) as f:
        classes = [l.strip() for l in f if l.strip()]
    total = len(classes)
    t0 = time.time()
    aC4 = aC4C8 = aC4C16 = aC4C8C16 = 0
    c4free_hasC8 = 0
    for i, c in enumerate(classes):
        G = nx.from_graph6_bytes(c.encode())
        h4 = has_c4(G)
        if not h4:
            aC4 += 1
            h8 = has_closed_cycle(G, 8)
            h16 = has_closed_cycle(G, 16)
            if not h8 and not h16:
                aC4C8C16 += 1
            if not h8:
                aC4C8 += 1
            if not h16:
                aC4C16 += 1
            if h8 and not h16:
                c4free_hasC8 += 1
        if (i+1) % 5000 == 0:
            print(f"  processed {i+1}/{total}  elapsed {time.time()-t0:.0f}s", flush=True)
    print(f"n=24 total={total} avoidsC4={aC4} avoidsC4C8={aC4C8} "
          f"avoidsC4C16={aC4C16} avoidsC4C8C16={aC4C8C16} c4free_hasC8_notC16={c4free_hasC8}", flush=True)

if __name__ == "__main__":
    main("/workspace/code/out/expansion_census/level_24_classes.txt")
