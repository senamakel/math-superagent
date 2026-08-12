#!/usr/bin/env python3
"""Fix the closed-form vs stored-point check: evaluate at m = L/40 exactly
(Fraction), keys are L. Also re-emit integer-m sequences."""
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

p3exact = {160:"56/135",240:"2/5",320:"36/91",400:"542/1377",480:"272/693",
           640:"1532/3915",800:"824/2109",1000:"1981/5076",1200:"1934/4959",
           1400:"444/1139",1600:"10532/27027",1800:"2237/5742",120:"4/9",
           200:"17/42",280:"118/297",360:"71/180",440:"112/285",520:"487/1242",
           560:"382/975",720:"658/1683",900:"4231/10836",1100:"6451/16536",
           2000:"5554/14259",2400:"896/2301",3000:"6352/16317",
           4000:"68312/175527",5000:"5959/15314"}
p4exact = {480:"3077/5985",560:"16033/31050",640:"2839/5481",900:"143561/275520",
           1100:"2493559/4773600",1300:"474941/907680",1500:"2249593/4294080",
           2000:"1044769/1990440",2500:"3723481/7085760",3000:"2454796/4667985",
           4000:"990791/1882335",5000:"35280338/66990105",1800:"166802/317985",
           2100:"6490703/12362400",2300:"25860019/49230720",2700:"1575557/2997280",
           2900:"53060149/100910880",3400:"1203242/2287065",3800:"15239168/28956015",
           4200:"6902786/13112415",4600:"3038972/5771475",4800:"5191253/9858015"}
bad3 = [k for k, s in p3exact.items() if p3(F(k)/40) != F(s)]
bad4 = [k for k, s in p4exact.items() if p4(F(k)/40) != F(s)]
print("p3 closed form vs stored exact: mismatches =", bad3)
print("p4 closed form vs stored exact: mismatches =", bad4)

out = {"p3_num": [], "p3_den": [], "p4_num": [], "p4_den": []}
for m in range(4, 41):
    a, b = p3(m), p4(m)
    out["p3_num"].append(int(a.numerator))
    out["p3_den"].append(int(a.denominator))
    out["p4_num"].append(int(b.numerator))
    out["p4_den"].append(int(b.denominator))
with open("code/out/numden_seq.json", "w") as f:
    json.dump(out, f, indent=2)
print("wrote code/out/numden_seq.json (m=4..40)")
print("p3_num:", out["p3_num"])
print("p4_num:", out["p4_num"])