from pathlib import Path
from collections import Counter

def read_pairs(path):
    out=[]
    for line in Path(path).read_text().splitlines():
        z=line.split()
        if len(z)==2 and all(t.isdigit() for t in z): out.append((int(z[0]),int(z[1])))
    return out

def read_ints(path): return [int(x) for x in Path(path).read_text().split()]

pairs=read_pairs('code/out/seq_sp_vec_10000000.txt')
print('S pairs',len(pairs),'p max',max(p for p,s in pairs),'S max',max(s for p,s in pairs))
print('all S even',all(s%2==0 for p,s in pairs))
print('p>7 S mod6 counts',Counter(s%6 for p,s in pairs if p>7))
print('p>7 mod6 violations',[(p,s) for p,s in pairs if p>7 and s%6==0])
print('mod3 exceptions',[(p,s) for p,s in pairs if p>3 and s%6 != (2 if p%3==1 else 4)])
for f in ['code/out/seq_rn_50000.txt','code/out/seq_gn.txt']:
 a=read_ints(f)
 print(f,'terms',len(a),'minmax',min(a),max(a),'gcd',__import__('math').gcd(*a))
 print('first 20',a[:20])
 print('last 10',a[-10:])
