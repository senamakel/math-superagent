#!/usr/bin/env python3
"""PE591 fully-independent solver.
d non-square, n=1e13. BQA_d(pi,n) = argmin over (a,b), |a|,|b|<=n of |pi-(a+b sqrt(d))|
with I_d(a+b sqrt(d)) = a, S = sum |a_d|.

Written FRESH from research/cabanillas_prop9_10_exact_statement.md:
  - Algorithm 3(ii) (alpha-numeration of beta)
  - Prop 9 (best RIGHT alpha-approximations)
  - Prop 10 (best LEFT alpha-approximations), irrational-alpha Case 2.

Governing reduction (for fixed d, alpha={sqrt d}, beta={pi} in [0,1[):
  For fixed b, optimal a = nint(pi - b sqrt d), error = ||b sqrt d - pi||_Z.
    b>=0: ||b alpha - beta||_Z   (solve Prop9v10 with beta)
    b<0:  b=-m, ||m alpha + beta||_Z = ||m alpha - (1-beta)||_Z  -> solve with 1-beta.
  The records of n -> ||n alpha - beta'||_Z (best alpha-approx) are the union of
  best-right (Prop 9) and best-left (Prop 10) approximants, given in closed
  O(log L) form. The global min over [0,L] is among them. Sign chosen by min dist.

EXACT-INTEGER CF: sqrt(d) via the periodic quadratic (P,Q,a) recurrence, so all
q_k are exact Python ints.  alpha = sqrt(d) - floor(sqrt(d)) has CF [0;a1,a2,..].
Numeration digits b_k via Algorithm 3(ii) at mpmath dps=200.

No function from solution.py / solution_bothsides.py is imported or copied.
"""
import math, sys
import mpmath as mp
from math import isqrt

mp.mp.dps = 220
PI_STR = ('3.141592653589793238462643383279502884197169399375105820974944592307'
          '816406286208998628034825342117067982148086513282306647093844609550582'
          '231725359408128481117450284102701938521105559644622948954930381964428'
          '810975665933446128475648233786783165271201909145648566923460348610454')
MPI = mp.mpf(PI_STR)


# ---------------------------------------------------------------- exact CF
def cf_sqrt(d):
    """Exact integer periodic CF of sqrt(d) -> (a0, period).
    sqrt(d) = [a0; a1,...,a_{m-1},2a0, a1,...,a_{m-1},2a0, ...]
    period = [a1,...,a_{m-1},2a0].  P,Q,a integers throughout.
    """
    a0 = isqrt(d)
    P, Q = 0, 1
    a = a0
    period = []
    seen = {}
    while True:
        P = a * Q - P
        Q = (d - P * P) // Q
        a = (a0 + P) // Q
        if (P, Q) in seen:
            break
        seen[(P, Q)] = len(period)
        period.append(a)
    return a0, period


def alpha_digit_fn(d):
    """Return a_k(k) giving the exact CF digit a_k of alpha={sqrt d}, k>=0 (a_0=0)."""
    a0, period = cf_sqrt(d)
    m = len(period)
    def a_k(k):
        if k == 0:
            return 0
        return period[(k - 1) % m]
    return a_k


def q_conv(a_k, n):
    """Exact integer q_k, k=-1..n; q_{-1}=0, q_0=1, q_k = a_k q_{k-1} + q_{k-2}."""
    q = {-1: 0, 0: 1}
    for k in range(1, n + 1):
        q[k] = a_k(k) * q[k - 1] + q[k - 2]
    return q


def delta_seq(a_k, alpha, n):
    """delta_{-1}=1, delta_0=alpha, delta_k = -a_k delta_{k-1} + delta_{k-2}.
    (This equals q_k alpha - p_k, magnitude = |q_k alpha - p_k|, -> 0.)"""
    D = {-1: mp.mpf(1), 0: alpha}
    for k in range(1, n + 1):
        D[k] = -a_k(k) * D[k - 1] + D[k - 2]
    return D


# ---------------------------------------------------------------- numeration
def numeration(a_k, D, beta, n, margin_tol):
    """Algorithm 3(ii): b_k = min(a_k, ceil(beta_{k-1}/delta_{k-1})),
    beta_k = b_k delta_{k-1} - beta_{k-1}.  Returns (b, min_gap).
    b: dict {k:int}. min_gap: min distance of beta_{k-1}/delta_{k-1} to Z.
    """
    b = {}
    cur = beta
    min_gap = mp.mpf(1)
    for k in range(1, n + 1):
        r = cur / D[k - 1]
        fr = r - mp.floor(r)
        gap = min(fr, 1 - fr)
        if gap < min_gap:
            min_gap = gap
        if gap < margin_tol:
            print(f"    [margin] ceil decision k={k} gap={mp.nstr(gap)} < tol")
        bk = min(a_k(k), mp.ceil(r))
        b[k] = int(bk)
        cur = bk * D[k - 1] - cur
    return b, min_gap


