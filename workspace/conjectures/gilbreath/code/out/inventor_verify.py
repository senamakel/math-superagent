"""
Inventor pre-proposal verification (exact integers).

Checks two candidate core identities before they are written as proposals:

(A) Morphological identity: |a-b| = max(a,b) - min(a,b)  (dilation minus erosion),
    and threshold commutation:  [max(a,b)>=t] = [a>=t] OR [b>=t],
                                [min(a,b)>=t] = [a>=t] AND [b>=t].
    Consequence: A_{k+1}(i) = D(A_k)(i) - E(A_k)(i) identically.

(B) Turning-point structure of the gap window: investigate whether A_k(1)
    admits an exact expression in terms of the local extrema (turning points)
    of the gap window g_1..g_k. This is exploratory: print A_k(1) and the
    extrema of the window for small k.

(C) The naive "independent threshold layers" claim, shown FALSE as a sanity
    check:  [|a-b| >= t] != [a>=t] XOR [b>=t]  in general.
"""
import json

def T(x):
    return [abs(x[i] - x[i+1]) for i in range(len(x)-1)]

# --- prime gaps from A_1 (positions 1..): A_1 = |primes differences|
# primes: 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
A0 = primes
A1 = T(A0)          # (1,2,2,4,2,4,2,4,6,2,...)
gaps = A1[1:]       # gaps after the first odd entry: prime gaps 2,2,4,2,4,2,4,6,2,6,4,...

print("=== (A) morphological identity |a-b| = max - min ===")
# verify A_{k+1} = D(A_k) - E(A_k) for the real rows
row = A1
maxdepth = 8
ok_A = True
left_edges = []
for k in range(maxdepth):
    D = [max(row[i], row[i+1]) for i in range(len(row)-1)]
    E = [min(row[i], row[i+1]) for i in range(len(row)-1)]
    DE = [D[i] - E[i] for i in range(len(D))]
    nxt = T(row)
    if DE != nxt:
        ok_A = False
        print("MISMATCH at depth", k)
        break
    left_edges.append(nxt[1] if len(nxt) > 1 else None)  # A_{k+1}(1)
    row = nxt
print("morphological identity A_{k+1}=D-E holds to depth", maxdepth, ":", ok_A)

print("\n=== (C) naive threshold-XOR identity (expected FALSE) ===")
# find a counterexample
def thresh(v, t): return 1 if v >= t else 0
for a in range(0, 8):
    for b in range(0, 8):
        for t in range(1, 6):
            lhs = thresh(abs(a-b), t)
            rhs = thresh(a, t) ^ thresh(b, t)
            if lhs != rhs:
                print("counterexample a=%d b=%d t=%d : [|a-b|>=t]=%d, [a>=t]XOR[b>=t]=%d" % (a,b,t,lhs,rhs))
                a = b = 99; break
        if a == 99: break
    if a == 99: break

print("\n=== (B) turning-point structure of gap window vs A_k(1) ===")
# A_k(1) for the prime gaps
row = gaps
depth = 10
for k in range(depth):
    # A_k(1) is row[0] where row = k-fold |diff| of gaps, with row = gaps at k=1 level?
    # A_1(1) = gaps[0] = 2 ; A_2(1) = |g1-g2| = T(gaps)[0]; etc.
    print("k=%2d  A_k(1)=%3d  window g1..g_k=%s" % (k+1, row[0], gaps[:k+1]))
    row = T(row)

# local extrema of the gap window: positions i where g_i is not between g_{i-1},g_{i+1}
def extrema(w):
    out = []
    for i in range(len(w)):
        if i == 0 or i == len(w)-1:
            out.append((i, w[i]))
        else:
            if (w[i] - w[i-1]) * (w[i] - w[i+1]) > 0:
                out.append((i, w[i]))
    return out

print("\n extrema (turning points) of successive windows:")
for k in range(1, 10):
    w = gaps[:k+1]
    print("  window g1..g%d = %s  extrema=%s" % (k+1, w, extrema(w)))
