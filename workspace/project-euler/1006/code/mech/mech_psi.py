"""Psi(k) by the mechanical-word (Sturmian) construction - exact arithmetic.

Verification gate for the mechanical route to PE1006.  The infinite Fibonacci
word S (limit of S_0 = 0, S_1 = 01, S_n = S_{n-1}S_{n-2}) is the characteristic
Sturmian word of slope alpha = 1/phi^2 = (3 - sqrt 5)/2.  For a rational slope
a = fib(n)/fib(n+2) (a continued-fraction convergent of alpha, q = fib(n+2)),
cut the circle R/Z at the k+1 points {-m*a mod 1 : m = 0..k}; the k+1 arcs so
obtained, read at their midpoints x with digits
    d_j(x) = floor(x + (j+1)a) - floor(x + ja),   j = 0..k-1,
are claimed to be exactly the k+1 distinct length-k factors of S (whenever the
denominator q > k, so all cut points are distinct and the cyclic order is the
right one).  Psi(k) = sum over these k+1 words of (decimal value)^2.

Two independent formulations of the same sum are computed and must agree:
  (A) arc midpoints directly (this is the source-backed construction);
  (B) left limits at the cut points: the value on the arc ending at the cut
      point -m*a equals v(-m*a - eps) as eps -> 0+.  In the telescoped form
          v(x) = floor(x+ka) - 10^(k-1) floor(x) + 9 sum_{l=1}^{k-1} 10^(k-1-l) floor(x+la),
      the left limit replaces floor((t-m)a - eps) by floor((t-m)a) - [t == m]
      (the floors jump by exactly 1 at x = -m*a only when t == m, since
      |t-m| <= k < q and gcd(p,q) = 1).
  The multisets of the k+1 values from (A) and (B) must also coincide.

Both use exact Fraction arithmetic; no floats anywhere.

Checks performed against three oracles:
  * code/brute.py functions (string factor extraction) for k = 1..50, exact;
  * code/out/psi_exact.txt (k = 1..25, exact big integers, produced by
    code/pattern_hunt/gen_sequences.py from long Fibonacci words);
  * code/out/psi_residues.txt (k = 1..400, mod M = 101001001, same generator).
Additionally, for k = 1..25 the slope q is varied over {smallest fib > k,
smallest fib > 2k+1, smallest fib > 5k}: all must give the same Psi, which
tests that the construction is insensitive to the rational approximation of
alpha (it converges to the irrational limit).
"""
from fractions import Fraction
import sys

M = 101001001


def fibs_upto(limit):
    """[0, 1, 1, 2, 3, 5, ...] with last element the smallest Fibonacci > limit."""
    f = [0, 1]
    while f[-1] <= limit:
        f.append(f[-1] + f[-2])
    return f


def slope_for(k, factor):
    """Rational slope a = fib(n)/fib(n+2) with fib(n+2) > factor*k.

    fib list is 0-based (fib(0)=0, fib(1)=1): if q = fib(idx), then p = fib(idx-2).
    """
    f = fibs_upto(factor * k)
    q = f[-1]
    p = f[-3] if len(f) >= 3 else 0
    return Fraction(p, q), q, p


