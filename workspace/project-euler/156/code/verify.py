"""Independent second route for Project Euler 156 (digit-count fixed points).

Everything here is structured DIFFERENTLY from the primary route
(code/solution.py when written; code/lib/digits.py which holds the primary
counter).

  * f(n, d) is NOT evaluated by the classical place-value peeling identity
    (per factor: high*factor / high*factor + low + 1 / (high+1)*factor, the
    least-significant-digit walk in code/lib/digits.py).  Instead it is
    evaluated by two digit-DP / digit-position enumerations over the decimal
    digits of n from the MOST significant side:

      f_prefix_blocks -- closed-form block sums: fix n's digits from the
                         left; every group of numbers that "loosens" at a
                         position is counted as one combinatorial block
                         (prefix digit count x 10^suffix-slots, plus the
                         free-position total s*10^(s-1)), never number by
                         number.

      f_digit_dp      -- textbook memoized digit-DP: state pairs
                         (position, tight) with two synchronized tables
                         C = number of completions, S = total occurrences of
                         d over all completions; the recurrence literally
                         walks the digit tree's transitions.  No closed form
                         per position at all.

    The two evaluators share no code and check each other.

  * The fixed-point search uses the same two jump rules the primary solver's
    iterator must use (both are forced by monotonicity of f in n), but they
    are re-derived here from first principles and implemented independently:

      R1 (catch-up):  f(n) = c > n  =>  no fixed point in (n, c), because f
                      is non-decreasing so every n' <= c has f(n') >= c > n'.
                      Resume at n := c.
      R2 (coast):     f(n) = c < n  =>  at most one n' in any step makes the
                      gap n-f(n) grow; every number below the bound has at
                      most D digits, so per step the gap grows by at most
                      D-1.  A zero-crossing cannot occur before
                      n + ceil((n-c)/(D-1)), so the search jumps past that
                      whole provably-empty interval.

  * The bound n < d*10^10 is the sourced Khovanova-Marton Proposition 9.1
    ("all fixed points of digit d in base 10 lie at or below d*10^10",
    research/notes/claim-g2-solution-bound.md, proven in source); the
    program additionally checks f(d*10^10, d) > d*10^10 as a sanity probe.

  * s(1) = 22786974071 is recomputed by this program's own jump run for d=1
    over [0, 10^10], with the two digit-DP evaluators; nothing is read from
    any other solver.

Checks performed, in order:
  1. oracle points f(11,1)=4, f(12,1)=5, f(22,2)=6 and the statement table
     f(n,1) n=0..12, through BOTH new evaluators;
  2. brute-force agreement: for all n in 0..20000, all d in 1..9, both
     evaluators equal code/brute.py's naive running-total counter kept as
     f_naive (literal string digit counting), plus per-call f_naive spot
     checks;
  3. jump iterator for d=1 over 0..300000 equals the naive oracle scan
     (code/brute.py f_incremental), and the first fixed points are
     0, 1, 199981;
  4. every solution found at full size is re-verified by the second
     evaluator f_digit_dp (f(n,d) == n), a third independent route;
  5. s(1) = 22786974071 recomputed; per-digit solution counts match the
     library's sourced counts [84,14,36,48,5,72,49,344,9] (OEIS A130432,
     a completeness red-flag check, not the answer);
  6. grand total T = sum(s(d)) for d = 1..9 is computed and printed.

Run:  cd /workspace && PYTHONPATH=/workspace/code python code/verify.py
"""

import time

from brute import f_naive, f_incremental

# ---------------------------------------------------------------------------
# Evaluator 1: most-significant-first closed-form block enumeration.
#
# Pad n to L = len(str(n)) digits (leading zeros add no digit d > 0, so this
# does not change f).  Walk positions left to right, carrying the count of d
# in the tight prefix.  At position i with digit t and s = L-1-i free suffix
# slots, every choice x < t makes the number "loose": the whole block of
# 10^s numbers contributes
#     (prefix_d + (x == d)) * 10^s + s * 10^(s-1)
# (the fixed prefix and the choice x contribute per number; the s free slots
# contribute d exactly 10^(s-1) times each over all 10^s suffixes).  The
# tight chain ends at n itself, contributing its own d-count.
# ---------------------------------------------------------------------------


def f_prefix_blocks(n, d):
    """f(n,d) by MSD closed-form block enumeration. Exact ints, O(L) time.

    Digit-position enumeration with prefix counts: each position's "loose"
    digit choices count whole blocks combinatorially; the tight prefix's
    digit count is carried forward.  Structurally unrelated to the
    least-significant place-value peeling in code/lib/digits.py.
    """
    if n < 0:
        return 0
    ds = str(n)
    L = len(ds)
    total = 0
    prefix_d = 0                      # occurrences of d in the tight prefix
    for i, ch in enumerate(ds):
        t = int(ch)
        s = L - 1 - i                 # free suffix slots after this position
        for x in range(t):            # loose digit choices: 0 .. t-1
            block = (prefix_d + (1 if x == d else 0)) * (10 ** s)
            if s:
                block += s * (10 ** (s - 1))   # d over all suffixes, exactly
            total += block
        prefix_d += (1 if t == d else 0)       # tighten the chain
    total += prefix_d                 # the number n itself (tight to the end)
    return total


