"""Bounded oracle: counterexample to summary closure.
complexity_class: exponential; oracle_bound: max_len <= 15.
"""
from collections import defaultdict
from lib.fibword import fib_prefix

def summary(w,k):
    v=[int(w[i:i+k]) for i in range(len(w)-k+1)]
    return len(v),sum(v),sum(x*x for x in v)

def first_collision(max_len=15,kmax=12):
    for k in range(1,kmax+1):
      for n in range(k,max_len+1):
        d=defaultdict(list)
        for mask in range(1<<n):
          w=''.join('1' if mask>>i&1 else '0' for i in range(n))
          d[summary(w,k)].append(w)
        for s,ws in d.items():
          for a in ws:
            for b in ws:
              if a!=b and summary(a+'0',k)!=summary(b+'0',k):
                return k,n,s,a,b,summary(a+'0',k),summary(b+'0',k)

def fib_boundary_examples():
 for k in range(1,8):
  w=fib_prefix(40); a,b=w[:20],w[20:]
  whole=summary(a+b,k); add=tuple(x+y for x,y in zip(summary(a,k),summary(b,k)))
  print(k,whole,add,whole!=add)

if __name__=='__main__':
 print('smallest local summary collision:',first_collision())
 print('Fibonacci boundary checks:')
 fib_boundary_examples()
