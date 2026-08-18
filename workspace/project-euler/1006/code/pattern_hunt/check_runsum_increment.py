"""PE1006: verify that the Psi recurrence increment summed over one full V-run
is closed-form in the run parameters (s_j, runlen L_j, V_j, A_j, d_j).

Recurrence: Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k),
with J(k) = 1 + floor((k+1)/phi^2).

Within a run [s_j, s_{j+1}-1]:
  V(R_k) = V_j  (constant),
  S1(s_j) = A_j,  and S1(k) = A_j + d_j*10^{s_j} for k in [s_j+1, s_{j+1}-1],
  J(k)   = 1 + floor((k+1)/phi^2)  (known additive).

So Psi(k+1) - 100*Psi(k) over the run, i.e. after L_j steps from Psi(s_j) to
Psi(s_{j+1}), is a function only of (s_j, L_j, V_j, A_j, d_j) plus a
geometric/floor sum of J(k).  We verify by exact computation that this
closed-form per-run increment reproducs the direct recurrence over all
proper runs up to KMAX, i.e. that a run-summation needs only these five
quantities (no per-k visits).

Actually, an O(log) collapse would still need V_j, A_j iterated across runs in
O(log) j.  This script merely *confirms the closed-form within-run increment*
so the run-sum decomposition is exact, and records the five quantities to
make clear what an O(log) scheme would have to drive.
"""
from decimal import Decimal, getcontext
getcontext().prec = 500

KMAX = 3000
M = 101001001

S1 = [0] * (KMAX + 1)
V = [0] * (KMAX + 1)
Psi = [None] * (KMAX + 1)
# Psi exact from psi_exact only to 25; use mod-M recurrence from psi_residues for k<=400,
# but we have exact Psi only to 25.  For verifying the within-run increment closure we
# need Psi at run boundaries -- compute Psi exactly via the recurrence starting from Psi(1)=1.
# Psi exact: psi(1)=1. Rebuild with modular arithmetic won't give exact; but we can
# carry Psi exactly (numbers get huge ~10^2k) -- only up to KMAX=3000 is infeasible.
# Instead verify the *increment identity as integers without Psi*, i.e. check that
# sum over run of [100*V^2 + 20*S1(k) + J(k)] equals the formula using (L, V, A, d, s).
for line in open('code/out/s1_exact.txt'):
    k, v = line.split(); S1[int(k)] = int(v)
for line in open('code/out/vR_exact.txt'):
    k, v = line.split(); V[int(k)] = int(v)

runs = []
start, v0 = 1, V[1]
for k in range(2, KMAX + 1):
    if V[k] != v0:
        runs.append((start, k - 1, v0)); start, v0 = k, V[k]
runs.append((start, KMAX, v0))

phi2 = (Decimal(3) + Decimal(5).sqrt()) / 2
from decimal import Decimal as D

def J(k):
    return 1 + int(D(k + 1) / phi2)

# within-run increment (integer, no Psi) computed both ways:
#  direct: sum_{k=a}^{b} [100 V(R_k)^2 + 20 S1(k) + J(k)]
#  closed: L*100*V^2 + 20*(A + d*10^{s} * (L-1 if L>=2)) + sum J(k)
#         (careful: S1(s)=A at k=s; S1(k)=A+d*10^s for k=s+1..b, i.e. (L-1) copies).
sumJ = {}
for k in range(1, KMAX + 1):
    sumJ[k] = sumJ.get(k - 1, 0) + J(k)     # prefix sum of J

bad = None
nchecked = 0
for j in range(1, len(runs)):
    a, b, v = runs[j]
    L = b - a + 1
    if L == 1:
        continue   # truncation singleton
    A = S1[a]
    d = (S1[a + 1] - S1[a]) // (10 ** a) if 10 ** a else None
    # direct
    direct = sum(100 * V[k] * V[k] + 20 * S1[k] + J(k) for k in range(a, b + 1))
    # closed
    closed = L * 100 * v * v
    if L >= 2:
        closed += 20 * (A + d * (10 ** a)) * (L - 1) + 20 * A
    else:
        closed += 20 * A
    closed += sumJ[b] - sumJ[a - 1]
    nchecked += 1
    if direct != closed:
        bad = (j, a, direct, closed)
        break

print("proper runs checked:", nchecked)
print("within-run increment closed-form in (s_j, L, V_j, A_j, d_j):",
      "VERIFIED" if bad is None else "MISMATCH " + str(bad))

# Also report the five quantities for the first several runs so an O(log) driver
# sees exactly what it must iterate.
print("\nfirst 10 runs: (j, s_j, L_j, V_j, A_j=S1(s_j), d_j)")
for j in range(1, 11):
    a, b, v = runs[j]
    L = b - a + 1
    d = (S1[a + 1] - S1[a]) // (10 ** a)
    print(f"  j={j:3d} s={a:5d} L={L} V={v} A={S1[a]} d={d}")
