#!/usr/bin/env python3
"""Independent verification of the n=1 refutation of G-coupling-half.

Lemma (G-coupling-half, as stated in the run's skeleton): For EVERY
distribution mu on {0,1}^n with H(mu)>0 and max_i Pr[A_i=1] < 1/2, there is a
conditionally-iid coupling (A,B) of (mu,mu) with H(A v B) > H(A).

Counterexample candidate (n=1): mu = Bernoulli(p), p in (1/3, 1/2).

For n=1, A and B are each Bernoulli(p).  For ANY coupling (the superset of the
conditionally-iid class, so if this fails the restricted class fails too):
    P(AvB=1) = P(A=1)+P(B=1) - P(A^B=1) = 2p - P(A^B) <= 2p.
So the mean of the Bernoulli A v B is at most 2p, hence H(AvB) <= h(2p).
Since h is concave symmetric, and for p in (1/3,1/2) we have 2p in (2/3,1),
h(2p) < h(p) = H(A).  So H(AvB) < H(A) for every coupling.  Refuted.

This program prints the table for several p to check the inequality h(2p)<h(p)
and confirms max H(A v B) = h(2p) is attained (via the disjoint coupling).
"""
import math
LP2 = math.log(2.0)
def h(x):
    if x<=0 or x>=1: return 0.0
    return -x*math.log(x)/LP2 - (1-x)*math.log(1-x)/LP2

print(f"{'p':>8}{'H(A)=h(p)':>14}{'max H(AvB)=h(2p)':>20}{'diff h(2p)-h(p)':>18}")
print("="*64)
worst=None
for k in range(10, 49):
    p = k/100.0
    if not (1/3 < p < 1/2):
        continue
    Hp = h(p)
    H2p = h(2*p)
    diff = H2p - Hp
    if worst is None or diff < worst:
        worst = diff
        worst_p = p
    print(f"{p:8.2f}{Hp:14.6f}{H2p:20.6f}{diff:18.6f}")

print()
print(f"Worst (most negative) H(AvB)-H(A) at p={worst_p:.2f}: {worst:.6f} < 0")
print("=> there exists mu (Bernoulli p, p in (1/3,1/2)) with H(mu)>0, marginal")
print("   p<1/2, but EVERY coupling (hence every conditionally-iid coupling)")
print("   has H(AvB) < H(A).  The lemma G-coupling-half is FALSE as stated.")
