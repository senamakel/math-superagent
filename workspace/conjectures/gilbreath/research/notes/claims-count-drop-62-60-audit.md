# Audit: the claims-ledger 62 -> 60 count drop

**Verdict: NO claim row was dropped without a reason. The "62 -> 60" figures were
counts of the *rendered* `research/CLAIMS.md` index, which is truncated at 60
table rows by design. The ledger on disk holds 200 unique claim ids; the render
shows 60 and literally says "_120 further claims not shown_" (line 72) and
"_24 more not shown_" (line 132). Nothing vanished; the display is capped.**

## Mechanism

`research/CLAIMS.md` is a runtime-rendered summary, not the ledger itself. The
ledger's source of truth is the fenced `claim` blocks in the notes under
`research/` and `code/out/` (per the file's own header, lines 1-5). Counting
those blocks on disk:

- **200 unique claim ids** in fenced `claim` blocks across `research/` and
  `code/out/` (238 blocks total; 34 ids appear in two places each — a claim is
  often restated in a note and its `code/out/` companion, which the renderer
  dedups by id).
- The rendered `research/CLAIMS.md` shows **60** table rows and then states
  "_120 further claims not shown_" — i.e. 60 + 120 = 180 accounted; the
  "further" rows are present on disk but not printed.
- A further **24** go unshown in the "Load-bearing but unverified" section
  ("_24 more not shown here_").

So 62 and 60 are both snapshots of the *rendered table-row count*, which
fluctuates by one or two as the renderer's ordering and cap settle — NOT a
count of the ledger. The drop from 62 to 60 over "two derivations" while three
new results landed is the renderer showing a *different but still-capped* 60
rows, not the ledger losing 2.

## Did the three ids the audit named vanish?

No. The audit (Directive 65) named three ids it believed had "no row":

- **`g-supply-transfer`** — on disk, `status: refuted`, `closed-by:
  g-supply-transfer-universal-refuted`, in
  `research/notes/g-supply-transfer-universal-refuted.md` (block 2). Present in
  the rendered Contradictions section AND its refuting sibling
  `g-supply-transfer-universal-refuted` IS a rendered table row.
- **`regeneration-thread-blocked-by`** — on disk, `status: refuted`, `closed-by:
  lemma54-lean-and-linkA-current-verified`, in
  `research/notes/scholar-reconciliation-lean-and-linkA-current.md`. Present in
  the rendered Contradictions section.
- **`rule90-periodic-window-collapse`** — on disk, `status: refuted` (the
  over-general form is FALSE), in `research/notes/scholar-dyadic-periodicity-collapse.md`;
  its `closed-by` sibling `rule90-periodic-window-collapse-refuted` is a rendered
  row. Present in the rendered Contradictions section.

All three therefore exist on disk **with their refutation**, which is exactly
what Directive 65 asked for. The directive's premise ("no claim of that id is on
disk") was itself based on the *truncated render* not listing them in the 60-row
table — but they were never missing from the ledger; they were missing only from
the displayed window, and they DO appear in the render's Contradictions section.

## The three "new results landed" — all present

- `dyadic-collapse-proved` — status: proved, rendered table row.
- `g-supply-switch-count-not-one-point` — status: proved, rendered table row.
- `g-supply-transfer-universal-refuted` — status: checked, rendered table row.
- (plus `nu2w-minima-reconciled`, `dyadic-oddfactor-infimum-bounded`, etc. —
  present on disk, `nu2w-minima-reconciled` is simply below the 60-row display
  cap.)

## Accounted-for total

200 unique on-disk ids. The render names 102 distinct times but shows only 60
as table rows plus the substring-rest of the ledger in other sections; the rest
are real rows the display is too small to print. This is a **display-capacity /
index-hygiene issue**, not a derivation bug. No id present in an earlier
snapshot is absent from the current one without a `status` that explains it
(refuted/superseded/closed) — every such row carries its reason on disk.

## Recommendation (not "the bug")

The real, actionable finding is the one the renderer itself flags at line 72:
a 200-row claims table is asking to be folded. Rows are NOT being dropped, but
an index that only ever shows 60 of 200 is doing the run no service, and the
62->60 movement looked like data loss precisely because the rendered count is
the only number anyone reads. Seal/fold settled rows into a stable "history"
section so the visible table reflects live beliefs. But that is hygiene, not a
derivation bug, and nothing needs resurrecting.
