"""Consolidate the F2 (p=2) Hasse-CA multiplier data into popcount classes.

Tests two crisp conjectures against every recorded n=3..24 male.

  C1: m(n,2) = 2^{pc(n)-1}   (holds for pc=1,2,3; first falsifier at pc=4, n=15)

Multiplier data (recording n -> m(n,2)=sat(n,2)/2), from consolidate_popcount:
"""
recorded = {
    3:2, 4:1, 5:2, 6:2, 7:8, 8:1, 9:2, 10:2, 11:8, 12:2, 13:8, 14:8,
    15:457, 16:1, 17:2, 18:2, 19:8, 20:2,
    21:8, 22:8, 23:466, 24:2,
}

print("n  pc  m    2^(pc-1)   m==2^(pc-1)?")
for n in sorted(recorded):
    pc = bin(n).count("1")
    pred = 2**(pc-1)
    match = recorded[n] == pred
    print(f"{n:2d}  {pc}  {recorded[n]:4d}   {pred:4d}      {match}")

# claim C1 restricted to pc<=3
bad_pc_le3 = [n for n in sorted(recorded) if bin(n).count("1") <= 3 and recorded[n] != 2**(bin(n).count("1")-1)]
print("\nC1 (2^(pc-1)) falsifiers with pc<=3:", bad_pc_le3 or "NONE (holds for every n with pc<=3 up to 24)")

# First falsifier of the unrestricted law m=2^(pc-1): smallest n where it breaks
first_break = min((n for n in sorted(recorded) if recorded[n] != 2**(bin(n).count("1")-1)), default=None)
print("First falsifier of unrestricted m=2^(pc-1):", first_break)
