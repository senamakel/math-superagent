"""
Structure probe for the SUPPLY fold, to ground inventor proposals.

Facts we hold (settled, cited not re-derived):
  T(n,d) = XOR_{o submasks of d} h[n-1-d+o]  (linearisation + Lucas)
  eps_d = (-1)^{T(n,d)} = prod_{j in M_d} x_j,  x_j = (-1)^{h_j}
  M_d = {n-1-d+o : o subset of d}   (fold row, reflected downset)
  S(n) = sum_{d=2}^{n-1} eps_d ;  nu2 = (n-2-S)/2
  eps_d eps_d' = prod_{j in M_d XOR M_d'} x_j
  S^2 = (n-2) + 2 sum_{d<d'} eps_d eps_d'

We probe:
  (1) the read-cone of each position j: C_j = {d in [2,n-1] : j in M_d}
  (2) the multiset of symmetric differences M_d XOR M_d' and their sizes
  (3) the witness e_6 vs e_5 and what separates them
  (4) stratification of the S^2 monomial set by "contiguous order" = minimal
      number of contiguous windows (of any length) needed to cover the support.
"""
import itertools

def pc(x):
    return bin(x).count('1')

def submask_xor(n, d, h):
    """T(n,d) over F2."""
    t = 0
    for o in range(d+1):
        if o & d == o:  # o submask of d
            j = n-1-d+o
            if 0 <= j < n:
                t ^= h[j]
    return t

def row_M(n, d):
    """M_d = set of positions j read at depth d."""
    return {n-1-d+o for o in range(d+1) if (o & d == o) and 0 <= n-1-d+o < n}

def read_cones(n):
    cones = {}
    for j in range(n):
        cones[j] = [d for d in range(2, n) if j in row_M(n, d)]
    return cones

def eps(n, d, h):
    return 1 - 2*submask_xor(n, d, h)

def S_of(n, h):
    return sum(eps(n, d, h) for d in range(2, n))

def contiguous_cover_rank(A, n):
    """Minimal number of contiguous intervals covering A (a set of positions)."""
    if not A:
        return 0
    A = sorted(A)
    k = 1
    for a, b in zip(A, A[1:]):
        if b != a+1:
            k += 1
    return k

n = 8
print("=== n =", n, "===")
print("read cones (position j -> depths d that read it):")
for j in range(n):
    print("  j=%d  cone=%s  |cone|=%d  pc(n-1-j)=%d" % (j, read_cones(n)[j],
          len(read_cones(n)[j]), pc(n-1-j)))

print()
print("row sets M_d:")
for d in range(2, n):
    print("  d=%d pc=%d  M_d=%s" % (d, pc(d), sorted(row_M(n, d))))

print()
print("symmetric differences M_d XOR M_d' (off-diagonal monomial supports of S^2):")
monomials = {}
for d in range(2, n):
    for dp in range(d+1, n):
        A = row_M(n, d) ^ row_M(n, dp)
        monomials[(d, dp)] = A
        print("  (%d,%d)  |A|=%2d  cover_rank=%d  A=%s" % (d, dp, len(A),
              contiguous_cover_rank(A, n), sorted(A)))

print()
# witness
h6 = [0]*8; h6[6] = 1
h5 = [0]*8; h5[5] = 1
print("witness: e_6 S=%d S^2=%d ; e_5 S=%d S^2=%d" % (
    S_of(8, h6), S_of(8, h6)**2, S_of(8, h5), S_of(8, h5)**2))

# what separates them: which cells differ
print("cells eps_d for e_6:", {d: eps(8, d, h6) for d in range(2,8)})
print("cells eps_d for e_5:", {d: eps(8, d, h5) for d in range(2,8)})

print()
print("=== distribution of |M_d XOR M_d'| and cover_rank over all pairs, n=8..12 ===")
for n in (8, 10, 12, 16):
    sizes = {}
    ranks = {}
    for d in range(2, n):
        for dp in range(d+1, n):
            A = row_M(n, d) ^ row_M(n, dp)
            sizes[len(A)] = sizes.get(len(A), 0) + 1
            ranks[contiguous_cover_rank(A, n)] = ranks.get(contiguous_cover_rank(A, n), 0) + 1
    print("n=%d  |A| histogram (size: count): %s" % (n, dict(sorted(sizes.items()))))
    print("n=%d  cover-rank histogram: %s" % (n, dict(sorted(ranks.items()))))
