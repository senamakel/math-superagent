"""Verify the NO4 growth law against the now-8-term sequence.

Prior run (7 terms) conjectured tail ratio a_n/a_{n-1} ~ 3(n-10),
and predicted NO4(17) in ~33-38M. NO4(17)=34,758,006 has now been computed.
Check: (a) does the new term land in the predicted range; (b) does the
consecutive ratio continue to match 3(n-10)?
"""
NO4 = {10:5, 11:9, 12:57, 13:503, 14:6059, 15:91433, 16:1655659, 17:34758006}
n_sorted = sorted(NO4)
print("n   a_n          ratio a_n/a_{n-1}   3(n-10)   ratio/3(n-10)")
for i in range(1, len(n_sorted)):
    n = n_sorted[i]
    na = n_sorted[i-1]
    r = NO4[n] / NO4[na]
    guess = 3*(n-10)
    print(f"{n:2d} {NO4[n]:>10d}   {r:10.4f}        {guess:3d}      {r/guess:.4f}")

# least-squares slope c in ratio = c*(n-10), using tail n=12..17
import numpy as np
for lo in [12, 13, 14]:
    ns = [n for n in n_sorted if n >= lo]
    X = np.array([[ (n-10) ] for n in ns], dtype=float)
    y = np.array([NO4[n]/NO4[ns[i-1]] for i,n in enumerate(ns) if i>0], dtype=float)
    # align: ratio at n is y[i], for n = ns[i]
    xs = np.array([ (ns[i]-10) for i in range(1,len(ns))], dtype=float)
    ys = np.array([NO4[ns[i]]/NO4[ns[i-1]] for i in range(1,len(ns))], dtype=float)
    c = np.sum(xs*ys)/np.sum(xs*xs)
    print(f"tail from n={lo}: least-squares c = {c:.4f}  resid={np.sum((ys-c*xs)**2):.3f}")

# does NO4(17) land in predicted 33-38M range?
print("NO4(17) =", NO4[17], "in [33e6,38e6]?", 33e6 <= NO4[17] <= 38e6)
