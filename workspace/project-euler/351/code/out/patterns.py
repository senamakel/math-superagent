"""Pattern extraction for PE 351 (hexagonal orchard hidden points).

Computes exact integer sequences from the closed-form identity
    H(n) = 3n(n+1) - 6*Phi(n) = 6*A063985(n),  Phi(n) = sum_{k<=n} phi(k),
over a long prefix via an O(N log log N) totient sieve (exact ints):

  seq_H        : H(n), n = 1..N                 (OEIS A216453)
  seq_A063985  : A063985(n) = n(n+1)/2 - Phi(n) (OEIS A063985)
  seq_cototient: c(k) = k - phi(k), k = 1..N    (OEIS A051953)
  seq_phi      : phi(k), k = 1..N               (OEIS A000010)
  seq_Phi      : Phi(n), n = 1..N               (OEIS A002088)

Checks performed:
  1. H(n) == 6*A063985(n) and H(n) % 6 == 0 for every n <= N.
  2. The order-4 recurrence found by find_linear_recurrence on the first 8
     terms, a(n) = (-13/7)a(n-1) + (23/7)a(n-2) + (41/7)a(n-3) + (-46/7)a(n-4),
     is evaluated at n = 9 (the first term that can falsify it).
  3. A063985(n) == Chai Wah Wu's O(sqrt n) recursion (OEIS A063985, the
     'totient-sum-fast-recursion' claim) at a list of probe values, including
     10^8 if affordable.  This is an independent route to Phi(10^8) and hence
     H(10^8) = 6*A063985(10^8).
  4. Growth: H(n)/n^2 at N vs the OEIS asymptotic (3*(1 - 6/pi^2)).
"""

import sys
from functools import lru_cache
import numpy as np

N_DEFAULT = 200_000


def phi_sieve(N):
    """Return numpy int32 array phi[0..N] with phi[k] = Euler phi(k)."""
    phi = np.arange(N + 1, dtype=np.int64)
    phi[0] = 0
    for p in range(2, N + 1):
        if phi[p] == p:  # p is prime
            phi[p::p] -= phi[p::p] // p
    return phi


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else N_DEFAULT
    phi = phi_sieve(N)
    cot = phi[1:N + 1].copy()
    cot = np.arange(1, N + 1, dtype=np.int64) - cot  # c(k) = k - phi(k)

    # prefix sums
    Phi = np.zeros(N + 1, dtype=np.int64)
    np.cumsum(phi[:N + 1], out=Phi)
    A = np.zeros(N + 1, dtype=np.int64)          # A063985(n)
    A[1:] = np.cumsum(cot)
    H = 6 * A[1:]                                # H(n) = 6*A063985(n), n=1..N
    H_direct = 3 * np.arange(1, N + 1, dtype=np.int64) * (
        np.arange(1, N + 1, dtype=np.int64) + 1) - 6 * Phi[1:N + 1]
    assert np.array_equal(H, H_direct), "H identity violated"

    print(f"N = {N}")
    print("H(1..30) =", H[:30].tolist())
    print("A063985(1..30) =", A[1:31].tolist())
    print("cototient(1..30) =", cot[:30].tolist())
    print("all H(n) divisible by 6:", bool(np.all(H % 6 == 0)))
    print("max |H(n) - 6*A063985(n)| over n<=N:",
          int(np.max(np.abs(H - 6 * A[1:]))))

    # Check 2: the spurious order-4 recurrence at n = 9 (first falsifying term)
    t = [0, 6, 12, 24, 30, 54, 60, 84]  # H(1..8)
    rec9 = (-13 * t[7] + 23 * t[6] + 41 * t[5] - 46 * t[4]) / 7
    print(f"order-4 recurrence prediction for H(9): {rec9!r}  actual H(9) = {int(H[8])}")
    print("order-4 recurrence survives at n=9:", rec9 == int(H[8]))

    # Check 4: growth ratio
    print("H(N)/N^2 =", float(H[N - 1]) / N / N,
          " asymptotic 3*(1-6/pi^2) =", 3 * (1 - 6 / np.pi ** 2))

    # save sequences
    np.savetxt("code/out/seq_H.txt", H, fmt="%d")
    np.savetxt("code/out/seq_A063985.txt", A[1:], fmt="%d")
    np.savetxt("code/out/seq_cototient.txt", cot, fmt="%d")
    np.savetxt("code/out/seq_phi.txt", phi[1:], fmt="%d")
    np.savetxt("code/out/seq_Phi.txt", Phi[1:], fmt="%d")

    # Check 3: Chai Wah Wu recursion, independent route to Phi(10^8)
    @lru_cache(maxsize=None)
    def A063985_rec(n):
        if n == 0:
            return 0
        c, j = 0, 2
        k1 = n // j
        while k1 > 1:
            j2 = n // k1 + 1
            c += (j2 - j) * (k1 * (k1 + 1) - 2 * A063985_rec(k1) - 1)
            j, k1 = j2, n // j2
        return (2 * n + c - j) // 2

    probes = [10, 100, 1000, 10_000, 100_000, 1_000_000]
    ok = True
    for p in probes:
        if p <= N:
            rec = A063985_rec(p)
            good = rec == int(A[p])
            ok = ok and good
            print(f"A063985_rec({p}) = {rec}  sieve = {int(A[p])}  MATCH={good}")
    if ok:
        print("recursion matches the sieve at every probe <= N")

    # The final-value probes (only if they complete quickly)
    for p in (10_000_000, 100_000_000):
        rec = A063985_rec(p)
        Phi_p = p * (p + 1) // 2 - rec
        print(f"A063985_rec({p}) = {rec};  Phi({p}) = {Phi_p};  H({p}) = {6 * rec}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
