#!/usr/bin/env python3
"""code/lib/phi.py — exact arithmetic for the universal rational set Phi.

Phi = { f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2 : primitive m > n >= 1 }
     = { sin(4 arctan(n/m)) }  =  the universal set of centre-line AP ratios
       of a 3x3 magic square of squares (see problem.md, CONTEXT.md).

This is the single subject module for every program in code/phi_triple_variety/
(and anything else on this thread).  Everything is exact integer arithmetic;
no floats anywhere.

Key identities used throughout:
  * f depends only on the ratio t = n/m (homogeneous degree 0):
        f(t) = 4t(1-t^2)/(1+t^2)^2 = 1 - R(t)^2,  R(t) = (1-2t-t^2)/(1+t^2).
  * For q = f(m,n):  1 + q = (m^2+2mn-n^2)^2 / (m^2+n^2)^2  is a RATIONAL
    SQUARE.  This is a necessary (not sufficient) condition for q in Phi,
    and it gives a cheap pre-filter on candidate sums, since the membership
    test we use is the (authoritative, exact, uncapped) test:
        reduced q = A/B in Phi  <=>  integer s != 0 with s^2 = B^2 - A^2
                                     and (B+s)/(2B), (B-s)/(2B) both
                                     rational squares.
  * The record (largest) values of f are the Pell pairs:
        f(P_k, P_{k-1}) = 1 - 1/P_{2k-1}^2,  P = Pell numbers.
"""

from math import gcd, isqrt

__all__ = [
    "f_pair", "phi_pairs", "phi_value_set", "in_phi", "plus_one_is_square",
    "sum_in_phi_prefilter", "pell", "record_pell_pairs",
    "sqrt_ok", "rational_square",
]


def sqrt_ok(x):
    """Exact: is x a perfect square?  int only."""
    if type(x) is not int or x < 0:
        return False
    r = isqrt(x)
    return r * r == x


def rational_square(num, den):
    """Exact: is reduced-or-not fraction num/den a rational square?
    Checks num and den individually are perfect squares."""
    if num <= 0 or den <= 0:
        return False
    g = gcd(num, den)
    num //= g
    den //= g
    return sqrt_ok(num) and sqrt_ok(den)


def f_pair(m, n):
    """Reduced (num, den) of f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2.  Exact.
    Requires primitive-looking m > n >= 1 but works for any m > n > 0."""
    m2, n2 = m * m, n * n
    num = 4 * m * n * (m2 - n2)
    den = (m2 + n2) ** 2
    g = gcd(num, den)
    return (num // g, den // g)


def phi_pairs(M):
    """All reduced (num, den) f-values for primitive m > n >= 1, m <= M.
    A set (collapses equal values, e.g. flip orbits)."""
    out = set()
    for m in range(2, M + 1):
        m2 = m * m
        for n in range(1, m):
            num = 4 * m * n * (m2 - n * n)
            den = (m2 + n * n) ** 2
            g = gcd(num, den)
            out.add((num // g, den // g))
    return out


def phi_value_set(M):
    """Set of reduced (num, den) values in Phi with a representation m <= M."""
    return phi_pairs(M)


def in_phi(A, B):
    """THE authoritative exact membership test (uncapped representation).
    Reduced or not q = A/B in Phi?  A,B > 0.  Returns bool."""
    B0, A0 = B, A                  # keep order: B is the denominator
    d = B0 * B0 - A0 * A0
    if d < 0:
        return False
    s = isqrt(d)
    if s * s != d:
        return False
    if s == 0:
        return False               # q=1 not in Phi (t=tan(pi/8) irrational)
    for ss in (s, -s):
        np_, dp_ = B0 + ss, 2 * B0
        nm_, dm_ = B0 - ss, 2 * B0
        if np_ <= 0 or dp_ <= 0 or nm_ <= 0 or dm_ <= 0:
            continue
        g1 = gcd(np_, dp_)
        a1, b1 = np_ // g1, dp_ // g1
        g2 = gcd(nm_, dm_)
        a2, b2 = nm_ // g2, dm_ // g2
        if (sqrt_ok(a1) and sqrt_ok(b1)
                and sqrt_ok(a2) and sqrt_ok(b2)):
            return True
    return False


def in_phi_squares(A, B):
    """Fast EXACT membership via the verified closed form.

    For REDUCED 0 < A < B (gcd(A,B)=1):  A/B in Phi  <=>  B, B-A, B+A
    are all perfect squares.  Proven by algebra (both 1-q and 1+q are
    rational squares for every q in Phi, and reducedness collapses the
    rational-square test to the three integers being squares) and VERIFIED
    exactly against in_phi on every reduced fraction B <= 400 (0 mismatches)
    and on all members of Phi(m<=N) for N up to 400.

    If A,B are NOT reduced, reduce first (the caller must).
    """
    if A <= 0 or A >= B:
        return False
    r = isqrt(B - A)
    c = isqrt(B)
    d = isqrt(B + A)
    return (r * r == B - A) and (c * c == B) and (d * d == B + A)


def plus_one_is_square(q_nd):
    """Necessary condition for q in Phi: 1+q is a rational square.
    Input reduced (num, den).  Cheap pre-filter."""
    A, B = q_nd
    return rational_square(B + A, B)


def sum_in_phi_prefilter(q1, q2):
    """Cheap NECESSARY-condition test that q1+q2 MIGHT be in Phi.

    q1,q2 are reduced (num,den).  Returns (sum_nd, survive).

    For ANY q in Phi, both 1-q and 1+q are rational squares (since
    f = 1 - R^2 so 1-f = R^2, and 1+f = ((m^2+2mn-n^2)/(m^2+n^2))^2).
    Therefore if q1+q2 is to be in Phi, the SUM must satisfy BOTH
    1-(q1+q2) and 1+(q1+q2) rational squares, and 0 < q1+q2 < 1.
    These are necessary (never false-negative a candidate), cheap, and
    knock out ~all pairs in practice."""
    A1, B1 = q1
    A2, B2 = q2
    num = A1 * B2 + A2 * B1
    den = B1 * B2
    g = gcd(num, den)
    A3, B3 = num // g, den // g
    # q1+q2 must lie in (0,1) to be in Phi
    if A3 >= B3 or A3 <= 0:
        return (A3, B3), False
    return (A3, B3), (rational_square(B3 - A3, B3)
                      and rational_square(B3 + A3, B3))


# ---------------------------------------------------------------------------
# Pell record pairs
# ---------------------------------------------------------------------------


def pell(k):
    """k-th Pell number: P_1=1, P_2=2, P_3=5, P_4=12, ..."""
    if k <= 1:
        return 1
    p0, p1 = 1, 2
    for _ in range(2, k):
        p0, p1 = p1, 2 * p1 + p0
    return p1


def record_pell_pairs(k_min=2, k_max=7):
    """Record (max-f) pairs (m,n) = (P_k, P_{k-1}) for k=2..k_max, with
    f(m,n) = 1 - 1/P_{2k-1}^2.  Returns list of (k, m, n, f_pair)."""
    out = []
    for k in range(k_min, k_max + 1):
        m = pell(k)
        n = pell(k - 1)
        out.append((k, m, n, f_pair(m, n)))
    return out
