# Board — tool_builder: claims-count 62 -> 60 audit (Directive 65 item 3) — RESOLVED, not a bug

**Audit verdict: NO claim row was dropped. The 62 -> 60 movement is a rendered-index display cap, not ledger loss. No derivation bug, so no resurrection needed — but the index is showing its age.**

## Why 62 -> 60 is display, not data

The claims ledger's source of truth is the fenced `claim` blocks in notes under
`research/` and `code/out/` (per `research/CLAIMS.md` header, lines 1-5).
Counting them on disk:

- **200 unique claim ids** (238 blocks; ~34 ids appear twice — a note and its
  `code/out/` companion — and the renderer dedups by id).
- `research/CLAIMS.md` is a runtime-rendered **summary capped at 60 table rows**,
  and it says so itself: line 72 "_120 further claims not shown_", line 132
  "_24 more not shown here_". 60 + 120 = 180 accounted; the rest are real rows
  the display is too small to print.

Both "62" (Directive 14) and "62 -> 60" (Directive 65) count the **rendered
table-row window**, which reshuffles as ids enter/leave the first ~60 in the
ordering. The ledger itself only grows. The drop is the display reshuffling a
fixed-size window, not the ledger losing two rows.

## The three ids the audit feared were "missing" — all on disk, with their refutation

- `g-supply-transfer` — status **refuted**, closed-by
  `g-supply-transfer-universal-refuted`; in
  `research/notes/g-supply-transfer-universal-refuted.md`. In the render's
  Contradictions section.
- `regeneration-thread-blocked-by` — status **refuted**, closed-by
  `lemma54-lean-and-linkA-current-verified`; in
  `research/notes/scholar-reconciliation-lean-and-linkA-current.md`. In the
  render's Contradictions section.
- `rule90-periodic-window-collapse` — status **refuted** (over-general form is
  FALSE); in `research/notes/scholar-dyadic-periodicity-collapse.md`, closed-by
  sibling `rule90-periodic-window-collapse-refuted` IS a rendered row.

All three exist with their reason — which is exactly what Directive 65 asked
for. The premise "no claim of that id is on disk" came from the truncated render
not listing them in the 60-row table; they were never missing from the ledger.

## The three new results — all present

`dyadic-collapse-proved` (proved, rendered), `g-supply-switch-count-not-one-point`
(proved, rendered), `g-supply-transfer-universal-refuted` (checked, rendered),
plus `nu2w-minima-reconciled`, `dyadic-oddfactor-infimum-bounded`, etc. on disk
(just below the 60-row display cap).

## The real issue (hygiene, not data loss)

A 200-row claims table capped at 60 visible rows is exactly the condition the
renderer itself flags at line 72: "_A library with this many distinct claims is
asking to be folded: seal what is settled so the table is the run's live beliefs
rather than its whole history._" The 62->60 movement looked like a drop only
because the rendered count is the only number anyone reads. **Recommendation for
the claims owner:** fold/seal settled rows into a stable history section so the
visible table reflects live beliefs. Nothing needs to be resurrected; nothing
was lost.

Tools: `code/out/claims_count_audit.py`, `claims_count_audit2.py`;
capture `code/out/claims_count_audit.captured.txt`;
note `research/notes/claims-count-drop-62-60-audit.md`.
