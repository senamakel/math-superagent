import numpy as np

# threshold weight w(n) = first weight at which linear supply becomes typical
# (mean nu2/n >= 0.40), from threshold_limit_exact.txt
ns   = [8, 10, 12, 14, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
ws   = [3, 3, 3, 4, 3, 5, 7, 11, 16, 24, 35, 52, 77]

lnn = np.log(np.array(ns, dtype=float))
lnw = np.log(np.array(ws, dtype=float))

def fit(idx):
    x = lnn[idx]; y = lnw[idx]
    A = np.vstack([x, np.ones_like(x)]).T
    coef, res, *_ = np.linalg.lstsq(A, y, rcond=None)
    alpha, logC = coef
    yhat = A@coef
    resid = y - yhat
    n = len(x)
    dof = n-2
    s2 = resid@resid/dof
    # standard error on slope
    Sxx = ((x-x.mean())**2).sum()
    se_alpha = np.sqrt(s2/Sxx)
    return alpha, se_alpha, np.exp(logC), resid

# per-doubling log-slope between consecutive pts in the ordered list where
# n doubles exactly: 8->16, 16->32, ..., 2048->4096
print("per-doubling log2(w)/log2(n) slopes (successive doublings of n):")
print(" n      log2(slope)")
prev = None
for n,w in zip(ns,ws):
    if prev is not None:
        dn = n/prev[0]
        if abs(dn-2) < 1e-9:
            sl = (np.log2(w)-np.log2(prev[1]))/np.log2(dn)
            print(f" {prev[0]:5d}->{n:5d}   {sl:.4f}")
    prev=(n,w)

print("\nlog-log OLS fits (alpha, std err, C):")
all_idx = list(range(len(ns)))
print(f"  all 13 pts:  alpha={fit(all_idx)[0]:.4f} +- {fit(all_idx)[1]:.4f}  C={fit(all_idx)[2]:.4f}")
for lo in [6,7,8,9]:
    idx = list(range(lo, len(ns)))
    a,se,C,_ = fit(idx)
    print(f"  last {len(idx)} pts (from n={ns[lo]}): alpha={a:.4f} +- {se:.4f}  C={C:.4f}")

# candidate exponents
cands = {
    "log4(3)=0.7925": np.log(3)/np.log(4),
    "1/2": 0.5,
    "log(3)/log(4)=0.7925": np.log(3)/np.log(4),
    "0.57(fitted)": 0.57,
}
# which candidate best tracks the large-n data? compare predicted vs actual w at n=4096
print("\nPredicted w(4096) from each candidate exponent (C from last 6 pts):")
idx = list(range(len(ns)-6, len(ns)))
a6,se6,C6,_ = fit(idx)
for name, expo in cands.items():
    # C re-fit at fixed exponent
    # ln w = expo*ln n + ln C  =>  ln C = mean(lnw - expo*lnn)
    lnC = (lnw[idx] - expo*lnn[idx]).mean()
    pred = np.exp(expo*np.log(4096)+lnC)
    print(f"  {name:22s}: pred w(4096)={pred:.1f} (actual 77)")

# residual analysis for the straight log-log fit to say WHERE it breaks
print("\nresiduals (lnw - fitted) for all-13 fit, in n order:")
a,se,C,resid = fit(all_idx)
for n,w,r in zip(ns,ws,resid):
    print(f"  n={n:5d} w={w:3d} resid={r:+.4f}")
