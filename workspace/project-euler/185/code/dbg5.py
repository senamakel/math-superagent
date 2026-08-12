import numpy as np
from solution2 import build_model, solve

L=5
cons5=[("90342",2),("70794",0),("39458",2),("34109",1),("51545",2),("12531",1)]
for i in range(6):
    sol,res = solve(L, cons5)
    x = res.x
    sel = [[d for d in range(10) if x[p*10+d]>0.5] for p in range(L)]
    print("run",i,"solve secret",sol,"reconstruct", "".join(str(s[0]) for s in sel),
          "res.success",res.success)
