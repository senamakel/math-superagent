#!/usr/bin/env python3
"""Tail analysis of nu2 supply - the regime G-supply actually needs (n>=1000).
Records min nu2/n and min exponent over n>=1000, plus the strongest linear
lower bound c supported with margin. Exact integers from nu2_dense.txt.
"""
import math

def load():
    nu2 = {}
    with open("/workspace/code/out/nu2_dense.txt") as f:
        for line in f:
            n, v = line.split()
            nu2[int(n)] = int(v)
    return nu2

def main():
    nu2 = load()
    for lo,label in [(1000,"n>=1000"),(5000,"n>=5000"),(10000,"n>=10000")]:
        sub = {n:v for n,v in nu2.items() if n>=lo}
        m = min(sub.items(), key=lambda kv: kv[1]/kv[0])
        e = min(sub.items(), key=lambda kv: math.log(kv[1])/math.log(kv[0]))
        Dmin = min(2*sub[n]-n for n in sub)
        Dmax = max(2*sub[n]-n for n in sub)
        print(f"[{label}] min nu2/n = {m[1]/m[0]:.4f} at n={m[0]} | "
              f"min log(nu2)/log(n) = {math.log(e[1])/math.log(e[0]):.4f} at n={e[0]} | "
              f"D in [{Dmin},{Dmax}]")

    # worst margin for the linear bound nu2 >= 0.4n, 0.45n, 0.49n over n>=1000
    for c in (0.40,0.45,0.49):
        sub = {n:v for n,v in nu2.items() if n>=1000}
        m = min(sub.items(), key=lambda kv: (kv[1]-c*kv[0]))
        print(f"n>=1000: tightest margin for nu2>={c}n is {m[1]-c*m[0]:.0f} at n={m[0]}")

if __name__=="__main__":
    main()
