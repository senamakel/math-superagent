"""Growth, oscillation and jump structure of the PE 351 sequences.

Checks over the exact 200000-term prefixes:
 1. H(n)/n^2 -> 3(1-6/pi^2): max deviation of H(n)/n^2 from the constant over
    the second half of the prefix.
 2. A063985(n)/n^2 -> (1/2 - 3/pi^2): same.
 3. Defect D(n) = Phi(n) - (3/pi^2)n^2 changes sign infinitely often:
    count sign changes over the prefix (strong numerical evidence; exact
    theorem is classical).
 4. Largest jumps: H(n) - H(n-1) = 6*(n - phi(n)); max at composite n;
    record the top-5 n and the value of n - phi(n) (exact).
 5. H mod 12 alternates 0 and 6 across consecutive n? (empirical, exact over
    the prefix; not a theorem claim).
"""
import numpy as np

N = 200_000
H = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)
A = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)
Phi = np.loadtxt("code/out/seq_Phi.txt", dtype=np.int64)
phi = np.loadtxt("code/out/seq_phi.txt", dtype=np.int64)

n = np.arange(1, N + 1, dtype=np.int64)

# 1,2: approach of H/n^2 and A/n^2 to their constants
c1 = 3 * (1 - 6 / np.pi ** 2)
c2 = 0.5 - 3 / np.pi ** 2
half = slice(N // 2, N)
print(f"max |H(n)/n^2 - {c1:.10f}| over n in [{N//2},{N}]: "
      f"{np.max(np.abs(H[half] / n[half]**2 - c1)):.3e}")
print(f"max |A(n)/n^2 - {c2:.10f}| over n in [{N//2},{N}]: "
      f"{np.max(np.abs(A[half] / n[half]**2 - c2)):.3e}")

# 3: sign changes of the totient defect
E = (3 / np.pi ** 2) * n ** 2
D = Phi - E
signs = np.sign(D)
changes = int(np.sum(signs[1:] != signs[:-1]))
print(f"totient defect D(n) sign changes over 1..{N}: {changes} "
      f"(last sign: {'+' if signs[-1] > 0 else '-'})")

# 4: jumps of H (exact)
jump = np.diff(H)                 # 6*(n - phi(n)) for n = 2..N
cot = n[1:] - phi[1:]
idx = np.argsort(jump)[-5:][::-1]
print("largest jumps H(n)-H(n-1) = 6*(n-phi(n)):")
for i in idx:
    nn = i + 2
    print(f"  n={nn:6d}  cototient={cot[i]:3d}  jump={jump[i]:4d}  "
          f"is_prime={bool(int(nn) in set(int(p) for p in range(2, int(nn**0.5)+1) if nn % p == 0) or nn == 2) if False else ''}")

# verify jump identity exactly for all n
assert np.array_equal(jump, 6 * cot), "H(n)-H(n-1) != 6(n-phi(n))"
print("jump identity H(n)-H(n-1) = 6(n-phi(n)): exact over all n<=N")

# 5: H mod 12 alternation pattern
r = H % 12
alt = np.array_equal(r[1:], 6 - r[:-1])
print(f"H mod 12 alternates 0,6,0,6,... across consecutive n: {alt}")
if not alt:
    # find first violation
    first = next(i for i in range(len(r) - 1) if r[i + 1] != 6 - r[i])
    print(f"  first violation at n={first + 1}: H={H[first]} (mod 12 = {r[first]}), "
          f"H(n+1)={H[first + 1]} (mod 12 = {r[first + 1]})")
