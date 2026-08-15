#!/usr/bin/env python3
"""Structural checks on the three candidate reformulations.

(1) level-set: is the cell rule A' = |a-b| monotone in its arguments?  A
    percolation/contact-process comparison needs a monotone rule; if raising a
    parent can LOWER the child, no monotone coupling to subcritical oriented
    percolation exists.
(3) Christoffel/cycle-lemma: is the halved prime-gap word w balanced
    (Sturmian-like, factor complexity ~ n+1) or does it have near-maximal
    complexity (not balanced)?
"""
from lib.gilbreath import primes_up_to, diff_block

def primes_gaps(p):
    return [p[i+1]-p[i] for i in range(len(p)-1)]

def halved_gap_word(p):
    # A_1 gaps are all even (2 is only even prime => p>=3 gaps between odds, even).
    # halved word h_n = (p_{n+2}-p_{n+1})/2
    gaps = primes_gaps(p)[1:]  # skip gap 3-2=1
    return [g//2 for g in gaps]

def balance_check(w, Lmax=8):
    """A word (over any alphabet) is balanced if for every length L, the
    counts of each symbol in any two length-L factors differ by <= 1.
    Returns list of max imbalance per length, and whether alphabet is small.
    """
    from collections import Counter
    res = {}
    for L in range(1, Lmax+1):
        counts = []
        for i in range(len(w)-L+1):
            counts.append(Counter(w[i:i+L]))
        # max imbalance per symbol
        n = len(w)
        maximb = 0
        for s in set(w[:2000]):
            vals = [c.get(s,0) for c in counts]
            maximb = max(maximb, max(vals)-min(vals))
        res[L] = maximb
    return res

def factor_complexity(w, Lmax=10):
    """Number of distinct factors of each length (Sturmian ~ L+1)."""
    res = {}
    for L in range(1, Lmax+1):
        res[L] = len(set(w[i:i+L] for i in range(len(w)-L+1)))
    return res

# ---------- (1) monotonicity ----------
print("== (1) level-set monotonicity ==")
# |a-b| as function of a, holding b:  a=4,b=4 ->0 ; a=4,b=0->4 ; a=8,b=4->4 ; a=0,b=4->4
# demonstrate non-monotone in first argument with second fixed:
for b in (4,):
    prev=None; seq=[]
    for a in (0,2,4,6,8,10):
        v=abs(a-b); seq.append((a,v))
    print(f"b={b}: (a,|a-b|) = {seq}  -> not monotone in a")
# two parents both large can give small child
print("  (100,100)->", abs(100-100), " both in S_4 but child not; rule not monotone")

# ---------- (3) gap word complexity ----------
print("\n== (3) halved prime-gap word balance/complexity ==")
P = primes_up_to(20000)   # ~2500 primes
w = halved_gap_word(P)
print("n primes:", len(P), "halved gaps:", len(w))
print("sample w[:30]:", w[:30])
print("factor complexity p(n) [Sturmian would be n+1]:")
fc = factor_complexity(w, 10)
for L,c in fc.items():
    print(f"  L={L}: {c}")
print("balance max-imbalance per length [balanced needs <=1]:")
bal = balance_check(w, 8)
for L,m in bal.items():
    print(f"  L={L}: max imbalance={m}")
from collections import Counter
print("alphabet (=unique gap values/2):", len(set(w)), "; Sturmian/Christoffel words are BINARY (2-letter)")
print("so `w` is not even over a 2-letter alphabet -> cannot be balanced/Christoffel/Sturmian")

# running differences of w (what the cycle lemma would control): bounded? 
import itertools
print("\nmax halved gap in window:", max(w), " (cycle lemma needs bounded increments / fixed sum)")
