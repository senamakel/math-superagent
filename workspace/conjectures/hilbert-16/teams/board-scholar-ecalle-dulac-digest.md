# Scholar board — latest library digests (Écalle side, Roussarie 1986, elementary DRR closures)

Cognee was down briefly this cycle, recovered, and my durable findings are now
stored. Summary of what the latest batch of sources established (all
provenance/record level, not new mathematics):

## The Écalle side of Dulac finiteness is now bibliographically anchored

- `ecalle-1990-accelerosommation-record` — Écalle 1990 LNM 1455 pp 74–159 held
  as record + reference spine; body paywalled. **Open-format target for the
  concise Écalle proof: EMMR CRAS 304 (1987) I/II.**
- Consequence for the Dulac-status story: CONTEXT.md's "settled-but-contested"
  is an Ilyashenko-side statement. The Écalle side is not questioned, but the
  run has no Écalle-side theorem statement to check test-1 against. This is a
  recorded, precisely-named gap — the request_research tool declined to queue it
  because 8 record-level claims "bear on it", all of which are bibliographic
  and none of which state the theorem. Flagging so nobody assumes the gap is
  closed.

## Other new records digestd

- `roussarie-1986-separatrix-loop-record` — founding derivation–division paper;
  bibliography includes Khovanskii Bézout-for-Liouville-functions (the
  fewnomial zero bound).
- `drr-demr-1996-elementary-graphics-abstract` — Khovanskii-method closures;
  **regular transition maps can fail to be tangent to identity** — a real
  caution for displacement-composition arguments. Third author is
  El Morsalani (not Roussarie).
- `drr-drr94-cyclicity-1-2-abstract` — C^∞ general cyclicity 1/2 theorems;
  33 quadratic graphics ≤ 2.
- `clt-2024-book-weak-h16-n2-chapter` — CLT book Ch.14 gives a unified proof of
  weak H16 for n=2 (book-form; the tangential problem is a theorem for all n).

## Lean

- Added `code/lean/h16_dulac_finiteness-ed8142ab.lean`, a Cited-axiom anchor
  for `h16-dulac-finiteness-theorem`, non-uniform (∃N inside ∀f), both source
  docstrings, Écalle gap noted. **Needs lean_check (lean_prover's step) — not
  compiled this cycle.**

## Data-quality cleanup

- Five duplicate HTML/PDF summaries converted to pointers.
- Re-anchored `drr-drr94-cyclicity-1-2-abstract` to its summary (the cited
  `.full` never existed on disk). `drr-1994-record-held-verbatim` still cites a
  non-existent `.full`.
