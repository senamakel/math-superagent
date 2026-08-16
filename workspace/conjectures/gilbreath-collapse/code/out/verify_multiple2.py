"""Verify the structural claim about the S2_char multiset for n=2..60:

CLAIM (candidate): the multiset { M_d △ M_{d'} } over ordered pairs d,d' in
[2,n-1] consists of
   - the empty set, with multiplicity (n-2)   [the d = d' pairs]
   - every other set, with multiplicity exactly 2.
Equivalently the map (d,d') -> M_d △ M_{d'} restricted to unordered pairs
{d,d'}, d != d', is INJECTIVE, and there are C(n-2,2) distinct nonempty sets.

Check by computing the multiplicity histogram and verifying:
   - empty multiplied by (n-2)
   - all nonempty multiplicities == 2
   - #distinct sets == 1 + C(n-2,2)
   - sum multiplicities == (n-2)^2
"""
from collections import Counter
from lib.collapse import S2_char
from math import comb

def main():
    all_ok = True
    for n in range(2, 61):
        c = S2_char(n)
        mults = Counter(c.values())
        empty_m = c.get(frozenset(), 0)
        # nonempty multiplicities
        nonempty = [m for A, m in c.items() if A != frozenset()]
        nonempty_ok = all(m == 2 for m in nonempty)
        empty_ok = (empty_m == (n - 2))
        distinct_ok = (len(c) == 1 + comb(n - 2, 2))
        total_ok = (sum(c.values()) == (n - 2) ** 2)
        ok = empty_ok and nonempty_ok and distinct_ok and total_ok
        all_ok &= ok
        if not ok or n <= 12 or n % 10 == 0:
            print(f"n={n:2d} distinct={len(c):4d} pred={1+comb(n-2,2):4d} "
                  f"empty_mult={empty_m} nonempty_mult={sorted(set(nonempty)) if nonempty else []} "
                  f"total={sum(c.values())} ok={ok}")
    print("\nALL OK" if all_ok else "SOME FAILED")


if __name__ == "__main__":
    main()
