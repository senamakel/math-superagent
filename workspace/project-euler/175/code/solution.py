#!/usr/bin/env python3
"""
Project Euler 175 -- efficient peeling solution.

f(0)=1; for n>=1 f(n) = # ways to write n as a sum of powers of 2 with each
2^k used at most twice.

Idea (proven recurrences from brute table): with r_n = f(n)/f(n-1),
    r_{2n}   = 1 + r_n            (n even -> LSB 0)
    r_{2n+1} = r_n / (1 + r_n)    (n odd, n>1 -> LSB 1)
with r_1 = 1/1 (the stopping root).

Peeling (inverse), p/q reduced, collect bits LSB-first:
    p > q : LSB 0, previous ratio (p-q)/q
    p < q : LSB 1, previous ratio p/(q-p)
    p == q: stop (n = 1).
MSB-first binary = "1" + reversed(bits).

Complexity: one iteration per output bit -> O(k) time/space with k = |binary n|.
No search over n.
"""

from fractions import Fraction


def peel(p, q):
    """Return (binary_str_MSB_first, sbe_run_lengths) for ratio p/q = f(n)/f(n-1)."""
    bits = []  # LSB-first
    # work on a mutable copy
    a, b = p, q
    while a != b:
        if a > b:
            bits.append(0)
            a, b = a - b, b
        else:
            bits.append(1)
            a, b = a, b - a
    # a == b == gcd, n = 1 root
    # binary MSB first is "1" followed by reversed(bits)
    binary = "1" + "".join(str(x) for x in reversed(bits))
    # run-length encode (MSB first)
    runs = []
    cur = binary[0]
    length = 1
    for ch in binary[1:]:
        if ch == cur:
            length += 1
        else:
            runs.append(length)
            cur = ch
            length = 1
    runs.append(length)
    return binary, runs


def forward_binary(binary):
    """From reconstructed binary (MSB first) recompute r_n = f(n)/f(n-1)."""
    r = Fraction(1, 1)  # n = 1
    for ch in binary[1:]:  # skip the leading '1'
        if ch == '0':
            r = 1 + r
        else:
            r = r / (1 + r)
    return r


def main():
    TARGET = Fraction(123456789, 987654321)

    # ---- (a) worked example -------------------------------------------------
    ex_bin, ex_runs = peel(13, 17)
    print("[a] worked example peel(13,17):")
    print(f"    binary = {ex_bin}")
    print(f"    SBE = {ex_runs}")
    assert ex_bin == "11110001", ex_bin
    assert ex_runs == [4, 3, 1], ex_runs
    print("    -> matches binary=11110001, SBE=[4,3,1]  OK")
    print()

    # ---- (b) cross-check against brute.py -----------------------------------
    import brute
    N = 5000
    f = brute.f_table(N)
    checked = 0
    for n in range(2, N + 1):
        if f[n - 1] == 0:
            continue
        b, runs = peel(f[n], f[n - 1])
        assert b == bin(n)[2:], f"mismatch at n={n}: {b} vs {bin(n)[2:]}"
        checked += 1
    print(f"[b] cross-check vs brute.py: f up to {N}, checked n=2..{N} with f[n-1]!=0")
    print(f"    checked {checked} values; all peel(f[n],f[n-1]) == bin(n)[2:]  OK")
    print()

    # ---- final answer --------------------------------------------------------
    fin_bin, fin_runs = peel(TARGET.numerator, TARGET.denominator)
    print("[c] final answer:")
    print(f"    reconstructed binary = {fin_bin}")
    print(f"    SBE = {fin_runs}")

    # forward independent check (second route)
    fwd = forward_binary(fin_bin)
    print(f"    forward recompute ratio from {fin_bin} = {fwd}")
    assert fwd == TARGET, (fwd, TARGET)
    print(f"    forward check == {TARGET}  OK")
    print()

    # ---- (3) print comma-separated with no whitespace ------------------------
    answer = ",".join(str(x) for x in fin_runs)
    print("[final answer]")
    print(answer)


if __name__ == "__main__":
    main()
