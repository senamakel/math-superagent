# Refute spray consolidation (directive 7/operator)

The `code/refute/` folder held a spray of near-identical one-off runners for one
refutation. Consolidated into ONE parameterised script.

## The ONE established refutation this run confirms

The literal windowed form of G-sup-implies-switch, and the unqualified
R-switch-equivalence, are FALSE. Witness family h = e_{n-1} (single 1 at the
window's final index n-1, zeros elsewhere):

- The depth-d diagonal cell is T(n,d) = XOR over bitwise submasks o of d of
  h[n-1-d+o]. For every d in [2,n-1], offset o = d is a submask of d landing
  on the final index n-1 where h=1, so T(n,d)=1 for all n-2 depths.
- Hence nu2(n) = wt(Phi_n h) = n-2 = Theta(n) while the switch density (fraction
  of ones away from the amplified boundary spike) is 0.

## What replaced it

`code/refute/refute_single_boundary_sweep.py` — the single consolidated runner.
Sweeps n = 4..12 for h = e_{n-1}, computes nu2(n) by the exact submask-XOR fold
(lib.supply_fold.s_sos checked against t_direct), reports nu2, nu2/n, and
switch density; prints a negative control h = e_0 (single 1 at the FIRST index)
which does NOT give linear weight, showing the shared-final-index boundary spike
is the mechanism, not "a single 1 anywhere". Writes
`code/out/refute_single_boundary_sweep.txt`.

Verified output (reproduced the banked n=6 case nu2=4=6-2, and nu2(e_{n-1})=n-2
for every n in 4..12 while the control nu2(e_0)=1). Range swept: n = 4..12
inclusive, h length n, d in [2,n-1].

## Files deleted (all superseded by the consolidated script)

Under `code/refute/`: fixed_single_bound_n7.p, fixed_single_one.py,
random_pointwise_n4_analysis.md, rank_and_concentration.py,
rank_and_concentration_main.py, rank_and_concentration_run.py, run_all_checks.py,
run_rank_conc.py, run_rank_conc.txt, run_single.py, single_boundary_n6.p,
single_one.py, sparse_last_one.p, sparse_one_linear.p, sparse_one_linear_n8.p,
sparse_one_linear_n8v2.p, windowed_sparse_one_n5.p, wrapper.py.
Root: refute_actual_fold_run.py (run-once stub named in directive).

`code/refute/` now holds INDEX.md, __init__.py, and the one consolidated script.

## Findings preserved before deletion

- `random_pointwise_n4_analysis.md` carried a distinct small-n result (the
  exp(-Omega(n)) concentration form of R-random-pointwise FAILS at n=4 and n=5).
  Preserved to `research/notes/refute_random_pointwise_small_n.md` and to Cognee.
- The fold-rank result (rank = n-2 for the operative (n-2)x n matrix) was already
  banked as claim `fold-rank-is-n-2-nullity-2-alternating`; nothing was lost.
