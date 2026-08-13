#!/usr/bin/env python3
"""|Phi(M)| = number of distinct rational values f(m,n) for m>n>=1, m<=M.
Emits the sequence at M = 10,20,...,150 (and a couple further points)."""
from math import gcd

def phi_count(M):
    out = set()
    for m in range(2, M+1):
        m2 = m*m
        for n in range(1, m):
            num = 4*m*n*(m2-n*n)
            den = (m2+n*n)**2
            g = gcd(num,den)
            out.add((num//g, den//g))
    return len(out)

if __name__ == "__main__":
    vals = []
    for M in range(10, 151, 10):
        vals.append(phi_count(M))
    print("|Phi(M)| M=10..150 step10:", ",".join(map(str,vals)))
