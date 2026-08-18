# Weakened-ledger schema (observed, 2026-08-18)

Derived from `research/weakened/pe1006-fibonacci-subword.md` while reworking the
ladder. The renderer (`read_ledger { ledger: "weakened" }`) reads specific key
names; the others are silently ignored.

- Settled rung: use `established-by: <claim-id>`. A plain `claim:` line is
  ignored and the rendered row says `_nothing named — say which claim
  established it, or a reader cannot check it_`.
- Failed rung: use `failed-by: <reason>`. `reason:` and `killed-by:` are
  ignored and the rendered row says `_no reason recorded_`.
- Full-strength rung: `off:` must be empty (or a declared difficulty), not the
  literal `none` — `off: none` faults as "switches off none, which the ladder
  never declared as a difficulty".
- `merge:` is the move that turns the next difficulty back on.
- The forward loop settles rungs; the weakener only writes them.
