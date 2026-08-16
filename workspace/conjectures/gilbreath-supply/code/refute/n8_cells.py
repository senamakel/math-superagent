# Verify the n=8 fold-cell parity pattern used in the TPTP encoding.
# Cell T(n,d) = XOR over submasks o of d of h[n-1-d+o], d in [2,n-1].
def cells(n=8):
    out = {}
    for d in range(2, n):
        idx = [n-1-d+o for o in range(d+1) if (o & d) == o]
        out[d] = idx
    return out

for d, idx in cells().items():
    print(f"T({8},{d}) = XOR of h{idx}  (parity positions)")
