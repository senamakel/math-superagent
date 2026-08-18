"""Independently attack the mod-100 regularity: is Psi(k) = c1(k) = 1+floor(k/phi^2) (mod 100)?
Check over every available recorded term: psi_residues.txt (mod M, k=1..400) and
psi_exact.txt (k=1..25). Also probe mods 100, 1000, 10000, and 100000 to find where it
first fails (strength of the claim).
"""
import mpmath as mp
mp.mp.dps = 80
PHI2_INV = mp.mpf(1) / ((1 + mp.sqrt(5)) / 2) ** 2
M = 101001001

def c1(k):
    return 1 + int(mp.floor(k * PHI2_INV))

def load_pairs(path):
    out = {}
    for line in open(path):
        p = line.split()
        if len(p) >= 2:
            out[int(p[0])] = int(p[1])
    return out

res = load_pairs("code/out/psi_residues.txt")   # Psi mod M, k=1..400
exact = load_pairs("code/out/psi_exact.txt")    # exact Psi, k=1..25

# The residues are mod M. Since M is not a multiple of 100, taking mod 100 of the
# residue gives Psi mod 100 correctly (residue == Psi mod M; and Psi mod 100 =
# (Psi mod M) mod 100 iff 100 | M, which it does NOT). So for k=1..400 the residue
# mod 100 is NOT necessarily Psi mod 100. Need Psi mod 100 from the exact values
# only (1..25) OR from the recurrence. Use exact for 1..25 here, and also build Psi
# via the validated recurrence for 1..3000 to get real Psi mod 100.
vR = load_pairs("code/out/vR_exact.txt")   # V(R_k) exact, k=1..2999
s1 = load_pairs("code/out/s1_exact.txt")   # S1(k) exact, k=1..3000
Psi = {1: 1}
for k in range(1, 3000):
    Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)

# sanity vs recorded exact
assert all(Psi[k] == exact[k] for k in range(1, 26)), "recurrence broke exact values"

for mod in [100, 1000, 10000, 100000, 1000000]:
    bad = [k for k in range(1, 3001) if Psi[k] % mod != c1(k) % mod]
    if bad:
        print(f"mod {mod}: FAILS at {len(bad)} of 3000; first failing k = {bad[:8]}")
    else:
        print(f"mod {mod}: HOLDS EXACTLY for k=1..3000")

# Also check the raw residue data: is Psi mod 100 recoverable? cross-check exact 1..25
print("\nmod-100 check on exact Psi k=1..25:")
bad100 = [k for k in range(1, 26) if exact[k] % 100 != c1(k) % 100]
print("  failures:", bad100 if bad100 else "NONE (holds exactly k=1..25)")
