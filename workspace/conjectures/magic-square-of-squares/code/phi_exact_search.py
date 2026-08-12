#!/usr/bin/env python3
"""EXACT, uncapped additive-chain search in the universal difference set Phi.

Phi = { f(n/m) : m > n >= 1 }  with  f(t) = 4t(1-t^2)/(1+t^2)^2 = sin(4 arctan t).

The four-difference condition (u,v,u+v,u-v in S(e)) implies, dividing by e^2:
    q1 = u/e^2, q2 = v/e^2, q1+q2, |q1-q2|  all in Phi     (q1 != q2 > 0)
and a quadruple in Phi LIFTS to a genuine full magic square of squares with
centre e = lcm(m_i^2+n_i^2) over the four representations.  Similarly a
triple q1,q2,q1+q2 in Phi lifts to a magic square with 7 square entries.
So Phi-triple/quadruple existence is a NECESSARY condition for the open
problem, and a hit would CONSTRUCT a solution.

Membership test (exact, no cap on the representing pair):
    r = A/B (reduced) is in Phi
        <=> exists integer s with s^2 = B^2 - A^2     (s = cos(4 theta))
            and (B+s)/(2B), (B-s)/(2B) are both rational squares
Proof: r = 2XY with X = 2t/(1+t^2), Y = (1-t^2)/(1+t^2) on the unit circle;
X^2+Y^2=1 and 2XY=r give s = X^2-Y^2, s^2 = 1-r^2, X^2 = (1+s)/2, and t
rational iff (X,Y) rational iff both (1±s)/2 rational squares; then
t = X/(1+Y) in (0,1).

Program:
  [1] |Phi(M)| for M = 10..150 (sequence).
  [2] exact triple search: q1>q2>0 in Phi(M), q1+q2 <= 1, test q1+q2 in Phi
      (uncapped).  Report all hits (expected: none for M up to chosen cap).
  [3] exact quadruple search: additionally test q1-q2 in Phi.
  [4] any hit -> lift to (e,u,v) and verify the full grid with isqrt.
"""
from math import gcd, isqrt
from fractions import Fraction
import time


