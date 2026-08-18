#!/usr/bin/env python3
"""Exact minimal obstruction: ECT is not closed under passage summation."""
import sympy as sp
from naive_examples_oracle import naive_count
x=sp.symbols('x')
def W(fs): return sp.factor(sp.det(sp.Matrix([[sp.diff(f,x,j) for f in fs] for j in range(len(fs))])))
def run():
 print('RUN: exact four-passage ECT obstruction; exact Q; degree <=1')
 print('ORACLE: naive worked-example guard; no floating point')
 for cs,e in [([1,-1],1),([0],0),([1],0),([2,-3,1],2),([2,-5,4,-1],1)]: assert naive_count(cs)==e
 p=[1,x]; q=[-1,-x]; s=[p[i]+q[i] for i in range(2)]
 print('W(p)=',W(p),'W(q)=',W(q),'sum=',s,'W(sum)=',W(s))
 assert W(p)!=0 and W(q)!=0 and W(s)==0
 a=sp.symbols('a'); fam=[a,a*x]
 print('W(family)=',W(fam),'W(boundary)=',W([f.subs(a,0) for f in fam]))
 assert W(fam)==a**2 and W([f.subs(a,0) for f in fam])==0
 print('RESULT: REFUTED naive ECT closure; cancellation/rank loss')
 print('SCOPE: toy algebraic obstruction, not a dynamical I^1_6b counterexample')
if __name__=='__main__': run()
