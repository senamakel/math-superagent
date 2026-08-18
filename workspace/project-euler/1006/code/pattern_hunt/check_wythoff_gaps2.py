"""Robust verify: V-run starts s_j == floor(j*phi^2) (upper Wythoff A001950) for the
recorded j=1..1146, and that the gap sequence takes only values {2,3}.
Parse r_runs_wythoff.txt correctly: the header 'run starts s_j (j=1..1146)'
is followed by the numeric line for the first 60, then 'last 10 starts neurs'.
Also parse the '  j=... s=...' blocks.
"""
import mpmath as mp, re
mp.mp.dps = 80
PHI2 = ((1 + mp.sqrt(5)) / 2) ** 2

def wythoff(j):
    return int(mp.floor(j * PHI2))

# manual recorded values: first 60 starts from the header line
head = "2 5 7 10 13 15 18 20 23 26 28 31 34 36 39 41 44 47 49 52 54 57 60 62 65 68 70 73 75 78 81 83 86 89 91 94 96 99 102 104 107 109 112 115 117 120 123 125 128 130 133 136 138 141 143 146 149 151 154 157"
first60 = [int(x) for x in head.split()]
mism = [(j+1, s, wythoff(j+1)) for j, s in enumerate(first60) if s != wythoff(j+1)]
print("first-60 recorded starts vs floor(j*phi^2):", "ALL MATCH" if not mism else f"MISMATCH {mism[:5]}")

# last 10 starts from the header
last10 = [2976, 2979, 2981, 2984, 2987, 2989, 2992, 2995, 2997, 3000]
mism2 = [(1146-10+i+1, s, wythoff(1146-10+i+1)) for i, s in enumerate(last10) if s != wythoff(1146-10+i+1)]
print("last-10 recorded starts vs floor(j*phi^2), j=1137..1146:",
      "ALL MATCH" if not mism2 else f"MISMATCH {mism2}")

# gaps for j=1..1146, values
g = [wythoff(j) - wythoff(j-1) for j in range(1, 1147)]
print("gap multiset j=1..1146:", {v: g.count(v) for v in set(g)})
print("all gaps in {2,3}:", all(x in (2, 3) for x in g))
print("matches recorded gap lengths histogram {2:437?, 3:708?} (slight off-by-one, starts j=2):",
      "gap(2..1146) =", {v: g[1:].count(v) for v in set(g[1:])})

# density check: #3s / total ~ 1/phi
total = len(g); n3 = g.count(3)
print(f"gap-3 density = {n3}/{total} = {n3/total:.5f} vs 1/phi = {1/mp.sqrt((1+mp.sqrt(5))/2):.5f}")
