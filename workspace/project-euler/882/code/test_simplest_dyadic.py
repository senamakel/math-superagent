#!/usr/bin/env python3
"""Validate simplest_dyadic.simplest_between against an independent birthday
oracle (cached small enumeration)."""
import random
from fractions import Fraction
from toolkits.simplest_dyadic import simplest_between

MAXB = 16          # dyadics with birthday <= MAXB (small)

def birthday(x):
    x = abs(x)
    if x == 0:
        return 0
    n = x.numerator // x.denominator
    f = x - n
    if f == 0:
        return n
    # count binary digits of f
    d = 0
    while f.denominator > 1:
        f *= 2
        d += 1
    return n + d + 1

_cache = None
def dyadic_set():
    global _cache
    if _cache is not None:
        return _cache
    out = set()
    out.add(Fraction(0))
    # pure integers n (birthday n)
    for n in range(1, MAXB + 1):
        out.add(Fraction(n)); out.add(Fraction(-n))
    # integer part n in 0..MAXB, fractional f with digits d, birthday=n+d+1<=MAXB
    for n in range(0, MAXB + 1):
        for d in range(1, MAXB - n):        # birthday = n+d+1 <= MAXB -> d <= MAXB-n-1
            for m in range(1, 2 ** d):
                f = Fraction(m, 2 ** d)
                if f < 1:
                    out.add(Fraction(n) + f)
                    out.add(-(Fraction(n) + f))
    _cache = out
    return out

def birthday_oracle(a, b):
    best = None; best_b = None
    for x in dyadic_set():
        if a < x < b:
            bb = birthday(x)
            if best_b is None or bb < best_b:
                best_b = bb; best = x
    return best

def main():
    random.seed(12345)
    pairs = []
    for (a,b) in [(0,1),(1,2),(0,2),(Fraction(1,2),2),(-1,1),
                  (Fraction(1,4),Fraction(1,2)),(Fraction(1,4),1),
                  (Fraction(3,4),Fraction(7,4)),(-2,-1),(0,Fraction(1,8)),
                  (Fraction(5,2),3),(1,3),
                  (0,Fraction(1,2)),(Fraction(1,2),1),(Fraction(1,4),Fraction(3,4)),
                  (Fraction(1,3),Fraction(2,3))]:
        pairs.append((Fraction(a),Fraction(b)))
    cnt = 0
    while cnt < 150:
        x = Fraction(random.randint(0,12), 2**random.randint(0,5))
        y = Fraction(random.randint(0,12), 2**random.randint(0,5))
        a,b = (x,y) if x<y else (y,x)
        if a!=b: pairs.append((a,b)); cnt+=1
    bad=0
    for a,b in pairs:
        got = simplest_between(a,b)
        want = birthday_oracle(a,b)
        if got != want:
            bad+=1
            if bad<=15:
                print(f"MISMATCH ({a},{b}) got={got} ({birthday(got)}) oracle={want}"
                      f" ({birthday(want) if want is not None else '-'})")
    print(f"checked {len(pairs)} intervals, mismatches = {bad}")
    return bad

if __name__ == "__main__":
    import sys
    sys.exit(1 if main() else 0)
