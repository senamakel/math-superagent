import json
from decimal import Decimal, getcontext
getcontext().prec=60

# read exact state to get vR run blocks over k=1..120
D=json.load(open("out/exact_state_1_120.json"))
vrs=[D[str(k)]['vR'] for k in range(1,121)]
runs=[]; cs=None
for k in range(1,121):
    v=vrs[k-1]
    if v!=cs:
        if cs is not None: runs.append((cs_start,k-1,cs))
        cs=v; cs_start=k
runs.append((cs_start,120,cs))

starts=[s for (s,e,v) in runs]
lens=[e-s+1 for (s,e,v) in runs]
print("block starts:", starts)
print("block lens  :", lens)

# now check lens pattern against mechanical sequence.
# lens are 2 and 3. Map 3->X,2->Y and check if X/Y pattern is a Sturmian mechanical word of slope beta.
# Try to see which position each block starts at relative to Fibonacci structure.
# Candidate: block starts at Fibonacci numbers? starts:1,2,5,7,10,13,15,18,20,23,26,28,31,34,36,39,41,44,47,49,52,54,57,60,62,65,68,70,73,75,78,81,83,86,89,91,94,96,99,102,104,107,109,112,115,117,120
# diffs:1,3,2,3,3,2,3,2,3,3,2,3,3,2,3,2,3,3,2,3,2,3,3,2,3,3,2,3,2,3,3,2,3,2,3,3,2,3,3,2,3,2,3,3,2,3
print("diff from k=1:", [starts[i+1]-starts[i] for i in range(len(starts)-1)])

# Also print vR mod within, and check: is vR reversibly built from string of left-neighbor?
# Print for each block: start, vR
for (s,e,v) in runs:
    print(f"start={s} end={e} len={e-s+1} vR={v}")
