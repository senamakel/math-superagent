# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it. Carries established results with their basis,
dead approaches, computed numbers, and durable memory — not a file catalogue,
not a narration.

**Token budget 10,000.** The file is re-sent on every model call in every role,
so length is a bill paid many times over.

## Problem (Project Euler 346 — sourced, `problem.md`)

A **strong repunit**: a number that is a repunit (all `1`s) in **>=2 distinct
bases `b > 1`**. Repunit `R_b(k) = 1+b+...+b^{k-1} = (b^k-1)/(b-1)`, `k>=1`.
Every `n>=3` is `11` in base `n-1`; `1` is a single-digit repunit in every base.
**Task:** sum of strong repunits below `10^12`.

## Established

- **Structural fact (computed & checked):** a number `n>1` is strong **iff**
  it is a repunit of length `k>=3` in some base `b>1` (the length-2 repunit at
  `n-1` is always the second base); `1` is strong by itself. So
  `answer = 1 + sum(distinct (b^k-1)/(b-1) for b>=2, k>=3, <= N)`.
- **Bound is comfortable:** for `k>=3`, `b^(k-1) < 10^12` caps `b < 10^6`
  (and shrinks fast with k), so work scales with the count of (b,k) pairs,
  ~`10^6`, not with the `10^12` bound. This is what defeats scanning all n.
- **Oracle (proved against statement):** `code/pe346/brute.py` gives below 50
  -> `{1,7,13,15,21,31,40,43}` (count 8, sum 171) and below 1000 -> 47 strong
  repunits, sum **15864**. Both match the statement exactly. Also `code/brute.py`
  (the naive per-n oracle) reproduces them.
- **FINAL ANSWER (computed & checked):** sum of strong repunits below `10^12`
  = **336108797689259276**, count 1011529.
  `code/pe346/solution.py` (pw-arithmetic enumeration) and the independent
  `code/pe346/verify.py` (per-length `val=val*b+1` walk, different structure,
  no pw arithmetic) agree on both the sum and the count at `10^12`.
- The sorted strong-repunit list (with `1` prepended) is **OEIS A053696**
  (sourced, `research/summaries/oeis_a053696.md`), confirmed by enumeration
  matching the exhaustive program — consistent, not an independent check.
- **Duplicate structure (computed & checked, `code/pe346/check_reduction.py`):**
  the dedup correction is exactly **2** for every N in [10^4, 10^12] — the only
  two values representable as length>=3 repunits in two distinct bases are
  **31** (=11111_2 = 111_5) and **8191** (=1111111111111_2 = 111_90). So
  `strong_sum(N) = 1 - 31 - 8191 + Σ_{b,k>=3}(b^k-1)/(b-1)` for N>=8191;
  reproduces the 10^12 sum exactly. Why the pair-count is 2 above the
  set-count. Fails trivially for N<=8191.

## Ruled out

- Brute force over all `n < 10^12` (scanning the bound) — the naive wrong
  method the structural fact avoids; never run at full size.
- Constant-coefficient linear recurrence for the count/sum sequences: a 5th
  order fit over 10 terms gave huge rational coefficients (meaningless),
  not polynomial, no exploitable recurrence. Dead end; enumeration stays exact.

## Numbers

- Count of strong repunits per `10^p` (p=1..11): 2, 13, 47, 141, 403, 1172,
  3501, 10671, 32962, 102713, 321792. Sums per `10^p` (p=1..10): 8, 540,
  15864, 450740, 12755696, 372810163, 11302817869, 348635395606,
  10849978873789, 339706288602849; p=11 (i.e. `10^12`) -> 336108797689259276.
- Count at `10^12` = 1011529 (both routes).

## Recalled

- `recall_memory` has **no prior-run finding** for Euler 346 itself; the only
  durable PE346 memory is this pattern_finder note: strong-repunit list =
  A053696, confirmed by enumeration (marked **recalled**, source pattern_finder
  run — its hypothesis (the length>=3 characterization) is what solution.py and
  verify.py both check, and those checks agree with the exhaustive oracle).
- Scratch (`recall_scratch`) holds only provisional notes; the numbers above
  come from executed programs.

## Contradictions

None. The two independent implementations agree with the exhaustive oracle.

## Gaps

None of substance: oracle reproduces both examples, method verified by a second
route at full size. Method/derivation written up in `MEMORY.md`; run log
`config/start.log`.
