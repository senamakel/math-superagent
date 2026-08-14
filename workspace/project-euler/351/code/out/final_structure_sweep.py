"""Final exact sweep over the stored 200000-term prefixes for structure the
prior passes did not cover:

1. A063985 at primes p (p <= 200000): subsequence A(p).
2. A063985 at triangular numbers T_k = k(k+1)/2.
3. A063985 at prime powers p^2, p^3 for odd primes p <= 200000.
4. Full-prefix period scan: A mod 6, H mod 36 (periods 1..24), and H mod 60
   (periods 1..40) -- the low-composite moduli not yet checked (prior pass
   covered A mod 2, A mod 4, H mod 24, H mod 12).
5. First differences of the halves: is A_e(k+1)-A_e(k) or A_o(k+1)-A_o(k)
   a recognizable sequence (e.g. cototient-like)?

All exact integer arithmetic; every claim is over the terms actually on disk.
"""
import json
import numpy as np

N = 200_000
A = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)
H = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)
assert len(A) == N and len(H) == N

# --- primes via a small sieve -------------------------------------------
spf = np.zeros(N + 1, dtype=np.int64)
for i in range(2, N + 1):
    if spf[i] == 0:
        spf[i] = i
        if i * i <= N:
            spf[i * i::i] = i  # mark multiples (values >1 mean composite)
primes = [i for i in range(2, N + 1) if spf[i] == i]

# 1. A at primes
A_p = [int(A[p - 1]) for p in primes]
print("A(p), first primes:", json.dumps(A_p[:40]))
print("count of primes used:", len(A_p))

# 2. A at triangular numbers
T = []
k = 1
while k * (k + 1) // 2 <= N:
    T.append(k * (k + 1) // 2)
    k += 1
A_T = [int(A[t - 1]) for t in T]
print("A(T_k), k=1..%d:" % len(T), json.dumps(A_T[:40]))

# 3. A at p^2, p^3 for odd primes
def vals_power(e):
    out = []
    for p in primes:
        if p == 2:
            continue
        pe = p ** e
        if pe > N:
            break
        out.append(int(A[pe - 1]))
    return out

for e in (2, 3):
    v = vals_power(e)
    print(f"A(p^{e}), odd primes:", json.dumps(v[:30]))

# 4. period scans over the full prefix
def period(Aarr, n_from, mod, pmax, label):
    found = []
    for p in range(1, pmax + 1):
        ok = True
        for n in range(n_from, N + 1 - p):
            if (Aarr[n - 1] - Aarr[n + p - 1]) % mod != 0:
                ok = False
                break
        if ok:
            found.append(p)
    print(f"{label}: exact periods <= {pmax} over n = {n_from}..{N}: {found}")

period(A, 2, 6, 24, "A mod 6")
period(H, 2, 36, 24, "H mod 36")
period(H, 2, 60, 40, "H mod 60")

# 5. first differences of the even/odd halves vs cototient
#    A(2k) - A(2k-2) = c(2k-1) + c(2k); c = cototient on disk
C = np.loadtxt("code/out/seq_cototient.txt", dtype=np.int64)
d_e = [A[2 * k] - A[2 * k - 2] for k in range(1, N // 2)]  # A(2k+2)-A(2k)
expect = [C[2 * k] + C[2 * k + 1] for k in range(N // 2 - 1)]  # c(2k+1)+c(2k+2)
print("half-difference identity A(2k+2)-A(2k) == c(2k+1)+c(2k+2):",
      all(d_e[i] == expect[i] for i in range(len(d_e))))
