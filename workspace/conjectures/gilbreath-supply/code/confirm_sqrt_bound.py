#!/usr/bin/env python3
"""Confirm the bounded |S(n)|/sqrt(n) regularity and second moment of the
excess E2(n)=-S(n), exact, n up to 40000. Also confirm variance-of-nu2/n decays
as the run claims. Negative control: iid +/-1 walk would give max|S|~std*sqrt(n)
~ O(n^0.5*90); we check primes stay far below that."""
import sys, math
sys.path.insert(0, "/workspace/code")
from lib.nu2 import fold_nu2
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)
    # running: max|S|, max|S|/sqrt(n), mean of E2^2/n, first-14 moments tail
    maxS = 0; maxR = 0.0; maxRn = 0
    # second moment of E2(n)/sqrt(n): mean of (E2/sqrt n)^2 over tail
    acc_m2 = 0.0; cnt = 0
    # increment statistics in tail [N/2,N]
    prevS = None
    incs = []
    for n in range(2, N + 1):
        v = fold_nu2(n, h)
        S = 2*v - (n-2)
        aS = abs(S)
        if aS > maxS: maxS = aS
        r = aS/math.sqrt(n)
        if r > maxR: maxR = r; maxRn = n
        if n >= N//2:
            acc_m2 += (S/math.sqrt(n))**2; cnt += 1
        if prevS is not None and n >= N//2:
            incs.append(S - prevS)
        prevS = S
    mean_inc = sum(incs)/len(incs)
    var_inc = sum((x-mean_inc)**2 for x in incs)/len(incs)
    print(f"N={N}: max|S|={maxS}  max|S|/sqrt n={maxR:.3f} @n={maxRn}")
    print(f"  tail mean of (S/sqrt n)^2 = {acc_m2/cnt:.3f}  -> root-mean S ~ {math.sqrt(acc_m2/cnt):.3f}*sqrt n")
    print(f"  tail inc: mean={mean_inc:.2f} var={var_inc:.1f} std={math.sqrt(var_inc):.1f}  "
          f"(random-walk pred for max|S| ~ {math.sqrt(var_inc)*math.sqrt(N):.0f})")

if __name__ == "__main__":
    main(40000)
