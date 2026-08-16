"""Run the existing sparse-image curve to test G-sup-sw vs G-weak-input-strictness."""
import sys
sys.path.insert(0, 'code/out')
from sparse_image_curve import phi_rows_lucas, gauss_rank


def image_weight_rows(rows, h, ncols):
    wt = 0
    for row in rows:
        s = 0
        for j in row:
            if j < len(h):
                s ^= h[j]
        wt += s
    return wt


print("=== Phi_n rank/nullity (windowed / right-diagonal construction) ===")
print(f"{'n':>3} {'nrows':>5} {'ncols':>5} {'rank':>5} {'nullity(n-2 dom)':>18}")
for n in range(2, 21):
    rows = phi_rows_lucas(n)
    ncols = n
    rk = gauss_rank(rows, ncols)
    dom = ncols
    print(f"{n:>3} {len(rows):>5} {ncols:>5} {rk:>5} {dom-rk:>18}")
