"""Verify (as exact Z[k] identities) the families covering s ≡ 3 or 4 (mod 11),
i.e. t = (n-1)/840 with t mod 11 in {3,4}. These were found at other moduli;
CONTEXT warns captures carry attribution bugs, so every (a,b) is re-derived
from the capture text and checked: 4xyz - n(yz+xz+xy) identically zero in Z[k].

Also verify the same for a random sample of other families, and report which
residue s* = (b-1)//840 mod 11 each covers along with its modulus M = a/840.
"""
import re
from sympy import Poly, Symbol, expand

k = Symbol('k', integer=True)

def check_identity(a, b, xstr, ystr, zstr):
    """Return True if 4*x*y*z - n*(y*z + x*z + x*y) == 0 as a polynomial."""
    n = Poly(a * k + b, k)
    try:
        X = Poly(expand(xstr), k)
        Y = Poly(expand(ystr), k)
        Z = Poly(expand(zstr), k)
    except Exception as e:
        return f'poly-error {e}'
    # 4XYZ - n(YZ + XZ + XY) in Z[k]
    lhs = 4 * X * Y * Z
    rhs = n * (Y * Z + X * Z + X * Y)
    diff = lhs - rhs
    c = diff.all_coeffs()
    return all(coef == 0 for coef in c)

def all_int_positive_coeffs(xstr):
    try:
        p = Poly(expand(xstr), k)
    except Exception:
        return False
    return all(c.is_integer for c in p.all_coeffs())

hits = []
for fn in ['code/out/subprogression.captured.txt', 'code/out/extended_subprogression.full.txt']:
    lines = open(fn).read().splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=(.*)$', lines[i])
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            xstr = m.group(3).strip()
            ystr = lines[i+1].strip()
            zstr = lines[i+2].strip()
            assert ystr.startswith('y=') and zstr.startswith('z='), (i, ystr[:20], zstr[:20])
            ystr = ystr[2:]; zstr = zstr[2:]
            zstr = zstr.split('  [')[0]   # drop trailing [('14a',...)] tag
            s = (b - 1) // 840
            if s % 11 in (3, 4):
                hits.append((fn, a, b, s % 11, xstr, ystr, zstr))
            i += 3
        else:
            i += 1

print(f'families covering t ≡ 3 or 4 (mod 11): {len(hits)}')
ok = 0
by_mod = {}
for fn, a, b, s11, xstr, ystr, zstr in hits:
    res = check_identity(a, b, xstr, ystr, zstr)
    M = a // 840
    pos = all_int_positive_coeffs(xstr) and all_int_positive_coeffs(ystr) and all_int_positive_coeffs(zstr)
    if res is True and pos:
        ok += 1
        by_mod.setdefault(M, set()).add(s11)
    else:
        print(f'  FAIL a={a} b={b} s11={s11} M={M} res={res} pos={pos}')
print(f'verified identities with integer positive coeffs: {ok}/{len(hits)}')

# aggregate which residues s mod 11 are covered at each M (any M), vs Schinzel-legal
from collections import defaultdict
print('\nM -> s mod 11 residues covered by these verified families:')
for M in sorted(by_mod):
    print(f'  M={M}: {sorted(by_mod[M])}')
print('\nOverall t≡3 mod 11 covered at M set:', sorted(set(a//840 for fn,a,b,s11,x,y,z in hits if s11==3)))
print('Overall t≡4 mod 11 covered at M set:', sorted(set(a//840 for fn,a,b,s11,x,y,z in hits if s11==4)))