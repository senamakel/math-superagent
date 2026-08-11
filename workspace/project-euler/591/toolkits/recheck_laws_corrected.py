"""Re-check the m^2*divisibility scaling law and |I|-relation on the CORRECTED both-sign data."""
import math, mpmath as mp
mp.mp.dps=50
PI = mp.mpf('3.14159265358979323846264338327950288419716939937510')

res = {}
for line in open('/workspace/results_full_bothsides.txt'):
    p = line.split()
    if p and p[0].isdigit():
        res[int(p[0])] = (int(p[1]), int(p[2]), int(p[3]))

# |I| = |nint(b sqrt d - pi)| relation
ok_rel = 0; tot = 0; fails = []
for d in res:
    b,a,absa = res[d]
    sd = mp.sqrt(d)
    r = abs(mp.nint(b*sd - PI))       # |round(b sqrt d - pi)|
    tot += 1
    if r == absa: ok_rel += 1
    else: fails.append((d, r, absa))
print(f"|I| == |nint(b*sqrt(d)-pi)|: {ok_rel}/{tot}, fails={fails[:5]}")

# m^2 scaling law (b divisible rule)
ok=0; tot=0; fails=[]
for d0 in sorted(res):
    for m in range(2,10):
        d1 = m*m*d0
        if d1 in res and d1 != d0:
            tot += 1
            b0 = res[d0][0]
            same = (res[d1][2] == res[d0][2])
            pred = (b0 % m == 0)
            if same == pred: ok += 1
            else: fails.append((d1,d0,m,same,pred,b0%m))
print(f"m^2 law: {ok}/{tot}, fails={fails}")
# when equal, b1 = b0/m?
okb=0; totb=0; bf=[]
for d0 in sorted(res):
    for m in range(2,10):
        d1=m*m*d0
        if d1 in res and d1!=d0 and res[d1][2]==res[d0][2]:
            totb+=1
            if res[d1][0] == res[d0][0]//m: okb+=1
            else: bf.append((d1,d0,m,res[d1][0],res[d0][0]))
print(f"when equal, b1 == b0/m (integer div): {okb}/{totb}, fails={bf[:5]}")