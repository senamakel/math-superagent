import numpy as np

# Operator directive 45 data: exact-mean threshold weights w(n) = min w with mean_n(w) >= 0.40
n = np.array([64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], dtype=float)
w = np.array([7, 11, 16, 24, 35, 52, 77, 112, 164, 239], dtype=float)

ln = np.log(n)
lw = np.log(w)

# per-doubling slope of log2(w) vs log2(n)
l2n = np.log2(n); l2w = np.log2(w)
print("=== per-doubling slopes (log2(w)/log2(n)) ===")
for i in range(1, len(n)):
    slope = (l2w[i]-l2w[i-1])/(l2n[i]-l2n[i-1])
    print(f"  n={n[i]:6.0f}  slope={slope:.4f}")

# ---- 1) OLS: log w = log C + a log n  (pure power w ~ C n^a) ----
# over the large-n tail as directed
for lo, hi, label in [(0,len(n),"all"), (4,len(n),"n>=1024"), (5,len(n),"n>=2048"), (6,len(n),"n>=4096")]:
    A = np.vstack([np.ones(len(n[lo:hi])), ln[lo:hi]]).T
    coef, res, *_ = np.linalg.lstsq(A, lw[lo:hi], rcond=None)
    resid = lw[lo:hi] - A@coef
    dof = len(n[lo:hi])-2
    s2 = resid@resid/dof
    cov = s2*np.linalg.inv(A.T@A)
    se = np.sqrt(np.diag(cov))
    print(f"\n--- pure power fit  w ~ C*n^a  [{label}, {len(n[lo:hi])} pts] ---")
    print(f"  a = {coef[1]:.4f} +- {se[1]:.4f}   lnC = {coef[0]:.3f} +- {se[0]:.3f}")
    print(f"  residual std (in log2) = {np.sqrt(resid@resid/len(resid)):.4f}")
    print(f"  |a - 1/2| = {abs(coef[1]-0.5):.4f} (in units of SE: {abs(coef[1]-0.5)/se[1]:.2f})")
    print(f"  |a - log4(3)=0.7925| = {abs(coef[1]-0.7925):.4f}")

# ---- 2) test w = c*sqrt(n): tabulate w/sqrt(n) ----
print("\n=== hypothesis w = c*sqrt(n): tabulate w/sqrt(n) ===")
for i in range(len(n)):
    r = w[i]/np.sqrt(n[i])
    print(f"  n={n[i]:6.0f}  w={w[i]:3.0f}  w/sqrt(n)={r:.4f}")
print("  flat?  std of column above (should be near 0 if power exactly 1/2)")
r = w/np.sqrt(n)
print(f"  mean={r.mean():.4f} std={r.std():.4f} rel_var={r.std()/r.mean():.3f}")

# ---- 3) test w = c*sqrt(n)*log(n) : tabulate w/(sqrt(n)*log n) ----
print("\n=== hypothesis w = c*sqrt(n)*log(n): tabulate w/(sqrt(n)*ln n) ===")
for i in range(len(n)):
    r = w[i]/(np.sqrt(n[i])*np.log(n[i]))
    print(f"  n={n[i]:6.0f}  w/(sqrt(n)lnn)={r:.5f}")
r = w/(np.sqrt(n)*np.log(n))
print(f"  mean={r.mean():.5f} std={r.std():.5f} rel_var={r.std()/r.mean():.3f}")

# ---- 4) test w = C*n^(log_4 3): tabulate w/n^0.7925 ----
print("\n=== hypothesis w = C*n^(log_4 3): tabulate w/n^0.7925 ===")
for i in range(len(n)):
    r = w[i]/n[i]**0.7925
    print(f"  n={n[i]:6.0f}  w/n^0.7925={r:.5f}")
r = w/n**0.7925
print(f"  mean={r.mean():.5f} std={r.std():.5f} rel_var={r.std()/r.mean():.3f}")

# ---- formal nested-model comparison: is adding log(n) to sqrt justified? ----
# fit log w = lnC + 0.5 ln n + beta ln(ln n)   (w ~ C sqrt(n) (ln n)^beta)
print("\n=== nested: log w = lnC + 0.5 ln n + beta ln(ln n), over n>=1024 ===")
lo=4
lnl = np.log(ln[lo:])
A = np.vstack([np.ones(len(n[lo:])), lnl]).T  # fix exponent at 1/2, let beta free
coef, res, *_ = np.linalg.lstsq(A, lw[lo:]-0.5*ln[lo:], rcond=None)
resid = (lw[lo:]-0.5*ln[lo:]) - A@coef
dof = len(n[lo:])-2
s2 = resid@resid/dof
cov = s2*np.linalg.inv(A.T@A)
se = np.sqrt(np.diag(cov))
print(f"  beta = {coef[1]:.4f} +- {se[1]:.4f}   lnC={coef[0]:.3f}+-{se[0]:.3f}")
print(f"  |beta|/SE = {abs(coef[1])/se[1]:.2f}  (if >~2, sqrt*log^n not just sqrt)")
print(f"  residual std(in log2) = {np.sqrt(resid@resid/len(resid)):.4f}")

# full 3-param: log w = lnC + a ln n + beta ln(ln n)
print("\n=== full: log w = lnC + a ln n + beta ln(ln n), n>=1024 ===")
A = np.vstack([np.ones(len(n[lo:])), ln[lo:], lnl]).T
coef, res, *_ = np.linalg.lstsq(A, lw[lo:], rcond=None)
resid = lw[lo:]-A@coef
dof = len(n[lo:])-3
s2 = resid@resid/dof
cov = s2*np.linalg.inv(A.T@A)
se = np.sqrt(np.diag(cov))
print(f"  a={coef[1]:.4f}+-{se[1]:.4f}  beta={coef[2]:.4f}+-{se[2]:.4f}  lnC={coef[0]:.3f}+-{se[0]:.3f}")
print(f"  residual std(in log2) = {np.sqrt(resid@resid/len(resid)):.4f}")
