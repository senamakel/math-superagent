import sys, random
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

# For a block-0 solution x (f(x,d)=x), n=k*10^10+x is a solution iff
#   R := f(n,d) - f(x,d)  equals  k*10^10   (since f(n)-n = R - k*10^10).
# Compute R's exact form for test x values.
print("R(k,x,d) = f(k*10^10+x,d) - f(x,d)  for random x, k=1..8")
random.seed(3)
for d in [1,3,8]:
    print(f"--- d={d} ---")
    for _ in range(3):
        x = random.randrange(0, 10**10)
        row = []
        for k in range(1,9):
            n = k*10**10+x
            R = f_place_value(n,d) - f_place_value(x,d)
            row.append((k, R-k*10**10))  # delta from k*10^10
        print(f"  x={x}: deltas(R-k*10^10) per k: {row}")

# Now test the real conjecture on actual block-0 solutions:
# for digit d, is R(x,k) exactly k*10^10 for every block-0 solution x and k<=d-1
print("\nTesting on ACTUAL block-0 solutions: R(x,k)==k*10^10 ?")
import os
for d in range(1,10):
    sols=[int(x) for x in open(f"/workspace/code/out/solutions-d{d}.txt").read().split()]
    # block-0 solutions are those < 10^10
    b0=[x for x in sols if x < 10**10]
    S=set(b0)
    allok=True
    for x in b0:
        for k in range(1,d):
            n = k*10**10+x
            if not (f_place_value(n,d)-f_place_value(x,d) == k*10**10):
                allok=False; break
        if not allok: break
    print(f"  d={d}: block0 solutions={len(b0)} k=1..d-1 R==k*10^10: {allok}")
