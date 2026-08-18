from pathlib import Path
import sympy as sp
R=Path('code/out')
def read(name,last=False):
 a=[]
 for l in (R/name).read_text().splitlines():
  z=l.split()
  if not z: continue
  try:a.append(int(z[-1] if last else z[0]))
  except:pass
 return a
def first_bad(a,pred):
 for i,x in enumerate(a):
  if not pred(i+1,x):return i+1,x
 return None
# psi_exact is one-column; residues have index + residue
for name,last in [('psi_exact.txt',False),('psi_residues.txt',True)]:
 a=read(name,last)
 print(name,'psi mod100==c1:',first_bad(a,lambda k,x:x%100==read('c1_terms.txt')[k-1]%100))
 print(name,'psi mod1000==c1:',first_bad(a,lambda k,x:x%1000==read('c1_terms.txt')[k-1]%1000))
# exact finite identities in the already generated range
c=read('c1_terms.txt',True)
print('c1 first differences first 20:',[c[i]-c[i-1] for i in range(1,20)])
d=read('dj_raw.txt',True)
print('dj length',len(d),'values',sorted(set(d))[:20],'max',max(d))
print('dj adjacent Fibonacci recurrence first bad:',first_bad(d,lambda j,x: x==d[j-2]+d[j-3] if j>=3 else True))
# run start formula from existing report, independently exact using integer sqrt bounds
s=[]
for l in (R/'vr_runvals.txt').read_text().splitlines():
 z=l.split()
 if len(z)>=2:
  try:s.append(int(z[0]))
  except:pass
print('vr run positions n',len(s),'first',s[:12])
print('vr gaps',sorted(set(s[i+1]-s[i] for i in range(len(s)-1))))
print('vr gap first 40',[s[i+1]-s[i] for i in range(min(40,len(s)-1))])
