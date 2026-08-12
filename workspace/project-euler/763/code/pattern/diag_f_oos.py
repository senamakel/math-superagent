"""Out-of-sample test of the diagonal f-distribution conjecture.

Conjecture: among 3D PE763 configs after N divisions with max level M==N
(the 'diagonal' configs), the distribution of f (number of dividable cells)
is exactly  3 * C(N-2, f-3) * 2^(f-3)  for f=3..N.

We compute this fresh at N=13 and N=14 (never used to form the conjecture)
using the memory-compact bitmask BFS, decoding each config transiently.
Total on diagonal must equal 3^(N-1).
"""
import sys, time
from collections import Counter, defaultdict
from lib.amoeba import next_level_bits, decode_bits, lvl, f_of

def main(Nmax):
    W = Nmax + 1
    level = {1}
    t0 = time.time()
    for n in range(1, Nmax + 1):
        level = next_level_bits(level, W)
        print(f"n={n} D={len(level)} {time.time()-t0:.1f}s", flush=True)
        if n >= Nmax - 1:
            # compute diagonal (M==n) f-distribution
            diag = Counter()
            for S in level:
                cells = decode_bits(S, W)
                M = max(lvl(p) for p in cells)
                if M == n:
                    diag[f_of(cells)] += 1
            tot = sum(diag.values())
            print(f"  N={n} diagonal f-distribution: {dict(sorted(diag.items()))}")
            print(f"  total on diagonal={tot}  3^(N-1)={3**(n-1)}  match={tot==3**(n-1)}")
            # conjecture check
            import math
            ok = True
            for fv, cnt in diag.items():
                pred = 3 * math.comb(n-2, fv-3) * (2**(fv-3))
                if pred != cnt:
                    ok = False
                    print(f"    FAIL f={fv}: data={cnt} pred={pred}")
            print(f"  conjecture 3*C(N-2,f-3)*2^(f-3) holds at N={n}: {ok}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 14)
