"""Naive oracle for Project Euler 1006.

Fibonacci subwords: contiguous substrings of some S_n, where
S_0 = "0", S_1 = "01", S_n = S_{n-1} + S_{n-2}.

Psi(k) = sum of squares of the (k+1) distinct Fibonacci subwords of length k,
interpreting each as a decimal integer (leading zeros ignored).

Naive method: build one big S_N, take every distinct contiguous substring of
length k, interpret as int, sum squares. Correct because any length-k
substring of the infinite Fibonacci word already appears in S_N once N is
large enough (S_N embeds S_{N-1}, so for k much smaller than |S_N| the set of
length-k substrings is the full set).

Exact integer arithmetic throughout.
"""


def S(n):
    """Return the n-th Fibonacci word as a Python str."""
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


def psi_brute(k, N_max=40):
    """Psi(k) by brute force using a single big Fibonacci word S_N.

    The set of length-k factors of the infinite Fibonacci word is the eventual
    value of the length-k factor set of S_N, and it is monotone in N because
    S_N is a prefix of S_{N+1}. So tightening the word (increasing N) only ever
    adds factors. We stop at the first N where the count reaches k+1, the
    stabilised value, and assert it.
    """
    prev = None
    for N in range(2, N_max + 1):
        word = S(N)
        subs = subword_set(word, k)
        assert len(subs) >= (prev or 0), "factor set not monotone"
        prev = len(subs)
        if len(subs) == k + 1:
            total = 0
            for s in subs:
                value = int(s)  # Python int() already ignores leading zeros
                total += value * value
            return len(subs), total, N
    raise RuntimeError(f"count never reached k+1 for k={k} within N_max={N_max}")


if __name__ == "__main__":
    MOD = 101001001

    # Worked example 1: k=3 -> {001,010,100,101}, Psi = 20302
    n, total3, Nused = psi_brute(3)
    print("k=3: number of distinct subwords =", n, "(expect 4)")
    print("k=3: Psi(3) =", total3, "(expect 20302)  [tightest N =", Nused, "]")

    # Worked example 2: Psi(10) mod 101001001 -> 10699667
    n, total10, Nused = psi_brute(10)
    print("k=10: number of distinct subwords =", n, "(expect 11)")
    print("k=10: Psi(10) mod", MOD, "=", total10 % MOD, "(expect 10699667)")

    print()
    print("k : count(k+1 given) : Psi(k)")
    count_ok = True
    for k in range(1, 31):
        cnt, tot, Nused = psi_brute(k)
        ok = (cnt == k + 1)
        count_ok = count_ok and ok
        print(f"{k:2d} : {cnt:3d} (N={Nused:2d}, expect {k+1:3d}, {'OK' if ok else 'FAIL'}) : {tot}")
    print()
    print("Stabilization (|set| == k+1) held for every k=1..30:", count_ok)
