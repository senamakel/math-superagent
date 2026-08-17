"""Exact brute-force dump of the k+1 Fibonacci subwords of length k, k=1..40.

Method identical to code/brute.py: build Fibonacci words S_N (S_0="0",
S_1="01", S_n = S_{n-1}+S_{n-2}) until the set of distinct length-k contiguous
substrings stabilises at size k+1. That set is exactly the (k+1) Fibonacci
subwords of length k. For each k we record the sorted factor list, Psi(k),
Psi(k) mod 101001001, the multiset of number-of-ones, and the per-position
one-counts N(i;k). All arithmetic is exact integers.

Outputs the full table to stdout and saves the sorted factor sets to
code/out/factors_k40.json (dict k -> sorted list of factor strings).
"""

import json
import os


def S(n):
    """Return the n-th Fibonacci word as a str."""
    a, b = "0", "01"
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def factors_of_length(k, N_max=32):
    """Return the stabilized set of distinct length-k factors of S_N."""
    word = S(N_max)  # one comfortably large word (|S_40| >> any k here)
    subs = {word[i:i + k] for i in range(len(word) - k + 1)}
    assert len(subs) == k + 1, f"k={k}: count {len(subs)} != k+1 in S_{N_max}"
    return subs


MOD = 101001001


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "out")
    os.makedirs(out_dir, exist_ok=True)
    factors_json = {}
    count_ok = True

    print("k : count : Psi(k) : Psi(k) mod 101001001")
    for k in range(1, 41):
        subs = factors_of_length(k)
        count_ok = count_ok and (len(subs) == k + 1)
        factors = sorted(subs)
        factors_json[str(k)] = factors

        psi = 0
        ones_multiset = []
        for s in factors:
            v = int(s)
            psi += v * v
            ones_multiset.append(s.count("1"))
        ones_multiset.sort()

        # per-position one-counts: N(i;k) = number of factors with a '1' at
        # string-position i (i counting from 0 = leftmost).
        pos_counts = [0] * k
        for s in factors:
            for i, ch in enumerate(s):
                if ch == "1":
                    pos_counts[i] += 1

        print(f"{k:2d} : {len(subs):3d} : Psi={psi} : mod={psi % MOD}"
              f" : ones{ones_multiset} : pos{pos_counts}")

    out_path = os.path.join(out_dir, "factors_k40.json")
    with open(out_path, "w") as fh:
        json.dump(factors_json, fh, indent=0)
    print()
    print("count == k+1 held for every k in 1..40:", count_ok)
    print("Saved factor sets to", out_path)

    # Print N(i;k) rows for k=8..15 as requested.
    print()
    print("Per-position one-counts N(i;k), k=8..15 (i from 0=leftmost):")
    for k in range(8, 16):
        subs = factors_of_length(k)
        factors = sorted(subs)
        pos_counts = [0] * k
        for s in factors:
            for i, ch in enumerate(s):
                if ch == "1":
                    pos_counts[i] += 1
        print(f"k={k:2d}: " + " ".join(f"{c:2d}" for c in pos_counts))


if __name__ == "__main__":
    main()
