"""Extend the f-distribution column analysis to fresh N=13,14 (OOS).

The diagonal (M=N) f-distribution = 3*C(N-2,f-3)*2^(f-3) is already verified
OOS.  Now compute the SAME per-column f-distributions at N=13,14 for the
sub-diagonal offsets k=1,2,3 (M=N-1,N-2,N-3) via bitmask BFS, to check whether
those columns also have closed-form f-distributions.

We want data to test conjectures like:
  column k=1 (M=N-1), f-distribution: ?
Look at the k=1 pattern from structure_probe:
  N=4:  {3:3}
  N=5:  {4:12, 5:6}
  N=6:  {4:12, 5:42, 6:24, 7:3}
  N=7:  {4:12, 5:78, 6:144, 7:78, 8:12}
  ...
Guess: column k=1 counts are multiples of 6 (all even).  total column = 3*(N-3)*3^(N-3) [since Q_1=(N-3), total = (N-3)*3^(N-3)].

We'll just dump fresh N=13,14 per-column f-distributions from a full bitmask
BFS and compare with the (N<=12) pattern.
"""
import sys, time
from collections import Counter, defaultdict
from lib.amoeba import next_level_bits, decode_bits, lvl, f_of

def main(N):
    W = N + 1
    level = {1}
    t0 = time.time()
    cols = defaultdict(Counter)  # (N,k)-> f-dist
    for n in range(1, N + 1):
        level = next_level_bits(level, W)
        print(f"n={n} D={len(level)} {time.time()-t0:.1f}s", flush=True)
        if n >= N - 1:
            col_f = defaultdict(Counter)
            for S in level:
                cells = decode_bits(S, W)
                M = max(lvl(p) for p in cells)
                k = n - M
                col_f[k][f_of(cells)] += 1
            for k in sorted(col_f):
                d = dict(sorted(col_f[k].items()))
                print(f"  N={n} k={k} M={n-k} tot={sum(col_f[k].values())}: {d}")
    print("\ncomplete")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 14)
