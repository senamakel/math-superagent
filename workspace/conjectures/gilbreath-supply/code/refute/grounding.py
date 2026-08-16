#!/usr/bin/env python3
import random
from lib.supply_fold import s_sos, s_direct
from lib.primes import prime_gap_parity

def nu2_direct(n, h):
    c = 0
    for d in range(2, n):
        x = 0
        for o in range(d+1):
            if (o & d) == o:
                x ^= h[n-1-d+o]
        c += x
    return c

hprime = prime_gap_parity(300)
print("== primes: nu2 via s_sos vs nu2_direct vs s_direct ==")
for n in [53, 64, 100, 200, 300]:
    S, ones_sos = s_sos(n, hprime[:n])
    d_ = nu2_direct(n, hprime)
    Sd, ones_d = s_direct(n, hprime)
    ident = (2*ones_sos-(n-2)) == -S
    print(f"n={n}: nu2_sos={ones_sos} direct={d_} sdirect={ones_d} nu2/n={ones_sos/n:.4f} S={S} 2nu2-(n-2)=-S? {ident}")

print("\n== R-random-pointwise: uniform h Binomial law ==")
def submask_cols(d, n):
    return [n-1-d+o for o in range(d+1) if (o&d)==o and 0 <= n-1-d+o < n]
def wt_image(n, h):
    return sum(1 for d in range(2,n) if sum(h[j] for j in submask_cols(d,n)) % 2)
for n in [8, 16, 32]:
    S_trials = 20000
    mean = 0.0; below = 0
    for _ in range(S_trials):
        h = [random.getrandbits(1) for _ in range(n)]
        w = wt_image(n, h)
        mean += w
        if w < n/4: below += 1
    mean /= S_trials
    print(f"n={n}: mean wt={mean:.3f} pred={(n-2)/2} P(wt<n/4)={below/S_trials:.5f}")

print("\n== sparse-but-growing: 1s at all powers of 2 ==")
def powers_of_two_h(N):
    h = [0]*N; p = 1
    while p < N:
        h[p] = 1; p <<= 1
    return h
for n in [100, 200, 400, 800, 1600]:
    h = powers_of_two_h(n)
    ones = sum(h)
    S, ones_sos = s_sos(n, h)
    print(f"n={n}: ones={ones} density={ones/n:.4f} nu2={ones_sos} nu2/n={ones_sos/n:.4f}")
