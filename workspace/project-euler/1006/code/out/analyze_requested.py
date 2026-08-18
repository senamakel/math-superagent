from pathlib import Path
from collections import Counter
from fractions import Fraction
import re

def load(name):
 p=Path('code/out')/name
 out=[]
 for line in p.read_text().splitlines():
  a=line.split()
  if a and a[0].lstrip('-').isdigit():
   nums=[int(x) for x in a if x.lstrip('-').isdigit()]
   out.append(nums)
 return out

def scalar(name,col=1): return [x[col] for x in load(name) if len(x)>col]
def first_falsifier(a, pred):
 for i,x in enumerate(a[1:],2):
  if not pred(i,x,a): return i,x
 return None

def berlekamp_massey(seq, mod):
 C=[1]; B=[1]; L=0; m=1; b=1
 for n in range(len(seq)):
  d=seq[n]%mod
  for i in range(1,L+1): d=(d+C[i]*seq[n-i])%mod
  if d==0: m+=1; continue
  T=C[:]; coef=d*pow(b,-1,mod)%mod
  if len(C)<len(B)+m:C += [0]*(len(B)+m-len(C))
  for j in range(len(B)): C[j+m]=(C[j+m]-coef*B[j])%mod
  if 2*L<=n: L=n+1-L; B=T; b=d; m=1
  else:m+=1
 return L,C

def report(name,a):
 print('\n',name,'terms',len(a),'first',a[:10])
 for label,p in [('affine',lambda i,x,s:x==s[-2]+(s[-2]-s[-3]) if i>=3 else True),
  ('fib-add',lambda i,x,s:i<3 or x==s[-2]+s[-3]),
  ('shift100',lambda i,x,s:i<2 or x==100*s[-2])]:
  print(label,first_falsifier(a,p))
 for mod in [101001001,100,1000]:
  b=[x%mod for x in a]
  try: print('BM mod',mod,berlekamp_massey(b,mod)[0])
  except ValueError: print('BM mod',mod,'not applicable (nonunit discrepancy)')

for f in ['psi_exact.txt','psi_residues.txt','c1_terms.txt','lmin.txt','ext_recurrence.txt']:
 rows=load(f); print('\nFILE',f,'rows',len(rows),'widths',Counter(map(len,rows)))
 if f.startswith('psi'): report(f,scalar(f))
# targeted ext columns
r=load('ext_recurrence.txt')
for c in range(1,5): print('ext col',c,scalar('ext_recurrence.txt',c)[:15])
# c1 golden floor check and lmin formula inspect
c=scalar('c1_terms.txt'); print('c1 first diff', [c[i]-c[i-1] for i in range(1,30)])
l=scalar('lmin.txt'); print('lmin first',l[:20], 'diff', [l[i]-l[i-1] for i in range(1,20)])
