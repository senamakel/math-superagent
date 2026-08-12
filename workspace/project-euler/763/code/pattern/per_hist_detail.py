#!/usr/bin/env python3
"""For selected N, print each distinct histogram with its multiplicity
(#configs realizing it), and factor the multiplicity to expose structure."""
import glob, collections
from math import gcd

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def prime_power_parts(v):
    # return 2^a * 3^b * rest
    a=b=0
    while v%2==0: v//=2; a+=1
    while v%3==0: v//=3; b+=1
    return (a,b,v)

for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    if n not in (4,6,8,10,12):
        continue
    per = collections.Counter()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        per[hist] += 1
    print(f"===== N={n} =====")
    for hist, m in sorted(per.items(), key=lambda kv:-kv[1]):
        a,b,r = prime_power_parts(m)
        print(f"  hist={hist}  mult={m}  =2^{a}*3^{b}*{r}  M(last on axis)")
    print()
