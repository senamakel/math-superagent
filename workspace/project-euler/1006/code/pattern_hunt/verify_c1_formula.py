"""PE1006 pattern hunt: lead-1 factor count closed form.

c1(k) = number of distinct length-k Fibonacci subwords starting with '1'.

Conjecture (spotted from check_leading_counts.py output):
    c1(k) = 1 + floor(k / phi^2),   phi^2 = (3+sqrt(5))/2
          = 1 + floor(k * (3 - sqrt(5))/2)
Equivalently the increments c1(k) - c1(k-1) are the letters of the infinite
Fibonacci word itself: c1(k) - c1(k-1) = f_{k-1}, f = 0100101001001...

Three independent computations, must all agree:
  (i)   factor enumeration on a long prefix (safe length >= 3k, Lmin bound)
  (ii)  1 + (number of 1s among the first k-1 letters of the infinite word)
  (iii) 1 + floor(k*(3-sqrt(5))/2) via 50-digit Decimal (irrational slope,
        distance to nearest integer >= 1/(0.4 k), huge margin at k <= 10^4)
"""

from decimal import Decimal, getcontext
getcontext().prec = 60

SQRT5 = Decimal(5).sqrt()
C = (Decimal(3) - SQRT5) / 2  # 1/phi^2 ~ 0.381966


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def c1_by_enumeration(k, word):
    n = len(word)
    facs = {word[i:i + k] for i in range(n - k + 1)}
    assert len(facs) == k + 1, f"k={k}: got {len(facs)} factors, expected {k+1}"
    return sum(1 for w in facs if w[0] == '1')


def c1_by_prefix_ones(kmax, word):
    # c1(k) = 1 + #{j <= k-1 : word letter j (1-indexed) == '1'}
    out = []
    ones = 0
    for k in range(1, kmax + 1):
        out.append(1 + ones)
        if k <= len(word) and word[k - 1] == '1':
            ones += 1
    return out


def c1_by_slope(kmax):
    return [1 + int((Decimal(k) * C).to_integral_value(rounding='ROUND_FLOOR'))
            for k in range(1, kmax + 1)]


def main():
    KMAX = 400
    PREFIX_LEN = 3 * KMAX + 10
    W = fib_prefix(PREFIX_LEN)
    print(f"prefix len = {len(W)}  (>= 3*KMAX)")

    # (i) factor enumeration
    enum = [c1_by_enumeration(k, W) for k in range(1, KMAX + 1)]

    # (ii) prefix-one counts
    byones = c1_by_prefix_ones(KMAX, W)

    # (iii) slope formula
    byslope = c1_by_slope(KMAX)

    assert enum == byones, "enumeration vs prefix-ones mismatch"
    assert enum == byslope, "enumeration vs slope formula mismatch"
    print(f"c1(k) verified exactly for k = 1..{KMAX}: all three routes agree")
    print("first 30 terms:", enum[:30])
    print("increments c1(k)-c1(k-1), k=2..31:",
          [enum[k] - enum[k - 1] for k in range(1, 31)])
    print("Fibonacci word letters f_1..f_30:      ",
          list(W[:30]))
    # boundary checks at Fibonacci indices
    fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    for K in fibs:
        if K <= KMAX:
            print(f"  c1({K}) = {enum[K-1]}   (1+floor({K}/phi^2) = {byslope[K-1]})")
    # also check c0 = (k+1) - c1 stays consistent
    for k in range(1, KMAX + 1):
        assert (k + 1) - enum[k - 1] >= 0
    print(f"c0(k) = k+1-c1(k) nonneg for k=1..{KMAX}: OK")
    # write terms for OEIS / tools
    with open('code/out/c1_terms.txt', 'w') as fh:
        for k, v in enumerate(enum, 1):
            fh.write(f"{k} {v}\n")
    print("wrote code/out/c1_terms.txt")


if __name__ == '__main__':
    main()