"""Check directive 1's pair-correlation/autocorrelation formula EXACTLY
(integer arithmetic) for k = F_n - 1, against the exact Psi(k) values that
brute.py and gen_sequences.py computed.

Claims being checked (directive 1):
  For n >= 2 with N = F_n, q = the standard word with N letters and m = #ones,
  the N = k+1 length-k factors at k = F_n - 1 are rotations of the truncated
  standard word, and
      Psi(k) = sum_{j,jp} C(j,jp) * 10^(2k-2-j-jp),
      C(j,jp) = A(jp - j),  A(d) = max(0,m-t)+max(0,m-(N-t)),
      t = (d*m) mod N.

We do NOT derive this; we test the exact integer equality in both directions:
  (a) enumerate the k+1 distinct factors of S_1..S_{n+1}, read them as decimal
      ints, square, sum -> Psi_brute;
  (b) construct the k+1 rotations, form each decimal value, square, sum ->
      Psi_rot;
  (c) compute Psi_corr from the autocorrelation formula A(d) with the
      geometric weights.
All three are exact integers.  Psi_brute must equal the recorded exact values.
"""

M = 101001001
# exact Psi(k) from code/out/psi_exact.txt, as a dict
exact = {}
for line in open('code/out/psi_exact.txt'):
    k, v = line.split()
    exact[int(k)] = int(v)


def fib_word(min_len):
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b


def std_word(n):
    """Standard word q_n of length F_n (n>=2), q_2='01', q_3='010', ..."""
    a, b = '0', '01'
    for _ in range(n - 2):
        a, b = b, b + a
    return b


def psi_brute(k):
    """All distinct length-k factors of a long word, decimal-square sum."""
    w = fib_word(3 * k + 5)
    facs = {w[i:i + k] for i in range(len(w) - k + 1)}
    assert len(facs) == k + 1
    return sum(int(f) ** 2 for f in facs), facs


def psi_rot(n):
    """Psi via directive 1: N rotations of the truncated standard word."""
    N = len(std_word(n))          # F_n
    q = std_word(n)
    k = N - 1
    rotvals = []
    for r in range(N):
        rot = (q[r:] + q[:r])[:k]  # rotation by r, truncated to length k
        rotvals.append(int(rot) if rot else 0)
    return sum(v * v for v in rotvals), rotvals


def psi_corr(n):
    """Psi via autocorrelation formula A(d) = max(0,m-t)+max(0,m-(N-t)),
    t = (d*m) mod N, with geometric weights 10^(2k-2-j-jp)."""
    N = len(std_word(n))
    q = std_word(n)
    m = q.count('1')
    k = N - 1
    A = [0] * N
    for d in range(N):
        t = (d * m) % N
        A[d] = max(0, m - t) + max(0, m - (N - t))
    # sum over j,jp in 0..k-1 of A[(jp-j) mod N] * 10^(2k-2-j-jp)
    # (positions measured from the left; leftmost = weight 10^(k-1))
    total = 0
    for j in range(k):
        for jp in range(k):
            total += A[(jp - j) % N] * 10 ** (2 * k - 2 - j - jp)
    return total


def main():
    print("k = F_n - 1: comparing brute, rotation, and autocorrelation formulas")
    for n in range(2, 9):          # F_2=2 -> k=1 ... F_8=34 -> k=33
        N = len(std_word(n))
        k = N - 1
        if k not in exact:
            continue
        pb, facs = psi_brute(k)
        pr, rotvals = psi_rot(n)
        pc = psi_corr(n)
        exp = exact[k]
        print(f"n={n} N={N:4d} k={k:4d}  "
              f"brute={pb}  rot={pr}  corr={pc}  exact={exp}")
        print(f"     brute==rot: {pb==pr}  brute==corr: {pb==pc}  "
              f"brute==exact: {pb==exp}  (#facs={len(facs)})")


if __name__ == '__main__':
    main()