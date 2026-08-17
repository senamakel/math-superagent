# Demontis, "The union-closed set conjecture is true" (arXiv:2405.03731)

<!-- source: https://arxiv.org/pdf/2405.03731 | converted from PDF -->

May 2024 preprint by Roberto Demontis **claiming a full proof of Frankl's
union-closed sets conjecture**. This library holds it because a claimed proof
is exactly what a reference library must keep for audit — but its status here
is **claimed, unaudited, with no positive reception found**. It is NOT an
established result, and nothing in it may be cited as established.

## What it claims

Theorem 1: for any union-closed F ⊆ A := 2^[n] ∖ {∅}, there is i ≤ n with
|F| ≤ 2|F_i| (i ∈ at least half the members).

Proof architecture (from the text):
- B(F) = the *basis*: X ∈ F that is not a union of two other members. Lemma 1:
  every X ∈ F is a union of basis elements.
- **Union-closed deletion sequences**: A0 = A, each step deletes one set so
  each A_r remains union-closed, ending at F (Theorem 2). Lemma 2: deleting a
  basis element preserves union-closure.
- **Ideal sequences** (Lemma 5): a deletion sequence that deletes all
  i-free sets first, then all i-containing sets.
- **Vincolation** (Definitions 6–7): X ∈ D = A∖F is *vincolated* if
  F ∪ {X} is not union-closed, i.e. ∃Y ∈ F with X∪Y ∈ D; "vincolated to"
  a pair-relationship.
- Theorem 3: under a vincolation hypothesis one can find Y ∈ D∖D_i vincolated
  to a non-vincolated R ∈ D_i. Lemma 6: an *optimal sequence* always exists.
- Theorems 4 and 5 establish `2|D_j| ≤ |D| + 1` for j minimal on D (|D| ≥ 2,
  D ≠ {{j}}).
- Final line: |F| = |A| − |D| = 2|A_i| − 1 − |D| ≤ 2|A_i| − 2|D_i| = 2|F_i|.

## Reception — the critical part

- arXiv 2405.03731v1 (6 May 2024), no revisions.
- Google Scholar / arXiv listing: **0 citations** found. No critique, no
  endorsement, no published follow-up found in this search.
- The same text appears in a journal "Curr Res Stat Math" (OPAST publishers),
  submitted 1 May 2024, **accepted 27 May 2024** — a 26-day acceptance in a
  non-mainstream publisher, with no peer-review record. (OPAST is a predatory-
  adjacent venue; the entire front matter of that PDF is the same arXiv text.)
- The workspace's claimed-proof audit (Spence, `spence-auditing-claimed-proofs-...`,
  which audits two OTHER claimed proofs) does NOT cover Demontis.

## Structural red flags

- The proof is short (~9 pages) for a 45-year-old open problem; the historical
  prior is that claimed full proofs (Blinovsky, Schäge) are false (Hu 2017
  survey, already on disk).
- Lemma 1's "basis" argument and the vincolation machinery are elementary;
  a number of steps (e.g. Theorem 4's induction, the case |D_t| = 1 conclusion)
  are stated tersely and would need checking.
- The proof never uses the entropy method or any modern machinery, and neither
  cites nor engages the (3−√5)/2 / 0.38234 literature at all — suspiciously
  self-contained for a full solution.

## Status in this library

**Claimed-proof artifact: DO NOT cite as established.** This run's PIs
(negative controls, reason-vs-numerics) require any UC claim to survive attack;
Demontis's has had none recorded. Proper disposition if the run revisits it:
hunt the specific step that fails (a candidate: the final inequality relies on
`2|D_i| ≥ ...` relationships from Theorems 4–5 whose hypotheses may not align).
Until then it is filed, flagged, and closed as "unaudited claimed proof".

## Claim block

```claim
id: demontis-claimed-uc-proof-unaudited
statement: Demontis (arXiv:2405.03731, 2024) claims a complete proof that every
  finite union-closed family F ≠ {∅} has an element in ≥ |F|/2 members.
  The claim has no recorded reception (0 citations, no peer review; published
  in OPAST's Curr Res Stat Math with a 26-day acceptance). It is filed as an
  unaudited claimed proof, NOT an established result; nothing in it is cited
  as established anywhere in this library.
hypotheses: finite union-closed F ⊆ 2^[n] ∖ {∅}.
holds-here: unknown (unchecked claim)
status: asserted-by-source (claim only; no verification found)
bearing: marks a live claimed-proof artifact for audit; prevents the run citing
  "UC is proved" from this source. If a later pass audits and refutes it, the
  specific failing step should be recorded here.
falsifies: any independent verification of the proof, or a located error
  (which would close it as a false claim); equally, if a later thorough audit
  finds it correct, its status would change to established.
anchor: research/sources/demontis-union-closed-set-conjecture-is-true-2024.full.md
```