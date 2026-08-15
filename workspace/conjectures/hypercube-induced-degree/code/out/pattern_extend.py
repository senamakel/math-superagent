"""Extend exact f(n) values upward; single-threaded to avoid OpenBLAS fork crash."""
import os, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
sys.path.insert(0, "/workspace/code")
from lib.fmax import decision_ilp

def ceil_sqrt(n):
    r = 1
    while r * r < n:
        r += 1
    return r

# For each n, SQL lower bound from spectral theorem gives f(n) >= ceil(sqrt(n)).
# Equality iff decision_ilp(n, ceil_sqrt(n)) is feasible.
for n in [8, 9, 10, 11]:
    cs = ceil_sqrt(n)
    start = time.time()
    ok = decision_ilp(n, cs)
    print(f"n={n} |S|={(1<<(n-1))+1} d={cs} feasible={ok}  ceil_sqrt={cs}  [{time.time()-start:.2f}s]", flush=True)
