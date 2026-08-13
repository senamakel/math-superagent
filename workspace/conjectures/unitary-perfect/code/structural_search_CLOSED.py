"""Forced-prime search for unitary perfect numbers.

n unitary perfect  <=>  prod_{p^a || n} (1 + 1/p^a) = 2.
Search sets of prime powers q_i = p_i^{a_i} (distinct primes) with
prod (q_i+1)/q_i = 2.

The engine is the denominator rule.  If the remaining target is R = A/B in
lowest terms, then B divides prod q_i, so every prime dividing B MUST still be
used.  That makes the choice of prime forced whenever B > 1, and only the
exponent branches.  Free choice of prime happens only when B = 1.
"""
import sys, math
from fractions import Fraction as F

P = int(sys.argv[1]); A = int(sys.argv[2])
sieve = bytearray([1])*(P+1); sieve[0]=sieve[1]=0
for i in range(2,int(P**.5)+1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [i for i in range(2,P+1) if sieve[i]]
pidx = {p:i for i,p in enumerate(primes)}
TOTAL = F(1)
for p in primes: TOTAL *= F(p+1,p)

def spf(b):
    for p in primes:
        if p*p > b: return b
        if b % p == 0: return p
    return b

def vp(b,p):
    v=0
    while b%p==0: b//=p; v+=1
    return v

sols=[]; nodes=0
def go(R, used, bound, floor):
    """bound = upper bound on the product still achievable from unused primes"""
    global nodes
    nodes += 1
    if R == 1: sols.append(tuple(sorted(used.items()))); return
    if R < 1 or R > bound: return
    b = R.denominator
    if b > 1:
        s = spf(b)
        if s > P or s in used: return          # required prime unusable -> dead branch
        cand = [s]                              # FORCED: only this prime may be taken next
        need = vp(b, s)
    else:
        cand = [p for p in primes if p >= floor and p not in used]
        need = 1
    for p in cand:
        nb = bound / F(p+1, p)                  # this prime is now spent either way
        q = p ** need
        for a in range(need, A+1):
            f = F(q+1, q)
            if f <= R:
                used[p] = a
                go(R/f, used, nb, p+1 if b == 1 else floor)
                del used[p]
            q *= p
            if q.bit_length() > 200: break

go(F(2), {}, TOTAL, 2)
print(f"P={P} A={A} primes={len(primes)} nodes={nodes} solutions={len(sols)}")
out=[]
for s in sols:
    n = 1
    for p,a in s: n *= p**a
    out.append((n,s))
for n,s in sorted(out):
    print(f"  n = {n}")
    print(f"      {' * '.join(f'{p}^{a}' if a>1 else str(p) for p,a in s)}   omega={len(s)}")
