#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.gilbreath import diff_block
import itertools

def build_triangle(bits, n):
    seq = [2, 3]
    seq.append(seq[-1] + 2)
    for j in range(2, n):
        bit = bits[j-2]
        G = 4 - 2*bit
        seq.append(seq[-1] + G)
    rows = [seq]
    for k in range(1, n):
        rows.append(diff_block(rows[-1]))
    return rows

def nu2_of(rows, n):
    d = [rows[k][n-k] for k in range(n)]
    tail = d[2:-1]
    i = len(tail)
    while i > 0 and tail[i-1] in (0, 2):
        i -= 1
    cyc = tail[i:]
    return cyc.count(2)

def main():
    for n in range(4, 15):
        viol_half = []
        viol_23 = []
        min_ratio = 1e9
        for bits in itertools.product([0,1], repeat=n-2):
            rows = build_triangle(bits, n)
            nu2 = nu2_of(rows, n)
            w = sum(bits)
            if w == 0:
                continue
            r = nu2/w
            if r < min_ratio:
                min_ratio = r
            if nu2 < w/2:
                viol_half.append((tuple(bits), nu2, w))
            if nu2 < (2/3)*w:
                viol_23.append((tuple(bits), nu2, w))
        print(f"n={n}: nonzero-w strings checked; min nu2/w={min_ratio:.3f} "
              f"viol nu2<w/2: {len(viol_half)}  viol nu2<(2/3)w: {len(viol_23)}", flush=True)
        if viol_half:
            print("   first nu2<w/2 example:", viol_half[0], flush=True)
        if viol_23:
            print("   first nu2<(2/3)w example:", viol_23[0], flush=True)

if __name__ == "__main__":
    main()
