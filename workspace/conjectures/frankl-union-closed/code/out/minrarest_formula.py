"""Verify the headlined structural claim B' with a proof-by-program:

CLAIM (min-rarest-count formula). For every union-closed family F on ground set
[n] with |F| = m and every element x present in F, letting c_x = count_x:

    c_x  >=  m - 2^{n-1}.

Proof of the general theorem: the members of F not containing x are subsets of
[n]\{x}, so all live in the power set on n-1 elements, which has exactly
2^{n-1} members. There are m - c_x of them. Hence m - c_x <= 2^{n-1}, i.e.
c_x >= m - 2^{n-1}. (Trivially also c_x >= 1 for a present element, so
c_x >= max(1, m - 2^{n-1}).) This holds for every n by a containment/counting
argument -- it does NOT use the entropy/Nagel machinery.

Here we check exhaustively (n <= 4, lib.uc oracle) that the formula is TIGHT:
min over UC families of size m of (rarest present element's count) equals
exactly max(1, m - 2^{n-1}), and that the inequality c_x >= m - 2^{n-1} holds
for every present element of every family.

Second independent route for the same number is NOT reused (worst_independent
already gave WORST(2), WORST(3) by a hand-written selector); this program adds
the uniform lower-bound check c_x >= m - 2^{n-1} elementwise.
"""
from lib.uc import decide_union_closed, abundance


def main():
    for n in range(1, 5):
        two_p = 2 ** (n - 1)
        all_masks = list(range(1 << n))
        min_rare_by_m = {}
        elementwise_violations = 0
        nc = 0
        for sub in range(1 << len(all_masks)):
            fam = set()
            for i, mask in enumerate(all_masks):
                if (sub >> i) & 1:
                    fam.add(mask)
            if not fam or fam == {0}:
                continue
            if not decide_union_closed(fam):
                continue
            nc += 1
            counts = abundance(fam, n)
            m = len(fam)
            for c in counts:
                if c > 0 and c < m - two_p:
                    elementwise_violations += 1
            present = [c for c in counts if c > 0]
            mn = min(present)
            prev = min_rare_by_m.get(m)
            if prev is None or mn < prev:
                min_rare_by_m[m] = mn
        # compare per-m minimum to formula max(1, m-two_p)
        formula_match = True
        for m in range(1, (1 << n) + 1):
            if m not in min_rare_by_m:
                continue
            formula = max(1, m - two_p)
            if min_rare_by_m[m] != formula:
                formula_match = False
        print(f"n={n}: 2^{n-1}={two_p}; UC families={nc}; "
              f"elementwise c_x >= m-2^{n-1} violations={elementwise_violations}")
        print(f"   min_rare_by_m = {sorted(min_rare_by_m.items())}")
        print(f"   formula max(1, m-2^{n-1}) is tight over all sizes: "
              f"{formula_match}")


if __name__ == "__main__":
    main()
