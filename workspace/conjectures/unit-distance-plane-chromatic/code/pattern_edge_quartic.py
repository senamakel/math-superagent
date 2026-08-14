from fractions import Fraction as F

# Measured exact counts, k = 1..11 (Minkowski powers of calibrated spindle A)
n = {1:7, 2:26, 3:70, 4:155, 5:301, 6:532, 7:876, 8:1365, 9:2035, 10:2926, 11:4082}
e = {1:11, 2:69, 3:240, 4:628, 5:1375, 6:2659, 7:4694, 8:7730, 9:12053, 10:17985, 11:25884}

def quartic(coeffs, k):
    # coeffs low->high
    return sum(F(c) * k**i for i, c in enumerate(coeffs))

# Candidate closed forms (from the fit through k=2..10, coeffs -10,77/6,2,8/3,3/2)
e_form = lambda k: (F(9)*k**4 + F(16)*k**3 + F(12)*k**2 + F(77)*k - 60) / 6
n_form = lambda k: (F(1)*k**4 + F(6)*k**3 + F(14)*k**2 + F(15)*k + 6) / 6

print("e(k) = (9k^4 + 16k^3 + 12k^2 + 77k - 60)/6  for k>=2 :")
for k in range(1, 12):
    if k == 1:
        print(f"  k={k}: formula={e_form(k)} meas={e[k]} MATCH={e_form(k)==e[k]}")
    else:
        print(f"  k={k}: formula={e_form(k)} meas={e[k]} MATCH={e_form(k)==e[k]}")

print("\nn(k) = (k^4 + 6k^3 + 14k^2 + 15k + 6)/6 for k=1..11 :")
for k in range(1, 12):
    print(f"  k={k}: formula={n_form(k)} meas={n[k]} MATCH={n_form(k)==n[k]}")

# ratio e/n formula vs measured for the closed forms
print("\ne/n (closed-form) for k=2..11:")
for k in range(2, 12):
    print(f"  k={k}: {e_form(k)/n_form(k)}  (meas {F(e[k])/F(n[k])})")
