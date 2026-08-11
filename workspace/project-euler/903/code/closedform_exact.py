#!/usr/bin/env python3
"""closedform_exact.py — EXACT (Fraction / big-int) verification of PE 903.

Verifies the closed forms of the derivation (code/closedform_derivation.md):

  f_n(k) = #{(pi,i): 0<=i<n!, (pi^i)(k) < (pi^i)(0)} = A_n + (k-1) B_n,
  A_n/(n!)^2 = 1/2 + E2/[n(n-1)] - (E11-E1)/[2 n (n-1)],
  B_n/(n!)^2 = [n - (n+1)E1 + E11 - 2 E2]/[n(n-1)(n-2)],
  E1 = H_n,  E2 = (1/4) H_{floor(n/2)},  E11 = n + S(n),
  S(n) = sum_{a+b<=n} 1/lcm(a,b),
  Q(n) = (n!)^2 + A_n (n!-1) + (B_n/2) T(n),  T(n)=sum_{m=1}^{n-1} m(m-1)m!.

Three independent checks, all exact (no mod, no floats):

(a) DIRECT per-class enumeration of Campion-Loth Lemma 4.7 (arXiv:2301.00898):
    for n = 4..7, for EVERY conjugacy class (cycle type) and every gap k,
    count #{sigma in C_lambda : sigma(k) < sigma(0)} / |C_lambda| and compare
    with the Lemma 4.7 formula (i=0, j=k).  This pins the source identity
    itself, not merely the composite A_n/B_n.

(b) The three mu-moments by DIRECT orbit summation: for n = 3..9, iterate
    over ALL pi, compute ord(pi), sum g over the ord distinct powers
    g(pi^i) (g = a_1, a_2, a_1^2), weight by (n!/ord), divide by (n!)^2 to
    get E_mu[g], compare with H_n, (1/4)H_{floor(n/2)}, n+S(n).

(c) The composite closed forms: f_n(k) from A_n, B_n (as exact Fractions,
    times P=(n!)^2) must equal the oracle rows in out/extend_f.json for
    n=2..11 (big-int equality, all gaps); and Q(n) via the verified reduction
    must equal brute Q(2..8), Q(9), Q(10), Q(11) (computed from extend_f
    rows), with Q(10) mod p == 468421536 (statement oracle).

Exits non-zero on any FAIL.
"""
import itertools
import json
import math
import os
from fractions import Fraction as F

MOD = 10**9 + 7
HERE = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------
def harmonic(n):
    return sum(F(1, k) for k in range(1, n + 1))


def S_lcm(n):
    """S(n) = sum_{a=1}^{n-1} sum_{b=1}^{n-a} 1/lcm(a,b)  (exact Fraction)."""
    return sum(F(1, math.lcm(a, b))
               for a in range(1, n) for b in range(1, n - a + 1))


