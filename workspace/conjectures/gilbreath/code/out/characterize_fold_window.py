"""Characterise exactly what lib.rule90fold computes and which fold reproduces
true nu2.  Compares:
  (1) lib.fold_weight_h(h, m)     -- abstract m-bit h, windows [m-k, m-1]
  (2) lib.fold_weight(hcol, n)    -- hcol indexed by column c, windows [n-k, n-1]
  (3) true nu2 (canonical cycle_and_nu2)
  (4) the geometric suffix fold ending at column n-1 (this run's exact match)
"""
from lib.rightdiag import incremental_diagonals, cycle_and_nu2
from lib.rule90fold import fold_weight_h, fold_weight, fold_cell_bit


def thue_morse(j):
    return bin(j).count('1') & 1


def build_q(D):
    q = [2, 3]
    for j in range(D + 2):
        q.append(q[-1] + (2 if thue_morse(j) else 4))
    return q


def hcol_of(q, n):
    return {c: ((q[c + 1] - q[c]) // 2) & 1 for c in range(2, n)}


def geometric_suffix_fold(q, n, hcol):
    """Windows [n-k, n-1] (ending at column n-1), k=2..n-2."""
    cnt = 0
    for k in range(2, n - 1):
        x = 0
        for i in range(k):
            if (i & (k - 1)) == i:
                x ^= hcol[n - k + i]
        cnt += x
    return cnt


def main():
    D = 4000
    q = build_q(D)
    ds = list(incremental_diagonals(q))
    for n in (100, 4000):
        diag = ds[n]
        tau, nu2 = cycle_and_nu2(diag)
        hcol = hcol_of(q, n)
        # lib fold_weight needs hcol as a list indexed by column;
        # hcol keys 2..n-1 -> make list with 0,1 unused.
        hcol_list = [0] * (n + 1)
        for c in range(2, n):
            hcol_list[c] = hcol[c]
        fw_col = fold_weight(hcol_list, n)          # windows [n-k, n-1]
        m = n - 2
        h = [hcol_list[c] for c in range(2, n)]     # h[0..m-1]=cols 2..n-1
        fw_h = fold_weight_h(h, m)                  # abstract, windows [m-k,m-1]
        # indexed fold cell bits over the same k=2..n-1 range
        gtw = geometric_suffix_fold(q, n, hcol)
        print(f"n={n}: TRUE nu2 = {nu2}")
        print(f"   lib.fold_weight(hcol,n)   = {fw_col}  ==nu2? {fw_col == nu2}")
        print(f"   lib.fold_weight_h(h,m)    = {fw_h}  ==nu2? {fw_h == nu2}")
        print(f"   geometric suffix-fold (k=2..n-2) = {gtw}  ==nu2? {gtw == nu2}")
        print()


if __name__ == '__main__':
    main()
