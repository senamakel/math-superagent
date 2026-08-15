#!/usr/bin/env python3
"""Oracle check for candidates 1 (majorization/Schur-flatness) and 2
(Dirichlet energy / electric network) against the real prime rows.

Halving convention: for k >= 1 every entry A_k(i), i>=1, is even (2 is the
only even prime). Halved row h = A_k/2 (position 0 is A_k(0)=1, halved = .5
in general, so we only consider i >= 1 for halved integer entries).

Candidate 1 majorization test: is sorted(h_{k+1}) majorized by sorted(h_k)?
(For equal-length comparison we truncate to a common width; the rows have
different widths, so the honest test is "does the sorted halved row become
flatter" which we check via the Schur-convex test function sum of squares.)
"""
from lib.gilbreath import primes_up_to, rows_generator, block_profile

DEPTH = 60
SIEVE = 200000

primes = primes_up_to(SIEVE)
gen = rows_generator(primes, DEPTH)
rows = [next(gen) for _ in range(DEPTH + 1)]  # rows[0] = primes A_0

def halved(row):
    # row entries: A_k(0)=1, rest even. halve the even part (drop position 0)
    return [v//2 for v in row[1:]]

# If any halved entry is not an integer, the parity invariant broke
def check_parity(rows):
    for k in range(1, DEPTH + 1):
        for v in rows[k][1:]:
            if v % 2 != 0:
                return k
    return None

pb = check_parity(rows)
print(f"Parity invariant ok (all even entries): {pb is None} (first break {pb})")

# Candidate 1: sum-of-squares = 2*sum over pairs... For a Schur-convex func,
# x majorizes y  =>  sum phi(y_i) <= sum phi(x_i) for all convex phi.
# The flattest vector minimizes sum of squares (phi=t^2 convex). So test:
# does sum(h_{k+1}^2) <= sum(h_k^2) (i.e. h_k majorizes h_{k+1})?
# But widths differ (row k+1 is one shorter). Compare on the common prefix.
def sq_sum(h):
    return sum(t*t for t in h)

viol_major = []
for k in range(1, DEPTH):
    hk = halved(rows[k])
    hk1 = halved(rows[k+1])
    common = min(len(hk), len(hk1))
    a = sq_sum(hk[:common])
    b = sq_sum(hk1[:common])
    if b > a:  # row k+1 is "less flat" -> h_k does NOT majorize h_{k+1}
        viol_major.append((k, a, b))
print("Candidate 1 majorization (sum-of-squares test, common prefix):")
print(f"  violations (sos increases): {len(viol_major)} / {DEPTH-1}")
print(f"  first {min(viol_major[:6], default=None)}")

# Stronger: sum-of-squares over the FULL halved row (drop position 0 only)
viol_full = []
for k in range(1, DEPTH):
    a = sq_sum(halved(rows[k]))
    b = sq_sum(halved(rows[k+1]))
    if b > a:
        viol_full.append((k, a, b))
print("  full-row violations:", len(viol_full), "first", min(viol_full[:6], default=None))

# Check flat prefix: does the number of {0,1}-valued halved entries at the
# start equal b_k (the leading {0,2} block)?
mismatch = []
for k in range(1, DEPTH + 1):
    hk = halved(rows[k])
    b = block_profile(rows[k])
    flat = 0
    for v in hk:
        if v in (0, 1):
            flat += 1
        else:
            break
    if flat != b:
        mismatch.append((k, flat, b))
print(f"Flat prefix == block length: mismatches {len(mismatch)} / {DEPTH}")
print(f"  first {min(mismatch[:6], default=None)}")

# Candidate 2: Dirichlet energy on halved row
# c_i = 1 if |h_i - h_{i+1}| <= 1 else 0 (a "break")
# E = sum c_i (h_i - h_{i+1})^2
def energy(h):
    E = 0
    for i in range(len(h) - 1):
        d = abs(h[i] - h[i+1])
        if d <= 1:
            E += d * d
    return E

energy_data = []
viol_energy = []
max_increase = (0, None, None)
for k in range(1, DEPTH):
    hk = halved(rows[k])
    hk1 = halved(rows[k+1])
    e1 = energy(hk)
    e2 = energy(hk1)
    energy_data.append((k, e1, e2, e2 - e1))
    if e2 > e1:
        viol_energy.append((k, e1, e2, e2 - e1))
        if e2 - e1 > max_increase[0]:
            max_increase = (e2 - e1, k, (e1, e2))

print("\nCandidate 2 Dirichlet energy E = sum c_i |h_i-h_{i+1}|^2:")
print(f"  violations (E increases): {len(viol_energy)} / {DEPTH-1}")
print(f"  max single increase: {max_increase}")
print(f"  first 6: {min(viol_energy[:6], default=None)}")

# Also full unhalved variant isn't needed; report first few energy rows:
print("  sample (k, E_k, E_{k+1}, dE):", energy_data[:6])
