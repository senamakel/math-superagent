# PE156 — fixed-point enumeration of f(n,d)=n

Solve Project Euler 156: for each d ∈ {1..9}, find every n ≥ 0 with f(n,d)=n
(f(n,d) = count of digit d in the decimal writings of 0..n), sum them per
digit s(d), and report Σs(d).  The library now supplies every lemma the
solver needs; this thread tracks what remains to be computed.

## Governing claims

- `G1-digit-count-closed-form` / `G1-checked` — O(log n) exact evaluation of
  f(n,d): verified by the run against the brute-force oracle (statement
  table, f(22,2), every n in 0..20000, all 14 solutions in 0..300000, first
  solutions 0,1,199981).
- `G2-solution-bound` / `km-prop91-bound` — every solution satisfies
  n ≤ d·10^10 (Khovanova–Marton Prop 9.1, proven in v2).
- `km-lemma71-skip` — the interval-skip rule (a≥(d)>x and f_d(y)<x ⇒
  a≥(d)>y); `bentley-yao-unbounded-search` — the doubling/halving search
  engine rationale.
- `oeis-per-digit-counts`, `d1-sequence-finiteness` — catalogue term counts
  (84,14,36,48,5,72,49,344,9 incl. 0) that the solver must reproduce;
  d=1's 84 terms end at 1,111,111,110.

## Status

`open` — library closed, solver not yet implemented. G1 is checked; G2 is
proved in source; G3 (skip-completeness) is stated but the run's own
implementation/verification of the jump iterator is not yet done.

## Next

1. tool_builder: implement `code/solution.py` — per-digit jump iterator over
   [0, d·10^10] using f_place_value, with the two skip rules
   (record-and-step when f=n; jump n→c when f=c>n;
   jump n→⌈n+(n−c)/(D−1)⌉ when c<n), D = digits of the bound.
2. Verify: agreement with brute.py on [0, 10^5] (all 9 digits), reproduction
   of the statement's oracle (f-table, first solutions, f(n,1)=3 never
   occurs, s(1)=22786974071), and per-digit counts matching A130432.
3. Second independent route: the math.SE analytic form (crasic) as a second
   f-evaluator, plus the OEIS A094798 generating-function recurrence
   g(x) = x/((1−x)(1−x^10)) + ((1−x^10)/(1−x))^2 g(x^10) — agreement over
   the reachable range and at the oracle points.
4. Report Σs(d) with the verification command and saved files.

## Guardrails

- Never read A216398 or the per-digit b-files (answer contamination; the
  search-results page `research/sources/oeis-search-fixed-points.full.md`
  physically contains A216398's terms — do not use them even to check).
- Complexity must not scale with the bound: visiting numbers up to ~2·10^10
  per digit is prohibited; only per-candidate O(log n) evaluations with
  skips are allowed.

```thread
question: What is Σ_{d=1}^{9} s(d) for PE156, and what program/claims make that number exact?
status: open (library complete; solver to be implemented and verified)
rests-on: G1-digit-count-closed-form, G1-checked, G2-solution-bound, km-prop91-bound, km-lemma71-skip, oeis-per-digit-counts
blocked-by: none in the library; the remaining work is implementation and verification (G3's iterator to be checked by tool_builder)
next: implement code/solution.py per the skeleton research/backward/fixed-point-enumeration.md; verify against oracle + naive counts on [0,10^5] + A130432 counts; second route = crasic analytic form + A094798 generating function; never touch A216398.
```