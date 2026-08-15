#!/usr/bin/env python3
"""Verify the two directions of the descent<->Lebesgue equivalence EXACTLY,
and expose the sign-dependence of the forward map.

Claim to analyse:
    r^q - 2^{mq-2} s^q = +-1  <-->  x^2 - y^q = 1,  q odd prime, m>=1, r,s>=1,
    gcd(r,s)=1, with alleged map  x = 2 r^q + 1, y = 2^m r s.

Hand-derivation of the forward direction:
    x^2 - 1 = (2 r^q + 1)^2 - 1 = 4 r^q (r^q + 1)
    y^q     = (2^m r s)^q = 2^{mq} r^q s^q
    x^2 - y^q = 1  <-->  r^q + 1 = 2^{mq-2} s^q
                     <-->  r^q - 2^{mq-2} s^q = -1        (the -1 branch)
    For the +1 branch (r^q - 2^{mq-2}s^q = +1): r^q + 1 = 2^{mq-2}s^q + 2,
    so the single map x=2r^q+1 gives x^2 - y^q = 1 + 8 r^q, NOT 1.  Use
    x = 2 r^q - 1 instead (then x^2-1 = 4 r^q (r^q-1) = 4 r^q 2^{mq-2} s^q = y^q).
"""
import itertools, sys
from math import gcd

def check_forward_minus(q, m, r, s):
    """-1 branch: r^q - 2^{mq-2}s^q = -1  =>  x=2r^q+1,y=2^m rs  solves x^2-y^q=1."""
    target = 2 ** (m * q - 2)
    if r ** q - target * (s ** q) != -1:
        return None
    x, y = 2 * r ** q + 1, (2 ** m) * r * s
    return (x ** 2 - y ** q == 1, x, y)

def check_forward_plus_stated_map(q, m, r, s):
    """+1 branch with the ALLEGED map x=2r^q+1: SHOW it fails (x^2-y^q = 1+8 r^q)."""
    target = 2 ** (m * q - 2)
    if r ** q - target * (s ** q) != 1:
        return None
    x, y = 2 * r ** q + 1, (2 ** m) * r * s
    return (x ** 2 - y ** q, x, y, 1 + 8 * r ** q)   # expect (1+8 r^q, ..., 1+8 r^q)

def check_forward_plus_fixed_map(q, m, r, s):
    """+1 branch with corrected map x=2r^q-1: solves x^2-y^q=1."""
    target = 2 ** (m * q - 2)
    if r ** q - target * (s ** q) != 1:
        return None
    x, y = 2 * r ** q - 1, (2 ** m) * r * s
    return (x ** 2 - y ** q == 1, x, y)

def all_descent_sols(q, M, S):
    """Enumerate descent solutions (m,r,s,val) in range."""
    out = []
    for m in range(1, M + 1):
        target = 2 ** (m * q - 2)
        for r in range(1, S + 1):
            for s in range(1, S + 1):
                if gcd(r, s) != 1:
                    continue
                val = r ** q - target * (s ** q)
                if val in (1, -1):
                    out.append((m, r, s, val))
    return out

print("=" * 78)
print("FORWARD, -1 branch:  r^q - 2^{mq-2}s^q = -1")
print("   map x=2r^q+1, y=2^m rs  ->  x^2 - y^q == 1 ?")
print("=" * 78)
ok = True
for q in [3, 5, 7]:
    for (m, r, s) in [(1,1,1), (1,2,1), (2,1,1), (1,3,2)]:
        res = check_forward_minus(q, m, r, s)
        if res:
            good, x, y = res
            print(f"  q={q} m={m} r={r} s={s}: r^q-2^..s^q=-1 -> x={x} y={y} solves: {good}")
            ok = ok and good
print("all -1-branch forward checks pass:", ok)

print()
print("=" * 78)
print("FORWARD, +1 branch with the ALLEGED SINGLE MAP x=2r^q+1:")
print("   expectation from hand-algebra: x^2 - y^q = 1 + 8 r^q  (NOT 1)")
print("=" * 78)
found_plus = False
for q in [3, 5, 7]:
    for (m, r, s) in [(1,1,1), (1,2,1), (2,1,1)]:
        res = check_forward_plus_stated_map(q, m, r, s)
        if res:
            found_plus = True
            val, x, y, expect = res
            print(f"  q={q} m={m} r={r} s={s}: +1 branch, x^2-y^q = {val}  |  1+8r^q = {expect}  match={val==expect}")
print("(+1 branch solutions with these small (m,r,s): none decoded w/ gcd=1 reset below)")
if not found_plus:
    print("  no +1-branch solutions found in the tiny sample (expected: none here)")

print()
print("=" * 78)
print("Search actual +1-branch descent solutions (does the +1 branch ever occur?)")
print("=" * 78)
plus_hits = []
minus_hits = []
for q in [3, 5, 7]:
    for (m, r, s, val) in all_descent_sols(q, 8, 60):
        if val == 1:
            plus_hits.append((q, m, r, s))
        else:
            minus_hits.append((q, m, r, s))
print("  -1 branch hits (q,m,r,s):", minus_hits)
print("  +1 branch hits (q,m,r,s):", plus_hits)
print("  => known solution (3,1,1,1) present in minus:", (3,1,1,1) in minus_hits)

print()
print("=" * 78)
print("FORWARD +1 branch with CORRECTED map x=2r^q-1: verify it closes")
print("=" * 78)
if plus_hits:
    for (q, m, r, s) in plus_hits:
        good, x, y = check_forward_plus_fixed_map(q, m, r, s)
        print(f"  q={q} m={m} r={r} s={s}: x={x} y={y} solves x^2-y^q=1: {good}")
else:
    # give a synthetic +1-branch datum to test the corrected map algebraically
    # pick r,s,m with r^q - 2^{mq-2}s^q = +1 : try m=1 => target=2^{q-2}
    print("  (no real +1 hits in range; checking the identity symbolically for r=3,s=2,m=2,q=3)")
    q,m,r,s = 3,2,3,2   # target=2^{4}=16 ; r^3 - 16 s^3 = 27 - 128 = -101 no; try below
    # find one: brute over which r^q = 2^{mq-2}s^q + 1
    got = None
    for qq in [3]:
        for mm in range(1,6):
            t = 2**(mm*qq-2)
            for rr in range(1,200):
                for ss in range(1,200):
                    if gcd(rr,ss)==1 and rr**qq - t*ss**qq == 1:
                        got = (qq,mm,rr,ss); break
                if got: break
            if got: break
        if got: break
    print("  a real +1-branch solution found:", got)
    if got:
        q,m,r,s = got
        good, x, y = check_forward_plus_fixed_map(q, m, r, s)
        print(f"  +1 branch q={q} m={m} r={r} s={s}: corrected map x={x} y={y} solves: {good}")
