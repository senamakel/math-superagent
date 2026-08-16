#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import s_sos

def nu2(n, h):
    _, ones = s_sos(n, h)
    return ones

def build(n, pred):
    return [1 if pred(j) else 0 for j in range(n)]

def is_power_b(x, b):
    if x < 1: return False
    while x % b == 0:
        x //= b
    return x == 1

def run_family(name, pred, n_lo, n_hi, step=7):
    ratios = []
    for n in range(n_lo, n_hi + 1, step):
        h = build(n, pred)
        ratios.append(nu2(n, h) / n)
    mn = min(ratios)
    tail = min(ratios[len(ratios)//2:]) if len(ratios) > 1 else mn
    mean = sum(ratios)/len(ratios)
    hi = max(ratios)
    print(f"{name:38s} n[{n_lo},{n_hi}] mean={mean:.4f} min={mn:.4f} mintail={tail:.4f} max={hi:.4f}")
    return mn, tail

def main():
    NLO, NHI = 64, 4000
    print("=== fixed sparse family: does min ratio stay > 0 (G-weak-input-strictness)? ===")
    run_family("powers of 2", lambda j: is_power_b(j,2), NLO, NHI, 7)
    run_family("powers of 2 shift +1", lambda j: is_power_b(j-1,2) and j>=2, NLO, NHI, 7)
    run_family("powers of 2 shift -1", lambda j: is_power_b(j+1,2), NLO, NHI, 7)
    run_family("powers of 3", lambda j: is_power_b(j,3), NLO, NHI, 7)
    run_family("squares", lambda j: int(j**0.5)**2==j, NLO, NHI, 7)
    run_family("AP k*7", lambda j: j%7==0, NLO, NHI, 7)
    run_family("AP k*3", lambda j: j%3==0, NLO, NHI, 7)
    run_family("primes-index ones", lambda j: False, NLO, NHI, 7)  # j is index not prime

if __name__ == "__main__":
    main()