def mech_psi(k, q=None, factor=1):
    """Psi(k) by the mechanical construction.  Returns (totalA, totalB, valsA, valsB)."""
    if q is None:
        a, q, p = slope_for(k, factor)
    else:
        # find p with a = p/q: p = fib at index (index_of_q - 2)
        f = fibs_upto(q)
        assert f[-1] == q, "q must be a Fibonacci number"
        p = f[-3]
        a = Fraction(p, q)
    assert q > k, "need denominator q > k for distinct cut points"

    # Cut points {-m*a mod 1 : m = 0..k}
    pts = sorted((Fraction(-m * p, q)) % 1 for m in range(k + 1))

    pw = [10 ** e for e in range(k + 1)]  # pw[e] = 10^e

    # (A) arc midpoints
    valsA = []
    for i in range(k + 1):
        c1 = pts[i]
        c2 = pts[(i + 1) % (k + 1)] if i < k else pts[0] + 1  # wrap arc
        xm = (c1 + c2) / 2
        if xm >= 1:
            xm -= 1
        # floors of xm + j*a for j = 0..k (precomputed; never on a cut point:
        # a midpoint of two consecutive cut points cannot itself be a cut point)
        fl = [((xm + Fraction(j) * a).numerator) // ((xm + Fraction(j) * a).denominator)
              for j in range(k + 1)]
        v = sum((fl[j + 1] - fl[j]) * pw[k - 1 - j] for j in range(k))
        valsA.append(v)

    # (B) left limits at the cut points, using the telescoped identity
    g = {t: ((Fraction(t) * a).numerator // (Fraction(t) * a).denominator)
         - (1 if t == 0 else 0) for t in range(-k, k + 1)}
    valsB = []
    for m in range(k + 1):
        v = g[k - m] - pw[k - 1] * g[-m] + 9 * sum(
            pw[k - 1 - l] * g[l - m] for l in range(1, k))
        valsB.append(v)

    return sum(v * v for v in valsA), sum(v * v for v in valsB), sorted(valsA), sorted(valsB)


def main():
    fails = []

    # --- brute.py oracle, k = 1..50, exact ---
    from brute import psi_of, fib_word
    print("== (1) mech_psi vs code/brute.py (string oracle), k = 1..50, exact ==")
    bad = 0
    for k in range(1, 51):
        b, _ = psi_of(fib_word(3 * k), k)
        tA, tB, vA, vB = mech_psi(k)
        ok = (tA == tB == b) and (vA == vB)
        if not ok:
            bad += 1
            print(f"    k={k}: MISMATCH brute={b} A={tA} B={tB} multiset_eq={vA==vB}")
    print(f"    k=1..50: all three agree and (A)==(B) multisets  ->  {bad == 0}")
    if bad:
        fails.append("brute k=1..50")

    # --- slope-insensitivity: k = 1..25 with q in {>k, >2k+1, >5k} ---
    print("== (2) slope approximation insensitivity, k = 1..25 ==")
    bad = 0
    for k in range(1, 26):
        base = mech_psi(k)[0]
        for factor in (2, 5):
            tA, tB, vA, vB = mech_psi(k, factor=factor)
            if tA != base or tA != tB or vA != vB:
                bad += 1
                print(f"    k={k} factor={factor}: MISMATCH base={base} got={tA}")
    print(f"    all q choices agree for k=1..25  ->  {bad == 0}")
    if bad:
        fails.append("slope sensitivity k=1..25")

    # --- recorded exact values k = 1..25 ---
    print("== (3) mech_psi vs code/out/psi_exact.txt, k = 1..25 ==")
    exact = {}
    with open("code/out/psi_exact.txt") as fh:
        for line in fh:
            kk, vv = line.split()
            exact[int(kk)] = int(vv)
    bad = 0
    for k in range(1, 26):
        tA, tB, vA, vB = mech_psi(k)
        if tA != exact[k] or tA != tB:
            bad += 1
            print(f"    k={k}: MISMATCH table={exact[k]} A={tA} B={tB}")
    print(f"    k=1..25 agree with recorded exact values  ->  {bad == 0}")
    if bad:
        fails.append("psi_exact k=1..25")

    # --- recorded residues k = 1..400 (minimal q = smallest fib > k) ---
    print("== (4) mech_psi vs code/out/psi_residues.txt, k = 1..400 (q minimal > k) ==")
    res = {}
    with open("code/out/psi_residues.txt") as fh:
        for line in fh:
            kk, vv = line.split()
            res[int(kk)] = int(vv)
    bad = 0
    for k in range(1, 401):
        tA, tB, vA, vB = mech_psi(k)
        if tA % M != res[k] or tA != tB or vA != vB:
            bad += 1
            if bad <= 5:
                print(f"    k={k}: MISMATCH table={res[k]} A={tA % M} B={tB % M} "
                      f"multiset_eq={vA == vB}")
    print(f"    k=1..400 agree with recorded residues, (A)==(B), multisets equal  ->  {bad == 0}")
    if bad:
        fails.append(f"psi_residues k=1..400 ({bad} mismatches)")

    print()
    print("== Summary ==")
    if fails:
        print("FAILURES:", fails)
        sys.exit(1)
    print("ALL CHECKS PASSED: mechanical construction reproduces Psi(k) exactly at "
          "every oracle-reachable k (brute string oracle k<=50, recorded exact k<=25, "
          "recorded residues k<=400), formulation (B) == formulation (A) in every case, "
          "and the result is insensitive to the rational slope approximant.")


if __name__ == "__main__":
    main()