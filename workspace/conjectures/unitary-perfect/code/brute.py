"""Naive oracle for unitary perfect numbers.

A unitary divisor of n is a divisor d | n with gcd(d, n/d) = 1, i.e. d is a
product of full prime-power components p^a || n.  sigma_star is multiplicative
over prime powers with sigma_star(p^a) = p^a + 1, so

    sigma_star(n) = prod_{p^a || n} (p^a + 1).

n is unitary perfect iff sigma_star(n) == 2 * n.

This is the deliberately naive, obviously-correct oracle: factor by trial
division, accumulate the exact integer product, compare with 2n.  No floats,
no optimisations.  Brute force at full search size is prohibited by policy; this
is only pinned to the five worked examples in problem.md.
"""
from fractions import Fraction


def factor(n):
    """Return {p: a} with p^a || n, trial division over odd integers only."""
    fs = {}
    m = n
    c = 2
    while c * c <= m:
        while m % c == 0:
            fs[c] = fs.get(c, 0) + 1
            m //= c
        c += 1 if c == 2 else 2
    if m > 1:
        fs[m] = fs.get(m, 0) + 1
    return fs


def sigma_star(n):
    """Exact sum of the unitary divisors of n, over the integers."""
    if n < 1:
        raise ValueError("n must be >= 1")
    out = 1
    for p, a in factor(n).items():
        out *= p**a + 1
    return out


def is_unitary_perfect(n):
    return sigma_star(n) == 2 * n


def product_identity(n):
    """Return prod_{p^a||n} (1 + 1/p^a) as an exact Fraction."""
    num = den = 1
    for p, a in factor(n).items():
        num *= p**a + 1
        den *= p**a
    return Fraction(num, den)


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def oracle_report(n):
    """Full report on one candidate, reproducing every worked example check."""
    fs = factor(n)
    a = fs.get(2, 0)
    ss = sigma_star(n)
    sig = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(fs.items()))
    lines = [
        f"n = {n}",
        f"  = {sig}",
        f"  sigma_star = {ss}   2n = {2*n}   UNITARY PERFECT: {is_unitary_perfect(n)}",
    ]
    # product identity: prod (1 + 1/p^a) should be exactly 2 for unitary perfect
    pi = product_identity(n)
    lines.append(f"  prod (1+1/p^a) = {pi.numerator}/{pi.denominator}"
                 + (f"  == 2: True" if pi == 2 else "  == 2: False"))
    # 2-adic budget identity: sum v2(p^e + 1) == a + 1
    budget = sum(v2(p**e + 1) for p, e in fs.items())
    odd_omega = sum(1 for p in fs if p != 2)
    lines.append(
        f"  sum v2(p^e+1) = {budget}, a+1 = {a+1}, identity: {budget == a+1}")
    lines.append(f"  omega(odd part) = {odd_omega} <= a+1 = {a+1}"
                 + (": True" if odd_omega <= a + 1 else ": False"))
    return "\n".join(lines)


if __name__ == "__main__":
    five = [6, 60, 90, 87360, 146361946186458562560000]

    # Hand-checked controls per GOAL.md: 6 is unitary perfect; 12, 28 are not.
    controls = {"6 (pos control)": 6, "12 (neg control)": 12, "28 (neg control)": 28}
    for label, n in controls.items():
        ss = sigma_star(n)
        print(f"control {label}: sigma_star = {ss} 2n = {2*n} "
              f"unitary_perfect = {is_unitary_perfect(n)}")
    print()

    for n in five:
        print(oracle_report(n))
        print()

    all_ok = all(is_unitary_perfect(n) for n in five)
    controls_ok = (is_unitary_perfect(6)
                   and not is_unitary_perfect(12)
                   and not is_unitary_perfect(28))
    print(f"ALL FIVE UNITARY PERFECT: {all_ok}")
    print(f"CONTROLS (6 yes, 12/28 no): {controls_ok}")
