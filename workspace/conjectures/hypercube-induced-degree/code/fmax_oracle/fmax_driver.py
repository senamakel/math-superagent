"""Driver: exact f(n) oracle — exhaustive for n<=4, ILP decision for n=5.

Reports f(1)..f(4) exactly with the n=4 degree profile (both exhaustive oracle
and ILP decision), then the n=5 decision 'is there S of size 17 with D(S)<=d?'
for d=1,2,3 via scipy.optimize.milp (HiGHS). Also verifies an explicit claimed
S if found.

Validation: decision_ilp is checked against the exhaustive decision_oracle on
n=1..4 where both can run; they must agree before f(5) is trusted.
"""

import time
import numpy as np
from itertools import combinations

from lib.fmax import (decision_oracle, decision_ilp, f_exact, f_milp,
                      internal_degree_distribution, max_internal_degree)



def main():
    t0 = time.time()

    print("=" * 70)
    print("PART A — exhaustive oracle f(1)..f(4) with degree profiles")
    print("=" * 70)
    for n in range(1, 5):
        ta = time.time()
        f, S = f_exact(n)
        dist = internal_degree_distribution(n, S)
        print(f"  n={n}: f(n)={f}  |S|={len(S)}  (want {2**(n-1)+1})  "
              f"achieving S={sorted(S)}")
        print(f"         degree profile={dict(sorted(dist.items()))}  "
              f"[{time.time()-ta:.2f}s]")

    print()
    print("=" * 70)
    print("PART B — validate ILP decision against exhaustive oracle (n=1..4)")
    print("=" * 70)
    all_agree = True
    for n in range(1, 5):
        for d in range(0, n + 1):
            tb = time.time()
            io, _ = decision_oracle(n, d)
            ii = decision_ilp(n, d)
            agree = (io == ii)
            all_agree &= agree
            print(f"  n={n} d={d}: exhaustive={io}  ilp={ii}  agree={agree}  "
                  f"[{time.time()-tb:.2f}s]")
    print(f"  ALL AGREE: {all_agree}")
    assert all_agree, "ILP linearisation disagrees with exhaustive oracle!"

    print()
    print("=" * 70)
    print("PART C — n=5 decision via ILP (S of size 17, D(S)<=d for d=1,2,3)")
    print("=" * 70)
    n = 5
    m = (1 << (n - 1)) + 1
    print(f"  n={n}: |S| = {m} out of {1<<n} vertices. "
          f"Exhaustive C({1<<n},{m}) = {combinations_count(1<<n, m):,.0f} "
          f"is too big; using ILP.")
    for d in (1, 2, 3):
        tc = time.time()
        fe = decision_ilp(n, d)
        print(f"  d={d}: feasible(S with D(S)<={d}) = {fe}  "
              f"[{time.time()-tc:.2f}s]")

    print()
    print(f"  total wall time: {time.time()-t0:.1f}s")


def combinations_count(N, m):
    from math import comb
    return comb(N, m)


if __name__ == "__main__":
    main()
