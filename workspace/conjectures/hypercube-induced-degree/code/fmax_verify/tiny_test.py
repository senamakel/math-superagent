import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
from ortools.sat.python import cp_model

n = 3
d = 2
S = {0, 1, 2, 5, 6}
N = 1 << n
m = (1 << (n - 1)) + 1

# full model with all 8 vars, but force the 5 witness vars on and others off
model = cp_model.CpModel()
x = [model.NewBoolVar(f'v{i}') for i in range(N)]
model.Add(sum(x) == m)
for v in range(N):
    model.Add(sum(x[v ^ (1 << k)] for k in range(n)) <= d)
# force the witness
for v in range(N):
    model.Add(x[v] == (1 if v in S else 0))

s = cp_model.CpSolver()
st = s.Solve(model)
print('full forced model', s.StatusName(st))
print('sizeof x', len(x))
