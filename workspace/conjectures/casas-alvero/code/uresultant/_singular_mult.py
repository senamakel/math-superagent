"""Singular: exact multiplicity (= length, ideal is m-primary at origin) of
R/I at n=4 slice a1=0. Compare to the eliminant degree."""
import subprocess, tempfile, os, sympy as sp
from sympy import symbols, Poly, expand, resultant, factor
a1,a2,a3,a4 = symbols('a_1 a_2 a_3 a_4')
x = symbols('x')
def hasse(f,x,i):
    p=Poly(sp.expand(f),x);c={j:p.coeff_monomial(x**j) for j in range(p.degree()+1)}
    return sum(sp.binomial(j,i)*cc*x**(j-i) for j,cc in c.items() if j>=i)
f=x**4+a1*x**3+a2*x**2+a3*x+a4
R=[sp.expand(resultant(f,hasse(f,x,i),x).subs(a1,0)) for i in (1,2,3)]

script = """
ring R = 0,(a(2),a(3),a(4)),dp;
ideal I = %s;
ideal G = std(I);
int L = vdim(G);
"VIRTUAL_DIM=" + string(L);
// multiplicity at 0 by reading GB over (a2,a3,a4) with local ordering? use mult via locstd
LIB "primdec.lib";
list P = primdecGTZ(I);
"PRIMARY_COMPONENTS=" + string(size(P));
for (int k=1;k<=size(P);k++) {
  "  comp k: ideal=" + string(P[k][1]) + "  isolated?";
}
"LOCAL_MULT: use std then mult at origin";
"""
# Actually vdim gives the dimension of the quotient for a 0-dim ideal = length
# write R polys as singular
def tosing(expr):
    s=str(sp.expand(expr))
    for nm in ['a_2','a_3','a_4']:
        s=s.replace(nm, nm.replace('_','(')+')') # a_2 -> a(2)
    s=s.replace('a(2)','a(2)').replace('a(3)','a(3)').replace('a(4)','a(4)')
    return s

rstr = ",".join(tosing(r) for r in R)
script = """
ring R = 0,(a(2),a(3),a(4)),dp;
ideal I = %s;
ideal G = std(I);
int L = vdim(G);
"VIRTUAL_DIM=" + string(L);
list P = primdecGTZ(I);
"NUM_COMP=" + string(size(P));
""" % rstr
fd,path = tempfile.mkstemp(suffix=".sing")
with os.fdopen(fd,"w") as fh: fh.write(script)
proc = subprocess.run(["Singular","-q",path],capture_output=True,text=True,timeout=600)
print(proc.stdout)
print("STDERR:", proc.stderr[-2000:] if proc.stderr else "")
os.unlink(path)
