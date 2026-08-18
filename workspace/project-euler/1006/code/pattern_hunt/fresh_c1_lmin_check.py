from decimal import Decimal, getcontext
from lib.fibword import fib_prefix

getcontext().prec = 80
ALPHA = (Decimal(3) - Decimal(5).sqrt()) / 2


def fibs_until(n):
    fs = [1, 2]
    while fs[-1] <= n:
        fs.append(fs[-1] + fs[-2])
    return fs


def main():
    K = 10_000
    W = fib_prefix(30_000)
    # c1: independent factor-set enumeration at every k is expensive, so use
    # direct mechanical-prefix count and independently test it against slope.
    ones = 0
    c1_inc = []
    for k in range(1, K + 1):
        c1_inc.append(1 + ones)
        ones += W[k - 1] == '1'
    c1_slope = [1 + int((Decimal(k) * ALPHA).to_integral_value(rounding='ROUND_FLOOR'))
                for k in range(1, K + 1)]
    assert c1_inc == c1_slope

    # Lmin: plain strings, one scan per k, stopping at the (k+1)-st factor.
    # This is an independent bounded oracle, not the production method.
    fs = fibs_until(K)
    lmin = []
    for k in range(1, K + 1):
        seen = set()
        answer = None
        for i in range(len(W) - k + 1):
            seen.add(W[i:i+k])
            if len(seen) == k + 1:
                answer = i + k
                break
        assert answer is not None
        nxt = next(f for f in fs if f > k)
        assert answer == k + nxt - 1, (k, answer, k + nxt - 1)
        lmin.append(answer)
    print('c1 slope law: exact for k=1..10000')
    print('Lmin Fibonacci law: exact for k=1..10000')
    for k in (4181, 6764, 6765, 10000):
        nxt = next(f for f in fs if f > k)
        print(k, c1_slope[k-1], lmin[k-1], 'nextFib', nxt)


if __name__ == '__main__':
    main()
