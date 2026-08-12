#!/usr/bin/env python3
"""Measure growth of the vector-sum backtracking level by level, in C-speed-ish
terms: precompute per-column digit patterns and count surviving prefixes.
"""
import sys,time
FULL="""5616185650518293 ;2
3847439647293047 ;1
5855462940810587 ;3
9742855507068353 ;3
4296849643607543 ;3
3174248439465858 ;1
4513559094146117 ;2
7890971548908067 ;3
8157356344118483 ;1
2615250744386899 ;2
8690095851526254 ;3
6375711915077050 ;1
6913859173121360 ;1
6442889055042768 ;2
2321386104303845 ;0
2326509471271448 ;2
5251583379644322 ;2
1748270476758276 ;3
4895722652190306 ;1
3041631117224635 ;3
1841236454324589 ;3
2659862637316867 ;2"""

def parse(t):
    o=[]
    for l in t.strip().splitlines():
        s,c=l.split(";");o.append((s.strip(),int(c.strip())))
    return o

g=parse(FULL); n=len(g); L=len(g[0][0])
targets=[c for _,c in g]
# per column, per digit: pattern bitmask length n -> python int
# pattern[p][d] = int whose bit i set iff guess i has digit d at column p
cols=[g2[0] for g2 in g]
pat=[[0]*10 for _ in range(L)]
for p in range(L):
    for d in range(10):
        m=0
        for i in range(n):
            if cols[i][p]==str(d):
                m|=1<<i
        pat[p][d]=m
# precompute count of set bits for each mask we may need
bitcount={}
def bc(x):
    if x not in bitcount:
        bitcount[x]=bin(x).count('1')
    return bitcount[x]

# full target mask is (1<<n)-1; we match against counts per guess. Use the
# two-sided bound with a full n-bit sum. To keep it fast, represent current
# sum of patterns as python int (each bit = one guess's running count), but
# we need per-guess counts to check bounds, so track counts array.
# Instead count nodes reaching each depth with the bound check.
survived=[0]*(L+1)
def rec(depth, counts):
    survived[depth]+=1
    if depth==L:
        return
    r=L-depth
    for d in range(10):
        ok=True
        nc=counts[:]
        m=pat[depth][d]
        # add bit i to nc[i] where m has bit i
        mm=m
        while mm:
            lb=mm & -mm
            i=lb.bit_length()-1
            nc[i]+=1
            mm-=lb
        for i in range(n):
            if nc[i]>targets[i] or nc[i]+(r-1)<targets[i]:
                ok=False;break
        if ok:
            rec(depth+1,nc)

t=time.time()
rec(0,[0]*n)
print("time",time.time()-t)
print("survivors per depth:",survived)
