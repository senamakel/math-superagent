import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from solution2 import build_model

L=5
cons5=[("90342",2),("70794",0),("39458",2),("34109",1),("51545",2),("12531",1)]
c, integrality, bounds, lc = build_model(L, cons5)

for opts in [None, {"time_limit":3600}]:
    kw = {} if opts is None else {"options":opts}
    res = milp(c=c, integrality=integrality, bounds=bounds, constraints=lc, **kw)
    x = res.x
    sel = [ [d for d in range(10) if x[p*10+d]>0.5] for p in range(L) ]
    print(opts, "success", res.success, "secret", "".join(str(s[0]) for s in sel))
