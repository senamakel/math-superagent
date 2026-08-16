"""Verify: for uniform h, E[S(n,h)^2] = n-2, BY Walsh orthogonality (O'Donnell
fact: E[chi_A] = 1 iff A empty), AND directly by exhaustive enumeration at small n.

Direct: E[S^2] = (1/2^n) sum_h S(n,h)^2.
Walsh:   E[S^2] = #{ (d,d') : M_d △ M_d' = empty } = number of pairs with M_d = M_d'.
         Since M_d is injective in d, that count = (n-2).

Nonnegative control that the predicate can fail: replace E[chi_A]=1_{A empty}
with a wrong 1_{A empty OR |A|=1} and show the count changes.
"""
import sys
from lib.collapse import S2_char, S, downset

def popcount(x):
    return bin(x).count("1")

def main():
    for n in range(2, 11):
        # Direct enumeration (2^n strings)
        total = 0
        for h in range(1 << n):
            hl = [(h >> i) & 1 for i in range(n)]
            s = S(n, hl)
            total += s * s
        E_direct = total / (1 << n)

        # Walsh: count pairs (d,d') with M_d == M_d'
        ms = {d: downset(d, n) for d in range(2, n)}
        cnt = 0
        for d in range(2, n):
            for dp in range(2, n):
                if ms[d] == ms[dp]:
                    cnt += 1
        # injectivity check: are M_d all distinct?
        distinct = len(set(ms.values())) == len(ms)
        E_walsh = cnt  # = n-2 if injective

        # Negative control: wrong orthogonality, count pairs with |M_d△M_d'| in {0,1}
        neg = 0
        for d in range(2, n):
            for dp in range(2, n):
                if len(ms[d] ^ ms[dp]) <= 1:
                    neg += 1

        status = "OK" if abs(E_direct - E_walsh) < 1e-9 else "MISMATCH"
        print(f"n={n:2d} E_direct={E_direct:9.4f} E_walsh={E_walsh:3d} "
              f"n-2={n-2:2d} distinct={distinct} neg_ctrl={neg} -> {status}")

if __name__ == "__main__":
    main()
