"""Verify the incremental base-3 digit counter against direct count.
Compare parity-counts over n=1..200 both ways."""
import sys

def direct_counts(N):
    a0 = a2 = 0
    for n in range(1, N+1):
        m = 2**n
        c0 = c1 = c2 = 0
        while m > 0:
            d = m % 3
            if d == 0: c0 += 1
            elif d == 1: c1 += 1
            else: c2 += 1
            m //= 3
        assert c1 % 2 == 0
        if c0 % 2: a0 += 1
        if c2 % 2: a2 += 1
    return a0, a2

N = 200
da0, da2 = direct_counts(N)

# incremental
digits = [1]
a0 = a2 = 0
for n in range(1, N+1):
    carry = 0
    for i in range(len(digits)):
        v = digits[i]*2 + carry
        digits[i] = v % 3
        carry = v // 3
    while carry:
        digits.append(carry % 3); carry //= 3
    c0 = c1 = c2 = 0
    for d in digits:
        if d == 0: c0 += 1
        elif d == 1: c1 += 1
        else: c2 += 1
    if c0 % 2: a0 += 1
    if c2 % 2: a2 += 1

print("direct:", da0, da2, " incremental:", a0, a2, " match:", (da0,da2)==(a0,a2))
