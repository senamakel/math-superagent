#!/usr/bin/env python3
"""Extract exact reduced numerators and denominators of p(3,L) and p(4,L)
over m = L/40 for m = 4..40, from the verified closed forms. Outputs JSON
used for sequence analysis / OEIS."""
from fractions import Fraction as F
import json

def p3(m):
    m = F(m)
    return (7*m*m - 17*m + 12) / (18*m*m - 45*m + 27)

def p4(m):
    m = F(m)
    num = 19*m**3 - 119*m**2 + 244*m - 162
    den = 9*(m-2)*(2*m-5)*(2*m-3)
    return num/den

out = {"p3_num": [], "p3_den": [], "p4_num": [], "p4_den": [],
       "p3_float": [], "p4_float": []}
for m in range(4, 41):
    a, b = p3(m), p4(m)
    out["p3_num"].append(int(a.numerator))
    out["p3_den"].append(int(a.denominator))
    out["p4_num"].append(int(b.numerator))
    out["p4_den"].append(int(b.denominator))
    out["p3_float"].append(float(a))
    out["p4_float"].append(float(b))

with open("code/out/numden_seq.json", "w") as f:
    json.dump(out, f, indent=2)

# sanity checks against stored exact points
from fractions import Fraction as Ff
p3exact = {160:"56/135",240:"2/5",320:"36/91",400:"542/1377",480:"272/693",
           640:"1532/3915",800:"824/2109",1000:"1981/5076",1200:"1934/4959",
           1400:"444/1139",1600:"10532/27027",1800:"2237/5742",2800:"118/297",
           3600:"71/180",4400:"112/285",5200:"487/1242",5600:"382/975",
           7200:"658/1683",9000:"4231/10836",11000:"6451/16536",
           20000:"5554/14259",24000:"896/2301",30000:"6352/16317",
           40000:"68312/175527",50000:"5959/15314"}
bad = 0
for L, s in p3exact.items():
    if p3(F(int(L)//40)) != F(s):
        bad += 1
        print("P3 MISMATCH", L, s)
p4exact = {480:"3077/5985",560:"16033/31050",640:"2839/5481",900:"143561/275520",
           1100:"2493559/4773600",1300:"474941/907680",1500:"2249593/4294080",
           2000:"1044769/1990440",2500:"3723481/7085760",3000:"2454796/4667985",
           4000:"990791/1882335",5000:"35280338/66990105",1800:"166802/317985",
           2100:"6490703/12362400",2300:"25860019/49230720",2700:"1575557/2997280",
           2900:"53060149/100910880",3400:"1203242/2287065",3800:"15239168/28956015",
           4200:"6902786/13112415",4600:"3038972/5771475",4800:"5191253/9858015"}
for L, s in p4exact.items():
    if p4(F(int(L)//40)) != F(s):
        bad += 1
        print("P4 MISMATCH", L, s)
print("closed forms vs stored exact points: mismatch count =", bad)
print("p3 reduced numerators m=4..20:", out["p3_num"][:17])
print("p3 reduced denoms     m=4..20:", out["p3_den"][:17])
