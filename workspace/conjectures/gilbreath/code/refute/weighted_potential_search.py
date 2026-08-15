"""Search for a componentwise defect increase refuting R-weighted-excess-potential.

The rung claims: there exist summable weights w_i >= 0, w_1 > 0, such that for
EVERY nonneg-integer absolute-difference array A (with leading entry 1, interior
even), P(A) = sum_i w_i d_i is non-increasing under the row operator, where
d_i = max(0, A(i) - 2).

If we find a row A and its image A' with d'(i) >= d(i) for all i and d'(j) > d(j)
for some j, then sum w_i d'_i > sum w_i d_i for any nonneg weights with w_j > 0,
refuting the claim for ALL weight sequences.

We search over small rows. Interior entries are even (2-then-odds shape).
"""
import itertools

def defects(interior):
    """interior is a list of even interior entries; defects are max(0, a-2)."""
    return tuple(max(0, a - 2) for a in interior)

def next_row(interior):
    """Interior of the next row: A(1) = |1 - A(1)|, A(i) = |A(i) - A(i+1)|.
    A[0]=1 leading marker."""
    prev = [1] + list(interior)
    out = []
    for i in range(len(interior)):
        out.append(abs(prev[i] - prev[i+1]))
    return tuple(out)

def comp_dominates(a, b):
    """True if a[i] >= b[i] for all i and a[j] > b[j] for some j (same length)."""
    n = min(len(a), len(b))
    if any(a[i] < b[i] for i in range(n)):
        return False
    # treat model as truncated to common length; require strict somewhere in common
    return any(a[i] > b[i] for i in range(n))

def main():
    print("Searching for componentwise defect increase (child >= parent, strict somewhere)")
    print("over 2-then-odds rows with interior entries in {0,2,4} (even small alphabet).")
    found = 0
    for L in range(2, 9):
        count = 0
        for interior in itertools.product((0, 2, 4), repeat=L):
            child = next_row(interior)
            # child interior has length L (same). defects:
            dp = defects(interior)
            dc = defects(child)
            if comp_dominates(dc, dp):
                found += 1
                if count < 5:
                    print(f"  L={L} parent={interior} d_parent={dp}")
                    print(f"        child ={child} d_child ={dc}  DOMINATES parent")
                count += 1
        if count:
            print(f"L={L}: {count} dominating transitions (of {3**L}).")
    print(f"TOTAL dominating transitions found: {found}")

main()
