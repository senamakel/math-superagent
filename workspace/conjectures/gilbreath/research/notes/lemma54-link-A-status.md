# Lemma 5.4 re-derivation — what is executed vs still open (accurate status 2026)

Source anchor for the re-derivation: `research/notes/lemma54-re-derived.md`
(claim `lemma54-re-derived`), which documents the combinatorial core and the
BHP demand side, and `research/notes/lemma54-discarded-case-is-universal.md`
(claim `lemma54-discarded-case-universal`).

## What has a captured run on disk

1. **Combinatorial core (executed, exhaustive).** `code/out/lemma54_descent_check.captured.txt`
   runs `code/lemma54_descent_check.py`: all 131,070 patterns of {0,2}^L for
   L=1..16, 2,621,432 (pattern, even v) pairs, zero violations on
   - (1) `x_L in {0,2} <=> v <= 2*nu2+2` (exact biconditional)
   - (2) runway `v > 2*nu2+2 => x_L = v - 2*nu2`
   - (3) {0,2}-absorption (closure)
   The delta=0 case is the *null step* (x -> x, descends nothing; only 2-steps
   drop by 2 while x>=2). This is the heart of the re-derivation and it IS done.

2. **Real-column iff/sufficiency + the discarded-case universality (executed).**
   `code/out/lemma54_iff_check.captured.txt`: 2480 columns, all-successful,
   iff violations 0, sufficiency violations 0, discarded delta=0 case in
   100% of rows. Independent route: `code/out/verify_granville_nu2_independent.captured.txt`
   (zero-entry statistic 50.0% of gray-block entries).

3. **ν₂ density measurement (executed).** `code/out/nu2_granville_check.captured.txt`
   (and two independent re-verifiers agree): ν₂/n in [0.42,0.52], n=50..3999.

## What exists only as a program with NO captured output (unrun)

`code/out/verify_lemma54_v_le_gstar.py` — the **Link A** bound entry
(`v <= g*_n` by induction: |a-b| <= max(a,b), so no diagonal step exceeds the
record gap) and its composition (`g*_n <= 2*nu2+2 => v <= g*_n <= 2*nu2+2 =>
x_L in {0,2} => success`). **Directive 45:** `code/out/verify_lemma54_v_le_gstar.captured.txt` and
`.captured2.txt` DO exist but are **vacuous** — the column loop ran over 0
columns (`checked: 0`, `max margin 0.000`), because the {0,2}-suffix scan
breaks on the terminal left-column entry 1 before finding any start. Link A
remains **unverified** until fixed and re-run. The Link-A proof itself is elementary (a one-line induction,
already argued in the script's comments and consistent with the non-increasing
row max), but **it has not been machine-verified in-container**. Do not report
the full composition as `checked`; it is `asserted` (elementary proof) plus the
exhaustively-checked core.

## Genuinely open (a real test-shape gap, not just an unrun script)

The sufficiency implication `g*_n <= 2*nu2+2 => success` has only ever been
confirmed on **all-successful** prime columns (every prime column succeeds
because Gilbreath holds this far), so both sides of the iff were true
throughout — vacuously in the failing direction. The discriminating test —
approaching the threshold `2*nu2+2` **from the failing side on sequences that
do fail** (Granville's own "closest failing sister" construction in his §5.1,
or synthetic Poisson-gap sequences in his §4) — has never been run. That is
the experiment that would actually exercise the delta=0 repair. It is the
next step for Route B, not another confirmation sweep.

## Bottom line

- The delta=0 repair at the combinatorial level is **proved exhaustively**
  (2.6M pairs, zero violations) — the hardest part is done.
- Link A (`v <= g*_n`) is elementary but **unexecuted**; run
  `code/out/verify_lemma54_v_le_gstar.py` to close it.
- The **failing-side validation** remains genuinely open and is the
  discriminating test worth building.
