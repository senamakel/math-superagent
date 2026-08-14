"""Exact verification of the derived mod-4 residue law for the PE 351
sequences, over the full 200000-term prefix on disk.

Derived facts to check (each follows from phi(k) even for k >= 3, phi(1)=phi(2)=1,
so Phi(n) = sum_{k<=n} phi(k) is even for every n >= 2):
  L1. A063985(n) mod 2 == C(n+1,2) mod 2          for all n >= 2
      i.e. A063985(n) is odd  iff  n mod 4 in {1, 2}
  L2. A063985(n+4) == A063985(n) (mod 2)          for all n >= 2
  L3. H(n) mod 12 == 6 iff n mod 4 in {1, 2}      for all n >= 2
      (H(n) mod 12 == 0 iff n mod 4 in {0, 3})
  L4. cototient c(k) = k - phi(k): for k >= 3, c(k) is odd iff k is odd
      (phi(k) even for k >= 3).  Boundary anomalies: c(1) = 0 even (odd k),
      c(2) = 1 odd (even k) because phi(2) = 1 is the unique odd phi-value
      among k >= 2.
  L5. the single exception is n = 1: A063985(1)=0 is even though 1 == 1 (mod 4).

Also counts, for the record: how many n <= N violate each law (must be 0
apart from the explicitly listed exceptions), and confirms the run's
growth_checks "alternation False at n=3" is exactly the period-4 law.
"""
import numpy as np

N = 200_000
A = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)      # A(1..N)
H = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)            # H(1..N)
Phi = np.loadtxt("code/out/seq_Phi.txt", dtype=np.int64)        # Phi(1..N)
phi = np.loadtxt("code/out/seq_phi.txt", dtype=np.int64)        # phi(1..N)
c = np.arange(1, N + 1, dtype=np.int64) - phi                   # cototient
n = np.arange(1, N + 1, dtype=np.int64)

# Phi(n) even for n >= 2
even_ok = np.all(Phi[1:] % 2 == 0)           # Phi(2..N)
print(f"Phi(n) even for all 2 <= n <= {N}: {bool(even_ok)}")

# L1: A063985(n) mod 2 == C(n+1,2) mod 2  for n >= 2
tri = (n * (n + 1) // 2) % 2
l1 = np.array_equal(A[1:] % 2, tri[1:])      # indices 1..N-1 => n=2..N
print(f"L1: A(n) mod 2 == C(n+1,2) mod 2 for n=2..{N}: {bool(l1)}")

# L1b: A(n) odd iff n mod 4 in {1,2}  (n >= 2)
odd_pred = np.isin(n % 4, [1, 2])
l1b = np.array_equal((A % 2).astype(bool)[1:], odd_pred[1:])
print(f"L1b: A(n) odd iff n mod 4 in {{1,2}}, n=2..{N}: {bool(l1b)}")

# L2: period 4 from n=2: A(n+4) == A(n) mod 2 for all 2 <= n <= N-4
l2 = np.all((A[5:N-1] % 2) == (A[1:N-5] % 2))  # A(n+4) vs A(n), n=2..N-4
print(f"L2: A(n) mod 2 period 4 for n=2..{N-4}: {bool(l2)}")

# L3: H(n) mod 12 == 6 iff n mod 4 in {1,2}  (n >= 2)
l3 = np.array_equal((H % 12 == 6)[1:], odd_pred[1:])
residues = sorted(set((H % 12).tolist()))
print(f"L3: H(n) mod 12 == 6 iff n mod 4 in {{1,2}}, n=2..{N}: {bool(l3)}; "
      f"H mod 12 residues over n=2..N: {residues}")

# L4: c(k) odd iff k odd for k >= 3 (c(1), c(2) are the boundary anomalies)
l4 = np.array_equal((c % 2 == 1)[2:], (n[2:] % 2 == 1))
print(f"L4: c(k) odd iff k odd, k=3..{N}: {bool(l4)}")
print(f"    c(1) = {c[0]} (even at odd k), c(2) = {c[1]} (odd at even k): "
      f"the two boundary anomalies, from phi(1)=phi(2)=1")

# L5: exceptions: n=1 only
ex = np.nonzero((A % 2) != (tri % 2))[0] + 1   # n where L1 would fail
print(f"L5: n violating the parity law: {ex.tolist()}  "
      f"(A(1)={A[0]}, C(2,2) mod 2 = {tri[0]})")

# The run's growth_checks observation: 'H mod 12 alternates 0,6,0,6' is False,
# first violation at n=3.  Show the true period-4 pattern from n=2:
print("pattern H(n) mod 12, n=2..9:", ((H[1:9] % 12).tolist()))
print("pattern A(n) mod 2,   n=2..9:", ((A[1:9] % 2).tolist()))
print("expected (period 4):         ", [6, 0, 0, 6, 6, 0, 0, 6])
print("expected A mod 2:            ", [1, 0, 0, 1, 1, 0, 0, 1])
