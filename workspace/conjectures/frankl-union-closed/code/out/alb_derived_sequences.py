"""Report derived sequences from the |Alb| distribution over nonempty UC families:
  (a) total number of abundant-element incidences = sum_F |Alb(F)|
  (b) average |Alb| per family (exact Fraction)
  (c) the |Alb|=0 count (= number of families with NO abundant element; should
      be 0 for every n, since UC holds — a live check of the conjecture on n<=5)
  (d) |Alb|=1 .. |Alb|=n columns as n-sequences for structure search.
Exact integers / Fractions only. Data from the cascade table in
alb_distribution_profile.captured.txt.
"""
from fractions import Fraction

# |Alb| distribution over NONEMPTY UC families (excludes the {empty} outlier),
# from alb_distribution_profile.captured.txt
dist = {
    1: {1: 2},
    2: {1: 6, 2: 6},
    3: {1: 18, 2: 60, 3: 42},
    4: {1: 64, 2: 942, 3: 2460, 4: 1492},
    5: {1: 265, 2: 30340, 3: 450750, 4: 1332525, 5: 957222},
}

totals = {n: sum(dist[n].values()) for n in dist}
print("n : #families | sum_F|Alb| | avg|Alb| | #Alb==0 | #Alb==1")
for n in sorted(dist):
    d = dist[n]
    sw = sum(k * v for k, v in d.items())
    tot = totals[n]
    avg = Fraction(sw, tot)
    alb0 = d.get(0, 0)
    alb1 = d.get(1, 0)
    print(f"{n} : {tot:9} | {sw:10} | {avg} | {alb0:6} | {alb1:6}")

print("\nSequences over n=1..5:")
print("  total UC (nonempty):", [totals[n] for n in sorted(dist)])
print("  sum_F |Alb(F)|      :", [sum(k * v for k, v in dist[n].items()) for n in sorted(dist)])
print("  avg |Alb|           :",
      [Fraction(sum(k * v for k, v in dist[n].items()), totals[n]) for n in sorted(dist)])
print("  |Alb|==0            :", [dist[n].get(0, 0) for n in sorted(dist)])
print("  |Alb|==1            :", [dist[n].get(1, 0) for n in sorted(dist)])
print("  |Alb|==2            :", [dist[n].get(2, 0) for n in sorted(dist)])
print("  |Alb|==n (max)      :", [dist[n].get(n, 0) for n in sorted(dist)])
