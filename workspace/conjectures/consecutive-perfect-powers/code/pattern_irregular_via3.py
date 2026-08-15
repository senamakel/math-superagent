"""Third independent irregularity route for the double-Wieferich primes,
using the standard modular Bernoulli recurrence with a *diagonal* structure
(no factorial arrays), cross-checked against the two earlier implementations.

For even 2k <= p-3, B_{2k} is p-integral and p | num(B_{2k}) <=> B_{2k}==0 mod p.
"""
import time

def bernoulli_even_via_partial_sums(p):
    """B[n] = -1/(n+1) sum_{k=0}^{n-1} C(n+1,k) B[k]; binomial updated in place
    so C(n+1,k) is used DIRECTLY (no off-by-one)."""
    B = [0] * (p - 1)
    B[0] = 1 % p
    for n in range(1, p - 2):
        # C(n+1,k) for k=0..n
        ck = 1  # C(n+1, 0) = 1
        s = B[0]  # k=0 term, C(n+1,0)*B[0]
        for k in range(1, n):
            ck = ck * (n + 1 - (k - 1)) * pow(k, -1, p) % p   # C(n+1,k) from C(n+1,k-1)
            s = (s + ck * B[k]) % p
        B[n] = (-s * pow(n + 1, -1, p)) % p
    return [2 * k for k in range(1, (p - 1) // 2) if B[2 * k] == 0]

for p in [83, 911, 2903, 4871, 18787]:
    t = time.time()
    idx = bernoulli_even_via_partial_sums(p)
    print(f"p={p}: indices={idx}  regular={idx==[]}  (%.1fs)" % (time.time() - t))
