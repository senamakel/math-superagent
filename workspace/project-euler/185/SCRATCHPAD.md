# Scratchpad (pattern_finder checks)

## Pattern analysis is COMPLETE and closed-out. Findings (all supported by
exact tools against the run's verified data, current this check):

State of results (checked this run): only code/solution2.py has produced an
L=16 answer — `4640261571849533`, all 22 counts verified, uniqueness confirmed
(no-good re-solve), see `code/out/solution2_run.log`. The backtracking
`solution.py` recorded only the L=5 confirmation (437 nodes) before the run
window ended; its L=16 result was never produced, so the two recorded routes do
NOT yet agree on L=16. That is a solver-state gap, not a pattern fact.

The one sequence that matters — the L=16 secret digits
[4,6,4,0,2,6,1,5,7,1,8,4,9,5,3,3] and its per-position hitcounts
[3,4,6,2,4,2,3,2,4,2,1,3,0,3,1,4] — were re-verified this run:
- not low-degree polynomials (differences never constant);
- NO constant-coefficient linear recurrence of order <= 6;
- OEIS: no catalogue entry (dead thread; do not look again).
Definition-forced identity holds: sum(hitcounts) = sum(c_i) = 44.

## Closing the last survivor (NEW this run)
Code `code/pat_c1_test.py` (200000 Monte Carlo trials, seed 12345, random
length-16 secret + 22 random guesses with c_i = actual match count): the
chance that all c=1 guess single-match positions are pairwise distinct is
~12.2% (>=6 such guesses) / ~5.5% (exactly 6). Real data (6 c=1 guesses, all
distinct) is barely above this baseline — so the last surviving conjecture is
an empirical coincidence consistent with randomness, NOT a derivation lead.
This closes the final survivor. No exploitable structure exists in the PE185
secret or its constraint data.

New files this run: `code/pat_refresh.py` (re-derives current facts),
`code/pat_c1_test.py` (baseline test of the c=1 conjecture), `code/pat_c1_l5.py`
(pre-existing, holds L=5 c=1 check).
