from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
FILES={
 'psi_exact':'psi_exact.txt','psi_residues':'psi_residues.txt','c1':'c1_terms.txt',
 'lmin':'lmin.txt','dj':'dj_raw.txt','toeplitz_defects':'topelitz_defects.txt',
}

def rows(name):
 p=ROOT/'out'/FILES[name]
 out=[]
 for line in p.read_text().splitlines():
  t=[]
  for x in line.replace(',',' ').split():
   try:t.append(int(x))
   except ValueError:pass
  if t: out.append(t[-1])
 return out

def rec(seq,r):
 if len(seq)<=2*r:return None
 cs=sp.symbols('c:'+str(r))
 eq=[sp.Eq(seq[i],sum(cs[j]*seq[i-1-j] for j in range(r))) for i in range(r,len(seq))]
 sols=sp.solve(eq,cs,dict=True)
 for s in sols:
  c=tuple(s.get(x,x) for x in cs)
  if all(seq[i]==sum(c[j]*seq[i-1-j] for j in range(r)) for i in range(r,len(seq))):return c
 return None

def first_bad(seq,p):
 for i,x in enumerate(seq):
  if not p(i,x):return i+1,x
 return None

for name in FILES:
 s=rows(name)
 print(f'{name}: n={len(s)} prefix={s[:10]} suffix={s[-3:]}')
 hit=None
 for r in range(1,13):
  c=rec(s,r)
  if c: hit=(r,c);break
 print('  rational_recurrence<=12=',hit)
 d=[s[i+1]-s[i] for i in range(len(s)-1)]
 print('  diff_prefix=',d[:15])
 if name=='c1':
  # exact integer floor using alpha=(3-sqrt5)/2
  a=(3-sp.sqrt(5))/2
  print('  c1_formula_first_bad=',first_bad(s,lambda i,x:x==1+sp.floor((i+1)*a)))
 if name=='lmin':
  fib=[0,1]
  while fib[-1]<max(s)+2:fib.append(fib[-1]+fib[-2])
  def nxt(k):return next(x for x in fib if x>k)
  print('  lmin_formula_first_bad=',first_bad(s,lambda i,x:x==(i+1)+nxt(i+1)-1))
 if name=='toeplitz_defects':
  print('  zero_indices=',[i+1 for i,x in enumerate(s) if x==0])
  print('  universal_zero_first_bad=',first_bad(s,lambda i,x:x==0))
 if name=='dj':
  print('  dj_fib_additive_first_bad=',first_bad(s,lambda i,x: i<2 or x==s[i-1]+s[i-2]))
