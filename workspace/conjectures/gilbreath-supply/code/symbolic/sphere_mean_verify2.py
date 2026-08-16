"""Direct verification: parts (a),(b),(c) only (cheap)."""
import itertools, random
from math import comb
from fractions import Fraction

def kraw(w, m, n):
    return sum((-1) ** j * comb(m, j) * comb(n - m, w - j) for j in range(w + 1))

def submasks_weight_w(n, w):
    for combo in itertools.combinations(range(n), w):
        h = 0
        for j in combo:
            h |= 1 << j
        yield h

def xor_over_A(h, A):
    x = 0
    for j in A:
        x ^= (h >> j) & 1
    return x

print("(a) sum_{h in S_w} (-1)^{h.1_A} == K_w(m;n) ?")
allok = True
for n in range(3, 11):
    for w in range(0, n + 1):
        for m in range(0, n + 1):
            A = list(range(m))
            s = sum((-1) ** xor_over_A(h, A) for h in submasks_weight_w(n, w))
            if s != kraw(w, m, n):
                print(f"  FAIL n={n} w={w} m={m}: got {s}, kraw {kraw(w,m,n)}")
                allok = False
print("  ALL OK" if allok else "  FAILURES above")

print("(b) #{h in S_w : xor over A = 1} == (C(n,w)-K_w(m;n))/2 ?")
allok2 = True
random.seed(1)
for n in range(3, 13):
    for w in range(0, n + 1):
        for _ in range(8):
            m = random.randint(0, n)
            A = random.sample(range(n), m)
            cnt = sum(1 for h in submasks_weight_w(n, w) if xor_over_A(h, A) == 1)
            lhs = cnt
            rhs = (comb(n, w) - kraw(w, m, n)) // 2
            if lhs != rhs:
                print(f"  FAIL n={n} w={w} m={m}: count {lhs}, form {rhs}")
                allok2 = False
print("  ALL OK" if allok2 else "  FAILURES above")

print("(c) ratio K_w(m;n)/C(n,w) vs (1-2w/n)^m for n large, m fixed")
for wfrac in [1/8, 1/4, 1/2]:
    print(f"  alpha={wfrac}:")
    for m in [1, 2, 4, 8]:
        row = []
        for n in [64, 256, 1024, 4096]:
            w = int(round(wfrac * n))
            r = Fraction(kraw(w, m, n), comb(n, w))
            row.append(f"n={n}:{float(r):.5f}")
        print(f"    m={m}: " + "  ".join(row) + f"   target={(1-2*wfrac)**m:.5f}")
