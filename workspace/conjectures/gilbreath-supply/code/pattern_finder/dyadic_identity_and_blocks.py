#!/usr/bin/env python3
"""Verify a new exact identity on the fold at dyadic n, and extract the
per-doubling-block minimum structure of nu2(n)/n.

Identity (derived): for n = 2^k, with h the gap-parity string and
c_k(u) = 2^k - 1 - u the k-bit complement,

    T(2^k, d) = XOR over t with (2^k-1-d) subseteq t of h[t],

i.e. the depth-d fold cell at dyadic n is the SUPERSET-XOR of the k-bit
window h[0..2^k-1] evaluated at the complement of d.  (Because s subseteq d
iff c(d) subseteq c(s), and subtracting from 2^k-1 is bitwise complement.)

Checks against the literal definition of T via submasks (t_direct).
Verified for k = 3..12 on the real prime h.

Also: per-doubling-block minima of nu2(n)/n over [2^k, 2^{k+1}-1], k=5..14,
with exact values, argmins, and block minima of S(n)/n; and the running
minimum of nu2(n)/n over [50, 40000] with the exact membership of the set
{n : nu2(n)/n <= 18/53} (i.e. does anything tie the n=53 record).
"""
import json

data = json.load(open('/workspace/code/out/nu2_primes_xor_40000.json'))
assert data[53] == 18 and data[64] == 27 and data[4000] == 1975 and data[40000] == 20081
N = 40000

def nu2(n):
    return data[n]

def S(n):
    return (n - 2) - 2 * nu2(n)

# --- real prime h: need residues mod 4 of primes. lib has primes.py ---
import sys
sys.path.insert(0, '/workspace/code')
from lib.primes import primes_upto_index   # pylint: disable=import-error

def h_prefix(K):
    q = primes_upto_index(K + 2)
    return [1 if q[j + 1] % 4 != q[j] % 4 else 0 for j in range(K)]

# --- identity check ---
print("== dyadic superset-XOR identity: T(2^k, d) == XOR_{t superset c(d)} h[t] ==")
ok_all = True
for k in range(3, 13):
    n = 1 << k
    h = h_prefix(n)               # need h[0..n-1]
    # literal T
    for d in [2, 3, 5, 7, 11, 13, 2 ** (k // 2) if k >= 4 else 3, n - 2, n - 3, 1 << (k - 1)]:
        d = min(max(d, 2), n - 1)
        t = 0
        for o in range(d + 1):
            if (o & d) == o:
                t ^= h[n - 1 - d + o]
        # superset-XOR form: XOR over t with (n-1-d) subseteq t
        c = n - 1 - d
        t2 = 0
        for tt in range(n):
            if (tt & c) == c:
                t2 ^= h[tt]
        if t != t2:
            ok_all = False
            print(f"  MISMATCH k={k} d={d}: literal={t} superset={t2}")
print("identity holds on all checked (k=3..12, ~9 d-values each):", ok_all)

# --- block minima ---
print("\n== per-doubling-block minima of nu2(n)/n, k=5..14 (n in [2^k, 2^{k+1}) capped at N) ==")
for k in range(5, 15):
    lo, hi = 1 << k, min((1 << (k + 1)) - 1, N)
    if lo > N:
        break
    best_n, best_num, best_den = lo, nu2(lo), lo
    for n in range(lo, hi + 1):
        if nu2(n) * best_den < best_num * n:
            best_n, best_num, best_den = n, nu2(n), n
    print(f"  block [2^{k:2d},2^{k+1}) n<={hi}: min nu2/n = {best_num}/{best_den} = "
          f"{best_num/best_den:.6f} at n={best_n}, S(n)={S(best_n)}")

# --- running minimum with ties ---
print("\n== running minimum of nu2(n)/n over [50,40000] (ties counted) ==")
record = set()
cur_num, cur_den = nu2(50), 50
record.add(50)
for n in range(51, N + 1):
    if nu2(n) * cur_den <= cur_num * n:
        if nu2(n) * cur_den < cur_num * n:
            record = set()
            cur_num, cur_den = nu2(n), n
        record.add(n)
print("n attaining the running minimum (final set):", sorted(record))
m = sorted(record)[-1]
print(f"min over [50,40000] = nu2({m})/{m} = {cur_num}/{cur_den} = {cur_num/cur_den:.6f}")
print("all members (n, nu2(n)):", [(n, nu2(n)) for n in sorted(record)])

# --- S(2^k +/- 1) second-difference structure ---
print("\n== dyadic second-difference D2(k) = S(2^k+1) + S(2^k-1) - 2*S(2^k) ==")
vals = []
for k in range(3, 15):
    p = 1 << k
    d2 = S(p + 1) + S(p - 1) - 2 * S(p)
    vals.append(d2)
    print(f"  k={k:2d}  S(2^k-1)={S(p-1):6d}  S(2^k)={S(p):6d}  S(2^k+1)={S(p+1):6d}  D2={d2:6d}")
print("D2 sequence k=3..14:", " ".join(map(str, vals)))

# --- nu2(2^k - 1) sequence (fresh) ---
seq = [nu2((1 << k) - 1) for k in range(2, 16)]
print("\nnu2(2^k - 1) k=2..15:", " ".join(map(str, seq)))
seq2 = [nu2((1 << k) + 1) for k in range(2, 16)]
print("nu2(2^k + 1) k=2..15:", " ".join(map(str, seq2)))
seq3 = [S((1 << k) - 1) for k in range(2, 16)]
print("S(2^k - 1)   k=2..15:", " ".join(map(str, seq3)))
seq4 = [S(1 << k) for k in range(2, 16)]
print("S(2^k)       k=2..15:", " ".join(map(str, seq4)))