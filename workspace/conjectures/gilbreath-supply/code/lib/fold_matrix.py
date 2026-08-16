"""Fold matrix Phi_n as the submask-XOR matrix Z, plus exact F2 algebra.

SUPPLY fold (problem.md fact 1): the depth-d cell is

    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o],   d in [2,n-1],
    nu2(n) = wt(Phi_n h) = #{ d in [2,n-1] : T(n,d) = 1 }.

Substituting s = d - o (no borrow, since o is a submask of d) and writing
g[s] = h[n-1-s],

    T(n,d) = XOR_{ s : (s & d) == s } g[s] = sum_s Z[d][s] g[s],

with the SUBMASK-XOR matrix

    Z[d][s] = 1 if (s & d) == s  (s a bitwise submask of d), else 0.

The full square Z on indices 0..n-1 is UNIT LOWER-TRIANGULAR:
  (A) s a submask of d  =>  s <= d  (bitwise submask implies numeric <=), and
  (B) Z[d][d] = 1.
So Z is invertible (determinant 1), rank n, a bijection F2^n -> F2^n.

The operator the fold actually applies is M = Z with the rows d = 0, 1 dropped
(only d in [2,n-1] ever enters nu2). Because Z is a bijection,

    g in ker M  <=>  v = Zg  has v_2 = ... = v_{n-1} = 0,
                   i.e. only the two image coordinates v_0, v_1 are free,

so dim ker M = 2 and rank M = n - 2. The two dropped directions (the
submask-sums at d = 0 and d = 1) are exactly the alternating vectors
even-alt = (1,0,1,0,...) and odd-alt = (0,1,0,1,...); we verify directly that
each lies in ker M (even/odd submask counts are 0 mod 2 for every d >= 2) and
that they are independent, so they span the kernel. all-ones = even XOR odd is
also in the kernel, consistent with closed door 1.

All arithmetic exact (F2 bits / integer counts). Matrices are lists of rows,
each row a list of 0/1.
"""


def submasks(d):
    """Yield every bitwise submask of d (incl. d and 0), largest first."""
    s = d
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & d


def submask_matrix(n):
    """Full n x n Z with Z[d][s] = 1 iff s is a bitwise submask of d."""
    return [[1 if (s & d) == s else 0 for s in range(n)] for d in range(n)]


def fold_operator(n):
    """M = Z with rows d=2..n-1 kept, columns 0..n-1: the (n-2) x n map the
    fold actually applies (the matrix whose weight nu2(n) = wt(M g) counts)."""
    return [[1 if (s & d) == s else 0 for s in range(n)] for d in range(2, n)]


def is_unit_lower_triangular(mat):
    """True iff mat is square, 1 on the diagonal, 0 above the diagonal."""
    n = len(mat)
    for i in range(n):
        if mat[i][i] != 1:
            return False
        for j in range(i + 1, n):
            if mat[i][j] != 0:
                return False
    return True


def rank_f2(mat):
    """Row rank of a 0/1 matrix over F2 by Gaussian elimination. Exact."""
    if not mat:
        return 0
    m, n = len(mat), len(mat[0])
    A = [row[:] for row in mat]
    rank = 0
    for col in range(n):
        piv = None
        for r in range(rank, m):
            if A[r][col]:
                piv = r
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(m):
            if r != rank and A[r][col]:
                for c in range(col, n):
                    A[r][c] ^= A[rank][c]
        rank += 1
    return rank


def matvec(M, v):
    """M v over F2: length-len(M) result, each entry a parity."""
    return [sum(M[r][j] * v[j] for j in range(len(v))) % 2 for r in range(len(M))]


def in_kernel(M, v):
    """M v == 0 over F2."""
    return all(x == 0 for x in matvec(M, v))
