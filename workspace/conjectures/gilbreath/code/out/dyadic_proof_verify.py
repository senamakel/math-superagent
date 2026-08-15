#!/usr/bin/env python3
"""Verification for the dyadic-collapse dichotomy proof (Directives 57-60).

Checks the two structural reformulations of the fold, then both legs:
  - Leg (1): h periodic minimal period 2^k  =>  Y_c = 0 for all c >= 2^k,
    hence nu2(n) <= 2^k - 1 (bounded in n).
  - Leg (2): h periodic minimal period with an odd factor > 1  =>  nu2(n) ~ c*n
    with c > 0 (positive linear).  Best-argument half: report measured slope.

Fold definitions (must agree):
  (A) direct:    Y_c = XOR_{i: (i & c)==i} h[T - c + i]   (reversed-input form)
  (B) zeta form: set g_j = h[T-j];  Y_c = XOR_{j: (j & c)==j} g_j
Both are the Pascal/Lucas fold: C(c,i) is odd iff i is a submask of c.
"""
import itertools, functools

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

def zeta(g, c):
    return functools.reduce(lambda a,b:a^b,(g[j] for j in submasks(c)),0)

def build_periodic(word, m):
    L=len(word); return [int(word[i % L]) for i in range(m)]

def y_seq_direct(h, T):
    """Y_c for c = 1..T using direct form XOR_{i submask of c} h[T-c+i]."""
    return [functools.reduce(lambda a,b:a^b,(h[T-c+i] for i in submasks(c)),0)
            for c in range(1, T+1)]

def y_seq_zeta(h, T):
    """Y_c for c = 1..T using zeta form with g_j = h[T-j]."""
    g=[h[T-j] for j in range(T+1)]
    return [zeta(g,c) for c in range(1,T+1)]

def minimal_period(word):
    L=len(word)
    for p in range(1,L+1):
        if L % p==0 and all(word[i]==word[i%p] for i in range(L)):
            return p
    return L

def odd_part(P):
    while P % 2 ==0: P//=2
    return P

# ---- 0. The two formulations agree ----
agree=True
for m in [30, 100, 377]:
    for word in [[0,0,1],[1,0],[0,0,0,1],[0,0,1,0,1],[0]*4+[1],[0,0,0,0,0,0,1]]:
        h=build_periodic(word,m); T=m-1
        a=y_seq_direct(h,T); b=y_seq_zeta(h,T)
        if a!=b: agree=False; print("MISMATCH", word, m, a, b)
print("1) direct vs zeta form agree:", agree)

# ---- Leg (1): minimal period 2^k  =>  Y_c = 0 for c >= 2^k  ----
print("\nLeg(1): minimal period 2^k => Y_c=0 for all c >= 2^k")
for k in range(1,5):
    L=2**k
    allok=True
    # try representative words (constant + tail1 + generic); exhaustive for k<=3
    words=[]
    if k<=3:
        words=list(itertools.product([0,1],repeat=L))
    else:
        words=[[0]*(L-1)+[1], [0]*L, [1]*L,
               [i%2 for i in range(L)], [i%3==0 for i in range(L)]]
    for bits in words:
        # ensure minimal period is exactly L: for exhaustive k=1..3 filter
        if minimal_period(list(bits)) != L: continue
        for m in [L+5, 400, 1000]:
            h=build_periodic(list(bits),m); T=m-1
            for c in range(L, T+1):
                if zeta([h[T-j] for j in range(T+1)], c)==1:
                    allok=False
                    print("  VIOLATION k=",k,"word=",bits,"m=",m,"c=",c)
    print(f"  k={k} period {L}: all Y_c=0 for c>=2^{k} across words&m:", allok)

# ---- Leg (1) bounded nu2: max nu2(m) over m for a period-2^k word ----
print("\nLeg(1) bounded nu2: max weight over m in a range, per period-2^k word")
for k in range(1,5):
    L=2**k
    word=[0]*(L-1)+[1]
    maxw=0
    for m in range(L, 1000):
        h=build_periodic(word,m); T=m-1
        w=sum(y_seq_zeta(h,T))
        maxw=max(maxw,w)
    print(f"  k={k}: max nu2(m) over m<1000 = {maxw}  (bound claimed: <= {L-1})")

# ---- Leg (2): odd factor in minimal period => positive linear growth ----
print("\nLeg(2): odd factor => nu2(m) ~ c*m, estimate slope c")
for P in [1,2,3,4,5,6,7,8,9,10,12,14,15]:
    word=[0]*(P-1)+[1]           # tail-1 word
    mp=minimal_period(word)
    mm=[200,500,1000,2000,4000]
    vals=[]
    for m in mm:
        h=build_periodic(word,m); T=m-1
        vals.append(sum(y_seq_zeta(h,T)))
    # slope using largest two points
    c_last=(vals[-1]-vals[-2])/(mm[-1]-mm[-2])
    op=odd_part(mp)
    print(f"  P={P:2d} minperiod={mp:2d} oddpart={op:2d} nu2={vals}  last-slope={c_last:+.4f}")
