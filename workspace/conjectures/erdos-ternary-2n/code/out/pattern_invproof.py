"""Upgrade: verify the FULL proof of S ∩ S^{-1} = {1} in Z_3.

Claim: the only unit x with ALL ternary digits in {0,1} whose inverse also has
all ternary digits in {0,1} is x = 1.

Proof (rigorous). Let x in S, x != 1, unit (low digit 1). Let m = v_3(x-1) >= 1.
Since x in S has digit 1 (not 2) at position m, and x-1 = 3^m y with y not div
by 3, the lowest digit of y is 1, so y ≡ 1 (mod 3) and x = 1 + 3^m y.
In Z_3: x^{-1} = (1+3^m y)^{-1} = 1 - 3^m y + (3^m y)^2 - (3^m y)^3 + ...
Each term ±3^{jm} y^j (j>=2) is divisible by 3^{2m} >= 3^{m+1} (m>=1), so it
contributes 0 to the 3^m-digit place (i.e. to x^{-1} mod 3^{m+1}).
So x^{-1} ≡ 1 - 3^m y (mod 3^{m+1}), and the digit at position m is
(-y mod 3) = -1 ≡ 2 (mod 3) since y ≡ 1 (mod 3).
Hence x^{-1} has digit 2 at position m: contradiction with x^{-1} in S.
Therefore every x != 1 in S has x^{-1} NOT in S.  So S ∩ S^{-1} = {1}.  QED.

Here we numerically verify the two load-bearing claims for a range:
(A) for x=1+3^m (y=1, lowest digit 1), inverse has digit 2 at position m;
(B) in general x = 1 + 3^m(1+3w), digit_m(x^{-1}) == 2.
"""
def digit_at(t, m):
    return (t // 3**m) % 3

print("=== (A) minimal offender x = 1+3^m ===")
for m in range(1, 12):
    mod = 3**(m+2)
    x = (1 + 3**m) % mod
    inv = pow(x, -1, mod)
    print(f" m={m:2d} inv(1+3^m) mod 3^{m+2} digit@{m} = {digit_at(inv,m)}  (expect 2)")

print("\n=== (B) general: x = 1+3^m(1+3w), w=0..3, digit_m(x^-1) == 2 ===")
bad = []
for m in range(1, 8):
    for w in range(0, 4):
        y = 1 + 3*w            # y ≡ 1 mod 3, lowest digit 1
        x = (1 + 3**m * y) % 3**(m+2)
        # sanity: x must be in S mod 3^(m+2) (lower m digits 0, digit m =1, digit m+1 comes from carry of 3w)
        inv = pow(x, -1, 3**(m+2))
        d = digit_at(inv, m)
        if d != 2:
            bad.append((m, w, d))
print("  all digit_m == 2:", not bad, bad[:5])
