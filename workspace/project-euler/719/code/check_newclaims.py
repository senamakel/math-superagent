"""Independent check of newly-filed structural claims in research/."""
import sys
from itertools import product

def expr(t, d):
    if t < 0:
        return False
    if t == int(d):
        return True
    return any(expr(t - int(d[:i]), d[i:]) for i in range(1, len(d)))

def is_sroot(m):
    return m >= 2 and expr(m, str(m*m))

# 1 & 2: F1/F2 families. (10^k-1,10^k) k>=2; (10^k-10,10^k-9) k>=3
f1_ok = all(is_sroot(10**k - 1) and is_sroot(10**k) for k in range(2, 8))
f2_ok = all(is_sroot(10**k - 10) and is_sroot(10**k - 9) for k in range(3, 8))
print("F1 (10^k-1,10^k) k=2..7:", f1_ok)
print("F2 (10^k-10,10^k-9) k=3..7:", f2_ok)

# 3: (10^k-10^j, +1) pair fails at k=j+2 for j>=2
for j in range(2, 6):
    k = j + 2
    a, b = 10**k - 10**j, 10**k - 10**j + 1
    print(f"  j={j} k={j+2}: is_sroot(pair) = {is_sroot(a)},{is_sroot(b)}")

# 4: repunit-witness identity
def repunit_check(m):
    s = str(m*m)
    n = len(s)
    for cuts in product([0,1], repeat=n-1):
        blocks, start = [], 0
        for i in range(n-1):
            if cuts[i]:
                blocks.append(s[start:i+1]); start = i+1
        blocks.append(s[start:])
        if len(blocks) < 2:
            continue
        vals = [int(b) for b in blocks]
        if sum(vals) != m:
            continue
        # L_i = digits strictly to the right of block i (0 = units)
        Ls = []
        pos = n
        for b in reversed(blocks):
            pos -= len(b)
            Ls.append(pos)
        Ls = Ls[::-1]
        lhs = m*(m-1)//9
        rhs = sum(v*(10**L - 1)//9 for v, L in zip(vals, Ls))
        return lhs == rhs, (vals, Ls)
    return None

for m in [82, 91, 99, 45, 55, 100, 9801]:
    if m > 100 and not expr(m, str(m*m)):
        pass
    res = repunit_check(m)
    if res is None:
        print(f"  m={m}: no 2+block split summing to m -- not an S-root here?")
    else:
        ok, det = res
        print(f"  m={m}: repunit identity holds = {ok}  blocks={det[0]} L={det[1]}")

# 5: mod-9 invariant over the 408 b-file roots
roots = [int(x) for x in open('out/roots408.txt').read().split() if x.strip()]
viol = [m for m in roots if m % 9 not in (0,1)]
print("mod-9 violations among 408 roots:", len(viol))
