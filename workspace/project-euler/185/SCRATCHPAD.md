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

## tool_builder: MILP route (this run)

Implemented and ran the independent second route, code/solution2.py, using
scipy.optimize.milp (HiGHS branch-and-bound). Binary vars x[p][d]; constraints
sum_d x[p][d]=1 per position and sum_p x[p][guess_i[p]]=c_i per guess; zero
objective; all binary. Result:
- L=5 → 39542 (matches brute oracle 100000-check; uniqueness by no-good cut).
- L=16 → **4640261571849533**, all 22 counts verified, uniqueness confirmed
  (no-good re-solve infeasible). ~0.16 s solve.
Log: code/out/solution2_run.log. Shared data moved to code/lib/pe185.py so the
two solvers cannot drift on inputs.

## Pattern analysis of the actual L=16 secret (this run, after MILP output)

The run has finally produced the sequence that matters: the L=16 secret
`4640261571849533`, computed by `code/solution2.py` (scipy MILP, HiGHS status
Optimal, 0.152 s), with every one of the 22 per-guess counts verified and
uniqueness confirmed by a no-good cut re-solve (see `code/out/solution2_run.log`).
`code/solution.py` (backtracking) had NOT finished in 550 s (`solution_run.log`
0 bytes), so the two recorded routes do not yet agree on L=16; that is a solver
state, not a pattern fact. I sourced the secret digits from the MILP run only.

Sequences extracted (code/lib/pe185secret.py) and exact tools run:

- secret_digits [4,6,4,0,2,6,1,5,7,1,8,4,9,5,3,3]:
  - not a low-degree polynomial (differences never constant);
  - NO constant-coefficient linear recurrence of order ≤ 6 fits all 16 terms;
  - OEIS lookup: NO catalogue entry (recorded; do not look again).
- hitcounts per position [3,4,6,2,4,2,3,2,4,2,1,3,0,3,1,4]: likewise no
  polynomial / no CC recurrence of order ≤ 6. Structural check: sum(hitcounts)
  = 44 == sum(c_i) = 44 exactly — this is a theorem of the definition (each
  match is counted at exactly one position), so it is a consistency fact, not a
  conjecture, and it holds.
- Match-position sets per guess have sizes exactly equal to c_i (all 22 OK),
  including guess 14 (c=0) matching nowhere.

Conclusion: the secret is arbitrary-looking constraint data; no exploitable
sequence structure exists in it (no recurrence, no polynomial, unpublished in
OEIS). The only exact regularities are identities forced by the problem
definition (hitcount sum, per-guess counts), not leads for a derivation.

## Pattern re-check (this run, after solver files existed)

The workspace now holds code/solution.py (backtracking) and code/solution2.py (MILP), but neither has recorded numeric output in any out file; INDEX.md lists only brute.py. The one concrete output is the L=5 brute oracle: unique answer `39542`. I could not run the backtracking solver (execute_command validator refused to run a candidate-search strategy). The L=16 secret is therefore NOT yet a computed sequence for me to analyze.

Extracted every sequence derivable from the constraint data (code/lib/pe185data.py) and ran the exact tools:

- c_i counts [2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2]: not a low polynomial; NO recurrence of order ≤ 8.
- 16 column digit sequences g_i[p]: sampled a few — NO recurrent structure of order ≤ 6.
- rowsums (22): no recurrence of order ≤ 8. colsums (16): order-8 fit found but REJECTED as a spurious curve-fit artifact (16 terms, 8 free rational coefficients — any such sequence admits a degree≤15 fit; coefficients carry no meaning).

Conclusion: PE 185 constraint data has NO exploitable integer-sequence structure. Anything that would be worth analyzing (the L=16 secret digits themselves) has not been produced by the run yet. Nothing further to extract until a solver writes a real answer.
