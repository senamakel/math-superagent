import numpy as np

def submask(s, d):
    return (s & d) == s

def zeta_matrix(n):
    Z = np.zeros((n, n), dtype=int)
    for d in range(n):
        for s in range(n):
            Z[d][s] = 1 if submask(s, d) else 0
    return Z

for n in (4, 8, 16):
    Z = zeta_matrix(n)
    Z2 = (Z @ Z) % 2
    print(f"n={n}: Z^2 == I mod 2? {np.array_equal(Z2, np.eye(n, dtype=int))}")

def gram_disjoint(n):
    Z = zeta_matrix(n)
    G = (Z @ Z.T) % 2
    G2 = np.zeros((n, n), dtype=int)
    for d in range(n):
        for dp in range(n):
            G2[d][dp] = 1 if (d & dp) == 0 else 0
    return np.array_equal(G, G2)

for n in (4, 8, 16, 32):
    print(f"n={n}: G_{d,d'} == [d&d'==0]? {gram_disjoint(n)}")

# golden-ratio spectrum of disjointness matrix
from sympy import Matrix
for m in (2,3,4):
    # G = kron power of [[1,1],[1,0]]
    M = Matrix([[1,1],[1,0]])
    G = M
    for _ in range(m-1):
        G = Matrix([[G, G], [G, Matrix.zeros(*G.shape)]])
    ev = G.eigenvals()
    print(f"m={m}: eigenvalues (multiplicity) = {ev}")
