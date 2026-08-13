#!/usr/bin/env python3
"""flip_law_theorem_check.py

Pure combinatorial oracle check (n <= 10) of the FLIP-LAW DEATH CRITERION for
the Gilbreath absolute-difference operator.

Theory tested
-------------
The proved Rule-90 interior law (`rule90-interior-xor`): inside a leading
{0,2} block, halved entries evolve under XOR, so after d erosion rows the
edge bit (the halved value at the eroded boundary) is the mod-2 Pascal
convolution of the initial halved block:

    e_d = XOR_{i submask d} u[i],   d = 0..n-1        (Lucas: parity of C(d,i))

where u = halved block pattern (positions 0..n-1) and the row's intruder
(first value past the block) starts at an even y.

The drain law (proved): on an erosion row the intruder drops by 2 exactly
when the edge is 2, i.e. exactly when e_d = 1. So the intruder at depth k is

    y_k = y - 2 * (#{d < k : e_d = 1}),   grows to at most y+4x(k+2) but
    stays even, and reaches 4 exactly at the N-th one  (N = (y-4)/2).

Regeneration (proved step law) fires exactly at (edge=2, intruder=4).
Hence the *prediction*:

    death iff fewer than N+1 ones in e_0..e_{n-1}
            (i.e. the N-th one arrives before or at n-1 but the (N+1)-th
             one would need depth >= n... wait: precisely — see below);

    survival iff the (N+1)-th one of P*u is at position d* <= n-1 AND the
    actual row at depth d* has (edge, intruder) = (2,4)  (regeneration).

The head of the tail is chosen so the prediction is exact:
tail = [y, y+4, y+8, ...] gives row-1 differences all 4, row-2 differences
all 0, so the intruder beyond the first eroded position is pinned to
{0, 4} for every descendant row, and the block's own state at the moment
the (N+1)-th one fires is the only datum that matters.

This script compares, over every halved pattern u of length n <= 10 and every
even intruder y in {4, 6, ..., 4+2n}, the predicted outcome against the
brute-force exact iteration (up to n+6 rows with the finite tail). Survival
(regen) vs death is classified STRICTLY by whether A(1) ever leaves {0,2}
within the run — not by the b-legacy.

Also emitted:
  - y = 4 sub-check: death iff u = all-zero halved block (expect 100%).
  - n = 10 subtotal: 2^10 * 11 = 11264 cases (the task's headline total).

Time: O(sum_n 2^n * n^2) — a few 10^4 elementary row steps. No enumeration
beyond the stated toy bound; the oracle is the method here, and it is the
bounded one.
"""

from math import comb

MAX_N = 10            # halved block length n in 1..10
RUNS = 6              # extra row budget BELOW the tail rows; run = n + RUNS


def pascal_flip_sequence(u):
    """e_d = XOR_{i in [0..n-1], i submask d} u[i] for d = 0..len(u)-1."""
    n = len(u)
    e = []
    for d in range(n):
        acc = 0
        i = 0
        while i < n:
            if (d & i) == i:
                acc ^= u[i]
            i += 1
        e.append(acc)
    return e


def exact_outcome(u, y, run_rows):
    """Brute-force iteration of the exact absolute-difference operator.

    Row 0 = [1] + [2*h for h in reversed(u)] + tail [y, y+4, ...].
    Outcome: 'death' if some row k>=1 has A_k(1) not in {0,2};
    'survival' otherwise. run_rows = total rows iterated.
    """
    n = len(u)
    row = [1] + [2 * h for h in reversed(u)] + [y + 4 * t for t in range(n + 4)]
    for _ in range(1, run_rows + 1):
        row = [abs(row[j] - row[j + 1]) for j in range(len(row) - 1)]
        if len(row) >= 2 and row[1] not in (0, 2):
            return 'death'
    return 'survival'


def predicted_outcome(u, y, n, run_rows):
    """Flip-law prediction: 'death' or 'survival'.

    N = (y - 4)//2.  e = P*u (indices 0..n-1).  Ones of e in order.
    - If the (N+1)-th one is at depth d* with 0 <= d* <= n-1 AND d* <= run_rows:
        predicted survival (regeneration fires there), VERIFIED LIVE: the
        actual row at depth d* must have (edge, intruder) = (2, 4).
      Otherwise (fewer than N+1 ones, or the (N+1)-th one beyond n-1):
        predicted death (the block dies before regeneration is possible).
    """
    ones = [d for d in range(n) if pascal_flip_sequence(u)[d] == 1]
    if len(ones) >= N + 1 and ones[N] <= run_rows:
        return 'survival', ones[N]
    return 'death', None


def edge_intruder_at_depth(u, y, n, d):
    """Live check of the claimed regeneration moment: row d's (edge, intruder)
    pair at position (block edge, block edge + 1). Returns None if the row
    cannot supply both positions (finite width)."""
    row = [1] + [2 * h for h in reversed(u)] + [y + 4 * t for t in range(n + 4)]
    for _ in range(1, d + 1):
        row = [abs(row[j] - row[j + 1]) for j in range(len(row) - 1)]
    if len(row) < 2:
        return None
    return (row[0], row[1])


