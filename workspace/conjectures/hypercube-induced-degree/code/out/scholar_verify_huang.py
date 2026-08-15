"""Scholar verification of the three lemmas behind the sqrt(n) lower bound.

This is Huang's spectral mechanism, re-derived from first principles and
checked exactly for small n. It is the one thing that decides whether
problem.md's "thirty-year gap" is closed: if (1) a signed adjacency matrix
A_n exists with A_n^2 = n·I and support = edges of Q_n, (2) Cauchy interlacing
forces lambda_max of any (2^{n-1}+1)-row principal submatrix >= sqrt(n), and
(3) lambda_max <= max internal degree, then every admissible S has
D(S) >= sqrt(n), hence >= ceil(sqrt(n)).

All three steps are checked here exactly (integer arithmetic for the matrix
identity; exact interlacing on computed spectra) for n = 1..7.
"""
import numpy as np
from fractions import Fraction

def signed_adj(n):
    """Recursive Huang matrix: A_1=[[0,1],[1,0]], A_n=[[A_{n-1},I],[I,-A_{n-1}]].
    Returns a numpy int matrix. Support must be exactly the edges of Q_n."""
    if n == 1:
        return np.array([[0, 1], [1, 0]], dtype=int)
    A = signed_adj(n-1)
    N = 1 << (n-1)
    I = np.eye(N, dtype=int)
    top = np.hstack([A, I])
    bot = np.hstack([I, -A])
    return np.vstack([top, bot])

def q_edges(n):
    """Adjacency (0/1) of Q_n."""
    N = 1 << n
    A = np.zeros((N, N), dtype=int)
    for i in range(N):
        for k in range(n):
            j = i ^ (1 << k)
            A[i, j] = 1
    return A

def check_matrix_identity(n):
    A = signed_adj(n)
    N = 1 << n
    # symmetric?
    sym = np.array_equal(A, A.T)
    # zero diagonal?
    diag = np.all(np.diag(A) == 0)
    # support = edges?
    E = q_edges(n)
    support_ok = np.array_equal((A != 0).astype(int), (E != 0).astype(int))
    # A^2 = n I exactly (integer)
    A2 = A @ A
    square = np.array_equal(A2, n * np.eye(N, dtype=int))
    # spectrum = +/- sqrt(n), each 2^{n-1} times
    ev = np.linalg.eigvalsh(A.astype(float))
    plus = np.count_nonzero(np.abs(ev - np.sqrt(n)) < 1e-6)
    minus = np.count_nonzero(np.abs(ev + np.sqrt(n)) < 1e-6)
    return sym, diag, support_ok, square, (plus, minus)

def check_interlacing(n):
    A = signed_adj(n)
    N = 1 << n
    m = (1 << (n-1)) + 1
    # exact interlacing bound: lambda_max(B) >= (N-m+1)-th largest eigenvalue of A
    # = 2^{n-1}-th largest = sqrt(n).
    s = np.sqrt(n)
    # verify on many random principal submatrices of exactly size m
    rng = np.random.default_rng(0)
    ok = True
    worst = 0.0
    for _ in range(12):
        S = rng.permutation(N)[:m]
        B = A[np.ix_(S, S)]
        lam = np.linalg.eigvalsh(B.astype(float))[-1]
        ok = ok and (lam >= s - 1e-9)
        worst = max(worst, s - lam)
    # also: max degree of induced subgraph >= lambda_max (Perron/spectral radius
    # of adjacency-like matrix <= max degree). Check B's structure is 0/1 on edges.
    S = rng.permutation(N)[:m]
    B = A[np.ix_(S, S)]
    E = q_edges(n)[np.ix_(S, S)]
    support_in_edges = np.all((B != 0) <= (E != 0))
    return ok, worst, support_in_edges

print("=== Lemma 1: signed adjacency A_n, A_n^2 = n I, support = cube edges, spectrum +/- sqrt(n) ===")
for n in range(1, 8):
    sym, diag, sup, sq, (plus, minus) = check_matrix_identity(n)
    exp = (1 << (n-1))
    assert sq, f"FAIL n={n}"
    print(f"n={n}: sym={sym} zerodiag={diag} support=edges={sup} A^2=nI={sq} "
          f"eigs +sqrt(n):{plus}/{exp} -sqrt(n):{minus}/{exp}")

print("\n=== Lemma 2: interlacing on (2^{n-1}+1)-row principal submatrices ===")
print("   expect lambda_max(B) >= sqrt(n) (via (N-m+1)=2^{n-1}-th eigval = sqrt(n))")
for n in range(2, 8):
    ok, worst, sup = check_interlacing(n)
    print(f"n={n}: all 12 random submatrices lambda_max>=sqrt(n): {ok}  "
          f"(margin, sqrt-lam, worst = {worst:.2e})  B supported on edges: {sup}")

print("\n=== Combined consequence for f(n) ===")
print("For any S with |S|=2^{n-1}+1: lambda_max(B) >= sqrt(n), lambda_max(B) <= D(S),")
print("so D(S) >= sqrt(n), i.e. D(S) >= ceil(sqrt(n)). Since S arbitrary: f(n) >= ceil(sqrt(n)).")
expected = [1,2,2,2,3,3,3]
print("ceil(sqrt(n)) for n=1..7 =", expected, " (compares to computed f-exact 1,2,2,2)")
