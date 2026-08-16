#!/usr/bin/env python3
"""Per-scale second-moment split of S(n) = sum_d (-1)^{T(n,d)}.

g(d) = nu2(d+1) = number of trailing 1-bits of d (the scale). Group depths by g,
compute S_g(n) = sum over d with that g of (-1)^{T(n,d)}, and from the per-depth
term list the variance share E[S_g^2]/(n-2). Uses exact SOS term list.
"""
import sys
from lib.primes import mod4_string
from lib.supply_fold import h_from_r, s_terms_sos

def nu2_plus(x):  # number of trailing 1 bits = position of lowest 0 bit
    g = 0
    while x & 1:
        g += 1
        x >>= 1
    return g

def per_scale(n, r):
    h = h_from_r(r[:n+2])
    terms = s_terms_sos(n, h)   # index i -> d = i+2
    Sg = {}
    for i, t in enumerate(terms):
        d = i + 2
        g = nu2_plus(d)
        Sg[g] = Sg.get(g, 0) + t
    total = sum(terms)
    total_sq = sum(u*u for u in terms)          # = sum_d 1 = n-2 (each term +-1)
    share = {g: Sg[g]*Sg[g]/(n-2) for g in Sg}
    return Sg, total, share

from lib.primes import mod4_string
r = mod4_string(40000)     # residues of primes mod 4 through q_{40001}
for n in [400,1000,4000]:
    Sg, total, share = per_scale(n, r)
    gs = sorted(Sg)
    print(f"n={n}: S(n)={total}  n-2={n-2}")
    # variance share per scale
    totshare = sum(share.values())
    # cumulative
    cum = 0
    print(f"  per-scale variance share E[S_g^2]/(n-2):")
    for g in gs:
        cum += share[g]
        flag = ' <== cum<=1/2' if abs(cum-0.5)<0.05 and g==max(gs[:1]) else ''
        print(f"    g={g}: S_g={Sg[g]:3d}  share={share[g]:.3f}  cum={cum:.3f}")
    print(f"    total share = {totshare:.3f} (should be ~1)")
