#!/usr/bin/env python3
"""Complete seven-shape (Salez Prop 3) search for the legal-but-missing
sub-progression residues of the open class n=840t+1.

Targets: per-prime Schinzel-legal residues NOT realized by the run's 1451
families:
   M=17: s in {3,13}  -> (a,b) = (14280, 2521), (14280, 10921)
   M=19: s in {3,5,7,10} -> (a,b) = (15960, 2521), (15960, 4201), (15960, 5881), (15960, 8401)
   M=23: s in {3,8}  -> (a,b) = (19320, 2521), (19320, 6721)

The seven Salez shapes:
   14a: f=4BCD-1 | a, B+Cb == 0 mod f;  A=(B+pC)/f
   14b: g=4AB | a, E | A+B, E == -b mod g;  C=(A+B)/E, D=(p+E)/g
   14c: 4BD | a, 4BDE | a, E == -b mod 4BD, b+E+4B^2D == 0 mod 4BDE
   15a: g=4AB, E | A+B, bE+1 == 0 mod g, aE == 0 mod g;  C=(A+B)/E, D=(pE+1)/g
   15b: 4BC | a, F == -b mod 4BC, F | aB, bB+C == 0 mod F
   15c: 4BD | a, F == -b mod 4BD, F | 4B^2D+1
   15d: 4CD | a, F == -b mod 4CD, F | needed for Ak integral
with p = a*k+b, br14 -> (pBCD, pACD, ABD), br15 -> (BCD, ACD, pABD).

The run's earlier search capped parameters at 80-120; shapes 15a (E large,
AB effectively unbounded), 15b/c (F divides aB resp. 4B^2D+1, can be large)
were NOT complete. This search enumerates the divisor-based constraints.

VERIFICATION: every candidate is checked as an exact polynomial identity in k
(4xyz - p(yz+xz+xy) == 0 over Z[k]) and for positive integer coefficients of
x,y,z with p=ak+b.
"""
import sys, time
from math import gcd
from sympy import Symbol, Poly, expand

k = Symbol('k', integer=True)

