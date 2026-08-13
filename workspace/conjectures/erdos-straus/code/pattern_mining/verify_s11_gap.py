"""Verify families covering t ≡ 3 or 4 (mod 11) as exact Z[k] identities.

For every (a,b) block in the two captures with s=(b-1)/840 ≡ 3 or 4 (mod 11):
  * 4*x*y*z - n*(y*z + x*z + x*y) reduces to the zero polynomial in Z[k];
  * x, y, z are integer-coefficient polynomials, positive at k=1..5.
The identity is checked via expand-then-Poly (direct Poly multiplication in
this sympy version produces a wrong ZZ[k] domain, verified above).
"""
import re
from sympy import Symbol, expand, Poly, sympify

k = Symbol('k', integer=True)

def check_identity(a, b, xstr, ystr, zstr):
    X = sympify(xstr, locals={'k': k})
    Y = sympify(ystr, locals={'k': k})
    Z = sympify(zstr, locals={'k': k})
    n = sympify(a * k + b)
    expr = expand(4 * X * Y * Z - n * (Y * Z + X * Z + X * Y))
    p = Poly(expr, k)
    if not all(c == 0 for c in p.all_coeffs()):
        return ('not-identity', p)
    # integrality: coefficients of x,y,z all integers; positivity at k=1..5
    for name, ex in [('x', X), ('y', Y), ('z', Z)]:
        q = Poly(expand(ex), k)
        if not all(c.is_integer for c in q.all_coeffs()):
            return (f'{name}-nonint', q)
        for kk in range(1, 6):
            if not expand(ex).subs(k, kk) > 0:
                return (f'{name}-nonpos@k={kk}', q)
    return True

hits = []
for fn in ['code/out/subprogression.captured.txt', 'code/out/extended_subprogression.full.txt']:
    lines = open(fn).read().splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=(.*)$', lines[i])
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            xstr = m.group(3).strip()
            ystr = lines[i + 1].strip()[2:]
            zstr = lines[i + 2].strip()[2:].split('  [')[0]
            s = (b - 1) // 840
            if s % 11 in (3, 4):
                hits.append((fn, a, b, s % 11, xstr, ystr, zstr))
            i += 3
        else:
            i += 1

print(f'families covering t ≡ 3 or 4 (mod 11): {len(hits)}')
ok = 0
by_mod = {}
fails = []
for fn, a, b, s11, xstr, ystr, zstr in hits:
    res = check_identity(a, b, xstr, ystr, zstr)
    M = a // 840
    if res is True:
        ok += 1
        by_mod.setdefault(M, set()).add(s11)
    else:
        fails.append((a, b, s11, M, res))
print(f'verified identities: {ok}/{len(hits)}')
for f in fails[:10]:
    print('  FAIL', f)
print('\nM -> s11 covered (all verified):')
for M in sorted(by_mod):
    print(f'  M={M}: {sorted(by_mod[M])}')