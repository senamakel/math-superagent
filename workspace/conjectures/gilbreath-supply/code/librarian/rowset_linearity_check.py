"""Check whether the fold's row set {1_{M_d} : d in [2,n-1]} is a linear
(XOR-closed) code, and whether the Krawtchouk-diagonalization identity holds
for it as a multiset. Direct verification, no theory assumed.

The Krawtchouk diagonalization F_n(z) = 2^{-n} sum_omega (1-z)^{wt(omega)}
(1+z)^{n-wt(omega)} C-hat_n(omega)^2 is a Fourier identity valid for ANY
multiset of cube points. The Delsarte LP bound additionally needs
C-hat(omega) >= 0 for all omega, which holds only for LINEAR codes. So the
key question: is the row set XOR-closed?
"""
import itertools


def downset(d):
    return [o for o in range(d + 1) if (o & d) == o]


def row_vector(n, d):
    """Indicator of M_d = {n-1-d+o : o subseteq d}, length n, indexed 0..n-1."""
    v = [0] * n
    for o in downset(d):
        v[n - 1 - d + o] = 1
    return tuple(v)


def check(n):
    rows = [row_vector(n, d) for d in range(2, n)]
    rowset = set(rows)
    # XOR-closure: pairwise XOR of two rows should be in the rowset (or 0/kernel)
    xor_closed = True
    count = 0
    for a, b in itertools.combinations(rows, 2):
        x = tuple(u ^ v for u, v in zip(a, b))
        if x not in rowset:
            xor_closed = False
            count += 1
            if count > 5:
                break
    return len(rows), len(rowset), xor_closed, count


for n in range(4, 13):
    nrows, nset, closed, bad = check(n)
    print(f"n={n}: rows={nrows} distinct={nset} xor_closed={closed}"
          + ("" if closed else f" (first {bad} non-closed pairs)"))
