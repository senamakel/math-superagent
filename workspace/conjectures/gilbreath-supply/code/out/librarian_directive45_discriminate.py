# Directive 45 exponent discrimination on the threshold WEIGHT column.
# The operator's theta*n weights 7,11,16,24,35,52,77,112,164,239 for n=64..32768.
# Tests: w/sqrt(n) flatness (exponent 1/2), sqrt*log, n^log_4(3), and the fitted
# power, each with an error bar over the large-n rows. Measured-not-proved: the
# base data is exact per n (verified threshold formula); the exponent is a fit.

import numpy as np

ns  = np.array([64,128,256,512,1024,2048,4096,8192,16384,32768], float)
w   = np.array([7,11,16,24,35,52,77,112,164,239], float)

def report(name, col, tail_start=0):
    print(f"\n=== {name} ===")
    full = col / col[0]
    for i,n in enumerate(ns):
        print(f"  n={int(n):7d}  {name}={col[i]:9.4f}   ({name}[n]/{name}[n0]={full[i]:7.4f})")
    # flatness: relative spread over the whole listed range and over the last half
    spread = (col[tail_start:].max()-col[tail_start:].min())/col[tail_start:].mean()
    print(f"  relative spread (n>=ns[{tail_start}]={ns[tail_start]:.0f}): {spread:.4f}")

print("Per-doubling slope of log2(w) vs log2(n):")
d = np.log2(w[1:]) - np.log2(w[:-1])   # each is one doubling of n
for i in range(len(d)):
    print(f"  {int(ns[i]):7d}->{int(ns[i+1]):7d}:  slope={d[i]:.4f}")
print(f"  last four doublings mean slope: {d[-4:].mean():.4f}")
print(f"  last four doublings slopes: {np.round(d[-4:],3)}")

wt_sqrt   = w / np.sqrt(ns)                 # hypothesis w = c sqrt(n)
wt_sqrtln = w / (np.sqrt(ns)*np.log(ns))    # hypothesis w = c sqrt(n) log n
wt_lg43   = w / np.power(ns, np.log(3)/np.log(4))   # w = c n^log_4(3)
wt_n55    = w / np.power(ns, 0.55)

report("w/sqrt(n)", wt_sqrt, tail_start=4)
report("w/(sqrt(n) ln n)", wt_sqrtln, tail_start=4)
report("w/n^log_4(3)", wt_lg43, tail_start=4)
report("w/n^0.55", wt_n55, tail_start=4)

# OLS fit of exponent with standard error, over several tails
print("\nOLS log2 w = a + E log2 n :")
for sl in range(len(ns)-1):
    idx = range(sl, len(ns))
    x = np.log2(ns[idx]); y = np.log2(w[idx])
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A@coef; n = len(idx); dof = n-2
    s2 = resid@resid/dof
    cov = s2*np.linalg.inv(A.T@A)
    se = np.sqrt(np.diag(cov))
    print(f"  n>=ns[{sl}]={int(ns[sl]):6d}:  E={coef[0]:.4f} +- {se[0]:.4f}   resid_std={resid.std():.4f}")

# Is 1/2 rejected? t-stat of E vs 0.5 on the last-four-doublings tail (n>=2048)
idx = range(6, len(ns))
x = np.log2(ns[idx]); y = np.log2(w[idx])
A = np.vstack([x, np.ones_like(x)]).T
coef, *_ = np.linalg.lstsq(A, y, rcond=None)
resid = y - A@coef; dof = len(idx)-2
s2 = resid@resid/dof; cov = s2*np.linalg.inv(A.T@A); se = np.sqrt(np.diag(cov))
t_half = (coef[0]-0.5)/se[0]
print(f"\nn>=2048 tail: E={coef[0]:.4f}+-{se[0]:.4f};  t-stat vs 1/2 = {t_half:.2f}")
print("  (a |t|<2 means 1/2 is NOT rejected within 2 sigma on this tail)")
