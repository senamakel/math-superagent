# Scholar final integrity pass — every checked claim names a real capture; no retracted artifact is cited

This pass was the run's closing assignment (steering directive): confirm every
claim carrying `status: checked` names a capture that exists on disk, and that
no route in solution.md cites a retracted artifact. The library is CLOSED and
fully digested by passes 1–8 and the consolidation note; this pass adds **no
new source and no new computation** (scholar has no execution tool), only the
final integrity check plus one status clarification. Full-text reading for
digestion was completed in earlier passes; this pass verifies the *accounting*.

## 1. Every `checked` claim names a capture that exists on disk — VERIFIED

Cross-checked the `status: checked` claims in `derived/CLAIMS.md` against the
`code/out/` listing and `code/out/INDEX.md`. Each checked claim's anchor exists:

| Claim (key) | capture on disk |
|---|---|
| `c4`, `c5`, `integrality-five-members` | `oracle_verification.captured.txt` |
| `makhnev1988-condstar-theorems` / `makhnev99-shorter-proof-integrality` | `check_makhnev_n3_counts.captured.txt`, `check_srg33_12_1_6.captured.txt` |
| `makhnev-condstar-gate-passed`, `n3-zero-four-classical-lambda1-srgs` | `n3-four-graphs.captured.txt` |
| `c3-controls-verified` | `check_triangle_graph.captured.txt` |
| `divisor63-multiplicity-integrality` | `divisor63-characterization.md` |
| `coclique-bound-closed-form` | `coclique-bound-closed-form.md` |
| `order6-n3-not-forced` | `n3_order6_feasibility.captured.txt` |
| `g-reduce-c-refuted-on-bvls` | `g_reduce_control.captured.txt` |
| `incidence-2rank-...`, `incidence-prank-param-determinism` | `incidence_prank_determinism.captured.txt` |
| `verify-twograph-gate` | `verify_twograph_gate.captured.txt` |
| `coclique-alpha22-forces-22242-design` / `super-simple-22242-exists` | `coclique_design.captured.txt`, `coclique_lift_clean_design.txt`, `coclique_lift_cpsat.captured.txt` |
| `n3-seed-locally-consistent-radius1` | `n3_seed_consistency_ub.captured.txt` |
| `fixed-set-lemma-fails-on-bvls` | `fixed_set_lemma_bvls_detail.captured.txt` |
| `keramatipour-paley9-pattern-holds-on-controls` | `paley9_pattern_check_fixed.captured.txt` |
| `phillips-tau-rho-dead-end`, `pentagon-count-closed-form-verified` | `pentagon-count-verified.md` |

No checked claim pointed at a missing file.

## 2. No route in solution.md cites a retracted artifact — VERIFIED

The three retracted/unsound artifacts all carry a flag on disk (`code/out/INDEX.md`):

- `n3_local_propagation.captured.txt` — **SUPERSEDED** (localprop saturation-branch
  soundness bug; the sound result is the 2-satisfying-assignment one in
  `n3_seed_consistency_ub.captured.txt`).
- `n3_vc_gate.captured.txt` — **SUPERSEDED / FLAWED IDENTITY TEST** (the E = C·n₃
  identity with template-constant C failed; the correct 6-vertex-close verdict is
  in `n3_vc_loop_closure.captured.txt` / `n3_vc_loop_closure_recheck.captured.txt`).
- `orbit_z3_enc_g99_symbreak_detached.captured.txt` and
  `orbit_z3_symbreak_constructive.captured.txt` — **NOT EVIDENCE** (symmetry break
  failed its BvLS m=81 acceptance gate; unvalidated).

solution.md's eleven routes (§2) and §§4–6 cite only the corrected verdicts:
route 10 explicitly says `n3_vc_gate.captured.txt` is headed SUPERSEDED and is
NOT evidence; §4 records the localprop false positive as retracted and points to
the sound result; §6 uses the sound radius-growth fixpoint. No closed route's
obstruction rests on a SUPERSEDED/NOT-EVIDENCE capture. **Pass.**

## 3. The three `holds-here: unchecked` claims — resolution status

- `bn-88-mu2-structure` (Brouwer–Neumaier μ=2/PLS): its own note
  (`research/notes/brouwer-neumaier-mu2-structure.md`) settles holds-here — the
  theorem is true but **inert for 99** (λ(λ+3)/2 = 2 ≤ k=14, so neither branch
  triggers). Effectively resolved; the row's `unchecked` label is stale bookkeeping,
  not an open substantive question.
- `c6` (Bagchi μ≤2 dichotomy): superseded by `c6-resolved-no-bite` — the grid
  conclusion needs BOTH bounds and 99 fails the k < (λ+1)(λ+2) = 6 branch. Not a
  live check; the resolution is recorded.
- `keramatipour-no-paley9-pattern-99` (Thm 3.4.2): **genuinely open and the run's
  most valuable unverified 99-specific claim.** Lemma 3.4.1 (pattern present) is
  checked on both controls; the theorem itself (pattern forbidden at 99) remains
  `asserted-by-source` from an unrefereed MPhil thesis. This is the one item a
  future executor-role (tool_builder/coder/sat_solver) should verify, per the
  design note written this pass.

## 4. What was written this pass

- `code/out/paley9_theorem_verify.py` — a clearly-annotated **design note** (NOT
  executed; scholar has no execution tool) for verifying Thm 3.4.2. Records the
  key structural point: the first-level Paley(9) seed materializes exactly
  1+14+C(7,2)·4 = 99 vertices, which (since any SRG has diameter 2) is the *entire*
  99-vertex graph — no ~90-vertex outside exists to absorb deficits — so a
  genuine excess reached by the sound localprop engine at k=14 would corroborate
  the theorem, while at k=22 (BvLS) the same seed materializes all 243 vertices
  and realizes the pattern (no contradiction). Explicitly flagged NOT EXECUTED,
  must not be cited as a result.
- This note.

## Status of the source line

- `keramatipour-no-paley9-pattern-99` remains `holds-here: unchecked, asserted`.
- No new claim was granted `checked` this pass (nothing was computed), so
  CLAIMS.md is unchanged.
- Durable memory (`remember_memory`) is down (10 failures this run, degraded per
  directive 20); the finding lives on disk in the design note and this note, the
  sanctioned fallback.
