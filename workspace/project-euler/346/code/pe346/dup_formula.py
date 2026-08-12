"""Test the structural claim: the only duplicated repunits (values that are
repunits of length>=3 in >=2 distinct bases) are 31 and 8191.

Conjecture (Goormaghtigh): those are the ONLY two, ever. If so:
  strong_sum(N) = 1 + pair_sum(N) - sum(v in DUP where v<N)
with DUP = {31, 8191}.

This checks the formula at many N, and reports which values are duplicated.
"""
def pair_sum_and_dups(N):
    """Sum over all (b,k>=3) pairs of (b^k-1)/(b-1) < N; also count multi-dups."""
    from collections import Counter
    cnt = Counter()
    b = 2
    while b*b + b + 1 < N:
        pw = b*b*b
        while True:
            v = (pw - 1)//(b - 1)
            if v >= N:
                break
            cnt[v] += 1
            pw *= b
        b += 1
    ps = sum(v*c for v, c in cnt.items())
    dups = {v: c for v, c in cnt.items() if c >= 2}
    return ps, dups

def strong_sum(N):
    """Direct enumeration of distinct strong repunits (reference)."""
    s = set()
    if N >= 1:
        s.add(1)
    b = 2
    while b*b + b + 1 < N:
        pw = b*b*b
        while True:
            v = (pw - 1)//(b - 1)
            if v >= N:
                break
            s.add(v)
            pw *= b
        b += 1
    return sum(s)

print(f"{'N':>14} {'pair_sum':>16} {'strong_sum':>16} {'duplicates_>1base'}")
for p in range(1, 13):
    N = 10**p
    if N < 8:
        continue
    ps, dups = pair_sum_and_dups(N)
    ss = strong_sum(N)
    # formula: strong_sum = 1 + pair_sum - sum(dup values < N)
    pred = 1 + ps - sum(v for v in dups)
    ok = (pred == ss)
    print(f"{N:>14} {ps:>16} {ss:>16} {sorted(dups.items())}  formula_ok={ok}")
