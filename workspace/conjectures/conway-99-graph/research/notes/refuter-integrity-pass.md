# Refuter integrity pass — final check of the run's record

Per steering directive: the run is finished; the only thing owed is an integrity
pass over what is written, not a new computation. This is the refuter's version
of that — attacking the run's own claims for a false "checked".

## What was checked

1. **Every capture that solution.md §2 (routes 1–11) cites exists on disk and is
   non-empty.** All 14 cited files present and non-zero:
   `g_reduce_control`, `hexagon_identity_verified`, `n3_order6_feasibility`,
   `check_triangle_graph`, `coclique_lift_clean_design.txt`,
   `coclique_lift_cpsat`, `n3_global_ledger`, `incidence_prank_determinism`,
   `verify_twograph_gate`, `n3_vc_loop_closure_recheck`, `n3_vc_gate` (only one
   cited while SUPERSEDED — and solution.md §2 itself flags it as a retracted
   identity test, so that is correct handling, not a dangling live citation),
   `orbit_z3_enc_g99_plain_detached`, `orbit_order3_final_boundary`,
   `route11_boundary_final_verify`.

2. **Every checked-claim anchor file exists.** Verified through the claims
   ledger and the on-disk `code/out/` listing: `c3-controls-verified`,
   `c4`, `c5`, `coclique-alpha22-forces-22242-design`,
   `coclique-bound-closed-form`, `divisor63-multiplicity-integrality`,
   `fixed-set-lemma-fails-on-bvls` (3 captures all present),
   `g-reduce-c-refuted-on-bvls`, `incidence-2rank-...`,
   `integrality-five-members`, `keramatipour-paley9-pattern-holds-on-controls`
   (via `paley9_pattern_check_fixed.captured.txt` and
   `paley9_pattern_check.captured.txt`, both present),
   `makhnev-condstar-gate-passed`, `makhnev-lambda0-1331216-infeasible-integrality`
   (`check_srg33_12_1_6.captured.txt` + `check_makhnev_n3_counts.captured.txt`),
   `n3-99-forced-at-least-3`, `n3-cap-closed-form`
   (`n3_cap_closed_form.captured.txt`), `n3-seed-locally-consistent-radius1`
   (`n3_seed_consistency_ub.captured.txt` — the sound capture, distinct from the
   SUPERSEDED `n3_local_propagation.captured.txt` which is correctly retracted),
   `n3-zero-four-classical-lambda1-srgs`, `order6-n3-not-forced`,
   `pentagon-count-closed-form-verified`. All anchors present and non-empty.

3. **No citied artifact is 0 bytes.** The only 0-byte files on disk are helper
   `.err` channels (`n3_vc_loop_closure_recheck.err`,
   `six_vc_n3_type_recheck.err`) and `orbit_z3_enc_g99_detached.captured.txt`
   (0 bytes) — but that empty capture is **not** cited by any checked claim or
   by solution.md; the live orbit-matrix capture is the 48 KB
   `orbit_z3_enc_g99_plain_detached.captured.txt`. So the empty file is
   dead, not load-bearing.

## Verdict

**No false "checked" found; no route in solution.md cites a retracted artifact.
The record is internally consistent.** The run's deliverable (solution.md at
26,733 bytes, 11 closed routes, the n₃ ≥ 1 constraint, the checks on the two
controls) stands. The one SUPERSEDED capture (`n3_vc_gate.captured.txt`) is
cited by solution.md §2 only in its "SUPERSEDED / FLAWED IDENTITY TEST, Not
evidence" capacity — i.e. the run correctly kept the retraction live rather than
a dead result. `n3_local_propagation.captured.txt` (the localprop saturation
bug) is likewise annotated SUPERSEDED in its notes and is not cited as live
anywhere.

## Note on the refutation role and the directive

The directive says do not open a twelfth route, and the task ledger is empty.
That is correct: opening new mathematics against 99 has no budget and no purpose
left. The one genuinely owed item — an integrity pass over the record — is what
I did, and it is the strongest form of "attack the run's own claims" available
here: a false "checked" hiding behind a missing or retracted capture is exactly
the kind of small false statement this role exists to find.
