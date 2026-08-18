"""Pin the exact range where g(k) = floor(Psi(k)/10^(2k-2)) equals c1(k)=1+floor(k/phi^2).

Built from recorded exact vR/s1 (validated against recorded Psi(1..25) earlier).
"""
import sys
import mpmath as mp
sys.set_int_max_str_digits(20000)
mp.mp.dps = 80
PHI2_INV = mp.mpf(1) / ((1 + mp.sqrt(5)) / 2) ** 2

def c1(k):
    return 1 + int(mp.floor(k * PHI2_INV))

def load_pairs(path):
    out = {}
    for line in open(path):
        p = line.split()
        if len(p) >= 2:
            out[int(p[0])] = int(p[1])
    return out

vR = load_pairs('code/out/vR_exact.txt')
s1 = load_pairs('code/out/s1_exact.txt')
Psi = {1: 1}
for k in range(1, 3000):
    Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)

# g(k) = floor(Psi(k) / 10**(2k-2)); compare to c1(k)
good = []
first_bad = None
bad_examples = []
for k in range(1, 3001):
    g = Psi[k] // 10 ** (2 * k - 2)
    if g == c1(k):
        good.append(k)
    else:
        if first_bad is None:
            first_bad = k
        bad_examples.append((k, g, c1(k)))

print("g(k)=c1(k) holds for", len(good), "of 3000 k")
print("first failure at k =", first_bad, "with g, c1 =", bad_examples[0])
print("first 10 failures:", bad_examples[:10])
# consecutive blocks: max run of good
maxrun, cur, curstart, beststart = 0, 0, None, None
for k in range(1, 3001):
    g = Psi[k] // 10 ** (2 * k - 2)
    if g == c1(k):
        if cur == 0:
            curstart = k
        cur += 1
        if cur > maxrun:
            maxrun, beststart = cur, curstart
    else:
        cur = 0
print("longest consecutive run of g==c1 starts at", beststart, "length", maxrun)
# also: does g(k)==c1(k) hold exactly at the k=F_n-1 knots?
f = [1, 1]
while f[-1] <= 3000:
    f.append(f[-1] + f[-2])
kn = [F - 1 for F in f if 1 <= F - 1 <= 3000]
print("at k=F_n-1:", [(k, Psi[k] // 10 ** (2 * k - 2), c1(k)) for k in kn])
