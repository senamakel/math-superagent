"""Cross-check 1: the |F|=2^k distribution of half-density UC families on [n]
against the partial-set-partition counts sum_m C(n,m)*S(m,k) (set partitions of
a subset of [n] into exactly k blocks).  If the bijection (half-density family
<-> nonempty partial set partition, block -> join-irreducible atom) holds, the
two distributions coincide exactly.

Cross-check 2: the n<=3 half-density counts against the DIRECT brute-force
oracle path lib.uc (independent of the cascade), as top_half_direct.py did for
n<=4 -- re-run here to have the outputs in one file.

Exact integer arithmetic throughout.
"""
from fractions import Fraction
from itertools import combinations
from lib.uc import decide_union_closed, abundance

# Stirling numbers of the second kind S(m, k)
def stirling2(m, k):
    if k == 0:
        return 1 if m == 0 else 0
    if k > m:
        return 0
    from math import comb
    return sum((-1) ** (k - j) * comb(k, j) * j ** m for j in range(k + 1)) // _fact(k)

def _fact(k):
    r = 1
    for i in range(2, k + 1):
        r *= i
    return r

def partial_partition_distr(n):
    """{k: number of partial set partitions of [n] into exactly k blocks}"""
    distr = {}
    for k in range(1, n + 1):
        total = 0
        for m in range(k, n + 1):
            from math import comb
            total += comb(n, m) * stirling2(m, k)
        distr[k] = total
    return distr

# observed distributions from half_density_verify.py: |F| (a power of 2) -> count
observed = {
    1: {2: 1},
    2: {2: 3, 4: 1},
    3: {2: 7, 4: 6, 8: 1},
    4: {2: 15, 4: 25, 8: 10, 16: 1},
    5: {2: 31, 4: 90, 8: 65, 16: 15, 32: 1},
}

print("Cross-check 1: observed |F| distribution vs partial-set-partition counts")
ok = True
for n in range(1, 6):
    pred = partial_partition_distr(n)
    # observed maps |F|=2^k -> count; convert to k -> count (|F|=2^k, k>=1)
    obs_by_k = {}
    for size, cnt in observed[n].items():
        k = size.bit_length() - 1
        obs_by_k[k] = cnt
    match = obs_by_k == pred
    ok &= match
    print(f"  n={n}: observed(k->cnt)={sorted(obs_by_k.items())}")
    print(f"         predicted   (k->cnt)={sorted(pred.items())}  match={match}")
print("ALL n=1..5 distributions match partial-set-partition counts:", ok)
print()

print("Cross-check 2: direct brute-force oracle counts of half-density families")
for n in range(1, 5):
    all_masks = list(range(1 << n))
    cnt = 0
    for sub in range(1 << len(all_masks)):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if not decide_union_closed(fam):
            continue
        counts = abundance(fam, n)
        m = len(fam)
        present = [c for c in counts if c > 0]
        if present and Fraction(max(present), m) == Fraction(1, 2):
            cnt += 1
    bell = [1, 1, 2, 5, 15, 52]
    print(f"  n={n}: direct count={cnt}, Bell(n+1)-1={bell[n+1]-1}, match={cnt == bell[n+1]-1}")