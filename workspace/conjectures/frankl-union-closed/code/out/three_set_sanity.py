"""Sanity check on the refuted artifact code/out/refute/code_refute_uc_with_three_set.p.json.

That artifact records finding=refuted, CounterSatisfiable, against the rung
'every union-closed family containing a 3-element set has an abundant element',
with a 4-element domain model. UC is machine-verified to n=12, so no such
union-closed family can exist on <= 4 ground-set elements.

Exhaustive exact check with the canonical oracle (lib.uc): enumerate every
union-closed family on [n] (n<=4) that contains at least one 3-element set,
and verify each has an abundant element. If ALL PASS, the artifact's "refuted"
verdict is an encoding bug, not a mathematical counterexample.
"""
from lib.uc import decide_union_closed, abundance


def has_3set(fam, n):
    for s in fam:
        if bin(s).count("1") == 3 and s != 0 and s != (1 << n) - 1 or \
           (bin(s).count("1") == 3 and n == 3):
            if bin(s).count("1") == 3:
                return True
    return False


for n in range(1, 5):
    masks = list(range(1 << n))
    K = len(masks)
    total_uc_with_3set = 0
    failures = 0
    for sub in range(1 << K):
        fam = set()
        for i, m in enumerate(masks):
            if (sub >> i) & 1:
                fam.add(m)
        if not fam or fam == {0}:
            continue
        if not has_3set(fam, n):
            continue
        if not decide_union_closed(fam):
            continue
        total_uc_with_3set += 1
        counts = abundance(fam, n)
        present = [c for c in counts if c > 0]
        half2 = 2 * len(fam)          # abundant iff 2*count >= |F|
        abundant = any(2 * c >= len(fam) for c in present)
        if not abundant:
            failures += 1
            print(f"  FAIL n={n}: UC family with a 3-set but NO abundant element: {sorted(fam)}")
    print(f"n={n}: UC families containing a 3-set = {total_uc_with_3set}, "
          f"lacking an abundant element = {failures}")

print("\nIf every n shows failures=0, the 'refuted' finding is an encoding bug "
      "(no union-closed counterexample exists on these ground sets).")
