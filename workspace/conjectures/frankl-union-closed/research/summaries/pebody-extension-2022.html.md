# Luke Pebody, "Extension of a Method of Gilmer" — arXiv:2211.13139 (Nov 2022)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/2211.13139 (also arxiv.org/pdf/2211.13139).
> Full text: `research/sources/pebody-extension-2022.html.full.md`.

One of the four (independent) groups that simultaneously confirmed Gilmer's
conjecture and reached the `(3−√5)/2` constant. This is the least cited of the
four is the iid-line treatments (the other three being AHS, Chase–Lovett,
Sawin), but it is the natural companion to read for the exact inequality
verification.

## What it establishes

- Confirms Gilmer's conjectured push of his technique to the constant
  `(3−√5)/2 ≈ 0.3819` for union-closed families.
- Provides the one-variable entropy inequality verification / the sharpness
  statement that the iid-OR method attains exactly this value.
- In AHS's account: Pebody wrote the entropy inequality as "to be proven"
  (deferring the computer/symbolic verification), whereas AHS gave a
  computer-assisted proof and Boppana later gave an elementary one. So the
  *verification of the analytic inequality* is the load-bearing step that
  AHS/Boppana secure, and Pebody's own contribution is the reduction.

## Hypotheses and holds-here

- `ℱ` finite union-closed, `≠{∅}`. **Holds-here: yes.**

## What it lets the run do

- Completes the set of the four independent iid-line confirmations on disk.
  The analytic inequality is best read in Boppana (elementary) or AHS
  (computer-verified); Pebody is the methodological variant.

```claim
id: pebody-gilmer-extension
statement: Confirms Gilmer's technique extends to the constant (3−√5)/2 for
  union-closed families (one of four independent confirmations: AHS,
  Chase-Lovett, Sawin, Pebody).
hypotheses: ℱ finite union-closed, ≠{∅}
holds-here: yes
status: claimed in-paper; the underlying entropy inequality is verified by
  AHS (computer) and Boppana (elementary)
bearing: completes the iid-line confirmation set on disk
anchor: research/sources/pebody-extension-2022.html.full.md
follows-from: gilmer-constant-0point01
```
