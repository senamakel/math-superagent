#!/usr/bin/env python3
"""Verify: does the mod-6 forbidden-block structure of prime gaps survive the
fold's parity projection h[j] = ((g)/2) mod 2 ?

We test the claim: for m in 2..4, every parity block (b1..bm) in {0,1}^m has BOTH
an admissible mod-6 block and a forbidden mod-6 block that project onto it.
If so, the binary parity string h carries NO forbidden-block constraint from the
mod-6 enumeration, and Lacasa's unconditional K>1 structure does not survive.

The fold reads gap parity: h[j] = (g_j/2) mod 2 where g_j = p_{j+1}-p_j.
Projection of a mod-6 class c (0,2,4) is (c/2 mod 2) for representatives {0,2,4}
- but a gap g ≡ c mod 6 can be any g = 6a+c, and (g/2) mod 2 = (3a + c/2) mod 2
  which depends on a. The representatives c/2 mod 2 give only c=2->1, c=4->0, c=0->0
  but the actual parity is free (depends on a). We verify both readings:
  (A) "lift-free" projection: c -> (c/2) mod 2 using representatives {0,2,4}
  (B) "lift-dependent" projection: parity of (6a+c)/2 over all a, which is both 0,1.

Forbidden sets F(m), mod 6, from Lacasa Table I (as residue strings c in {0,2,4}).
"""
from itertools import product

# admissible = all over {0,2,4} except forbidden
F = {
    1: [],
    2: [(4,4)],
    3: [(0,2,2),(0,4,4),(2,0,2),(2,2,0),(2,2,2),(2,4,4),(4,0,4),(4,2,2),(4,4,0),(4,4,2),(4,4,4)],
    4: [(0,0,2,2),(0,0,4,4),(0,2,0,2),(0,2,2,0),(0,2,2,2),(0,2,2,4),(0,2,4,4),(0,4,0,4),(0,4,2,2),(0,4,4,0),
        (0,4,4,2),(0,4,4,4),(2,0,0,2),(2,0,2,0),(2,0,2,2),(2,0,2,4),(2,0,4,4),(2,2,0,0),(2,2,0,2),(2,2,0,4),
        (2,2,2,0),(2,2,2,2),(2,2,2,4),(2,2,4,0),(2,2,4,4),(2,4,0,4),(2,4,2,2),(2,4,4,0),(2,4,4,2),(2,4,4,4),
        (4,0,0,4),(4,0,2,2),(4,0,4,0),(4,0,4,2),(4,0,4,4),(4,2,0,2),(4,2,2,0),(4,2,2,2),(4,2,2,4),(4,2,4,4)],
}
SYMS = [0,2,4]

def liftfree_project(block):
    """(c/2) mod 2 for representatives {0,2,4}: c=0->0,c=2->1,c=4->0."""
    return tuple((c//2) % 2 for c in block)

def liftfree_possible(block):
    """Under (A), the singleton image."""
    return [liftfree_project(block)]

def liftdep_possible(block):
    """Under (B), each c -> both parities (depends on a), so all 2^m parity blocks possible."""
    return list(product([0,1], repeat=len(block)))

for m in [1,2,3,4]:
    Fm = F[m]
    forbidden = set(Fm)
    admissible = set(product(SYMS, repeat=m)) - forbidden
    for label, possible in [("liftfree(A)", liftfree_possible), ("liftdep(B)", liftdep_possible)]:
        print(f"--- m={m} {label} ---")
        for pb in product([0,1], repeat=m):
            # does pb arise from some admissible mod-6 block, and from some forbidden one?
            from_adm = any(pb in possible(b) for b in admissible)
            from_for = any(pb in possible(b) for b in forbidden)
            both = from_adm and from_for
            print(f"  parity block {pb}: from_admissible={from_adm} from_forbidden={from_for} both={both}")

print("DONE")
