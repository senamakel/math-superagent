"""Verify the folded-polyominoid definition: reproduce Eriksson Fig.3 n=3 column
from Theorem 9 condition (a),(b),(c) on vector pairs (u,v).

Theorem 9: For pebbling in Z^n with n>=3, folded polyominoids with boundary
path length k correspond bijectively to pairs of integer k-vectors u,v with a
total of k nonzero elements (labels) in {1,...,n} satisfying:
  (a) if |u...r| + |v...r| = r then u_{r+1} <= v_{r+1}   (for 0<=r<k)
  (b) |u...r| + |v...r| >= r   for all 1<=r<=k
  (c) if the same label occurs in u_i and v_j then |u...i| + |v...j| >= max(i,j)

Here |u...r| = number of nonzero labels in the initial r-segment of u.
Labels in {1,...,n}. Fig.3 counts folded polyominoes with circumference 2k
i.e. boundary length k... the theorem states "boundary-path length k" with
TOTAL of k nonzero labels over u and v together. So each of u,v is a length-k
vector and together they hold exactly k nonzero labels among the 2k places.

Also check the 2D G(k,m) CGMO recurrence reproduces A007902 (the 2D amoeba),
for the record.
"""
import itertools, sys

def nz(seq):
    return sum(1 for x in seq if x != 0)

def count_folded(n, k):
    """Count label assignments to (u,v), each length-k, total k nonzero labels
    in {1..n}, satisfying Thm 9 (a),(b),(c)."""
    # enumerate all ways: choose which of the 2k positions are nonzero and their labels.
    positions = 2*k
    c = 0
    # iterate over all tuples of labels for the 2k places where 0 = blank, 1..n = labels
    # total nonzero must equal k
    # build count by iterating over subsets of size k
    for nz_positions in itertools.combinations(range(positions), k):
        # distribute labels {1..n} over k nonzero positions (order matters, repr with repetition)
        for labels in itertools.product(range(1, n+1), repeat=k):
            u = [0]*k
            v = [0]*k
            for place, lab in zip(nz_positions, labels):
                if place < k:
                    u[place] = lab
                else:
                    v[place-k] = lab
            if ok(u, v):
                c += 1
    return c

def ok(u, v):
    k = len(u)
    # prefix sums of nz
    Pu = [0]*(k+1)
    Pv = [0]*(k+1)
    for r in range(1, k+1):
        Pu[r] = Pu[r-1] + (1 if u[r-1]!=0 else 0)
        Pv[r] = Pv[r-1] + (1 if v[r-1]!=0 else 0)
    # (b)
    for r in range(1, k+1):
        if Pu[r] + Pv[r] < r:
            return False
    # (a)
    for r in range(0, k):
        if Pu[r] + Pv[r] == r:
            # compare u_{r+1} <= v_{r+1}; if one is 0 use convention 0 <= everything? 
            # Condition says u_{r+1} <= v_{r+1}. Need an ordering on labels incl 0.
            # If both zero, fine. Interpret ordering by label value with 0 minimal.
            if u[r] > v[r]:
                return False
    # (c)
    for i in range(k):
        for j in range(k):
            if u[i]!=0 and u[i]==v[j]:
                # same label occurs in u_i and v_j
                if Pu[i+1] + Pv[j+1] < max(i+1, j+1):
                    return False
    return True

# labels ordering for (a): use numeric order, 0 = blank smallest
# Check n=3, k=0..6
fig3 = {0:1, 1:3, 2:12, 3:57, 4:300, 5:1680, 6:9900}
print("n=3 folded-polyominoid counts (Fig.3 expected -> computed):")
for k in range(0, 7):
    c = count_folded(3, k)
    exp = fig3[k]
    print(f"  k={k}: expected {exp}, computed {c}, {'OK' if c==exp else 'MISMATCH'}")
