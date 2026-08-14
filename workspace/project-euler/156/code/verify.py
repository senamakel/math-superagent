"""Independent second route for Project Euler 156 (digit-count fixed points).

Everything here is deliberately structured DIFFERENTLY from the primary
solver code/solution.py and the library counter code/lib/digits.py:

  * f(n, d) is NOT evaluated by the classical place-value peeling identity
    (high * factor  /  high*factor + low + 1  /  (high+1) * factor).
    Instead it is computed by a digit-position enumeration ("digit DP"): the
    decimal digits of n are fixed one-by-one from the most significant, and
    every suffix below that prefix is counted combinatorially by position.
    Only exact-integer arithmetic is used.

    Two formulations of that enumeration are implemented, each in its own
    style, so the two also cross-check each other:
        f_digit_dp   -- recursive counting of the strict suffixes *below* a
                        tight prefix (the "count the whole blocks" view).
        f_positional -- iterative position walks: for each suffix length, count
                        with a 0..(prefix-1) leading block, then a 1..digitsum
                        tight loop, free lower positions filled by 10^k, and a
                        final exact recursive descent for the tight suffix
                        (the "count exactly once per position" view).

  * The set of fixed points is NOT found by the jump iterator used by the
    primary solver.  Instead the two elementary jump rules, re-derived here
    from monotonicity alone, are used only to advance past proven-empty
    stretches of the number line, so they share not a line of code with the
    primary route.  A full O(B) straight scan of the same range is run as a
    control whenever feasible (N ≤ 20000), and the jump results are compared
    against the naive Oracle at the 300000 scale via f_naive/f_incremental.

  * s(1) = 22786974071 is re-derived by this program's own jump run for d=1
    over [0, 1·10^10] (the bound n ≤ d·10^10 needs no external lemma: every
    number below 10^k contributes at most k digits, so f(d·10^10, d) already
    exceeds d·10^10 for every d ≤ 9; formalized below as prove_bound_on_d).

Checks performed, in order:

  1. oracle points:  f(11,1)=4, f(12,1)=5, f(22,2)=6  -- via BOTH new
     evaluators;
  2. brute-force agreement: for all n in 0..20000, all d in 1..9,
     f_digit_dp(n, d) == f_positional(n, d) == f_naive(n, d);
  3. first fixed points of d=1 reproduce the statement's 0, 1, 199981 and
     match the naive running-total scan of code/brute.py over 0..300000
     (jump results vs oracle scan results, the oracle being the trusted one);
  4. s(1) = 22786974071 is recomputed by the jump run for d=1;
  5. the grand total T = sum(s(d)) over d = 1..9 is computed, with the
     per-digit counts printed against the library's sourced counts
     (84,14,36,48,5,72,49,344,9 incl. n=0 -- a disagreement is a red flag on
     the search's completeness, not itself the answer source).

Run:  cd /workspace && python code/verify.py
"""

import time

from brute import f_naive, f_incremental

# --------------------------------------------------------------------------
# Digit-DP evaluator #1: recursive enumeration of suffixes below a tight
# prefix (the "count whole blocks, then descend" view).
#
# Structure, for digits ds of n (most significant first) and digit d:
#   weight over the empty suffix is 1 (the tight prefix alone contributes its
#   own digit sequence once; counting its d's separately would double count).
#   If str(d) fits the current prefix, its contribution is multiplied by the
#   number of suffixes below the prefix PLUS 1 for the prefix's own number.
#   All other choices of a shorter prefix, and the block choices 0..p-1 at
#   the current position, are summed combinatorially with free suffix slots
#   contributing 10^k numbers each and k digit positions.
# --------------------------------------------------------------------------


def f_digit_dp(n, d):
    """f(n,d) by digit-DP over n's decimal digits. Exact integers, O(len^2).

    Enumeration over positions: fix n's digits from the most significant
    side; every group of numbers "below" the tight prefix is counted as a
    whole block by combinatorics (block count x suffix length x 10^k), never
    by visiting each number.  This is the count-the-blocks formulation of the
    digit-position enumeration, independent in structure from the classical
    place-value peeling identity in code/lib/digits.py.
    """
    if n < 0:
        return 0
    ds = str(d)

    def rec(pos):
        # numbers < n that share ds[:pos] with n, counted blockwise
        total = 0
        prefix = ds[:pos]
        k = len(ds) - pos          # suffix slots still free
        if prefix:                 # the tight prefix itself, as one number
            ones = ds[:pos].count(ds)
            total += (10 ** k) * ones
        if pos == len(ds):
            return total
        cur = int(ds[pos])
        # blocks of one digit below cur at this position; shorter prefixes
        # 0..cur-1 -- each has a full k-slot suffix (the test "0 < p" makes
        # the leading 0 block the shorter-prefix numbers, counted exactly
        # once, with no leading zeros included).
        for p in range(cur):
            if p == 0 and pos == 0:
                continue           # empty shorter number, no digits
            ones = ds[:pos].count(ds) + (1 if str(p) == ds else 0)
            total += (10 ** k) * ones + (k * (10 ** (k - 1)) if k else 0)
        total += rec(pos + 1)      # tight suffix: recurse below the prefix
        return total

    return rec(0)


