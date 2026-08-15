#!/usr/bin/env python3
"""
FIXED oracle for the dyadic-periodicity dichotomy (Directive 60 item 3).

REPLACES the defective code/out/dyadic_periodic_check.py, which was VACUOUS:
make_input_gaps() prepended a leading gap-1 for the 2->3 difference AND
build_triangle() did row=[1]+list(gaps), so A_1 = (1,1,2,4,...) had an ODD
second entry, the {0,2} regime never formed, and nu2 = 0 for every period.

FIX: build the proper 2-then-odds absolute-difference triangle using the
canonical streaming generator lib.gilbreath.rows_generator (one row live),
whose A_0 = q = the actual 2,3,5,7,...-type integer sequence. Then A_1 = the
differences = (1, even, even, ...) with second entry 2 (not 1), reproducing
the problem.md worked row, and nu2 is the literal count of 2s in the maximal
{0,2} suffix of the right diagonal through q_n.

Route A (this script): lib.gilbreath.rows_generator, half-diagonal extracted
per row, literal maximal-{0,2}-suffix count.
Route B (cross-check): lib.rightdiag.incremental_diagonals + cycle_and_nu2
(canonical convention), the same code path as dyadic_periodicity_correct.py,
so the two agree on the qualitative dichotomy AND this script independently
re-derives the on-disk numbers.

Validation embedded:
  1. A_1 (real primes) reproduces problem.md's (1,2,2,4,2,4,2,4,6,2,...).
  2. For each period P in {1,3,5,6,7,9,11,13,15} (odd factor) nu2 grows
     roughly linearly (~c*P n, c(P)>0).
  3. For each power of 2 P in {1,2,4,8,16} nu2 is O(1) (bounded).

Exact integers only; streaming O(W*D) with one row live.
"""
from lib.gilbreath import primes_up_to, rows_generator
from lib.rightdiag import incremental_diagonals, cycle_and_nu2

EXPECTED_A1 = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4]


def build_seq(h_pattern, n_terms):
    """q_1..q_{n_terms} from periodic bit pattern; q_1=2, q_2=3, and for the
    (m)-th appended term the gap is q_{m-1}->q_m governed by
    h[(m-3) % period], gap = 2 if bit else 4.  Exactly the construction of
    dyadic_periodicity_correct.py: h[0] governs gap 3->5."""
    q = [2, 3]
    period = len(h_pattern)
    while len(q) < n_terms:
        m = len(q) + 1          # we are appending q_m
        j = m - 3               # bit index for gap q_{m-1}->q_m (h[0]=gap 3->5)
        bit = h_pattern[j % period]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def nu2_routeA(word, n):
    """Streaming route: build triangle via rows_generator, extract the right
    diagonal half-diagonal of q_n = the integer q[n], count 2s in the maximal
    {0,2} suffix of the body (excluding the terminal left-edge entry).
    A_k[n-k] for k=0..n is the right diagonal through q_n."""
    q = build_seq(word, n + 1)
    rows = rows_generator(q, n)          # A_0..A_n, one row live
    d = [None] * (n + 1)
    for k, row in enumerate(rows):       # k=0..n
        if n - k < len(row):
            d[k] = row[n - k]
    # maximal {0,2} suffix of the body d[0..n-1] (exclude terminal A_n[0])
    body = d[:-1]
    i = len(body)
    while i > 0 and (i - 1) < len(body) and body[i - 1] in (0, 2):
        i -= 1
    return body[i:].count(2)


def nu2_routeB(word, n):
    """Canonical route: incremental_diagonals + cycle_and_nu2 (same path as
    dyadic_periodicity_correct.py)."""
    q = build_seq(word, n + 1)
    diags = list(incremental_diagonals(q))
    tau, nu2 = cycle_and_nu2(diags[n])
    return nu2


