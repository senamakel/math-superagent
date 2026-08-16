#!/usr/bin/env python3
"""Break the fitted sublinear exponent E~0.555 of the exact-mean linear-supply
threshold weight w*(n).

Prior passes fitted log2(w*) = a + E*log2(n), getting E~0.555, and rejected
pure sqrt(n) (E=0.5) at 27 sigma. But a pure-power OLS can absorb a slow
(log n)^B factor into an inflated E. Here we fit the richer family

    log w* = a + E*log n + B*log(log n)

to the FULL exact dataset (power-of-2 AND intermediate-phase n), and test
whether (i) E collapses toward 1/2 with a positive B (the binomial-tail
model), or (ii) B ~ 0 and E stays ~0.555 (genuine n^0.555).

Data: exact w*(n) from threshold_weight_logperiodic_extended.txt (all phases)
plus the non-power-of-two n. All per-n w* are EXACT integers from the verified
threshold formula.

This is a numerical fit, not a proof: it says which functional form the data
support, not what holds for all n.
"""
import math

# (n, w*) exact, from threshold_weight_logperiodic_extended.txt PART B &
# earlier threshold_limit_exact.txt.  All EXACT integer values.
DATA = [
    (8,3),(10,3),(12,3),(14,4),(16,3),
    (32,5),(64,7),
    (128,11),
    (256,16),(512,24),(768,32),(1024,35),(1536,47),(2048,52),(3072,70),
    (4096,77),(5120,95),(6144,102),(8192,112),(10240,138),(12288,149),
    (16384,164),(20480,202),(24576,218),(32768,239),(40960,296),(49152,319),
    (65536,349),
]

def ols(X, y):
    # X: list of rows, y: list. returns beta (lstsq-style)
    n = len(y)
    k = len(X[0])
    # normal equations
    import numpy as np
    Xa = np.array(X, dtype=float)
    ya = np.array(y, dtype=float)
    beta, res, rank, sv = np.linalg.lstsq(Xa, ya, rcond=None)
    # standard errors
    resid = ya - Xa @ beta
    dof = n - k
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.inv(Xa.T @ Xa)
    se = np.sqrt(np.diag(cov))
    return beta, se

def log2(x): return math.log2(x)

print("="*74)
print("Model 1: log2 w* = a + E*log2 n        (pure power)")
print("Model 2: log2 w* = a + E*log2 n + B*log2(log2 n)  (power * log-power)")
print("Model 3: log2 w* = a + 0.5*log2 n + B*log2(log2 n)  (forced sqrt * log^B)")
print("="*74)

for subset_name, subset in [
    ("ALL phases (power + intermediate)", DATA),
    ("powers of 2 only", [d for d in DATA if abs(math.log2(d[0])-round(math.log2(d[0])))<1e-9]),
    ("n>=256 all phases", [d for d in DATA if d[0]>=256]),
    ("n>=512 all phases", [d for d in DATA if d[0]>=512]),
]:
    print(f"\n--- {subset_name} ({len(subset)} pts) ---")
    X1 = [[1.0, log2(n)] for n,_ in subset]
    y  = [log2(w) for _,w in subset]
    b1, s1 = ols(X1, y)
    print(f"  Model1: E= {b1[1]:.5f} +/- {s1[1]:.5f}   a={b1[0]:.4f}")

    X2 = [[1.0, log2(n), log2(log2(n))] for n,_ in subset]
    b2, s2 = ols(X2, y)
    print(f"  Model2: E= {b2[1]:.5f} +/- {s2[1]:.5f}   B={b2[2]:.5f} +/- {s2[2]:.5f}  a={b2[0]:.4f}")

    # Model 3: force E=0.5, fit B
    X3 = [[1.0, log2(log2(n))] for n,_ in subset]
    y3 = [log2(w) - 0.5*log2(n) for n,w in subset]
    b3, s3 = ols(X3, y3)
    print(f"  Model3(forced sqrt): B={b3[1]:.5f} +/- {s3[1]:.5f}  a={b3[0]:.4f}")

    # Compare residuals
    import numpy as np
    def rss(Xb):
        Xa=np.array(Xb,float); ya=np.array(y,float)
        # use beta from model
        return 0
    # RSS model1 vs model2
    Xa1=np.array(X1,float); Xa2=np.array(X2,float); ya=np.array(y,float)
    r1 = np.sum((ya - Xa1@b1)**2)
    r2 = np.sum((ya - Xa2@b2)**2)
    r3 = np.sum((ya - (b3[0]+0.5*np.log2([n for n,_ in subset])+b3[1]*np.log2([math.log2(n) for n,_ in subset])))**2)
    print(f"  RSS: M1={r1:.5f}  M2={r2:.5f}  M3(forced sqrt)={r3:.5f}")

print("\n" + "="*74)
print("Interpretation: if Model 2 finds B significantly >0 and E pulled toward")
print("0.5, the data support w* ~ n^E (log n)^B rather than pure n^0.555. If B~0")
print("and E stays ~0.55 with RSS barely improving, the pure-power fit stands.")
print("This is a numerical model comparison, not a proof of any limit.")
