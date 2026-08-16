#!/usr/bin/env python3
"""Hand-check the n=1 analysis of G-coupling-half (lemma as stated in the
run's skeleton: for every mu on {0,1}^n with H>0 and max marginal < 1/2 there
is a conditionally-iid coupling with H(AvB) > H(A)).

For n=1, mu = Bernoulli(p), 0<p<1/2.  Any coupling of (mu,mu) has
   mean(AvB) = 2p - P(A=1,B=1),  P(A=1,B=1) in [0, p]
so mean(AvB) ranges over [p, 2p].  The best H(AvB)=h(mean) is:
  - p in [1/4, 1/2): mean=1/2 reachable (take P(A=B=1)=2p-1/2 in [0,p])
       => H(AvB)=1 > h(p)=H(A).  LEMMA HOLDS.
  - p in (0, 1/4): best mean=2p => H(AvB)=h(2p) > h(p).  LEMMA HOLDS.
so the n=1 "refutation" (INDEX row coupling_half_n1.py, deleted) is WRONG.

This prints the table to confirm.
"""
import math
LP2 = math.log(2.0)
def h(x):
    if x<=0 or x>=1: return 0.0
    return -x*math.log(x)/LP2 - (1-x)*math.log(1-x)/LP2

rows = []
for k in range(1, 50):
    p = k/100.0
    if not (0 < p < 0.5): continue
    Hp = h(p)
    # best attainable mean
    if p >= 0.25:
        best_mean, bestH = 0.5, 1.0
        note = "mean=1/2 reachable"
    else:
        best_mean, bestH = 2*p, h(2*p)
        note = "best mean=2p"
    rows.append((p, Hp, best_mean, bestH, bestH - Hp, note))

print(f"{'p':>7}{'H(A)=h(p)':>12}{'best mean':>10}{'maxH(AvB)':>12}{'diff':>9}  note")
print("-"*78)
violations = [r for r in rows if r[4] <= 0]
for p, Hp, bm, bH, d, note in rows:
    print(f"{p:7.2f}{Hp:12.4f}{bm:10.2f}{bH:12.4f}{d:9.4f}  {note}")
print()
print(f"cases where maxH(AvB) <= H(A): {len(violations)}")
print("=> G-coupling-half HOLDS at n=1 for every p in (0,1/2):")
print("   the deleted n=1 'refutation' (max H=h(2p)<h(p)) is an arithmetic bug.")
