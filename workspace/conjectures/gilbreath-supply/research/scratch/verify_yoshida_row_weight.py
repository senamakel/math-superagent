"""Verify Yoshida's row-weight consequence for p=2: W(B(t)) = 2^popcount(t).
B(t) is the t-th row of the Pascal matrix mod 2 (entries _tC_r mod 2), which
is nonzero at exactly the submasks r of t (Lucas). W = number of nonzero entries.
Also verify the full-matrix-bound W(B) = 3^m for L=2^m (from Corollary 1).
"""
import math

def row_weight(t):
    # entries C(t, r) mod 2 nonzero iff r is a submask of t (Lucas, p=2)
    return 2 ** bin(t).count("1")

def full_weight(L):
    # number of nonzero entries in the L x L Pascal matrix mod 2
    return 3 ** (L.bit_length() - 1) if L and (L & (L - 1)) == 0 else None  # only powers of 2

def brute_row_weight(t):
    # literally count nonzero C(t,r) mod 2 over r=0..t
    return sum(1 for r in range(t+1) if (math.comb(t, r) % 2) == 1)

ok = True
for t in range(0, 64):
    if row_weight(t) != brute_row_weight(t):
        print("MISMATCH", t, row_weight(t), brute_row_weight(t))
        ok = False
print("row-weight W(B(t)) = 2^popcount(t):", "OK" if ok else "FAIL")

# full matrix for L=8,16
for m in range(1, 7):
    L = 2**m
    # brute count nonzero entries
    cnt = sum(1 for t in range(L) for r in range(t+1) if math.comb(t, r) % 2 == 1)
    print(f"L=2^{m}={L}: W(B)={cnt}, Corollary predicts 3^{m}={3**m} ->", cnt == 3**m)
