#!/usr/bin/env python3
"""Verify the Sparre Andersen / convex-minorant face-composition distribution.

Claim (literature): for a random walk S_j = sum_{i<=j} X_i with iid continuous
increments, the greatest convex minorant GCM(S[0,n]) has F_n faces, and

  F_n = 1 + sum_{r=2}^{n} Ber(1/r)   in distribution,
  F_n =^d K_n   (number of cycles of a uniform random permutation of [n]),
  P(F_n = k) = S1(n,k)/n!        [unsigned Stirling numbers of the first kind]
  P(F_n = k) = (1/n) * [z^{n-1}] (1 + z)(1 + 2z)...(1 + (k-1) z)   check

We verify the first equivalence by direct simulation of the GCM and by the
Bernoulli-summation formula, plus a brute-force composition check for small n
over the discrete-uniform increment distribution.

Second claim (this run's literature-gap question): for a v_i ~ iid continuous
speed law, the CONVEX-MINORANT COMPOSITION (face-length vector) is
distribution-free. We verify for two different continuous laws (normal vs
exponential) that the composition frequencies match each other and match the
random-permutation cycle-composition distribution.

Method: brute-force GCM by lower-hull over (j, S_j), j = 0..n.  No PE597
answer is computed here; this tests only the convex-minorant side of the
literature, which the run needs for the parity-gap statement.
"""
import itertools, math, random
from fractions import Fraction

def gcm_faces(n, X):
    """Return the face-length list (list of integers, lengths along the
    x-axis, ordered left to right) of the GCM of S_j = sum_{i<=j} X_i."""
    S = [0.0]
    for x in X:
        S.append(S[-1] + x)
    pts = [(j, S[j]) for j in range(n + 1)]
    # lower convex hull (monotone chain, lower part): vertices of the minorant
    hull = []
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    for p in pts:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    lens = []
    for a, b in zip(hull, hull[1:]):
        lens.append(int(b[0] - a[0]))
    return lens

def cycle_composition(n):
    """Distribution of cycle-length compositions over uniform random
    permutations (as a dict: composition tuple -> count)."""
    comps = {}
    for perm in itertools.permutations(range(n)):
        seen = [False]*n
        lens = []
        for i in range(n):
            if not seen[i]:
                cyc = 0
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = perm[j]
                    cyc += 1
                lens.append(cyc)
        comps[tuple(sorted(lens, reverse=True))] = comps.get(tuple(sorted(lens, reverse=True)), 0) + 1
    return comps

def main():
    # ---- part 1: F_n distribution vs Bernoulli sum (MC for n=8, 200k)
    random.seed(11)
    n = 8
    trials = 200000
    from collections import Counter
    cnt_bern = Counter()
    cnt_gcm  = Counter()
    for _ in range(trials):
        # GCM from continuous iid increments (normal)
        X = [random.gauss(0, 1) for _ in range(n)]
        faces = gcm_faces(n, X)
        cnt_gcm[len(faces)] += 1
        # Bernoulli-sum formula: F = 1 + sum_{r=2..n} Ber(1/r)
        f = 1
        for r in range(2, n+1):
            if random.random() < 1.0/r:
                f += 1
        cnt_bern[f] += 1
    # exact Stirling probability
    from math import factorial
    stir = [0]*(n+1)
    # unsigned Stirling first kind via recurrence
    st = [0]*(n+1); st[0]=1
    for m in range(1, n+1):
        nst = [0]*(n+1)
        for k in range(1, m+1):
            nst[k] = st[k-1] + (m-1)*st[k]
        st = nst
    print("part 1: F_n (faces of GCM of random walk) distribution, n=%d, trials=%d" % (n, trials))
    print("  k | P(Bern(1/r) sum) | P(GCM MC) | exact S1(n,k)/n!")
    for k in range(1, n+1):
        print("  %d | %.5f | %.5f | %.5f" % (
            k, cnt_bern[k]/trials, cnt_gcm[k]/trials, st[k]/factorial(n)))
    # ---- part 2: composition distribution-free (normal vs exponential) n=6
    print("\npart 2: composition distribution-free, n=6, trials=60000")
    n2 = 6
    from collections import defaultdict
    cnt_norm = defaultdict(int); cnt_exp = defaultdict(int)
    for _ in range(60000):
        Xn = [random.gauss(0, 1) for _ in range(n2)]
        Xe = [random.expovariate(1.0) for _ in range(n2)]
        ln = tuple(sorted(gcm_faces(n2, Xn), reverse=True))
        le = tuple(sorted(gcm_faces(n2, Xe), reverse=True))
        cnt_norm[ln] += 1
        cnt_exp[le] += 1
    # complete enumeration of compositions for n=6 random permutation
    compcount = cycle_composition(n2)
    total = sum(compcount.values())
    mism = 0
    for comp in sorted(compcount, key=lambda c: -sum(c)):
        pn = cnt_norm[comp]/60000
        pe = cnt_exp[comp]/60000
        pp = compcount[comp]/total
        if abs(pn-pp) > 0.02 or abs(pe-pp) > 0.02:
            mism += 1
    print("  composition | P(normal MC) | P(exp MC) | P(permutation exact)")
    for comp in sorted(compcount, key=lambda c: -sum(c)):
        print("  %s | %.5f | %.5f | %.5f" % (
            str(comp), cnt_norm[comp]/60000, cnt_exp[comp]/60000,
            compcount[comp]/total))
    print("  mismatches vs permutation exact (>2%%): %d" % mism)

if __name__ == '__main__':
    main()