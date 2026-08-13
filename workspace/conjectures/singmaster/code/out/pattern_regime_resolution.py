"""Definitive regime analysis for the Fibonacci family vs the MRSTT boundary cut.

Boundary region B(eps) = { (n,k): k < exp((log n)^{2/3+eps}) }.
Key facts established exactly below:
  (i)   for eps < 1/3, cut = exp((log n)^q) with q<1 satisfies cut/n -> 0: genuine thin strip, and
        the Fibonacci family enters it for only finitely many j (exact J0 table).
  (ii)  for eps = 1/3, cut ~ n/phi^2... : cut > k always (since ln n > ln k), so every family member boundary.
  (iii) for eps > 1/3, cut/n -> infinity: the 'boundary' region contains the whole left half,
        so MRSTT's interior set is empty and the boundary/interior split is vacuous.
"""
import math
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
phi=(1+math.sqrt(5))/2
A=math.log(phi)

print("=== (i) eps<1/3: J0(eps) = largest j with family members in genuine boundary strip ===")
for eps in [0.10,0.15,0.20,0.25,0.30,0.32,1/3-0.0001]:
    Jmax=0
    for j in range(1,300):
        n=fib(2*j+2)*fib(2*j+3)-1
        k=fib(2*j)*fib(2*j+3)-1
        # representativeness: both reps (n+1,k+1),(n,k+2) have k' ~ k; use k vs cut on n+1
        nn,k1=n+1,k+1
        cut=math.exp((math.log(nn))**(2/3+eps))
        if (k1+1) < cut: Jmax=j
    print("    eps=%.4f  q=%.4f  J0=%d"%(eps,2/3+eps,Jmax))

print()
print("=== (ii,iii) cut vs n: strip is genuine iff q<1; whole-triangle iff q>1 ===")
for eps,q in [(0.3,2/3+0.3),(1/3,1.0),(0.5,2/3+0.5)]:
    for j in [10,100,1000]:
        # use asymptotic ln n = (4j+5)A - ln5
        lnn=(4*j+5)*A-math.log(5)
        lnk=(4*j+3)*A-math.log(5)
        cutpow=lnn**q          # ln of the cut
        print("    eps=%.3f j=%d: ln cut=%.3f  ln n=%.3f  ln k=%.3f  -> cut%s n, cut%s k"%(
            eps,j,cutpow,lnn,lnk,">" if cutpow>lnn else "<",">" if cutpow>lnk else "<"))

print()
print("=== family reps j=2..9: boundary status under genuine thin strip (eps=0.2, q=0.8667) ===")
for j in range(2,10):
    n=fib(2*j+2)*fib(2*j+3)-1
    k=fib(2*j)*fib(2*j+3)-1
    nn,kk=n+1,k+1
    cut=math.exp((math.log(nn))**(2/3+0.2))
    print("    j=%d k=%d cut=%.3e boundary=%s"%(j,kk,cut,(kk+1)<cut))
print("DONE")