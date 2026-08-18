from pathlib import Path

def ints(path):
    return [int(x.strip()) for x in Path(path).read_text().splitlines() if x.strip().lstrip('-').isdigit()]
def pairs(path):
    out=[]
    for line in Path(path).read_text().splitlines():
        a=line.split()
        if len(a)==2 and all(x.lstrip('-').isdigit() for x in a): out.append((int(a[0]),int(a[1])))
    return out

for f in ['code/out/seq_rn_50000.txt','code/out/seq_gn.txt','code/out/seq_sp.txt','code/out/seq_p_sorted.txt']:
    x=ints(f); print(f,len(x),x[:12],x[-5:])

a=pairs('code/out/seq_sp_vec_10000000.txt'); s=[y for _,y in a]; p=[x for x,_ in a]
print('S pairs',len(a),'pmax',max(p),'Smax',max(s),'all_even',all(x%2==0 for x in s))
print('residue violations',[(x,y) for x,y in a if x>7 and ((x%3==1 and y%6!=2) or (x%3==2 and y%6!=4))][:5])
