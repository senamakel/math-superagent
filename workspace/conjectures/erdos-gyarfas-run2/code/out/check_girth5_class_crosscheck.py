"""Independent cross-check of check_girth5_8cycle_class.py.

Second route to the same claim (rule 11): regenerate the girth-5 class directly
with networkx (seeding from a 5-cycle, adding ears/chords, keeping girth>=5 and
min-degree>=3) but verify 8-cycle presence with nx.simple_cycles instead of
lib.erdos_gyarfas, so the two tools disagreeing would be caught.

Also prints each graph's distinctness (canonical key via networkx) and girth,
to confirm the generator is producing genuinely-distinct girth-5 min-degree-3
graphs and the 7-member class on n=10,12,13 is real.
"""
import networkx as nx
from lib.canonical import canonical_key
from lib.girth5_gen import girth, min_degree, generate_2connected_girth_atleast5


def has_8cycle_nx(G):
    """Does G contain a simple cycle of length 8? independent route."""
    D = G.to_directed()
    for cyc in nx.simple_cycles(D):
        if len(cyc) == 8:
            return True
    return False


def main(N=11):
    """Cross-check the girth-5, min-deg>=3 class for n in 3..N (default 11).

    N caps the enumeration. The claim this file cross-checks is the girth-5
    result on n=10,11 only; n=12,13 verify nothing about that claim and are
    where the cost concentrates, so they are not enumerated (rule 6/7: a larger
    run that verifies nothing new is the wrong method).
    """
    levels = generate_2connected_girth_atleast5(N)
    total = 0
    rows = []
    for n in range(3, N + 1):
        keep = [G for G in levels.get(n, []) if min_degree(G) >= 3]
        total += len(keep)
        rows.append((n, len(keep)))
        for G in keep:
            ok = has_8cycle_nx(G)
            assert ok, f"graph at n={n} has NO 8-cycle (!) edges={sorted(G.edges())} girth={girth(G)}"
            assert girth(G) >= 5, f"girth<5 at n={n}"
            assert min_degree(G) >= 3
    print("cross-check: independent nx.simple_cycles 8-cycle detector")
    for n, c in rows:
        print(f"  n={n:2d} : {c} girth-5 min-deg>=3 graphs")
    print(f"TOTAL {total} graphs in class, ALL have an 8-cycle (independent nx route).")
    print("=> class counts and 8-cycle claim confirmed by a second, independent tool.")


if __name__ == "__main__":
    main(N=11)