# ---------------------------------------------------------------- candidates
def prefix_sums(b, q, K):
    """S[t] = sum_{i=1}^{t} b_i q_{i-1} for t=0..K (exact ints)."""
    S = {0: 0}
    for t in range(1, K + 1):
        S[t] = S[t - 1] + (b.get(t, 0)) * q[t - 1]
    return S


def prop9_right(b, q, S, L):
    """Prop 9 Case 2 (best RIGHT, irrational alpha): n=0; and for k>=1
    n = S[2k-1] + j*q[2k-1], j in 0..b[2k]-1, while prefix <= L."""
    out = {0}
    k = 1
    while S.get(2 * k - 1, 10 ** 30) <= L:
        pref = S[2 * k - 1]
        jmax = b.get(2 * k, 0) - 1
        for j in range(0, jmax + 1):
            cand = pref + j * q[2 * k - 1]
            if cand <= L:
                out.add(cand)
        k += 1
    return out


def prop10_left(b, q, S, L):
    """Prop 10 Case 2 (best LEFT, irrational alpha): for k>=0
    n = S[2k] + j*q[2k], j in 0..b[2k+1]-1, while prefix <= L."""
    out = set()
    k = 0
    while S.get(2 * k, 10 ** 30) <= L:
        pref = S[2 * k]
        jmax = b.get(2 * k + 1, 0) - 1
        for j in range(0, jmax + 1):
            cand = pref + j * q[2 * k]
            if cand <= L:
                out.add(cand)
        k += 1
    return out


def dist(n, alpha, beta):
    """||n alpha - beta||_Z at dps=200."""
    v = n * alpha - beta
    fr = v - mp.floor(v)
    return min(fr, 1 - fr)


# ---------------------------------------------------------------- solver
def solve_d(d, n):
    """Return (b, a_int, abs_a, margin_info) for BQA_d(pi,n), both signs."""
    sd = mp.sqrt(d)
    a0 = int(mp.floor(sd))
    alpha = sd - a0                      # {sqrt d} in [0,1[
    L = int(mp.floor(n / sd))
    beta = MPI - mp.floor(MPI)           # {pi}
    beta2 = 1 - beta                     # { -pi }

    a_k = alpha_digit_fn(d)
    # enough k so q_k >> L; digits and q are cheap to a generous bound
    K = 450
    q = q_conv(a_k, K)
    D = delta_seq(a_k, alpha, K + 2)

    b1, gap1 = numeration(a_k, D, beta, K, 1e-90)
    b2, gap2 = numeration(a_k, D, beta2, K, 1e-90)

    S1 = prefix_sums(b1, q, K)
    S2 = prefix_sums(b2, q, K)

    cands_pos = prop9_right(b1, q, S1, L) | prop10_left(b1, q, S1, L)
    cands_neg = prop9_right(b2, q, S2, L) | prop10_left(b2, q, S2, L)

    # positive side (b>=0): minimize ||m alpha - beta||
    mp_vals1 = sorted((dist(c, alpha, beta), c) for c in cands_pos)
    # negative side (b<0): minimize ||m alpha - beta2||, b=-m
    mp_vals2 = sorted((dist(c, alpha, beta2), c) for c in cands_neg)

    d1 = mp_vals1[0][0]; m1 = mp_vals1[0][1]
    d2 = mp_vals2[0][0]; m2 = mp_vals2[0][1]

    # 2nd-best gap report (min gap between best and 2nd best on chosen side)
    def second_gap(vals):
        if len(vals) < 2:
            return None
        return vals[1][0] - vals[0][0]

    gap_info = {
        'mag1_pos': mp.nstr(gap1, 4), 'mag1_neg': mp.nstr(gap2, 4),
        'sgp_pos': (mp.nstr(second_gap(mp_vals1), 4) if second_gap(mp_vals1) is not None else 'NA'),
        'sgp_neg': (mp.nstr(second_gap(mp_vals2), 4) if second_gap(mp_vals2) is not None else 'NA'),
    }

    if d1 <= d2:
        b = m1
    else:
        b = -m2

    a_mp = mp.nint(MPI - b * sd)
    a = int(a_mp)
    # clamp (should never bind for our data)
    if a > n:
        a = n
    if a < -n:
        a = -n
    return b, a, abs(a), gap_info


