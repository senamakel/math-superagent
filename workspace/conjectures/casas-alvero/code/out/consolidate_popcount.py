"""Consolidated p=2 multiplier m(n,2)=sat/2 data, merged recorded (n=3..20)
with the fresh locally-computed values (n=21..24).  Tests whether m depends
only on popcount(n)."""
recorded = {
    3:2, 4:1, 5:2, 6:2, 7:8, 8:1, 9:2, 10:2, 11:8, 12:2, 13:8, 14:8,
    15:457, 16:1, 17:2, 18:2, 19:8, 20:2,
    21:8, 22:8, 23:466, 24:2,      # fresh (this run, n=21..24)
}
by_pc = {}
for n in sorted(recorded):
    pc = bin(n).count("1")
    by_pc.setdefault(pc, {})[n] = recorded[n]
print("m(n,2) by popcount class:")
ok = True
for pc in sorted(by_pc):
    d = by_pc[pc]
    vals = set(d.values())
    const = len(vals) == 1
    if not const:
        ok = False
    print(f"  pc={pc}: n={sorted(d)} -> m={sorted(vals)} "
          f"({'constant '+str(next(iter(vals))) if const else 'VARIABLE: '+str(sorted(vals))})")
print("\npopcount hypothesis:", "HOLDS" if ok else
      "FALSIFIED (m(pc=4) = 457 at n=15 but 466 at n=23)")
# first term that falsifies
print("\nFirst falsifier: n=23 (pc=4): prediction 457, actual 466.")
