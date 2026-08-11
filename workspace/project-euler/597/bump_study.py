#!/usr/bin/env python3
"""Monte Carlo study of bump-pattern structure for small n at L=160.

For n=2 and n=3, draws many Exp(1) speed samples, records for each:
  - parity (0 even / 1 odd)
  - the exact multiset of bump events (which boat bumped which) in order
  - which boats finished
  - the number of pairs (i<j) joined by a bump chain i->...->j
Verifies the identity
      parity == (num_chains) mod 2
on every sample, reports MC probabilities with standard errors, and prints a
histogram of how often each bump-pattern type appears, split by parity.

Usage: python3 bump_study.py [N]
"""
import random, sys, math
from collections import Counter
from brute import outcome_parity
from toolkits.race_events import race_events


def mc_study(n, L, N, seed=7):
    rng = random.Random(seed)
    even = 0
    pattern_counter = Counter()      # pattern -> (even_count, total)
    ident_ok = True
    mismatches = 0
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        ev = race_events(n, L, speeds)
        par = ev['parity']
        if par == 0:
            even += 1
        # pattern signature: sorted bump edges + who finished
        bumpstr = ",".join(f"{a}>{b}" for (a, b) in sorted(ev['bumps'])) or "none"
        finstr = ",".join(str(f) for f in sorted(ev['finishes'])) or "none"
        sig = f"bumps={bumpstr};fin={finstr}"
        c = pattern_counter.get(sig, (0, 0))
        pattern_counter[sig] = (c[0] + (1 if par == 0 else 0), c[1] + 1)
        # identity check
        if par != (ev['num_chains'] % 2):
            ident_ok = False
            mismatches += 1
    p = even / N
    se = math.sqrt(p * (1 - p) / N)
    return p, se, pattern_counter, ident_ok, mismatches


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
    for (n, L) in [(2, 160), (3, 160)]:
        p, se, hist, ident_ok, mism = mc_study(n, L, N)
        print(f"n={n} L={L}  N={N}")
        print(f"  MC P(even) = {p:.6f}  +/- {se:.6f}")
        known = {3: 56/135}.get(n)
        if known:
            print(f"   exact     = {known:.6f}  (statement n=3,L=160)")
        print(f"  parity == (#chain pairs) mod 2 holds on all samples: {ident_ok}"
              f" (mismatches={mism})")
        print("  bump-pattern histogram (pattern: even_count/total, P(even|pattern)):")
        for sig in sorted(hist):
            e, t = hist[sig]
            print(f"    {sig:40s} {e:5d}/{t:<6d}  P(even)={e/t:.4f}")
        print()
