"""Verify the digit-argument proof of S ∩ S^{-1} = {1}:
for x = 1 + 3^m (mod higher) with m>=1, (1+3^m)^{-1} has a digit 2 at position m.
Check a range of m in the value domain."""
for m in range(1, 12):
    mod = 3**(m+2)
    x = (1 + 3**m) % mod
    inv = pow(x, -1, mod)
    # digit at position m of inv
    d = (inv // 3**m) % 3
    print(f"m={m:2d} (1+3^m)^{-1} mod 3^{m+2} = {inv:8d}  digit@m = {d}  -> has digit 2: {d==2}")
