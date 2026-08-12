#!/usr/bin/env python3
"""Test the conjectured structural regularity: p(n,L) is a rational function of
m = L/40 of degree (n-1)/(n-1).

Known:
  n=2: p = m/(2m-1)                  [degree 1/1, proven closed form]
  n=3: p = (7m^2-17m+12)/(18m^2-45m+27)  [degree 2/2, verified on 28 pts]
  n=4: fit  deg 3/3                  [to be tested on ALL held-out points]

Load every exact p(4,L) point on disk, test the 3/3 fit on points it was NOT
fit from (2100,2300,2700,2900,3400,3800,4200,4600,4800), and also try to find
a lower-degree fit that passes ALL points (to ensure 3/3 is minimal).
"""
from fractions import Fraction as F

# All exact p(4,L) points from the json files on disk
P4 = {
    160: "7/15", 240: "187/378", 320: "1951/3861", 400: "521/1020",
    480: "3077/5985", 560: "16033/31050", 640: "2839/5481",
    800: "54559/104895", 900: "143561/275520", 1000: "25382/48645",
    1100: "2493559/4773600", 1200: "68843/131670", 1300: "474941/907680",
    1400: "677228/1293435", 1500: "2249593/4294080", 1600: "57511/109725",
    1800: "166802/317985", 2000: "1044769/1990440", 2100: "6490703/12362400",
    2300: "25860019/49230720", 2500: "3723481/7085760", 2700: "1575557/2997280",
    2900: "53060149/100910880", 3000: "2454796/4667985", 3400: "1203242/2287065",
    3800: "15239168/28956015", 4000: "990791/1882335", 4200: "6902786/13112415",
    4600: "3038972/5771475", 4800: "5191253/9858015", 5000: "35280338/66990105",
}
pts = sorted((F(L, 40), F(v)) for L, v in P4.items())
print(f"{len(pts)} exact p(4,L) points")

# Candidate 3/3 fit found on the 22 older points:
# N = -9/2 + (61/9)m + (-119/36)m^2 + (19/36)m^3
# D = -15/2 + (47/4)m - 6 m^2 + m^3
def p4_fit(m):
    N = F(-9,2) + F(61,9)*m + F(-119,36)*m*m + F(19,36)*m*m*m
    D = F(-15,2) + F(47,4)*m - 6*m*m + m*m*m
    return N/D

bad = []
for m, p in pts:
    if p4_fit(m) != p:
        bad.append((m, p, p4_fit(m)))
print("3/3 fit mismatches:", len(bad))
for b in bad:
    print("  ", b)

# leading-coefficient limit: (19/36)/1
print("limit m->inf (pure-bump, n=4):", F(19,36), float(F(19,36)))
