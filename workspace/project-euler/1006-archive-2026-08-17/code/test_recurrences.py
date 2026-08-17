"""Self-test for lib.recurrences: BM must recover the exact order/coefficients
of a known random linear recurrence over a prime, on several test cases."""
from lib.recurrences import berlekamp_massey, verify_recurrence, rational_reconstruct


def test_bm():
    import random
    random.seed(1)
    tests = []
    # linear: A(k) = 3 A(k-1) - 2 A(k-2) + A(k-3)
    tests.append((3, [3, -2, 1]))
    # order 5
    tests.append((5, [1, 2, 3, 4, 5]))
    # order 1
    tests.append((1, [7]))
    # order 0: all zeros
    tests.append((0, []))

    P = 1000000007
    for order, coeffs in tests:
        seq = []
        for _ in range(order):
            seq.append(random.randrange(P))
        # generate the full recurrence tail
        for k in range(order, 80):
            total = sum(c * seq[k - 1 - j] for j, c in enumerate(coeffs))
            seq.append(total % P)
        L, C = berlekamp_massey(seq, P)
        ok, bad = verify_recurrence(seq, C, p=P)
        print(f"order={order} coeffs={coeffs} -> BM L={L} C={C} verify={ok}")
        assert L == order, (order, L)
        assert ok and bad is None


def test_rat():
    # 2/3 mod 1e9+7
    m = 1000000007
    x = (2 * pow(3, -1, m)) % m
    print("reconstruct 2/3:", rational_reconstruct(x, m))
    assert rational_reconstruct(x, m) == (2, 3)
    x2 = (7 * pow(11, -1, m)) % m
    print("reconstruct 7/11:", rational_reconstruct(x2, m))
    assert rational_reconstruct(x2, m) == (7, 11)


if __name__ == "__main__":
    test_bm()
    test_rat()
    print("all good")
