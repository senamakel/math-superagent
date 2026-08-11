import math

def I_d(d, x, n):
    """Return I_d = a = round(x - b*min*sqrt(d)) where bmin minimizes ||x - b*sqrt(d)|| , |b|<=n."""
    sd = math.sqrt(d)
    best_b = None
    best_err = float('inf')
    # scan b in [0,n]; symmetry b->-b (sign of error changes), a adjusts
    for b in range(0, n+1):
        buf = math.fmod(x - b*sd, 1.0)
        # distance to nearest integer
        err = min(buf, 1-buf) if buf>=0 else min(-buf, 1+buf)
        if err < best_err:
            best_err = err
            best_b = b
    a = round(x - best_b*sd)
    return a, best_b, best_err

pi = math.pi
vals = []
for d in range(2, 100):
    if int(math.isqrt(d))**2 == d:
        continue  # square
    a, b, err = I_d(d, pi, 10_000)
    vals.append((d, a, b, err))
    print(f"d={d:3d}  I={a:12d}  b={b:10d}  err={err:.6e}")
print("\n|I_d| sequence:")
print([abs(v[1]) for v in vals])