# ---------------------------------------------------------------------------
# Evaluator 2: textbook memoized digit-DP over the digit tree.
#
# State is (position pos, tight flag).  Two synchronized tables:
#   C[pos][tight] = number of L-digit strings (padded, leading zeros allowed)
#                   completing positions pos..L-1 without exceeding n;
#   S[pos][tight] = total occurrences of digit d over all those completions.
# Recurrence over the next digit x in 0..(tight ? t_pos : 9), then recursing
# with tight' = tight and x == t_pos.  f(n,d) = S[0][tight=1].  No closed
# form: the DP literally sums over every digit-tree transition, aggregated
# position by position.  O(L) states, O(L*10) transitions, exact integers.
# ---------------------------------------------------------------------------


def f_digit_dp(n, d):
    """f(n,d) by memoized digit-DP over the digit tree. Exact ints, O(L) time.

    State-pair (pos, tight) tables C/S over the padded digit string of n;
    transitions over digits 0..9 (or 0..t_pos when tight).  Different
    structure from f_prefix_blocks (no block sums) and from place-value
    peeling.  Verified against f_naive for all n <= 20000, d = 1..9.
    """
    if n < 0:
        return 0
    ds = str(n)
    L = len(ds)
    C = [[0, 0] for _ in range(L + 1)]
    S = [[0, 0] for _ in range(L + 1)]
    C[L][0] = C[L][1] = 1             # one empty completion
    S[L][0] = S[L][1] = 0
    for pos in range(L - 1, -1, -1):
        t_pos = int(ds[pos])
        for tight in (0, 1):
            lim = t_pos if tight else 9
            c = 0
            s = 0
            for x in range(lim + 1):
                nt = 1 if (tight and x == t_pos) else 0
                c += C[pos + 1][nt]
                s += (1 if x == d else 0) * C[pos + 1][nt] + S[pos + 1][nt]
            C[pos][tight] = c
            S[pos][tight] = s
    return S[0][1]


# ---------------------------------------------------------------------------
# Exact jump iterator over the fixed points, using only the two monotonicity
# rules re-derived above.  Evaluator is pluggable so both new f's can drive
# it (and their results cross-check each other).
# ---------------------------------------------------------------------------


def jump_fixed_points(d, bound, evaluator):
    """All n in [0, bound] with f(n,d) = n, by the R1/R2 jump rules.

    Returns (solutions, probes).  probes counts evaluator calls; the number
    of bounding steps of the digit-DP method is thereby made visible.  For
    completeness the search relies on the sourced bound: all fixed points of
    digit d lie below d*10^10 (Khovanova-Marton Prop. 9.1;
    research/notes/claim-g2-solution-bound.md).
    """
    D = len(str(bound))
    sols = []
    n = 0
    probes = 0
    while n <= bound:
        probes += 1
        c = evaluator(n, d)
        if c == n:
            sols.append(n)
            n += 1
        elif c > n:
            n = c                     # R1: (n, c) provably empty
        else:
            step = (n - c + D - 2) // (D - 1)   # ceil((n - c)/(D - 1))
            n += max(step, 1)         # R2: coast the provably empty gap
    return sols, probes


def prove_bound_probe(d):
    """Sanity probe for the search bound: f(d*10^10, d) > d*10^10."""
    return f_digit_dp(d * 10 ** 10, d) > d * 10 ** 10


