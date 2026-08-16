"""Fresh pattern probe: is #{n<=N : c0(n) odd} == #{n<=N : c2(n) odd} exact?

c1 even is proved. c0+c1+c2 = L(n); c0 == c2 + L (mod 2). Equal odd-counts
over 1..400 (both 211) is the candidate regularity -- test to large N by
INCREMENTAL base-3 digit counting under multiplication by 2.
"""
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000

# incremental: digits stored least-significant-first, each a count from the
# multiplying by 2 in base 3. We keep the digit list and re-count on change.
digits = [1]          # 2^0 = 1_3, lsb first
c0 = c1 = c2 = 0
for d in digits:
    if d == 0: c0 += 1
    elif d == 1: c1 += 1
    else: c2 += 1

a0 = a2 = 0
max_abs = 0
first_exceed = None
for n in range(1, N+1):
    # multiply digits (lsb first) by 2 in base 3
    carry = 0
    for i in range(len(digits)):
        v = digits[i] * 2 + carry
        digits[i] = v % 3
        carry = v // 3
    while carry:
        digits.append(carry % 3)
        carry //= 3
    # recount
    c0 = c1 = c2 = 0
    for d in digits:
        if d == 0: c0 += 1
        elif d == 1: c1 += 1
        else: c2 += 1
    assert c1 % 2 == 0, f"c1 odd at n={n}"
    L = len(digits)
    assert (c0 - c2 - L) % 2 == 0, f"c0==c2+L mod2 violated at n={n}"
    if c0 % 2: a0 += 1
    if c2 % 2: a2 += 1
    d = a0 - a2
    if abs(d) > max_abs:
        max_abs = abs(d)
    if first_exceed is None and a0 != a2:
        first_exceed = n

print(f"N={N}")
print("#{c0 odd}=", a0, " #{c2 odd}=", a2, " equal:", a0 == a2,
      " first n where counts differ:", first_exceed)
print("max |#c0odd - #c2odd|:", max_abs)
print("final ternary digits of 2^N count:", c0, c1, c2, "len", len(digits))
