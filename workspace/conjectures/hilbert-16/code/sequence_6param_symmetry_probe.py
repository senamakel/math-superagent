#!/usr/bin/env python3
"""Symmetry-support refutation for the 6-parameter complement conjecture.

Claim under attack: a6_d = (dim6(h) - c6(h))/2 with c6(h) = (h^2+22h+8)/8
comes from a monomial pairing: L_d odd under a signed-permutation involution
sigma on the 6 coefficients, so its support = all degree-h monomials minus
the sigma-fixed ones, i.e. c(h) = |Fix_sigma(h)| for one sigma for all h.

For monomial fixedness the signs are irrelevant (a monomial x^e maps to a
scalar multiple of x^{pi(e)}), so it suffices to enumerate ALL permutation
involutions on 6 letters (telephone number T_6 = 76) and test whether
|Fix_pi(h)| equals the observed complement for h = 2,4,6,8,10.

Observed (exact, from code/out/bautin_focal_values.captured.txt and the
exact dumps focal_6coeff_L10/L12.txt):
  a6_d = 6,56,220,628,1481 for d=4,6,8,10,12
  dim6(h) = C(h+5,5) for h=d-2
  c6(h) = dim6(h) - 2*a6_d = 9,14,22,31,41 for h=2,4,6,8,10
"""
from itertools import permutations
from math import comb


def involutions(n):
    """All permutations pi of {0..n-1} with pi(pi(i))==i (76 for n=6)."""
    out = []
    for p in permutations(range(n)):
        if all(p[p[i]] == i for i in range(n)):
            out.append(p)
    return out


def fixed_monomial_count(pi, h, n=6):
    """# exponent vectors e>=0, |e|=h, with pi(e) = e."""
    count = 0

    def rec(i, remaining, cur):
        nonlocal count
        if i == n:
            if remaining == 0 and all(cur[pi[j]] == cur[j] for j in range(n)):
                count += 1
            return
        for val in range(remaining + 1):
            cur.append(val)
            rec(i + 1, remaining - val, cur)
            cur.pop()

    rec(0, h, [])
    return count


def main():
    n = 6
    hs = (2, 4, 6, 8, 10)
    observed = {2: 9, 4: 14, 6: 22, 8: 31, 10: 41}
    dims = {h: comb(h + 5, 5) for h in hs}
    print("# Symmetry-support refutation, 6-param complement (exact search)")
    print("observed c6(h):", observed)
    print("ambient dims:", dims)
    print()
    invs = involutions(n)
    print(f"enumerating all {len(invs)} permutation involutions on 6 letters "
          "(signs irrelevant for monomial fixedness)")
    best = (0, None)
    matches = []
    for pi in invs:
        row = {h: fixed_monomial_count(pi, h, n) for h in hs}
        score = sum(1 for h in hs if row[h] == observed[h])
        if score == len(hs):
            matches.append((pi, row))
        if score > best[0]:
            best = (score, (pi, row))
    print("full matches:", len(matches))
    for pi, row in matches:
        print("  pi =", pi, " row =", row)
    print("best partial match:", best[0], "of", len(hs))
    if best[1] is not None:
        pi, row = best[1]
        print("  pi =", pi)
        print("  row =", row, " (observed 9,14,22,31,41)")
    # also: attainable values at h=4 (the smallest discriminating degree)
    vals = sorted({fixed_monomial_count(pi, 4, n) for pi in invs})
    print("attainable |Fix_pi(h=4)| over all involutions:", vals)
    print("needed c6(4) = 14; in list:", 14 in vals)
    verdict = ("REFUTED" if not matches
               else "SUPPORTED by an involution (report it)")
    print("VERDICT:", verdict, "(no signed-permutation pairing yields c6)")


if __name__ == "__main__":
    main()
