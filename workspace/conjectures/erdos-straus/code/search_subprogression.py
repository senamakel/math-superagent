#!/usr/bin/env python3
"""Search for explicit polynomial identity families covering sub-progressions
n = ak + b of the open class n ≡ 1 (mod 840).

Core facts (sourced):
  * Schinzel Thm 1: NO single Z[x]-polynomial identity
    4/(at+b)=1/F1+1/F2+1/F3 exists when b is a QR mod a.  Since 1 is a QR mod
    840, the class n = 840k+1 itself is blocked.  Answer: split into
    sub-progressions.
  * Salez Prop 3: for a degree-1 prime polynomial at+b (i.e. (a,b)=1), the
    identity exists iff one of SEVEN constant-coefficient modular equations
    (14a,b,c / 15a,b,c,d) holds, and for each shape A,B,C,D are explicit
    (constants or linear polynomials).  Enumerating those shapes is exhaustive
    for the prime-polynomial shape.
  * Rosati denominator formula (Prop 1): 4/p = 1/(BCD) + 1/(ACD) + 1/(pABD)
    [Type I: p | exactly one denominator] or 4/p = 1/(pBCD)+1/(pACD)+1/(ABD)
    [Type II: p divides two].

We search a = 840*M, b = 1 + 840*j (so b ≡ 1 mod 840), gcd(b,M)=1 so at+b is
a prime polynomial, b a QNR mod a (necessary by Schinzel).  For each candidate
we enumerate the seven shapes with small constant A,B,C,D,E,F and report every
(a,b) admitting an explicit verified family x(k),y(k),z(k).

Run:
    timeout 540 python3 code/search_subprogression.py 2>&1 | \
        tee code/out/subprogression.captured.txt
"""

from __future__ import annotations

from math import gcd
import time

from sympy import Symbol, simplify, Poly

k = Symbol("k", integer=True, positive=True)


def quad_residue(b: int, a: int) -> bool:
    return (b % a) in {(q * q) % a for q in range(a)}


def is_poly_int(expr):
    e = simplify(expr)
    if not e.is_polynomial(k):
        return None
    try:
        p = Poly(e, k)
    except Exception:
        return None
    # allow rational constant / cleared denominators
    if not all(c.is_integer for c in p.all_coeffs()):
        return None
    return p


def is_identity(x, y, z, n):
    return simplify(4 / n - (1 / x + 1 / y + 1 / z)) == 0


def pos_int(x, ks=(1, 2, 3, 5, 10, 50, 100)):
    e = simplify(x)
    for kk in ks:
        try:
            v = int(e.subs(k, kk))
        except Exception:
            return False
        if v <= 0:
            return False
    return True


def rosati_I(p, A, B, C, D):
    return B * C * D, A * C * D, p * A * B * D


def rosati_II(p, A, B, C, D):
    return p * B * C * D, p * A * C * D, A * B * D


def try_14a(a, b, Bmax=80, Cmax=80, Dmax=80):
    """Type I.  A = (B + pC)/(4BCD - 1).  f = 4BCD-1 const; need f | C*a and
    f | (B + C*b)."""
    out = []
    for B in range(1, Bmax):
        for C in range(1, Cmax):
            for D in range(1, Dmax):
                f = 4 * B * C * D - 1
                if f <= 0:
                    continue
                if a % f != 0 or (B + C * b) % f != 0:
                    continue
                Az = simplify((B + C * (a * k + b)) / f)
                if not Az.is_polynomial(k):
                    continue
                p = a * k + b
                x, y, z = rosati_I(p, Az, B, C, D)
                if is_identity(x, y, z, p):
                    out.append((x, y, z, ("14a-I", B, C, D, f)))
    return out


def try_14b(a, b, Amax=40, Bmax=40, Emax=40):
    """Type I.  C = (A+B)/E, D = (p+E)/(4AB).  Need 4AB | a and 4AB | (b+E)."""
    out = []
    for A in range(1, Amax):
        for B in range(1, Bmax):
            for E in range(1, Emax):
                if (A + B) % E != 0:
                    continue
                g = 4 * A * B
                if a % g != 0 or (b + E) % g != 0:
                    continue
                C = (A + B) // E
                p = a * k + b
                Dk = (a * k + b + E) // g
                x, y, z = rosati_I(p, A, B, C, Dk)
                if is_identity(x, y, z, p):
                    out.append((x, y, z, ("14b-I", A, B, E, C)))
    return out


def try_15a(a, b, Amax=40, Bmax=40, Emax=40):
    """Type II.  C = (A+B)/E, D = (pE+1)/(4AB).  Need 4AB | (aE) and
    4AB | (bE+1)."""
    out = []
    for A in range(1, Amax):
        for B in range(1, Bmax):
            for E in range(1, Emax):
                if (A + B) % E != 0:
                    continue
                g = 4 * A * B
                if (a * E) % g != 0 or (b * E + 1) % g != 0:
                    continue
                C = (A + B) // E
                p = a * k + b
                # Dk = (pE + 1) / (4AB) = (aE k + (bE+1)) / (4AB)
                Dk = (a * E // g) * k + ((b * E + 1) // g)
                if Dk < 0 or not simplify(Dk).is_polynomial(k):
                    continue
                x, y, z = rosati_II(p, A, B, C, Dk)
                if is_identity(x, y, z, p):
                    out.append((x, y, z, ("15a-II", A, B, E, C)))
    return out


def main():
    t0 = time.time()
    found = []
    for M in range(1, 81):
        a = 840 * M
        for j in range(M):
            b = 1 + 840 * j
            if gcd(b, M) != 1:
                continue
            if quad_residue(b, a):
                continue
            hits = []
            hits += try_14a(a, b)
            hits += try_14b(a, b)
            hits += try_15a(a, b)
            seen = set()
            for (x, y, z, info) in hits:
                key = (str(x), str(y), str(z))
                if key in seen:
                    continue
                seen.add(key)
                if pos_int(x) and pos_int(y) and pos_int(z):
                    found.append((a, b, x, y, z, info))
                    print(f"M={M} (a={a}) b={b}  x={x} y={y} z={z}  [{info}]",
                          flush=True)
    dt = time.time() - t0
    print(f"\n{len(found)} verified families in {dt:.1f}s", flush=True)


if __name__ == "__main__":
    main()
