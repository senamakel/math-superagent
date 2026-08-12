import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from solution2 import build_model, solve

L=5
cons5 = [("90342",2),("70794",0),("39458",2),("34109",1),("51545",2),("12531",1)]

sol, res = solve(L, cons5)
print("solve() ->", sol, res.success, res.message)
print("A@x diff:", (res.x is not None))
# check the returned secret
if sol:
    for g,c in cons5:
        hit = sum(1 for p in range(L) if sol[p]==g[p])
        print(g, hit, c, "OK" if hit==c else "WRONG")