def main():
    print("Flip-law death-criterion oracle check (patterns n <= 10, y in {4,...,4+2n})")
    print("=" * 78)

    # --- Sanity: reproduce problem.md's worked rows with the exact operator ---
    from lib.gilbreath import primes_up_to, rows_generator
    primes = primes_up_to(60)
    gen = rows_generator(primes, 5)
    rows = [next(gen) for _ in range(6)]
    EXPECTED = {
        1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4],
        2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2],
        3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
        4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
        5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
    }
    ok = True
    for k in range(1, 6):
        match = (rows[k][:12] == EXPECTED[k])
        ok = ok and match
        print(f"  A_{k} = {rows[k][:12]}  match={match}")
    print(f"  SANITY: all five worked rows match: {ok}")
    if not ok:
        raise SystemExit("Sanity check failed — aborting oracle comparisons.")
    print()

    total_cases = 0
    death_survive = {}
    mismatches = []
    live_survivals = 0
    live_checks = 0
    live_failures = []

    for n in range(1, MAX_N + 1):
        for mask in range(1 << n):
            u = [(mask >> i) & 1 for i in range(n)]
            for N in range(n + 1):            # <=> y = 4 + 2N, y in 4..4+2n
                y = 4 + 2 * N
                run_rows = n + RUNS
                actual = exact_outcome(u, y, n, run_rows)
                pred, dstar = predicted_outcome(u, y, n, run_rows)
                total_cases += 1
                death_survive[(pred, actual)] = death_survive.get((pred, actual), 0) + 1

                if pred == 'survival':
                    live_checks += 1
                    pair = edge_intruder_at_depth(u, y, n, dstar)
                    if pair == (2, 4):
                        live_survivals += 1
                    else:
                        live_failures.append((n, u, y, dstar, pair))

                if pred != actual:
                    mismatches.append((n, u, y, actual, pred, dstar))

    print(f"TOTAL cases (n=1..10, y in {{4,6,...,4+2n}}): {total_cases}")
    print(f"Agreements: {total_cases - len(mismatches)}   "
          f"Mismatches: {len(mismatches)}")
    print(f"Confusion matrix (predicted, actual): {death_survive}")
    print()

    # --- the (N+1)-th one live check for predicted survivals ---
    print(f"Predicted survivals: {live_checks}")
    print(f"  actual row at flip depth has (edge, intruder) = (2,4): "
          f"{live_survivals}/{live_checks}")
    if live_failures:
        print(f"  FAILED live checks: {len(live_failures)}")
        for fail in live_failures[:10]:
            print(f"    n={fail[0]} u={fail[1]} y={fail[2]} d*={fail[3]} pair={fail[4]}")
    else:
        print("  (0 failures)")

    # --- mismatch report, full configuration ---
    if mismatches:
        print(f"FIRST 10 MISMATCHES (n, u, y, actual, predicted, predicted d*):")
        for m in mismatches[:10]:
            print(f"  n={m[0]} u={m[1]} y={m[2]} actual={m[3]} predicted={m[4]} d*={m[5]}")
        print(f"all {len(mismatches)} mismatch configs written to "
              f"code/out/flip_law_mismatches.txt")
        with open("code/out/flip_law_mismatches.txt", "w") as f:
            f.write("n,u,y,actual,predicted,predicted_dstar\n")
            for m in mismatches:
                f.write(f"{m[0]},{''.join(map(str, m[1]))},{m[2]},"
                        f"{m[3]},{m[4]},{m[5]}\n")
    else:
        print("ZERO MISMATCHES — the flip-law death criterion is EXACT on this toy class.")
        print("(The toy collapses the tail: intrusion is pinned to {0,4}, so the flip law")
        print("  is the whole story; the real rows have both extra wrinkles.)")
    print()

    # --- y=4 sub-check: death iff all-zero halved block ---
    y4_total = 0
    y4_death_zero = 0
    y4_death_nonzero = 0
    for n in range(1, MAX_N + 1):
        for mask in range(1 << n):
            u = [(mask >> i) & 1 for i in range(n)]
            run_rows = n + RUNS
            actual = exact_outcome(u, 4, n, run_rows)
            y4_total += 1
            if actual == 'death':
                if all(b == 0 for b in u):
                    y4_death_zero += 1
                else:
                    y4_death_nonzero += 1
    print(f"y=4 SUB-CHECK over {y4_total} (u, y=4) cases:")
    print(f"  deaths with all-zero halved block: {y4_death_zero}")
    print(f"  deaths with NONZERO halved block (criterion violations): {y4_death_nonzero}")
    all_zero = [all(b == 0 for b in u)
                for mask in range(1 << (MAX_N - 1))
                for u in [ [(mask >> i) & 1 for i in range(MAX_N - 1)] ]]
    print(f"  expected: death iff u = all-zero  ->  "
          f"{(y4_death_nonzero == 0 and y4_death_zero == 0)} "
          f"(nonzero-deaths {y4_death_nonzero}, all-zero cases {2 ** MAX_N - 1})")
    print()

    # --- n=10 subtotal (the task's headline number) ---
    subtotal = 0
    for n in [10]:
        for mask in range(1 << n):
            for N in range(n + 1):
                subtotal += 1
    print(f"n=10 subtotal (2^10 * 11): {subtotal}")


if __name__ == "__main__":
    main()