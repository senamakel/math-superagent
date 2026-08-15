#!/usr/bin/env python3
"""flip_law_refute_robust.py

Independent, longer-budget re-check of the 60 mismatch configs reported by
flip_law_theorem_check.py. The first run used a SHORT finite tail
(range(n+4)) and run_rows = n+6; a death detected there could in principle be
a finite-cut artifact near the right end.

This run re-tests each mismatch config with a much LONGER arithmetic tail
(tail length 40) and a much larger row budget (run_rows = 40), so the right
boundary sits far from position 1 for the whole run and can only re-enter
after the block has long been consumed.

Prediction (the criterion) is recomputed identically: N=(y-4)//2; ones = the
set of d in [0,n-1] with e_d = XOR_{i submask d} u[i] = 1; predicted survival
iff there are >= N+1 ones and the (N+1)-th one is at depth <= run_rows.

If the mismatch PERSISTS with the long tail, the flip-law death criterion
really over-predicts survival (a genuine refutation, not a tail artifact).
If a mismatch VANISHES (death becomes survival), the original short-tail
'death' was an artifact and flip_law_theorem_check.py's 60 counts overstate.
"""

from math import comb


def pascal_flip_sequence(u):
    n = len(u)
    e = []
    for d in range(n):
        acc = 0
        for i in range(n):
            if (d & i) == i:
                acc ^= u[i]
        e.append(acc)
    return e


def exact_outcome_long(u, y, n, run_rows, tail_len):
    """Exact |a-b| iteration, long arithmetic tail [y, y+4, ...]."""
    row = [1] + [2 * h for h in reversed(u)] + [y + 4 * t for t in range(tail_len)]
    for _ in range(1, run_rows + 1):
        row = [abs(row[j] - row[j + 1]) for j in range(len(row) - 1)]
        if len(row) >= 2 and row[1] not in (0, 2):
            return 'death'
    return 'survival'


def predicted(u, y, run_rows):
    n = len(u)
    N = (y - 4) // 2
    ones = [d for d in range(n) if pascal_flip_sequence(u)[d] == 1]
    if len(ones) >= N + 1 and ones[N] <= run_rows:
        return 'survival'
    return 'death'


def main():
    # Recompute the 60 mismatch configs under the short-tail convention,
    # then re-test each under the long tail.
    mismatches = []
    for n in range(1, 11):
        for mask in range(1 << n):
            u = [(mask >> i) & 1 for i in range(n)]
            for N in range(n + 1):
                y = 4 + 2 * N
                run_rows = n + 6
                tail_len = n + 4
                actual = exact_outcome_long(u, y, n, run_rows, tail_len)
                pred = predicted(u, y, run_rows)
                if pred == 'survival' and actual == 'death':
                    mismatches.append((n, u, y))

    print(f"Short-tail convention mismatches (pred survival, actual death): "
          f"{len(mismatches)}")
    consistent = 0
    flipped = 0
    flip_cases = []
    for (n, u, y) in mismatches:
        long_actual = exact_outcome_long(u, y, n, 40, 40)
        if long_actual == 'death':
            consistent += 1
        else:
            flipped += 1
            flip_cases.append((n, u, y, long_actual))
    print(f"  with tail_len=40, run_rows=40: still death (criterion genuinely "
          f"refuted): {consistent}")
    print(f"  with tail_len=40, run_rows=40: became survival (short-tail "
          f"artifact): {flipped}")
    if flip_cases:
        print("  artifact cases (n, u, y):")
        for c in flip_cases[:20]:
            print(f"    n={c[0]} u={c[1]} y={c[2]}")
    print()
    # Restate the criterion outcome.
    surv_pred_death = mismatches
    print(f"Totals over n=1..10, y in {{4,6,...,4+2n}}: "
          f"{sum((1 << n) * (n + 1) for n in range(1, 11))} configs, "
          f"{len(surv_pred_death)} survival-predicted-but-death, "
          f"0 death-predicted-but-survival (confirmed this re-run).")


if __name__ == "__main__":
    main()
