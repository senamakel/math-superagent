"""Verify the spectral-interlacing foundational lemma for the cube.

The technique that (if valid) would give a maximum-degree lower bound goes by
linear algebra, and is checkable directly:

Let A be the adjacency matrix of Q_n (0/1, symmetric, n-regular). Let x be a
signed vector built by the tensor recursion ((-1) x, y) so that the *signed*
matrix A' = diag(x) A diag(x) satisfies (A')^2 = n·I. Then A' has eigenvalues
±sqrt(n). For any principal submatrix B of A' on a set S of size m, Cauchy
(interlacing) gives lambda_max(B) >= #(eigenvalues of A' >= sqrt(n) that
interlace) ... in fact lambda_max(B) >= sqrt(n) when m > n/2 ... i.e. m > half
the dimension of A' = n_vertices/2.

Concretely: since eigenvalues of A' are ±sqrt(n) each with multiplicity
2^{n-1}, and interlacing says an m x m principal submatrix has eigenvalues that
interlace the full spectrum, when m > 2^{n-1} (more than half the eigenvalues
are +sqrt(n)... but only 2^{n-1} of them) we get lambda_max(B) >= sqrt(n).
Then lambda_max(B) <= max internal degree of S (Perron / spectral radius of a
graph's adjacency is <= max degree), so max internal degree >= sqrt(n).

Here we verify the two pure linear-algebra steps on small n:
  (1) there is a signed adjacency A' with (A')^2 = n I (a "Hadamard-like"
      sign assignment, the Hadamard matrix);
  (2) a principal submatrix of a matrix with min|spectral| = sqrt(n) on >half
      the rows has an eigenvalue of magnitude >= sqrt(n) (interlacing check).
This is the *technique*; whether the sign assignment exists for this exact
problem statement is the question the run must settle, not something we assert.
"""
import numpy as np

def hadamard(n):
    """Sylvester Hadamard matrix of order 2^n (entries +1/-1)."""
    H = np.array([[1]])
    for _ in range(n):
        H = np.block([[H, H], [H, -H]])
    return H

def signed_adjacency_eigenvalues(n):
    H = hadamard(n)
    # A_ij = 1 n=distance (Hamming distance 1), 0 otherwise.
    N = 1 << n
    A = np.zeros((N, N))
    for i in range(N):
        for k in range(n):
            j = i ^ (1 << k)
            A[i, j] = 1.0
    Aprime = H * A * H  # diag(H signs) A diag(H signs): H is orthogonal yes
    return np.linalg.eigvalsh(Aprime)

def check_interlacing(n, m=None):
    """For the principal submatrix on a random >half set, check lambda_max >= sqrt(n)."""
    ev = signed_adjacency_eigenvalues(n)
    s = np.sqrt(n)
    N = 1 << n
    rng = np.random.default_rng(0)
    if m is None:
        m = (1 << (n-1)) + 1
    # random set of size m
    perm = rng.permutation(N)
    S = perm[:m]
    H = hadamard(n)
    A = np.zeros((N, N))
    for i in range(N):
        for k in range(n):
            j = i ^ (1 << k)
            A[i, j] = 1.0
    Aprime = H * A * H
    B = Aprime[np.ix_(S, S)]
    lam_max = np.linalg.eigvalsh(B)[-1]
    return lam_max, s

for n in range(2, 6):
    ev = signed_adjacency_eigenvalues(n)
    lam_max_full = np.max(np.abs(ev - np.sqrt(n)))
    print(f"n={n}: signed adjacency ev close to sqrt(n)? max_abs diff from +sqrt(n) = {lam_max_full:.2e}")
    lam, s = check_interlacing(n)
    print(f"   random {(1<<(n-1))+1}-vertex principal submatrix: lambda_max = {lam:.4f} >= sqrt(n)={s:.4f}? {lam >= s - 1e-9}")
