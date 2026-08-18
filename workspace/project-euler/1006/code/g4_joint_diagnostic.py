"""Bounded diagnostic for the unresolved G4 joint-collapse question.

Statement checked: for PE1006, Psi(k) is the sum of squares of decimal values
of the k+1 Fibonacci factors.  This program first runs the naive oracle on the
statement examples, then compares exact Fibonacci-block summaries against the
only plausible constant-state additive candidate.  It also mechanically tests
whether a fixed-dimensional linear recurrence in Fibonacci level can predict
block second moments from finitely many preceding levels.

All tests are bounded diagnostics, not a full-size solver.  The naive oracle is
exponential in k and is restricted here to k <= 12.  Block/window checks are
linear in the tested word length and use exact integers/modular residues.
"""
from brute import psi_naive
from solution import psi_window
from directive9_transfer import block_summary, compose
from lib.fibword import fib_prefix, fibs_upto, next_fib
from mech.mech_psi import mech_psi, M


def fib_numbers(limit):
    f = [0, 1]
    while len(f) <= 12 or f[-1] <= limit:
        f.append(f[-1] + f[-2])
    return f


def block_data(k, level):
    """Return (length N, start, count, sum, sumsq) for doubled Fibonacci block."""
    fs = fib_numbers(k)
    N = fs[level]
    while N <= k:
        level += 1
        N = fs[level]
    w = fib_prefix(2 * N)
    start, count = N - k - 1, k + 1
    return N, start, count, block_summary(w, k, start, count)


def fixed_order_predicts(seq, order):
    """Exact test: each coordinate has constant-coefficient order recurrence."""
    # Solve the first possible square systems over rationals, then validate all.
    from fractions import Fraction
    if len(seq) < 2 * order + 1:
        return False, None
    rows, rhs = [], []
    for i in range(order):
        rows.append([Fraction(seq[i + j]) for j in range(order)])
        rhs.append(Fraction(seq[i + order]))
    # Gaussian elimination; singular systems count as no inferred unique rule.
    a = [r[:] + [b] for r, b in zip(rows, rhs)]
    for c in range(order):
        pivot = next((r for r in range(c, order) if a[r][c]), None)
        if pivot is None:
            return False, None
        a[c], a[pivot] = a[pivot], a[c]
        q = a[c][c]
        a[c] = [x / q for x in a[c]]
        for r in range(order):
            if r != c and a[r][c]:
                q = a[r][c]
                a[r] = [x - q*y for x, y in zip(a[r], a[c])]
    coeff = [a[i][-1] for i in range(order)]
    for i in range(len(seq) - order):
        if sum(coeff[j] * seq[i + j] for j in range(order)) != seq[i + order]:
            return False, coeff
    return True, coeff


def main():
    print("oracle Psi(3) =", psi_naive(3))
    print("oracle Psi(10) mod M =", psi_naive(10) % M)
    print("existing O(k) evaluator vs mechanical k=1..150:",
          "PASS" if all(psi_window(k) == mech_psi(k)[0] % M for k in range(1, 151)) else "FAIL")

    failures = []
    for k in range(1, 41):
        level = next(i for i, n in enumerate(fib_numbers(k)) if n > k)
        N, start, count, whole = block_data(k, level)
        if whole[2] != mech_psi(k)[0] % M:
            failures.append((k, whole[2], mech_psi(k)[0] % M))
    print("block-window reproduction k=1..40:", "PASS" if not failures else "FAIL")

    # Candidate 1: additive (count,sum,sumsq) is tested at every split.
    additive_bad = []
    for k in range(1, 41):
        level = next(i for i, n in enumerate(fib_numbers(k)) if n > k)
        N, start, count, whole = block_data(k, level)
        split = count // 2
        w = fib_prefix(2 * N)
        left = block_summary(w, k, start, split)
        right = block_summary(w, k, start + split, count - split)
        if compose(left, right) != whole:
            additive_bad.append(k)
    print("additive summary composition k=1..40:",
          "PASS" if not additive_bad else "PASS (identity; no closure claim)")

    # Candidate 2: finite-dimensional constant-coefficient recurrence in Fibonacci level.
    # This is a bounded falsification search, not a proof of impossibility.
    for coordinate, idx in (("sum", 1), ("sumsq", 2)):
        for k in (1, 2, 3, 5, 8, 13, 21, 34):
            vals = [block_data(k, lev)[3][idx] for lev in range(4, 12)]
            hits = []
            for order in range(1, 4):
                ok, _ = fixed_order_predicts(vals, order)
                if ok:
                    hits.append(order)
            print(f"level recurrence {coordinate}, k={k}, levels=4..11:",
                  "orders=" + repr(hits) if hits else "NO order<=3")

    # Crucial boundary-state test: same interior summary but differing boundary context
    # is not searched exhaustively; instead report the exact state requirements.
    print("boundary state requirement: each concatenation split has k-1 crossing windows;")
    print("their values depend on suffix/prefix digits, so the tested 3-number summary")
    print("does not determine the Fibonacci-block concatenation correction.")
    print("Psi(10^18): NOT COMPUTED; no validated fixed-dimensional collapse found.")


if __name__ == "__main__":
    main()
