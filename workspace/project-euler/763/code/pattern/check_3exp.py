#!/usr/bin/env python3
"""Check full structure conjecture:
  mult(hist) = 2^{2*n4} * 3^{?} 
Find the (single) exception, and test whether 3-exponent equals some function
of (n5, or positions of 5s).  Report first the exceptions, then samples."""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def f23(v):
    a=b=0
    while v%2==0: v//=2; a+=1
    while v%3==0: v//=3; b+=1
    return a,b,v

excepts=[]
rows=[]
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in sorted(per.items(), key=lambda kv:-kv[1]):
        vals=list(map(int,hist.split()))
        n4=vals.count(4)
        a,b,rest=f23(m)
        if a!=2*n4 or rest!=1:
            excepts.append((n,hist,m,a,b,rest,n4))
        rows.append((n,hist,m,vals,a,b))

print("EXCEPTIONS (should be 1 expected: the 0 1 3 6 7 5 3 with factor 5):")
for e in excepts: print("  ",e)

# Now: for pure 2^a*3^b ones, fit b as function of histogram. Collect (n4,n5,n3,...)->b
data=collections.defaultdict(list)
for n,hist,m,vals,a,b in rows:
    if m not in (0,):
        pass
    n4=vals.count(4); n5=vals.count(5); n3=vals.count(3); n6=vals.count(6); n7=vals.count(7)
    data[(a,n4,n5,n3,n6,n7,tuple(vals))].append((n,b))
# show b vs a/n for the '2 2 2 ... 3' diagonal histograms
print("\nDiagonal family (0 2 2 ... 2 3): n4=0, a=0, b=n-1? check:")
for k,v in sorted(data.items()):
    a,n4,n5,n3,n6,n7,vals=k
    if n4==0 and n5==0:
        print(f"   vals={vals}  a={a} b={[bb for _,bb in v]}  n={[nn for nn,_ in v]}")
