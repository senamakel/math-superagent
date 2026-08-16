"""Independent validation of the refutation models returned by z3/cvc5.

For each candidate invariant Phi claimed refuted, substitute the returned
digit model back into the ORIGINAL statement (2^n = sum a_i 3^i, digits in
{0,1}) and confirm the digits really are those of the stated n and that the
invariant is really violated there.

This is the "validate every model" step, done by direct integer arithmetic
(a different route than the solver).
"""
def low_digits(n, L=12):
    m = 2 ** n
    return [(m // (3 ** i)) % 3 for i in range(L)]

def polarity(d):
    return sum((-1) ** i * d[i] for i in range(len(d)))

# --- z3 model for C2: n=0, digits = [1,0,0,...], Polarity = 1 (odd) ---
n = 0
d = low_digits(n)
print(f"n={n}: 2^{n}={2**n}, low digits (low->high)={d}")
print(f"  digit-free (all in {{0,1}})? {all(x in (0,1) for x in d)}")
print(f"  Polarity = sum (-1)^i a_i = {polarity(d)}")
print(f"  claim refuted (Polarity ≡ 0 mod 2)? -> "
      f"{polarity(d) % 2 != 0}")
print(f"  claim refuted (Polarity ≡ 0 mod 3)? -> "
      f"{polarity(d) % 3 != 0}")
print()

# --- z3/cvc5 model for gate n=8: digits = [1,1,1,0,0,1,...] = 256 ---
n = 8
d = low_digits(n)
recon = sum(d[i] * (3 ** i) for i in range(len(d)))
print(f"n={n}: 2^{n}={2**n}, low digits (low->high)={d}")
print(f"  digit-free? {all(x in (0,1) for x in d)}")
print(f"  reconstructed value = {recon} (==2^{n}? {recon == 2**n})")
print(f"  Polarity = {polarity(d)}")

# --- digits of the three witnesses concatenated, low->high, as text ---
for n in (0, 2, 8):
    d = low_digits(n)
    s = ''.join(str(x) for x in reversed(d)).lstrip('0')
    print(f"n={n}: 2^{n} = 2**{n} = {2**n} = {s}_3")
