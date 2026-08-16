"""Explicitly hand-check the canonical minimal witness for the refutation.
n=4: h=0010 vs h'=0100 -> equal C_1 (pair correlations through lag 1) but S^2 differs.
Prints the actual C_1 counts and S^2 for both, so the witness is on record."""
from lib.collapse import S2

def pair_counts(h, n, K):
    out = []
    for k in range(1, K + 1):
        for a in (0, 1):
            for b in (0, 1):
                c = 0
                for i in range(0, n - k):
                    if h[i] == a and h[i + k] == b:
                        c += 1
                out.append(c)
    return tuple(out)

h  = [0, 0, 1, 0]
hp = [0, 1, 0, 0]
print("n=4, h=0010, h'=0100")
print("C_1(h)  =", pair_counts(h, 4, 1))
print("C_1(h') =", pair_counts(hp, 4, 1))
print("S^2(h)  =", S2(4, h))
print("S^2(h') =", S2(4, hp))
print("C_1 equal:", pair_counts(h, 4, 1) == pair_counts(hp, 4, 1))
print("S^2 differ:", S2(4, h) != S2(4, hp))
