"""Extend the directive-1 check: for k = F_n - 1, verify that
   (a) the k+1 factors are exactly the N rotations of the truncated standard
       word q_n (so the rotation construction equals brute-factor enumeration),
   (b) Psi from the pair-correlation/autocorrelation formula A(d) equals the
       rotation-based Psi,
for n up to 12 (k up to 143), all in exact big integers.  No 64-bit limit here.
"""


def std_word(n):
    a, b = '0', '01'
    for _ in range(n - 2):
        a, b = b, b + a
    return b


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def brute_factors(k):
    w = fib_prefix(3 * k + 8)
    return {w[i:i + k] for i in range(len(w) - k + 1)}


def psi_rot(n):
    q = std_word(n)
    N = len(q)
    k = N - 1
    return sum(int((q[r:] + q[:r])[:k]) ** 2 for r in range(N))


def psi_corr(n):
    q = std_word(n)
    N = len(q)
    m = q.count('1')
    k = N - 1
    A = [0] * N
    for d in range(N):
        t = (d * m) % N
        A[d] = max(0, m - t) + max(0, m - (N - t))
    total = 0
    for j in range(k):
        for jp in range(k):
            total += A[(jp - j) % N] * 10 ** (2 * k - 2 - j - jp)
    return total


def rotations_set(n):
    q = std_word(n)
    N = len(q)
    k = N - 1
    return {(q[r:] + q[:r])[:k] for r in range(N)}


def main():
    for n in range(2, 13):
        N = len(std_word(n))
        k = N - 1
        # (a) rotation set == brute factor set (exact string sets)
        rotset = rotations_set(n)
        bfs = brute_factors(k)
        set_ok = (rotset == bfs) and len(rotset) == k + 1
        # (b) corr formula == rot Psi
        pr, pc = psi_rot(n), psi_corr(n)
        corr_ok = (pr == pc)
        print(f"n={n:2d} N={N:4d} k={k:4d}  set==brute:{set_ok}  corr==rot:{corr_ok}"
              + (f"  Psi(rot)={pr}" if n <= 8 else ""))


if __name__ == '__main__':
    main()