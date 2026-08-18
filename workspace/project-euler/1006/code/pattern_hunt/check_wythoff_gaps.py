"""Verify the run-gap structure of the V-runs: run starts s_j = floor(j*phi^2)
(upper Wythoff A001950), so the gaps d_j = s_{j+1}-s_j take values in {2,3}.
Check against the recorded r_runs_wythoff.txt starts and against the exact
irrational formula, and report the gap densities. Also verify the last-two-digit
cross-check c1(10^18) = 1 + floor(10^18/phi^2) == 52 (mod 100)."""
import mpmath as mp
mp.mp.dps = 80
PHI2 = ((1 + mp.sqrt(5)) / 2) ** 2

def floor_j_phi2(j):
    return int(mp.floor(j * PHI2))

# --- 1. parse recorded run starts from r_runs_wythoff.txt ---
starts = []
for line in open("code/out/r_runs_wythoff.txt"):
    line = line.strip()
    if line.startswith("run starts s_j") and "(j=1..1146), first 60:" in line:
        # this header's continuation lines hold the numbers; we instead re-derive
        # from the "first runs" lines which explicitly list (j, s_j, ...)
        pass
    if line.startswith("  j="):
        parts = line.split()
        # format: j=   2 s=    2 end=    4 len=3 V=10
        s = int(parts[2].split("=")[1])
        j = int(parts[0].split("=")[1])
        starts.append((j, s))

# the first-runs block starts at j=2; reconstruct full starts from formula and check
# the recorded first runs match, then verify formula for all j vs the Wythoff claim.
print("recorded first-runs (j, s_j) count:", len(starts))
mismatch = [(j, s, floor_j_phi2(j)) for (j, s) in starts if floor_j_phi2(j) != s]
print("formula floor(j*phi^2) mismatches in recorded first-runs:", mismatch if mismatch else "NONE")

# gaps from formula for j=1..1146
g = [floor_j_phi2(j) - floor_j_phi2(j-1) for j in range(1, 1147)]
from collections import Counter
c = Counter(g)
print("gap values (gaps between consecutive upper Wythoff numbers), j=1..1146:",
      dict(c), "  min/max:", min(g), max(g))
print("gap sequence length:", len(g))
print("first 30 gaps:", g[:30])

# --- 2. last-two-digit cross-check ---
import math
n = 10**18
# exact integer floor via integer sqrt of 5*n^2, n^2*phi^2 = ... ; phi^2 = (3+sqrt5)/2
# floor(n*phi^2) : phi^2 = (3+sqrt5)/2, so floor = floor((3n + n*sqrt5)/2)
# n*sqrt5 = sqrt(5 n^2)
s5 = math.isqrt(5*n*n)
v = (3*n + s5) // 2   # floor(n*phi^2) for the std Fibonacci density (this is ones-density weight)
# but c1 uses 1/phi^2: c1(n)=1+floor(n/phi^2). floor(n/phi^2) = floor(n*(3-sqrt5)/2) roughly.
s5b = math.isqrt(5*n*n)
c1_high = 1 + (3*n - s5b)//2  # careful: this is floor of n*phi^-2 via conjugate; verify below
# Actually 1/phi^2 = (3-sqrt5)/2. floor(n*(3-sqrt5)/2) = floor((3n - sqrt(5n^2))/2)
c1_val = 1 + (3*n - s5b) // 2
print("c1(10^18) = 1 + floor(10^18/phi^2) =", c1_val)
print("c1(10^18) mod 100 =", c1_val % 100, "(expect 52)")
print("floor(10^18/phi^2) =", (3*n - s5b)//2, "(expect 381966011250105152)")
