#!/usr/bin/env python3
"""Measure the SUPPLY side of Granville's route (G-supply).

For sample columns n in {50,100,200,400,800,1600,3200,3999} of the prime
Gilbreath triangle, computed along Granville's right diagonal through q_n
(delta_k(q_n) = A_k[n-k]):

  (1) nu_2(q_n) : number of 2s in the maximal {0,2} suffix of the diagonal
                  (tail = maximal {0,2} suffix of delta_2..delta_{n-2}),
                  exactly reproducing granville-nu2-density-measured;
  (2) the ancestor window of halved gap bits: h[j] = (A_1[j]//2) mod 2 for
                  j = 2..n-1  ( = 1 iff gap g_{j+1} == 2 mod 4 );
  (3) w(n) = Hamming weight of that window.

Because every diagonal cell (k, n-k) with k <= n-1 and n <= 3999 touches
row-0 columns in [0, 3999], truncating the triangle to the first 4001 prime
columns gives IDENTICAL diagonal values to a full sieve to 3e6 (that earlier
run over-sieved to feed g*_n, which this measurement does not need). So we
sieve only to 50000 (~5133 primes) and the whole run is tiny.

Math behind the ancestor window: cell (k, n-k) at depth k has row-1 ancestors
at columns [n-k, n-1]. The {0,2}-tail cells run k = K..n-2, i.e. row-1 columns
[n-k, n-1] with k in [K, n-2], whose union is the whole interval [2, n-1]
(the k = n-2 cell alone reaches column 2). So the ancestor window is the fixed
interval [2, n-1] of halved gap bits regardless of where the {0,2} suffix
starts.

Exact integer arithmetic throughout. O(N log log N) sieve + O(M^2) triangle.
"""
import math
from lib.gilbreath import primes_up_to

MAX_N = 3999
SAMPLES = [50, 100, 200, 400, 800, 1600, 3200, MAX_N]

# Small bound: only need W > MAX_N primes. 50000 gives ~5133 primes.
BOUND = 50000


def main():
    P = primes_up_to(BOUND)
    W = len(P)
    print("sieve to %d : %d primes (need > %d for the widest column)"
          % (BOUND, W, MAX_N))
    assert W > MAX_N + 2, "not enough primes for the widest diagonal"

    # Read off the halved-gap bits (row 1) directly, no triangle needed.
    # h[j] = (A_1[j]//2) mod 2, j = 0.. -> corresponds to gap g_{j+1}.
    hbits = [( (P[i+1] - P[i]) // 2 ) % 2 for i in range(W - 1)]
    one_gap_mod4 = (hbits[2-2]) if len(hbits) > 0 else None  # g_2 ... sanity only

    # Build the triangle rows we need: rows[k] = A_k, truncated at width MAX_N.
    rows = [P[:MAX_N + 2]]
    for k in range(1, MAX_N):
        prev = rows[-1]
        nxt = [abs(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)]
        rows.append(nxt)

    def diag(n):
        # delta_k(q_n) = A_k[n-k], k = 0..n-1  (length n)
        return [rows[k][n - k] for k in range(n)]

    print("\n%-6s %-8s %-8s %-8s %-8s %-8s %-8s" % (
        "n", "nu2", "w", "nu2/n", "nu2/w", "2*nu2+2", "g*-hyp"))

    # reproduce g* via prefix max over gaps (not needed for the transfer ratio,
    # but reported so the Lemma 5.4 hypothesis row matches the earlier record).
    gaps = [P[i + 1] - P[i] for i in range(len(P) - 1)]
    gstar = [0] * (MAX_N + 2)
    mx = 0
    for n in range(1, MAX_N + 2):
        mx = max(mx, gaps[n - 1])
        gstar[n] = mx

    min_ratio = 1e9
    results = []
    for n in SAMPLES:
        d = diag(n)
        tail = d[2:-1]                 # maximal {0,2} suffix candidate window
        i = len(tail)
        while i > 0 and tail[i - 1] in (0, 2):
            i -= 1
        cyc = tail[i:]
        nu2 = cyc.count(2)
        # ancestor window: halved gap bits h[j], j = 2..n-1
        w = sum(hbits[2:n])            # sum over j in [2, n-1]
        r_n = nu2 / n
        r_w = nu2 / w if w else float('inf')
        min_ratio = min(min_ratio, r_n)
        g = gstar[n]
        ok = g <= 2 * nu2 + 2
        results.append((n, nu2, w, r_n, r_w, g, ok))
        print("%-6d %-8d %-8d %-8.3f %-8.3f %-8d %s" % (
            n, nu2, w, r_n, r_w, 2 * nu2 + 2, ok))

    print("\nmin nu2/n seen = %.4f" % min_ratio)
    print("nu2/n range   = [%.3f, %.3f]" % (
        min(r[3] for r in results), max(r[3] for r in results)))
    print("nu2/w range   = [%.3f, %.3f]" % (
        min(r[4] for r in results), max(r[4] for r in results)))
    print("smallest nu2/w = %.3f (transfer nu2>=w/c with c=1.. this value)" % (
        min(r[4] for r in results)))

    # The transfer question: is a clean lower bound nu2 >= w/c (small c)
    # plausible? nu2/w ~ 1 means nu2 and the mod-4-gap density track each
    # other tightly, so c near 1 suffices at the sampled scales.
    vals = [r[4] for r in results]
    print("\nTransfer assessment: nu2/w min=%.3f max=%.3f mean=%.3f over %d "
          "samples." % (min(vals), max(vals), sum(vals)/len(vals), len(vals)))
    if min(vals) >= 0.5:
        print("  nu2 >= w/2 holds on every sample (c=2).")
    if min(vals) >= 1.0:
        print("  nu2 >= w holds on every sample (c=1).")


if __name__ == "__main__":
    main()
