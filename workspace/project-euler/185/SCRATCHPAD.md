# Scratchpad

Use this file for temporary calculations, partial derivations, and observations
that are not yet established well enough for `MEMORY.md`.

## pattern_finder

Checked on this run: workspace holds only the PE 185 statement, scaffolding,
and empty indices. No `brute.py`, `solution.py`, or derived sequences exist yet,
and no numeric output has been computed. PE 185 is a constraint-satisfaction
problem (a single 16-digit answer), not a sequence problem — there is no integer
sequence to run `analyze_sequence`/`find_linear_recurrence` on. Nothing to
pattern-match until the solver has produced output. Do not re-check until a
solution file exists.

## Re-check (this run)

Still no `solution.py`/`solution2.py`/out files — the run has produced no numeric data beyond the L=5 brute-force oracle confirmation (unique answer `39542`). The only integer sequence present is the L=16 required-count vector c_i = [2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2].
- `analyze_sequence`: differences do not become constant → not a low-degree polynomial; no clean growth ratio.
- `find_linear_recurrence` (order ≤ 6): NO constant-coefficient linear recurrence fits all 22 terms.

So the count vector has no exploitable sequence structure — it is arbitrary constraint data, not a generated sequence. Only genuine structural fact is sparsity (all c_i ≤ 3, so each guess matches in at most 3 of 16 positions — a constraint-sparsity property, not a pattern). Nothing more to extract until a solver produces the actual secret sequence.
