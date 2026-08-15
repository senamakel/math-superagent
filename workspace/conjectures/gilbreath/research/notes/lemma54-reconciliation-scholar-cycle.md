# Scholar cycle — what the flagged sources actually establish, reconciled

## Not "unread" — already deeply digested

The two FULLPDFs TASKS flagged as unread were in fact read and re-derived to a
high standard by prior cycles. I verified the digests directly against the full
texts this cycle:

- **Granville 2026** (`research/notes/lemma54-re-derived.md`,
  `lemma54-re-derived-proof.md`): Lemma 5.4's δ=0 case is handled (not
  discarded) and the lemma is **proved on the even domain** (parity descent:
  each 2 drops the value by 2, 0 passes through, {0,2} absorbing; budget
  `2ν_2+2` exactly tight). Located parity boundary: over ALL integers the
  lemma is false (odd v stays odd); real prime diagonals are even so the
  prime case is safe.
- **CHT 2026** (`research/notes/cht-2026-summary.md`): Theorem 1.6 verbatim,
  the column restriction `j ≥ N′` (right half only), the (i)–(iii)
  hypotheses, and the authors' own difficulty assessment on p.8. `holds-here:
  no`. The 6e8 right-half scan confirmed the {0,d}-block obstruction is absent
  at any reachable scale.
- **Chase 2024** (`arias-de-reyna-list-manipulation-conjecture-FULLPDF.full.md`):
  confirmed duplicate of `chase-2024-random-analogue-gilbreath` (the filename
  is a misnomer from the download). Theorems 1 & 2, Lemma 3.2 (block
  consumption), Lemma 3.5 (parity), §7 Proth-myth retraction all already in the
  ledger.

## The one real scholarly reconciliation this cycle

An apparent contradiction existed between two on-disk Lemma 5.4 checks:

- `code/lemma54_rederive.py` (captured): reports iff/suff violations (pass 1
  col n=5 Colonna; pass 2: g{2,4,6} iff_viol=3496/114000, g{2,4,6,8}=4960,
  g{2,4}=1574).
- the filtered run (`lemma54_rederive_filtered`, claim
  `lemma54-sufficiency-survives-proper-domain`): **zero** counterexamples over
  187,123 applicable columns, despite 390,657 failing columns total.

**Resolution (verified structurally, consistent with the ledger).** `rederive.py`
tests ALL columns without enforcing Lemma 5.4's hypothesis that the predecessor
q_1..q_{n-1} is itself a *successful* Gilbreath sequence. Those violating
columns have an already-failed predecessor, where the "green terminal = 1"
breaks. Once the successful-prefix premise is enforced (the proper domain), the
violation count collapses to zero. So Lemma 5.4's *statement* survives honest
testing on its own domain with the δ=0 case included; the published proof's
δ=0 "exception to ignore" is a proof defect, not a statement defect.

## What is still genuinely open on Route B

1. **Link A (`v ≤ g*_n`) is elementary but UNEXECUTED**: no
   `code/out/verify_lemma54_v_le_gstar.captured.txt` on disk. The verifier
   program exists (`code/out/verify_lemma54_v_le_gstar.py`). Until it runs,
   Lemma 5.4 should not be reported as fully machine-checked (only as
   elementary-proof + exhaustive core).
2. The **supply side `ν_2 > n^β, β > 0.525`** is the entire open content —
   nothing here or in any source proves it. Everything else in the Route B
   chain (IFF reduction, recharge identity, demand side unconditional via BHP,
   Lemma 5.4 re-derived) is settled.

## Sources that do not help / are dead ends

- **ZARKOUNA 2026** and **Maréchal** — classified not-load-bearing (claimed
  "proofs", files restricted/0-citation). Do not re-fetch or cite.
- **Miller 1970, Northshield 2010, Malyshev 2021** — full texts unobtainable
  (HTTP 403 / no text layer / paywalled respectively); content covered by held
  secondary sources. Recorded in REQUESTS.md unobtainable section.
- **"arias-de-reyna-list-manipulation-conjecture"** — mislabelled Chase 2024
  duplicate; do not re-read for content.

## No new contradiction with recalled memory

Everything I verified agrees with the run's established claims (`lemma54-rederivation-safe`,
`lemma54-re-derived-proof`, `granville-nu2-density-measured`, `cht-theorem16-verbatim-fullpdf`).
The only places two on-disk numbers appeared to disagree (rederive iff/suff
violations vs filtered zero) were artifacts of unenforced hypotheses, now
reconciled.

```claim
id: lemma54-reconcile-domain-enforcement
statement: The apparent Lemma 5.4 violation counts in code/lemma54_rederive.py
  (pass 1 col n=5; pass 2 iff_viol 3496/114000 g{2,4,6}, 4960 g{2,4,6,8},
  1574 g{2,4}) are an artifact of testing all columns without enforcing the
  lemma's hypothesis that q_1..q_{n-1} is successful. Enforcing the
  successful-prefix premise collapses the count to zero over 187,123
  applicable columns (3 gap families) despite 390,657 failing columns — so
  Lemma 5.4's sufficiency statement survives on its proper domain with the
  delta=0 bounce included; the published proof's delta=0 exception is a proof
  defect, not a statement defect.
hypotheses: random valid 2-then-odds, successful-prefix premise enforced,
  exact integer |a-b|, columns n=3..40
holds-here: yes
status: checked (two independent on-disk runs agree once the premise is enforced)
bearing: closes the apparent contradiction; Lemma 5.4 statement is trustworthy
  on its domain; the open pieces remain a machine-verified proof of the bounce
  invariant and the nu_2 > n^0.525 supply bound.
anchor: code/out/lemma54_rederive.captured.txt, code/out/lemma54_rederive_filtered.notes.md
contradicts: nothing — reconciles two outputs of the same check
```
