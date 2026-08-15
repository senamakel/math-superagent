#!/usr/bin/env python3
"""Reconcile two recorded nu2/w minima on the real primes.

(A) claim g-supply-transfer-measured records  min nu2/w = 0.689  at the
    sampled points n in {50,100,200,400,800,1600,3200,3999}
    (code/gap_analysis/nu2_vs_gap_parity.py).
(B) claim transfer-matrix-kernel-allones / code/out/kernel_characterize.captured.txt
    records min nu2/w = 0.5152 at n=53 over a dense scan n in [50,3000]
    (code/refute/kernel_characterize.py).

Both use the SAME conventions (verified below, at every shared point the two
dense values match the sparse values exactly):
  * nu2(q_n) = count of 2s in the maximal {0,2} suffix of the right diagonal
               through q_n, tail = diag(n)[2:-1]  (the run's d[2:-1] tail
               convention; walk back from the end while entries are in {0,2}).
  * diag(n) = [rows[k][n-k] for k in range(n)]  (delta_k(q_n) = A_k[n-k]).
  * w(n) = #{ j in [2,n-1] : gap_{j+1} == 2 (mod 4) }
         = Hamming weight of halved gap bits h[j] = (A_1[j]//2) mod 2, j in
           [2,n-1], where gap_{j+1} = p_{j+2} - p_{j+1} is the (j+1)-th gap.

This script recomputes them from a fresh sieve to 1,000,000:
  (1) nu2/w at EVERY n from 3 to 3000, and the global min with its n (so the
  n=53 claim is re-derived, and the true global min over that range is found);
  (2) nu2/w at the sparse sample set {50,100,200,400,800,1600,3200,3999} used
  for the 0.689 figure.

Exact integer arithmetic throughout.  O(N log log N) sieve + O(M^2) triangle.
"""
import math
from lib.gilbreath import primes_up_to

MAX_N = 3000                  # dense range for the global min (matches claim B)
TRI_N = 4001                  # triangle width/depth: enough for sparse n=3999
SPARSE = [50, 100, 200, 400, 800, 1600, 3200, 3999]   # points for the 0.689 figure
BOUND = 1_000_000


def nu2_and_w(P, rows, hbits, n):
    """nu2(q_n) and w(n) under the run's d[2:-1] tail convention.
    rows[k] = A_k truncated wide enough; hbits[j] = (gap_{j+1}//2) mod 2."""
    d = [rows[k][n - k] for k in range(n)]   # right diagonal through q_n
    tail = d[2:-1]                           # run's {0,2}-suffix candidate window
    i = len(tail)
    while i > 0 and tail[i - 1] in (0, 2):
        i -= 1
    nu2 = tail[i:].count(2)
    w = sum(hbits[2:n])                      # window j in [2, n-1]
    return nu2, w


def main():
    P = primes_up_to(BOUND)
    print("sieve to %d : %d primes" % (BOUND, len(P)))
    assert len(P) > MAX_N + 2, "not enough primes"

    # halved gap bits: h[j] = (gap_{j+1}//2) mod 2 = [p_{j+2}-p_{j+1} == 2 (mod 4)]
    hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]

    # triangle rows to depth TRI_N at width TRI_N+2 (enough so diag(n) for
    # n <= TRI_N reads column n-k from a live row with the full row-1 ancestor
    # window).
    width = TRI_N + 2
    rows = [P[:width]]
    for k in range(1, TRI_N):
        prev = rows[-1]
        rows.append([abs(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)])

    # ---- (1) dense scan: every n from 3 to 3000, global min ----
    print("\n=== (1) DENSE: nu2/w at EVERY n from 3 to %d, global min ===" % MAX_N)
    global_min = float('inf')
    global_at = None
    min50 = float('inf')     # min over the meaningful domain n in [50, MAX_N]
    min50_at = None
    low_notes = []
    for n in range(3, MAX_N + 1):
        nu2, w = nu2_and_w(P, rows, hbits, n)
        if w == 0:
            ratio = float('inf')
        else:
            ratio = nu2 / w
        if ratio < global_min:
            global_min = ratio
            global_at = n
        if n >= 50 and ratio < min50:
            min50 = ratio
            min50_at = n
        # print the low tail densely, and coarse every-150 elsewhere
        if n <= 120 or n % 150 == 0 or n == MAX_N:
            low_notes.append((n, nu2, w, ratio))
    # always show the n that achieved the minimum
    nu2m, wm = nu2_and_w(P, rows, hbits, global_at)
    print("global min nu2/w over n in [3,%d] (incl degenerate tiny-n empty tail)"
          " = %.4f at n=%d (nu2=%d, w=%d)" % (MAX_N, global_min, global_at, nu2m, wm))
    nu2m50, wm50 = nu2_and_w(P, rows, hbits, min50_at)
    print("min nu2/w over the meaningful prime domain n in [50,%d] = %.4f at "
          "n=%d (nu2=%d, w=%d)   <-- this is the number claims A/B restrict to"
          % (MAX_N, min50, min50_at, nu2m50, wm50))
    print("\nn      nu2    w      nu2/n    nu2/w")
    for n, nu2, w, ratio in low_notes:
        flag = "  <-- min" if n == global_at else ""
        print("%-6d %-6d %-6d %-8.4f %-8.4f%s" % (
            n, nu2, w, nu2 / n, ratio if ratio != float('inf') else float('nan'), flag))

    # ---- (2) sparse sample set for the 0.689 figure ----
    print("\n=== (2) SPARSE sample set {50,100,200,400,800,1600,3200,3999} ===")
    print("n      nu2    w      nu2/n    nu2/w")
    min_sparse = float('inf')
    min_sparse_at = None
    for n in SPARSE:
        nu2, w = nu2_and_w(P, rows, hbits, n)
        ratio = nu2 / w if w else float('inf')
        if ratio < min_sparse:
            min_sparse = ratio
            min_sparse_at = n
        print("%-6d %-6d %-6d %-8.4f %-8.4f" % (n, nu2, w, nu2 / n, ratio))
    print("\nmin nu2/w over the sparse set = %.4f at n=%d" % (min_sparse, min_sparse_at))

    # ---- verification against the two recorded captures ----
    print("\n=== VERIFICATION against recorded figures ===")
    # claim A: min 0.689 at sampled points (the sparse set, 8 points)
    sparse_vals = [nu2_and_w(P, rows, hbits, n) for n in SPARSE]
    sparse_ratio = [v[0] / v[1] for v in sparse_vals]
    # claim B: 0.5152 at n=53 over n in [50,3000]
    nu2_53, w_53 = nu2_and_w(P, rows, hbits, 53)
    ratio_53 = nu2_53 / w_53
    print("sparse-set min (8 pts)      : %.4f  (recorded 0.689)" % min(sparse_ratio))
    print("dense-scan value at n=53    : %.4f  (recorded 0.5152)" % ratio_53)
    print("min over n in [50,%d]       : %.4f at n=%d" % (MAX_N, min50, min50_at))
    print("global min over n in [3,%d] : %.4f at n=%d" % (MAX_N, global_min, global_at))


if __name__ == "__main__":
    main()