def main():
    t0 = time.perf_counter()

    # --- 0. oracle points through BOTH new evaluators ----------------------
    oracle_ok = True
    for (n, d, want) in [(11, 1, 4), (12, 1, 5), (22, 2, 6)]:
        a = f_prefix_blocks(n, d)
        b = f_digit_dp(n, d)
        if (a, b) != (want, want):
            oracle_ok = False
            print(f"ORACLE MISMATCH f({n},{d}): blocks={a} dp={b} want={want}")
    want_table = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 5]
    table = [f_prefix_blocks(n, 1) for n in range(13)]
    table2 = [f_digit_dp(n, 1) for n in range(13)]
    print(f"oracle f(11,1)=4, f(12,1)=5, f(22,2)=6 (both evaluators): "
          f"{'OK' if oracle_ok else 'FAIL'}")
    print(f"table f(n,1) n=0..12 matches statement: "
          f"{table == table2 == want_table}   {table}")

    # --- 1. brute-force agreement over 0..20000, all d ---------------------
    mism = 0
    for d in range(1, 10):
        vals = []
        total = 0
        for n in range(20001):
            total += str(n).count(str(d))     # naive running total f(n,d)
            vals.append(total)
        for n in range(20001):
            a = f_prefix_blocks(n, d)
            b = f_digit_dp(n, d)
            if a != vals[n] or b != vals[n]:
                mism += 1
                if mism <= 5:
                    print(f"  brute mismatch d={d} n={n}: "
                          f"naive={vals[n]} blocks={a} dp={b}")
    # per-call f_naive spot checks on top of the running-total sweep
    spot = all(f_prefix_blocks(n, d) == f_naive(n, d) and
               f_digit_dp(n, d) == f_naive(n, d)
               for d in range(1, 10)
               for n in (0, 1, 9, 10, 11, 12, 22, 99, 100, 999,
                         1000, 199981 % 20000, 20000))
    print(f"blocks & digit-DP equal brute force for all n<=20000, d=1..9: "
          f"{mism == 0}   (mismatches: {mism}); f_naive spot checks: {spot}")

    # --- 2. jump iterator vs the naive oracle scan (d=1, to 300000) --------
    limit = 300000
    naive_sols, _ = f_incremental(limit, 1)   # code/brute.py oracle
    j1, p1 = jump_fixed_points(1, limit, f_prefix_blocks)
    j2, p2 = jump_fixed_points(1, limit, f_digit_dp)
    print(f"jump iterator (blocks-evaluator) = naive oracle scan to 300000: "
          f"{j1 == naive_sols}  (probes {p1} vs {limit + 1} scanned)")
    print(f"jump iterator (dp-evaluator)     = naive oracle scan to 300000: "
          f"{j2 == naive_sols}  (probes {p2} vs {limit + 1} scanned)")
    print(f"first fixed points are 0, 1, 199981: "
          f"{j1[:3] == [0, 1, 199981]}")

    # --- 3. recompute s(1) = 22786974071 on [0, 10^10] ---------------------
    assert prove_bound_probe(1), "bound probe failed for d=1"
    sols1, probes1 = jump_fixed_points(1, 10 ** 10, f_prefix_blocks)
    s1 = sum(sols1)
    print(f"d=1: {len(sols1)} solutions (incl 0), sum s(1) = {s1}, "
          f"probes {probes1}; matches given s(1) = 22786974071: "
          f"{s1 == 22786974071}")

    # --- 4. grand total over d = 1..9, both evaluators ---------------------
    grand = 0
    grand_dp = 0
    counts = []
    for d in range(1, 10):
        assert prove_bound_probe(d), f"bound probe failed for d={d}"
        sols, pr = jump_fixed_points(d, d * 10 ** 10, f_prefix_blocks)
        sols_dp, _ = jump_fixed_points(d, d * 10 ** 10, f_digit_dp)
        # third independent route: every solution re-verified by f_digit_dp
        assert all(f_digit_dp(n, d) == n for n in sols), f"d={d} recheck"
        assert sols == sols_dp, f"d={d}: block-run and DP-run disagree"
        counts.append(len(sols))
        sd = sum(sols)
        sd_dp = sum(sols_dp)
        assert sd == sd_dp, f"d={d}: sums disagree {sd} vs {sd_dp}"
        grand += sd
        grand_dp += sd_dp
        print(f"d={d}: {len(sols):3d} solutions (incl 0), "
              f"s({d}) = {sd:14d}, probes {pr} "
              f"(DP-run agrees: {sols == sols_dp})")
    print("per-digit solution counts equal the library's sourced counts "
          "[84,14,36,48,5,72,49,344,9] (OEIS A130432, completeness flag):",
          counts == [84, 14, 36, 48, 5, 72, 49, 344, 9])
    print("grand total identical when computed by the digit-DP evaluator:",
          grand == grand_dp)

    print()
    print("=" * 70)
    print("GRAND TOTAL  sum(s(d)) for d = 1..9  =", grand)
    print("=" * 70)
    print(f"wall time {time.perf_counter() - t0:.2f} s")

    # --- structure note -----------------------------------------------------
    print()
    print("Structure vs the primary route:")
    print("  code/lib/digits.py peels n least-significant-digit first with")
    print("  the place-value identity high*factor / high*factor+low+1 /")
    print("  (high+1)*factor.  verify.py evaluates f(n,d) by two")
    print("  most-significant digit-position enumerations (closed-form block")
    print("  sums with prefix counts, and a memoized (pos,tight) digit-DP),")
    print("  sharing no code with it.  code/solution.py does not exist in")
    print("  this workspace, so the primary route is represented by")
    print("  code/lib/digits.py (its counter) and brute.py's scan; the jump")
    print("  rules are re-derived from monotonicity and implemented here,")
    print("  with the bound n < d*10^10 taken from Khovanova-Marton Prop 9.1")
    print("  (research/notes/claim-g2-solution-bound.md) and sanity-probed.")


if __name__ == "__main__":
    main()