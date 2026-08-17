# Executed result — orbit-matrix symmetry-break acceptance gate

State at end of attempt for tool_builder.

## The smallest executable I ran and what it settled

The open FIRST task in TASKS.md was the detained m=33 order-3 orbit-matrix
99 search (directive 30). The directives 31/34 made plain what was required
before any such search: confirm exactly one encoder runs, and never let a
symmetry-broken search report a verdict before the break survives its own
acceptance test on the BvLS control. That acceptance test was the executed
result.

**The symmetry break added to the 99 orbit-matrix encoder is UNVALIDATED:
it fails its acceptance gate at the BvLS m=81 control.**

The gate = "does some conjugate of the REAL orbit matrix of each control
satisfy the break {diag nondecreasing, row_0 lex-min} it imposes, and does
the fixed+break CP-SAT model then accept it?" Three independent probes, exact
integer arithmetic, OR-Tools CP-SAT:

- **rook(3) = srg(9,4,1,2), m=3**: exhaustive over all 6 conjugates — 6/6
  satisfy the break; fixed+break model OPTIMAL in 0.01 s. PASS. (Trivially,
  because all 6 conjugates are the same all-2-off-diagonal matrix.)
- **BvLS = srg(243,22,1,2), m=81**: the deterministic `canonical_conjugate`
  routine raises `AssertionError: row 0 not lex-min` — it cannot
  canonicalise the KNOWN-GOOD BvLS orbit matrix. FAIL.
- **BvLS, m=81**: 20,000 random conjugations of the real orbit matrix → 0
  satisfy the break; a constructive root-search (all 81 candidate row-0
  placements, columns sorted ascending) → 0 break-satisfying conjugates.
  BvLS's diagonal is constant (=2), so break condition A (diag nondecreasing)
  is vacuous and only `row_0 lex-min` (B) is in play — the construction fails.

This is not a partial pass at m=3 and a pass missing at m=81: m=81 is the
scale that exposes the canonicaliser as wrong. Any INFEASIBLE produced by a
symbreak=True run would be a false nonexistence result for the order-3 case —
the exact fear of directives 30/34.

## What I did about the unsound run (directive 31/32/34)

- Killed the detached symbreak 99 run that was running on the unvalidated
  break; its capture was already annotated "NOT EVIDENCE — SYMMETRY BREAK
  UNVALIDATED" before a verdict could be read from it. Confirmed dead
  (process list now shows one encoder only).
- Restarted the **sound** unbroken encoder (`orbit_z3_encoder.py g99 3600`,
  the one that accepts both controls OPTIMAL — rook 0.01 s, BvLS 3.30 s)
  detached on the 99 m=33 case, writing to
  `code/out/orbit_z3_enc_g99_plain_detached.captured.txt`. It is the only
  encoder process (PID verified against its cmdline and stdout fd). A slow
  correct search beats a fast unsound one.

## Files written (paths changed this attempt)

- `code/out/orbit_z3_symbreak_soundness.py` + `.captured.txt` — gate: 6/6 at
  rook, 0/20000 random at BvLS.
- `code/out/orbit_z3_symbreak_constructive.py` + `.captured.txt` — 81-root
  constructive search, 0 break-satisfying conjugates at BvLS.
- `code/out/orbit_z3_symbreak_fixed_accept.py` — canonicaliser that aborts at
  m=81.
- `code/out/symbreak_acceptance_gate.captured.txt` — settled-result record.
- `code/out/orbit_z3_enc_g99_symbreak_detached.captured.txt` — annotated
  NOT EVIDENCE (killed run).

## Returned verdict semantics (kept sharp)

INFEASIBLE proves only that no such order-3 automorphism exists, never that
the graph does not exist; UNKNOWN/TIMEOUT prove nothing. The sound plain 99
run (PID 5504, maxsec 3600) will report one of these on completion and the
distinction is preserved in its capture.

## Not touched

The two-graph gate (`verify-twograph-gate`) and the incidence p-rank gate
(`incidence-prank-parameter-determinism`) were already settled by earlier
agents with captures on disk; I verified that rather than re-running them.
Memory (Cognee) is down per the shared-context directive; the finding is fully
captured on disk, which directive 20 says is complete.
