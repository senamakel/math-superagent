"""Independent re-check of the mod-12 periodicity conjecture for H(n).

Route 1 (fresh phi computation, different code from patterns.py):
  recompute phi via phi(n) = n * prod_{p|n} (1 - 1/p) using smallest-prime
  factor sieve, then c(k) = k - phi(k), A(n) = sum c, H = 6A, and verify
  H(n) mod 12 == 6*((n+1)//2 mod 2) for all 2 <= n <= 200000.

Route 2 (elementary parity proof, checked computationally):
  phi(k) even for k >= 3, so c(k) = k - phi(k) has c(1)=0, c(2)=1 and
  c(k) == k (mod 2) for k >= 3.  Then A(n) mod 2 = 1 + floor((n-1)/2) mod 2
  and H(n) mod 12 = 6*(A(n) mod 2) for n >= 2, i.e. the period-4 pattern
  6,0,0,6 starting at n=2.

Route 3 (full-size prediction): from the stored exact H(10^8), check
  H(10^8) mod 12 == 6*((10^8+1)//2 mod 2) == 0.
"""
import numpy as np

# ---- Route 1: fresh smallest-prime-factor sieve (independent implementation)
N = 200_000
spf = np.zeros(N + 1, dtype=np.int64)
for i in range(2, N + 1):
    if spf[i] == 0:                     # i prime
        spf[i::i] = i                   # mark multiples (first hit is i itself)

phi = np.arange(N + 1, dtype=np.int64)
phi[0] = 0
# phi(n) = n * prod_{p|n}(1-1/p): for each prime p, multiply all its
# multiples n by (1 - 1/p) = (p-1)/p.
p_mask = np.zeros(N + 1, dtype=bool)
p_mask[2:] = spf[2:] == np.arange(2, N + 1, dtype=np.int64)
for p in np.nonzero(p_mask)[0]:
    m = np.arange(p, N + 1, p, dtype=np.int64)
    phi[m] = phi[m] * (p - 1) // p

c = np.arange(1, N + 1, dtype=np.int64) - phi[1:]
A = np.zeros(N + 1, dtype=np.int64)
A[1:] = np.cumsum(c)
H = 6 * A[1:]

n = np.arange(1, N + 1, dtype=np.int64)
pred = np.zeros(N, dtype=np.int64)
pred[1:] = 6 * (((n[1:] + 1) // 2) % 2)          # n >= 2
ok1 = np.array_equal(H % 12, pred)
print("Route 1: fresh spf-sieve phi;  H(n) mod 12 == 6*((n+1)//2 mod 2), 2<=n<=%d: %s"
      % (N, ok1))
assert ok1

# ---- Route 2: parity proof steps
assert c[0] == 0 and c[1] == 1                     # c(1)=0, c(2)=1
parity_ok = np.all((c[2:] % 2) == ((np.arange(3, N + 1) % 2)))   # k >= 3
print("Route 2: c(k) == k (mod 2) for 3<=k<=%d: %s" % (N, parity_ok))
assert parity_ok
Amod2 = (1 + (n[1:] - 1) // 2) % 2            # formula valid for n >= 2
AA = A[1:]                                     # AA[i] = A063985(i+1), i = 0..N-1
ok2 = np.array_equal(AA[1:] % 2, Amod2)        # AA[1:] = A(2..N)
print("Route 2: A063985(n) mod 2 == 1 + floor((n-1)/2) mod 2, 2<=n<=%d: %s"
      % (N, ok2))
assert ok2

# ---- Route 3: full-size prediction from stored exact value
H8 = 11762187201804552
pred8 = 6 * ((10**8 + 1) // 2 % 2)
print("Route 3: H(10^8) mod 12 = %d, predicted = 6*((10^8+1)//2 mod 2) = %d, "
      "match: %s" % (H8 % 12, pred8, H8 % 12 == pred8))
assert H8 % 12 == pred8 == 0

# residue pattern for n = 2..9 and a mid-range block, printed from Route-1 H
print("H mod 12 for n=2..9:", (H[1:9] % 12).tolist(), "(expect [6,0,0,6,6,0,0,6])")
print("H mod 12 for n=99997..100000:", (H[99996:100000] % 12).tolist(),
      "(n=99997,99998,99999,100000 -> n mod 4 = 1,2,3,0 -> 6,6,0,0)")
print("ALL CHECKS PASSED")
