"""Survival-depth on even n: g(m)=f(2m), the first base-3 digit position
(LSB-first) where 2^(2m) shows a digit 2.  For even n, units digit is 1 so
f>=1; f is exactly the sieve survival depth (n survives level k iff f(n)>=k).
Digit-free n (0,2,8) are of the form 2m with m in {0,1,4}; g = inf there.
This is the genuinely interesting subsequence (odd n trivially give f=0).
"""
def f_of_n(n):
    m = 2 ** n
    i = 0
    while m > 0:
        if m % 3 == 2:
            return i
        m //= 3
        i += 1
    return None

N = 800   # even n up to 798 -> m up to 399
evens = []
for m in range(0, N//2):
    n = 2*m
    evens.append(f_of_n(n))
print("=== g(m)=f(2m), m=0..%d ===" % (N//2 - 1))
print(evens)
print()
print("digit-free m (g=inf):", [m for m,v in enumerate(evens) if v is None])
print()
# raw integer sequence, digit-free omitted
raw = [v for v in evens if v is not None]
print("=== raw g(m) sequence, digit-free m omitted, m ascending ===")
print(raw)
print()
# distribution
from collections import Counter
c = Counter(v for v in evens if v is not None)
print("=== g distribution over surviving-m (digit-containing) even n ===")
for k in sorted(c):
    print(f"g={k}: {c[k]}")
