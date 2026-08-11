"""Structure of record b's: which continued fraction denominators do they match?
Fast float scan; CF denominators computed exactly for the specific irrational."""
import math
import sympy as sp

PI = 3.14159265358979323846264338327950288419716939937510

def cf_denoms(x, N):
    """Convergent denominators of CF of x, up to N, via exact high-precision."""
    xv = sp.Rational(x) if isinstance(x, int) else x
    t = sp.N(sp.pi / sp.sqrt(d), 120) if not isinstance(x, (int, float)) else x
    a = []
    # operate in high precision float is enough for order
    if hasattr(x, 'evalf'):
        tv = x.evalf(120)
    else:
        tv = x
    q_2, q_1 = 0, 1
    denoms = []
    for _ in range(400):
        ai = math.floor(tv)
        a.append(ai)
        q = ai * q_1 + q_2
        if q > N:
            break
        denoms.append(q)
        rem = tv - ai
        if rem < 1e-60:
            break
        tv = 1.0 / rem
        q_2, q_1 = q_1, q
    return denoms

def records_float(d, N):
    sd = math.sqrt(d)
    best = 1e18
    recs = []
    for b in range(0, N + 1):
        v = b * sd - PI
        r = round(v)
        err = abs(v - r)
        if err < best - 1e-18:
            best = err
            recs.append(b)
    return recs

d = 2
N = 2_000_000
recs = records_float(d, N)
print(f"d={d} records:", recs)

# denominators of CF of pi/sqrt(d) and pi*sqrt(d) and pi
for name, x in [("pi/sqrt2", sp.pi / sp.sqrt(2)), ("pi*sqrt2", sp.pi * sp.sqrt(2)),
                ("2*pi/sqrt2", 2*sp.pi/sp.sqrt(2)), ("pi/2", sp.pi/2)]:
    ds_ = cf_denoms(x, N)
    hit = [b for b in recs if b in set(ds_)]
    print(f"  {name}: {len(hit)}/{len(recs)} records in conv denoms. hit={hit}")