def closed_AB(n):
    """Return (A_n, B_n) as exact Fractions from the Section-5 closed forms.

    n = 2 is the documented special case: count A_2 = 1, so the normalized
    value A_2/(n!)^2 = 1/4 with B_2 = 0.
    """
    if n == 2:
        return F(1, 4), F(0)
    E1 = harmonic(n)
    E2 = F(1, 4) * harmonic(n // 2)
    E11 = n + S_lcm(n)
    An = F(1, 2) + E2 / F(n * (n - 1)) - (E11 - E1) / F(2 * n * (n - 1))
    Bn = (n - (n + 1) * E1 + E11 - 2 * E2) / F(n * (n - 1) * (n - 2))
    return An, Bn


def cycle_type(perm):
    """Reduce a permutation (tuple/list) to its sorted cycle-type partition."""
    n = len(perm)
    seen = [False] * n
    lens = []
    for s in range(n):
        if not seen[s]:
            c = s
            cnt = 0
            while not seen[c]:
                seen[c] = True
                c = perm[c]
                cnt += 1
            lens.append(cnt)
    return tuple(sorted((l for l in lens if l > 1), reverse=True)), lens


def class_params(lens):
    """a_1 = #fixed points, a_2 = #2-cycles from the cycle-length list."""
    return lens.count(1), lens.count(2)


# ----------------------------------------------------------------------
# (a) Lemma 4.7 by direct per-class enumeration
# ----------------------------------------------------------------------
def lemma_47_pr(n, a1, a2, k):
    """Lemma 4.7 probability Pr[sigma(0) > sigma(k)] on class with a1 fixed,
    a2 two-cycles; i=0, j=k.  Returns exact Fraction."""
    if n < 3:
        # degenerate; checked separately
        return F(1, 2)
    return (F(1, 2) + F(a2, n * (n - 1))
            - F(a1 * (a1 - 1), 2 * n * (n - 1))
            + F(k - 1, 1) * F(n - n * a1 - a1 + a1 * a1 - 2 * a2,
                              n * (n - 1) * (n - 2)))


def check_lemma():
    all_ok = True
    print("=" * 78)
    print("(a) Campion-Loth Lemma 4.7 (arXiv:2301.00898) — per-class count vs formula")
    print("    Pr[sigma(0) > sigma(k)] on class C_lambda, gaps k=1..n-1")
    print("    for EVERY conjugacy class of S_n (n = 4,5,6,7).")
    print("=" * 78)
    for n in range(4, 8):
        cls_counts = {}
        for perm in itertools.permutations(range(n)):
            _, lens = cycle_type(perm)
            ct = tuple(sorted((l for l in lens if l > 1), reverse=True))
            cls_counts.setdefault(ct, [0, [0] * (n - 1)])  # [size, per-gap count]
            cls_counts[ct][0] += 1
            for k in range(1, n):
                if perm[k] < perm[0]:
                    cls_counts[ct][1][k - 1] += 1
        cls_ok = True
        for ct, (size, counts) in sorted(cls_counts.items()):
            # a_1, a_2 from the *full* cycle lengths incl. fixed points:
            # class of cycle type ct has (n - len(ct too few) ) fixed points;
            # recompute from the partition's entries.
            total_len = sum(ct)
            a1 = n - total_len
            a2 = ct.count(2)
            for k in range(1, n):
                counted = F(counts[k - 1], size)
                formula = lemma_47_pr(n, a1, a2, k)
                ok = counted == formula
                cls_ok = cls_ok and ok
                if not ok:
                    print(f"  n={n} class {ct} k={k}: "
                          f"counted={counted} formula={formula}  FAIL")
        tag = "PASS" if cls_ok else "FAIL"
        all_ok = all_ok and cls_ok
        ncl = len(cls_counts)
        print(f"  n={n}: {ncl} classes x {n-1} gaps: [{tag}]")
    print("(a) result:", "ALL PASS" if all_ok else "SOME FAIL")
    return all_ok


# ----------------------------------------------------------------------
# (b) three mu-moments by direct orbit summation
# ----------------------------------------------------------------------
def cycle_lens(perm):
    n = len(perm)
    seen = [False] * n
    lens = []
    for s in range(n):
        if not seen[s]:
            c = s
            cnt = 0
            while not seen[c]:
                seen[c] = True
                c = perm[c]
                cnt += 1
            lens.append(cnt)
    return lens


def ord_perm(perm):
    l = 1
    for ln in cycle_lens(perm):
        l = l * ln // math.gcd(l, ln)
    return l


def a1_a2(pow_tuple):
    """(a_1, a_2) = (# fixed points, # 2-cycles) of the given permutation."""
    lens = cycle_lens(pow_tuple)
    return lens.count(1), lens.count(2)


def check_moments():
    all_ok = True
    print("=" * 78)
    print("(b) The three mu-moments by DIRECT orbit summation over all pi")
    print("    E_mu[g] = sum_pi (n!/ord) sum_{i mod ord} g(pi^i) / (n!)^2")
    print("    vs  H_n,  (1/4)H_{floor(n/2)},  n + S(n)")
    print("=" * 78)
    data = {}
    for n in range(3, 10):
        nf = math.factorial(n)
        N2 = nf * nf
        s_a1 = F(0)
        s_a2 = F(0)
        s_a11 = F(0)
        idt = tuple(range(n))
        for perm in itertools.permutations(range(n)):
            d = ord_perm(perm)
            w = F(nf, d)
            cur = idt
            orbit_sum_a1 = 0
            orbit_sum_a2 = 0
            orbit_sum_a11 = 0
            for _ in range(d):
                a1, a2 = a1_a2(cur)
                orbit_sum_a1 += a1
                orbit_sum_a2 += a2
                orbit_sum_a11 += a1 * a1
                cur = tuple(perm[x] for x in cur)
            s_a1 += w * orbit_sum_a1
            s_a2 += w * orbit_sum_a2
            s_a11 += w * orbit_sum_a11
        E1 = s_a1 / N2
        E2 = s_a2 / N2
        E11 = s_a11 / N2
        t1 = harmonic(n)
        t2 = F(1, 4) * harmonic(n // 2)
        t11 = n + S_lcm(n)
        ok1 = E1 == t1
        ok2 = E2 == t2
        ok3 = E11 == t11
        ok = ok1 and ok2 and ok3
        all_ok = all_ok and ok
        print(f"  n={n}: E[a1]={E1} vs H_n={t1} [{'PASS' if ok1 else 'FAIL'}]; "
              f"E[a2]={E2} vs (1/4)H[{n//2}]={t2} "
              f"[{'PASS' if ok2 else 'FAIL'}]; "
              f"E[a1^2]={E11} vs n+S(n)={t11} "
              f"[{'PASS' if ok3 else 'FAIL'}]")
        data[n] = [str(E1), str(E2), str(E11)]
    print("(b) result:", "ALL PASS" if all_ok else "SOME FAIL")
    print("    (largest n checked:", 9, ")")
    return all_ok


# ----------------------------------------------------------------------
# (c) composite closed forms vs oracle rows, and Q(n)
# ----------------------------------------------------------------------
def load_extend_f():
    with open(os.path.join(HERE, "out", "extend_f.json")) as fh:
        return {int(k): v for k, v in json.load(fh).items()}


def q_from_reduction(n, A_int, B_int):
    """Q(n) = (n!)^2 + A(n!-1) + (B/2) T(n), A,B = actual counts (big ints)."""
    nf = math.factorial(n)
    T = sum(m * (m - 1) * math.factorial(m) for m in range(1, n))
    # B*T is always even (each m(m-1) is even) -> exact halving
    return nf * nf + A_int * (nf - 1) + (B_int * T) // 2


def check_closed():
    all_ok = True
    print("=" * 78)
    print("(c) Closed-form A_n, B_n -> f_n(k) rows vs oracle (out/extend_f.json)")
    print("    and Q(n) via the verified reduction vs brute / extend_f values.")
    print("=" * 78)
    extend = load_extend_f()

    # ---- (c1) f_n(k) rows ----
    print("--- (c1) f_n(k) = (A_n + (k-1) B_n)(n!)^2 exact vs oracle rows ---")
    ok_rows = True
    for n in range(2, 12):
        row = extend[n]
        An, Bn = closed_AB(n)
        P = math.factorial(n) ** 2
        closed_row = [int((An + (k - 1) * Bn) * P) for k in range(1, n)]
        ok = closed_row == row
        ok_rows = ok_rows and ok
        print(f"  n={n}: A_n={An} B_n={Bn}  row match: "
              f"{'PASS' if ok else 'FAIL'}")
        if not ok:
            print(f"        closed={closed_row}\n        oracle={row}")
    all_ok = all_ok and ok_rows
    print("  (c1) result:", "ALL PASS" if ok_rows else "SOME FAIL")

    # ---- (c2) Q(n) ----
    print("--- (c2) Q(n) via verified reduction from closed-form A_n, B_n ---")
    brute = {2: 5, 3: 88, 4: 4808, 5: 597876, 6: 133103808,
             7: 47124948960, 8: 24768798220800}
    ok_Q = True
    for n in range(2, 12):
        An, Bn = closed_AB(n)
        P = math.factorial(n) ** 2
        A_int = int(An * P)
        B_int = int(Bn * P)
        Q = q_from_reduction(n, A_int, B_int)
        Qmod = Q % MOD
        if n <= 8:
            ok = Q == brute[n]
            ref = f"brute {brute[n]}"
        else:
            # expected Q from extend_f rows through the SAME verified reduction
            row = extend[n]
            A_ref, B_ref = row[0], row[1] - row[0]
            Q_ref = q_from_reduction(n, A_ref, B_ref)
            ok = Q == Q_ref
            ref = f"extend_f Q={Qmod} (mod p)"
        ok_Q = ok_Q and ok
        print(f"  n={n}: Q mod p = {Qmod}  vs {ref}  "
              f"[{'PASS' if ok else 'FAIL'}]")
    # statement oracle Q(10) mod p
    n10 = 10
    An, Bn = closed_AB(n10)
    P = math.factorial(n10) ** 2
    Q10 = q_from_reduction(n10, int(An * P), int(Bn * P)) % MOD
    ok10 = Q10 == 468421536
    ok_Q = ok_Q and ok10
    print(f"  Q(10) mod p = {Q10}  (statement oracle 468421536): "
          f"{'PASS' if ok10 else 'FAIL'}")
    all_ok = all_ok and ok_Q
    print("  (c2) result:", "ALL PASS" if ok_Q else "SOME FAIL")
    return all_ok


def main():
    a = check_lemma()
    b = check_moments()
    c = check_closed()
    print()
    print("=" * 78)
    print("closedform_exact.py overall:",
          "ALL PASS" if (a and b and c) else "SOME FAIL")
    print("=" * 78)
    return 0 if (a and b and c) else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
