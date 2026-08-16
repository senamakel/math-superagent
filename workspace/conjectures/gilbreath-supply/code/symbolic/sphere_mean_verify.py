"""Verify the sphere-mean Krawtchouk formula for E_Sw[nu2].

Claim (G-sphere-mean):
  E_{S_w}[nu2(h)] = sum_{d=2}^{n-1} P_d
  P_d = (1/2)(1 - K_w(m_d; n)/C(n,w)),   m_d = 2^popcount(d)
  K_w(m;n) = sum_{j=0..w} (-1)^j C(m,j) C(n-m, w-j)

Derivation to check:
  #{h in S_w : XOR over fixed m-subset A = 1} = (C(n,w) - K_w(m;n))/2
  via  sum_{h in S_w} (-1)^{sum_{j in A} h_j} = K_w(m;n)  (Krawtchouk eval)
  and P[X odd] = (1 - E[(-1)^X])/2.

Brute-force oracle: enumerate S_w, but nu2 evaluated directly.
"""
import itertools
from math import comb
from fractions import Fraction


def kraw(w, m, n):
    """K_w(m;n) = sum_{j=0..w} (-1)^j C(m,j) C(n-m, w-j)."""
    return sum((-1) ** j * comb(m, j) * comb(n - m, w - j) for j in range(w + 1))


def popcount(x):
    return bin(x).count("1")


def fold_cells(n):
    """Return m_d = 2^popcount(d) for each d in [2, n-1]."""
    return {d: 2 ** popcount(d) for d in range(2, n)}


def nu2_brute(h, n):
    """nu2(h) = #{d in [2,n-1] : XOR over submasks o of d of h[n-1-d+o] = 1}.

    h is an integer bitmask of length n (bit j = h[j]).
    """
    cnt = 0
    for d in range(2, n):
        x = 0
        for o in range(0, d + 1):
            if (o & d) == o:  # o is submask of d
                x ^= (h >> (n - 1 - d + o)) & 1
        cnt += x
    return cnt


def check_case(n, w):
    """Enumerate S_w, compute true mean E[nu2], compare to formula mean."""
    cells = fold_cells(n)
    formula_mean = Fraction(0)
    for d in range(2, n):
        md = cells[d]
        Pd = Fraction(1, 2) * (Fraction(1) - Fraction(kraw(w, md, n), comb(n, w)))
        formula_mean += Pd
    # brute force
    tot = 0
    count = 0
    for combo in itertools.combinations(range(n), w):
        h = 0
        for j in combo:
            h |= 1 << j
        tot += nu2_brute(h, n)
        count += 1
    brute_mean = Fraction(tot, count)
    return formula_mean, brute_mean, cells


if __name__ == "__main__":
    # The two anchoring checks from the task
    for (n, w) in [(4, 1), (8, 3)]:
        fm, bm, cells = check_case(n, w)
        print(f"n={n} w={w}")
        print(f"  cells m_d = {cells}")
        print(f"  formula E[nu2] = {fm} = {float(fm)}")
        print(f"  brute   E[nu2] = {bm} = {float(bm)}")
        print(f"  n-2 (max cells) = {n-2}   nu2/n = {float(fm)/n}")
        print(f"  MATCH: {fm == bm}")
        print()

    # Exhaustive sweep n=3..16 all w, formula vs brute
    print("Exhaustive sweep n=3..16, all w:")
    bad = []
    for n in range(3, 17):
        for w in range(0, n + 1):
            fm, bm, _ = check_case(n, w)
            if fm != bm:
                bad.append((n, w, fm, bm))
    if not bad:
        print("  ALL n in 3..16, ALL w: formula == brute EXACTLY")
    else:
        for b in bad:
            print("  MISMATCH", b)
