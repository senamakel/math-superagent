#!/usr/bin/env python3
"""Verify every distinct family in the CURRENT subprogression capture is an
exact polynomial identity, then recompute the coverage of n == 1 (mod 840)
rigorously.

The capture file has been overwritten by a longer run than the one recorded in
CONTEXT.md (94.72%), so the recorded number may not match the file. Re-derive
each family from its (a,b) header and its x,y,z polynomials, check
4xyz - n(yz+xz+xy) == 0 in Z[k] exactly, then aggregate the covered residue
classes of t and compute the union density exactly.

Usage:  python3 code/pattern_mining/verify_current_coverage.py
"""
import re
import sys
from fractions import Fraction
from sympy import Symbol, expand, Poly

k = Symbol("k")


def is_identity(xs, ys, zs, ns):
    """Return True iff 4xyz - n(yz+xz+xy) == 0 as polynomial in k."""
    for (x, y, z, n) in [(xs, ys, zs, ns)]:
        e = expand(4 * x * y * z - n * (y * z + x * z + x * y))
        return e == 0


def parse():
    txt = open("code/out/subprogression.captured.txt").read()
    blocks = []
    lines = txt.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"FOUND a=(\d+) b=(\d+)\s+x=(.*)", lines[i])
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            xs = m.group(3).strip()
            ys = zs = None
            j = i + 1
            while j < len(lines):
                ym = re.match(r"\s+y=(.*)", lines[j])
                zm = re.match(r"\s+z=(.*)", lines[j])
                if ym and ys is None:
                    ys = ym.group(1).strip().split("  [")[0]
                if zm and zs is None:
                    zs = zm.group(1).strip().split("  [")[0]
                if ys and zs:
                    break
                j += 1
            blocks.append((a, b, xs, ys, zs))
            i = j + 1
        else:
            i += 1
    return blocks


def main():
    blocks = parse()
    print(f"parsed {len(blocks)} FOUND blocks")
    # de-dup by (a,b) -- distinct residue classes
    seen = {}
    for (a, b, xs, ys, zs) in blocks:
        seen.setdefault((a, b), (xs, ys, zs))
    print(f"distinct (a,b): {len(seen)}")

    bad = []
    nbad = 0
    pairs = {}
    for (a, b), (xs, ys, zs) in sorted(seen.items()):
        try:
            X = eval(xs)
            Y = eval(ys)
            Z = eval(zs)
            N = a * k + b
            if not is_identity(X, Y, Z, N):
                nbad += 1
                bad.append((a, b))
            else:
                M = a // 840
                s = ((b - 1) // 840) % M
                pairs.setdefault(M, set()).add(s)
        except Exception as e:
            print(f"  parse/verify error a={a} b={b} x={xs} y={ys} z={zs}: {e}")
            nbad += 1
            bad.append((a, b))

    print(f"identity failures: {nbad}  -> {bad[:20]}")
    if nbad:
        print("ABORT: coverage invalid until failures resolved")
        sys.exit(1)

    print("\ncovered t-residue classes per modulus (from identity-verified families):")
    for M in sorted(pairs):
        print(f"  M={M}: {len(pairs[M])}/{M} s={sorted(pairs[M])}")

    # Coverage of n = 840t+1.  Moduli factor into an independent coupled prime
    # block {2,3,11,13,17,19,23?..} and standalone primes.
    # Build a small period over ALL primes present.
    primes = set()
    for M in pairs:
        x = M
        d = 2
        while d * d <= x:
            while x % d == 0:
                primes.add(d)
                x //= d
            d += 1
        if x > 1:
            primes.add(x)
    primes = sorted(primes)
    print("\nprimes involved:", primes)

    # Coverage of n = 840t+1.  The t-residue class covered by modulus M and
    # residue s is  t == s (mod M).  The moduli couple the small primes
    # {2,3} x {11,13,17,19} (M = 22,26,33,34,38,39) and carry 11,13,17,19
    # standalone; the rest (23,29,31,37,41,43) are independent.
    # => coupled block period = 2*3*11*13*17*19 = 277134; standalone primes
    # multiply independently.
    cperiod = 2 * 3 * 11 * 13 * 17 * 19
    cov = [False] * cperiod
    coupled = [11, 13, 17, 19, 22, 26, 33, 34, 38, 39]
    for M in coupled:
        for s in pairs.get(M, set()):
            for t in range(s, cperiod, M):
                cov[t] = True
    cc = sum(cov)
    uncov = Fraction(cperiod - cc, cperiod)
    print(f"\ncoupled block [{2*3*11*13*17*19}]: covered {cc}, "
          f"uncovered {uncov} = {100*float(uncov):.6f}%")
    total = uncov
    for p in [23, 29, 31, 37, 41, 43]:
        nc = len(pairs.get(p, set()))
        f = Fraction(p - nc, p)
        total = total * f
        print(f"  standalone p={p}: covered {nc}/{p} -> factor {f} "
              f"running uncovered {100*float(total):.6f}%")
    print(f"\n=== TOTAL uncovered within n=840t+1: {total} "
          f"= {100*float(total):.6f}%")
    print(f"=== TOTAL covered: {100*(1-float(total)):.6f}%")


if __name__ == "__main__":
    main()