def brute_scan(d, n, dps=50):
    """Independent brute scan of b in [-L,L], a=nint(pi-b sqrt d) clamped, dps=50.
    Returns (b,a) minimizing |pi-(a+b sqrt d)| (no ties expected)."""
    mp.mp.dps = dps
    try:
        sd = mp.sqrt(d)
        L = int(mp.floor(n / sd))
        best = None
        br = None
        ba = None
        for b in range(-L, L + 1):
            a = mp.nint(MPI - b * sd)
            if a > n:
                a = n
            if a < -n:
                a = -n
            err = abs(MPI - (a + b * sd))
            if best is None or err < best:
                best = err; br = b; ba = int(a)
        return br, ba
    finally:
        mp.mp.dps = 220


def non_square_ds():
    return [d for d in range(2, 100) if isqrt(d) ** 2 != d]


# ---------------------------------------------------------------- driver
def main():
    # (1) worked examples
    print("=== (1) worked examples ===")
    examples = [(2, 10, (6, -2)), (5, 100, (-55, 26)),
                (7, 10 ** 6, (560323, -211781)),
                (2, 10 ** 13, (-6188084046055, 4375636191520))]
    for d, n, expected in examples:
        b, a, absa, gi = solve_d(d, n)
        ok = (a, b) == expected
        tag = "OK" if ok else "MISMATCH"
        print(f"d={d:2d} n={n:>7} -> a={a} b={b} |a|={absa}  expected={expected}  [{tag}]  margins {gi}")

    # (2) validate all 90 d at n=1e6, both signs vs brute
    print("\n=== (2) all 90 non-square d, n=1e6, both signs vs brute scan ===")
    n = 10 ** 6
    bad = 0
    for d in non_square_ds():
        b, a, absa, gi = solve_d(d, n)
        bB, aB = brute_scan(d, n, dps=50)
        if (b, a) != (bB, aB):
            bad += 1
            print(f"  d={d} MISMATCH solver=({b},{a}) brute=({bB},{aB})")
    print(f"n=1e6: {bad} mismatches over {len(non_square_ds())} d")

    # (3) validate 16 d at n=1e7 vs results_brute_n7.txt
    print("\n=== (3) 16 d at n=1e7 vs results_brute_n7.txt ===")
    expected = {}
    with open('/workspace/results_brute_n7.txt') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3 and parts[0].isdigit():
                expected[int(parts[0])] = (int(parts[1]), int(parts[2]))
    bad = 0
    for d, (bB, aB) in sorted(expected.items()):
        b, a, absa, gi = solve_d(d, 10 ** 7)
        if (b, a) != (bB, aB):
            bad += 1
            print(f"  d={d} MISMATCH solver=({b},{a}) brute_n7=({bB},{aB})")
        else:
            print(f"  d={d}: ({b},{a}) OK")
    print(f"n=1e7: {bad} mismatches over {len(expected)} d")

    # (4) full run n=1e13
    print("\n=== (4) FULL RUN n=1e13 ===")
    n13 = 10 ** 13
    S = 0
    rows = []
    for d in non_square_ds():
        b, a, absa, gi = solve_d(d, n13)
        S += absa
        rows.append((d, b, a, absa))
    with open('/workspace/results_ostrowski_n13.txt', 'w') as f:
        for (d, b, a, absa) in rows:
            f.write(f"{d} {b} {a} {absa}\n")
        f.write(f"S {S}\n")
    for (d, b, a, absa) in rows:
        print(f"d={d:2d} b={b:14d} a={a:15d} |a|={absa:15d}")
    print("S =", S)

    # (5) row-by-row compare vs results_full_bothsides.txt
    print("\n=== (5) row-by-row (b,a) vs results_full_bothsides.txt ===")
    ref = {}
    with open('/workspace/results_full_bothsides.txt') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3 and parts[0].isdigit():
                ref[int(parts[0])] = (int(parts[1]), int(parts[2]))
    mism = 0
    for (d, b, a, absa) in rows:
        if (b, a) != ref.get(d):
            mism += 1
            print(f"  d={d} diff solver=({b},{a}) ref=({ref.get(d)})")
    print(f"row-by-row vs bothsides: {mism} mismatches over {len(rows)} d")

    # (6) independent exact re-sum of own file
    print("\n=== (6) independent exact re-sum of results_ostrowski_n13.txt ===")
    S2 = 0
    with open('/workspace/results_ostrowski_n13.txt') as f:
        for line in f:
            parts = line.split()
            if parts and parts[0].isdigit():
                S2 += int(parts[3])
    print(f"re-sum = {S2}   (matches full-run S: {S2 == S})")


if __name__ == '__main__':
    main()
