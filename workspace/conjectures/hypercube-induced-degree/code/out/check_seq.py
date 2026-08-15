"""Run a list of (n,d) ILP decisions sequentially, single-threaded BLAS."""
import sys, time
sys.path.insert(0, "/workspace/code")
os_env = None
try:
    import os
    os.environ['OPENBLAS_NUM_THREADS'] = '1'
    os.environ['OMP_NUM_THREADS'] = '1'
except Exception:
    pass
from lib.fmax import decision_ilp

cases = [(8,3),(9,3),(10,3),(10,4),(11,4),(12,4)]
for n, d in cases:
    t0 = time.time()
    try:
        ok = decision_ilp(n, d)
        print(f"n={n} d={d} feasible={ok} |S|={(1<<(n-1))+1} [{time.time()-t0:.2f}s]", flush=True)
    except Exception as e:
        print(f"n={n} d={d} ERROR {e}", flush=True)
