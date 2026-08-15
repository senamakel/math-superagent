#!/usr/bin/env python3
"""Quantify the second-entry run-length departure vs iid Bernoulli.

Observed overrepresentation of mid-length runs, underrepresentation of long
runs. Test whether this is real structure or sampling noise using a chi-square
goodness-of-fit of the observed run-length histogram vs the iid-geometric
expected histogram, on BOTH the depth-1000 and fresh depth-600 data.
Exact arithmetic (fractions) for expected counts; chi-square in float.
"""
from fractions import Fraction
import math
from lib.gilbreath import primes_up_to

def s_bits(primes, depth):
    row = primes[:]
    bits = []
    for k in range(1, depth+1):
        nxt = [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
        bits.append(nxt[1]//2)
        row = nxt
    return bits

def runs(bits_range, value):
    out = []
    cur = bits_range[0]; L = 1
    for x in bits_range[1:]:
        if x == cur: L += 1
        else:
            if cur == value: out.append(L)
            cur = x; L = 1
    if cur == value: out.append(L)
    return out

def chi2_geom(lenlist, n, p_v):
    """Chi-square of observed run lengths vs iid-geometric null.
    P(run of value v has length exactly m) = p_other * p_v^{m-1} (near boundary ignored).
    Group tail m>=8 into one cell."""
    R = len(lenlist)
    p_other = 1 - p_v
    bins = [0]*8  # lengths 1..7, and 8+ in last bin
    for r in lenlist:
        if r <= 7: bins[r-1] += 1
        else: bins[7] += 1
    exp = []
    for m in range(1, 8):
        # expected runs of exactly length m. Using boundary-corrected approx: 
        # P(exact m) = p_other*p_v^{m-1}, but the LAST run may be truncated; near-boundary.
        exp.append(R * float(Fraction(p_other) * Fraction(p_v)**(m-1)))
    # tail m>=8
    exp.append(R * float(Fraction(p_v)**7))  # prob length >=8 approx p_v^7
    chi = 0.0
    for o, e in zip(bins, exp):
        if e > 0:
            chi += (o-e)**2 / e
    dof = len(bins) - 1
    return chi, dof, bins, exp

for label, sieve, depth in [("depth-1000 (sieve 2e7)", 20_000_000, 1000),
                            ("fresh depth-600 (sieve 2e7)", 20_000_000, 600)]:
    bits = s_bits(primes_up_to(sieve), depth)
    n = len(bits)
    p0 = bits.count(0)/n; p1 = 1-p0
    print(f"\n=== {label}: n={n}, p0={p0:.3f}")
    for val, name, pv in [(0,"0-run",p0),(1,"1-run",p1)]:
        rl = runs(bits, val)
        chi, dof, bins, exp = chi2_geom(rl, n, pv)
        print(f"  {name}s: R={len(rl)}, chi2={chi:.2f}, dof={dof}")
        print(f"    observed bins(m=1..7,8+): {bins}")
        print(f"    expected               : {[f'{e:.1f}' for e in exp]}")
