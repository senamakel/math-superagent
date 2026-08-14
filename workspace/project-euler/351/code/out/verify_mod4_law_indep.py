"""Independent verification of the mod-4 residue law for PE 351 sequences.

Route: naive gcd-based phi (math.gcd), a different code path from the
totient sieve that produced code/out/seq_*.txt.  Checks the law over
n = 2..5000 freshly computed, then applies the law at the target scale
n = 10^8 using the run's verified H(10^8) and A(10^8) values.

Law (derived from phi(k) even for k >= 3, phi(1)=phi(2)=1):
  for every n >= 2,
    A063985(n) odd  iff n mod 4 in {1,2}       (A(n) = C(n+1,2) - Phi(n))
    H(n) mod 12 == 6 iff n mod 4 in {1,2}, else 0   (H(n) = 6 A(n))

Also: bounded negative checks that no exact period <= 1000 exists for
A(n) mod 4 or H(n) mod 24 from n = 2 (i.e. the mod-2 law does not lift to
mod 4 / mod 24; expected, since Phi(n) mod 4 has no closed periodic form).
"""
from math import gcd
import numpy as np

N = 5000
# naive phi
phi = np.zeros(N + 1, dtype=np.int64)
for k in range(1, N + 1):
    phi[k] = sum(1 for d in range(1, k + 1) if gcd(d, k) == 1)
Phi = np.cumsum(phi)                       # Phi(n), n = 0..N
A = np.arange(N + 1, dtype=np.int64) * (np.arange(N + 1, dtype=np.int64) + 1) // 2 - Phi
n = np.arange(1, N + 1, dtype=np.int64)

pred_odd = np.isin(n % 4, [1, 2])
ok1 = np.array_equal((A[2:] % 2) == 1, pred_odd[1:])     # n = 2..N
H = 6 * A
ok2 = np.array_equal(H[2:] % 12 == 6, pred_odd[1:])
print(f"independent (gcd-based): A(n) odd iff n mod 4 in {{1,2}} for n=2..{N}: {bool(ok1)}")
print(f"independent (gcd-based): H(n) mod 12 == 6 iff n mod 4 in {{1,2}} for n=2..{N}: {bool(ok2)}")
print(f"exception set (n where A(n) odd != C(n+1,2) odd, n=1..{N}):",
      np.nonzero((A % 2) != ((np.arange(N + 1) * (np.arange(N + 1) + 1) // 2) % 2))[0].tolist())

# at the target scale
n8 = 10**8
A8 = 1960364533634092
H8 = 11762187201804552
print(f"\ntarget scale: n = {n8} == {n8 % 4} (mod 4); law predicts A even, H mod 12 = 0")
print(f"  A(10^8) mod 2 = {A8 % 2}  (predicted 0)  match: {A8 % 2 == 0}")
print(f"  H(10^8) mod 12 = {H8 % 12}  (predicted 0)  match: {H8 % 12 == 0}")
print(f"  H(10^8) divisible by 12: {H8 % 12 == 0}")

# bounded negative checks: no period <= 1000 for A mod 4 or H mod 24 from n=2
A_big = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)
H_big = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)
for name, seq in (("A mod 4", A_big % 4), ("H mod 24", H_big % 24)):
    s = seq[1:]  # n = 2..N
    period = None
    for p in range(1, 1001):
        if np.array_equal(s[:-p], s[p:]):
            period = p
            break
    print(f"smallest exact period of {name} from n=2 over 200000 terms: "
          f"{period if period else 'none <= 1000'}")
