# Scratchpad

Use this file for temporary calculations, partial derivations, and observations
that are not yet established well enough for `MEMORY.md`.

## pattern_finder — L=16 secret now computed and verified (this run)

The run has changed since the last check: `code/solution2.py` (scipy MILP)
produced an L=16 secret, and I independently re-verified it (code/pat_verify.py,
run output below). The prior scratchpad entries concluded only that the
*published constraint data* had no sequence structure; the actual secret was not
then a computed sequence. It is now, so I re-ran the exact tools on it.

Secret digits `[4,6,4,0,2,6,1,5,7,1,8,4,9,5,3,3]` (answer 4640261571849533):
- analyze_sequence: not a low-degree polynomial (differences never constant).
- find_linear_recurrence (order ≤ 6): NO constant-coefficient recurrence fits.
- oeis_lookup on [4,6,4,0,2,6,1,5,7,1,8,4,9,5,3,3]: no entry (recorded, don't repeat).

Per-position hitcounts `[3,4,6,2,4,2,3,2,4,2,1,3,0,3,1,4]`:
- same three results: not polynomial, no CC recurrence of order ≤ 6, no OEIS
  entry.

Structural identities forced by the definition (NOT conjectures), all verified:
- sum(hitcounts) = 44 = sum(c_i) = 44 — double-counting each (guess,position)
  match once per side. Proven, holds.
- all 22 per-guess match counts == c_i exactly (incl. guess 14, c=0, matches
  nowhere). Verified.
- digit histogram shows no bias pattern: every digit 0..9 appears at least
  once, counts [1,2,1,2,3,2,2,1,1,1].

Conclusion: the L=16 secret is arbitrary-looking constraint data. No polynomial,
no linear recurrence (order ≤ 6), no OEIS catalogue. The only exact regularities
are identities forced by the problem definition, not leads for a derivation.

## Falsified structural hypotheses (this run, code/pat_structure.py)

Attacked the L=16 secret with two concrete, falsifiable structural guesses:

- **H1 (column-majority rule): secret[p] is the modal digit of the guess
  column at position p.** FALSIFIED: equal at only 1 of 16 positions
  (position 2). If the rule held, all 16; a random guess digit agrees with the
  mode with probability ≈ 1/3+, so 1/16 is below even the chance baseline.
  First counterexample: position 0 (column mode 2, secret 4).
- **H2 (match-position pair design): the 31 within-guess pairs of match
  positions form a regular design over position pairs.** FALSIFIED: 31 pairs
  cover only 30 distinct position-pairs of 120, coverage histogram
  {once: 29 pairs, twice: 1 pair} — no near-uniformity, consistent with
  random pair spread. Nothing to exploit.
- Multiset digit-overlap between guesses and secret (8..13, consistent with
  random expectation ≈9) carries no signal either.

## Solver cross-check status (context for the run)
- code/solution2.py (MILP) L=16 → 4640261571849533, all counts + uniqueness
  confirmed (solution2_run.log).
- code/solution.py (backtracking) log shows L=5 (39542) but NO L=16 output yet;
  the two recorded routes have NOT cross-confirmed on L=16. That is the solver
  track's concern, not pattern's; the MILP answer is self-verified (all 22
  counts + no-good uniqueness cut), and I re-verified all 22 counts directly.
