"""Verify: |I_{m^2 d0}| = |I_{d0}|  iff  m | b_{d0} (the record b for d0 at n).
More precisely: if b_{d0} is divisible by m then the min over multiples of m 
(coinciding with the d=m^2 d0 problem) is attained at the same value, giving
|I_{m^2 d0}| = |I_{d0}|. If not, they may still coincide but generally differ.
Test this on results_full.txt n=1e13.
"""
import math
res={}
for line in open('/workspace/results_full.txt'):
    p=line.split()
    if p and p[0].isdigit():
        res[int(p[0])]=(int(p[1]),int(p[2]),int(p[3]))
non_sq=sorted(d for d in range(2,100) if math.isqrt(d)**2!=d)
ok=0; total=0; fails=[]
for d0 in non_sq:
    for m in range(2,10):
        d1=m*m*d0
        if d1 in res and d1!=d0:
            total+=1
            b0=res[d0][0]
            same = (res[d1][2]==res[d0][2])
            pred = (b0 % m == 0)
            if same==pred:
                ok+=1
            else:
                fails.append((d1,d0,m,same,pred,b0%m))
print(f"rule |I_{'{m^2d0}'}|==|I_{'{d0}'}| iff m|b0 : {ok}/{total} correct")
for f in fails:
    print("  FAIL", f)
# also check that when same, b_{d1} = b_{d0}/m (the rescaled value within [0,L1])
okb=0; totb=0; bfails=[]
for d0 in non_sq:
    for m in range(2,10):
        d1=m*m*d0
        if d1 in res and d1!=d0 and res[d1][2]==res[d0][2]:
            totb+=1
            if res[d1][0] == res[d0][0]//m:
                okb+=1
            else:
                bfails.append((d1,d0,m,res[d1][0],res[d0][0]//m))
print(f"when equal, b_{'{m^2d0}'} == b_{'{d0}'}/m : {okb}/{totb}")
for f in bfails[:10]:
    print("  bfail", f)