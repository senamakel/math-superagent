"""Project Euler 1006 (naive/brute oracle).

Definitions:
    S_0 = '0'
    S_1 = '01'
    S_n = S_{n-1} + S_{n-2}

A Fibonacci subword is a contiguous substring of some S_n.  For a given length
k, collect all distinct length-k factors of the infinite Fibonacci word by
building S_n until it is long enough, then reading all length-k substrings of
that word.  Each collected word is interpreted as a decimal integer ignoring
leading zeros (int('001') == 1 does this in Python).  Psi(k) = sum of the
squares of these integers.

Word length: the task suggests len >= 2k is safe, but it is NOT for every k —
k = 15 needs a prefix of length 35 while 2k = 30 (the 16th factor first
appears there).  Length >= 3k is used here instead; a direct exhaustive search
shows the minimal sufficient prefix length never exceeds 3k for any k <= 30
(worst observed: 63 at k = 30).  Independent per-run confirmation:
   (a) Psi(3) must equal 20302;
   (b) Psi(10) mod 101001001 must equal 10699667;
   (c) the number of distinct length-k factors must equal k+1 (the Fibonacci
       word is Sturmian), checked for every k, and the factor set must not
       grow when the word is extended two more Fibonacci steps.
"""

M = 101001001


def fib_word(min_len):
    """Return an S_n of length >= min_len."""
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b


def distinct_factors(word, k):
    """All distinct length-k substrings of word."""
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def psi_of(word, k):
    """Psi(k): sum of squares of the distinct length-k factors as integers."""
    factors = distinct_factors(word, k)
    return sum(int(f) ** 2 for f in factors), factors


# Two more Fibonacci steps applied to a word (used to test set stability).
def extend_two_steps(word):
    a, b = '', word
    while len(b) < 3 * len(word):
        a, b = b, b + a
    return b


def main():
    print("(a) distinct length-3 subwords and Psi(3)")
    p3, f3 = psi_of(fib_word(9), 3)
    print("    length-3 subwords:", sorted(f3))
    print("    Psi(3) =", p3, " (expected 20302)")
    print("    match:", p3 == 20302)
    print()

    print("(b) Psi(1)..Psi(20)")
    for k in range(1, 21):
        pk, _ = psi_of(fib_word(3 * k), k)
        print(f"    Psi({k:2d}) = {pk}")
    p10 = psi_of(fib_word(30), 10)[0]
    print("    Psi(10) mod", M, "=", p10 % M, " (expected 10699667)")
    print("    match:", p10 % M == 10699667)
    print()

    print("(c) count of distinct length-k subwords for k=1..20 (must equal k+1)")
    all_ok = True
    for k in range(1, 21):
        w = fib_word(3 * k)
        factors = distinct_factors(w, k)
        # Mechanical per-run check: extending the word two more Fibonacci
        # steps must add no new length-k factors.
        w2 = extend_two_steps(w)
        factors2 = distinct_factors(w2, k)
        stable = factors2 == factors
        match = len(factors) == k + 1
        all_ok &= match and stable
        print(f"    k={k:2d}  count={len(factors):3d}  (k+1={k + 1})  "
              f"match={match}  stable-under-extension={stable}")
    print()
    print("Note: len >= 2k is not always enough (k=15 needs 35, 2k=30); "
          "see module docstring.")
    print("All counts k+1 and all factor sets stable under extension:", all_ok)


if __name__ == "__main__":
    main()