def divisors(n):
    ds = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            ds.append(d)
            if d*d != n:
                ds.append(n//d)
        d += 1
    return sorted(ds)

def factor_triples(T):
    """all (b,c,d) positive with b*c*d == T, b<=c<=d order-irrelevant"""
    out = []
    for b in divisors(T):
        T1 = T // b
        for c in divisors(T1):
            d = T1 // c
            if c <= d:  # avoid symmetry duplicates b<=c<=d
                out.append((b, c, d))
            # actually permutations matter for 14a (B,C,D not symmetric)
    # return ALL ordered triples
    out = []
    for b in divisors(T):
        T1 = T // b
        for c in divisors(T1):
            d = T1 // c
            out.append((b, c, d))
    return out

def inv_mod(a, m):
    """inverse of a mod m, or None; gcd(a,m)==1 assumed"""
    g, x0, x1 = m, 0, 1
    aa, mm = a, m
    g, x, y = mm, 0, 1
    while aa:
        q = g // aa
        g, aa = aa, g - q*aa
        x, y = y, x - q*y
    # g == 1
    return x % m

def is_identity(a, b, x, y, z):
    """exact polynomial identity 4xyz = p( yz+xz+xy ), p=ak+b, over Z[k]"""
    p = a*k + b
    lhs = expand(4*x*y*z)
    rhs = expand(p*(y*z + x*z + x*y))
    return Poly(lhs, k) - Poly(rhs, k) == Poly(0, k)

def pos_int_poly(expr):
    p = Poly(expand(expr), k)
    coeffs = p.all_coeffs()
    if not coeffs:
        return False
    # positive degree-1 coeffs, nonneg constant -> positive for k>=1
    return all(c >= 0 for c in coeffs) and coeffs[0] > 0  # all_coeffs is high->low

def emit(x, y, z, info, a, b, found, out):
    global COUNT
    if not (is_identity(a, b, x, y, z) and pos_int_poly(x) and pos_int_poly(y)
            and pos_int_poly(z)):
        return
    key = (str(Poly(expand(x), k).as_expr()), str(Poly(expand(y), k).as_expr()),
           str(Poly(expand(z), k).as_expr()))
    if key in found:
        return
    found.add(key)
    out.write(f"FOUND a={a} b={b}  x={expand(x)}\n    y={expand(y)}\n    z={expand(z)}  [{info}]\n")
    out.flush()

def p_expr(a, b):
    return a*k + b

def try_14a_complete(a, b, out, found):
    for f in divisors(a):
        if (f+1) % 4 != 0:
            continue
        T = (f+1)//4
        for (B, C, D) in factor_triples(T):
            if (B + C*b) % f != 0:
                continue
            p = p_expr(a, b)
            A = (B + C*p) // f
            x, y, z = p*B*C*D, p*A*C*D, A*B*D
            emit(x, y, z, f"14a B={B} C={C} D={D} f={f}", a, b, found, out)

def try_14b_complete(a, b, out, found, Emax=None):
    # g=4AB | a ; E | A+B ; E == -b mod g
    for A in divisors(a//4):
        for B in divisors(a//4):
            g = 4*A*B
            if a % g:
                continue
            # E == -b mod g, E | A+B
            e0 = (-b) % g
            # E = e0 + g*j, E | A+B
            S = A + B
            if e0 == 0 or S % e0 != 0:
                E = None
                # brute over j is bounded by E | S: E <= S
                # E in {e0 + g*j} intersect divisors of S
                for E in divisors(S):
                    if E % g == (-b) % g:
                        break
                else:
                    E = None
            else:
                E = e0
            # careful: need E | S AND E.equiv(-b) mod g; iterate divisors
            E = None
            for Ee in divisors(S):
                if Ee % g == (-b) % g:
                    E = Ee
                    break
            if E is None:
                continue
            C = S // E
            p = p_expr(a, b)
            D = (p + E) // g
            if not is_identity(a, b, p*B*C*D, p*A*C*D, A*B*D):
                continue
            x, y, z = p*B*C*D, p*A*C*D, A*B*D
            emit(x, y, z, f"14b A={A} B={B} E={E} C={C}", a, b, found, out)

def try_14c_complete(a, b, out, found):
    # 4BD | a, E == -b mod 4BD, 4BDE | a, b+E+4B^2D == 0 mod 4BDE
    seen = set()
    for B in range(1, a//4 + 1):
        if (a // 4) % B:
            continue
        for D in range(1, (a//4)//B + 1):
            g1 = 4*B*D
            if a % g1:
                continue
            e0 = (-b) % g1
            # E = e0 + g1*j, 4BDE | a  <=> E | a/(4BD)
            T = a // g1
            for E in divisors(T):
                if E % g1 != e0:
                    continue
                g2 = 4*B*D*E
                if a % g2:
                    continue
                if (b + E + 4*B*B*D) % g2:
                    continue
                if (g1, E) in seen:
                    continue
                seen.add((g1, E))
                p = p_expr(a, b)
                A = (p + E) // g1
                C = (p + E + 4*B*B*D) // g2
                x, y, z = p*B*C*D, p*A*C*D, A*B*D
                emit(x, y, z, f"14c B={B} D={D} E={E}", a, b, found, out)

def try_15a_complete(a, b, out, found, Amax, Bmax):
    """E | A+B, E == -b^{-1} mod 4AB, 4AB | aE.
    Bounded search over A,B (the old run: Amax=Bmax=80)."""
    for A in range(1, Amax+1):
        for B in range(1, Bmax+1):
            g = 4*A*B
            if gcd(b, g) != 1:
                continue
            # bE == -1 mod g
            e = inv_mod(b, g)
            if e is None:
                continue
            # need E = e + g*j with E | A+B and 4AB | aE
            S = A + B
            if e > S:
                continue
            # candidates E | S, E ≡ e mod g
            E = None
            for Ee in divisors(S):
                if Ee % g == e:
                    E = Ee
                    break
            if E is None:
                continue
            # check (b*E+1)%g==0 and a*E % g == 0
            if (b*E + 1) % g or (a*E) % g:
                continue
            p = p_expr(a, b)
            C = S // E
            D = (p*E + 1) // g
            x, y, z = B*C*D, A*C*D, p*A*B*D
            emit(x, y, z, f"15a A={A} B={B} E={E} C={C}", a, b, found, out)

def try_15b_complete(a, b, out, found, Cmax, Fmax):
    """4BC | a; F == -b mod 4BC; F | aB; bB+C == 0 mod F; F <= Fmax"""
    for B in range(1, a//4 + 1):
        for C in range(1, Cmax+1):
            g = 4*B*C
            if a % g:
                continue
            if B*C > a//4:
                continue
            # F ≡ -b mod g, F | aB, F ≤ Fmax
            f0 = (-b) % g
            for F in range(f0 if f0 > 0 else g, min(a*B, Fmax) + 1, g):
                if F == 0:
                    continue
                if (a*B) % F:
                    continue
                if (b*B + C) % F:
                    continue
                p = p_expr(a, b)
                D = (p + F) // g
                A = (a*B//F)*k + ((b*B + C)//F)
                x, y, z = B*C*D, A*C*D, p*A*B*D
                emit(x, y, z, f"15b B={B} C={C} F={F}", a, b, found, out)

def try_15c_complete(a, b, out, found, Fmax):
    """4BD | a; F ≡ -b mod 4BD; F | 4B^2D+1; F ≤ Fmax"""
    for B in range(1, a//4 + 1):
        for D in range(1, (a//4)//B + 1):
            g = 4*B*D
            if a % g:
                continue
            f0 = (-b) % g
            if f0 == 0:
                f0 = g
            for F in range(f0, Fmax+1, g):
                if (4*B*B*D + 1) % F:
                    continue
                p = p_expr(a, b)
                C = (p + F) // g
                E = (4*B*B*D + 1) // F
                A = C*E - B
                x, y, z = B*C*D, A*C*D, p*A*B*D
                emit(x, y, z, f"15c B={B} D={D} F={F} E={E}", a, b, found, out)

def try_15d_complete(a, b, out, found, Fmax):
    """4CD | a; F ≡ -b mod 4CD; Ak=(p*Bk+C)/F polynomial"""
    for C in range(1, a//4 + 1):
        for D in range(1, (a//4)//C + 1):
            g = 4*C*D
            if a % g:
                continue
            f0 = (-b) % g
            if f0 == 0:
                f0 = g
            for F in range(f0, Fmax+1, g):
                p = p_expr(a, b)
                B = (p + F) // g
                A = expand((p*B + C) / F)
                if not A.is_polynomial(k):
                    continue
                x, y, z = B*C*D, A*C*D, p*A*B*D
                emit(x, y, z, f"15d C={C} D={D} F={F}", a, b, found, out)

def main():
    targets = [
        (14280, 2521, 'M17-s3'),
        (14280, 10921, 'M17-s13'),
        (15960, 2521, 'M19-s3'),
        (15960, 4201, 'M19-s5'),
        (15960, 5881, 'M19-s7'),
        (15960, 8401, 'M19-s10'),
        (19320, 2521, 'M23-s3'),
        (19320, 6721, 'M23-s8'),
    ]
    out = sys.stdout
    found_all = set()
    for (a, b, tag) in targets:
        t0 = time.time()
        print(f"\n=== target {tag}: n = {a}k + {b} ===", flush=True)
        local_found = set()
        try_14a_complete(a, b, out, local_found)
        try_14b_complete(a, b, out, local_found)
        try_14c_complete(a, b, out, local_found)
        try_15a_complete(a, b, out, local_found, Amax=1500, Bmax=1500)
        try_15b_complete(a, b, out, local_found, Cmax=200, Fmax=200000)
        try_15c_complete(a, b, out, local_found, Fmax=200000)
        try_15d_complete(a, b, out, local_found, Fmax=200000)
        print(f"--- {tag}: {len(local_found)} verified families in {time.time()-t0:.1f}s", flush=True)
        found_all |= local_found
    print(f"\nTOTAL new verified families: {len(found_all)}", flush=True)

if __name__ == '__main__':
    main()