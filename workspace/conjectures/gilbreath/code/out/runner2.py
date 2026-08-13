from lib.gilbreath import primes_up_to, rows_generator
import random, itertools

def build(seq):
    A = [list(seq)]
    while len(A[-1]) > 2:
        A.append([abs(A[-1][i] - A[-1][i + 1]) for i in range(len(A[-1]) - 1)])
    return A

random.seed(42)
fails = 0
for _ in range(3000):
    n = random.randint(5, 14)
    seq = [2] + [random.choice([3,5,7,9,11,13,15,17,19]) for _ in range(n - 1)]
    A = build(seq); A1 = A[1]; ok = True
    for k in range(2, len(A)):
        row = A[k]
        for i in range(1, len(row)):
            lo = i - 1; hi = lo + k - 1
            if hi >= len(A1): break
            w = A1[lo:hi + 1]
            if row[i] > max(w) - min(w): ok = False
    if not ok: fails += 1
print("C1 universality 3000 random arrays: failures =", fails)

def T_bits(x): return [x[i] ^ x[i+1] for i in range(len(x)-1)]
def phi_c(x, c): return max(x[i] + c[i] for i in range(len(x)))

found = None
for n in [2,3,4]:
    for c in itertools.product(range(-2,3), repeat=n):
        monotone = True
        for x in itertools.product([0,1], repeat=n):
            y = T_bits(x)
            if phi_c(y, c[:len(y)]) > phi_c(x, c):
                monotone = False; break
        if monotone:
            found = (n, c); break
    if found: break
print("C3 max-plus affine c on {0,1} interior: candidate found?", found)
