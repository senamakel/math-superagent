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

K = 500
n = 0
while word_len(n) < 4*(K+1):
    n += 1
word = S(n)
F = word[:K]  # prefix of infinite fibonacci word

fails_vR = 0
fails_N1 = 0
fails_N0 = 0
alpha = (3-5**0.5)/2
import math
for k in range(1, K+1):
    wk = {word[i:i+k] for i in range(len(word)-k+1)}
    wk1 = {word[i:i+k+1] for i in range(len(word)-(k+1)+1)}
    vals = {w:int(w) for w in wk}
    N1 = sum(1 for w in wk if (w+'1') in wk1)
    N0 = sum(1 for w in wk if (w+'0') in wk1)
    vR = next(vals[w] for w in wk if (w+'0') in wk1 and (w+'1') in wk1)
    # check vR = reverse(F[:k])
    val_rev = int(F[:k][::-1])
    if val_rev != vR: fails_vR += 1
    # check N1 = ceil((k+1)*alpha)
    ce = math.ceil((k+1)*alpha)
    if N1 != ce: fails_N1 += 1
    # N0 = ceil((k+1)*(1-alpha))
    ce0 = math.ceil((k+1)*(1-alpha))
    if N0 != ce0: fails_N0 += 1

print("vR==reverse(F[:k]) fails:", fails_vR)
print("N1==ceil((k+1)*alpha) fails:", fails_N1)
print("N0==ceil((k+1)*(1-alpha)) fails:", fails_N0)