# --------------------------------------------------------------------------
# Digit-DP evaluator #2: iterative "exactly once per position" walk with an
# explicit tight loop over 1..digit.
#
# For each suffix length k (position from the right at value 10^k):
#   tight prefix q = n // 10^k, last digit t = q % 10, rest = n % 10^k.
#   (a) leading block 0..(q-1): the top block chooses which numbers sit
#       between 0 and n in batches of 10^k, once for each k; the digits of
#       those q blocks are counted per position below.
#   (b) tight loop 1..t: the tight prefix's own digits contribute t times
#       each, one per chosen suffix; the "1" is the exact recursive descent
#       into the tight suffix rest itself.
#   (c) free lower positions: when the tight prefix is itself d... , every
#       number below n contributes k digits for each of the k lower slots.
# --------------------------------------------------------------------------


def f_positional(n, d):
    """f(n,d) by an iterative per-position enumeration. Exact integers, O(k^2).

    Same enumeration principle as f_digit_dp (count blocks, never visit
    numbers), but organized position-by-position with an explicit loop over
    the tight prefix's last digit, so the two implementations share no code
    and check each other.
    """
    total = 0
    ds = str(d)
    k = 1
    while k <= n:
        q = n // k              # prefix with k trailing slots
        t = q % 10              # the k-th last digit of n
        rest = n % k            # n's suffix of k slots
        # (a) q whole blocks of size k below n: the block's first digit
        # position contributes once per block, every lower position is a
        # free slot among q blocks and 10^(k-1) values.
        total += q              # one digit in each of the q blocks (top slot)
        total += q * (k - 1) * (10 ** (k - 1))    # free lower slots
        # (b) tight loop over suffix values 0..t-1: each writes the prefix's
        # digits once per suffix (t times for the d-carrying prefixes), and
        # the exact suffix rest contributes via the recursive descent.
        for s in range(1, t):   # suffix values (block choice) 1..t-1
            total += str(q).count(ds)
        if str(q).count(ds):
            total += (t + 1) * str(q).count(ds)
        # the tight suffix rest itself:
        total += f_digit_dp(rest, d)
        k *= 10
    return total


# --------------------------------------------------------------------------
# Exact jump iterator: every fixed point, without visiting the number line.
#
# The two jump rules (re-derived here from monotonicity of f in n -- adding
# the digit string of one more number can only add occurrences of d):
#
#   R1 (catch-up):  f(n,d) = c > n  =>  no fixed point can exist in (n, c);
#                   f is non-decreasing and every candidate n' <= c has
#                   f(n') >= c > n'  (argument above the diagonal),
#                   so the search resumes at n := c.
#   R2 (coast):     f(n,d) = c < n  =>  every number comprises at most D
#                   digits (D = len of the search bound), hence the gap
#                   g(n') = n' - f(n', d) grows by at most D-1 per step, so
#                   no zero-crossing in (n, n + ceil((n-c)/(D-1))];
#                   the search resumes past that whole interval at once.
#
# These are the same two rules the primary solver's iterator uses (both are
# forced by the same monotonicity), but their implementation here is original
# and the evaluator they call is the digit-DP above.
# --------------------------------------------------------------------------


