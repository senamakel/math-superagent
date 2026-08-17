"""Test the conjecture: Psi(k) mod q is periodic in k, with period related to
lcm(ord_10(q), Pisano(q)), by scanning the factor sets.

For a modulus q, compute P(k)=Psi(k) mod q for k=1..N, find the smallest
period T (with a possible preperiod) and compare T to
lcm(ord_10(q), Pisano(q)) or its small multiples.
"""
import os, sys
from math import lcm

def factor_set(f, k):
    return {f[i:i+k] for i in range(len(f) - k + 1)}

def build_fib_word(L):
    a, b = "0", "01"
    while len(b) < L:
        a, b = b, b + a
    return b

def berlekamp_period_or_search(seq, N):
    # find smallest T such that seq[i]==seq[i+T] for all i, using window
    for T in range(1, N//2+1):
        if all(seq[i] == seq[i+T] for i in range(N - T)):
            return T
    return None

def ord10(q):
    if q % 2 == 0 or q % 5 == 0:
        return None
    # order of 10 mod q
    x = 10 % q
    order = 1
    while x != 1:
        x = (x * 10) % q
        order += 1
    return order

def pisano(q):
    a, b = 0, 1
    for t in range(1, 6*q+2):
        a, b = b, (a+b) % q
        if a == 0 and b == 1:
            return t
    return None

def psi_mod(f, N, q):
    out = []
    for k in range(1, N+1):
        fs = factor_set(f, k)
        assert len(fs) == k+1, (q,k,len(fs))
        P = sum(int(w)**2 for w in fs) % q
        out.append(P)
    return out

def main():
    mod = int(sys.argv[1])
    N = int(sys.argv[2])
    f = build_fib_word(3*N + 50)
    seq = psi_mod(f, N, mod)
    T = berlekamp_period_or_search(seq, N)
    o = ord10(mod) if mod % 2 and mod % 5 else None
    pi = pisano(mod)
    print(f"mod={mod}, N={N}")
    print(f"  ord_10={o}, Pisano={pi}")
    if o and pi:
        print(f"  lcm(ord_10,Pisano)={lcm(o,pi)}")
    print(f"  smallest pure period T in data = {T}")
    if T and o and pi:
        D = lcm(o, pi)
        print(f"  T mod D = {T % D} (0 => T divides D)")
        # also check T is a multiple of D
        print(f"  T/D = {T/D if D else None}")

main()
