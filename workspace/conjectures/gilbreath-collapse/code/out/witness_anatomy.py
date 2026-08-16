"""Anatomy of the boundary witnesses: what C_K sees and what it misses.

The clean witnesses at odd n (n=2m+1, K=m):  h = 2^m, h' = 2^(2m)+1.
  * h has bit m set (position m), h' has bit 2m set AND bit 0 set.
  * They share C_m: every ordered pair count at lags 1..m.
  * Yet S^2 differs (e.g. n=9: 1 vs 25; n=17: 1 vs 169).

Why can C_m not see the difference?  Build C_m for each h by hand:
  * h = 2^m: a single 1 at position m.  Lags 1..m pair (m, m+k) -- the pair
    (1,0) is off the end for k>=1 ... etc.
  * h' = 2^(2m)+1: 1s at positions 2m and 0.  Their distance is 2m > K = m,
    so at every lag 1..m at most one of the two 1s is inside a counted pair.

Under the prefix-XOR/runs view: h and h' have ONE 1 each in different places,
so their runs differ totally, yet C_K is identical.  The Walsh character for
the far pair {position m, position 2m} ... (see note below).

This program prints C_K for the canonical odd-n witness and for its mirror
(complement), checks C_K equality by an independent slow path, and prints S^2.
"""
from lib.collapse import S2

def C_K_slow(hbits, K):
    n = len(hbits)
    out = []
    for k in range(1, K+1):
        for a in (0,1):
            for b in (0,1):
                out.append(sum(1 for i in range(0, n-k)
                               if hbits[i]==a and hbits[i+k]==b))
    return out

pairs = [(a,b) for k in X for a in (0,1) for b in (0,1)]  # placeholder, filled below

def pretty_CK(hbits, K):
    n = len(hbits)
    lines = []
    for k in range(1, K+1):
        row = []
        for a in (0,1):
            for b in (0,1):
                c = sum(1 for i in range(0, n-k) if hbits[i]==a and hbits[i+k]==b)
                row.append(f"N_{a}{b}({k})={c}")
        lines.append("  ".join(row))
    return "\n".join(lines)

def bits(h, n):
    return [(h >> i) & 1 for i in range(n)]

for m in (3, 4, 5):
    n = 2*m + 1
    K = m
    h, hp = 1 << (2*m), 1  # h' = 2^(2m) + 1
    # proper: hp = (1 << (2*m)) | 1
    hp = (1 << (2*m)) + 1
    hb, hpb = bits(h, n), bits(hp, n)
    print(f"n={n} (m={m})  K={K}")
    print(f"  h  = {h:>9}  bits at {[i for i in range(n) if hb[i]]}")
    print(f"  h' = {hp:>9}  bits at {[i for i in range(n) if hpb[i]]}")
    assert C_K_slow(hb, K) == C_K_slow(hpb, K)
    print(f"  C_K equal (slow recompute): YES")
    sh, shp = S2(n, hb), S2(n, hpb)
    print(f"  S2(h)={sh:>3}   S2(h')={shp:>3}   differ: {sh != shp}")
    print(f"  S(h)={ (n-2) - 2*sum(1 for d in range(2,n) if __import__('lib.collapse', fromlist=['T']).T(n,d,hb)) :>3}  "
          f"S(h')={ (n-2) - 2*sum(1 for d in range(2,n) if __import__('lib.collapse', fromlist=['T']).T(n,d,hpb)) :>3}")
    print()