#!/usr/bin/env python3
"""
Vectorized (numpy) computation of S(p) = least even n whose minimal Goldbach
partition has least prime p, up to N = 2e6.  Attack the conjecture:

  (C) p > 7  ==>  S(p) != 0 (mod 6),
i.e. the only minimal primes with S(p) = 0 (mod 6) are p in {5, 7} (plus 3).

Exact theorem being cross-checked (forced by the mod-3 congruence):
  p > 3, p = 1 (mod 3)  ==>  S(p) = 0 or 2 (mod 6)
  p > 3, p = 2 (mod 3)  ==>  S(p) = 0 or 4 (mod 6)

Method: process primes p in increasing order; for each, mark all still
unassigned even n = p + q (q >= p prime) as having minimal prime p.
Correct by construction: n is unassigned when we reach p iff no smaller
prime p' has p' + q' = n.
"""
import numpy as np
from math import isqrt
import sys, time

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * ((n - i*i)//i + 1)
    return [i for i, v in enumerate(sieve) if v]

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    pmax = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    t0 = time.time()
    primes = primes_upto(N)
    P = np.array(primes, dtype=np.int64)
    Pset = set(primes)
    print(f"N={N}, pi(N)={len(primes)}, sieve {time.time()-t0:.1f}s", file=sys.stderr)

    # even n in [4, N]
    evens = np.arange(4, N + 1, 2, dtype=np.int64)
    assigned = np.zeros(len(evens), dtype=bool)
    minprime = np.zeros(len(evens), dtype=np.int64)
    idx_of = np.zeros(N + 1, dtype=np.int64)  # n -> index in evens (for even n)
    idx_of[evens] = np.arange(len(evens))

    cand = P[P <= pmax]
    print(f"candidate minimal primes: {len(cand)} (p <= {pmax})", file=sys.stderr)
    for p in cand:
        # q >= p, q prime, p + q <= N, p+q even (automatic: p odd, q odd -> even)
        q = P[P >= p]
        q = q[q <= N - p]
        ns = p + q
        ix = idx_of[ns]
        m = ~assigned[ix]
        assigned[ix[m]] = True
        minprime[ix[m]] = p

    un = evens[~assigned]
    print(f"unassigned (p(n) > {pmax}): {len(un)}; first: {un[:10]}", file=sys.stderr)
    # only even n with n <= N and n - p prime for p <= pmax are assigned;
    # for n to be a counterexample to Goldbach it needs NO partition at all.

    # S(p) map
    sp_p = []
    sp_val = []
    seen = np.zeros(int(pmax) + 1, dtype=bool)
    for i in range(len(evens)):
        p = int(minprime[i])
        if p > 0 and not seen[p]:
            seen[p] = True
            sp_p.append(p)
            sp_val.append(int(evens[i]))
    print(f"distinct minimal primes found: {len(sp_p)} ({time.time()-t0:.1f}s)", file=sys.stderr)

    # --- Test C: S(p) mod 6 for p > 7 ---
    bad = [(p, s) for p, s in zip(sp_p, sp_val) if p > 7 and s % 6 == 0]
    print(f"\n=== (C) p > 7 with S(p) = 0 (mod 6): {len(bad)} ===")
    if bad:
        print(f"  violations: {bad[:10]}")
    else:
        print(f"  holds for all {len([p for p in sp_p if p > 7])} primes p > 7 with S(p) <= {N}")

    # --- Exact theorem check ---
    badth = []
    for p, s in zip(sp_p, sp_val):
        if p > 3:
            if p % 3 == 1 and s % 6 == 4:
                badth.append((p, s))
            if p % 3 == 2 and s % 6 == 2:
                badth.append((p, s))
    print(f"=== exact mod-3 congruence violations: {len(badth)} ===")

    # --- residues of S(p) for p>3, count by class ---
    from collections import Counter
    cres = Counter()
    for p, s in zip(sp_p, sp_val):
        if p > 3:
            cres[(p % 3, s % 6)] += 1
    print(f"=== (p mod 3, S(p) mod 6) counts: {dict(cres)} ===")

    # --- OeS S_min/S_max bounds ---
    import math
    bmin = bmax = 0
    for p, s in zip(sp_p, sp_val):
        p4 = p ** 0.4
        if s < 0.06 * p4 * math.exp(p4):
            bmin += 1
        if s > 11.05 * p4 * math.exp(p4):
            bmax += 1
    print(f"=== OeS bounds violations: S_min {bmin}, S_max {bmax} of {len(sp_p)} ===")

    # --- save ---
    with open(f'/workspace/code/out/seq_sp_vec_{N}.txt', 'w') as f:
        for p, s in zip(sp_p, sp_val):
            f.write(f"{p} {s}\n")
    # first-appearance order = the order above by construction
    print(f"saved seq_sp_vec_{N}.txt", file=sys.stderr)
    print(f"\nfirst_appearance_p = {sp_p}")
    print(f"first_appearance_S = {sp_val}")

if __name__ == '__main__':
    main()