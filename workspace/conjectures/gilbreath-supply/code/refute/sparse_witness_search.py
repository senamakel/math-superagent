#!/usr/bin/env python3
"""Attack G-weak-input-strictness: is there a FIXED binary string h with
switch density 0 (1-count = o(n)) whose fold weight nu2(n) = wt(Phi_n h)
satisfies liminf nu2(n)/n > 0?

The run's own data shows powers-of-2 and squares both fail (liminf -> 0 due to
the boundary drop at exact powers of 2). The witness, if it exists, must be
sparse-but-growing and must avoid the boundary drop.

Here we search a WIDE family of fixed density-0 support sets S (the same S for
every n; h[j]=1 iff j in S) and compute, over a large n-range, the empirical
lower envelope of nu2(n)/n. Any set keeping a positive lower envelope on ALL
large n supports G-weak-input-strictness; if every candidate's envelope decays
to 0, that is evidence no fixed sparse string works.

Exact oracle: lib.supply_fold.s_sos (O(n log n)) cross-checked vs literal.

This is a MEASUREMENT/search, not a proof of any infinite statement. The
deliverable is which families keep a positive envelope and where each dies.
"""
import os, sys
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos

def nu2(n, h):
    S, ones = s_sos(n, h)
    return ones

def indicator(n, S):
    h = [0]*n
    for j in S:
        if 0 <= j < n:
            h[j] = 1
    return h

def envelope(family_fn, n_lo, n_max, name):
    """Min ratio over the whole range and over the top half (tail), and the
    overall minimum with its n. family_fn(n) builds the length-n string."""
    lows = []
    tailmin = 10.0
    arg = None
    for n in range(n_lo, n_max+1):
        h = family_fn(n)
        r = nu2(n, h)/n
        if r < tailmin:
            tailmin = r
            arg = (n, r)
        lows.append(r)
    whole_min = min(lows)
    tail_lo = len(lows)//2
    tail_min = min(lows[tail_lo:])
    print(f"{name:38s} n[{n_lo},{n_max}] whole_min={whole_min:.4f} "
          f"tail_min={tail_min:.4f}  argmin_tail={arg}")
    return whole_min, tail_min, arg

# ---- families of fixed sparse support ----
def fam_powers2(n):
    return indicator(n, [1<<k for k in range(64)])

def fam_squares(n):
    return indicator(n, [k*k for k in range(1, 2000)])

def fam_pow2_minus1(n):
    return indicator(n, [(1<<k)-1 for k in range(1, 64)])

def fam_pow2_plus1(n):
    return indicator(n, [(1<<k)+1 for k in range(1, 64)])

def fam_primes(n):
    # 1s at prime indices -- density ~ 1/log n -> 0
    import sympy
    return indicator(n, list(sympy.ntheory.generate.primerange(0, n+100)))

def fam_squares_and_shift(n):
    # squares and squares+1 : denser but still density 0
    S = set(k*k for k in range(1, 2000))
    S |= set(k*k+1 for k in range(1, 2000) if k*k+1 < 4_000_000)
    return indicator(n, S)

def fam_cubes(n):
    return indicator(n, [k**3 for k in range(1, 100)])

def fam_fib(n):
    a,b=[],[]
    x,y=1,1
    while x < 4000000:
        a.append(x); b= (x, x+y)
    return indicator(n, a)

def fam_luccus(n):
    # Luc(k) = 2^k (already powers2); try values near 2^k + one "buffer" bit
    S = set()
    for k in range(1, 40):
        S.add(1<<k)
        S.add((1<<k)+ (1<<(k//2)))
    return indicator(n, S)

def main():
    print("=== fixed sparse supports: lower envelope of nu2(n)/n ===\n")
    everyone = []
    R = 512
    tests = [
        ("powers2", fam_powers2),
        ("squares", fam_squares),
        ("pow2-1", fam_pow2_minus1),
        ("pow2+1", fam_pow2_plus1),
        ("prime indices", fam_primes),
        ("squares & +1", fam_squares_and_shift),
        ("luc(k)=2^k+2^{k/2}", fam_luccus),
    ]
    for name, fn in tests:
        r = envelope(fn, 256, 4096, name)
        everyone.append((name, r))
    print("\nNOTE: tail_min is min over top half of the n-range, a proxy for the")
    print("large-n liminf. Only a family with tail_min bounded away from 0 over")
    print("an increasing range would be a G-weak-input-strictness witness.")

if __name__ == "__main__":
    main()
