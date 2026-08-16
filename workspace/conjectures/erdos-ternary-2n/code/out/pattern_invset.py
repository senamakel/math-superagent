"""Verify the value-domain theorem S ∩ S^{-1} = {1} in Z_3, where S = digit-{0,1}
3-adic integers. Enumerate ALL units x mod 3^k with ternary digits in {0,1} and
low digit 1, and check only x=1 has inverse with all digits in {0,1}.
This is pure value domain (not restricting to powers of 2 / the orbit)."""
def digit_free_01(t, k):
    for _ in range(k):
        if t % 3 == 2:
            return False
        t //= 3
    return True

for k in range(2, 13):
    mod = 3**k
    # all units with digits in {0,1}, low digit 1: digits positions 1..k-1 each in {0,1}
    bad = []
    for mask in range(2**(k-1)):
        x = 1
        mm = mask
        for i in range(1, k):
            if mm & 1:
                x += 3**i
            mm >>= 1
        # x is a unit with {0,1} digits, low digit 1
        inv = pow(x, -1, mod)
        if digit_free_01(inv, k):
            if x != 1:
                bad.append(x)
    print(f"k={k:2d} mod={mod:6d} #units-in-S={2**(k-1):5d} "
          f"units-with-{0,1}-inverse: {bad if bad else '{1 only}'}")
