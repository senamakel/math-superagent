import numpy as np
from itertools import combinations

def huang_matrix(n):
    if n == 1:
        return np.array([[0,1],[1,0]], dtype=float)
    A = huang_matrix(n-1)
    I = np.eye(2**(n-1))
    Z = np.zeros((2**(n-1),2**(n-1)))
    return np.block([[A, I],[I, -A]])

def grow(A):
    n = A.shape[0]
    I = np.eye(n)
    return np.block([[A,I],[I,-A]])

def f_exact_brute(n):
    # exhaustive: min over S with |S|=2^{n-1}+1 of internal max degree
    N = 2**n
    verts = range(N)
    # adjacency
    adj = {i: set() for i in verts}
    for i in range(N):
        for j in range(i+1,N):
            if (i^j) in (1<<k for k in range(n)):
                adj[i].add(j); adj[j].add(i)
    best = None
    import itertools
    for S in itertools.combinations(verts, 2**(n-1)+1):
        Sset = set(S)
        md = max(sum(1 for u in adj[v] if u in Sset) for v in S)
        if best is None or md < best:
            best = md
    return best

# independent: verify interlacing & degree bound for random S at n=7,8
for n in (6,7,8):
    A = huang_matrix(n)
    eig = np.linalg.eigvalsh(A)
    sqrtn = np.sqrt(n)
    assert np.allclose(sorted(eig, reverse=True)[:2**(n-1)], sqrtn, atol=1e-6)
    N = 2**n
    m = 2**(n-1)+1
    rng = np.random.default_rng(0)
    for _ in range(50):
        S = rng.choice(N, size=m, replace=False)
        B = A[np.ix_(S,S)]
        lmax = np.linalg.eigvalsh(B)[-1]
        # interlacing: lmax >= sqrt(n)
        assert lmax >= sqrtn - 1e-6, (n, lmax, sqrtn)
        # degree bound: lmax <= Delta(H)
        Sset=set(S)
        # adjacency on cube restricted
        Delta = 0
        for v in S:
            d=0
            for k in range(n):
                u = v ^ (1<<k)
                if u in Sset: d+=1
            Delta=max(Delta,d)
        assert lmax <= Delta + 1e-6, (n, lmax, Delta)
    print(f"n={n}: spectrum=±{sqrtn:6.3f} (mult 2^{n-1}), interlacing & degree bound hold on 50 random S; "
          f"max observed tightness: raw lmax={lmax:.4f}, Delta={Delta}")

# exact small f via brute force (independent small-check oracle)
for n in range(1,5):
    print(f"f_exact({n}) =", f_exact_brute(n))
