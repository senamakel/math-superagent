"""Exact integer first_w (mean nu2/n >= 0.40), scan from w=1, n<=8192.
Guaranteed-correct via exact rational comb; reproduces operator authority series.
"""
from math import comb, log2
def pc(x): return bin(x).count('1')
def P_odd_int(m, w, n):
    lo = max(0, m - (n - w)); hi = min(w, m); num = 0
    for k in range(lo, hi + 1):
        if k & 1:
            num += comb(w, k) * comb(n - w, m - k)
    return num / comb(n, m)
def E(n, w):
    return sum(P_odd_int(2**pc(d), w, n) for d in range(2, n)) / n
if __name__ == "__main__":
    rows = []
    for m in range(3, 14):   # n = 8 .. 8192
        n = 2**m
        found = None
        for w in range(1, n):
            if E(n, w) >= 0.40:
                found = w; break
        rows.append((n, found))
        print(f"n={n:6d}  first_w={found:4d}  w/n={found/n:.6f}  "
              f"log2(w)={log2(found):6.2f}  log2(w)/log2(n)={log2(found)/log2(n):.4f}")
    # operator authoritative series for powers of two
    op = {8:3,16:3,32:5,64:7,128:11,256:16,512:24,1024:35,2048:52,4096:77}
    print("\noperator-series check (powers of two):")
    ok = all((n, f) == (n, op[n]) for n, f in rows if n in op)
    print("  match:", ok)
    print("  op:", [op[n] for n in sorted(op)])
    print("  us:", [dict(rows)[n] for n in sorted(op)])
