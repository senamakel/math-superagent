"""Verify the residue structure on Phi_p(a^q+1) = ((a^q+1)^p - 1)/a^q.

Conjecture (from data in cassels_descent_probe): when q > p-1 (odd primes
p != q), the integer q-th root of Phi_p(a^q+1) is exactly b = a^{p-1}, and
Phi_p(a^q+1) = a^{q(p-1)} + [p mod a^q residue]: i.e.
    Phi_p(a^q+1) mod a^q  ==  p mod a^q   (= p when p < a^q)
and Phi_p(a^q+1) is never a perfect q-th power in this range (the Cassels
descent lemma).

We check both exactly, and also the same residue fact for q < p-1 where the
root b is NOT a^{p-1} (to show the clean fact really needs q > p-1).
"""
from math import isqrt

def phi(a, p, q):
    # Phi_p(a^q + 1), exact integer
    x = a**q + 1
    return (x**p - 1) // (x - 1)

def iroot(n, k):
    # integer k-th root (floor), via Newton / binary
    if n < 0:
        return -iroot(-n, k)
    if n < 2:
        return n
    x = 2 ** ((n.bit_length() + k - 1) // k)
    while True:
        y = ((k - 1) * x + n // (x ** (k - 1))) // k
        if y >= x:
            return x
        x = y

fails_const = 0
fails_root = 0
checked_q_gt = 0
checked_q_lt = 0
perf_q = 0
csamp = []

for p in [3, 5, 7, 11, 13, 17, 19]:
    for q in [3, 5, 7, 11, 13, 17, 19, 23]:
        if q == p or q % 2 == 0:
            continue
        for a in range(2, 40):
            v = phi(a, p, q)
            b = iroot(v, q)
            # is it a perfect q-th power?
            if b**q == v:
                perf_q += 1
                print(f"  PERFECT POWER p={p} q={q} a={a}: Phi={v} = {b}^{q}")
            if q > p - 1:
                checked_q_gt += 1
                if b != a**(p-1):
                    fails_root += 1
                    if fails_root <= 10:
                        print(f"  ROOT MISMATCH q>p-1 p={p} q={q} a={a}: b={b} a^(p-1)={a**(p-1)}")
                # residue: gap mod a^q should equal p mod a^q
                gap_mod = (v - (b**q)) % (a**q)
                want = p % (a**q)
                if gap_mod != want:
                    fails_const += 1
                    if fails_const <= 10:
                        print(f"  RESIDUE MISMATCH q>p-1 p={p} q={q} a={a}: gapmod={gap_mod} want={want}")
            else:
                checked_q_lt += 1
                # does the b=a^{p-1} claim FAIL when q < p-1? (expected)
                if b == a**(p-1):
                    csamp.append((p, q, a, b))
                # still record residue for reference
                gap_mod = (v - (b**q)) % (a**q)
                want = p % (a**q)
                if gap_mod != want:
                    if len(csamp) < 12:
                        csamp.append((p, q, a, b))

print(f"\nq > p-1 cases checked: {checked_q_gt}, root-failures: {fails_root}, "
      f"residue-failures: {fails_const}")
print(f"q < p-1 cases checked: {checked_q_lt}")
print(f"perfect q-th powers found (all a>=2): {perf_q}")

# Now push residue check harder: larger a, all odd prime p,q with q>p-1
fails2 = 0
cnt2 = 0
bigperf = 0
for p in [3, 5, 7, 11]:
    for q in [5, 7, 11, 13]:
        if q == p or q <= p-1:
            continue
        for a in range(2, 2000):
            v = phi(a, p, q)
            b = iroot(v, q)
            if b**q == v:
                bigperf += 1
                print(f"  BIG PERFECT POW p={p} q={q} a={a}")
            cnt2 += 1
            if b != a**(p-1):
                fails2 += 1
            if (v - b**q) % (a**q) != p % (a**q):
                fails2 += 1
print(f"\nlarge a (2..1999), q>p-1: cases={cnt2}, failures={fails2}, "
      f"perfect-powers={bigperf}")
