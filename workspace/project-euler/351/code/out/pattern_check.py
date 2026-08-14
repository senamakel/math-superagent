"""Pattern checks on the PE 351 sequences produced by patterns.py.

Reads the computed sequences from disk (200000 terms each), verifies the
oracle values and the exact identities, and prints the first 40 terms of each
sequence for feeding the sequence tools.  Exact integer arithmetic throughout.
"""
import numpy as np

H = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)         # H(n), n=1..N
A = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)   # A063985(n), n=1..N
P = np.loadtxt("code/out/seq_Phi.txt", dtype=np.int64)       # Phi(n), n=1..N
c = np.loadtxt("code/out/seq_cototient.txt", dtype=np.int64) # c(k)=k-phi(k), k=1..N
N = len(H)
n = np.arange(1, N + 1, dtype=np.int64)

# --- oracles from the statement ---
assert H[4] == 30, H[4]
assert H[9] == 138, H[9]
assert H[999] == 1177848, H[999]
print("oracles H(5)=30, H(10)=138, H(1000)=1177848: OK (from seq files)")

# --- exact identities, checked over every one of the N terms ---
assert np.array_equal(H, 6 * A), "H = 6*A063985 violated"
print("H(n) == 6*A063985(n) for all n <= %d: OK" % N)
assert np.array_equal(H, 3 * n * (n + 1) - 6 * P), "H = 3n(n+1) - 6*Phi violated"
print("H(n) == 3n(n+1) - 6*Phi(n) for all n <= %d: OK" % N)
assert np.array_equal(np.diff(A, prepend=0), c), "A differences != cototient"
assert np.array_equal(np.diff(H, prepend=0), 6 * c), "H differences != 6*cototient"
print("dH(n) = H(n)-H(n-1) == 6*(n - phi(n)) for all n <= %d: OK" % N)

# --- c(k) == 1 iff k prime, by a sieve over all k <= N ---
isprime = np.ones(N + 1, dtype=bool)
isprime[:2] = False
for p in range(2, int(N ** 0.5) + 1):
    if isprime[p]:
        isprime[p * p::p] = False
prime1 = (c == 1)
assert np.array_equal(prime1, isprime[1:]), "c(k)==1 iff k prime violated"
print("c(k) == 1 iff k prime, for all k <= %d: OK" % N)

# --- mod-12 pattern: H(n) = 6*ceil(n/2) (mod 12) for n >= 2 ---
# derived from: phi(k) even for k>=3, c(1)=0, c(2)=1  =>
#   A063985(n) mod 2 = 1 + floor((n-1)/2) mod 2  =>  period 4 from n=2.
pred = np.zeros(N, dtype=np.int64)
pred[1:] = 6 * (((n[1:] + 1) // 2) % 2)          # n >= 2
assert np.array_equal(H % 12, pred), "mod-12 period-4 pattern violated"
print("H(n) mod 12 == 6*((n+1)//2 mod 2) for all 2 <= n <= %d: OK" % N)
print("residue pattern (n=2..9):", (H[1:9] % 12).tolist(), "(expect 6,0,0,6,6,0,0,6)")

# --- growth ratios at N ---
print("H(N)/N^2 = %.10f   asymptotic 3*(1-6/pi^2) = %.10f" %
      (H[-1] / N ** 2, 3 * (1 - 6 / np.pi ** 2)))
print("Phi(N)/N^2 = %.10f   asymptotic 3/pi^2 = %.10f" %
      (P[-1] / N ** 2, 3 / np.pi ** 2))

# --- first 40 terms for the sequence tools ---
for name, seq in (("H", H), ("A063985", A), ("Phi", P), ("cototient", c)):
    print(name + ":", ", ".join(map(str, seq[:40].tolist())))
