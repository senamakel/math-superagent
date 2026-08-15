#!/usr/bin/env python3
"""Verify the CB-dying-pair defect on real failing 2-then-odds triangles.

The open lemma states: at the first failure row K, the dying row K-1
satisfies b_{K-1} = 1, A_{K-1}(0)=1, and A_{K-1}(1) in {4,6,8,...}.

Claim: "dying" (A_{K-1}(1) not in {0,2}, which is what makes A_K(0)!=1 by
the reduction) is INCOMPATIBLE with b_{K-1}=1 (which requires
A_{K-1}(1) in {0,2}).  The block-length-1 row is K-2, not K-1.

Check on several real failing sequences (delete-7, delete-5, delete-11,
and a random 2-then-odds with a big gap).
"""
from lib.gilbreath import rows_generator, block_profile

def first_failure_row(rows):
    for k in range(1, len(rows)):
        if rows[k][0] != 1:
            return k
    return None

cases = {
  "delete7": [2,3,5,11,13,17,19,23,29,31,37,41,43,47],
  "delete5": [2,3,7,11,13,17,19,23,29,31,37,41,43,47],
  "delete11": [2,3,5,7,13,17,19,23,29,31,37,41,43,47],
  "gap6-insert": [2,3,5,11,13,17,23,29,31,37,41,43,47,53],  # a 6-gap then more
}

for name, prim in cases.items():
    rows = list(rows_generator(prim, 12))
    K = first_failure_row(rows)
    if K is None:
        print(f"{name}: NO FAILURE within depth 12")
        continue
    dying = rows[K-1]
    b_dying = block_profile(dying)
    b_Km2 = block_profile(rows[K-2])
    a1_dying = dying[1] if len(dying) > 1 else None
    print(f"\n{name}: first failure at K={K}")
    print(f"  dying row K-1 = {dying[:8]}  b={b_dying}  A(K-1,1)={a1_dying}")
    print(f"  row K-2 = {rows[K-2][:8]}  b={b_Km2}")
    # test the lemma's conjunction
    lemmas_conj = (b_dying == 1) and (a1_dying in (4,6,8,10,12))
    print(f"  lemma's conjunction (b_Km1=1 & A(1) in {{4,6,..}}): {lemmas_conj}")
    # the correct setup
    print(f"  dying has b=0? {b_dying==0}  (b=1 sits at K-2? {b_Km2==1})")
    print(f"  reduction |1-A(K-1,1)| = {abs(1-a1_dying)}  (should be !=1 at failure)")
