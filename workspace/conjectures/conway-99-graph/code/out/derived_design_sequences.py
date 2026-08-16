"""Exact vertex-derived-design counts across the (v,k,1,2) family.

For an srg(v,k,1,2) fix a vertex v0.  Its neighbourhood N(v0) is (k/2)K2.
Facts (parameter-uniform, derived in research/backward/derived-design-at-a-vertex.md):
  - lines through v0:                 k/2
  - distance-2 vertices:              k(k-2)/2   (bijection with non-edges of N(v0))
  - cross lines (1 in N, 2 at dist2): k(k-2)/2
  - outer blocks (wholly at dist2):   k(k-2)(k-4)/12
  - replication of outer design:      (k-4)/2
  - every outer block has 3 distance-2 points (partial STS), and the counting
    identity b*3 = N*r always holds.

We print these for the five integrality-feasible members and for the infeasible
ones (8, 32, 44) to see what 99's row looks like versus the controls 9 and 243.
"""
members = [
    (4, 9), (8, 33), (14, 99), (22, 243), (32, 513), (44, 969),
    (112, 6273), (994, 494019),
]
print("k    v      t0      d2     cross   outer     rep   b*3=N*r?")
for k, v in members:
    t0 = k // 2                       # lines through v0
    d2 = k * (k - 2) // 2             # distance-2 vertices
    cross = k * (k - 2) // 2          # cross lines
    outer = k * (k - 2) * (k - 4) // 12
    rep = (k - 4) // 2                # replication of outer STS
    bign = d2 * rep                   # b*3
    bigb = outer * 3
    ok = "-" if bign != bigb else "OK"
    print(f"{k:>3} {v:>6} {t0:>5} {d2:>6} {cross:>6} {outer:>7} {rep:>4}  {ok}")

# The integer sequences that matter, as lists, for the five feasible members.
feas = [(4, 9), (14, 99), (22, 243), (112, 6273), (994, 494019)]
print()
print("distance-2 vertex counts (feasible k):",
      [k * (k - 2) // 2 for k, _ in feas])
print("outer block counts (feasible k):      ",
      [k * (k - 2) * (k - 4) // 12 for k, _ in feas])
print("replication (feasible k):              ",
      [(k - 4) // 2 for k, _ in feas])
print("multiplicities f(r) (feasible):        ",
      [4, 54, 132, 3280, 250914])
print("multiplicities g(s) (feasible):        ",
      [4, 44, 110, 2992, 243104])
