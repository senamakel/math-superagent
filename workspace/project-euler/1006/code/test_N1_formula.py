import math

def S(n):
    a, b = "0", "01"
    if n == 0: return a
    if n == 1: return b
    for _ in range(2, n+1):
        a, b = b, b + a
    return b

def word_len(n):
    a, b = 1, 2
    if n == 0: return a
    if n == 1: return b
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

K = 2000
n = 0
while word_len(n) < 3*(K+1):
    n += 1
word = S(n)

# N1(k) = number of length-(k+1) factors ending in 1
# Use rational approximation for alpha = 1/phi^2 = (3-sqrt5)/2
# compare against ceil((k+1)*alpha) via exact integer: ceil(x) = floor(x-1)+1...
# ceil(a/b) for rational. alpha is irrational; but "ceil((k+1)*alpha)".
# We can test the pattern: N1(k) in {floor((k+1)*alpha), floor((k+1)*alpha)+1, ...}
# Let's just compare with round and ceil computed in high precision.

from decimal import Decimal, getcontext
getcontext().prec = 60
alpha = (Decimal(3) - Decimal(5).sqrt())/2
fail_ceil = []
fail_floor = []
fail_round = []
for L in range(2, K+2):
    subs = {word[i:i+L] for i in range(len(word)-L+1)}
    e = sum(1 for s in subs if s[-1]=='1')
    k = L-1
    x = Decimal(L)*alpha
    ce = (x).to_integral_value(rounding='ROUND_CEILING')  # Math.ceil(L*alpha)
    fl = x.to_integral_value(rounding='ROUND_FLOOR')
    rn = x.to_integral_value(rounding='ROUND_HALF_UP')
    if e != int(ce):
        fail_ceil.append((k, L, e, int(ce)))
    if e != int(fl) and e != int(fl)+1:
        fail_floor.append((k, L, e, int(fl)))
    if e != int(rn):
        fail_round.append((k, L, e, int(rn)))

print("N1(k) = ceil((k+1)*alpha) failures:", len(fail_ceil), fail_ceil[:10])
print("N1(k) in {floor,floor+1} failures:", len(fail_floor), fail_floor[:10])
print("N1(k) = round((k+1)*alpha) failures:", len(fail_round), fail_round[:10])

# Also N0(k) = number of length-(k+1)? No. N0(k) from state = # length-k factors w with w0 a factor.
# Check N0 similarly. From state file it looked N0 ~ 2k/3 + something.
# N0(1..): [2,2,3,4,4,5,...] slope ~ 0.625? ratio N0(k)/k -> ?
# candidate N0(k) = floor((k+1)*beta) for beta=?
N0_vals = [2,2,3,4,4,5,5,6,7,7,8,9,9,10,10,11,12,12,13,13,14,15,15,16,17,17,18,18,19,20,20,21,22,22,23,23,24,25,25,26,26,27,28,28,29,30,30,31,31,32,33,33,34,34,35,36,36,37,38,38,39,39,40,41,41,42,43,43,44,44,45,46,46,47,47,48,49,49,50,51,51,52,52,53,54,54,55,56,56,57,57,58,59,59,60,60,61,62,62,63]
# compute N0 directly for length k factors ending... N0(k)=# length-k factors w with w0 a (k+1) factor
