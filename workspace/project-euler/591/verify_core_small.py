"""Validate core_best (Ostrowski candidate enumeration) against brute force
on many small random cases for several d. Reports mismatch counts per d."""
import random
import math
from toolkits.core_best import core_best


def circdist_brute(alpha, beta, B):
    best = 0
    bd = 2.0
    for n in range(0, B + 1):
        f = n * alpha - math.floor(n * alpha)
        d = f - beta
        if d < 0:
            d += 1
        d = min(d, 1 - d)
        if d < bd:
            bd = d
            best = n
    return best, bd


def run_cases(d, ncases, Bmax=300):
    a0 = math.isqrt(d)
    alpha = math.sqrt(d) - a0
    mism = 0
    for _ in range(ncases):
        B = random.randint(1, Bmax)
        beta = random.random()
        bb, db, _ = core_best(d, beta, B, dps=80)
        bb2, db2 = circdist_brute(alpha, beta, B)
        if abs(db2 - float(db)) > 1e-9:
            mism += 1
            print(f"  d={d} B={B} beta={beta:.6f}: algo b={bb} d={float(db):.10f}, "
                  f"brute b={bb2} d={db2:.10f}")
    return mism


if __name__ == "__main__":
    total = 0
    for d in [2, 3, 5, 7, 10, 13, 19, 29, 41, 97]:
        f = run_cases(d, 2000)
        total += f
        print(f"d={d}: {f} mismatches")
    print("TOTAL mismatches:", total)
