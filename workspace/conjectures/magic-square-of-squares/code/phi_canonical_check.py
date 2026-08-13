#!/usr/bin/env python3
"""Exact structural analysis of Phi = {4mn(m^2-n^2)/(m^2+n^2)^2 : m>n>=1}.

Conjecture under test (pattern_finder): f(t) = sin(4 arctan t) has the flip
symmetry  f(t) = f((1-t)/(1+t)), i.e. f(m,n) = f(m+n, m-n), and since sin
is 2-to-1 on (0,pi) this is the ONLY collision.  Hence the map

    (M,N) coprime, opposite parity, 1 <= N < M   |-->  f(M,N)

is a BIJECTION onto Phi.  Each orbit {(m,n), (m+n,m-n)} (halving the
same-parity mate) contains exactly one opposite-parity pair.

Consequent EXACT closed form (to be verified against direct enumeration):

    |Phi(B)|  =  #{opposite-parity coprime (M,N) : M <= B}
              =  sum_{M even <= B} phi(M)  +  (1/2) sum_{M odd <= B} phi(M)

  (M even: every reduced residue is odd -> phi(M) candidates.
   M odd : reduced residues pair as {N, M-N}, one even each -> phi(M)/2.)

Part B: the top of Phi(B) -- maxima of f over m <= B are attained at Pell
pairs (P_k, P_{k-1}) (best approximations of sqrt(2)-1), with the exact
identity  f(P_k, P_{k-1}) = 1 - 1/(P_{2k-1})^2  (conjectured; program-checks).

Every number printed is exact (integer arithmetic; halves are exact since
phi(M) is even for odd M > 1).
"""
from math import gcd
from collections import defaultdict


def f_reduced(m, n):
    """f(m,n) as reduced (num, den)."""
    num = 4 * m * n * (m * m - n * n)
    den = (m * m + n * n) ** 2
    g = gcd(num, den)
    return (num // g, den // g)


def totient_sieve(N):
    phi = list(range(N + 1))
    for p in range(2, N + 1):
        if phi[p] == p:                      # p prime
            for j in range(p, N + 1, p):
                phi[j] -= phi[j] // p
    return phi


def part_a(Bmax):
    """Verify the bijection and the closed form."""
    print(f"=== A. canonical-pair bijection, B <= {Bmax} ===")
    # group coprime pairs by value
    groups = defaultdict(list)
    for m in range(2, Bmax + 1):
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            groups[f_reduced(m, n)].append((m, n))
    bad = 0
    for val, pairs in groups.items():
        # each orbit must be {(M,N), (M+N,M-N)}, i.e. all pairs in the group
        # are {t, (1-t)/(1+t)}; flip partners:
        orbit = set()
        for (m, n) in pairs:
            m2, n2 = m + n, m - n
            g = gcd(m2, n2)
            m2, n2 = m2 // g, n2 // g          # primitive mate
            orbit.add((m, n))
            orbit.add((m2, n2))
        if set(pairs) != orbit or len(orbit) > 2:
            bad += 1
            if bad < 6:
                print(f"  COLLISION NOT ORBIT value={val}: {pairs}")
        # exactly one opposite-parity pair in the orbit
        opp = [p for p in orbit if (p[0] + p[1]) % 2 == 1]
        if len(opp) != 1:
            bad += 1
            print(f"  PARITY BAD value={val}: orbit {sorted(orbit)}")
    print(f"  orbits with wrong size/parity structure: {bad} "
          f"({len(groups)} distinct values) -> "
          f"{'PASS' if bad == 0 else 'FAIL'}")

    # closed form vs direct enumeration
    phi = totient_sieve(Bmax)
    cf = [0] * (Bmax + 1)
    for B in range(2, Bmax + 1):
        cf[B] = cf[B - 1] + (phi[B] if B % 2 == 0 else phi[B] // 2)
    direct = [0] * (Bmax + 1)
    seen = set()
    for m in range(2, Bmax + 1):
        for n in range(1, m):
            seen.add(f_reduced(m, n))
        direct[m] = len(seen)
    mism = [(B, direct[B], cf[B]) for B in range(2, Bmax + 1)
            if direct[B] != cf[B]]
    print(f"  |Phi(B)| direct vs totient-closed-form, B = 2..{Bmax}: "
          f"{'PASS' if not mism else 'FAIL at ' + str(mism[:5])}")
    print(f"  |Phi(150)| = {direct[150]} (recorded 4582), "
          f"|Phi(200)| = {direct[200]} (recorded 8156), "
          f"|Phi(400)| = {direct[400]} (recorded 32495)")
    return direct, cf


def part_b(seq, cf, BmaxDirect):
    """Top of Phi(B): maxima over m <= B and the Pell-pair identity."""
    print("\n=== B. maxima of Phi(B) (record pairs) ===")
    rec = []
    best = -1.0
    bestpair = None
    # recompute maxima exactly by ratio comparison via cross-multiplication
    bestnum, bestden = 0, 1
    for m in range(2, BmaxDirect + 1):
        for n in range(1, m):
            num, den = f_reduced(m, n)
            if num * bestden > bestnum * den:      # num/den > best
                bestnum, bestden = num, den
                bestpair = (m, n)
        # record when the pair's max-coordinate is m itself
        if bestpair and max(bestpair) == m:
            rec.append((m, bestpair, (bestnum, bestden)))
    top = [r for r in rec if r[0] <= 220]
    print("  record pairs (m, (m',n'), f value):")
    for m, pr, val in top:
        print(f"    m={m}: pair {pr} f={val[0]}/{val[1]}")

    print("\n=== C. Pell-pair identity f(P_k,P_{k-1}) = 1 - 1/(P_{2k-1})^2 ===")
    P = [0, 1]
    for k in range(2, 60):
        P.append(2 * P[k - 1] + P[k - 2])
    bad = 0
    for k in range(2, 30):
        m, n = P[k], P[k - 1]
        num, den = f_reduced(m, n)
        want_den = P[2 * k - 1] ** 2
        if not (den == want_den and num == want_den - 1):
            bad += 1
            print(f"  PELL FAIL k={k}: pair ({m},{n}) f={num}/{den}, "
                  f"want (P_{{2k-1}}^2-1)/P_{{2k-1}}^2 = "
                  f"{want_den - 1}/{want_den}")
    print(f"  identity f(P_k,P_{k-1}) = 1 - 1/P_{{2k-1}}^2, k=2..29: "
          f"{'PASS' if bad == 0 else 'FAIL'}")
    print(f"  note: record types for m -> the Pell hypotenuse values "
          f"P_{{2k-1}} = {[P[2*k-1] for k in range(2, 10)]}")

    print("\n=== D. extended |Phi(B)| via closed form (exact) ===")
    for B in (500, 800, 1000, 1200, 1500, 2000, 3000):
        lim = min(B, len(cf) - 1)
        print(f"    |Phi({B})| = {cf[lim] if lim == B else 'need bigger sieve'}")
    # head terms for the sequence tools
    print("\n=== E. |Phi(n)| n = 1..200 ===")
    print(",".join(str(cf[n]) if n >= 2 else "0" for n in range(1, 201)))


def main():
    Bmax = 400
    direct, cf = part_a(Bmax)
    # push the closed form further for part D
    phi = totient_sieve(3000)
    cf = [0] * 3001
    for B in range(2, 3001):
        cf[B] = cf[B - 1] + (phi[B] if B % 2 == 0 else phi[B] // 2)
    part_b(direct, cf, Bmax)


if __name__ == "__main__":
    main()