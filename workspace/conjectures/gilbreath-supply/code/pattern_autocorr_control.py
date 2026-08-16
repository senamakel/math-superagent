#!/usr/bin/env python3
"""Control for the autocorrelation finding: is the persistent positive
autocorrelation of nu2(n)/n a property of the prime h, or an artifact of the
fold acting on generic input? Same probe as pattern_longlag on (a) iid random
h, (b) Thue-Morse h. If random h shows the same persistence, the regularity is
a fold artifact, not a primes signal.
"""
import sys, random
from lib.supply_fold import s_sos

def thue_morse(j):
    return bin(j).count('1') % 2

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    label = sys.argv[2] if len(sys.argv) > 2 else "random"
    random.seed(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    if label == "random":
        h = [random.randint(0,1) for _ in range(N+1)]
    elif label == "thue":
        h = [thue_morse(j) for j in range(N+1)]
    nu = [0]*(N+1)
    for n in range(2, N+1):
        _, ones = s_sos(n, h[:n])
        nu[n] = ones
    r = [nu[n]/n for n in range(2, N+1)]
    m = sum(r)/len(r)
    dev = [x-m for x in r]
    var = sum(x*x for x in dev)/len(dev)
    L = len(dev)
    print(f"[{label}] N={N} mean={m:.4f} var={var:.4e}")
    cum=0.0
    print("  lag  rho")
    for k in [1,2,3,5,8,13,21,34,55]:
        num=sum(dev[i]*dev[i+k] for i in range(L-k))
        cum += num/var/L
        print(f"   {k:3d}  {num/var/L:+.4f}")
    print(f"  tau(55) = {1+2*cum:.2f}")

if __name__ == "__main__":
    main()
