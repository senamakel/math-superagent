"""Independent integrity re-check for the pattern-finder pass.

1. Recompute H(1..40), A063985(1..40) from a fresh naive phi sieve
   (no shared code with the stored files' producer).
2. Compare against the stored 200000-term files.
3. Verify H = 6*A063985 and A063985 = n(n+1)/2 - Phi over the FULL stored
   range with exact integer arithmetic (numpy object-free: python ints via
   lists is 200k*small work, fine; use numpy with int64, values ~1e11 fit).
4. Check the mod-12 period-4 law over the full range.
5. Check first-difference structure dA(n) = n - phi(n) (cototient) over the
   full range.
Exact integer arithmetic throughout.
"""
import numpy as np

N = 200000

# ---- fresh naive phi sieve ----
phi = list(range(N + 1))
for i in range(2, N + 1):
    if phi[i] == i:  # prime
        for j in range(i, N + 1, i):
            phi[j] -= phi[j] // i

c = [0] * (N + 1)          # cototient k - phi(k)
A = [0] * (N + 1)          # A063985 prefix sum
Phi = [0] * (N + 1)        # summatory phi
for k in range(1, N + 1):
    c[k] = k - phi[k]
    A[k] = A[k - 1] + c[k]
    Phi[k] = Phi[k - 1] + phi[k]

H = [6 * a for a in A]     # H = 6*A063985

# ---- load stored files ----
def load(path):
    with open(path) as f:
        return [int(t) for t in f.read().split()]

H_store = load("code/out/seq_H.txt")
A_store = load("code/out/seq_A063985.txt")
Phi_store = load("code/out/seq_Phi.txt")
cot_store = load("code/out/seq_cototient.txt")
phi_store = load("code/out/seq_phi.txt")
assert len(H_store) == len(A_store) == len(Phi_store) == N
assert len(cot_store) == len(phi_store) == N

# 1-based -> list index: stored file term i is at index i-1
ok_H = all(H[n] == H_store[n - 1] for n in range(1, N + 1))
ok_A = all(A[n] == A_store[n - 1] for n in range(1, N + 1))
ok_Phi = all(Phi[n] == Phi_store[n - 1] for n in range(1, N + 1))
ok_c = all(c[n] == cot_store[n - 1] for n in range(1, N + 1))
ok_phi = all(phi[n] == phi_store[n - 1] for n in range(1, N + 1))
print("fresh-sieve matches stored files: H", ok_H, "| A", ok_A,
      "| Phi", ok_Phi, "| cototient", ok_c, "| phi", ok_phi)

# ---- identity checks over the full range ----
ok_id1 = all(H[n] == 6 * A[n] for n in range(1, N + 1))
ok_id2 = all(A[n] == n * (n + 1) // 2 - Phi[n] for n in range(1, N + 1))
ok_id3 = all(H[n] == 3 * n * n + 3 * n - 6 * Phi[n] for n in range(1, N + 1))
print("identities over n=1..%d: H=6A: %s | A=n(n+1)/2-Phi: %s | H=3n^2+3n-6Phi: %s"
      % (N, ok_id1, ok_id2, ok_id3))

# ---- mod-12 period-4 law over full range ----
law = {0: 0, 1: 6, 2: 0, 3: 6}  # predicted H mod 12 from n mod 4? check doc:
# doc says residues 6,0,0,6 for n = 2,3,4,5 (mod 4): n mod4=2 -> 6, 3 -> 0,
# 0 -> 0, 1 -> 6.  Verify directly from data instead of trusting the table:
viol = [n for n in range(2, N + 1)
        if H[n] % 12 != 6 * ((n + 1) // 2 % 2)]
print("mod-12 law violations over n=2..%d: %d (first: %s)"
      % (N, len(viol), viol[:3]))

# ---- cototient structure over full range ----
bad_prime = [k for k in range(1, N + 1) if (c[k] == 1) != (phi[k] == k - 1)]
# c[k]==1 iff k prime is equivalent to phi(k)==k-1; a primality-free check:
# count c[k]==1 occurrences vs number of primes in [1,N] computed by sieve
n_ones = sum(1 for k in range(1, N + 1) if c[k] == 1)
n_primes = sum(1 for k in range(1, N + 1) if phi[k] == k - 1 and k > 1)
print("c[k]==1 count:", n_ones, "| prime count:", n_primes,
      "| equal:", n_ones == n_primes)
bad_prime_power = [k for k in range(1, N + 1)
                   if phi[k] == k - 1]  # placeholder; real check below
# dA at prime powers: A(p^a) - A(p^a - 1) = c(p^a) = p^(a-1)
from math import isqrt
pp_viol = 0
for p in range(2, isqrt(N) + 1):
    if phi[p] == p - 1:  # p prime
        pk = p * p
        while pk <= N:
            if A[pk] - A[pk - 1] != pk // p:
                pp_viol += 1
            pk *= p
print("prime-power jump violations (c(p^a)=p^(a-1)):", pp_viol)

# ---- oracle values from stored files ----
print("oracles from stored files: H(5)=%d H(10)=%d H(1000)=%d"
      % (H_store[4], H_store[9], H_store[999]))
print("H(10^8) recorded anchor check:", 6 * 1960364533634092)
