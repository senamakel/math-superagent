import json
from lib.gilbreath import primes_up_to
P = primes_up_to(500000)
u = [0]*len(P)
for i,p in enumerate(P):
    u[i] = 1 if p%4==1 else (-1 if p%4==3 else 0)
i0 = P.index(2)
uv = u[i0+1:]
# e over n: for each prefix of pairs
# e(n) = #switches - #nonswitches among first n pairs (p_2..p_{n+1})
e = []
sw = nsw = 0
for k in range(3, len(uv)+1):
    if uv[k-2]==uv[k-1]:
        nsw += 1
    else:
        sw += 1
    e.append(sw - nsw)
# examine: how many zeros / small values
vals = e  # index 0 corresponds to n=3
nf = len(vals)
zeros = [ (i+3) for i,v in enumerate(vals) if v==0 ]
print("total n (pairs):", nf)
print("count of n with e=0:", len(zeros), "at n in", zeros[:60])
# tail minima
# recompute min properly (loop below)
import sys
for T in [17,100,1000,10000,30000, 50000, len(vals)+2]:
    seg = [( (i+3), v) for i,v in enumerate(vals) if (i+3)>=T]
    if seg:
        mn = min(v for _,v in seg)
        n_at = [n for n,v in seg if v==mn][0]
        print("min e over n>=%d = %d at n=%d" % (T, mn, n_at))
