# Candidate 1 (window-range-bound) is false on live rows; the C2 alternating-sum identity holds exactly

Three scripts had sat in `code/out/` with no captured output. They were run by the
operator on the host (CPython 3, exact integers, no sympy), unchanged, from the
workspace root with `PYTHONPATH=code`:

    PYTHONPATH=code python3 code/out/verify_c1.py
    PYTHONPATH=code python3 code/out/runner1.py
    PYTHONPATH=code python3 code/out/check_window_range_empirical.py

all EXIT=0. Captures are at `code/out/verify_c1.captured.txt`,
`code/out/runner1.captured.txt`, `code/out/check_window_range_empirical.captured.txt`.
Setting: `primes_up_to(200000)`, `rows_generator(primes, 160)`, so rows `A_1..A_159`.

## What C1 asserts, verbatim from the code

For row `k` and position `i`, take the window `w = A_1[i-1 .. i-1+(k-1)]` of length
`k` in the first difference row, and put `R = max(w) - min(w)`. C1 is the claim
`A_k(i) <= R`. The docstring of `check_window_range_empirical.py` states what it
would buy: "with the range bound `A_k(i) <= R(k)` on the intruder's feeding window,
the drain law gives a (2,4)-event at least once every ~`(R(k)-4)/(2p)` rows" — that
is, a bounded inter-giant gap, which is step 6 of the chain.

## Result

    C1 all-cells: checked=2828595 violations=12393
    C1 intruder:  live=64 events=29 intruder>R viol=5 meanR_all=31.7 meanR_at_event=29.03
    C2 identity:  rows checked 159, violations=0

C1 is false. It fails on 12,393 of 2,828,595 cells (0.44%), and — the part that
matters, since only the intruder feeds the drain law — it fails at the intruder
position on 5 of 64 live rows (7.8%). A hypothesis violated at 7.8% of the exact
positions its conclusion is drawn from cannot carry that conclusion.

A second observation cuts the same way. The mean window range over live rows is
31.7, but at the rows where a (2,4)-event actually fires it is 29.03 — events
occur where `R` is *smaller* than typical. The drain heuristic behind C1 wants the
opposite: large `R` should mean more room and a sooner event. The correlation has
the wrong sign, so C1 is not merely loose here, it is pointing the wrong way.

C2, by contrast, holds exactly. For every one of the 159 consecutive row pairs,
with `W = len(A_k) - 1` and `sigma(v) = sum_i (-1)^i v_i`,

    sigma(A_{k+1}) = A_k(0) - (-1)^W A_k(W) - 2 * sum_{i<W} (-1)^i min(A_k(i), A_k(i+1))

with zero violations. This is an identity in the row, not a statistical regularity:
it follows from `|a-b| = a + b - 2 min(a,b)` telescoping under the alternating sum.

```claim
id: window-range-bound-refuted
statement: The window-range bound C1, A_k(i) <= max(w) - min(w) for w = A_1[i-1 .. i-1+(k-1)], is false. Over rows A_2..A_159 from primes below 200000 it fails at 12393 of 2828595 cells, and at the intruder position on 5 of the 64 live rows. Furthermore the mean window range at (2,4)-event rows (29.03) is smaller than over live rows generally (31.7), so the drain-law heuristic that C1 was to support has the wrong sign.
hypotheses: primes below 200000; rows A_1..A_159 from lib.gilbreath.rows_generator; exact integer arithmetic; C1 as written in code/out/runner1.py lines 18-30
holds-here: yes
status: checked
bearing: Closes the window-range route to step 6 (bounded inter-giant gap) as stated. Any revival needs a different window, an additive slack R + c, or a bound proved only at the intruder rather than all cells.
anchor: code/out/runner1.captured.txt, code/out/verify_c1.captured.txt, code/out/check_window_range_empirical.captured.txt
source: operator-computation
```

```claim
id: c2-alternating-sum-identity
statement: For every row A_k with W = len(A_k) - 1, sigma(A_{k+1}) = A_k(0) - (-1)^W A_k(W) - 2 * sum_{i<W} (-1)^i min(A_k(i), A_k(i+1)), where sigma(v) = sum_i (-1)^i v_i. Verified with zero violations on all 159 consecutive row pairs.
hypotheses: primes below 200000; rows A_1..A_159; exact integer arithmetic
holds-here: yes
status: checked
bearing: An exact conserved relation between consecutive rows. It is a candidate invariant for the erosion/regeneration balance and should be proved symbolically from |a-b| = a+b-2min(a,b), after which it becomes proved rather than checked.
anchor: code/out/runner1.captured.txt
source: operator-computation
```

Both claims are operator computations. Verify them independently before adopting:
re-run the three scripts inside the container and reproduce the six numbers above
(12393, 2828595, 5, 64, 29, and 0 C2 violations) before changing any ledger entry.
