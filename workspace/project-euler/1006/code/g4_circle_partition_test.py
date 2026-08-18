"""Executable bounded test for the circle-partition / interval-indicator route to G4.

Two deliverables in one file:

  PART 1 (correctness gate).  The exact reduction.  With slope a = p/q a
  Fibonacci convergent of 1/phi^2, the k+1 factors are read on the k+1 arcs
  cut by the orbit points {x_m = frac(-m a) : 0 <= m <= k}.  Each digit is an
  interval indicator on R/Z, so with w_j = 10^(k-1-j):

      Psi(k) = sum_{j,l=0}^{k-1} w_j w_l * C_k(j,l),
      C_k(j,l) = #{ m : d_j(x_m) = d_l(x_m) = 1 }.

  Every C_k(j,l) is an exact orbit count in an interval intersection, i.e. a
  difference of two floor-counts for rational slope (a finite sum of floor
  sums after sorting the cut points).  The test verifies this expansion
  against a direct arc-midpoint computation (independent implementation) for
  every k <= bound, and prints the two official anchors Psi(3) = 20302 and
  Psi(10) mod 101001001 = 10699667 as self-checks.

  PART 2 (bounded-state probe).  The G4 question is whether the family
  {C_k(j,l)} collapses to a fixed number of distinct rows/values independent
  of k (which is what a fixed-dimensional O(log k) aggregate would need).
  The test records, for each k, the number of distinct correlation rows and
  distinct pair values, and compares growth.  Prior work establishes the
  Toeplitz collapse ONLY at k = F_n - 1; this probe measures the general-k
  departure.

Run:   python3 code/g4_circle_partition_test.py [bound]
Exit:  0 if the expansion gate passes for all k <= bound (verdict line
       prints the bounded-state conclusion); 1 on any expansion mismatch.

complexity_class: exponential (oracle only)
oracle_bound: 60
"""
from fractions import Fraction
import sys

M = 101001001

def fibs(limit):
    f = [0, 1]
    while f[-1] <= limit:
        f.append(f[-1] + f[-2])
    return f

def slope(k, mult=5):
    """a = F(n-2)/F(n), a convergent of 1/phi^2, q > mult*k."""
    f = fibs(mult * k)
    return Fraction(f[-3], f[-1])

def frac(x):
    return x % 1

def digit(x, a, j):
    """d_j(x) = floor(x + (j+1)a) - floor(x + ja), exact."""
    return ((x + (j + 1) * a).numerator // (x + (j + 1) * a).denominator
            - (x + j * a).numerator // (x + j * a).denominator)

def direct(k):
    """Psi(k) by arc midpoints (independent implementation, mech_psi A-style)."""
    a = slope(k)
    pts = sorted(frac(-m * a) for m in range(k + 1))
    vals = []
    for i in range(k + 1):
        c1 = pts[i]
        c2 = pts[(i + 1) % (k + 1)] + (1 if i == k else 0)
        y = frac((c1 + c2) / 2)
        v = 0
        for j in range(k):
            v = 10 * v + digit(y, a, j)
        vals.append(v)
    return sum(v * v for v in vals), vals

def orbit_counts(k, a):
    """C_k(j,l) by direct orbit-point evaluation (interval indicator counts)."""
    xs = [frac(-m * a) for m in range(k + 1)]
    dig = [[digit(x, a, j) for j in range(k)] for x in xs]
    C = {}
    for j in range(k):
        for l in range(k):
            C[(j, l)] = sum(dig[m][j] * dig[m][l] for m in range(k + 1))
    return C

def run(bound=60):
    a3 = slope(3)
    vals3 = direct(3)[1]
    if sorted(vals3) != [1, 10, 100, 101]:
        print("FAIL: k=3 factor set", sorted(vals3))
        return 1
    if direct(3)[0] != 20302:
        print("FAIL: Psi(3) != 20302")
        return 1
    if direct(10)[0] % M != 10699667:
        print("FAIL: Psi(10) mod M != 10699667")
        return 1
    print("ANCHORS OK: Psi(3)=20302, Psi(10) mod 101001001 = 10699667")

    rows = []
    for k in range(1, bound + 1):
        a = slope(k)
        psi, _ = direct(k)
        C = orbit_counts(k, a)
        expanded = sum(C[(j, l)] * 10 ** (2 * k - 2 - j - l)
                       for j in range(k) for l in range(k))
        if expanded != psi:
            print(f"FAIL k={k}: expanded={expanded} direct={psi}")
            return 1
        rowtypes = len({tuple(C[(j, l)] for l in range(k)) for j in range(k)})
        valtypes = len(set(C.values()))
        rows.append((k, rowtypes, valtypes))

    print(f"CIRCLE INTERVAL EXPANSION: PASS k=1..{bound} (exact identity)")
    print("k rowtypes distinct_C")
    for r in rows:
        print(*r)
    maxrt = max(r[1] for r in rows)
    maxvt = max(r[2] for r in rows)
    last = rows[-1]
    half = rows[len(rows) // 2]
    print(f"max rowtypes={maxrt}, max distinct C values={maxvt}")
    print(f"rowtypes at k={half[0]}: {half[1]} ; at k={last[0]}: {last[1]}")
    if last[1] > half[1]:
        print("VERDICT: correlation-row complexity GROWS with k; "
              "no fixed-dimensional row-type aggregate at general k "
              "(bounded-state premise not supported).")
    else:
        print("VERDICT: row complexity bounded in tested range; "
              "bounded-state premise not refuted (test only up to "
              f"k={bound}, oracle).")
    return 0

if __name__ == "__main__":
    sys.exit(run(int(sys.argv[1]) if len(sys.argv) > 1 else 60))
