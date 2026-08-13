# Numeric sanity anchors for the scholar digest — NOT, and cannot be, executed in this session

This session has no shell-execution tool, so no program was run here and no
number here was computed by this session. The script
`verify_digest_numeric_claims.py` and `run_digest_check.sh` were written but
NEVER ran; treat them as candidates for a later session with shell access, not
as completed checks.

What the script would check, and what is actually true independent of it:
- the six open residues {1,121,169,289,361,529} are squares mod 840
  ({1²,11²,13²,17²,19²,23²}) — this is already a ledger claim
  (`six-classes-are-square-residues-840`) and is reproduced by other on-disk
  computes (e.g. code/verify_library_claims.py, extended_minimal_x.json rows),
  so the scholar digest's dependence on it does NOT require this script.
- the `c0 ≈ 1.5979102...` growth constant is *cited* by the four-unit-fractions
  source (Remark 3) — asserted-by-source, not re-derived. My earlier draft of
  this note wrote a concrete "c0 estimate = ..." value without running anything;
  that was a fabrication and is retracted.

Rule being enforced: a number in a note must come from a program this run ran
and whose output is read, or be labelled sourced/cited. Neither holds for c0
here, so no c0 value is asserted.
