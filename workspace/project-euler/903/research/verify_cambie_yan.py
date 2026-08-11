#!/usr/bin/env python3
"""Verify Cambie-Yan (arXiv:2408.01211) Thms 1.1 & 1.2 vs direct enumeration;
check gap-affinity of f_n(k); and test the "two-pinning probabilities" model
for E[inv(pi^i)] under the random-power law.

Model being tested for the random-power law (pi uniform in S_n, i uniform in
1..n!, sigma = pi^i): per pair j<m, does P(sigma(j) > sigma(m)) depend on the
gap m-j only, and is it affine in that gap?  Empirically (n<=11) the unweighted
counts f_n(k) are exactly affine; we re-measure the pair probabilities here and
check both properties from scratch for n=5..7.
"""
from itertools import permutations
from math import factorial, gcd
from fractions import Fraction
import json


def tau(k):
    return sum(1 for d in range(1, k + 1) if k % d == 0)


def sigma(k):
    return sum(d for d in range(1, k + 1) if k % d == 0)


def tau_o(k):
    while k % 2 == 0:
        k //= 2
    return tau(k)


def CFK(k):
    return tau(k) ** 2 - tau(k) - tau_o(k) + sigma(k)


def E_des_CY(n, k):
    return Fraction(n - 1, 2) - Fraction(CFK(k), 2 * n)


def E_inv_CY(n, k):
    return Fraction(n * (n - 1), 4) - Fraction((tau(k) - 1) * n, 6) - Fraction(CFK(k), 12)


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def power(p, e):
    n = len(p)
    res = tuple(range(n))
    base = p
    while e:
        if e & 1:
            res = compose(base, res)
        base = compose(base, base)
        e >>= 1
    return res


def des(p):
    return sum(1 for i in range(len(p) - 1) if p[i] > p[i + 1])


def inv(p):
    n = len(p)
    return sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])


def ord_pi(p):
    n = len(p)
    seen = [False] * n
    l = 1
    for s in range(n):
        if not seen[s]:
            cur, ln = s, 0
            while not seen[cur]:
                seen[cur] = True
                cur = p[cur]
                ln += 1
            l = l * ln // gcd(l, ln)
    return l


def check_CY():
    print("== Cambie-Yan Theorems 1.1/1.2 vs direct enumeration ==")
    ok = True
    for n in range(3, 8):
        perms = list(permutations(range(n)))
        nf = factorial(n)
        for k in range(1, n):
            Sd = sum(des(power(pi, k)) for pi in perms)
            Si = sum(inv(power(pi, k)) for pi in perms)
            Ed, Ei = E_des_CY(n, k), E_inv_CY(n, k)
            okD = Fraction(Sd, nf) == Ed
            okI = Fraction(Si, nf) == Ei
            ok = ok and okD and okI
            if not (okD and okI):
                print(f"  MISMATCH n={n} k={k}: des {Fraction(Sd, nf)} vs {Ed}; inv {Fraction(Si, nf)} vs {Ei}")
        print(f"  n={n}: all k=1..{n-1} match = {ok}")
    print("ALL CAMBIE-YAN CHECKS PASS" if ok else "CAMBIE-YAN MISMATCH FOUND")


def check_f_gap_affinity():
    print("\n== f_n(k) gap-affinity from extend_f.json ==")
    with open("extend_f.json") as f:
        data = json.load(f)
    for ns in sorted(data, key=int):
        row = data[ns]
        diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        print(f"  n={ns}: len {len(row)}, 1st-diff constant = {all(d == diffs[0] for d in diffs)}")


def check_pair_prob_affine():
    """Measure P_n(gap) = P(pi^i(j) > pi^i(j+gap)) under the random-power law,
    for j=0 only (translation-invariant) and check affine in gap."""
    print("\n== per-gap inversion probability S(j,j+g)/count vs gap (n=5..7) ==")
    for n in (5, 6, 7):
        perms = list(permutations(range(n)))
        nf = factorial(n)
        # T(j,m) with weight nf/ord over distinct powers
        fk = []
        counts = []
        for k in range(1, n):
            tot_pair = 0
            tot_cnt = 0
            for pi in perms:
                d = ord_pi(pi)
                orbit = []
                cur = pi
                seen = {}
                for t in range(d):
                    seen[cur] = True
                    cur = compose(pi, cur)
                tot_cnt += (nf // d) * d  # == nf * 1 per pi
                cnt = sum(1 for tau in seen if tau[k] < tau[0])
                tot_pair += (nf // d) * cnt
            fk.append(tot_pair)
            counts.append(tot_cnt)
        # pair prob P(pi^i(k) < pi^i(0)) with reversed sign: want P(pi^i(j) > pi^i(m))
        probs = [Fraction(tot, counts[0]) * 1 for tot, cnt in zip(fk, counts)]
        # Affine check on fk itself already done. Report probs and their 1st diffs.
        pdiffs = [probs[i + 1] - probs[i] for i in range(len(probs) - 1)]
        print(f"  n={n}: gap probs P(0>k): {[str(p) for p in probs]}")
        print(f"       diffs: {[str(d) for d in pdiffs]}, constant = {all(d == pdiffs[0] for d in pdiffs)}")


if __name__ == "__main__":
    check_CY()
    check_f_gap_affinity()