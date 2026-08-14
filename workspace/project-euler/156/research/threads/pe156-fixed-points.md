# PE156 — fixed-point enumeration of f(n,d)=n

Solve Project Euler 156: for each d ∈ {1..9}, find every n ≥ 0 with f(n,d)=n
(f(n,d) = count of digit d in the decimal writings of 0..n), sum them per
digit s(d), and report Σs(d).  The library supplies every lemma; the solver
is implemented and the answer is computed and triple-verified.

## Governing claims (all verified this cycle against the full texts on disk)

- `G1-digit-count-closed-form` / `G1-checked` — O(log n) exact evaluation of
  f(n,d).  Verified verbatim in Khovanova & Marton §7 eq. (1) (arXiv
  2305.10357v2 and AMM 132(8) 2025): with Y = ⌊x/10^k⌋·10^(k−1),
  c_d(x_k) = Y (x_k<d), Y + (x mod 10^(k−1)) + 1 (x_k=d), Y + 10^(k−1)
  (x_k>d).  Also checked by the run against the brute-force oracle (statement
  table, f(22,2)=6, every n in 0..20000, all 14 solutions in 0..300000).
- `G2-solution-bound` / `km-prop91-bound` — every solution satisfies
  n ≤ d·10^10.  Verified verbatim as Prop 9.1 of the arXiv v2 (with proof:
  f_b(b^b)=b^b; f_d(d·b^b)=d·b^b+1; no solution in [d·b^b,(d+1)·b^b] since
  every number there has leading digit d; f_d((d+1)b^b)=(d+2)b^b; base-b
  Lemma 5.1 pushes the count permanently ahead).  AMM §4 states the bound,
  Table 3 lists the actual maxima — all nine match the run's computed last
  solutions (1 111 111 110 / 10 535 000 000 / 20 500 000 000 / 30 500 000 000
  / 40 000 000 000 / 59 628 399 995 / 69 971 736 170 / 79 998 399 997 /
  80 000 000 000).
- `km-lemma71-skip` — the interval-skip rule (a≥(d)>x and f_d(y)<x ⇒
  a≥(d)>y), verified verbatim as Lemma 7.1 (proof: f_d non-decreasing).
  `bentley-yao-unbounded-search` is the efficiency rationale for the
  doubling/halving probe schedule, not a correctness input.
- `ruskey-theorem5-digit-count-generating-function` — CORRECTED this cycle:
  Theorem 5 (verified verbatim) gives an **infinite series of rational
  terms**, 1/(1−z)·Σ_{m≥0} z^{d·k^m}/(1+z^{k^m}+⋯+z^{(k−1)k^m}) — a
  Mahler/divide-and-conquer object, NOT a rational function (the paper itself
  contrasts the Zeckendorf case: "does not have a rational generating
  function").  Background tier only.
- `oeis-per-digit-counts`, `d1-sequence-finiteness` — catalogue term counts
  (84,14,36,48,5,72,49,344,9 incl. 0, A130432) and d=1's 84 terms ending at
  1,111,111,110; both match the run's output.

## Status

`solved and verified`.  code/solution.py implements the jump iterator over
[0, d·10^10] with the closed-form evaluator; code/verify.py is the
independent second route (two MSD evaluators — prefix-block sums and
memoized digit-DP — sharing no code with the place-value peeler in
code/lib/digits.py).  All three evaluators agree with brute.py on the
reachable range and produce identical per-digit solutions and sums.

## Result

Σ s(d) for d = 1..9 = **21295121502550**
(per-digit s(d): 22786974071, 73737982962, 372647999625, 741999999540,
100000000000, 2434703999430, 1876917059570, 15312327487352, 360000000000;
counts 84,14,36,48,5,72,49,344,9 = A130432; maxima = paper Table 3).

## Verification record

- brute.py oracle: statement table f(n,1) n=0..12, f(22,2)=6, first fixed
  points 0,1,199981, f(n,1)=3 never in 0..300000
  (code/out/brute-oracle-output.txt).
- verify.py: both evaluators equal brute force for all n≤20000, d=1..9;
  d=1 jump run = naive scan to 300000 (458 probes); s(1)=22786974071;
  grand total identical under the digit-DP evaluator
  (code/out/verify-output.txt).
- solution.py: reproduces the statement table, s(1), grand total, 661
  solutions in 86 649 iterations, 0.70 s; writes solutions-d{d}.txt
  (code/out/solution-run.log).
- Per-digit files end at the paper's Table 3 maxima; d=1's 84 terms equal the
  OEIS A014778 b-file term-for-term through 1111111110.
- Pending tool_builder run: code/out/indep-total-check.py re-aggregates the
  grand total from the on-disk solution files by plain addition (no
  digit-counting code), checking counts vs A130432, order, Table 3 maxima,
  s(1), and the total.

## Guardrails

- Never read A216398 or the per-digit b-files (answer contamination; the
  search-results page research/sources/oeis-search-fixed-points.full.md
  physically contains A216398's terms — do not use them even to check).
- Complexity must not scale with the bound; only per-candidate O(log n)
  evaluations with skips are allowed (86 649 total f-evaluations for all
  nine digits, not ~10^10 visits).

```thread
question: What is Σ_{d=1}^{9} s(d) for PE156, and what program/claims make that number exact?
status: solved — answer 21295121502550 computed and triple-verified (three
  structurally different evaluators + oracle agreement + catalogue count/max
  cross-checks); one optional re-aggregation script pending tool_builder.
rests-on: G1-digit-count-closed-form, G1-checked, G2-solution-bound,
  km-prop91-bound, km-lemma71-skip, oeis-per-digit-counts,
  ruskey-theorem5-digit-count-generating-function (corrected)
blocked-by: none
next: tool_builder runs code/out/indep-total-check.py as a third independent
  aggregation; then close the thread.
```
