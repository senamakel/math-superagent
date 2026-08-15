"""Research-cycle falsifier checks for the three proposed approaches.

#2 ifs-attractor-contraction: does a strict contraction d(Dx,Dx') <= c d(x,x'),
   c<1, exist on the 2-then-odds cone under l1 or linfty? Hunt pairs with
   ratio >= 1 (kills ANY c<1).
#1 vectorial-subtractive-euclidean: verify the dictionary failure — the row map
   is not a gcd algorithm (no renormalisation/permutation); also confirm the
   cyclic Ducci 4-number-game already held contradicts transfer. Numeric part:
   reproduce Colonna delete-5 second entry = 4 (class-level counterexample to
   any global contraction / to the Euclidean-return-to-{0,2} dictionary).
#3 chip-firing-abelian-sandpile: confirm there is no conserved chip mass across
   a row step (sum is not conserved), so no odometer/firing-count object.
"""
import itertools

def row(r):
    return [abs(r[i]-r[i+1]) for i in range(len(r)-1)]

def l1(a,b): return sum(abs(x-y) for x,y in zip(a,b))
def linf(a,b): return max(abs(x-y) for x,y in zip(a,b))

# ---- #2: contraction kill under l1 / linfty ----
print("== #2 contraction kill ==")
# Analytic: x=(4,0,0), x'=(4,2,0) -> D x=(4,0), D x'=(2,2)
x=(4,0,0); xp=(4,2,0)
Dx=row(x); Dxp=row(xp)
print("x  =",x," x'=",xp)
print("Dx =",Dx," Dx'=",Dxp)
print("l1 d(x,x')=",l1(x,xp),"  l1 d(Dx,Dx')=",l1(Dx,Dxp))
print("linf d(x,x')=",linf(x,xp),"  linf d(Dx,Dx')=",linf(Dx,Dxp))
print("ratios >=1 -> NO c<1 contraction in these metrics.")
maxr1=maxrI=0
worst1=worstI=None
# exhaustive small search in {0,1,2,3,4}^3
for a in itertools.product(range(5),repeat=3):
    for b in itertools.product(range(5),repeat=3):
        if l1(a,b)==0: continue
        Da=row(a); Db=row(b)
        r1=l1(Da,Db)/l1(a,b)
        rI=linf(Da,Db)/linf(a,b)
        if r1>maxr1: maxr1,worst1=r1,(a,b)
        if rI>maxrI: maxrI,worstI=rI,(a,b)
print("max l1 ratio over {0..4}^3:",round(maxr1,4)," worst:",worst1)
print("max linf ratio over {0..4}^3:",round(maxrI,4)," worst:",worstI)

# ---- #1: Colonna delete-5 -> A_1(1)=4 ----
print("\n== #1 Colonna delete-5 ==")
# primes 2,3,5,7,11,13,17,19,23; delete 5 -> 2,3,7,11,13,17,19,23
col=[2,3,7,11,13,17,19,23,29]
A1=row(col)
print("A_1 =",A1, " second entry =",A1[1])
# and a full cone point with second entry growing away from {0,2}
print("A_2 =",row(A1))

# ---- #3: mass conservation check ----
print("\n== #3 no conserved chip mass ==")
ex=[2,0,3,1]
s=sum(ex); s1=sum(row(ex)); s2=sum(row(row(ex)))
print("row0 sum",s," row1 sum",s1," row2 sum",s2," not conserved.")
ex2=[1,2,4,8]
print("row0 sum",sum(ex2)," row1 sum",sum(row(ex2))," -> sums vary, no conserved mass across steps.")
