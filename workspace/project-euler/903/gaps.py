#!/usr/bin/env python3
"""Compute T(j,m) = #{(pi,i): 0<=i<n!, (pi^i)(m) < (pi^i)(j)} for n=2..9.

Method — period formula (no literal iteration over all n! powers):
for pi of orbit-period d = ord(pi) (a group element's order; d | n!), each
distinct power in <pi> appears exactly n!/d times among i = 0..n!-1, so

  T(j,m) = sum_pi (n!/d) * #{tau in <pi>: tau(m) < tau(j)}.

We accumulate the rationals exactly (Fraction) and report the integer T.

Also compute the literal double-count for n=2,3 as an oracle and verify
agreement, and verify translation invariance T(j,j+k) independent of j.
"""
import itertools
import math
import time
from fractions import Fraction


def cycle_order(perm):
    """ord(perm) = lcm of cycle lengths (order of perm as a group element)."""
    n = len(perm)
    seen = [False] * n
    l = 1
    for i in range(n):
        if not seen[i]:
            cur = i
            cnt = 0
            while not seen[cur]:
                seen[cur] = True
                cur = perm[cur] - 1
                cnt += 1
            l = l * cnt // math.gcd(l, cnt)
    return l


def apply_power(perm, cur):
    """one step along the orbit: (pi applied to cur)."""
    return tuple(perm[v - 1] for v in cur)


def T_pairs_exact(n):
    """Return Tp (n x n, j,m 1-indexed stored at [j-1][m-1]) and nfac."""
    nfac = math.factorial(n)
    idt = tuple(range(1, n + 1))
    Tp = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for perm in itertools.permutations(range(1, n + 1)):
        d = cycle_order(perm)
        weight = Fraction(nfac, d)
        cur = idt
        for _ in range(d):          # one pass through the distinct powers of pi
            for m in range(n):
                cm = cur[m]
                for j in range(n):
                    if cm < cur[j]:
                        Tp[j][m] += weight
            cur = apply_power(perm, cur)
    return Tp, nfac


def literal(n):
    """Literal oracle: iterate every i=0..n!-1 for every pi (small n only)."""
    perms = list(itertools.permutations(range(1, n + 1)))
    nfac = math.factorial(n)
    idt = tuple(range(1, n + 1))
    T = [[0] * n for _ in range(n)]
    for perm in perms:
        cur = idt
        for _ in range(nfac):
            for m in range(n):
                cm = cur[m]
                for j in range(n):
                    if cm < cur[j]:
                        T[j][m] += 1
            cur = apply_power(perm, cur)
    return T


def main():
    for n in range(2, 10):
        t0 = time.time()
        Tp, nfac = T_pairs_exact(n)
        dt = time.time() - t0
        # f_n(k) = T(1,1+k), integer
        fk = [Tp[0][k] for k in range(1, n)]
        # translation invariance: T(j,j+k) == T(1,1+k) for all j
        inv = all(Tp[j - 1][j - 1 + k] == fk[k - 1]
                  for k in range(1, n) for j in range(1, n - k + 1))
        # flatten to exact integers (confirm denominators are 1)
        fk_int = [int(x) for x in fk]
        diffs = [fk_int[i + 1] - fk_int[i] for i in range(len(fk_int) - 1)]
        second = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)] if len(diffs) >= 2 else []
        is_arith = len(second) > 0 and all(s == 0 for s in second)

        lit = "n/a"
        if n in (2, 3):
            Tl = literal(n)
            lit = "PASS" if all(Tl[0][k] == fk_int[k - 1] for k in range(1, n)) else "FAIL"

        print(f"\n=== n = {n}  (time {dt:.2f}s, literal-check {lit}) ===")
        print(f"  f_n(k)=T(1,1+k), k=1..n-1 : {fk_int}")
        print(f"  1st diffs: {diffs}")
        if len(second) > 0:
            print(f"  2nd diffs: {second}")
        print(f"  translation-invariant: {inv}")
        if is_arith:
            print(f"  EXACTLY ARITHMETIC: A_n=f(1)={fk_int[0]}, step B_n={diffs[0]}")
        else:
            print("  NOT exactly arithmetic")

    print("\nAll numeric tables above.")


if __name__ == "__main__":
    main()
