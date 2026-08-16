"""Push the pair-injectivity verification much further (n to 256).
Claim remains: every nonempty M_d △ M_{d'} has multiplicity exactly 2 in the
ordered-pair multiset; empty has multiplicity n-2; #distinct = 1+C(n-2,2).
Fast path: use popcount-based size (no need to materialize) only for the count
of distinct sets we need the actual frozensets. We verify a few landmark n.
"""
from collections import Counter
from lib.collapse import S2_char
from math import comb

def main():
    for n in [64, 80, 96, 128, 160, 192, 256]:
        c = S2_char(n)
        empty_m = c.get(frozenset(), 0)
        nonempty = [m for A, m in c.items() if A != frozenset()]
        nonempty_ok = all(m == 2 for m in nonempty)
        empty_ok = empty_m == (n - 2)
        distinct_ok = len(c) == 1 + comb(n - 2, 2)
        total_ok = sum(c.values()) == (n - 2) ** 2
        print(f"n={n:4d} distinct={len(c):6d} pred={1+comb(n-2,2):6d} "
              f"empty={empty_m} nonempty_all2={nonempty_ok} "
              f"empty_ok={empty_ok} distinct_ok={distinct_ok} total_ok={total_ok} "
              f"-> {'ALL OK' if all([nonempty_ok,empty_ok,distinct_ok,total_ok]) else 'FAIL'}")

if __name__ == "__main__":
    main()
