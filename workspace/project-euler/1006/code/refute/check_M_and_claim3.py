"""Check two asserted-but-unverified facts that gate PE1006.

(1) M = 101001001 is prime  (directive asserts it is; CONTEXT marks it
    "asserted, not shown".)
(2) Directive 9 Claim 3: for ANY k < F_n, the full CYCLIC sum over all F_n
    windows of the doubled standard word q_n q_n equals
        sum_{j,jp} A(jp-j) * 10^(2k-2-j-jp)
    with A(d) = cyclic autocorrelation of q_n = # positions i where digit i
    and digit (i+d) are both 1 (cyclically).  This is the corrected Toeplitz
    identity that the final O(log) reduction rests on.

Here the "cyclic windows" are the F_n contiguous length-k windows of q_n q_n
starting at positions 0..F_n-1 (every cyclic shift).  Their sum of decimal
values squared, mod M, is compared against the Toeplitz collapse.
"""
from fractions import Fraction
from sympy import isprime

M = 101001001


def fibs(n):
    out = [0, 1]
    while len(out) <= n:
        out.append(out[-1] + out[-2])
    return out


def standard_word(n):
    """Standard Sturmian word q_n with |q_n| = F_n (0-based: q_0='0', q_1='01',
    q_n = q_{n-1} q_{n-2})."""
    if n == 0:
        return '0'
    if n == 1:
        return '01'
    a, b = '0', '01'
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def cyclic_windows(q, k):
    """All F_n cyclic length-k windows of q q starting at 0..F_n-1."""
    qq = q + q
    N = len(q)
    return [qq[r:r + k] for r in range(N)]


def A_cyclic(q, d):
    """Cyclic autocorrelation: count positions i with q[i]=='1' and q[(i+d)%N]=='1'."""
    N = len(q)
    return sum(1 for i in range(N) if q[i] == '1' and q[(i + d) % N] == '1')


def claim3_test(nmin, nmax):
    """Compare cyclic-window sum-of-squares vs Toeplitz collapse for all k < F_n."""
    F = fibs(nmax + 2)
    bad = []
    tested = 0
    for n in range(nmin, nmax + 1):
        q = standard_word(n)
        N = F[n]
        m = sum(1 for c in q if c == '1')
        for k in range(1, N):  # ANY k < F_n
            wins = cyclic_windows(q, k)
            # cyclic sum = sum of (decimal value of window)^2  (mod M)
            cyclic = sum(int(w) ** 2 for w in wins) % M
            # Toeplitz collapse: sum_{j,jp} A(jp-j) 10^(2k-2-j-jp) mod M
            col = 0
            for j in range(k):
                for jp in range(k):
                    col += A_cyclic(q, (jp - j) % N) * 10 ** (2 * k - 2 - j - jp)
            col %= M
            tested += 1
            if cyclic != col:
                bad.append((n, k, cyclic, col))
                if len(bad) >= 5:
                    return bad, tested
    return bad, tested


if __name__ == "__main__":
    print("(1) M primality:")
    print(f"    isprime(101001001) = {isprime(M)}")

    print("\n(2) Directive-9 Claim 3 (Toeplitz cyclic sum for ANY k < F_n):")
    bad, tested = claim3_test(2, 8)
    print(f"    tested (n,k) pairs with k<F_n: {tested}")
    if bad:
        for n, k, cyc, col in bad:
            print(f"    MISMATCH n={n} (F_n={fibs(n)}) k={k}: cyclic={cyc} collapse={col}")
    else:
        print("    ALL MATCH: cyclic sum == Toeplitz collapse for every k < F_n, n=2..8")
