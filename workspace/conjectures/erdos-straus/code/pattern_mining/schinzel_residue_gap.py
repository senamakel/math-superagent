#!/usr/bin/env python3
"""Test the Schinzel QNR constraint against the realized residue set for the
sub-progression covering of n=840K+1.

For a family n = a*k + b covering the whole AP n == b (mod a), Schinzel Thm 1
forbids it when b is a quadratic RESIDUE mod a. Here a = 840*M, b = 840t+1
with t == s (mod M). So a necessary condition for s to be realizable is that
b = 840s+1 (modifying by the modulus a) is a QNR mod 840*M.

For M=23: is the realized set exactly {s : 840s+1 QNR mod 19320}, or are there
QNR-allowed residues that are NOT realized (gap = additional obstruction or
just an uncovered family)?
"""
import re
from collections import defaultdict
from math import gcd

def legendre(a, p):
    return pow(a % p, (p - 1) // 2, p)  # 1 if QR, p-1 if NQR, 0 if divisible

def is_qr_mod(a, m):
    """a quadratic residue modulo m (m = 2^3 * 3 * 5 * 7 * 23, i.e. prime-power
    factorization with odd primes)."""
    # factor m
    mm = m
    facs = []
    q = 2
    while q*q <= mm:
        if mm % q == 0:
            e = 0
            while mm % q == 0:
                mm //= q
                e += 1
            facs.append((q, e))
        q += 1
    if mm > 1:
        facs.append((mm, 1))
    from sympy import is_quad_residue
    for p, e in facs:
        if p == 2:
            # x^2 mod 2^e: for e>=3 a quadratic residue is 1 mod 8 (when odd)
            # and must satisfy the standard condition
            if not is_quad_residue(a, 2**e):
                return False
        else:
            if not is_quad_residue(a, p**e):
                return False
    return True

def sub(Q, p):
    """Q mod p^e via sympy"""
    from sympy import is_quad_residue
    if p == 2:
        return is_quad_residue(Q, Q ** 0 + 8)  # dummy
    return None

txt = open('/workspace/code/out/extended_subprogression.full.txt').read()
lines = txt.splitlines()
per = defaultdict(set)
for ln in lines:
    m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=', ln)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        M = a // 840
        c = (b - 1) // 840
        per[M].add(c)

from sympy import is_quad_residue
print("For each prime modulus M, compare realized t-residues vs Schinzel-QNR condition")
for M in sorted(per):
    if M not in (11, 13, 17, 19, 23, 29, 31, 37):
        continue
    S = per[M]
    a = 840 * M
    realized = []
    qnr_allowed = []   # s where b=840s+1 is QNR mod 840*M
    qr_blocked = []    # s where b is QR mod 840*M (Schinzel-forbidden)
    for s in range(M):
        bmod = (840 * s + 1) % a
        bmod = bmod % a if bmod else (bmod % a)  # 840s+1 mod 840M
        # b=840s+1, but we care b as a full value; QR mod a
        is_qr = is_quad_residue(840*s+1, a) if (gcd(840*s+1, a) == 1) else 'nonun'
        # gcd must be 1 for a unit; if not coprime, b shares factor with a -> still
        # Schinzel needs (a,b)=1; here gcd(840*s+1, 840)=1 always since 840s+1==1 mod 840
        # but mod M: gcd(840s+1, M) could be >1
        g = gcd(840*s+1, a)
        if is_qr == 'nonun':
            status = 'nonunit'  # b not coprime to a
        else:
            status = 'QR-blocked' if is_qr else 'QNR-allowed'
        if s in S:
            realized.append((s, status))
        else:
            if status == 'QNR-allowed':
                qnr_allowed.append(s)
            elif status == 'QR-blocked':
                qr_blocked.append(s)
    realized_set = {s for s, st in realized}
    print(f"M={M}: realized {sorted(realized_set)}")
    print(f"    QNR-allowed-but-NOT-realized (gap, worth targeting): {qnr_allowed}")
    print(f"    QR-blocked (Schinzel-forbidden, never realizable): {qr_blocked}")
    # consistency: all realized must be QNR-allowed or nonunit
    bad = [s for s, st in realized if st == 'QR-blocked']
    print(f"    realized that are QR-blocked (would violate Schinzel): {bad}")
