# Scholar cycle report — digesting the latest library records

## What the cycle asked
Turn the library against the investigation (H16.2 via displacement functions /
finite cyclicity), recording what each new source actually establishes, storing
durable findings, flagging dead ends and contradictions.

## Work done

### Real notes written (replacing placeholder digests), each with a claim block
1. **`ecalle-1990-finitude-accelerosommation.md`** — first Écalle-side primary
   record. Record + reference spine; body paywalled. Identifies EMMR CRAS 304
   (1987) as the open target for the concise Écalle proof. Claim
   `ecalle-1990-accelerosommation-record`.
2. **`roussarie-1986-separatrix-loop-limit-cycles.md`** — founding
   derivation–division paper; bibliography includes Khovanskii Bézout-for-
   Liouville-functions. Claim `roussarie-1986-separatrix-loop-record`.
3. **`dumortier-rousseau-rousseau-1996-elementary-graphics-full.md`** —
   Khovanskii-method elementary closures; regular transition maps can be
   non-identity-tangent. Claim `drr-demr-1996-elementary-graphics-abstract`.
4. **`roussarie-1994-elementary-graphics-cyclicity-1-2.md`** — general C^∞
   cyclicity 1/2 theorems; 33 quadratic graphics ≤ 2. Claim
   `drr-drr94-cyclicity-1-2-abstract`.
5. **`christopher-li-torregrosa-limit-cycles-2024.md`** — book TOC; Ch.14 =
   unified weak-H16-n=2 proof. Claim `clt-2024-book-weak-h16-n2-chapter`.

### Duplicates converted to pointers (carry nothing new)
- `buzzi-gasull-santana...html.md`, `marin-villadelprat-dulac-coefficient-properties...html.md`,
  `dukov-multiplicity...html.md`, `queiroz-arakaki-santana...html.md`,
  `mourtada-1991...pdf.md` — all five now point to their fully-digested
  sibling notes.

### The genuinely-new records are all provenance/record level
None of them establishes new mathematics on its own (they are bibliographic /
abstract-level anchors for the elementary and Écalle sides). The most valuable
single output is the **Écalle-side gap now named precisely**.

## Lean
Added `code/lean/h16_dulac_finiteness-ed8142ab.lean`: a Cited-axiom anchor for
`h16-dulac-finiteness-theorem` (every fixed polynomial planar field has finitely
many limit cycles; Ilyashenko 1991 + Écalle 1992). Non-uniform form (∃N inside
∀f) preserves the H16.2 uniformity gap; docstring notes the Écalle-side theorem-
statement gap and the Yeung 2024-25 contention. **Verdict conditional; NOT yet
lean_check-compiled — that is lean_prover's step.**

## Data-quality fixes
- Re-anchored `drr-1994-citation-anchor`, `drr-1994-record-held-verbatim`,
  `drr-drr94-cyclicity-1-2-abstract` away from `.full` source files that never
  existed on disk, to the record summaries that are the real held content.
- Confirmed `drr-demr-1996` and `roussarie-1986` anchors DO resolve (real `.full`
  files on disk).
- Noted a dangling contradiction id `drr-88-then-closed-all-four` in the derived
  natural-language ledger (exists nowhere); harmless.

## Memory
Cognee recovered mid-cycle. Stored: (1) the digest findings for the five new
record sources; (2) the data-quality / anchor fixes; (3) the new Lean Cited
axiom and its conditional verdict. Also stored a provisional note in workspace
(`research/notes/scholar-digest-ecalle-drr-records.md`) while Cognee was down.

## Open gap (Écalle side) — flagged, request tool declined
The request tool refused to queue a request for the Écalle-side theorem
statement because 8 record-level claims "bear on it". All 8 are bibliographic;
none states Écalle's theorem hypotheses. The run still cannot (a) answer
problem.md test-1 for the Écalle side, (b) add an Écalle-side Cited axiom with
real hypotheses, or (c) check whether Yeung's Ilyashenko-side critique has an
Écalle-side counterpart. Recorded in the digest note and board.

## What the run still lacks (unchanged)
- DRR 1994 raw 121-id catalogue / consolidated post-2020 ledger (two open
  requests).
- Écalle 1990 body or EMMR 1987 CRAS note (Écalle-side theorem statement).
- Clean-room re-execution of two Lu bundle scripts (upgrades asserted → checked).
- lean_check run on the new `h16_dulac_finiteness-ed8142ab.lean`.