def validate_a1():
    P = primes_up_to(80)
    rows = list(rows_generator(P, 1))
    got = rows[1][:12]
    ok = (got == EXPECTED_A1)
    print(f"validation A_1: got {got}")
    print(f"validation A_1 == problem.md: {ok}")
    return ok


def dichotomy_table(ns, route):
    """Periods 1..16, two words each (tail-1 and alt), nu2 at the given n's.
    Returns (rows, classification_report)."""
    print(f"\n=== dichotomy over n={ns} (route {route}) ===")
    print(f"{'P':>3} {'word':>9} " + "".join(f"n={n:<9}" for n in ns) + "  class")
    classes = {}
    for P in range(1, 17):
        w1 = [0] * (P - 1) + [1]                       # tail-1 word
        w2 = [1 if (i % 2 == 0) else 0 for i in range(P)]  # alt word
        rows = []
        for tag, w in (("tail1", w1), ("alt", w2)):
            vals = [nu2_routeA(w, n) if route == "A" else nu2_routeB(w, n) for n in ns]
            # classify by growth of the last value relative to the first
            grow = (vals[-1] > vals[0] * (ns[-1] // max(ns[0], 1)) // 2)
            classes.setdefault(P, set()).add("grow" if (vals[-1] > 2 * vals[0] or vals[-1] > ns[-1] // 4) else "O(1)")
            print(f"{P:>3} {tag:>9} " + "".join(f"{v:<9}" for v in vals) +
                  ("  GROW" if (vals[-1] > 2 * vals[0] or vals[-1] > ns[-1] // 4) else "  O(1)"))
    return classes


def is_power2(P):
    return (P & (P - 1)) == 0


def main():
    print("FIXED dyadic-periodicity oracle (Directive 60 item 3)")
    print("=" * 72)
    ok_a1 = validate_a1()

    print("\n--- small-n check of the fix: compare route A vs route B on the")
    print("    defective period set at n=200,400,800,1200 ---")
    tests = [
        ("period 1 h=1", [1]),
        ("period 3 h=001", [0, 0, 1]),
        ("period 5 h=00001", [0, 0, 0, 0, 1]),
        ("period 7 h=0000001", [0, 0, 0, 0, 0, 0, 1]),
        ("period 2 h=01", [0, 1]),
        ("period 4 h=0001", [0, 0, 0, 1]),
    ]
    ns = [200, 400, 800, 1200]
    print(f"{'period':>16} {'n':>5} {'routeA':>7} {'routeB':>7} {'agree':>6}")
    for name, w in tests:
        for n in ns:
            a = nu2_routeA(w, n)
            b = nu2_routeB(w, n)
            print(f"{name:>16} {n:>5} {a:>7} {b:>7} {str(a==b):>6}")

    print("\n=== GROWTH CLASSIFICATION: odd-factor periods must GROW,")
    print("    powers of 2 must be O(1) (route A, streaming) ===")
    ns2 = [200, 500, 1000, 2000, 4000]
    classes = dichotomy_table(ns2, "A")

    print("\n=== Classification summary ===")
    all_ok = True
    for P in range(1, 17):
        cls = classes.get(P, set())
        expected_grow = not is_power2(P)
        growish = any(c == "grow" for c in cls)
        hit = (growish == expected_grow)
        all_ok &= hit
        print(f"P={P:>2} power_of_two={is_power2(P)} classes={sorted(cls)} "
              f"predict={'grow' if expected_grow else 'O(1)'} hit={hit}")
    print("\ncondition: odd-factor periods grow, powers of 2 collapse ->",
          "PASS" if (all_ok and ok_a1) else "FAIL")

    # sanity: at least one odd-factor period actually linear (not degenerate)
    v200 = nu2_routeA([0, 0, 1], 200)
    v4000 = nu2_routeA([0, 0, 1], 4000)
    print(f"\nsanity: P=3 tail-1 nu2(200)={v200} nu2(4000)={v4000} "
          f"growth={'linear' if v4000 > 10*v200 else 'weak'}")
    return 0 if (all_ok and ok_a1) else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
