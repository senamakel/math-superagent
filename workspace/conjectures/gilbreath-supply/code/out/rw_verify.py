"""Oracle check of Rampersad-Wiebe: sums of C(a1n+a2k,a3n+a4k)*C(n,k) mod 2
equal the run-length transform of a linear-recurrence sequence S.

Run-length transform: T(n) = product over maximal runs of 1s in bin(n), lengths L, of S(L).
Verify against Theorem 5 (Fibonacci) and Theorem 9 (positive integers).
Also check the SUBMASK-XOR transform used in SUPPLY's fold Phi: the map
T(d) = XOR over i submask of d of h(i) is an invertible F2-linear map (zeta/Mobius).
"""
from math import comb, gcd

def binom_mod2(n, k):
    if k < 0 or k > n:
        return 0
    return comb(n, k) % 2

def sum_T(n, a1, a2, a3, a4):
    """T(n) = sum_{k=0..n} [ C(a1n+a2k, a3n+a4k) * C(n,k) mod 2 ]  (0/1 sum)."""
    s = 0
    for k in range(n + 1):
        N = a1 * n + a2 * k
        K = a3 * n + a4 * k
        if N < K:          # binomial zero
            continue
        if binom_mod2(N, K) and binom_mod2(n, k):
            s += 1
    return s

def runs_of_ones(n):
    b = bin(n)[2:]
    runs = []
    cur = 0
    for c in b:
        if c == '1':
            cur += 1
        else:
            if cur:
                runs.append(cur)
                cur = 0
    if cur:
        runs.append(cur)
    return runs

def runlen_transform(n, S):
    """T(n)=product of S(L) over runs of 1s; here the sequences take values in Z,
    so it's a PRODUCT, not a sum.  (Paper's Def 1 uses 'sum' but it means S(i) as
    a product over the runs.)"""
    p = 1
    for L in runs_of_ones(n):
        p *= S[L]
    return p

def fib_seq(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def posint_seq(n):
    return list(range(1, n + 1))

# Theorem 5: (1,-1,0,2), Fibonacci run-length transform
print("== Theorem 5: Fibonacci run-length transform ==")
Fib = {i: v for i, v in enumerate(fib_seq(20))}
ok = True
for n in range(1, 20):
    Tn = sum_T(n, 1, -1, 0, 2)
    RLT = runlen_transform(n, Fib)
    status = "OK" if Tn == RLT else "MISMATCH"
    if Tn != RLT:
        ok = False
    print(f"n={n:2d} sumT={Tn} runlen={RLT} {status}")
print("Theorem5 all match:", ok)

# Theorem 9: (1,1,1,-1), run-length transform of the positive integers.
# Paper statement: T(n) = sum_k [ C(n+k, n-k) * C(n,k) mod 2 ], and the proof
# gives the sequence by S(0)=1, S(1)=2, S(n)=2S(n-1)-S(n-2)  =>  S(L) = L+1.
# An earlier version of this checker used S(L)=L, which mismatched for every n;
# that wrong choice is kept below as the negative control.
print("\n== Theorem 9: positive integers run-length transform ==")
ok9 = True
ok9_wrong = True   # negative control: the pre-fix S(L)=L reading
for n in range(1, 20):
    Tn = sum_T(n, 1, 1, 1, -1)
    RLT_correct = runlen_transform(n, {i: i + 1 for i in range(1, 20)})  # S(L)=L+1
    RLT_wrong   = runlen_transform(n, {i: i     for i in range(1, 20)})  # S(L)=L, pre-fix
    if Tn != RLT_correct:
        ok9 = False
        print(f"n={n:2d} sumT={Tn} runlen(S=L+1)={RLT_correct} MISMATCH")
    if Tn == RLT_wrong:
        ok9_wrong = False   # the wrong reading must NOT match (negative control)
print("Theorem9 all match with S(L)=L+1:", ok9)
print("Negative control (S(L)=L must fail):", ok9_wrong)

# SUBMASK-XOR transform: T(d)=XOR_{i submask d} h(i).  Check invertibility (zeta/Mobius).
print("\n== SUPPLY fold Phi: submask-XOR transform invertibility ==")
def submasks(d):
    i = d
    while True:
        yield i
        if i == 0:
            break
        i = (i - 1) & d

def zeta_xor(h):
    """T(d) = XOR over i submask of d of h(i)."""
    k = len(h)
    T = [0] * k
    for d in range(k):
        x = 0
        for i in submasks(d):
            x ^= h[i]
        T[d] = x
    return T

def mobius_xor(T):
    """Inverse: h(i) = XOR over j submask of i of T(j)."""
    k = len(T)
    h = [0] * k
    for i in range(k):
        x = 0
        for j in submasks(i):
            x ^= T[j]
        h[i] = x
    return h

# random strength check over small grids
import random
random.seed(0)
all_ok = True
for trial in range(50):
    k = random.choice([4, 8, 16, 32])
    h = [random.randint(0, 1) for _ in range(k)]
    T = zeta_xor(h)
    h2 = mobius_xor(T)
    if h2 != h:
        all_ok = False
        print("inversion failed", trial)
        break
print("Zeta (Phi) transform invertible round-trips over 50 random h:", all_ok)

# Weight of Phi_n h compared to weight of h: does dense h give dense T?
print("\n== weight of transform for random dense h (dimension sqrt-ish) ==")
for k in [16, 32, 64]:
    h = [random.randint(0, 1) for _ in range(k)]
    T = zeta_xor(h)
    print(f"k={k:3d} wt(h)={sum(h):3d}/{k}  wt(Phi h)={sum(T):3d}/{k}")
