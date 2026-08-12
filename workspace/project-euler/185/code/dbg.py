import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from solution2 import build_model, solve

L=5
cons=[("90342",2),("70794",0),("39458",2),("34109",1),("51545",2),("12531",1)]

c, integrality, bounds, lc = build_model(L, cons)
print("A shape", lc.A.shape)
print("lb", lc.lb)
print("ub", lc.ub)

# what does milp actually solve?
res = milp(c=c, integrality=integrality, bounds=bounds, constraints=lc)
print("success", res.success, res.message)
x = res.x
print("x =", x)
# reconstruct
for p in range(L):
    vals=[x[p*10+d] for d in range(10)]
    print("pos",p,"idx1 nonzero", [(d,round(v,3)) for d,v in enumerate(vals) if v>0.5])

# check constraints manually
Ax = lc.A @ x
print("A@x", Ax)
print("lb", lc.lb)
print("diff", Ax - lc.lb)
