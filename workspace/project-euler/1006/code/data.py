"""Data generation for Project Euler 1006, building on brute.py.

(a) For k=1..12, print the DISTINCT length-k Fibonacci subwords (the actual
    binary strings) and, for each, its integer value.
(b) Compute Psi(k) exactly for k=1..150 by scanning a Fibonacci word S_n with
    |S_n| >= 3k, extracting all contiguous length-k substrings, deduping,
    verifying count == k+1, and summing the squares of the integer values.

Exact integer arithmetic throughout.
"""

import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def S(n):
    """Return the n-th Fibonacci word as a str: S_0="0", S_1="01", S_n=S_{n-1}S_{n-2}."""
    a, b = "0", "01"
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def subword_set(word, k):
    """Set of all distinct contiguous substrings of `word` of length k."""
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def word_len(n):
    """|S_n|. |S_0|=1, |S_1|=2, |S_n|=|S_{n-1}|+|S_{n-2}| (F_{n+2})."""
    a, b = 1, 2
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def psi_scan(k, N_MAX=40):
    """Psi(k) by scanning a Fibonacci word S_n with |S_n| >= 3k.

    Returns (count, psi, N_used, word_len). The set of length-k factors of the
    infinite Fibonacci word stabilises at exactly k+1 elements (standard
    Sturmian/factorisation fact); we pick the smallest n with |S_n| >= 3k and
    assert the count reaches k+1.
    """
    # smallest n with |S_n| >= 3k
    n = 0
    while word_len(n) < 3 * k:
        n += 1
    assert n <= N_MAX
    word = S(n)
    subs = subword_set(word, k)
    cnt = len(subs)
    assert cnt == k + 1, f"k={k}: count {cnt} != k+1={k+1}"
    total = sum(int(s) ** 2 for s in subs)
    return cnt, total, n, word_len(n)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # ---- (a) factor words for k=1..12 ----
    factor_lines = []
    factor_lines.append("Distinct length-k Fibonacci subwords and their integer values (k=1..12)")
    factor_lines.append("-" * 60)
    for k in range(1, 13):
        n = 0
        while word_len(n) < 3 * k:
            n += 1
        subs = sorted(subword_set(S(n), k))
        factor_lines.append(f"k={k} (count={len(subs)}, expected {k+1}):")
        for s in subs:
            factor_lines.append(f"    {s!r:>20}  int = {int(s)}")
        factor_lines.append("")
    factor_text = "\n".join(factor_lines)
    print(factor_text)

    factors_path = os.path.join(OUT_DIR, "factors_k12.txt")
    with open(factors_path, "w") as f:
        f.write(factor_text)

    # ---- (b) Psi(k) for k=1..150 ----
    psi_lines = []
    psi_lines.append("Psi(k) = sum of squares of the (k+1) distinct Fibonacci subwords of length k,")
    psi_lines.append("each interpreted as a decimal integer (leading zeros ignored).")
    psi_lines.append("Computed by scanning S_n with |S_n| >= 3k; count == k+1 verified for every k.")
    psi_lines.append("-" * 60)
    psi_lines.append(" k : count==k+1 : |S_n|>=3k : Psi(k)")
    count_ok = True
    for k in range(1, 151):
        cnt, total, n_used, wlen = psi_scan(k)
        ok = (cnt == k + 1)
        count_ok = count_ok and ok
        psi_lines.append(f"{k:3d} : {ok!s:>5} : n={n_used:2d},|S|={wlen:4d} : {total}")
    psi_text = "\n".join(psi_lines)
    print(psi_text)

    psi_path = os.path.join(OUT_DIR, "psi_data_1_150.txt")
    with open(psi_path, "w") as f:
        f.write(psi_text)

    print()
    print("count == k+1 held for every k=1..150:", count_ok)
    print("Wrote:", factors_path)
    print("Wrote:", psi_path)


if __name__ == "__main__":
    main()
