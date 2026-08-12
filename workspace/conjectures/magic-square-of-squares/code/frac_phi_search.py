#!/usr/bin/env python3
"""Exact rational search over the e-independent difference set Phi.

Every d in S(e) (= AP differences through centre e^2) has the form
    d = e^2 * q,  q = 4mn(m^2-n^2)/(m^2+n^2)^2,  gcd(m,n)=1? (any m>n>=1),
where d/e^2 is a rational number in the UNIVERSAL set

    Phi = { 4mn(m^2-n^2)/(m^2+n^2)^2 : m > n >= 1 }

(proof: d in S(e) iff e = k(m^2+n^2), d = 4k^2 mn(m^2-n^2); so
d/e^2 = 4mn(m^2-n^2)/(m^2+n^2)^2, and e^2 q is an integer iff
(m^2+n^2) | e, since gcd(mn(m^2-n^2),(m^2+n^2)^2)=1.)

Hence the four-difference condition u, v, u+v, u-v in S(e) implies, dividing
by e^2:  q_u, q_v, q_u+q_v, |q_u-q_v|  all in Phi  (with q_u != q_v > 0).
This is a NECESSARY condition independent of e; a quadruple in Phi would
construct a genuine full nine-square magic square with centre
e = lcm of the denominators of q_u, q_v, q_u+q_v, q_u-q_v.

This program:
  [1] builds Phi(M) = distinct rational values with m <= M, exact Fractions;
  [2] counts |Phi(M)| for M = 10,20,40,60,80 (sequence);
  [3] searches for additive quadruples q1,q2,q1+q2,q1-q2 all in Phi;
  [4] searches for the weaker triple condition q1,q2,q1+q2 in Phi;
  [5] checks the 2-adic block: is every q in Phi == 0 mod 8?
  [6] if a quadruple is found, lifts it to (e,u,v) and verifies the
      resulting grid entry-by-entry with isqrt (full magic square of
      squares check).
"""
from fractions import Fraction
from math import gcd, isqrt
import time


def phi_set(M):
    out = set()
    for m in range(2, M + 1):
        m2 = m * m
        for n in range(1, m):
            num = 4 * m * n * (m2 - n * n)
            den = (m2 + n * n) ** 2
            g = gcd(num, den)
            out.add(Fraction(num // g, den // g))
    return frozenset(out)


def v2(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def lift_and_verify(q1, q2):
    """Given q1+q2, q1-q2, q1, q2 in Phi, construct the full solution."""
    from fractions import Fraction as F
    vals = [q1, q2, q1 + q2, abs(q1 - q2)]
    # centre e = lcm of denominators
    e = 1
    for v in vals:
        e = e * v.denominator // gcd(e, v.denominator)
    c = e * e
    u, v = c * q1, c * q2
    u, v = int(u), int(v)
    grid = [
        [c + u, c - u - v, c + v],
        [c - u + v, c, c + u - v],
        [c - v, c + u + v, c - u],
    ]
    ok_entries = all(x > 0 and isqrt(x) ** 2 == x for row in grid for x in row)
    sums = [sum(r) for r in grid] + \
           [grid[i][j] for j in (0, 1, 2) for i in (0, 1, 2)][::3] or []
    sums = [grid[0][0] + grid[1][0] + grid[2][0],
            grid[0][1] + grid[1][1] + grid[2][1],
            grid[0][2] + grid[1][2] + grid[2][2],
            grid[0][0] + grid[1][1] + grid[2][2],
            grid[0][2] + grid[1][1] + grid[2][0]]
    ok_magic = all(s == 3 * c for s in sums)
    distinct = len(set(x for row in grid for x in row)) == 9
    return e, u, v, grid, ok_entries, ok_magic, distinct


def main():
    t0 = time.time()
    sizes = []
    phis = {}
    for M in (10, 20, 40, 60, 80):
        phis[M] = phi_set(M)
        sizes.append(len(phis[M]))
    print("[1] |Phi(M)| distinct rational values, M = "
          "10,20,40,60,80:", sizes)

    for M in (40, 80):
        Phi = sorted(phis[M])
        Phiset = set(Phi)
        n = len(Phi)
        quad = []
        triples = 0
        t = time.time()
        for i in range(n):
            q1 = Phi[i]
            for j in range(i):
                q2 = Phi[j]
                if q1 + q2 in Phiset:
                    triples += 1
                    if q1 - q2 in Phiset:
                        quad.append((q1, q2))
                elif q1 - q2 in Phiset:
                    if q1 + q2 in Phiset:
                        triples += 1  # parity; count once below
        # recount triples cleanly
        triples = sum(1 for i in range(n) for j in range(i)
                      if Phi[i] + Phi[j] in Phiset)
        print(f"[2] Phi({M}): |Phi| = {n}; additive quadruples "
              f"(q1,q2,q1+q2,q1-q2 in Phi): {len(quad)}; "
              f"Phi-triples (q1,q2,q1+q2): {triples}; {time.time()-t:.1f}s")
        for q1, q2 in quad[:3]:
            e, u, v, grid, oe, om, od = lift_and_verify(q1, q2)
            print(f"    QUADRUPLE q1={q1} q2={q2}: e={e}, u={u}, v={v}, "
                  f"entries-all-squares={oe}, magic={om}, distinct={od}")
        if not quad:
            print("    -> no quadruple in Phi(M); the four-difference "
                  "condition fails already at the rational (e-free) level "
                  "for m,n <= M")

    # 2-adic block check
    Phi = phis[80]
    all_v2 = {v2(q.numerator) - v2(q.denominator) for q in Phi}
    print("[3] 2-adic valuations of q in Phi(80):", sorted(all_v2),
          " (all >= 3 means every q == 0 mod 8)")

    # distinctness of representation: how many (m,n) pairs give each q
    from collections import Counter
    rep = Counter()
    for m in range(2, 81):
        m2 = m * m
        for n in range(1, m):
            num = 4 * m * n * (m2 - n * n)
            den = (m2 + n * n) ** 2
            g = gcd(num, den)
            rep[Fraction(num // g, den // g)] += 1
    multi = {q: c for q, c in rep.items() if c > 1}
    print(f"[4] q in Phi(80) with >1 (m,n) representations: "
          f"{len(multi)} of {len(rep)}; max multiplicity "
          f"{max(rep.values())}; examples {list(multi.items())[:4]}")
    print(f"    total {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()