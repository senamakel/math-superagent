import itertools, random
from lib.submasks import and_subsets

def T(n, d, h):
    acc = 0
    for o in and_subsets(d):
        acc ^= h[n - 1 - d + o]
    return acc

def delta_pow(h, k):
    out = []
    for j in range(len(h) - k):
        acc = 0
        for i in and_subsets(k):
            acc ^= h[j + i]
        out.append(acc)
    return out

bad = 0
total = 0
examples = []
for n in range(4, 13):
    for k in range(1, 8):
        for _ in range(8):
            h = [random.randint(0,1) for _ in range(n + k + 2)]
            for d in range(2, n):
                total += 1
                lhs = T(n, d, delta_pow(h, k))
                rhs = T(n + k, d + k, h)
                if lhs != rhs:
                    bad += 1
                    if len(examples) < 10:
                        examples.append((n,k,d,lhs,rhs,h[:10]))
print("total cells checked:", total)
print("mismatches:", bad)
for e in examples:
    print("MISMATCH", e)
