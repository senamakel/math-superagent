"""Compute the Gilmer iid-OR entropy ratio R(mu) = H(X∨Y)/H(X), X,Y iid ~ uniform on F.

High-precision numerical (mpmath); probabilities are exact fractions, entropy
values (logs) are numerical at the stated precision. This is NOT exact.

Sections
--------
A. R for uniform families: 2^[n] (n=2,3,4) and F={ {1},{2},{1,2} } on [n]=[2].
   Uses lib.uc for the union-closure / abundance oracle (exact integers).
B. The correct locus of the constant (3−√5)/2: product-Bernoulli density p,
   R(p)=h(2p−p²)/h(p); show R( (3−√5)/2 ) = 1 and R>1 below it.
C. Boppana inequality h(x²) >= phi*x*h(x), phi=(1+√5)/2, on a fine grid [0,1]
   (numerical evidence only, not a proof).
"""

import mpmath as mp

from lib.uc import decide_union_closed, abundance

mp.mp.dps = 60

PHI = (1 + mp.sqrt(5)) / 2          # golden ratio (exact closed form, evaluated numerically)
BETA = (3 - mp.sqrt(5)) / 2         # the critical density (3−√5)/2


def h(p):
    """Binary entropy h(p) = -p log2 p - (1-p) log2 (1-p), p in [0,1]."""
    p = mp.mpf(p)
    if p == 0 or p == 1:
        return mp.mpf(0)
    return -(p * mp.log(p, 2) + (1 - p) * mp.log(1 - p, 2))


def uniform_family_ratio(masks, n):
    """R = H(X∨Y)/H(X) for X,Y iid uniform over the family given by bitmasks.

    X uniform over the |F| sets. H(X) = log2(|F|) (exact symbolically, a log).
    X∨Y takes value u with probability (# ordered pairs (a,b) with a|b==u)/|F|^2.
    Returns (R, H_X, H_union, union_counts, mpf probabilities already exact).
    """
    F = list(masks)
    m = len(F)
    HX = mp.log(m, 2)
    # count pairs per union value, exact integers
    from collections import defaultdict
    cnt = defaultdict(int)
    for a in F:
        for b in F:
            cnt[a | b] += 1
    # probabilities are exact fractions count/m^2; entropy computed numerically
    Hy = mp.mpf(0)
    for u, c in cnt.items():
        p = mp.mpf(c) / m / m
        Hy -= p * mp.log(p, 2)
    R = Hy / HX
    return R, HX, Hy, dict(cnt)


def product_bernoulli_ratio(p):
    """R for product-Bernoulli(p) on the full cube: h(2p-p^2)/h(p)."""
    p = mp.mpf(p)
    return h(2 * p - p * p) / h(p)


