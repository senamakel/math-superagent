# Verify the Pirzada recurrence arithmetic against the paper's stated claim.
import sympy as sp

# Paper's Table 1 recurrence (as printed):
#   |G_i| = |G_{i-1}| + 2^{i+4}
# Paper's stated orders: G1=94, G2=222, G3=478.
print("Paper's printed recurrence |G_i|=|G_{i-1}|+2^(i+4):")
v = 94
for i in (1, 2, 3):
    if i == 1:
        print(f"  G1 = 94")
    else:
        v = v + 2 ** (i + 4)
        print(f"  applying recurrence at i={i}: |G_{i}| = {v}   (paper says 222 for G2, 478 for G3)")

# Derived closed form from the construction: |X_i| = 32*2^i - 17, |G_i| = 2|X_i| = 2^{i+6} - 34.
print("\nDerived closed form |G_i| = 2^(i+6) - 34:")
for i in range(1, 6):
    print(f"  i={i}: {2**(i+6) - 34}")

# The half-order |X_i| = 32*2^i - 17 bounds cycles in a half: max cycle < |X_i| < 2^{i+5}.
for i in range(1, 6):
    half = 32 * 2**i - 17
    print(f"  i={i}: |X_i|={half}  =>  no cycle of length >= 2^{i+5} = {2**(i+5)}; unique 2-power = 2^{i+4} = {2**(i+4)}")

# Confirm no power of two sits in (2^{i+4}, |X_i|).
for i in range(1, 6):
    half = 32 * 2**i - 17
    below = [2**k for k in range(2, 20) if 2**k <= half]
    print(f"  i={i}: powers-of-two <= |X_i|={half}: {below}  (largest is 2^{i+4}={2**(i+4)})")
