import sys
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

# Conjecture: k*10^10 is a solution of f(n,d)=n  <=>  0 <= k <= d-1
print("Testing conjecture: k*10^10 is a solution of f(n,d)=n  <=>  k in [0, d-1]")
fails = []
for d in range(1,10):
    for k in range(0, 10):
        n = k*10**10
        f = f_place_value(n, d)
        is_sol = (f == n)
        pred = (0 <= k <= d-1)
        if is_sol != pred:
            fails.append((d,k,n,f,is_sol,pred))
        tag = "SOL" if is_sol else "   "
        print(f"d={d} k={k} n={n} f={f} {tag} predicted={pred}")
print("\nFAILURES:", fails)
print("conjecture holds over tested range:", not fails)
