import os

# Explore block structure in the solution files.
# Many solutions look like A*10^10 + B where B is a 'seed' from the small range,
# and consecutive runs around multi-digit boundaries.

for d in [1,2,3]:
    sols=[int(x) for x in open(f"/workspace/code/out/solutions-d{d}.txt").read().split()]
    print(f"--- d={d} ({len(sols)} solutions) ---")
    # group by floor(n/10^10)
    from collections import defaultdict
    grp=defaultdict(list)
    for n in sols: grp[n//10**10].append(n)
    for k in sorted(grp):
        block=grp[k]
        print(f"  block k={k}: n_sol={len(block)} min={block[0]} max={block[-1]}")
