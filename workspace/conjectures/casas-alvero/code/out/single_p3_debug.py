"""Single-process p=3 Hasse-CA satisfier count for small n — debug / cross-check.
Inlined (no package import) to avoid module path issues."""
from math import comb

def pas_triangle(n):
    rows = []
    prev = [1]
    rows.append(prev)
    for r in range(1, n + 1):
        cur = [(prev[k] if k < len(prev) else 0) +
               (prev[k - 1] if k - 1 >= 0 else 0) for k in range(r + 1)]
        rows.append([c % 3 for c in cur])
        prev = cur
    return rows

def hasse_deriv(digs, i, triangle):
    n = len(digs) - 1
    out = [0] * (n - i + 1)
    for j in range(i, n + 1):
        c = triangle[j][i] * digs[j] % 3
        if c:
            out[j - i] = (out[j - i] + c) % 3
    return out

def trim(d):
    while len(d) > 1 and d[-1] == 0:
        d.pop()
    return d

def dp_mod(a, b):
    a = trim(a[:]); b = trim(b[:])
    degb = len(b) - 1
    inv = pow(b[-1], 1, 3)
    while len(a) - 1 >= degb:
        deg = len(a) - 1 - degb
        coef = a[-1] * inv % 3
        if coef:
            for k in range(degb + 1):
                a[deg + k] = (a[deg + k] - coef * b[k]) % 3
        a = trim(a)
    return a

def dp_gcd(a, b):
    if all(x == 0 for x in a): return b
    if all(x == 0 for x in b): return a
    a = trim(a[:]); b = trim(b[:])
    while not all(x == 0 for x in b):
        a, b = b, dp_mod(a, b)
    return a

def degree(p):
    return len(trim(p[:])) - 1

def is_ca(digs, n, TRI):
    for i in range(1, n):
        hi = hasse_deriv(digs, i, TRI)
        if all(x == 0 for x in hi): continue
        if degree(dp_gcd(digs, hi)) == 0: return False
    return True

def is_pure(digs, n):
    for a in (0,1,2):
        bits = [comb(n,k)*pow(a,n-k,3)%3 for k in range(n+1)]
        if bits == digs: return True
    return False

def base3_polys(n):
    for v in range(3**n):
        digs = [0]*n+[1]
        x=v
        for j in range(n):
            digs[j]=x%3; x//=3
        yield digs

for n in (3,4,5,6):
    TRI = pas_triangle(n)
    sat=ce=0
    for digs in base3_polys(n):
        if is_ca(digs,n,TRI):
            sat+=1
            if not is_pure(digs,n): ce+=1
    print(f"n={n} sat={sat} ce={ce} m=sat/3={sat//3}")
