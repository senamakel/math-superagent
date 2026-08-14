"""Exhaustive checks of the residue identity behind the block structure.

Claim being tested (conjecture; the mechanism of the block decomposition):
  for 1 <= d <= 9, 1 <= k <= d-1, m >= 1, and EVERY 0 <= x < 10^m,
      f(k*10^m + x, d) - f(x, d)  ==  k * m * 10^(m-1).
  (At m = 10 the increment is exactly k*10^10, so fixed points of f(n,d)=n
  are preserved by the translation x -> k*10^10 + x, k = 0..d-1.)

Three independent evaluations, no random sampling for the small sizes:
  (E1) m = 1,2,3 EXHAUSTIVE over every x in [0,10^m), all d=1..9, all k<=d-1,
       using a raw string-counting f (definition-level, no closed form).
  (E2) m = 4 EXHAUSTIVE over every x in [0,10^4) using the place-value
       closed form (agreeing with strings on all n<=20000, verified earlier).
  (E3) m = 5..12 sampled (3000 random x per (d,k)) with the closed form,
       plus a workload cap so the run stays small.

Also checks the CONTROLLED BREAK at k = d:
  f(d*10^10 + x, d) - f(x, d) - d*10^10 == x + 1  for sampled x
(this is what makes n >= d*10^10 have f(n,d) > n, closing the bound).
"""
import random

def f_naive(n, d):
    return sum(str(i).count(str(d)) for i in range(n + 1))

def f_place_value(n, d):
    total = 0
    factor = 1
    while factor <= n:
        low = n % factor
        cur = (n // factor) % 10
        high = n // (factor * 10)
        if cur < d:
            total += high * factor
        elif cur == d:
            total += high * factor + low + 1
        else:
            total += (high + 1) * factor
        factor *= 10
    return total

fails = []
checked = 0

# E1: exhaustive, string-counting
for m in (1, 2, 3):
    for d in range(1, 10):
        for k in range(1, d):
            for x in range(10**m):
                n = k * 10**m + x
                lhs = f_naive(n, d) - f_naive(x, d)
                pred = k * m * 10**(m-1)
                checked += 1
                if lhs != pred:
                    fails.append(("E1", m, d, k, x, lhs, pred))
                    if len(fails) > 5: break
            if len(fails) > 5: break
        if len(fails) > 5: break
    if len(fails) > 5: break
print(f"E1 exhaustive string-counting f, m=1..3 (every x): checked={checked} holds={not fails}")

# E2: exhaustive, m=4, closed form
for d in range(1, 10):
    for k in range(1, d):
        for x in range(10**4):
            n = k * 10**4 + x
            lhs = f_place_value(n, d) - f_place_value(x, d)
            pred = k * 4 * 10**3
            checked += 1
            if lhs != pred:
                fails.append(("E2", 4, d, k, x, lhs, pred))
                if len(fails) > 5: break
        if len(fails) > 5: break
    if len(fails) > 5: break
print(f"E2 exhaustive closed form, m=4 (every x): checked={checked} holds={not fails}")

# E3: sampled, m=5..12, closed form
random.seed(2026)
for m in range(5, 13):
    for d in range(1, 10):
        for k in range(1, d):
            for _ in range(3000):
                x = random.randrange(0, 10**m)
                n = k * 10**m + x
                lhs = f_place_value(n, d) - f_place_value(x, d)
                pred = k * m * 10**(m-1)
                checked += 1
                if lhs != pred:
                    fails.append(("E3", m, d, k, x, lhs, pred))
                    if len(fails) > 5: break
            if len(fails) > 5: break
        if len(fails) > 5: break
    if len(fails) > 5: break
print(f"E3 sampled closed form, m=5..12 (3000 x per (d,k)): holds={not fails}")

print(f"\nTOTAL residue-identity checks: {checked}; failures: {len(fails)}")
for f_ in fails[:8]:
    print("  FAIL", f_)

# controlled break at k = d, m = 10
print("\nControlled break at k=d, m=10:  f(d*10^10+x,d)-f(x,d)-d*10^10 == x+1 ?")
random.seed(9)
bad = 0
for d in range(1, 10):
    for _ in range(200):
        x = random.randrange(0, 10**10)
        n = d * 10**10 + x
        lhs = f_place_value(n, d) - f_place_value(x, d) - d * 10**10
        if lhs != x + 1:
            bad += 1
            print(f"  BREAK-FAIL d={d} x={x} lhs={lhs} x+1={x+1}")
            break
    if bad: break
print(f"  break identity holds on 200 sampled x per d: {bad == 0}")