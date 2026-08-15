#!/usr/bin/env python3
"""Independent re-derivation of the G-supply transfer bridge.

NOTE (scholar): authored but NOT executed here — this scholar role has no
shell tool in this run. The two-route verification it was meant to provide
ALREADY exists on disk from two distinct programs:
  - code/out/nu2_vs_gap_parity.captured.txt   (nu2/w in [0.689,0.867], w/n~0.60)
  - code/out/nu2_dense_transfer.captured.txt  (nu2/w in [0.827,0.864] to N=30000)
Both recompute the same right-diagonal nu2 and the halved-gap-bit Hamming
weight w independently; they agree, so the transfer constant is two-routed as
recorded. This file is offered as a third route for a coder to run if the
existing pair is ever in doubt; it must not be reported as a check until run.
"""
from lib.gilbreath import primes_up_to

MAX_N = 4000
BOUND = 100000  # ~9592 primes, enough for columns to n=4000+2

P = primes_up_to(BOUND)
assert len(P) > MAX_N + 2

rows = [P[: MAX_N + 3]]
for k in range(1, MAX_N):
    prev = rows[-1]
    rows.append([abs(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)])

# halved gap bits: h[j] = 1 iff gap_{j+1} == 2 (mod 4), window j = 2..n-1
hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]

samples = [50, 100, 200, 400, 800, 1600, 3200, MAX_N]
print("%-6s %-8s %-8s %-8s %-8s" % ("n", "nu2", "w", "nu2/n", "nu2/w"))
for n in samples:
    diag = [rows[k][n - k] for k in range(n)]
    tail = diag[2:-1]
    i = len(tail)
    while i > 0 and tail[i - 1] in (0, 2):
        i -= 1
    cyc = tail[i:]
    nu2 = cyc.count(2)
    w = sum(hbits[2:n])
    print("%-6d %-8d %-8d %-8.3f %-8.3f" % (n, nu2, w, nu2 / n, nu2 / w))

w_full = sum(hbits[2:MAX_N])
print("\nw(4000) = %d , w/n = %.4f  (gaps==2 mod 4 density)" %
      (w_full, w_full / (MAX_N - 2)))
