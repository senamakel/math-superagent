import sys

def ternary_digits_low(x, k):
    # low k base-3 digits of x, least significant first
    digs = []
    for _ in range(k):
        digs.append(x % 3)
        x //= 3
    return digs

def digit_free(m):
    # base-3 expansion of m avoids digit 2 (ground truth)
    while m > 0:
        if m % 3 == 2:
            return False
        m //= 3
    return True

def sieve(k):
    # A_k = { n mod 2*3^(k-1) : low k ternary digits of 2^n mod 3^k avoid 2 }
    mod_n = 2 * (3 ** (k - 1))
    mod_3k = 3 ** k
    survivors = []
    for n in range(mod_n):
        r = pow(2, n, mod_3k)
        if all(d in (0, 1) for d in ternary_digits_low(r, k)):
            survivors.append(n)
    return survivors

if __name__ == "__main__":
    # verify digit_free on witnesses
    assert digit_free(1) == True      # 2^0
    assert digit_free(4) == True      # 2^2 = 11_3
    assert digit_free(256) == True    # 2^8 = 100111_3
    assert digit_free(2) == False     # 2_3 contains digit 2
    assert digit_free(5) == False     # 12_3 contains digit 2
    assert digit_free(3) == True      # 10_3 has no digit 2
    assert digit_free(8) == False     # 22_3 contains 2
    print("digit_free witness checks passed")

    for k in range(1, 13):
        A = sieve(k)
        nset = set(A)
        # check witnesses membership
        w = {0: nset.__contains__(0 % (2*3**(k-1))),
             2: nset.__contains__(2 % (2*3**(k-1))),
             8: nset.__contains__(8 % (2*3**(k-1)))}
        print(f"k={k:2d}  |A_k|={len(A):4d}  witnesses_in_A={w}")
