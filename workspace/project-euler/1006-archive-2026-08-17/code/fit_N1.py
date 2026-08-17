import os

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

# We need length-(k+1) factors. Use a big word.
# |S_n| grows fast; S_25 ~ F_27 ~ 317811. For N1 up to K, need word len >= 3*(K+1).
def N1_upto(K):
    n = 0
    while word_len(n) < 3*(K+1):
        n += 1
    word = S(n)
    res = []
    prev_set = set()
    for L in range(2, K+2):
        # length-L factors
        subs = {word[i:i+L] for i in range(len(word)-L+1)}
        ending1 = sum(1 for s in subs if s[-1]=='1')
        res.append((L, ending1))
    return res

K = 2000
res = N1_upto(K)
# res[i] = (L, N1(L-1)) count of length-L factors ending in 1 = N1(L-1)
import math
# fit N1(k) = round(c*(k+1) + d)? Let's just find empirical slope
slopes = []
for L, e in res:
    # e = N1(L-1)
    pass
# Print N1(k) for k = L-1
N1 = {L-1: e for L, e in res}
print("N1(1..40):", [N1[k] for k in range(1,41)])
print("N1(999):", N1[999], "N1(2000):", N1[2000], "ratio:", N1[2000]/2000)

# test candidate: N1(k) = floor((k+1)*alpha - phi) or floor((k+1)*alpha + c)
phi = (1+5**0.5)/2
alpha = 1/phi**2  # 0.381966
# try N1(k) = round((k+1)*c) for c in range
best = None
for cnum in range(381000, 392000, 1):
    c = cnum/1000000.0
    ok = all(e == round(c*(L)) for L, e in res)
    # compare count of length L ending in 1
    # Actually res e is for length L. 
    if ok:
        best = c
        break
# try broader: N1(k) = floor((k+1)*c + d)
import itertools
def fit_integer_floor(seq, func, c):
    pass

print("First candidate c for N1(k)=round((k+1)*c):", best)
