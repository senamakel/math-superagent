"""Fibonacci-word tools for PE1006.

One subject per module: the infinite Fibonacci word S = 0100101001001...
(S_0='0', S_1='01', S_n = S_{n-1} S_{n-2}, limit word), its prefixes, the
fibonacci-index arithmetic around it, and the minimal prefix length Lmin(k)
containing all k+1 distinct length-k factors.

Every function here uses exact integer arithmetic.
"""

from bisect import bisect_right


def fibs_upto(N):
    """Fibonacci numbers F_2=1, F_3=2, ... up to N inclusive, ascending."""
    f = [1, 2]
    while f[-1] < N:
        f.append(f[-1] + f[-2])
    return f


def next_fib(k, fibs=None):
    """Least Fibonacci number (F_2=1, F_3=2, ...) strictly greater than k.

    Exact: bisection on the Fibonacci list; the list defaults to
    fibs_upto(k+1), which always contains the answer.
    """
    if fibs is None:
        fibs = fibs_upto(k + 1)
    return fibs[bisect_right(fibs, k)]


def fib_prefix(L):
    """Return a prefix of the infinite Fibonacci word of length >= L.

    Built by the doubling S_n = S_{n-1} S_{n-2} until len >= L, so the
    returned string is exactly the first len(b) characters of the limit word.
    """
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def lmin_seq(W, kmax):
    """Lmin(1..kmax) from one prefix W: for each k, the least length of a
    prefix of W containing all k+1 distinct length-k factors.

    Factor extraction is exact-integer by bit mask: W is read as a binary
    integer WI with W[0] as the most significant bit, and the factor
    W[i:i+k] is (WI >> (len(W) - k - i)) & ((1 << k) - 1).  The scan for a
    given k stops as soon as the set reaches size k+1, so per-k cost is
    O(Lmin(k)) set insertions, not O(len(W)).

    Returns a list lm with lm[k-1] = Lmin(k), or None for a k whose factor
    set did not reach k+1 within W (caller must pass W long enough; the
    safe bound is len(W) > max Lmin, in particular len(W) >= 3.5*kmax).
    """
    L = len(W)
    WI = int(W, 2)
    out = []
    for k in range(1, kmax + 1):
        s = set()
        found = None
        for i in range(L - k + 1):
            s.add((WI >> (L - k - i)) & ((1 << k) - 1))
            if len(s) == k + 1:
                found = i + k
                break
        out.append(found)
    return out


def lmin_formula(k):
    """The conjectured exact value: k + NextFib(k) - 1."""
    return k + next_fib(k) - 1