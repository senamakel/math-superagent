#!/usr/bin/env python3
"""code/phi_triple_variety/ratio_search.py — (A) closed-form ratio search.

Search for an additive triple q1, q2, q1+q2 (q1>q2>0) all in Phi, using the
VERIFIED closed-form membership test  A/B in Phi  <=>  B, B-A, B+A all
perfect squares (reduced 0<A<B).  Exactly equivalent to the authoritative
uncapped in_phi (verified on every reduced fraction B<=400), but is three
isqrt calls, so the search pushes well past the prior m,n<=400 bound.

Pair loop exploits value order: pairs sorted ASCENDING by value; for fixed
larger q1=pairs[i], q2 ranges over pairs[0..i) ascending, so sum grows
monotonically in j and the loop breaks as soon as q1+q2 >= 1.  This avoids
visiting the [1,2) tail of sums entirely, so the cost is ~the number of
pairs with sum < 1 (about 1/4 of all pairs for these values) not all pairs.

Fully exact integer arithmetic.  Checkpointed: pass M and a resume outer
index; deterministic ordering makes a resumed run revisit i<resume cheaply.

Usage: python3 code/phi_triple_variety/ratio_search.py M [resume] [--timeout S]
"""
import sys
import time
from math import gcd, isqrt
from lib.phi import phi_pairs, in_phi_squares


def search(M, resume=0, budget=580.0):
    t0 = time.time()
    Phi = phi_pairs(M)
    pairs = sorted(Phi, key=lambda nd: nd[0] * 1.0 / nd[1])
    P = len(pairs)
    triples = []
    n_exact = 0
    reached = resume
    for i in range(resume, P):
        A1, B1 = pairs[i]
        B1B2_prod = B1
        for j in range(i):
            A2, B2 = pairs[j]
            # sum >= 1  <=>  A1*B2 + A2*B1 >= B1*B2 ; since B2 (and A2) grow
            # with j (ascending value), the sum is monotone in j -> break.
            if A1 * B2 + A2 * B1 >= B1 * B2:
                break
            g = gcd(A1 * B2 + A2 * B1, B1 * B2)
            num = (A1 * B2 + A2 * B1) // g
            den = (B1 * B2) // g
            n_exact += 1
            if in_phi_squares(num, den):
                triples.append(((A1, B1), (A2, B2), (num, den)))
            if time.time() - t0 > budget:
                reached = i
                print(f"[M={M}] budget exhausted at outer i={i}/{P} "
                      f"(resume {i})", flush=True)
                return triples, reached, P
        reached = i + 1
    print(f"[M={M}] |Phi|={P} exact tests: {n_exact} triples: {len(triples)} "
          f"reached-i={reached}/{P} {time.time()-t0:.0f}s", flush=True)
    return triples, reached, P


def main():
    args = sys.argv[1:]
    nums = [a for a in args if a.lstrip('-').isdigit() and not a.startswith('--')]
    budget = 580.0
    for a in args:
        if a.startswith("--timeout"):
            budget = float(a.split("=")[1])
    M = int(nums[0]) if nums else 600
    resume = int(nums[1]) if len(nums) >= 2 else 0
    print(f"M={M} resume_i={resume} budget={budget:.0f}s", flush=True)
    triples, reached, P = search(M, resume, budget)
    if triples:
        (A1, B1), (A2, B2), (A3, B3) = triples[0]
        print(f"  *** TRIPLE at M={M}: {A1}/{B1}+{A2}/{B2}={A3}/{B3}")
    else:
        print(f"  M={M}: no triple through outer-i {reached}/{P}")


if __name__ == "__main__":
    main()
