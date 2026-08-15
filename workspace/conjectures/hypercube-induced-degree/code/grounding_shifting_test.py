"""Test candidate 1's load-bearing compression claim: does coordinate
shifting (compression of {0,1}^n toward initial segments) not-increase the
max internal degree D(S) of an induced subgraph Q_n[S]?

Standard shifting: for a coordinate i, shift S by replacing each vertex with
a 1 in coordinate i but x_{i+1..n}=0 by the same vertex with 0 in coordinate i
(if the latter is not already in S). This makes the family "initial-segment-
like" in the binary/numeric order. The candidate claims D(S) is monotone
(does not increase) under any such shift. If shifting can INCREASE D(S), the
claim is false.
"""
import itertools

def popcount(x): return bin(x).count("1")

def degree_in(n, S, v):
    return sum(1 for u in S if (u ^ v) and (u ^ v) & (u ^ v - 1) == 0)

def D(S, n):
    return max(degree_in(n, S, v) for v in S)

# standard i-th shift (Brualdi/compression): for coordinate i (0-indexed),
# vertices x with bit_i=1 and all bits < i zero get shifted down
def shift(S, n, i):
    S = set(S)
    changed = True
    while changed:
        changed = False
        for x in list(S):
            if (x >> i) & 1:
                # zero out bits strictly below i
                y = x & ~((1 << (i+1)) - 1)  # keep bits >= i+1, zero bits <= i except set bit i off
                # we want bit i and below all zero, keep higher bits
                keep = x & ~((1 << (i+1)) - 1)
                y = keep  # bit i is now 0 since (1<<(i+1))-1 masks bits 0..i
                if y not in S:
                    S.discard(x); S.add(y); changed = True
    return frozenset(S)

def test(n):
    verts = list(range(2**n))
    violations = 0
    tested = 0
    # sample random sets and all valid shifts
    import random
    random.seed(0)
    for _ in range(2000):
        k = random.randint(2**(n-1)+1, 2**n)
        S = frozenset(random.sample(verts, k))
        d0 = D(S, n)
        for i in range(n):
            S2 = shift(S, n, i)
            d1 = D(S2, n)
            tested += 1
            if d1 > d0:
                violations += 1
                if violations <= 5:
                    print(f"VIOLATION n={n} size={k} i={i} D before={d0} D after={d1}")
    print(f"n={n}: {tested} shift trials, {violations} violations of 'D not increased by shifting'")

for n in (3,4,5):
    test(n)
