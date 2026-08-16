import math
from fractions import Fraction

# ---- Candidate 3: are n=0,2,8 convergent denominators of log_3(2)? ----
alpha = math.log(2)/math.log(3)
print("log_3 2 ~", alpha)

def convergents_cf(x, nterms=30):
    # returns list of (p,q) convergents
    convs = []
    a = []
    xcur = x
    # first entry a0 = integer part (0 here)
    for i in range(nterms):
        ai = int(math.floor(xcur))
        a.append(ai)
        # build convergent from partial quotients
        # p/q recurrence
        p_prev2, q_prev2 = 1, 0
        p_prev1, q_prev1 = ai, 1
        for aj in a[1:]:
            p_prev2, p_prev1 = p_prev1, aj*p_prev1 + p_prev2
            q_prev2, q_prev1 = q_prev1, aj*q_prev1 + q_prev2
        convs.append((p_prev1, q_prev1))
        frac = xcur - ai
        if frac == 0:
            break
        xcur = 1.0/frac
    return convs, a

convs, palph = convergents_cf(alpha)
print("partial quotients:", palph[:20])
qs = [q for (p,q) in convs]
print("convergent denominators q:", qs[:20])
for n in (0,2,8):
    print(f"n={n}: is a convergent denominator? {n in qs}")

# middle block check claim: for which n<=large is middle block digit-2-free?
def digits3(m):
    ds=[]
    while m:
        ds.append(m%3); m//=3
    return ds

def mid_block_free(n, lo, hi):
    m=2**n
    ds=digits3(m)
    L=len(ds)
    a=int(lo*L); b=int(hi*L)
    for j in range(max(0,a), min(L,b)):
        if ds[j]==2: return (False, ds)
    return True, ds

for n in (0,1,2,3,8,9,10,20,50,100):
    ok,ds = mid_block_free(n,0.3,0.5)
    print(f"n={n:>4} len={len(ds)} mid[0.3,0.5) free={ok}")

# ---- Candidate 2: run identity & LTE for n=8 ----
# 2^8 = 256 = 100111_3 -> runs of 1s
n=8
ds=digits3(2**n)
print("\n2^8 digits (LSB first):", ds)
# find runs of 1s: (start offset s, length r)
runs=[]
i=0
while i < len(ds):
    if ds[i]==1:
        j=i
        while j<len(ds) and ds[j]==1: j+=1
        runs.append((i, j-i)); i=j
    else:
        i+=1
print("runs (s,r):", runs)
total=sum(3**s*(3**r-1)//2 for (s,r) in runs)
print("sum of run contributions =", total, "expect 2^8 =", 2**8)
tot2=sum((3**(s+r)-3**s) for (s,r) in runs)
print("2*(sum contribution)=2^(n+1)?", tot2, 2**9)

def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
for r in range(1,15):
    lte = 1 if r%2==1 else 2+v2(r)
    direct = v2(3**r-1)
    assert lte==direct, (r,lte,direct)
print("LTE v_2(3^r-1) agrees with direct for r=1..14")

# ---- Candidate 1: nondegeneracy ----
# For digit-2-free 2^n = sum_{a in A}3^a, equation 2^n - sum 3^a = 0 nondegenerate
# terms {2^n, -3^{a1},...,-3^{ak}}. check: no proper subsum vanishes
def digit_free(m):
    return all(d in (0,1) for d in digits3(m))
def nondeg(n):
    m=2**n
    if not digit_free(m): return None
    A=[i for i,d in enumerate(digits3(m)) if d==1]
    terms=[2**n]+[-3**a for a in A]
    from itertools import combinations
    for r in range(1,len(terms)):
        for sub in combinations(terms,r):
            if sum(sub)==0:
                return False,(terms,sub)
    return True,A
for n in (0,2,8,12):
    r=nondeg(n)
    print(f"n={n}: digit-free? {'yes' if r else 'no'}  nondeg result: {r[0] if isinstance(r,tuple) else r}")
