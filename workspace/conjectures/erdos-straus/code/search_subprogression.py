#!/usr/bin/env python3
"""Search for explicit polynomial identity families covering sub-progressions
n = ak + b of the open class n ≡ 1 (mod 840).

Sourced background:
  * Schinzel Thm 1: no single Z[x] poly identity covers n = 840k+1 (b=1 is QR
    mod 840).  Escape: split into sub-progressions  n = ak+b, b ≡ 1 mod 840,
    with b a QNR mod a.
  * Salez Prop 3: for degree-1 prime polynomial at+b, an identity exists iff
    one of seven modular equations (14a,b,c, 15a,b,c,d) holds, with explicit
    A,B,C,D.  Enumerating the seven shapes is exhaustive for this shape.
  * Rosati decomposition (Salez Prop 1/eq 4): 4ABCD = p3 A + p3 B + p2 C with
      - branch 14 (p divides TWO): 4ABCD=A+B+pC, denoms (pBCD, pACD, ABD)
      - branch 15 (p divides ONE): 4ABCD=p(A+B)+C, denoms (BCD, ACD, pABD)

KEY INSIGHT: b ≡ 1 mod 840 implies b is a QR mod each of 2,3,5,7 (b≡1 mod all;
also mod 8 since b≡1 mod 8).  So b is a QR mod a=840M for any M whose primes
all divide 840.  A family is only possible when M has a prime factor q NOT
dividing 840 with b a QNR mod q.  We only search such M.

The seven converse directions (Salez Prop 3) give explicit A,B,C,D:
  14a: A=(B+pC)/(4BCD-1)
  14b: C=(A+B)/E,  D=(p+E)/(4AB)
  14c: A=(p+E)/(4BD), C=(p+E+4B^2D)/(4BDE)
  15a: C=(A+B)/E,  D=(pE+1)/(4AB)
  15b: D=(p+F)/(4BC),  A=(pB+C)/F
  15c: C=(p+F)/(4BD), E=(4B^2D+1)/F, A=CE-B
  15d: B=(p+F)/(4CD), A=(pB+C)/F

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


def is_poly_int_positive(expr):
    e = simplify(expr)
    if not e.is_polynomial(k):
        return False
    try:
        p = Poly(e, k)
    except Exception:
        return False
    return all(c.is_integer for c in p.all_coeffs())


def is_identity(x, y, z, n):
    return simplify(4 / n - (1 / x + 1 / y + 1 / z)) == 0


def pos_int(x, ks=(1, 2, 3, 5, 10, 50, 100, 1000)):
    e = simplify(x)
    for kk in ks:
        try:
            if int(e.subs(k, kk)) <= 0:
                return False
        except Exception:
            return False
    return True


def br14(p, A, B, C, D):
    return p * B * C * D, p * A * C * D, A * B * D


def br15(p, A, B, C, D):
    return B * C * D, A * C * D, p * A * B * D


def verify_and_emit(x, y, z, info, a, b, out, seen):
    key = (str(simplify(x)), str(simplify(y)), str(simplify(z)))
    if key in seen:
        return
    seen.add(key)
    if (is_poly_int_positive(x) and is_poly_int_positive(y)
            and is_poly_int_positive(z) and pos_int(x) and pos_int(y)
            and pos_int(z)):
        out.append((a, b, x, y, z, info))
        print(f"FOUND a={a} b={b}  x={x}\n    y={y}\n    z={z}  [{info}]", flush=True)


def try_14a(a, b, out, seen, Bmax=120, Cmax=120, Dmax=120):
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
                verify_and_emit(*br14(p, Az, B, C, D), ("14a", B, C, D, f),
                                a, b, out, seen)


def try_14b(a, b, out, seen, Amax=80, Bmax=80, Emax=80):
    for A in range(1, Amax):
        for B in range(1, Bmax):
            for E in range(1, Emax):
                if (A + B) % E:
                    continue
                g = 4 * A * B
                if a % g or (b + E) % g:
                    continue
                C = (A + B) // E
                Dk = (a * k + b + E) // g
                if not is_poly_int_positive(Dk):
                    continue
                p = a * k + b
                verify_and_emit(*br14(p, A, B, C, Dk), ("14b", A, B, E, C),
                                a, b, out, seen)


def try_14c(a, b, out, seen, Bmax=50, Dmax=50, Emax=50):
    for B in range(1, Bmax):
        for D in range(1, Dmax):
            for E in range(1, Emax):
                g1 = 4 * B * D
                if a % g1 or (b + E) % g1:
                    continue
                g2 = 4 * B * D * E
                if a % g2 or (b + E + 4 * B * B * D) % g2:
                    continue
                Ak = (a * k + b + E) // g1
                Ck = (a * k + b + E + 4 * B * B * D) // g2
                if not (is_poly_int_positive(Ak) and is_poly_int_positive(Ck)):
                    continue
                p = a * k + b
                verify_and_emit(*br14(p, Ak, B, Ck, D), ("14c", B, D, E),
                                a, b, out, seen)


def try_15a(a, b, out, seen, Amax=80, Bmax=80, Emax=80):
    for A in range(1, Amax):
        for B in range(1, Bmax):
            for E in range(1, Emax):
                if (A + B) % E:
                    continue
                g = 4 * A * B
                if (a * E) % g or (b * E + 1) % g:
                    continue
                C = (A + B) // E
                Dk = (a * E // g) * k + ((b * E + 1) // g)
                if not is_poly_int_positive(Dk):
                    continue
                p = a * k + b
                verify_and_emit(*br15(p, A, B, C, Dk), ("15a", A, B, E, C),
                                a, b, out, seen)


def try_15b(a, b, out, seen, Bmax=80, Cmax=80, Fmax=80):
    for B in range(1, Bmax):
        for C in range(1, Cmax):
            for F in range(1, Fmax):
                g = 4 * B * C
                if a % g or (b + F) % g:
                    continue
                if (a * B) % F or (b * B + C) % F:
                    continue
                Dk = (a * k + b + F) // g
                Ak = (a * B // F) * k + ((b * B + C) // F)
                if not (is_poly_int_positive(Dk) and is_poly_int_positive(Ak)):
                    continue
                p = a * k + b
                verify_and_emit(*br15(p, Ak, B, C, Dk), ("15b", B, C, F),
                                a, b, out, seen)


def try_15c(a, b, out, seen, Bmax=80, Dmax=80, Fmax=80):
    for B in range(1, Bmax):
        for D in range(1, Dmax):
            for F in range(1, Fmax):
                g = 4 * B * D
                if a % g or (b + F) % g:
                    continue
                if (4 * B * B * D + 1) % F:
                    continue
                Ck = (a * k + b + F) // g
                E = (4 * B * B * D + 1) // F
                if not is_poly_int_positive(Ck):
                    continue
                Ak = simplify(Ck * E - B)
                if not is_poly_int_positive(Ak):
                    continue
                p = a * k + b
                verify_and_emit(*br15(p, Ak, B, Ck, D), ("15c", B, D, F, E),
                                a, b, out, seen)


def try_15d(a, b, out, seen, Cmax=80, Dmax=80, Fmax=80):
    for C in range(1, Cmax):
        for D in range(1, Dmax):
            for F in range(1, Fmax):
                g = 4 * C * D
                if a % g or (b + F) % g:
                    continue
                p = a * k + b
                Bk = (a * k + b + F) // g   # (p+F)/(4CD)
                Ak = simplify(p * Bk + C) / F
                if not is_poly_int_positive(Ak):
                    continue
                verify_and_emit(*br15(p, Ak, Bk, C, D), ("15d", C, D, F),
                                a, b, out, seen)


def trial_primes_and_M(Mmax=60):
    """Return M values that have at least one new prime factor q∤840."""
    result = []
    small = {2, 3, 5, 7}
    for M in range(1, Mmax + 1):
        if any(p not in small for p in prime_factors(M)):
            result.append(M)
    return result


def prime_factors(n):
    f = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            f.add(d)
            n //= d
        d += 1
    if n > 1:
        f.add(n)
    return f


def main():
    t0 = time.time()
    found = []
    seen_global = set()
    Ms = [M for M in trial_primes_and_M(61) if gcd(M, 840) and M <= 90]
    # make sure we include primes 11,13,17,19,23 individually and their products
    probe = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    Ms = sorted(set(Ms) | set(probe) | {11 * 13, 13 * 17, 11 * 17, 840 + 11})
    total_attempts = 0
    for M in Ms:
        a = 840 * M
        for j in range(M):
            b = 1 + 840 * j
            if gcd(b, M) != 1:
                continue
            if quad_residue(b, a):
                continue
            total_attempts += 1
            try_14a(a, b, found, seen_global)
            try_14b(a, b, found, seen_global)
            try_14c(a, b, found, seen_global)
            try_15a(a, b, found, seen_global)
            try_15b(a, b, found, seen_global)
            try_15c(a, b, found, seen_global)
            try_15d(a, b, found, seen_global)
    dt = time.time() - t0
    print(f"\n{len(found)} verified families over {total_attempts} candidate "
          f"(a,b) in {dt:.1f}s", flush=True)
    print(f"M values searched: {Ms}", flush=True)
    # Also record which CLASSES (mod 840) each family covers
    print("\n--- families by residue r = b mod 840 ---")
    for (a, b, x, y, z, info) in found:
        print(f"residue {b % 840}: n = {a}k + {b}  [{info}]", flush=True)


if __name__ == "__main__":
    main()
