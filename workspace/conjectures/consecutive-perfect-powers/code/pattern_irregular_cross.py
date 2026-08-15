"""Independent cross-check of irregularity for 4871 and 18787.
Both implementations use factorial arrays -> true O(p^2), p <= 18787 ~ 3.5e8.
Implementation 1: modular inverse via pow (repeated).
Implementation 2: precomputed inverses + incremental binomial (different structure).
"""
import gmpy2
import time

def _prep(p):
    fact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i - 1] * i % p
    inv_fact = [1] * p
    inv_fact[p - 1] = pow(fact[p - 1], -1, p)
    for i in range(p - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % p
    return fact, inv_fact

def irr_rec1(p):
    fact, inv_fact = _prep(p)
    B = [0] * (p - 1); B[0] = 1
    for n in range(1, p - 2):
        s = 0; nn = n + 1
        for j in range(n):
            c = fact[nn] * inv_fact[j] % p * inv_fact[nn - j] % p
            s = (s + c * B[j]) % p
        B[n] = (-s * pow(nn, -1, p)) % p
    return [2 * k for k in range(1, (p - 1) // 2) if B[2 * k] == 0]

def irr_rec2(p):
    inv = [0] * p
    for i in range(1, p):
        inv[i] = int(gmpy2.invert(i, p))
    B = [0] * (p - 1); B[0] = 1
    for n in range(1, p - 2):
        s = 0; c = 1; nn = n + 1
        for k in range(n):
            s = (s + c * B[k]) % p
            c = c * (nn - k) * inv[k + 1] % p
        B[n] = (-s * inv[nn]) % p
    return [2 * k for k in range(1, (p - 1) // 2) if B[2 * k] == 0]

import sympy as sp
def exact_at(p, kvals):
    return {m: (sp.bernoulli(m).p % p) for m in kvals}

for p in [4871, 18787]:
    t = time.time()
    r1 = irr_rec1(p)
    r2 = irr_rec2(p)
    print(f"p={p}: rec1 indices={r1}  (%.1fs)" % (time.time() - t))
    print(f"p={p}: rec2 indices={r2}")
    print(f"p={p}: AGREE={r1==r2}  REGULAR={r1==[]}")
    if p == 4871:
        vals = exact_at(p, [2, 4, 6, 8, 10, 32, 60, 100])
        print(f"  exact num(B_m)%%p spot-check: {vals}")

for p in [83, 911, 2903]:
    print(f"p={p}: rec1={irr_rec1(p)} rec2={irr_rec2(p)} agree={irr_rec1(p)==irr_rec2(p)}")
