#!/usr/bin/env python3
"""Verify Cambie-Yan (arXiv:2408.01211) Theorems 1.1 & 1.2 against direct
enumeration, and check the gap-affinity of f_n(k) (workspace tables).

Theorem 1.1: E[des(pi^k)] = (n-1)/2 - (tau(k)^2 - tau(k) - tau_o(k) + sigma(k)) / (2n)
Theorem 1.2: E[inv(pi^k)] = n(n-1)/4 - (tau(k)-1)*n/6
                            - (tau(k)^2 - tau(k) - tau_o(k) + sigma(k)) / 12
valid for n >= 2k+1 (remark: actually for n >= k + l(k), l(k) = largest proper divisor).
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
    """Common factor appearing in both theorems: tau^2 - tau - tau_o + sigma."""
    return tau(k) ** 2 - tau(k) - tau_o(k) + sigma(k)


def E_des_CY(n, k):
    return Fraction(n - 1, 2) - Fraction(CFK(k), 2 * n)


def E_inv_CY(n, k):
    return Fraction(n * (n - 1), 4) - Fraction((tau(k) - 1) * n, 6) - Fraction(CFK(k), 12)


def compose(a, b):
    """a∘b? Here we want iterate: p^e. We define mult(p,q)[i] = p[q[i]] and
    powers via repeated squaring, so p^1 = p, p^2[i] = p[p[i]], etc."""
    n = len(a)
    return tuple(a[b[i]] for i in range(n))


def power(p, e):
    n = len(p)
    res = tuple(range(n))
    base = tuple(p)
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
            # direct averages
            Sd = sum(des(power(pi, k)) for pi in perms)
            Si = sum(inv(power(pi, k)) for pi in perms)
            Ed, Ei = E_des_CY(n, k), E_inv_CY(n, k)
            okD = (Fraction(Sd, nf) == Ed)
            okI = (Fraction(Si, nf) == Ei)
            ok = ok and okD and okI
            if not (okD and okI):
                print(f"  MISMATCH n={n} k={k}: des {Fraction(Sd, nf)} vs {Ed}; inv {Fraction(Si, nf)} vs {Ei}")
        print(f"  n={n}: all k in 1..{n-1} match = {ok}")
    print("ALL CAMBIE-YAN CHECKS PASS" if ok else "CAMBIE-YAN MISMATCH FOUND")


def check_gap_affinity():
    print("\n== f_n(k) gap-affinity & linearity (from extend_f.json) ==")
    with open("extend_f.json") as f:
        data = json.load(f)  # keys are strings "2".."11"
    for ns in sorted(data, key=int):
        row = data[ns]
        n = int(ns)
        diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        constant = all(d == diffs[0] for d in diffs)
        print(f"  n={n}: length {len(row)}, first diffs constant = {constant}")
        # also verify the normalization-range sanity: 0 < f < n!^2 for all k
        nf2 = factorial(n) ** 2
        sane = all(0 < v < nf2 for v in row)
        print(f"     0 < f_n(k) < n!^2 for all k: {sane}")


def check_f_vs_invsum():
    """Check: sum_{j<m} T(j,m) = sum_{pi,i} inv(pi^i).  By translation
    invariance, sum_{j<m} T(j,m) = sum_{k=1}^{n-1} (n-k) f_n(k).
    Direct RHS: sum_{pi} (n!/ord(pi)) * sum_{tau in <pi>} inv(tau)."""
    print("\n== sum_{j<m} T(j,m) == sum_{pi,i} inv(pi^i), n=5,6 ==")
    for n in (5, 6):
        perms = list(permutations(range(n)))
        nf = factorial(n)
        LHS_by_f = sum((n - k) * T for k, T in enumerate((0,) + tuple(range(n)), start=1)) if False else None
        # compute f row on the fly (gap k=1..n-1): f(k)=T(0,k)
        fk = []
        for k in range(1, n):
            tot = 0
            for pi in perms:
                d = ord_pi(pi)
                seen = {}
                cur = pi
                for t in range(d):
                    seen[cur] = True
                    cur = compose(pi, cur)
                cnt = sum(1 for tau in seen if tau[k] < tau[0])
                tot += (nf // d) * cnt
            fk.append(tot)
        Tsum_f = sum((n - k) * fk[k - 1] for k in range(1, n))
        RHS = 0
        for pi in perms:
            d = ord_pi(pi)
            cur = pi
            s = 0
            for t in range(d):
                s += inv(cur)
                cur = compose(pi, cur)
            RHS += (nf // d) * s
        print(f"  n={n}: sum_k (n-k) f_n(k) = {Tsum_f}, sum_{pi,i} inv(pi^i) = {RHS}, equal = {Tsum_f == RHS}")


if __name__ == "__main__":
    check_CY()
    check_gap_affinity()
    check_f_vs_invsum()