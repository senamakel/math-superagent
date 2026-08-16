#!/usr/bin/env python3
"""Check whether the pass's clean E=0.555 is identifiable at fixed log-periodic
phase, and whether the residual is dominated by the log-periodic ~0.07 swing
rather than by a (log n)^B drift.

Question: is the source of the 'exponent' actually a bounded log2-periodic
oscillation around a mean slope, as the pass claimed (directive 46/47), and can
the data actually separate E=0.555 from sqrt*(log n)^B?  Uses only exact w*.
"""
import math, numpy as np

DATA = [
    (8,3),(10,3),(12,3),(14,4),(16,3),
    (32,5),(64,7),(128,11),(256,16),(512,24),(768,32),(1024,35),(1536,47),
    (2048,52),(3072,70),(4096,77),(5120,95),(6144,102),(8192,112),(10240,138),
    (12288,149),(16384,164),(20480,202),(24576,218),(32768,239),(40960,296),
    (49152,319),(65536,349),
]

lg2 = math.log2
def phase(n):
    # frac = n / 2^floor(log2 n)
    f = math.floor(lg2(n))
    return n / 2.0**f

# Residual of pure-power OLS at fixed phase, to see if it is bounded-periodic.
print("Fixed-phase residual of log2 w* against n^0.5568 (all points), grouped by phase-tolerance 0.25:")
X = np.array([[1.0, lg2(n)] for n,_ in DATA])
y = np.array([lg2(w) for _,w in DATA])
beta = np.linalg.lstsq(X,y,rcond=None)[0]
resid = y - X@beta
for ph in [1.0, 1.25, 1.5]:
    phs = [r for (n,_),r in zip(DATA,resid) if abs(phase(n)-ph)<0.03]
    ns  = [n for n,_ in DATA if abs(phase(n)-ph)<0.03]
    if len(phs)>=3:
        print(f"  phase {ph:.2f}: n={ns} resid range [{min(phs):.3f},{max(phs):.3f}] drift(max-min)={max(phs)-min(phs):.3f}")

# Now: does the residual show a monotone (log n)^B drift or bounded oscillation?
# Split tail n>=128, fit resid vs log2(log2 n).
sub = [(n,w) for n,w in DATA if n>=128]
X2 = np.array([[1.0, lg2(lg2(n))] for n,_ in sub])
y2 = np.array([lg2(w) for _,w in sub])
X1 = np.array([[1.0, lg2(n)] for n,_ in sub])
res2 = y2 - X1@np.linalg.lstsq(X1,y2,rcond=None)[0]
B = np.linalg.lstsq(X2,res2,rcond=None)[0][1]
rho = np.corrcoef(X2[:,1], res2)[0,1]
print(f"\nTail n>=128: corr(log2 log2 n, pure-power residual) = {rho:+.3f}")
print(f"  slope of residual on log2 log2 n = {B:+.4f}  (if strongly +, (log n)^B is real; if ~0, bounded-periodic)")

# Amplitudes
print("\nFull-period amplitude check: for phase-1.0 points, w*/n^0.5568: ")
for n,w in [(256,16),(512,24),(1024,35),(2048,52),(4096,77),(8192,112),(16384,164),(32768,239),(65536,349)]:
    print(f"   n={n}: w/n^0.5568 = {w/n**0.5568:.4f}")
