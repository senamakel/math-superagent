#!/usr/bin/env python3
"""
Push the S(p) mod-6 conjecture to N = 1e7 (vectorized, as extend_sp_vec.py).

Conjecture (C): p > 7  ==>  S(p) != 0 (mod 6);  for p > 7 the residue table
is exactly (p mod 3, S(p) mod 6) = (1,2) or (2,4).
Falsifier to hunt: a prime p > 7 with S(p) = 0 (mod 6).

The OeS empirical relation p ~ 0.33 (log S log log S)^2 gives p ~ 660 at
S ~ 1e7; bound pmax = 20000 to be safe.
"""
import numpy as np
from math import isqrt
import sys, time
from collections import Counter

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
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    pmax = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    t0 = time.time()
    primes = primes_upto(N)
    P = np.array(primes, dtype=np.int64)
    print(f"N={N}, pi(N)={len(primes)}, sieve {time.time()-t0:.1f}s", file=sys.stderr)

    evens = np.arange(4, N + 1, 2, dtype=np.int64)
    assigned = np.zeros(len(evens), dtype=bool)
    minprime = np.zeros(len(evens), dtype=np.int64)
    idx_of = np.zeros(N + 1, dtype=np.int64)
    idx_of[evens] = np.arange(len(evens))

    cand = P[P <= pmax]
    print(f"candidate primes p <= {pmax}: {len(cand)}", file=sys.stderr)
    t1 = time.time()
    for p in cand:
        q = P[P >= p]
        q = q[q <= N - p]
        ns = p + q
        ix = idx_of[ns]
        m = ~assigned[ix]
        assigned[ix[m]] = True
        minprime[ix[m]] = p
    print(f"assignment done {time.time()-t1:.1f}s", file=sys.stderr)

    un = evens[~assigned]
    print(f"unassigned with p(n) > {pmax}: {len(un)}; first: {un[:10]}", file=sys.stderr)
    if len(un):
        print("WARNING: pmax bound too low for some n", file=sys.stderr)

    # S(p): first n with minprime == p, in increasing n order
    sp_p, sp_val = [], []
    seen = np.zeros(pmax + 1, dtype=bool)
    for i in range(len(evens)):
        p = int(minprime[i])
        if p > 0 and not seen[p]:
            seen[p] = True
            sp_p.append(p)
            sp_val.append(int(evens[i]))
    print(f"distinct minimal primes: {len(sp_p)} ({time.time()-t0:.1f}s)", file=sys.stderr)

    bad = [(p, s) for p, s in zip(sp_p, sp_val) if p > 7 and s % 6 == 0]
    print(f"\n=== (C) p > 7 with S(p) = 0 (mod 6): {len(bad)} ===")
    if bad:
        print(f"  FALSIFIERS: {bad[:10]}")
    else:
        print(f"  holds for all {len([p for p in sp_p if p > 7])} primes p > 7 with S(p) <= {N}")

    cres = Counter()
    for p, s in zip(sp_p, sp_val):
        if p > 3:
            cres[(p % 3, s % 6)] += 1
    print(f"=== (p mod 3, S(p) mod 6) counts: {dict(cres)} ===")

    with open(f'/workspace/code/out/seq_sp_vec_{N}.txt', 'w') as f:
        for p, s in zip(sp_p, sp_val):
            f.write(f"{p} {s}\n")
    print(f"saved seq_sp_vec_{N}.txt", file=sys.stderr)
    print(f"first_appearance_p = {sp_p}")
    print(f"first_appearance_S = {sp_val}")

if __name__ == '__main__':
    main()