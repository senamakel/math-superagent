"""Small-case checks of G-coupling-half (n=1, n=2), exact where possible.

Claim (G-coupling-half): for every mu on {0,1}^n with H(mu)>0 and
max_i Pr[A_i=1] < 1/2, there is a conditionally-iid coupling (A,B) of (mu,mu)
with H(A∨B) > H(mu).

We check whether ANY coupling (a strict superset of conditionally-iid) can
achieve H(A∨B) > H(mu).  If none can, the claim is refuted.  If some can, the
claim is NOT refuted by this mu (it may still fail in the conditionally-iid
subclass, which we note but can't compute here).

n=1 exact: mu=Bernoulli(p), q=Pr[A∨B=1] ranges over [p, 2p] over all couplings.
  H(A∨B)=h(q), H(mu)=h(p).  h is unimodal at 1/2, increasing on [0,1/2].
  h(q)>h(p) iff q in (p, 1-p).  The interval [p,2p] hits (p,1-p) iff
  min(2p, 1-p) > p.  Since p in (0,1/2): 2p>p and 1-p>p, so min>p.  Hence
  EVERY p in (0,1/2) admits q with h(q)>h(p).  n=1 passes (not refuted).
"""
import math


def h(t):
    return 0.0 if t in (0.0, 1.0) else -t * math.log2(t) - (1 - t) * math.log2(1 - t)


print("=== n=1: q ranges over [p,2p] over all couplings ===")
print(f"{'p':>6}{'q(p,1-p)hit?':>14}{'h(p)':>8}{'h(q)max':>9}{'beats?':>8}")
for p in [0.1, 0.25, 0.3, 0.4, 0.45, 0.49]:
    hit = min(2 * p, 1 - p) > p
    q = (p + min(2 * p, 1 - p)) / 2
    print(f"{p:6.3f}{str(hit):>14}{h(p):8.4f}{h(q):9.4f}{str(h(q) > h(p)):>8}")

print("\n=== n=2 candidate: mu uniform on {00,01,10} (masks 0,1,2) ===")
print("family {empty,{2},{1}}: marginals 1/3 each, H(mu)=log2(3)=%.4f" % math.log2(3))
print("All-couplings analysis (existence of any coupling beating H(mu)):")
print("  Any coupling: OR support {00,01,10,11}; the iid coupling gives")
# iid: q(00)=1/9, q(01)=1/3, q(10)=1/3, q(11)=2/9
orp = [1/9, 1/3, 1/3, 2/9]
print("  OR(iid) =", dict(zip(['00','01','10','11'], [round(x,4) for x in orp])),
      "  H(OR)=", round(h(1/9)+h(1/3)+h(1/3)+h(2/9), 4)
      if False else round(-sum(x*math.log2(x) for x in orp if x>0), 4))
print("  H(OR) > H(mu)=1.585? ->", -sum(x*math.log2(x) for x in orp if x>0) > math.log2(3))
