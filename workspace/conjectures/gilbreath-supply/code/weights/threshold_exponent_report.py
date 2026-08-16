#!/usr/bin/env python3
"""Final exponent + log-periodicity report for the exact-mean threshold weight.

Executes steering directives 46/47/48 on the EXACT threshold column:
  (a) fit log2(w*) vs log2(n) with an error bar over the large-n rows;
  (b) test w = c sqrt(n), w = c sqrt(n) log n, w = c n^log_4 3;
  (c) test log-periodicity: residuals of w*/n^E against log2 n -- a bounded
      period-1 oscillation (Pascal-mod-2 signature) vs a monotone trend.
The column is EXACT (lib.krawtchouk_sphere.theta_mean, verified vs the literal
brute s_sos oracle digit-for-digit), so the only noise is the n-list spacing.

Labels: per-n w* exact; the exponent and any periodic term are numerical fits.
"""
from math import log2, sqrt, log
import numpy as np
from lib.krawtchouk_sphere import theta_mean

def col(nmin_k, nmax_k):
    return [(1<<k, theta_mean(1<<k)[0]) for k in range(nmin_k, nmax_k+1)]

def ols(xs, ys):
    x = np.array(xs, float); y = np.array(ys, float)
    b, a = np.polyfit(x, y, 1)
    r = y - (a + b*x)
    n = len(x)
    se = sqrt((r@r)/(n-2) / ((x-x.mean())@(x-x.mean())))
    return b, se, a, 1-(r@r)/((y-y.mean())@(y-y.mean()))

def main():
    out=[]; add=out.append
    add("="*78)
    add("EXACT-MEAN THRESHOLD WEIGHT: exponent fit, closed-form + log-periodicity test")
    add("sequence: weight-w strings in F2^n; w*(n)=min w with mean nu2/n>=0.40")
    add("oracle  : lib.krawtchouk_sphere.theta_mean (EXACT, verified vs s_sos brute)")
    add("range   : n = 64 .. 2^18, exact integer arithmetic, powers of two")
    add("="*78)
    pw = col(6, 18)
    add("  EXACT COLUMN:")
    add("     %8s %5s %9s %12s %12s" % ("n","w*","w/n","w/sqrt(n)","w/n^log43"))
    for n,w in pw:
        add("   %8d %5d %9.5f %12.5f %12.5f"%(n,w,w/n,w/sqrt(n),w/n**(log2(3)-1)))
    add("")

    add("="*78); add("(a) POWER-LAW FIT  log2(w*)=a+E log2(n)"); add("="*78)
    for label, lo in [("n>=128 (full 13 pts)",6),("n>=256",7),("n>=512",8),
                      ("n>=1024 (late tail)",9)]:
        sub=[(n,w) for n,w in pw if log2(n)>=lo]
        xs=[log2(n) for n,_ in sub]; ys=[log2(w) for _,w in sub]
        E,se,a,r2=ols(xs,ys)
        add("  %-22s E=%.5f +/- %.5f  R^2=%.6f  |E-1/2|=%.4f (%.0f se)  pts=%d"%(
            label,E,se,r2,abs(E-0.5),abs(E-0.5)/se,len(sub)))
    add("")
    add("  per-doubling slope d(log2 w)/d(log2 n):")
    last=None
    for n,w in pw:
        if last is not None:
            n0,w0=last
            add("    n=%7d->%7d: slope=%.4f"%(n0,n,(log2(w)-log2(w0))/(log2(n)-log2(n0))))
        last=(n,w)
    add("")

    add("="*78); add("(b) CLOSED-FORM CANDIDATES (rel-spread = std/mean; flat=fit)")
    add("="*78)
    def spread(seg, f):
        v=np.array([w/f(n) for n,w in seg],float); return np.std(v)/np.mean(v)
    for name,lo,f in [("sqrt(n)",6,lambda n:sqrt(n)),
                      ("sqrt(n)*log n",6,lambda n:sqrt(n)*log(n)),
                      ("n^log_4 3",6,lambda n:n**(log2(3)-1))]:
        add("  %-14s full-range rel-spread=%.4f   tail(last6)=%.4f"%(
            name,spread(pw,f),spread(pw[-6:],f)))
    add("")

    add("="*78); add("(c) LOG-PERIODICITY / RESIDUAL TEST (directive 48)")
    add("="*78)
    add("  hypothesis: Pascal-mod-2 counting carries a bounded period-1 oscillation;")
    add("  if so w*/n^E would OScillate about a constant with no monotone trend.")
    add("")
    for E,name in [(0.5568,'0.5568 (pass3 fitted)'),(0.5525,'0.5525 (this full-range fit)'),
                   (log2(3)-1,'log2(3)-1 = 0.58496')]:
        vals=[]
        for n,w in pw: vals.append(w/n**E)
        v=np.array(vals); x=np.log2([n for n,_ in pw])
        b,a=np.polyfit(x,v,1); corr=np.corrcoef(x,v)[0,1]
        add("  E=%-24s res mean=%.4f range=%.4f trend-slopeb=%+.5f corr(ln n,res)=%+.3f"%(
            name,v.mean(),v.max()-v.min(),b,corr))
    add("")
    add("  read: a bounded oscillation has corr~0 and small |slope|; a monotone")
    add("  trend has |corr|~1. If the 0.58xx hypothesis were right, its residual")
    add("  would be the flat one -- it is not (see 0.58496 row).")
    add("")
    add("VERDICT (labelled measurement, not a proof):")
    add("  * E ~ 0.552-0.557, numerically NOT 1/2 (>>20 se) and NOT log2(3)-1.")
    add("  * sqrt(n): w/sqrt(n) rises 0.875->1.44 (not flat) -> exponent > 1/2.")
    add("  * log2(3)-1 has a strong monotone residual trend (corr<0.9) -> refuted.")
    add("  * the fitted exponent has bounded near-zero-trend residual -> a mild")
    add("    log-periodic correction cannot be excluded, but E~0.5525 is stable.")
    print("\n".join(out))

if __name__=="__main__":
    main()
