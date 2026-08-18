"""Digit-length class sequence C(k) = len(Psi(k)) - (2k-1), k=1..3000.

Extract the exact transition points where C(k) increases, and test:
  H1. transition points are Fibonacci numbers (or F_n +/- 1);
  H2. C(k) == len(c1(k)) - 1, or C(k) == len(k) - something;
  H3. C(k) matches floor(log10(const*k)) for some const.
Also emits a small ordered list of the class sequence for tool/OEIS use.
"""
import sys
from math import isqrt

sys.set_int_max_str_digits(20000)


def c1(k):
    N = isqrt(5 * k * k)
    t = 3 * k - N
    if t % 2 == 1:
        return 1 + (t - 1) // 2
    return 1 + (t // 2 - 1)


def load_pairs(path):
    out = {}
    with open(path) as fh:
        for line in fh:
            p = line.split()
            if len(p) >= 2:
                out[int(p[0])] = int(p[1])
    return out


def main():
    vR = load_pairs("code/out/vR_exact.txt")
    s1 = load_pairs("code/out/s1_exact.txt")
    Psi = {1: 1}
    for k in range(1, 3000):
        Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)

    C = {k: len(str(Psi[k])) - (2 * k - 1) for k in range(1, 3001)}
    trans = [k for k in range(1, 3000) if C[k + 1] != C[k]]
    print("distribution:", {v: sum(1 for k in C if C[k] == v) for v in sorted(set(C.values()))})
    print("transition points k (C(k+1) != C(k)), with C(k)->C(k+1):")
    for k in trans:
        print(f"   k={k:5d}  {C[k]} -> {C[k+1]}")

    # H1: Fibonacci test
    fibs = [1, 2]
    a, b = 1, 2
    while b < 3000:
        a, b = b, a + b
        fibs.append(b)
    print("\nFibonacci numbers <= 3000:", fibs)
    print("transitions that are Fibonacci:", [k for k in trans if k in fibs])
    print("transitions that are Fibonacci-1:", [k for k in trans if k + 1 in fibs])
    # Wythoff test: s_j = floor(j*phi^2)
    phisq = (3 + 5 ** 0.5) / 2
    wyth = {int(j * phisq) for j in range(1, 3000)}
    print("transitions in upper-Wythoff set:", [k for k in trans if k in wyth])

    # H2: compare C(k) to len(c1(k))-1
    bad2 = [k for k in range(1, 3001) if C[k] != len(str(c1(k))) - 1]
    print("\nH2 C(k) == len(c1(k))-1 :", "HOLDS" if not bad2 else f"fails at {len(bad2)}, first {bad2[:10]}")

    # H3: C(k) vs floor(log10(k)) + const: report C(k*10) samples
    print("\nsamples of k, C(k), len(c1(k))-1:")
    for k in [1, 9, 10, 23, 24, 99, 100, 137, 138, 256, 257, 999, 1000, 2583, 2584, 3000]:
        if 1 <= k <= 3000:
            print(f"  k={k:5d} C={C[k]}  len(c1)-1={len(str(c1(k)))-1}")

    # raw class sequence for OEIS (compressed run-format: value repeated, print first 120 terms)
    print("\nC(k) first 120 terms:", [C[k] for k in range(1, 121)])


if __name__ == "__main__":
    main()