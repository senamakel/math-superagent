#!/usr/bin/env python3
"""Independent MC check of exact p(4,L) values from code/out/exact_pn.json."""
import sys, os, json, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import outcome_parity

def mc(n, L, N, seed=7):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n, L, v) == 0:
            even += 1
    return even/N

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    data = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out','exact_pn.json')))
    for L in ('160','240','320','400'):
        from fractions import Fraction as F
        ex = float(F(data['L'][L]['p']))
        m = mc(4, int(L), N, seed=555+int(L))
        se = math.sqrt(ex*(1-ex)/N)
        print(f"n=4 L={L:5s} exact={ex:.8f}  MC={m:.8f}  diff={m-ex:+.6f} (SE~{se:.5f})")

if __name__ == '__main__':
    main()
