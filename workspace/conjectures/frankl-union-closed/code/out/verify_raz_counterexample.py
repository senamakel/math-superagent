"""Verify Raz's (2017) counterexample to Balla/Gowers' Conjecture 3.

Claim: the 11 sets below, on universe [8], satisfy Reimer's Condition 1
(a filter bijection A -> F_A with A subset F_A and pairwise-disjoint
intervals [A,F_A]) but NO element lies in >= |A|/2 sets.

This only verifies the abundance half of the claim (each element in <= 5
of 11 sets). The Condition-1 filter/bijection half is asserted by the
source; the appendix gives the full explicit bijection.

|A| = 11, so an abundant element would need to be in >= 6 sets.
The paper states each element appears in at most 5.
"""

S = [
    {1,2,3,4,5,6,7,8},   # A0
    {2,4,6,7,8},         # A1
    {1,3,5,8},           # A2
    {1,4,7,8},           # A3
    {2,3,5,6},           # A4
    {1,3,7},             # A5
    {2,3,5},             # A6
    {2,4,6},             # A7
    {4,5,6,7},           # A8
    {8},                 # B1,2
    {1},                 # B3,4
]

def main():
    n = len(S)
    assert n == 11
    universe = sorted(set().union(*S))
    print(f"|A| = {n}; half = {n/2}; universe {universe}")
    counts = {}
    for x in universe:
        c = sum(1 for A in S if x in A)
        counts[x] = c
    print("per-element counts:", counts)
    abundant = [x for x, c in counts.items() if 2*c >= n]
    print("abundant elements (2c >= n):", abundant)
    assert all(c <= 5 for c in counts.values()), "an element exceeds 5"
    assert not abundant, "should be NO abundant element"
    print("VERIFIED: every element in <= 5 = |A|/2 - 0.5 sets, none abundant.")

if __name__ == "__main__":
    main()
