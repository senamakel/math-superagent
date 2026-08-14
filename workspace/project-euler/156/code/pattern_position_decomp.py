"""Direct check of the per-position decomposition that proves the residue
identity  f(k*10^m+x,d) - f(x,d) = k*m*10^(m-1)  for k <= d-1.

The standard per-position identity for f(n,d): every decimal position i
contributes c_i(n,d) = high*f + (low+1 if cur==d else 0) + f*(1 if cur>d else 0)
where high=n//10^(i+1), cur=(n//10^i)%10, low=n%10^i, f=10^i.

For n = k*10^m + x, k<=d-1, 0<=x<10^m:
  - positions i < m of n equal positions i of x (same digit cur, same low;
    high differs only by the leading k, which is < d so never counts);
  - position i = m has digit k < d, high = 0, low = x:
        c_m(n,d) = 0*f + 0 = 0 for x's own representation, PLUS the count
        from the numbers 0..n themselves at that place: k*m*10^(m-1).
  - positions i > m are all zero digits (n < 10^(m+1)), contribute 0.
So f(n,d) - f(x,d) = k*m*10^(m-1).  Verify the per-position decomposition
exactly on the actual numbers, no sampling for the decisive cases:
  (a) exact enumeration of c_i(n,d) over positions for a range of n covering
      many (m,d,k) with both the closed form and raw string counting;
  (b) verify c_i(n,d) = c_i(x,d) for all i<m by direct position inspection;
  (c) verify c_m(n,d) = k*m*10^(m-1) by raw string counting of the digit d
      at the m-th position (i.e. the count of j in [0,n] whose 10^m place
      digit is d) for exhaustive x at small m, plus sampled at larger m.
"""
import random

def c_position_naive(n, d, i):
    """Count of numbers j in 0..n whose 10^i-place digit equals d (raw)."""
    f = 10**i
    return sum(1 for j in range(n + 1) if (j // f) % 10 == d)

def c_position_formula(n, d, i):
    f = 10**i
    high = n // (f * 10)
    cur = (n // f) % 10
    low = n % f
    if cur < d:
        return high * f
    if cur == d:
        return high * f + low + 1
    return (high + 1) * f

def f_naive(n, d):
    return sum(str(j).count(str(d)) for j in range(n + 1))

# (a) per-position closed form == raw counting, all positions, many n
bad = []
for n in range(0, 60000):
    for d in range(1, 10):
        for i in range(0, 8):
            if 10**i > n: break
            if c_position_formula(n, d, i) != c_position_naive(n, d, i):
                bad.append((n, d, i))
                if len(bad) > 5: break
        if len(bad) > 5: break
    if len(bad) > 5: break
print(f"(a) per-position formula == raw count for n in 0..59999, all d, all positions: {len(bad)==0}")

# (b) position-wise: for i<m, c_i(k*10^m+x,d) == c_i(x,d)  (exhaustive at m<=3, sampled above)
bad_b = []
checked_b = 0
random.seed(5)
for m in range(1, 7):
    for d in range(1, 10):
        for k in range(1, d):
            xs = range(10**m) if m <= 3 else [random.randrange(10**m) for _ in range(3000)]
            for x in xs:
                n = k * 10**m + x
                for i in range(m):
                    lhs = c_position_formula(n, d, i)
                    rhs = c_position_formula(x, d, i)
                    checked_b += 1
                    if lhs != rhs:
                        bad_b.append((m, d, k, x, i, lhs, rhs))
                        if len(bad_b) > 5: break
                if len(bad_b) > 5: break
            if len(bad_b) > 5: break
        if len(bad_b) > 5: break
    if len(bad_b) > 5: break
print(f"(b) positions i<m unchanged by the k*10^m translate: checked={checked_b} holds={len(bad_b)==0}")

# (c) position m: c_m(k*10^m + x, d) == k*m*10^(m-1), raw counting
bad_c = []
checked_c = 0
random.seed(6)
for m in range(1, 5):
    for d in range(1, 10):
        for k in range(1, d):
            xs = range(10**m) if m <= 2 else [random.randrange(10**m) for _ in range(3000)]
            for x in xs:
                n = k * 10**m + x
                got = c_position_naive(n, d, m)
                pred = k * m * 10**(m - 1)
                checked_c += 1
                if got != pred:
                    bad_c.append((m, d, k, x, got, pred))
                    if len(bad_c) > 5: break
            if len(bad_c) > 5: break
        if len(bad_c) > 5: break
    if len(bad_c) > 5: break
# sampled big-m position-m check (formula-based, since raw would be enormous)
random.seed(7)
for m in range(5, 11):
    for d in range(1, 10):
        for k in range(1, d):
            for _ in range(500):
                x = random.randrange(10**m)
                got = c_position_formula(k * 10**m + x, d, m)
                pred = k * m * 10**(m - 1)
                checked_c += 1
                if got != pred:
                    bad_c.append((m, d, k, x, got, pred))
                    if len(bad_c) > 5: break
            if len(bad_c) > 5: break
        if len(bad_c) > 5: break
    if len(bad_c) > 5: break
print(f"(c) position-m contribution == k*m*10^(m-1): checked={checked_c} holds={len(bad_c)==0}")
print("failures:", bad_c[:6])

# (d) positions i > m contribute 0
bad_d = []
for d in range(1, 10):
    for k in range(1, d):
        for x in [0, 1, 12345, 9999999999]:
            n = k * 10**10 + x
            for i in range(11, 14):
                if c_position_formula(n, d, i) != 0:
                    bad_d.append((d, k, x, i))
print(f"(d) positions above m contribute 0 at m=10: {len(bad_d)==0}")

print("\nAll per-position decomposition checks:", (len(bad)==0 and len(bad_b)==0 and len(bad_c)==0 and len(bad_d)==0))