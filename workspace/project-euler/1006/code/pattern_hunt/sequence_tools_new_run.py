from pathlib import Path
import sympy as sp

ROOT=Path('code/out')

def load(name, col=1):
    rows=[]
    for line in (ROOT/name).read_text().splitlines():
        z=line.split()
        try:
            nums=[int(x) for x in z]
            if len(nums)>col: rows.append(nums[col])
        except ValueError: pass
    return rows

def bm_order(a, mod):
    C=[1]; B=[1]; L=0; m=1; b=1
    for n in range(len(a)):
        d=a[n]%mod
        for i in range(1,L+1): d=(d+C[i]*a[n-i])%mod
        if d==0: m+=1; continue
        T=C[:]; coef=d*pow(b,-1,mod)%mod
        if len(C)<len(B)+m: C += [0]*(len(B)+m-len(C))
        for j in range(len(B)): C[j+m]=(C[j+m]-coef*B[j])%mod
        if 2*L<=n: L=n+1-L; B=T; b=d; m=1
        else: m+=1
    return L

def report(name,col):
    a=load(name,col)
    print(name,'terms',len(a),'first10',a[:10])
    if len(a)>=4:
      for r in range(1, min(12,len(a)//2)+1):
        try: rec=sp.polys.ring_series.find_simple_recurrence(a,n=r)
        except Exception: rec=None
        if rec not in (None,[],[0]*r): print(' exact_simple_recurrence',r,rec)
    for mod in (101001001,100,1000):
      try: print(' BM',mod,bm_order(a,mod))
      except ValueError: print(' BM',mod,'nonunit')
    d=[a[i+1]-a[i] for i in range(len(a)-1)]
    print('diff_first20',d[:20])

for name,col in [('psi_exact.txt',0),('psi_residues.txt',1),('c1_terms.txt',1),('lmin.txt',1),('r_runs_wythoff.txt',1),('dj_raw.txt',1),('dj_mod.txt',1),('vr_runvals.txt',1),('vr_rungaps.txt',1),('counts.txt',1),('ext_recurrence.txt',1)]:
    report(name,col)