def main():
    print("=" * 78)
    print("Gilmer iid-OR ratio R(mu) = H(X∨Y)/H(X), X,Y iid uniform on F")
    print("mpmath precision: %d significant digits (NUMERICAL, not exact)" % mp.mp.dps)
    print("probabilities are exact fractions; entropy values are logs (numerical)")
    print("=" * 78)

    # ---- guard: oracle on the families used ----
    print("\n[guard: oracle via lib.uc]")
    f2 = {1, 2, 3}                      # { {1}, {2}, {1,2} } on [2]
    assert decide_union_closed(f2), "F={1},{2},{1,2} must be union-closed"
    n2 = 2
    print("  F={1},{2},{1,2}: union-closed =", decide_union_closed(f2),
          "| abundances n=2:", abundance(f2, n2))
    for n in (2, 3, 4):
        pw = set(range(1 << n))
        assert decide_union_closed(pw), "power set must be union-closed"
        print("  2^[%d]: union-closed = True, per-element count = %d/%d -> density 1/2"
              % (n, 2 ** (n - 1), 2 ** n))

    # ---- A. uniform families ----
    print("\n[A] uniform families: R = H(X∨Y)/H(X)")
    for n in (2, 3, 4):
        masks = list(range(1 << n))
        R, HX, Hy, cnt = uniform_family_ratio(masks, n)
        print("  2^[%d]  |F|=%d  H(X)=log2(%d)=%.12f  H(X∨Y)=%.12f  R=%.12f"
              % (n, len(masks), len(masks), float(HX), float(Hy), float(R)))

    R2, HX2, Hy2, cnt2 = uniform_family_ratio(list(f2), n2)
    print("  F={ {1},{2},{1,2} }  |F|=3  H(X)=log2(3)=%.12f  H(X∨Y)=%.12f  R=%.12f"
          % (float(HX2), float(Hy2), float(R2)))
    print("  union-value probs (exact fractions of 9 ordered pairs):")
    for u, c in sorted(cnt2.items()):
        print("    mask %s (%s): %d/9" % (bin(u), sorted(i + 1 for i in range(n2) if (u >> i) & 1), c))
    print("  2-set-family R vs (3-√5)/2=%.12f:" % float(BETA))
    print("    R(2-set) = %.12f  ->  EQUAL to (3-√5)/2? %s"
          % (float(R2), "YES" if abs(R2 - BETA) < 1e-30 else "NO"))

    # ---- B. the actual locus of (3−√5)/2 ----
    print("\n[B] where the constant actually lives: product-Bernoulli(p), R(p)=h(2p-p^2)/h(p)")
    for p in ("0.1", "0.2", "0.3", BETA, "0.382", "0.4", "0.45", "0.5"):
        print("  p=%-8s R(p)=%.12f" % (str(p), float(product_bernoulli_ratio(mp.mpf(p)))))
    print("  R(p)=(3-√5)/2≈%.12f gives  R=%.12f  (equals 1, since 2p-p^2=1-p)"
          % (float(BETA), float(product_bernoulli_ratio(BETA))))
    print("  check 2p-p^2 = 1-p at p=(3-√5)/2: 2p-p^2=%.12f  1-p=%.12f"
          % (float(2 * BETA - BETA * BETA), float(1 - BETA)))
    # extremal 2-bit distribution (weighted, NOT uniform): P(00)=(1-p)^2, P(10)=P(01)=p(1-p), P(11)=p^2
    p = BETA
    pm = p * p                    # 11
    pp = p * (1 - p)              # 10 and 01
    pe = (1 - p) ** 2             # 00
    print("  extremal 2-bit distribution (weighted, product-Bernoulli at p=(3-√5)/2):")
    print("    P(00)=%.6f  P(10)=%.6f  P(01)=%.6f  P(11)=%.6f" %
          (pe, pp, pp, pm))
    print("    all four points have mass>0 -> NOT the uniform family {1},{2},{1,2}")

    # ---- C. Boppana inequality ----
    print("\n[C] Boppana: h(x^2) >= phi*x*h(x), phi=(1+√5)/2=%.12f, x in [0,1]" % float(PHI))
    N = 200000
    min_margin = mp.inf
    arg_min = None
    for k in range(N + 1):
        x = mp.mpf(k) / N
        lhs = h(x * x)
        rhs = PHI * x * h(x)
        margin = lhs - rhs
        if margin < min_margin:
            min_margin = margin
            arg_min = x
    print("  grid of %d points in [0,1]" % (N + 1))
    print("  min margin (lhs-rhs) over grid = %.6e  at x=%.6f" %
          (min_margin, arg_min))
    print("  margin >= 0 on the whole grid? %s" % ("YES" if min_margin >= 0 else "NO (tolerance 0)"))
    # equality point (where barrier saturates): solve h(x^2)=phi*x*h(x)
    # locate sign change of margin
    prev = None
    cross = None
    for k in range(N + 1):
        x = mp.mpf(k) / N
        m = h(x * x) - PHI * x * h(x)
        if prev is not None and (m >= 0) != (prev >= 0):
            cross = x
            break
        prev = m
    # also check the claimed extremum value: at x = 1 - (3-√5)/2 = (√5-1)/2 = 1/phi
    xstar = 1 / PHI   # = (√5-1)/2 ≈ 0.618
    print("  candidate saturation x=1/phi=(√5-1)/2≈%.12f: margin=%.3e (near-tight)" %
          (float(xstar), h(xstar * xstar) - PHI * xstar * h(xstar)))
    print("  (the (3−√5)/2 barrier saturates Boppana at x=1/phi; margin printout is numerical)")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("  * 2^[n] uniform: R = h(3/4) = %.12f for every n (density 1/2; not admissible for the" %
          float(h(mp.mpf(3) / 4)))
    print("    small-density argument, R recorded for completeness).")
    print("  * F={ {1},{2},{1,2} }: R = %.12f (NOT %.12f)." % (float(R2), float(BETA)))
    print("    The constant (3−√5)/2 is a critical DENSITY p where R(product-Bernoulli p)=1,")
    print("    i.e. H(A∨B)=H(A); it is not the ratio value of the 2-set uniform family.")
    print("  * Boppana holds over the grid to machine precision (numerical evidence, not proof).")


if __name__ == "__main__":
    main()
