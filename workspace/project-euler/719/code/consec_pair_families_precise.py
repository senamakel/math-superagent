#!/usr/bin/env python3
"""Precisely identify which consecutive-pair families (x, x+1) are S-roots
UNIFORMLY (all relevant k). The notes listed pairs like (990,991),(9990,9991)
(99900,99901),(99990,99991). Find the exact uniform families + first k where
each holds, and measure how many roots they cover (fraction of the set)."""
import re

B_FILE = "research/sources/oeis_a038206_b.full.md"
def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m: roots.append(int(m.group(2)))
    return roots
R = load_roots(B_FILE)
S = set(R); MAXR = max(R)

def uniform_family(builder, kstart, kmax):
    """builder(k) -> value; check value and value+1 in S for k=kstart..kmax.
    Returns (all_ok, first_fail_k)."""
    for k in range(kstart, kmax+1):
        v = builder(k)
        if v > MAXR: break
        if v not in S or (v+1) not in S:
            return (False, k)
    return (True, None)

cands = {
  "10^k-10 / -9":      lambda k: 10**k - 10,
  "10^k-100 / -99":    lambda k: 10**k - 100,
  "10^k-1000 / -999":  lambda k: 10**k - 1000,
  "10^k-1 / 10^k (repunit/p10)": lambda k: 10**k - 1,
}
print("Uniform consecutive-pair families (need both x and x+1 = S-roots):")
for name, b in cands.items():
    # find kstart = min k where both in range and both roots
    start = None
    for k in range(2, 12):
        v = b(k)
        if v > MAXR: break
        if v in S and (v+1) in S:
            start = k; break
    if start is None:
        print(f"  {name}: no k in range has both")
        continue
    ok, ffail = uniform_family(b, start, 15)
    states = []
    for k in range(start, 12):
        v = b(k)
        if v > MAXR: break
        states.append(f"{v}:{'Y' if v in S and (v+1) in S else 'n'}")
    print(f"  {name}: holds from k={start}, states={states}, "
          f"uniform-to-max={'yes' if ffail is None else 'FAILS at k='+str(ffail)}")

# count how many roots come from the densest uniform pair family <= 10^6
fam = set()
for k in range(3, 7):   # up to 10^6
    v = 10**k - 10
    if v <= 10**6: fam.update((v, v+1))
    v = 10**k - 100
    if v <= 10**6: fam.update((v, v+1))
R6 = {r for r in R if r <= 10**6}
print(f"\nRoots <=10^6 covered by the (10^k-10,-9) & (10^k-100,-99) uniform families: {len(fam & R6)} / {len(R6)}")
