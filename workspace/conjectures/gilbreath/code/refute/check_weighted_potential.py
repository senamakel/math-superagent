"""Hand-check the weighted-excess-potential refutation.

Claim R-weighted-excess-potential: exists summable w_i>=0, w_1>0, such that
P(A) = sum w_i d_i (d_i = max(0,A(i)-2)) is non-increasing under the row map
for EVERY nonneg-integer absolute-difference array.

Family A_L = (1, 0,0,...,0, Z): Z in column L, all others 0.
  parent interior = (0,...,0,Z) length L   -> P = w_L (Z-2)
  child  interior = (0,...,0,Z) length L-1 -> P = w_{L-1} (Z-2)
  monotonicity (child <= parent) forces w_{L-1} <= w_L.
Holds for every L -> w_1 <= w_2 <= ... -> all >= w_1 > 0 -> NOT summable.
Refuted, provided the monotonicity checks on the concrete family are exact.
"""
def d(a):
    return max(0, a - 2)

def child(interior):
    """full row (1)+interior; child row; return child interior (drop front)."""
    row = [1] + list(interior)
    crep = [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
    return tuple(crep[1:])   # drop front

def check(L, Z):
    interior = tuple(0 for _ in range(L-1)) + (Z,)
    ci = child(interior)
    # P_parent = w_L (Z-2), P_child = w_{L-1} (Z-2). Verify shapes:
    assert interior[-1] == Z and len(interior) == L
    assert ci == tuple(0 for _ in range(L-2)) + (Z,), (L, Z, ci)
    # defects
    pp = d(Z); pc = d(Z)
    print(f"L={L}, Z={Z}: parent interior ends {interior[-1]}, "
          f"child interior ends {ci[-1]}, both defect d(Z)={pp}; "
          f"forces w_{L-1} <= w_{L}")

for L in range(2, 7):
    check(L, 8)
    check(L, 6)
print("All concrete descendants have the same shape (1,0,...,0,Z) with Z one column closer.")

# show summability contradiction
print("\nSince w_1 <= w_2 <= ... and w_1 > 0, each w_i >= w_1 > 0, so")
print("sum_i w_i >= sum_i w_1 = +infinity. Not summable. REFUTED.")
