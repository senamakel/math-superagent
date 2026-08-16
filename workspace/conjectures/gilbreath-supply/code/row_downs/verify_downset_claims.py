"""Exact integer verification of three claims about bitwise-submask down-sets.

   downset(d)   = { o in [0,d] : o is a bitwise submask of d }
   runs_of(S)   = lengths of maximal blocks of consecutive integers in S
"""
import sys
from itertools import product


def downset(d):
    return {o for o in range(d + 1) if (o & ~d) == 0}


def runs_of(S):
    """Maximal run lengths of the integer set S, in ascending order."""
    if not S:
        return []
    lst = sorted(S)
    runs = []
    start = prev = lst[0]
    for x in lst[1:]:
        if x == prev + 1:
            prev = x
        else:
            runs.append(prev - start + 1)
            start = prev = x
    runs.append(prev - start + 1)
    return runs


def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0


def part1(lo=0, hi=127):
    """All run lengths occurring in downset(d)^downset(d'), d,d' in [lo,hi].
       Identify any non-power-of-2 lengths and their witness pairs."""
    all_lengths = set()
    non_pow2 = {}          # length -> list of (d,d') witnesses
    for d, dp in product(range(lo, hi + 1), repeat=2):
        rr = runs_of(downset(d) ^ downset(dp))
        for L in rr:
            all_lengths.add(L)
            if not is_power_of_two(L):
                non_pow2.setdefault(L, []).append((d, dp))
    print("=== PART (1) ===")
    print(f"range d,d' in [{lo},{hi}]  pairs = {(hi-lo+1)**2}")
    print(f"distinct run lengths that occur: {sorted(all_lengths)}")
    pow2 = [L for L in sorted(all_lengths) if is_power_of_two(L)]
    nop2 = [L for L in sorted(all_lengths) if not is_power_of_two(L)]
    print(f"power-of-2 lengths:   {pow2}")
    print(f"NON-power-of-2 lengths: {nop2}")
    for L in sorted(nop2):
        w = non_pow2[L]
        print(f"  length {L}: {len(w)} witness pairs, e.g. {w[:5]}")
    return all_lengths


def part2(lo=0, hi=127):
    """Check downset(d)^downset(d') subseteq {o : d&d' subseteq o subseteq d|d'}."""
    fails = 0
    total = 0
    first_fail = None
    for d, dp in product(range(lo, hi + 1), repeat=2):
        total += 1
        A, B = d & dp, d | dp           # bitmask "d&d'", "d|d'"
        symdiff = downset(d) ^ downset(dp)
        # lower bound: A subseteq o  <=>  (o & A) == A
        # upper bound: o subseteq B   <=>  (o & ~B) == 0   <=>  (o | B) == B
        bad = [o for o in symdiff if not ((o & A) == A and (o | B) == B)]
        if bad:
            fails += 1
            if first_fail is None:
                first_fail = (d, dp, A, B, sorted(bad)[:8])
    print("\n=== PART (2) ===")
    print(f"pairs checked: {total}, pass: {total - fails}, fail: {fails}")
    print(f"first failure (d,d',d&d',d|d', offending o in delta): {first_fail}")
    return fails, total


def part3(ns=(64, 128, 256)):
    """Sum, over ordered pairs (d,d') in [2,n-1]^2, of the number of
       maximal runs of length exactly L in downset(d)^downset(d')."""
    results = {}
    for n in ns:
        count = {L: 0 for L in (1, 2, 4, 8)}
        for d, dp in product(range(2, n), repeat=2):
            rr = runs_of(downset(d) ^ downset(dp))
            for L in rr:
                if L in count:
                    count[L] += 1
        results[n] = count
        print(f"\n=== PART (3) n={n} (ordered pairs [2,{n-1}]^2 = {(n-2)**2}) ===")
        for L in (1, 2, 4, 8):
            print(f"  total runs of length {L}: {count[L]}")
    # scaling ratios for singletons
    print("\n--- singleton scaling ---")
    base = None
    for n in ns:
        c = results[n][1]
        ratio_n2 = c / (n * n)
        ratio_nlogn = c / (n * (n and __import__('math').log(n)))
        print(f"n={n}: singletons={c:>12}  c/n^2={ratio_n2:.6f}  c/nlogn={ratio_nlogn:.6f}")
        if base is not None:
            prevn = previous_n
            print(f"   growth{prevn}->{n}: factor={c / base:.4f}  (n ratio={n/prevn:.4f}, n^2 ratio={(n/prevn)**2:.4f})")
        previous_n = n
        base = c
    return results


if __name__ == "__main__":
    part1()
    part2()
    part3(ns=(64, 128, 256))
