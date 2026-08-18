from pathlib import Path
from collections import Counter

MOD = 101001001

def rows(name):
    out=[]
    for line in (Path('code/out')/name).read_text().splitlines():
        a=line.split()
        if len(a)>=2 and a[0].lstrip('-').isdigit():
            out.append([int(x) for x in a if x.lstrip('-').isdigit()])
    return out

def bm(seq, mod):
    C=[1]; B=[1]; L=0; m=1; b=1
    for n in range(len(seq)):
        d=seq[n]%mod
        for i in range(1,L+1): d=(d+C[i]*seq[n-i])%mod
        if d==0: m+=1; continue
        T=C[:]; coef=d*pow(b,-1,mod)%mod
        C += [0]*max(0,len(B)+m-len(C))
        for j in range(len(B)): C[j+m]=(C[j+m]-coef*B[j])%mod
        if 2*L<=n: L=n+1-L; B=T; b=d; m=1
        else: m+=1
    return L, C

def analyze(name, col=1):
    seq=[r[col] for r in rows(name) if len(r)>col]
    print(f'{name} terms={len(seq)} first10={seq[:10]}')
    print('BM modulus', MOD, 'order=', bm(seq,MOD)[0])
    if name=='c1_terms.txt':
        d=[seq[i]-seq[i-1] for i in range(1,len(seq))]
        print('first differences=',d[:30])
    if name=='lmin.txt':
        d=[seq[i]-seq[i-1] for i in range(1,len(seq))]
        print('first differences=',d[:30])

for n in ('psi_exact.txt','psi_residues.txt','c1_terms.txt','lmin.txt','ext_recurrence.txt'):
    analyze(n)
