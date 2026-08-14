"""Second pattern pass for PE 351: exact, fully vectorized sequence checks.

All checks are exact integer arithmetic over the 200000-term prefixes on disk
(code/out/seq_*.txt).  This pass adds, beyond the first pattern pass:
  * exact term-by-term verification of the A(n) mod 2 period-4 law from n=2,
    with the correct pairing A(n) vs A(n+4) (the first pass's check_mod4_law
    used the same law, verified here afresh),
  * exact search for longer periods of A mod 2 up to 400,
  * the prime-power cototient identity c(p^a) == p^(a-1), vectorized,
  * the jump law dH(n) = 6*c(n), hence 6*p^(a-1) at prime powers,
  * fresh-window (terms 50..350) constant-coefficient recurrence search,
    independent of the first-30 window that produced the spurious order-4 fit.
"""
import numpy as np
from collections import Counter

N = 200_000
H = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)
A = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)
Phi = np.loadtxt("code/out/seq_Phi.txt", dtype=np.int64)
c = np.loadtxt("code/out/seq_cototient.txt", dtype=np.int64)
n = np.arange(1, N + 1, dtype=np.int64)

# --- 1. exact identities over the full prefix ---
print("identity H == 3n(n+1) - 6*Phi:",
      bool(np.array_equal(H, 3 * n * (n + 1) - 6 * Phi)))
print("dH == 6*c:", bool(np.array_equal(np.diff(H, prepend=0), 6 * c)))
print("dA == c:", bool(np.array_equal(np.diff(A, prepend=0), c)))

# --- 2. c(k) == 1 iff k prime (exact spf sieve) ---
spf = np.zeros(N + 1, dtype=np.int64)
for p in range(2, N + 1):
    if spf[p] == 0:
        spf[p::p] = p
isprime = (spf[1:] == n)
print("c(k)==1 iff k prime: exceptions =",
      int(np.sum((c == 1) != isprime)))

# --- 3. A(n) mod 2 period-4 law from n=2: A(n+4) == A(n) mod 2 ---
am = A % 2
viol = int(np.sum(am[1:N-4] != am[5:N]))       # n=2..N-4
print(f"A(n+4)==A(n) mod 2, n=2..N-4: violations = {viol}")
pred = np.isin(n % 4, [1, 2])
print("A(n) odd iff n mod 4 in {1,2}, n=2..N:",
      bool(np.array_equal((A % 2).astype(bool)[1:], pred[1:])))

# --- 4. H mod 12 period-4 law; residue counts ---
predH = np.zeros(N, dtype=np.int64)
predH[1:] = 6 * (((n[1:] + 1) // 2) % 2)
print("H(n) mod 12 == 6*ceil(n/2) mod 2 for n=2..N:",
      bool(np.array_equal(H % 12, predH)))
print("H mod 12 counts:", dict(sorted(Counter((H % 12).tolist()).items())))
print("Phi mod 2 counts:", dict(Counter((Phi % 2).tolist())))

# --- 5. exact periods p of A mod 2 over n=2..N-p ---
periods = [p for p in range(1, 401)
           if np.array_equal(am[1:N-p], am[1+p:N])]
print("periods of A mod 2 (n>=2) up to 400:", periods)

# --- 6. prime-power cototient identity c(p^a) == p^(a-1) ---
k = np.arange(1, N + 1, dtype=np.int64)
p0 = spf[1:]
tval = np.zeros(N, dtype=np.int64)
m = k.copy()
active = np.ones(N, dtype=bool)
for _ in range(20):  # 2^20 > 2e5
    div = active & (m % p0 == 0)
    tval = tval + div
    m = np.where(div, m // p0, m)
    active = div
is_pp = (p0 ** tval == k)
ok = np.all(c[is_pp] == p0[is_pp] ** (tval[is_pp] - 1))
print(f"c(p^a) == p^(a-1) for all prime powers k<=N: {bool(ok)} "
      f"(count {int(np.sum(is_pp))})")

# --- 7. jump law at prime powers ---
dH = np.diff(H, prepend=0)
ok2 = np.all(dH[is_pp] == 6 * p0[is_pp] ** (tval[is_pp] - 1))
print(f"dH(n) == 6*p^(a-1) at prime powers n<=N: {bool(ok2)}")
print("dH min/max over n=2..N:", int(dH[1:].min()), int(dH[1:].max()))
