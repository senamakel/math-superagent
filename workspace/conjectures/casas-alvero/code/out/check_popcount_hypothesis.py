"""Verify the popcount hypothesis over the run's recorded p=2 multiplier data,
then identify which fresh n (beyond 20) would test it.

Hypothesis (from extend_p2_popcount.py and satisfier_multiplier_over_Fp.md):
    m(n,2) = sat(n,2)/2 depends ONLY on popcount(n):
        popcount 1 -> 1 ; 2 -> 2 ; 3 -> 8 ; 4 -> 457 ; 5 -> ?
i.e. m(pc) is a function of pc(n), constant across all n with that popcount.
"""
from math import comb

# Recorded p=2 multipliers m(n,2)=sat/2, n=3..20 (from pattern file + extension).
recorded = {
    3:2, 4:1, 5:2, 6:2, 7:8, 8:1, 9:2, 10:2, 11:8, 12:2, 13:8, 14:8,
    15:457, 16:1, 17:2, 18:2, 19:8, 20:2,
}

bad = []
by_pc = {}
for n in sorted(recorded):
    pc = bin(n).count("1")
    by_pc.setdefault(pc, {})[n] = recorded[n]

print("multiplier value per (popcount, n):")
ok = True
for pc in sorted(by_pc):
    d = by_pc[pc]
    vals = set(d.values())
    print(f"  popcount {pc}: n={sorted(d)} -> m={sorted(vals)} "
          f"({'constant' if len(vals)==1 else 'VARIABLE!'})")
    if len(vals) != 1:
        ok = False

print("\nHYPOTHESIS over recorded n=3..20:", "HOLDS" if ok else "FAILS")

print("\nFresh test targets: first n>20 by popcount class (2^n = oracle size):")
for n in range(21, 33):
    pc = bin(n).count("1")
    if pc not in by_pc:          # a NEW popcount class first reaches pc=5 at n=31
        tag = "NEW popcount class (pc=5!)" if pc == 5 else "extends existing class"
        print(f"  n={n:2d} 2^n={1<<n:>12d} popcount={pc}  <- {tag}")
