"""Reconcile the induced-C5 (pentagon) count for srg(v,k,1,2).

Round 16 / report14 claim pentagons = v*k*(k-2)*(k-4)//5  -> [0,33264,384912,...]
Round 17 on-disk script uses v*k*(k-1)*(k-2)*(k-3)//120   -> [1,19819,355509,...]

Decide by brute force on the one small family member we can build exactly:
rook(3) = srg(9,4,1,2). The closed form v*k*(k-2)*(k-4)/5 at (9,4) gives 0,
and rook(3) has no induced 5-cycles (girth/rook structure), so 0 is the truth
if brute force agrees. Then the round-17 script value [1,...] must be wrong.
"""
from itertools import combinations
from lib.srg import rook

def count_induced_c5(A, n):
    """Exact count of induced 5-cycles (each cycle vertex adjacent to exactly
    the 2 cycle neighbours and nothing else inside the 5-set)."""
    cnt = 0
    for s in combinations(range(n), 5):
        # adjacency within the 5-subset
        adj = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if j != i and A[s[i]][s[j]]:
                    adj[i][j] = 1
        # induced: no diagonal chords; vertices labelled s0..s4 fixed
        # a chordless 5-cycle exists iff exactly those edges that form a cycle
        # Among 5 vertices an induced C5 iff total edges ==5 and it's a single
        # cycle (each vertex degree 2 in the induced subgraph).
        degs = [sum(r) for r in adj]
        total = sum(degs)//2
        if total == 5 and all(d == 2 for d in degs):
            cnt += 1
    return cnt

A = rook(3)
n = 9
brute = count_induced_c5(A, n)
formula_round16 = n*4*(4-2)*(4-4)
print("rook(3) = srg(9,4,1,2), n=9, k=4")
print("  brute force induced C5:", brute)
print("  round16 formula v*k*(k-2)*(k-4)/5 :", formula_round16, "(expect 0)")
print("  round17 script value at u=1       : 1   (v*k*(k-1)*(k-2)*(k-3)/120)")

# also check the family values claimed by each side for the two existing family members
print()
for (name, f) in [("round16 v*k*(k-2)*(k-4)//5", lambda k,v: v*k*(k-2)*(k-4)//5),
                  ("round17 v*k*(k-1)*(k-2)*(k-3)//120", lambda k,v: v*k*(k-1)*(k-2)*(k-3)//120)]:
    print(name, "u=1(9,4):", f(4,9), " u=3(99,14):", f(14,99), " u=4(243,22):", f(22,243))
