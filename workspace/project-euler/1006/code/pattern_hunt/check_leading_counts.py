"""Clean check: among the k+1 distinct length-k factors of the Fibonacci word,
how many start with '1' and how many with '0'?  Use a long prefix and dedupe.

The earlier extract_subseqs.py print looked suspicious (sum != k+1), so this
recomputes it cleanly and cross-checks the total against k+1.
"""


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def main():
    W = fib_prefix(3000)
    n = len(W)
    print(f"prefix len {n}")
    for k in range(1, 31):
        facs = {W[i:i + k] for i in range(n - k + 1)}
        c1 = sum(1 for w in facs if w[0] == '1')
        c0 = sum(1 for w in facs if w[0] == '0')
        print(f"k={k:2d} total={len(facs)} (k+1={k+1})  lead-1={c1} lead-0={c0}")


if __name__ == '__main__':
    main()