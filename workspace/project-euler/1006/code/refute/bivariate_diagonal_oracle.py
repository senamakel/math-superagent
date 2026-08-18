"""Small oracle attacking fixed-degree bivariate diagonal closure.
complexity_class: exponential; oracle_bound: n <= 12.

A degree-d closure whose state is only (count, sum, sumsq) would assign the
same concatenation correction to words with the same three summaries. We find
the smallest collision where appending the same one-letter right block gives
different corrections, exposing the missing diagonal/boundary coordinate.
"""
from collections import defaultdict

def vals(w,k):
    return [int(w[i:i+k],2) for i in range(len(w)-k+1)]
def summary(w,k):
    v=vals(w,k)
    return (len(v),sum(v),sum(x*x for x in v))
def cross(w,k):
    return sum(x*x for x in vals(w,k))
def search(N=12):
    for k in range(1,N+1):
      for n in range(k,N+1):
        buckets=defaultdict(list)
        for x in range(1<<n):
          w=format(x,f'0{n}b'); buckets[summary(w,k)].append(w)
        for s, ws in buckets.items():
          for a in ws:
            for b in ws:
              if a>=b: continue
              aa,bb=a+'0',b+'0'
              if cross(aa,k)!=cross(bb,k):
                return k,n,s,a,b,summary(aa,k),summary(bb,k)
    return None
if __name__=='__main__':
    print(search())
