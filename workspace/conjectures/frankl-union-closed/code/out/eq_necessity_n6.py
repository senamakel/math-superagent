"""Extend the EQ structural-lemma necessity check beyond n=5 by exhaustive
enumeration of SMALL union-closed families on [6] with |F| in {2,3,4}.

Lemma (crux): an empty-free UC family with f == min{N, 2k-N+1} is a singleton
or a strict two-chain.  Equivalently, no family with >= 3 sets achieves the
KPT equality.  Verified exhaustively n<=5 (all families).  Here, at n=6, we
exhaustively enumerate ALL UC families with |F| <= 4 sets (the 2-chain bound
does not touch these: the question is whether any >=3-set family is EQ) and
check the equality.

Enumerate all subsets of [6] as masks; for each size m in 2..4, all C(2^6,m)
subfamilies, test union-closure via lib.uc, compute f and the equality.
Exact integers.  A single non-singleton/twochain EQ family refutes the lemma.
"""
from itertools import combinations
from lib.uc import decide_union_closed, abundance


def popcount(x):
    return bin(x).count("1")


def main():
    n = 6
    masks = list(range(1 << n))
    nz = [x for x in masks if x != 0]
    print(f"exhaustive EQ necessity check at n={n}, small family sizes")
    print("oracle: lib.uc (decide_union_closed, abundance), exact")
    print("range : ALL empty-free UC families on [6] with |F| in 2..4")
    bad = []
    eq_count = 0
    for m in [2, 3, 4]:
        total_uc = 0
        eq_here = 0
        bad_here = 0
        for combo in combinations(nz, m):
            F = set(combo)
            if not decide_union_closed(F):
                continue
            total_uc += 1
            counts = abundance(F, n)
            f = sum(1 for c in counts if 2 * c > m)
            ks = sorted(popcount(s) for s in F)
            k = ks[0]
            N = ks[-1]
            if f == min(N, 2 * k - N + 1):
                eq_here += 1
                eq_count += 1
                # is it a 2-chain?
                if m == 2:
                    a, b = tuple(F)
                    sa, sb = popcount(a), popcount(b)
                    small, large = (a, b) if sa <= sb else (b, a)
                    is_tc = (small | large) == large and popcount(large) == popcount(small) + 1
                else:
                    is_tc = False
                if not is_tc:
                    bad_here += 1
                    if len(bad) < 10:
                        bad.append((m, sorted(F), k, N, f))
        print(f"  |F|={m}: UC families={total_uc}  eq={eq_here}  "
              f"non-single/twochain-equality={bad_here}")
    print(f"\nTOTAL EQ families (|F|=2..4, n=6): {eq_count}")
    print(f"counterexamples to lemma: {len(bad)}")
    for b in bad:
        print(f"   BAD: |F|={b[0]} k={b[2]} N={b[3]} f={b[4]} masks={sorted(b[1])}")


if __name__ == "__main__":
    main()
