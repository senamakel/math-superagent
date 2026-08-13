#!/usr/bin/env python3
"""CHT Theorem 1.6 hypothesis check against the real prime rows.

Normalized gaps (claim cht-normalized-gap-definition):
    a_n = (p_{n+2} - p_{n+1})/2 - 1

Compute over the window of gaps that the depth-1000 triangle spans (the first
~1.27e6 primes, sieve to 2e7):
  (1) M  = ceil(log2(max a_n))  so that a_n <= 2^M
  (2) L  = longest run of consecutive 0s among the a_n, and where it occurs
  (3) R0 = 100 * L * 8^M  (the CHT threshold for the no-{0,d}-block condition)

Then state whether R_0 is satisfiable at any depth <= 1000.

Method policy: this is a catalogue-style measurement of actual data — the
answer is read directly from the real prime gaps, not searched. Sieving to
2e7 is O(n log log n) time, O(n) space (bytearray). Exact integer arithmetic
only.
"""
from math import isqrt, log2, ceil


def primes_up_to(n):
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def main():
    LIMIT = 20_000_000
    primes = primes_up_to(LIMIT)
    num = len(primes)
    print(f"primes <= {LIMIT}: {num}")

    # normalized gaps a_n = (p_{n+2} - p_{n+1})/2 - 1, for n=1..num-2
    # (uses primes p_2..p_num, i.e. the first num-1 primes' forward gaps,
    #  matching the window the depth-1000 triangle spans)
    gaps = []
    for i in range(1, num - 1):
        g = (primes[i + 1] - primes[i]) // 2 - 1
        gaps.append(g)
    G = len(gaps)  # should be num - 2
    print(f"num normalized gaps a_n: {G}")

    max_a = max(gaps)
    M = ceil(log2(max_a))
    print(f"max a_n = {max_a}   (occurs at prime gap "
          f"{(max_a+1)*2} between some consecutive primes)")
    print(f"M = ceil(log2({max_a})) = {M}")
    print(f"check: 2^M = {2**M}  >= max a_n = {max_a}: {2**M >= max_a}")

    # longest run of consecutive 0s and where it occurs
    best_len = 0
    best_start = -1
    cur_len = 0
    cur_start = -1
    for idx, v in enumerate(gaps):
        if v == 0:
            if cur_len == 0:
                cur_start = idx
            cur_len += 1
            if cur_len > best_len:
                best_len = cur_len
                best_start = cur_start
        else:
            cur_len = 0
    print(f"L = longest run of consecutive 0s = {best_len}  (a_n=0 from "
          f"n={best_start+1} to n={best_start+best_len})")

    R0 = 100 * best_len * (8 ** M)
    print(f"R_0 = 100 * L * 8^M = 100 * {best_len} * 8^{M} = {R0}")
    print(f"log10(R_0) = {ceil(log2(R0))*log2(10)/10 if False else (__import__('math').log10(R0)):.1f}")
    print(f"depth-1000 triangle reaches depth D=1000.")
    print(f"R_0 >> 1000 ? {R0 > 1000}")
    # how deep would we need to reach to even see a {0,d}-block length R_m?
    # the CHT no-{0,d}-block condition demands no such block at depth <= 2R_{m-1}
    # with R_m >= 4 R_{m-1}; the first threshold is R_0 itself. Report.
    import math
    print(f"log2(R_0) = {math.log2(R0):.1f}")

    verdict = ("no" if R0 > 1000 else "yes")
    print(f"\nholds-here verdict: the CHT inverse theorem's R_0 threshold "
          f"= {R0}, which {'≫' if R0 > 1000 else '≤'} 1000, so the no-{{0,d}}-block "
          f"hypothesis is NOT satisfiable at any depth ≤ 1000 (actual row "
          f"count needed ~ R_0). The theorem does not bite at reachable "
          f"depths. holds-here = {verdict}")


if __name__ == "__main__":
    main()
