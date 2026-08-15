#!/usr/bin/env python3
"""Explore leg (2): for g periodic with minimal period P (odd factor > 1),
is the zeta output Y_c = XOR_{j subset c} g_j eventually periodic?  What
period and what density of 1's?  This decides how much of 'nu2 ~ c*n' is
provable versus conjectured.
Also: the parity N_p(c) = |{j subset c : j == p mod P}| mod 2, the building
block (Y_c = XOR_p g_p * N_p(c)).
"""
import functools

def fast_zeta(seq, T):
    z=seq[:]
    nb=T.bit_length()
    for b in range(nb):
        bit=1<<b
        for mask in range(T+1):
            if mask & bit:
                z[mask]^=z[mask^bit]
    return z

def build_periodic(word, T):
    L=len(word)
    return [int(word[i%L]) for i in range(T+1)]

def minimal_period(word):
    L=len(word)
    for p in range(1,L+1):
        if L%p==0 and all(word[i]==word[i%p] for i in range(L)):
            return p
    return L

def find_period(seq, start, look):
    """minimal p with seq[i]==seq[i+p] for i in [start, start+look)."""
    for p in range(1, look//2+1):
        ok=True
        for i in range(start, start+look-p):
            if seq[i]!=seq[i+p]: ok=False; break
        if ok: return p
    return None

print("Is Y eventually periodic for odd-period words?")
for word in [[0,0,1],[0,0,0,0,1],[0]*6+[1],[0]*14+[1]]:
    P=minimal_period(word)
    T=6000; g=build_periodic(word,T)
    Y=fast_zeta(g,T)
    # candidate periods: try the word period and its multiples, and powers*P
    cands=[P,2*P,3*P,4*P,6*P,8*P]
    found=None
    for c in cands:
        if c<=0: continue
        start=800; look=2000
        ok=True
        for i in range(start, start+look-c):
            if Y[i]!=Y[i+c]: ok=False; break
        if ok and look-c>c: found=c; break
    # density over a clean window
    a,b=3000,6000
    dens=sum(Y[a:b])/(b-a)
    print(f"  P={P} word={word}: Y eventually periodic? period={found}  density(1s) in [{a},{b}]={dens:.4f}")

print("\nParity N_p(c)=|{j<=c: j==p mod P}| mod 2: eventually periodic in c?")
for P in [3,5,6,7]:
    T=4000
    for p in range(P):
        cnt=[0]*(T+1)
        for c in range(T+1):
            s=0
            for j in range(c+1):
                if (j & c)==j and j%P==p: s^=1
            cnt[c]=s
        # check eventual period in c: N_p(c) vs N_p(c+P)
        run=1200; bad=0
        for c in range(run, T-P):
            if cnt[c]!=cnt[c+P]: bad+=1
        print(f"  P={P} p={p}: mismatches vs period-P on [{run},{T}]={bad}")
