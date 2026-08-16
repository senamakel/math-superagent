"""Naive oracle for the Erdos ternary conjecture.

digit_free(m): decide whether the base-3 expansion of m avoids the digit 2.
    Exact integer arithmetic, no floats. O(log_3 m) in time and space.

scan(n_max): print every n in [0, n_max] with 2^n in base 3, marking which are
    digit-2-free. This is ground truth for the conjecture, reproduced by
    materialising 2**n as a big integer -- deliberately naive, NOT the sieve.

The three known exceptions are n = 0 (1_3), n = 2 (11_3), n = 8 (100111_3).
Any claimed obstruction must let those three pass while forbidding n > 8.
"""


def to_base3(m):
    """Return the base-3 digit string of m (most significant first). m >= 0."""
    if m == 0:
        return "0"
    digs = []
    while m > 0:
        digs.append(str(m % 3))
        m //= 3
    return "".join(reversed(digs))


def digit_free(m):
    """True iff the base-3 expansion of m contains no digit 2. Exact."""
    if m == 0:
        return True  # 0 = 0_3, no 2
    while m > 0:
        if m % 3 == 2:
            return False
        m //= 3
    return True


def check_witnesses():
    """Verify digit_free by hand against the statement's worked examples."""
    # The three exceptions: 2^n must be digit-free.
    answers = {0: True, 2: True, 8: True}
    # Values the statement/context give as containing a 2.
    contains_2 = {3: "22_3", 5: "1012_3", 6: "2101_3"}
    ok = True
    for n, expect in answers.items():
        m = 2 ** n
        got = digit_free(m)
        match = got == expect
        ok = ok and match
        print(f"n={n}: 2^n={m} = {to_base3(m)}_3  digit_free={got} "
              f"(expected {expect}) {'OK' if match else 'MISMATCH'}")
    for n, known in contains_2.items():
        m = 2 ** n
        got = digit_free(m)
        print(f"n={n}: 2^n={m} = {to_base3(m)}_3  digit_free={got} "
              f"(should be False; {known}_3)")
        ok = ok and (got is False)
    return ok


def scan(n_max):
    """List n in [0, n_max] whose 2^n avoids the digit 2 in base 3."""
    free = []
    for n in range(0, n_max + 1):
        m = 2 ** n
        if digit_free(m):
            free.append((n, m, to_base3(m)))
    return free


if __name__ == "__main__":
    print("=== Witness check (the three exceptions must pass) ===")
    ok = check_witnesses()
    print("Witness check:", "PASSED" if ok else "FAILED")
    print()
    print("=== Scan n in [0, 20] ===")
    free = scan(20)
    for n, m, s in free:
        print(f"n={n:2d}: 2^n={m} = {s}_3   <- digit-free")
    print("digit-free n found up to 20:", [n for n, _, _ in free])
