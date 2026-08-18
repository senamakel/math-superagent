"""Exact finite-range checks of non-Psi Fibonacci-word sequences."""
from fractions import Fraction
from math import sqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'

def fibs(n):
    a,b=1,2
    out=[]
    while a<=n:
        out.append(a); a,b=b,a+b
    return out

def c1(k):
    # count leading-one factors by direct factors
    w='0'
    while len(w)<3*k+20: w,w0=w+'0',''
    a,b='0','01'
    while len(b)<3*k+20: a,b=b,b+a
    return sum(x[0]=='1' for x in {b[i:i+k] for i in range(len(b)-k+1)})

def lmin_direct(k, w):
    seen=set()
    for i in range(len(w)-k+1):
        seen.add(w[i:i+k])
        if len(seen)==k+1:return i+k
    return None

def main():
    # exact Fibonacci word prefix, enough for supplied finite ranges
    a,b='0','01'
    while len(b)<10000: a,b=b,b+a
    rows=[]
    for k in range(1,1001):
        fs={b[i:i+k] for i in range(len(b)-k+1)}
        c=sum(s[0]=='1' for s in fs)
        fib=next(x for x in fibs(10**7) if x>k)
        lm=lmin_direct(k,b)
        rows.append((k,c,1+(k*(3-sqrt(5))//2),lm,k+fib-1))
    c1bad=next((r for r in rows if r[1]!=1+int(r[0]*(3-sqrt(5))/2)),None)
    lbad=next((r for r in rows if r[3]!=r[4]),None)
    print('c1 formula first falsifier:',c1bad)
    print('Lmin formula first falsifier:',lbad)
    print('c1 exact sample k=1..20:',[(k,c) for k,c,_,_,_ in rows[:20]])
    print('Lmin exact sample k=1..20:',[(k,l) for k,_,_,l,_ in rows[:20]])

if __name__=='__main__':main()
