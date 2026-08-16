"""Abundance-profile check for the kth-most-frequent element (Nagel / Das-Wu).

Das-Wu (arXiv:2412.03862) Theorem 1.4: for union-closed F with |U F| >= k >= 2,
the kth-most-frequent element lies in >= |F|/(2^{k-1}+1) sets, with equality iff
F is a near-k-cube.

Near-k-cube (correct form): F = 2^{[k-1]} ∪ { [k-1] ∪ {k} }. Ground set [k].
  * |F| = 2^{k-1} + 1, |U F| = k.
  * element k  (bit k-1): in exactly 1 set (the top set)         -> frequency 1
  * element i < k-1 (bits 0..k-2): in 2^{k-2} subsets containing i, plus the
    top set -> frequency 2^{k-2}+1.
  * kth-most-frequent element (the rare one) frequency = 1
    = |F|/(2^{k-1}+1)  (equality in Nagel's bound).
Union-closed: any subset of [k-1] unioned with the top set is the top set itself.

Prints the exact abundance profile as an integer sequence.
"""
from lib.uc import abundance, decide_union_closed


def near_k_cube(k):
    top = 1 << (k - 1)                      # {k}
    F = set()
    for mask in range(1 << (k - 1)):        # all subsets of [k-1]
        F.add(mask)
    F.add(top | ((1 << (k-1)) - 1))         # [k-1] ∪ {k}
    assert decide_union_closed(F), "near-k-cube must be union-closed"
    return F


def main():
    print("Near-k-cube abundance profile (exact), k=2..8\n")
    print(" k | |F| = 2^{k-1}+1 | profile counts | kth-freq | == |F|/den ?")
    print("---+---------------+----------------+-----------+-------------")
    ok = True
    for k in range(2, 9):
        F = near_k_cube(k)
        m = len(F)
        den = 2**(k-1) + 1
        counts = sorted(abundance(F, k), reverse=True)
        kth = counts[k-1]
        equality = (kth * den == m)
        ok &= equality
        print(f" {k:2} | {m:5} ={den:5}  | "
              f"{counts} | {kth:5} | {['ok','FAIL'][not equality]}")
    print("\nEquality |F|/(2^{k-1}+1) kth-most-frequent:",
          "ALL PASS" if ok else "SOME FAIL")

    # The abundance profiles as an integer sequence (row k = counts sorted desc).
    print("\nProfiles (ground set [k], counts sorted desc):")
    for k in range(2, 9):
        F = near_k_cube(k)
        counts = sorted(abundance(F, k), reverse=True)
        print(f"  k={k}: {counts}")
    print("\nStructure: [2^{k-2}+1 repeated k-1 times, 1]  -> kth (last) = 1,")
    print("  so the Nagel bound |F|/(2^{k-1}+1) is attained with equality.")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
