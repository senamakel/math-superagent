"""Hand-check the F_7 witness f = x^4 + x^3 + 4x for CA degree 4.

Independent hand-check (small enough to do by inspection), recorded so the
TPTP encoding has a human-verified arithmetic reference. Values mod 7.
"""
p = 7
x = range(7)

def ev(coeffs, t):
    # coeffs[0] + coeffs[1] x + ... ascending
    acc = 0
    for k, c in enumerate(coeffs):
        acc = (acc + c * (t ** k)) % p
    return acc

# f = x^4 + x^3 + 4x   => ascending coeffs [0,4,0,1,1]
f_co = [0, 4, 0, 1, 1]
# H_1 = 4x^3 + 3x^2 + 4
h1_co = [4, 0, 3, 4]
# H_2 = 6x^2 + 3x
h2_co = [0, 3, 6]
# H_3 = 4x + 1
h3_co = [1, 4]

f_vals = [ev(f_co, t) for t in x]
h1_vals = [ev(h1_co, t) for t in x]
h2_vals = [ev(h2_co, t) for t in x]
h3_vals = [ev(h3_co, t) for t in x]

print("f  values:", f_vals)
print("H1 values:", h1_vals)
print("H2 values:", h2_vals)
print("H3 values:", h3_vals)

def shares(fv, hv):
    return [t for t in x if fv[t] == 0 and hv[t] == 0]

print("common roots with H1:", shares(f_vals, h1_vals))
print("common roots with H2:", shares(f_vals, h2_vals))
print("common roots with H3:", shares(f_vals, h3_vals))

# pure power check: (x-a)^4 value tables mod 7
for a in range(7):
    pp = [pow((t - a) % p, 4, p) for t in x]
    if pp == f_vals:
        print("f IS a pure power (x-%d)^4" % a)
        break
else:
    print("f is NOT a pure power (x-a)^4 for any a in F_7")

print("pure-power tables:")
for a in range(7):
    print(" a=%d:" % a, [pow((t - a) % p, 4, p) for t in x])
