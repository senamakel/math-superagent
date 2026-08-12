#!/usr/bin/env python3
"""Diagnose why CLAIM B fails: D(N+1) < sum_C f(C).

D(N+1) == sum_C f(C) fails because the forward map (C,p) -> child is NOT
injective: some child configs are reachable from two different parents, so
sum f(C) overcounts distinct children.  This probe counts, per reachable
child config C', the number of distinct parents p 'recoverable' from it
(an empty-in-C' cell whose full child triangle sits inside C'), i.e. the
preimage multiplicity, and shows where collisions occur.

f(C) = #cells in C with none of its children in C (dividable cells) is the
degree of C in the forward map; sum_C f(C) = total preimage count, and
D(N+1) = #distinct child configs = #children.  We check
    sum_C f(C)  ==  sum_{C'} recovery_mult(C')  ==  #(C,p) pairs
and
    #children == D(N+1) == #C' with recovery_mult>=1,
and report multiplicity distribution, i.e. how many C' have 2+ parents
(the collisions that break B).
"""
from collections import defaultdict
from lib.amoeba import forward_level, children, lvl, dividable_count

def f_of(C):
    """#dividable cells of C == lib.amoeba.dividable_count(C, 3).

    Local wrapper kept for call sites; delegates to the canonical
    lib/amoeba function (was a duplicated local definition).
    """
    return dividable_count(C, 3)

def recovery_mult(Cp):
    """#cells p with p notin Cp and p+e_i in Cp for all i (preimage parents)."""
    Sset = set(Cp)
    cnt = 0
    for p in Sset:
        ch = set(children(p, 3))
        if ch.issubset(Sset) and p not in Sset:
            cnt += 1
    return cnt

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(8):
        Sf = sum(f_of(C) for C in level)
        nxt = forward_level(level, 3)
        mult_dist = defaultdict(int)
        for Cp in nxt:
            mult_dist[recovery_mult(Cp)] += 1
        total_preimages = sum(m * c for m, c in mult_dist.items())
        print(f"N={N}: sum f(C)={Sf}  #children(D(N+1))={len(nxt)}  "
              f"sum recovery_mult={total_preimages}  "
              f"mult_dist={{mult:count}}={dict(sorted(mult_dist.items()))}")
        level = nxt

if __name__ == "__main__":
    main()