def f_frac(m, n):
    num = 4 * m * n * (m * m - n * n)
    den = (m * m + n * n) ** 2
    g = gcd(num, den)
    return Fraction(num // g, den // g)


def phi_set(M):
    out = set()
    for m in range(2, M + 1):
        for n in range(1, m):
            out.add(f_frac(m, n))
    return out


def in_phi(r):
    """Exact membership: r = A/B (Fraction) in Phi?  Unbounded representation."""
    A, B = r.numerator, r.denominator
    # s^2 = B^2 - A^2
    d = B * B - A * A
    if d < 0:
        return False
    s = isqrt(d)
    if s * s != d:
        return False
    if s == 0:
        # r = 1: f(t)=1 needs t = tan(pi/8) irrational -> r=1 not in Phi;
        # but r < 1 strictly in our uses (q in (0,1)); handle safely.
        return False
    for ss in (s, -s):
        num_p, den_p = B + ss, 2 * B
        num_m, den_m = B - ss, 2 * B
        if num_p <= 0 or den_p <= 0 or num_m <= 0 or den_m <= 0:
            continue
        g1 = gcd(num_p, den_p)
        a1, b1 = num_p // g1, den_p // g1
        g2 = gcd(num_m, den_m)
        a2, b2 = num_m // g2, den_m // g2
        if (isqrt(a1) ** 2 == a1 and isqrt(b1) ** 2 == b1
                and isqrt(a2) ** 2 == a2 and isqrt(b2) ** 2 == b2):
            return True
    return False


def verify_membership_samples():
    """Sanity: in_phi agrees with direct f(n/m) evaluation on a sample,
    and agrees with brute enumeration for all r = f(m,n), m,n <= 40."""
    bad = 0
    # (a) all values from pairs m,n <= 40 must test in
    for m in range(2, 41):
        for n in range(1, m):
            r = f_frac(m, n)
            if not in_phi(r):
                bad += 1
                print(f"  FALSE NEGATIVE r={r} from m={m},n={n}")
    # (b) random rationals with denominators <= 200 must test out unless
    # actually representable (compare against brute enumeration to 200)
    import random
    rng = random.Random(7)
    brute = phi_set(200)
    for _ in range(5000):
        t = Fraction(rng.randint(1, 199), rng.randint(2, 200))
        if t >= 1:
            continue
        r = f_frac(t.denominator, t.numerator)  # f(n/m) with m>n
        # r is obviously in Phi; instead test a random rational q:
    # (b') random reduced fractions A/B with B <= 300: compare in_phi
    # against f-values with m <= 300 (the only possible small preimages)
    brute300 = phi_set(300)
    for _ in range(4000):
        A = rng.randint(1, 299)
        B = rng.randint(max(2, A + 1), 300)
        if gcd(A, B) != 1:
            continue
        r = Fraction(A, B)
        got = in_phi(r)
        want = r in brute300
        if got != want:
            bad += 1
            if bad < 6:
                print(f"  DISAGREE r={r}: in_phi={got} brute300={want}")
    print(f"[verify] membership test vs brute: "
          f"{'PASS' if bad == 0 else str(bad) + ' FAILS'}")
    return bad == 0


def main():
    t0 = time.time()
    ok = verify_membership_samples()
    if not ok:
        print("membership test broken — aborting search")
        return

    sizes = []
    phis = {}
    for M in (10, 20, 40, 60, 80, 100, 120, 150):
        phis[M] = phi_set(M)
        sizes.append(len(phis[M]))
    print("[1] |Phi(M)| M=10,20,40,60,80,100,120,150:",
          ",".join(str(x) for x in sizes))

    M = 150
    Phi = sorted(phis[M])
    Phiset = set(Phi)
    n = len(Phi)
    print(f"    Phi(150): {n} values, min {Phi[0]} max {Phi[-1]}")

    t = time.time()
    triples = []
    quads = []
    tested = 0
    for i in range(n):
        q1 = Phi[i]
        for j in range(i):
            q2 = Phi[j]
            rp = q1 + q2
            if rp >= 1:
                continue
            tested += 1
            if in_phi(rp):
                triples.append((q1, q2, rp))
                rm = q1 - q2
                if in_phi(rm):
                    quads.append((q1, q2, rp, rm))
    print(f"[2] exact triple search over Phi(150) pairs with sum<1 "
          f"({tested} pairs): triples found: {len(triples)}")
    for q1, q2, rp in triples[:5]:
        print(f"    TRIPLE q1={q1} q2={q2} q1+q2={rp}")
    if not triples:
        print("    no additive triple q1+q2 in Phi — the necessary "
              "condition already fails at the rational level for all "
              f"q1,q2 from m,n <= 150, with the third term UNBOUNDED")
    print(f"[3] quadruples among them: {len(quads)}", )
    for q1, q2, rp, rm in quads[:5]:
        print(f"    QUADRUPLE q1={q1} q2={q2} sum={rp} diff={rm}")
    print(f"    {time.time()-t:.1f}s")

    # lift + verify any triple (constructs a 7-square magic grid) or quad
    for q1, q2, rp in (triples + [(a, b, c) for a, b, c, _ in quads]):
        pass  # handled below only if hits exist
    if triples:
        q1, q2, rp = triples[0]
        # representations: need (m,n) for q1, q2, rp
        reps = {}
        target = [q1, q2, rp]
        for m in range(2, 10000):
            m2 = m * m
            for nn in range(1, m):
                r = f_frac(m, nn)
                if r in target and r not in reps:
                    reps[r] = (m, nn)
            if len(reps) == len(target):
                break
        e = 1
        for r in target:
            m3, n3 = reps[r]
            e = e * (m3 * m3 + n3 * n3) // gcd(e, m3 * m3 + n3 * n3)
        c = e * e
        u, v = c * q1, c * q2
        u, v = int(u), int(v)
        grid = [
            [c + u, c - u - v, c + v],
            [c - u + v, c, c + u - v],
            [c - v, c + u + v, c - u],
        ]
        entries = [x for row in grid for x in row]
        sq = all(x > 0 and isqrt(x) ** 2 == x for x in entries)
        distinct = len(set(entries)) == 9
        sums = [sum(row) for row in grid]
        sums += [grid[0][j] + grid[1][j] + grid[2][j] for j in range(3)]
        sums += [grid[0][0] + grid[1][1] + grid[2][2],
                 grid[0][2] + grid[1][1] + grid[2][0]]
        magic = all(s == 3 * c for s in sums)
        print(f"[4] LIFT of first triple: e={e}, u={u}, v={v}, grid rows "
              f"{[row[:3] for row in grid]}")
        print(f"    all squares: {sq}, distinct: {distinct}, magic: {magic}")
    print(f"    total {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()