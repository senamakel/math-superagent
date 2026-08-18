from pathlib import Path

def ints(path):
    out=[]
    for line in Path(path).read_text().splitlines():
        s=line.strip()
        if s and s.lstrip('-').isdigit(): out.append(int(s))
    return out

def pairs(path):
    out=[]
    for line in Path(path).read_text().splitlines():
        z=line.split()
        if len(z)==2 and all(x.lstrip('-').isdigit() for x in z): out.append((int(z[0]),int(z[1])))
    return out

r=ints('code/out/seq_rn_50000.txt')
g=ints('code/out/seq_gn.txt')
a=pairs('code/out/seq_sp_vec_10000000.txt')
print('lengths',len(r),len(g),len(a))
print('r first20',r[:20]); print('r last5',r[-5:])
print('g first20',g[:20]); print('g last5',g[-5:])
print('S first20',[s for p,s in a[:20]])
print('S all_even',all(s%2==0 for p,s in a))
print('p>7 S%6 violations',[(p,s) for p,s in a if p>7 and s%6==0])
print('p>7 residue violations',[(p,s) for p,s in a if p>7 and ((p%3==1 and s%6!=2) or (p%3==2 and s%6!=4))])
print('S first differences',[a[i][1]-a[i-1][1] for i in range(1,min(20,len(a)))])
