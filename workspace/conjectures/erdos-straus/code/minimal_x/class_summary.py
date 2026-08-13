"""Per-class summary for the pattern report: smallest prime with excess >= 2,
max excess, distribution of e, and the d=3/d=7 criterion agreement per class.
"""
import json
from sympy import isprime

rows = json.load(open('code/out/extended_minimal_x.json'))['rows']
OPEN = [1, 121, 169, 289, 361, 529]

for r in OPEN:
    arr = sorted([t for t in rows if t['r'] == r], key=lambda t: t['k'])
    primes = [t for t in arr if t['prime']]
    ge2 = [t for t in arr if t['excess'] >= 2]
    ge1 = [t for t in arr if t['excess'] >= 1]
    p_ge2 = [t for t in primes if t['excess'] >= 2]
    maxe = max(arr, key=lambda t: t['excess'])
    n0 = arr[0]['n']
    print(f"r={r:>3}: n0={n0:<6} rows={len(arr):<4} e=0:{sum(1 for t in arr if t['excess']==0):<4} "
          f"e>=1:{len(ge1):<4} e>=2:{len(ge2):<4} max e={maxe['excess']} at k={maxe['k']} (n={maxe['n']}, "
          f"prime={maxe['prime']})")
    if p_ge2:
        t = min(p_ge2, key=lambda s: s['n'])
        print(f"     smallest PRIME with e>=2: n={t['n']} (k={t['k']}) e={t['excess']}")
    else:
        print(f"     no prime with e>=2 among {len(primes)} primes (k <= 450)")
    # smallest n (any) with e>=2
    if ge2:
        t = min(ge2, key=lambda s: s['n'])
        print(f"     smallest n with e>=2: n={t['n']} (k={t['k']}) e={t['excess']} prime={t['prime']}")