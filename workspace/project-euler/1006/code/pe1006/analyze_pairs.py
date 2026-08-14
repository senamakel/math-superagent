"""Deep structure of the factor matrix: columns (N(i;k)) and pair correlations
C(i,l;k) = # distinct length-k factors with a 1 in both positions i and l.

Goal: find the structure needed to compute Psi(k) = sum_j val(w_j)^2 for huge k.
Psi(k) = sum_i N(i) 10^{2(k-1-i)} + 2 sum_{i<l} C(i,l) 10^{2k-2-i-l}
so we need N(i;k) (diagonal) and C(i,l;k) (cross). Probe their structure.

Exact integer arithmetic.
"""
import json
import os

MOD = 101001001
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")


def load_factors():
    return json.load(open(DATA))


def main():
    data = load_factors()

    print("Column structure of the (k+1)xk factor matrix (1=1,0=0), k=8,12,14,20:")
    for k in [8, 12, 14, 20]:
        facs = data[str(k)]
        print(f"\nk={k}. Columns (positions 0..{k-1}, 1=leftmost):")
        for i in range(k):
            # which factors have a 1 at position i
            bits = [1 if f[i] == '1' else 0 for f in facs]
            print(f"  col{i}: {bits}   (#ones N={sum(bits)})")

    print("\n\nPair-correlation C(i,l;k) = # factors with 1 at both i and l.")
    print("Look at C for fixed gap d=l-i as i varies.")
    for k in [10, 16, 20]:
        facs = data[str(k)]
        print(f"\n--- k={k} ---")
        for d in [1, 2, 3, 5, 7]:
            row = []
            for i in range(0, k - d):
                l = i + d
                c = sum(1 for f in facs if f[i] == '1' and f[l] == '1')
                row.append(c)
            print(f"  gap d={d}: C(i,i+{d}) = {row}")


if __name__ == "__main__":
    main()
