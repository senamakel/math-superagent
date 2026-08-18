from pathlib import Path
from ast import literal_eval

def ints(path):
    vals=[]
    for line in Path(path).read_text().splitlines():
        s=line.strip()
        if s and s.lstrip('-').isdigit(): vals.append(int(s))
    return vals

def pairs(path):
    out=[]
    for line in Path(path).read_text().splitlines():
        z=line.split()
        if len(z)==2 and all(x.lstrip('-').isdigit() for x in z): out.append((int(z[0]),int(z[1])))
    return out

for name,path in [('r50000','code/out/seq_rn_50000.txt'),('r999','code/out/seq_rn.txt'),('g999','code/out/seq_gn.txt')]:
    a=ints(path)
    print(name,len(a),a[:12],a[-5:])

for path in ['code/out/seq_sp_vec_10000000.txt','code/out/seq_sp_vec_2000000.txt','code/out/seq_sp_50000.txt']:
    a=pairs(path); print(Path(path).name,'pairs',len(a),'first',a[:5],'last',a[-5:])
    # S in first-appearance order is file order
    S=[x[1] for x in a]; P=[x[0] for x in a]
    print(' C_bad',[(p,s) for p,s in a if p>7 and s%6==0][:5])
    print(' congr_bad',[(p,s) for p,s in a if p>3 and ((p%3==1 and s%6!=2) or (p%3==2 and s%6!=4))][:5])