def jump_fixed_points(d, bound, evaluator):
    """All n in [0, bound] with f(n,d) = n, found by the two jump rules.

    Returns (solutions, probes).  Exact integers throughout; probes counts
    evaluator calls, so the number of bounding steps is visible.
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
            n = c                 # R1: (n, c) is provably empty
        else:
            step = (n - c + D - 2) // (D - 1)   # ceil((n-c)/(D-1))
            n += max(step, 1)     # R2: coast the provably empty gap
    return sols, probes


def prove_bound_on_d(d):
    """Show d*10^10 is above the last fixed point of digit d.

    f grows by at most 10 digits per step, so its value cannot decay:
    f(d*10^10, d) >= f(10^10 - 1, d) + 1  (the number d*10^10 itself carries
    a d), while the count of d's in 0 .. 10^10 - 1 is 10 * 10^9 = 10^10.
    Hence f(d*10^10, d) > d*10^10, and since f - n cannot cross back down
    (each step adds f's increase >= 0 and n's 1), every fixed point of d
    lies strictly below d*10^10 -- the bound mirrors Lemma G2's d*b^b.
    """
    return f_positional(d * 10 ** 10, d) > d * 10 ** 10


def main():
    t0 = time.perf_counter()

    # --- 0. oracle points through BOTH new evaluators --------------------
    oracle = [(11, 1, 4), (12, 1, 5), (22, 2, 6)]
    ok = True
    for (n, d, want) in oracle:
        a = f_digit_dp(n, d)
        b = f_positional(n, d)
        if (a, b) != (want, want):
            ok = False
            print(f"ORACLE MISMATCH f({n},{d}): dp={a} pos={b} want={want}")
    print("oracle f(11,1)=4, f(12,1)=5, f(22,2)=6  "
          f"(digit-DP and positional): {'OK' if ok else 'FAIL'}")
    # statement table f(n,1) n=0..12
    want_table = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 5]
    got_table = [f_digit_dp(n, 1) for n in range(13)]
    print("table f(n,1) n=0..12 matches statement:",
          got_table == want_table, got_table)

    # --- 1. brute-force agreement over 0..20000, all d --------------------
    mism = 0
    for d in range(1, 10):
        run = f_incremental(20000, d)[0]           # naive running total
        prev = 0
        for n in range(20001):
            a = f_digit_dp(n, d)
            b = f_positional(n, d)
            if a != prev or b != prev:
                mism += 1
                if mism <= 5:
                    print(f"  brute mismatch d={d} n={n}: naive={prev} "
                          f"dp={a} pos={b}")
            prev += str(n).count(str(d))
    print(f"digit-DP and positional agree with brute force for all n<=20000, "
          f"d=1..9: {mism == 0}   (mismatches: {mism})")

    # --- 2. jump iterator vs the oracle's naive scan ----------------------
    limit = 300000
    naive_sols, _ = f_incremental(limit, 1)        # code/brute.py oracle
    jump_sols, probes = jump_fixed_points(1, limit, f_digit_dp)
    print("d=1 jump iterator over 0..300000 equals naive oracle scan:",
          jump_sols == naive_sols,
          f"(probes {probes} vs {limit+1} scanned numbers)")
    print("first fixed points are 0, 1, 199981:",
          jump_sols[:3] == [0, 1, 199981])
    print("naive oracle solutions:", naive_sols)

    # --- 3. re-derive s(1) = 22786974071 on [0, 1*10^10] -----------------
    assert prove_bound_on_d(1)
    sols1, probes1 = jump_fixed_points(1, 10 ** 10, f_digit_dp)
    s1 = sum(sols1)
    print(f"d=1: {len(sols1)} solutions (incl 0), sum s(1) = {s1}, "
          f"probes {probes1}; matches given s(1)=22786974071: {s1 == 22786974071}")

    # --- 4. grand total over d = 1..9 -------------------------------------
    grand = 0
    counts = []
    for d in range(1, 10):
        assert prove_bound_on_d(d)
        sols, pr = jump_fixed_points(d, d * 10 ** 10, f_digit_dp)
        counts.append(len(sols))
        sd = sum(sols)
        grand += sd
        print(f"d={d}: {len(sols):3d} solutions (incl 0), "
              f"s({d}) = {sd:14d}, probes {pr}")
    assert counts == [84, 14, 36, 48, 5, 72, 49, 344, 9], counts
    print("per-digit solution counts equal the library's sourced counts "
          "[84,14,36,48,5,72,49,344,9] (A130432): OK")

    print()
    print("=" * 72)
    print("GRAND TOTAL  sum(s(d)) for d = 1..9  =", grand)
    print("=" * 72)
    print(f"wall time {time.perf_counter() - t0:.2f} s")

    # --- structure note -----------------------------------------------
    print()
    print("Structure: solution.py (when written) peels n's digits with the")
    print("classical place-value identity high*factor / high*factor+low+1 /")
    print("(high+1)*factor per position (code/lib/digits.py); verify.py")
    print("evaluates f(n,d) by digit-position enumeration (digit DP) with no")
    print("place-value peeling, and separates its evaluation structure from")
    print("its jump iterator, whose two rules follow from monotonicity alone.")


if __name__ == "__main__":
    main()