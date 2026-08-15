"""Check a single (n,d) decision ILP: is there S of size 2^{n-1}+1 with D(S)<=d?"""
import sys, time
sys.path.insert(0, "/workspace/code")
from lib.fmax import decision_ilp

n = int(sys.argv[1]); d = int(sys.argv[2])
t0 = time.time()
ok = decision_ilp(n, d)
print(f"n={n} d={d} feasible={ok} |S|={(1<<(n-1))+1} [{time.time()-t0:.2f}s]", flush=True)
