"""Directive-9 contiguous-window experiment.

This deliberately implements the proposed transfer recurrence literally for a
finite doubled Fibonacci block, and compares it with the independent
mechanical-word oracle. It is an O(N) finite-block experiment, not the
forbidden single-intercept reduction and not a 10**18 solver.
"""
from lib.fibword import fib_prefix, fibs_upto, next_fib
from mech.mech_psi import mech_psi, M


def q_block(n):
    """Return the finite Fibonacci prefix of length F_n, doubled."""
    f = fibs_upto(n + 2)
    N = f[-1] if f[-1] <= n else next_fib(n, f)
    w = fib_prefix(2 * N)
    return w[:2 * N], N


def window_values(word, k, start, count):
    """Values of consecutive binary windows, by rolling decimal update."""
    v = int(word[start:start + k])
    out = [v]
    for r in range(start + 1, start + count):
        v = 10 * v - int(word[r - 1]) * (10 ** k) + int(word[r + k - 1])
        out.append(v)
    return out


def transfer_prefix(word, k, upto):
    """Prefix sums (sum v, sum v^2) from the rolling transfer recurrence."""
    vals = window_values(word, k, 0, upto)
    s1 = s2 = 0
    for v in vals:
        s1 = (s1 + v) % M
        s2 = (s2 + v * v) % M
    return s1, s2


def block_summary(word, k, start, count):
    """Constant-size transfer summary (count,sum v,sum v^2) for a block."""
    vals = window_values(word, k, start, count)
    return (len(vals), sum(vals) % M, sum(v * v for v in vals) % M)


def compose(left, right):
    """Composition law for the additive second-moment transfer summary."""
    return (left[0] + right[0], (left[1] + right[1]) % M,
            (left[2] + right[2]) % M)


def check(max_k=150):
    failures = []
    for k in range(1, max_k + 1):
        # Pick a strict Fibonacci length N>k.  The finite experiment uses the
        # actual infinite-word prefix; no intercept enumeration is involved.
        N = next_fib(k, fibs_upto(k + 1))
        w = fib_prefix(2 * N)
        start = N - k - 1
        got = block_summary(w, k, start, k + 1)[2]
        want = mech_psi(k)[0] % M
        if got != want:
            failures.append((k, got, want))
    return failures


def check_composition(max_k=150):
    """Check summary composition after every split of the target block."""
    failures = []
    for k in range(1, max_k + 1):
        N = next_fib(k, fibs_upto(k + 1))
        w = fib_prefix(2 * N)
        start, count = N - k - 1, k + 1
        whole = block_summary(w, k, start, count)
        split = count // 2
        joined = compose(block_summary(w, k, start, split),
                         block_summary(w, k, start + split, count - split))
        if whole != joined:
            failures.append((k, whole, joined))
    return failures


if __name__ == "__main__":
    bad = check()
    print("directive9 finite transfer checks k=1..150:", "PASS" if not bad else "FAIL")
    if bad:
        print("first failures:", bad[:5])
    comp = check_composition()
    print("summary composition checks k=1..150:", "PASS" if not comp else "FAIL")
    for k in (3, 10):
        N = next_fib(k, fibs_upto(k + 1))
        w = fib_prefix(2 * N)
        start = N - k - 1
        got = block_summary(w, k, start, k + 1)[2]
        print(k, N, got, mech_psi(k)[0] % M)
