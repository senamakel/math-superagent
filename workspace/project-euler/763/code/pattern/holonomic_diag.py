# Diagnostic holonomic scan: see WHY each fit fails and find the first
# non-integer/pole step. Wider order/degree range.
from sympy import Rational, Matrix, symbols
from lib.holonomic import fit

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
     514419, 1749267, 5949063]
NTERM = len(D)
n = symbols('n')

def first_failure(m, d, sol):
    seq = list(D)
    for Ncur in range(0, 101):
        if Ncur + m <= len(seq)-1:
            continue
        if Ncur + m > len(seq):
            return None, seq   # done
        num = sum(sum(sol[j*(d+1)+t]*(Ncur**t) for t in range(d+1))*Rational(seq[Ncur+j]) for j in range(m))
        den = sum(sol[m*(d+1)+t]*(Ncur**t) for t in range(d+1))
        if den == 0:
            return f"pole at N={Ncur}", seq
        val = -num/den
        if val.denominator != 1:
            return f"non-int at N={Ncur}: {val}", seq
        seq.append(val)
    return None, seq

for m in range(1, 9):
    for d in range(1, 6):
        ns = fit(m, d)
        if not ns:
            continue
        # look at first nullspace vector
        sol = ns[0]
        fail, seq = first_failure(m, d, sol)
        # count how many nullspace dims
        print(f"m={m} d={d}: nulls={len(ns)} firstfail={fail}")
        if fail is None:
            d20 = seq[20]; d100m = seq[100]%10**9
            print(f"   !! extends: D20={d20} match={d20==9204559704}, D100mod={d100m} match={d100m==780166455}")
            for j in range(m+1):
                pj = sum(sol[j*(d+1)+t]*n**t for t in range(d+1))
                print(f"      p_{j}={pj}")
