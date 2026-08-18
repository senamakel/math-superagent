#!/usr/bin/env python3
from pathlib import Path
import ast

def ints(path):
    text=Path(path).read_text()
    return [int(x) for x in text.split() if x.lstrip('-').isdigit()]

def pairs(path):
    out=[]
    for line in Path(path).read_text().splitlines():
        a=line.split()
        if len(a)==2 and all(x.lstrip('-').isdigit() for x in a):
            out.append((int(a[0]),int(a[1])))
    return out

for f in ['code/out/seq_sp_vec_10000000.txt','code/out/seq_sp_50000.txt']:
    a=pairs(f)
    s=[y for _,y in a]
    p=[x for x,_ in a]
    print(f, 'pairs',len(a),'p_first_last',p[:5],p[-5:],'S_first_last',s[:5],s[-5:])
    print('all S even:',all(x%2==0 for x in s))
    print('p>7 residue violations:',[(x,y) for x,y in a if x>7 and ((x%3==1 and y%6!=2) or (x%3==2 and y%6!=4))][:10])
    print('S divisible by 6 for p>7:',[(x,y) for x,y in a if x>7 and y%6==0][:10])

for f in ['code/out/seq_rn.txt','code/out/seq_gn.txt','code/out/seq_rn_50000.txt']:
    a=ints(f)
    print(f,'terms',len(a),'head',a[:12],'tail',a[-12:])
    print('min,max',min(a),max(a),'gcd',__import__('math').gcd(*a))

fail=[302,332,458,542,632,692,872,902,1544,1964,2522,2642,2834,4544,4952,6932,7442,9170,11114,11672,12224,13562,17072,22922,34082,34892,35912]
print('Chen failures',len(fail),'all 2 mod 6',all(x%6==2 for x in fail),'gaps',[b-a for a,b in zip(fail,fail[1:])])
