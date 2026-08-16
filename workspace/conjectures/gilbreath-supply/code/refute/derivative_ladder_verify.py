"""Verify the derivative-ladder identities (L1)-(L5) against brute submask-XOR.

These are the load-bearing identities of the adopted approach
`derivative-ladder-delta-commutation`. No number theory is used; this is
pure F2 bookkeeping. Prints PASS/FAIL per identity and shows a negative control.
"""
import sys

def T(h, n, d):
    """Fold cell T(n,d) = XOR_{o submask of d} h[n-1-d+o]."""
    acc = 0
    for o in range(d + 1):
        if (o & d) == o:            # o is a bitwise submask of d
            idx = n - 1 - d + o
            if 0 <= idx < len(h):
                acc ^= h[idx]
    return acc

def delta(h, k):
    """Delta^k h over F2, Delta = 1 + sigma (left shift)."""
    out = h[:]
    for _ in range(k):
        out = [ (out[j] ^ (out[j+1] if j+1 < len(out) else 0)) for j in range(len(out)) ]
    return out

def check(cond, name, detail=""):
    print(("PASS" if cond else "FAIL"), name, detail)
    return cond

ok = True

# --- (L1): T_{Delta^k h}(n,d) = T(n+k, d+k), for all n<=N, d in [2,n-1], k in {1,2,4}
N = 200
allpass = True
for k in (1, 2, 4):
    for n in range(3, N+1):
        # use a fixed pseudo-random-ish deterministic h long enough
        h = [( (j*7 + j*j) >> 3 ) & 1 for j in range(n + k + 5)]
        dh = delta(h, k)
        for d in range(2, n):
            lhs = T(dh, n, d)
            rhs = T(h, n + k, d + k)
            if lhs != rhs:
                allpass = False
                print("FAIL L1", k, n, d, lhs, rhs)
                break
        if not allpass: break
    ok &= check(allpass, f"L1 k={k} (T_{'{Delta'}^k h}(n,d) = T(n+k,d+k), n<=200)")
    if not allpass: break

# --- (L4): anti-Pascal T(n+1,d) = T(n,d) xor T(n+1,d+1)
allpass = True
for n in range(3, N):
    h = [( (j*11 + 3) >> 2 ) & 1 for j in range(n + 3)]
    for d in range(2, n):
        lhs = T(h, n+1, d)
        rhs = T(h, n, d) ^ T(h, n+1, d+1)
        if lhs != rhs:
            allpass = False
            print("FAIL L4", n, d, lhs, rhs)
            break
    if not allpass: break
ok &= check(allpass, "L4 anti-Pascal T(n+1,d)=T(n,d)^T(n+1,d+1)")

# --- (L2): nu2(n+1) = wt(Phi_n Dh) + (h[n-2] ^ h[n]), using the excess form
# nu2 = (n-2 - S)/2 with S = sum_{d=2}^{n-1} (-1)^{T(n,d)}; verify on the excess directly.
def S_of(h, n):
    return sum((-1) ** T(h, n, d) for d in range(2, n))

def nu2(h, n):
    return (n - 2 - S_of(h, n)) // 2

allpass = True
for n in range(3, N):
    h = [( (j*13 + 5) >> 1 ) & 1 for j in range(n + 2)]
    dh = delta(h, 1)
    # wt(Phi_n Dh) = nu2(Dh, n)
    lhs = nu2(h, n+1)
    rhs = nu2(dh, n) + (h[n-2] ^ h[n])
    if lhs != rhs:
        allpass = False
        print("FAIL L2", n, lhs, rhs)
        break
ok &= check(allpass, "L2 nu2(n+1) = wt(Phi_n Dh) + (h[n-2]^h[n])")

# --- (L3): nu2(n+k) = wt(Phi_n Delta^k h) + #{d in [2,k+1]: T(n+k,d)=1}
allpass = True
for k in (1, 2, 4):
    for n in range(3, N):
        h = [( (j*17 + 7) >> 3 ) & 1 for j in range(n + k + 3)]
        dh = delta(h, k)
        lhs = nu2(h, n + k)
        rhs = nu2(dh, n) + sum(T(h, n+k, d) for d in range(2, k+2))
        if lhs != rhs:
            allpass = False
            print("FAIL L3", k, n, lhs, rhs)
            break
    if not allpass: break
ok &= check(allpass, "L3 nu2(n+k) = wt(Phi_n Delta^k h) + #{d in [2,k+1]: T(n+k,d)=1}")

# --- (L5): Dh[j] = [q_j != q_{j+2} mod 4] on the literal prime residues
primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
r = [p % 4 for p in primes]
h = [1 if r[j] != r[j+1] else 0 for j in range(len(r)-1)]
dh = delta(h, 1)
target = [1 if r[j] != r[j+2] else 0 for j in range(len(r)-2)]
ok &= check(dh[:len(target)] == target, "L5 Dh[j] = [q_j != q_{j+2} mod 4] on primes")

# --- negative control: the REFUTED substitution rule T(2n,2d)=T(n,d) must FAIL
h = [0,0,0,1]
neg = (T(h,4,2) == T(h,2,1))   # must be False
ok &= check(not neg, "negative control: T(2n,2d)=T(n,d) fails (should FAIL, i.e. this is False)")

print("\nALL PASS" if ok else "\nSOME FAILED")
sys.exit(0 if ok else 1)
