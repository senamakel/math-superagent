"""Verify the two exact structural claims consolidated this pass:
(A) support-2 ce count = 2^popcount(n) - 2, for every n computed;
(B) the pc=3 support-size PROFILE is fully rigid: {2:6, 4:5, 6:3} at every
    pc=3 degree, so the whole ce set depends only on popcount for pc=3.
(C) pc=4 small supports (2,4) rigid, large supports vary -> multiplier varies.

Prints a compact table reusing the already-captured shape data hardcoded here
(the data was produced by exact enumeration in this run)."""
profiles = {
    # n: (pc, {support-size: count})
    5:  (2, {2:2}),
    6:  (2, {2:2}),
    7:  (3, {2:6, 4:5, 6:3}),
    9:  (2, {2:2}),
    10: (2, {2:2}),
    11: (3, {2:6, 4:5, 6:3}),
    13: (3, {2:6, 4:5, 6:3}),
    15: (4, {2:14, 4:106, 6:390, 7:4, 8:236, 10:139, 12:18, 14:5}),
    17: (2, {2:2}),
    18: (2, {2:2}),
    19: (3, {2:6, 4:5, 6:3}),
    20: (2, {2:2}),
    21: (3, {2:6, 4:5, 6:3}),
    22: (3, {2:6, 4:5, 6:3}),
    23: (4, {2:14, 4:106, 6:411, 8:248, 10:130, 12:17, 14:4}),
    24: (2, {2:2}),
    25: (3, {2:6, 4:5, 6:3}),
    26: (3, {2:6, 4:5, 6:3}),
    27: (4, {2:14, 4:106, 6:352, 8:228, 10:112, 12:18, 14:4}),
}
print("=== (A) support-2 ce count == 2^popcount(n) - 2 ===")
okA = True
for n, (pc, prof) in sorted(profiles.items()):
    s2 = prof.get(2, 0)
    pred = 2**pc - 2
    good = s2 == pred
    okA &= good
    print(f"  n={n:2d} pc={pc} support-2={s2:3d}  2^{pc}-2={pred:3d}  {'OK' if good else 'FAIL'}")

print("\n=== (B) pc=3 profile rigidity: all equal {2:6,4:5,6:3} ===")
pc3 = {n: p for n, (pc, p) in profiles.items() if pc == 3}
ref = {2:6, 4:5, 6:3}
okB = all(p == ref for p in pc3.values())
print(f"  pc=3 degrees {sorted(pc3)}: all profiles == {{2:6,4:5,6:3}}? {okB}")

print("\n=== (C) pc=4: small-supports rigid, large vary ===")
pc4 = {n: p for n, (pc, p) in profiles.items() if pc == 4}
for n, p in sorted(pc4.items()):
    total = sum(p.values())
    m = total // 2 + 1
    print(f"  n={n}: support2={p[2]} support4={p[4]} support6+={sum(v for k,v in p.items() if k>=6)} total_ce={total} m={m}")

print("\n=== SUMMARY ===")
print(f"(A) support-2==2^pc-2 across {len(profiles)} degrees: {'ALL OK' if okA else 'FAIL'}")
print(f"(B) pc=3 full-profile rigidity across {len(pc3)} degrees: {'HOLDS' if okB else 'FAILS'}")
print(f"(C) pc=4 m varies over {{457,466,418}} while support-2,4 stay {[p[2] for p in pc4.values()]},{[p[4] for p in pc4.values()]} "
      "(all equal)")
