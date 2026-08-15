"""Gate check for hilbert-projective-metric-birkhoff-contraction.

The candidate's Birkhoff companion is supposed to be order-preserving
(homogeneous) so Birkhoff's theorem can contract it in the Hilbert projective
metric.  Test order-preservation of:
  (i)  the literal halved cell map   h_i -> |h_i - h_{i+1}|   (non-order-pred)
  (ii) the excess operator  E(t)_i = max(0, |t_i - t_{i+1}| - 1)
  (iii) the max of a halved row  M(h) = max_i h_i  (order-preserving, but does
       not move the block boundary / second entry: it only stays put).
Also test the candidate's own falsifier gate: is E order-preserving on the
nonnegative cone?  Exact integers, small length.
"""
from itertools import product

def literal_map(h):
    return [abs(h[i]-h[i+1]) for i in range(len(h)-1)]

def excess_map(h):
    return [max(0, abs(h[i]-h[i+1])-1) for i in range(len(h)-1)]

def ord_pred(coords, mapfn, name):
    """Return (is_order_preserving, witness_pair) over length-n coordinatewise."""
    n = len(coords)
    best = None
    for a in product(range(coords), repeat=n):
        for b in product(range(coords), repeat=n):
            if all(x<=y for x,y in zip(a,b)):
                fa = mapfn(a); fb = mapfn(b)
                if not all(x<=y for x,y in zip(fa,fb)):
                    return False, (a,b,fa,fb)
    return True, None

# witness cited by candidate: |a-4| for a in 0,2,4,6,8
print("literal |a-4| at a=0,2,4,6,8:", [abs(a-4) for a in (0,2,4,6,8)])
print("  -> non-monotone (falls then rises):",
      [abs(a-4) for a in (0,2,4,6,8)] == sorted(abs(a-4) for a in (0,2,4,6,8)))

for n,tag in [(3,"len3"),(4,"len4")]:
    ok,w = ord_pred(5, literal_map, "literal")
    print(f"literal map order-preserving on {tag} over {{0..4}}: {ok}", w if w else "")
for n,tag in [(3,"len3"),(4,"len4")]:
    ok,w = ord_pred(5, excess_map, "E")
    print(f"excess E order-preserving on {tag} over {{0..4}}: {ok}", w if w else "")

# explicit candidate witness for E
t  = (0,4)
tp = (2,4)
Et  = excess_map(t);  Etp = excess_map(tp)
print("E(0,4)=",Et," E(2,4)=",Etp,"  t<=t' but E(t)<=E(t')?", Et[0]<=Etp[0])
