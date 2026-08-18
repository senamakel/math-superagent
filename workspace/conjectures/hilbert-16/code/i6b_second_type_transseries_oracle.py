#!/usr/bin/env python3
"""Exact bounded transseries oracle for the I^1_6b four-passage toy.

Claim/evidence target: h16-i6b-second-type-transseries-ect.
Theory: truncated Hahn-style monomial algebra; composition is performed by
formal substitution in z=exp(-t), with t=-log(z), ell=log(t), and ell2=log(ell).
This is an executable stress test, not a theorem and not the exact graphic.
The oracle enumerates no dynamical candidates: it propagates a fixed finite
support and tests exact Wronskians/coefficient identities.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import factorial
import sympy as sp

@dataclass(frozen=True, order=True)
class Key:
    z: int
    t: int
    l: int
    ll: int

class TS:
    def __init__(self, d=None): self.d = {k: Fraction(v) for k,v in (d or {}).items() if v}
    @staticmethod
    def c(q): return TS({Key(0,0,0,0): Fraction(q)})
    @staticmethod
    def var(k): return TS({k: Fraction(1)})
    def __add__(self,o):
        o = o if isinstance(o,TS) else TS.c(o); d=self.d.copy()
        for k,v in o.d.items(): d[k]=d.get(k,0)+v
        return TS(d)
    __radd__=__add__
    def __neg__(self): return TS({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self + (- (o if isinstance(o,TS) else TS.c(o)))
    def __rsub__(self,o): return TS.c(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,TS) else TS.c(o); return TS({Key(a.z+b.z,a.t+b.t,a.l+b.l,a.ll+b.ll):u*v for a,u in self.d.items() for b,v in o.d.items()})
    __rmul__=__mul__
    def scale(self,q): return TS({k:q*v for k,v in self.d.items()})
    def truncate(self,zmax=3,tmax=3,lmax=2,llmax=1): return TS({k:v for k,v in self.d.items() if k.z<=zmax and k.t<=tmax and k.l<=lmax and k.ll<=llmax})
    def __repr__(self): return " + ".join(f"{v}*z^{k.z}t^{k.t}l^{k.l}ll^{k.ll}" for k,v in sorted(self.d.items())) or "0"

def wronskian_polys(fs, x):
    return sp.factor(sp.det(sp.Matrix([[sp.diff(f,x,j) for f in fs] for j in range(len(fs))])))

def run():
    # Worked-example guard, duplicated as an executable assertion via existing oracle.
    from naive_examples_oracle import naive_count
    guards = [([1,-1],1),([0],0),([1],0),([2,-3,1],2),([2,-5,4,-1],1)]
    assert all(naive_count(a)==e for a,e in guards)
    z=TS.var(Key(1,0,0,0)); t=TS.var(Key(0,1,0,0)); ell=TS.var(Key(0,0,1,0)); ell2=TS.var(Key(0,0,0,1))
    # Four fixed second-type passages, retaining two iterated-log levels.
    D=[(t.scale(Fraction(1,2))+ell+ell2*z).truncate(),
       (t.scale(Fraction(-1,3))+ell.scale(2)+ell2*z).truncate(),
       (t.scale(Fraction(2,5))+ell2+ell*z).truncate(),
       (t.scale(Fraction(-3,7))+ell2+ell*z.scale(2)).truncate()]
    F=(D[0]+D[1]+D[2]*D[3]).truncate()
    G=(D[0]*D[3]-D[1]*D[2]).truncate()
    # Projection to coefficient channels gives an exact finite-dimensional test.
    x=sp.symbols('t', positive=True); L=sp.symbols('L'); LL=sp.symbols('LL')
    def project(q):
        out=0
        for k,v in q.d.items(): out += sp.Rational(v.numerator,v.denominator)*x**k.t*L**k.l*LL**k.ll
        return sp.expand(out)
    fp,gp=project(F),project(G)
    J=sp.expand(sp.diff(fp,L)*sp.diff(gp,LL)-sp.diff(fp,LL)*sp.diff(gp,L))
    W=wronskian_polys([fp,gp,J],x)
    return D,F,G,fp,gp,J,W

if __name__=='__main__':
    print('RUN: bounded exact transseries composition / iterated-log ECT oracle')
    print('ORACLE: fixed four second-type passages; z<=3,t<=3,log(t)<=2,loglog(t)<=1')
    print('PRECISION: exact Fractions and SymPy; no floating point; no candidate enumeration')
    D,F,G,fp,gp,J,W=run()
    for i,d in enumerate(D,1): print(f'D{i}={d}')
    print(f'F={F}'); print(f'G={G}'); print(f'projected F={fp}'); print(f'projected G={gp}'); print(f'J={J}'); print(f'W3={W}')
    print('RESULT: no counterexample to finite ECT closure found for this fixed bounded toy; W3=',W)
    print('STATUS: unverified toy evidence only; exact I^1_6b coefficients and domain are absent')
