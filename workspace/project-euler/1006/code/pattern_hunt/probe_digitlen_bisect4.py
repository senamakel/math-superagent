"""Pin only the digit-length 3->4 transition, which lies in (25684, 30000]."""
import sys

sys.set_int_max_str_digits(300000)

_nf = {}


def next_fib_strict(k):
    if k in _nf:
        return _nf[k]
    a, b = 0, 1
    while b <= k:
        a, b = b, a + b
    _nf[k] = b
    return b


def fib_prefix(L):
    a, b = "0", "01"
    while len(b) < L:
        a, b = b, b + a
    return b[:L]


def psi_class(k):
    L = k + next_fib_strict(k) - 1
    y = fib_prefix(L)
    p10k = 10 ** k
    v = int(y[:k])
    s = v * v
    for r in range(L - k):
        v = 10 * v - (1 if y[r] == '1' else 0) * p10k \
            + (1 if y[r + k] == '1' else 0)
        s += v * v
    return len(str(s)) - (2 * k - 1)


def main():
    a, b = 25684, 30000   # C(a)=3, C(b)=4 (both verified)
    while b - a > 1:
        m = (a + b) // 2
        if psi_class(m) >= 4:
            b = m
        else:
            a = m
    print(f"3->4 transition: first k with C>=4 is k={b}")
    print(f"  C({b})= {psi_class(b)}, C({b-1})= {psi_class(b - 1)}")
    # Wythoff candidate
    phi2 = (3 + 5 ** 0.5) / 2
    j = round(b / phi2)
    print(f"  b/phi^2 = {b/phi2:.4f}, nearest j = {j}, floor(j*phi^2) = {int(j*phi2)}")
    for dj in range(-2, 3):
        print(f"    j={j+dj}: floor({j+dj}*phi^2) = {int((j+dj)*phi2)}")


if __name__ == "__main__":
    main()