"""Independent, second-route attack on the crux claim pf-s2multiset.

CLAIM under attack: the multiset { M_d △ M_{d'} }, d,d' in [2,n-1], is
   - empty set with multiplicity (n-2)      (the diagonal d = d')
   - every nonempty set with multiplicity exactly 2
i.e. the map on UNORDERED pairs {d,d'} -> M_d △ M_{d'} (d != d') is injective,
giving 1 + C(n-2,2) distinct sets.

This file deliberately does NOT import lib.collapse; it re-derives M_d from
Lucas / submask enumeration independently, so the two routes share nothing.

Checks (all against the claim's predictions):
  A. empty multiplicity == n-2
  B. all nonempty multiplicities == 2, distinct count == 1 + C(n-2,2)
  C. total == (n-2)^2
  D. (the real attack) unordered injectivity: count distinct sets directly and
     compare to 1 + C(n-2,2). If this fails the claim is dead.

Negative control: re-run the same assertions against a DELIBERATELY BROKEN
prediction (empty multiplicity n-2+1) and require they fail for >= one n.
"""
from collections import Counter
from math import comb


def submasks(d):
    o = d
    while True:
        yield o
        if o == 0:
            break
        o = (o - 1) & d


def M(d, n):
    """M_d = { n-1-d+o : o subseteq d } as frozenset of positions."""
    return frozenset(n - 1 - d + o for o in submasks(d))


def multiset(n):
    """Counter of frozenset |d,d' -> M_d △ M_{d'}| over ordered pairs."""
    Ms = {d: M(d, n) for d in range(2, n)}
    c = Counter()
    for d in range(2, n):
        for dp in range(2, n):
            c[frozenset(Ms[d] ^ Ms[dp])] += 1
    return c


def run(empty_mul_offset=0):
    """Return (all_ok_per_n, any_failed) under a possibly broken prediction."""
    any_failed = False
    per_n = {}
    for n in range(2, 26):
        c = multiset(n)
        empty_m = c.get(frozenset(), 0)
        nonempty = [m for A, m in c.items() if A != frozenset()]
        ok = (empty_m == (n - 2) + empty_mul_offset
              and all(m == 2 for m in nonempty)
              and len(c) == 1 + comb(n - 2, 2)
              and sum(c.values()) == (n - 2) ** 2)
        any_failed |= (not ok)
        per_n[n] = (ok, empty_m, sorted(set(nonempty)) if nonempty else [],
                    len(c), 1 + comb(n - 2, 2))
    return per_n, any_failed


def main():
    per_n, any_failed = run(0)
    print("== Independent attack on pf-s2multiset (n=2..25) ==")
    for n in (n for n in per_n if n <= 12 or n % 5 == 0):
        ok, e, ne, distinct, pred = per_n[n]
        mark = "OK " if ok else "FAIL"
        print(f"n={n:2d} [{mark}] empty={e} nonempty_mults={ne} "
              f"distinct={distinct} pred={pred}")
    print("ANY FAILURE (true prediction):", any_failed)

    # negative control: broken prediction must fail
    broken, bfail = run(1)   # offset makes empty multiplicity wrong
    print("negative control: broken prediction fails somewhere:", bfail)

    # attack D specifically to n=256 using big-n spot checks
    print("== big-n spot checks (n = 64,128,256) ==")
    for n in (64, 128, 256):
        c = multiset(n)
        empty_m = c.get(frozenset(), 0)
        nonempty = [m for A, m in c.items() if A != frozenset()]
        ok = (empty_m == n - 2 and all(m == 2 for m in nonempty)
              and len(c) == 1 + comb(n - 2, 2)
              and sum(c.values()) == (n - 2) ** 2)
        print(f"n={n} empty={empty_m} nonempty_uniq={sorted(set(nonempty))} "
              f"distinct={len(c)} pred={1+comb(n-2,2)} total_ok="
              f"{sum(c.values())==(n-2)**2} OK={ok}")


if __name__ == "__main__":
    main()
