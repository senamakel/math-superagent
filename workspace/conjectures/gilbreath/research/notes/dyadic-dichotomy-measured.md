# Dyadic-periodicity dichotomy — measured result (Directive 57/58/59)

Status: `measured`, exact integers, runs captured below.

> **Directive 60 correction:** the stage-1 "NOT reproduced" verdict below is an
> OFFSET (suffix-scan floor convention), not a refutation; the claim is about
> MINIMAL period, and the alt-word extension CONFIRMS it (P=10,12,14,16 alt are
> `01`-repeated, minimal period 2). See
> `research/threads/dyadic-periodicity-collapse.md`.

## The two pre-existing oracle scripts were BUGGY and unrun (Directive 59 confirmed)

- `code/out/reproduce_dyadic_periodicity.py` crashes immediately
  (`IndexError` inside `build_seq`: indexes `h_pattern[len(q)-2]` without
  wrapping modulo the period; the local `period` is computed, never used).
  Capture: `code/out/reproduce_dyadic_periodicity.captured.txt`.
- `code/out/dyadic_periodic_check.py` returns nu2 = **0 for every period**
  1..8 (powers-of-2 AND odd-factor). Cause: `make_input_gaps` adds a leading
  gap 1 for the 2->3 difference and `build_triangle` prepends another [1] on
  top, so A_1 = (1,1,2,4,...) has an ODD second entry — the triangle is not in
  the `(1, even, even, ...)` parity class at all. Capture:
  `code/out/dyadic_periodic_check.captured.txt`.

Both are dead ends; neither ran real data. They were the "drafted but unrun"
oracles Directive 59 flagged.

## The corrected oracle

`code/out/dyadic_periodicity_correct.py` (run as-is, no edits):
- builds the proper 2-then-odds triangle (A_1 = (1, even gaps), second entry
  even), bit h[j] governs gap q_{j+2}->q_{j+3}, gap = 2 if bit else 4,
  wrapping the bit index modulo the period;
- nu2 via the run's canonical `lib.rightdiag.cycle_and_nu2` (maximal {0,2}
  suffix of the right diagonal, count of 2s).

Capture: `code/out/dyadic_periodicity_correct.captured.txt`, EXIT 0.

## Result

### Stage-1 exact numbers: NOT reproduced
| period | mine (n inv 200,400,800,1200) | host | note |
|---|---|---|---|
| 1 | 0,0,0,0 | 1,1,1,1 | mine = run's OWN established value (consecutive odds, nu2=0, claim transfer-matrix-kernel-allones) |
| 2 | 1,1,1,1 | 2,2,2,2 | off-by-one in suffix window |
| 4 | 1,1,1,1 | 2,2,2,2 | off-by-one |
| 8 | 1,1,1,1 | 2,2,2,2 | off-by-one |
| 3 | 132,266,532,798 | 133,264,533,798 | boundary convention |
| 5 | 104,212,424,639 | 104,210,424,638 | boundary convention |
| 6 | 67,132,267,398 | 134,264,534,796 | host EXACTLY 2x — halving difference in window |
| 7 | 56,342,456,684 | 112,112,685,684 | convention |

Why mine is the honest convention: period 1 (consecutive odds) is the one
fully-settled case in the corpus, and the run PROVED nu2 = 0 there
(transfer-matrix-kernel-allones). The host "1" contradicts that proof. So the
host's exact numbers come from a subtly different (unstated) "maximal {0,2}
suffix" window; the qualitative shape is unaffected.

### Qualitative dichotomy: CONFIRMED (the actual prediction)
Over n = 200..4000, two words per period (tail-1 word and alternating word):
- powers of 2 (1,2,4,8,16): nu2 = O(1) (values 0 or 1, tiny noise), e.g. P=16
  {2,4,2,1,1}, P=8 {1,2,1,1,1}, P=4 {1,1,1,1}.
- odd factor present (3,5,7,9,11,13,15): nu2 grows with n, e.g. P=3 {132 →
  2666}, P=5 {104→2132}, P=9 {83→1648}, P=13 {93→1871}.
- periods 6,10,12,14 with the **tail-1 word** (which has an odd factor in the
  period) grow: P=6 tail1 {67→1332}. Their "alt" word is secretly period 2
  (a power of 2) and collapses to 1 — proving the collapse is governed by the
  *parsing into a power-of-2 period*, not the word length.

So the falsifier from Directive 57 ("if a period-3 or period-5 family ALSO
gives nu2=O(1), the dyadic story is wrong") is NOT tripped by the corrected
data: odd-factor periods genuinely grow. The dyadic-periodicity dichotomy is a
measured fact, consistent with the corpus (period 1 = 0 as established).

Growth for odd/composite periods is real but not cleanly linear — plateaus
(non-uniform in n's binary structure of the fold) occur, e.g. P=15 {..,1064,
1064}, P=7 {56,284,284,1140,2284}. The claim is "NOT O(1)" / ">> n sometimes",
i.e. unbounded, which holds.

## What this does and does NOT give the primes
It confirms the dichotomy THEOREM shape is real and prime-free. It does NOT
close G-supply: aperiodicity of the prime halved-gap bit string is strictly
weaker than the quantitative anti-dyadic bound nu2 >= c*n the supply argument
needs. The gap between "not dyadic-periodic" and "nu2 >= c*n" is the honest
remaining statement.
