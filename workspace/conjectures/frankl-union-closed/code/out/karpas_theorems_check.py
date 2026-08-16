"""Independent check of Karpas's two theorems (arXiv:1708.01434) against the
canonical oracle, on all union-closed families on [n], n <= 4.

The check routes union-closure and abundance through lib.uc (the canonical
oracle). It is not a new oracle; it verifies two published structural theorems
on the exhaustive small-family data:

  Theorem 1.2 (large families): if |F| >= 2^(n-1) then some element is
    abundant (|F_i| >= |F|/2).
  Theorem 1.3 (upper shadow): |upper_shadow(F) \\ F| <= 2^(n-1), where
    upper_shadow(F) = { A | {i} : i notin A } over A in F.

Also your-work negative control: a non-UC antichain must be rejected.
"""
from lib.uc import decide_union_closed, abundant_elements

N_MAX = 4


def upper_shadow(F, n):
    out = set()
    for A in F:
        for i in range(n):
            if not (A >> i) & 1:
                out.add(A | (1 << i))
    return out


def enumerate_uc_families(n):
    """Yield every union-closed family on [n] (excluding {empty}).
    Subfamily index over the 2^n masks; classic 2^(2^n) enumeration, oracle-only."""
    masks = list(range(1 << n))
    for sub in range(1 << len(masks)):  # 2^(2^n)
        fam = {m for j, m in enumerate(masks) if (sub >> j) & 1}
        if not fam:
            continue
        if fam == {0}:
            continue
        if decide_union_closed(fam):
            yield fam


def main():
    fail_thm12 = fail_thm13 = 0
    families = 0
    for n in range(0, N_MAX + 1):
        for F in enumerate_uc_families(n):
            families += 1
            m = len(F)
            # Theorem 1.2
            if m >= 2 ** (n - 1):
                if not abundant_elements(F, n):
                    fail_thm12 += 1
                    if fail_thm12 <= 3:
                        print(f"  THM1.2 FAIL n={n} |F|={m}: {sorted(F)}")
            # Theorem 1.3
            us = upper_shadow(F, n)
            if len(us - F) > 2 ** (n - 1):
                fail_thm13 += 1
                if fail_thm13 <= 3:
                    print(f"  THM1.3 FAIL n={n} |F|={m} shadow={len(us - F)}")
    # negative control: antichain {{1},{2},{3}} on n=3
    n = 3
    antichain = {0b001, 0b010, 0b100}  # {1},{2},{3}
    uc_rejected = not decide_union_closed(antichain)
    print(f"UC families enumerated (n=0..4): {families}")
    print(f"Theorem 1.2 (|F|>=2^(n-1) => abundant) violations: {fail_thm12}")
    print(f"Theorem 1.3 (upper shadow <= 2^(n-1)) violations:    {fail_thm13}")
    print(f"negative control antichain rejected as non-UC:        {uc_rejected}")
    ok = (fail_thm12 == 0 and fail_thm13 == 0 and uc_rejected)
    print("RESULT:", "ALL KARPAS CHECKS PASSED" if ok else "FAILURES PRESENT")


if __name__ == "__main__":
    main()
