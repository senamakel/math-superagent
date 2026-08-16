"""Cross-check my bit-parallel F2 Hasse-CA checker against the run's ALREADY
RECORDED p=2 multiplier data for n=3..16 (independently established values from
satisfier_multiplier_over_Fp.md / commands.log):
  recorded m(n,2) for n=3..16 = [2,1,2,2,8,1,2,2,8,2,8,8,457,1]

Reuse the exact code from extend_p2_multiplier.py by importing it (it has no
side-effect guard, so import then call the functions).
"""
import importlib.util
spec = importlib.util.spec_from_file_location("ep", "code/out/extend_p2_multiplier.py")
# importing would run the __main__ block; instead copy the two needed functions here.
# Safer: redefine directly (bit-parallel F2), minimal.

def Cparity(n, k):
    return (k & n) == k

def hasse_deriv(fbits, i):
    out = 0
    j = 0
    fb = fbits
    while fb:
        if fb & 1 and (i & j) == i:
            out |= 1 << (j - i)
        fb >>= 1
        j += 1
    return out

def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a

def pgcd(a, b):
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, pmod(a, b)
    return a

def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return False
    return True

def is_pure_power_f2(fbits, n):
    if fbits == (1 << n):
        return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j):
            bits |= 1 << j
    return fbits == bits

def counts(n):
    sat = ce = 0
    for v in range(1 << n):
        fbits = (1 << n) | v
        if is_ca_f2(fbits):
            sat += 1
            if not is_pure_power_f2(fbits, n):
                ce += 1
    return sat, ce

recorded = {3:2,4:1,5:2,6:2,7:8,8:1,9:2,10:2,11:8,12:2,13:8,14:8,15:457,16:1}
ok = True
for n, rec_m in sorted(recorded.items()):
    sat, ce = counts(n)
    m = sat // 2
    match = (m == rec_m)
    ok = ok and match
    print(f"n={n:2d}: mine m={m:4d} recorded m={rec_m:4d} ce={ce:4d} match={match}")
print("ALL MATCH recorded n=3..16:", ok)
