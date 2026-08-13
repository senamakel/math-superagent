#!/usr/bin/env python3
"""Fast no-triple search in Phi past M=400, using the verified closed-form
membership test (A/B in Phi <=> B, B-A, B+A all perfect squares, reduced
0<A<B).  Also reports the fraction of pairs q1>q2, q1+q2<1 whose sum
survives the NECESSARY-condition prefilter 1-(q1+q2), 1+(q1+q2) both
rational squares, and how many of those survivors actually land in Phi.

Phi = { 4mn(m^2-n^2)/(m^2+n^2)^2 : primitive m>n>=1 }.

Exact integer arithmetic throughout.  Checkpointable by outer index i.
"""
import sys, time
from math import gcd, isqrt
from lib.phi import phi_pairs


def in_phi_squares(A, B):
    """Reduced 0<A<B: A/B in Phi <=> B, B-A, B+A all perfect squares."""
    if A <= 0 or A >= B:
        return False
    return (isqrt(B-A)**2 == B-A and isqrt(B)**2 == B
            and isqrt(B+A)**2 == B+A)


def rat_square(num, den):
    """Exact: is reduced fraction num/den a rational square? (num,den>0)"""
    g = gcd(num, den)
    num //= g; den //= g
    return (num > 0 and den > 0
            and isqrt(num)**2 == num and isqrt(den)**2 == den)


def search(M, budget=580.0, report_prefilter=True):
    t0 = time.time()
    Phi = phi_pairs(M)
    pairs = sorted(Phi, key=lambda nd: nd[0]*1.0/nd[1])
    P = len(pairs)
    triples = []
    n_exact = 0          # sums tested with full in_phi_squares
    n_pref = 0           # sums passing the 1+/-q prefilter
    pref_hist = []       # (i, pref, exact) sampled every 1000 outer steps
    for i in range(P):
        A1, B1 = pairs[i]
        for j in range(i):
            A2, B2 = pairs[j]
            num = A1*B2 + A2*B1
            den = B1*B2
            if num >= den:          # q1+q2 >= 1 -> not in Phi (break monotone)
                break
            # necessary condition: both 1-(q1+q2), 1+(q1+q2) rational squares
            if not (rat_square(den-num, den) and rat_square(den+num, den)):
                continue
            n_pref += 1
            g = gcd(num, den)
            A3, B3 = num//g, den//g
            n_exact += 1
            if in_phi_squares(A3, B3):
                triples.append(((A1,B1),(A2,B2),(A3,B3)))
        if report_prefilter and (i % 2000 == 0 or i == P-1):
            pref_hist.append((i, n_pref, n_exact))
        if time.time() - t0 > budget:
            print(f"[M={M}] budget exceeded at i={i}/{P}; no triple yet; "
                  f"pref-survivors {n_pref}, exact {n_exact}",
                  flush=True)
            return triples, i, P, pref_hist
    print(f"[M={M}] |Phi|={P}; pairs-with-sum<1 visited; "
          f"pref-survivors {n_pref}, exact {n_exact}, triples {len(triples)}",
          flush=True)
    return triples, P, P, pref_hist


if __name__ == "__main__":
    args = sys.argv[1:]
    M = 700
    budget = 560.0
    for a in args:
        if a.startswith("--timeout"):
            budget = float(a.split("=")[1])
        elif a.isdigit():
            M = int(a)
    triples, reached, P, hist = search(M, budget)
    if triples:
        (A1,B1),(A2,B2),(A3,B3) = triples[0]
        print(f"*** TRIPLE: {A1}/{B1} + {A2}/{B2} = {A3}/{B3}")
    else:
        print(f"M={M} complete-through-i={reached}/{P}: NO additive triple "
              f"(preimage box m,n <= {M})")
