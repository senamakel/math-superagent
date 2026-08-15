# Colonna deletion left-edge failure — hand-verified from the explicit example

**Claim upgraded:** `colonna-deletion-left-edge-failure` (was `asserted` from a
record-page footnote) — the explicit delete-11 (and delete-5, delete-7) examples
are verified here by exact hand arithmetic on the nested absolute differences.
This is load-bearing: it kills the plain bounded-gap general-class strategy at
gap bound `g ≥ 4` (Eppstein defeats the unbounded-gap class; Colonna's delete-5
gives a concrete `g=4` left-edge failure).

## Hand check (no program; exact integer arithmetic on the triangle)

**Delete-11** — `S = (2,3,5,11,13,17,19)`. Gaps `(1,2,6,2,4,2)`, max gap = 6.
- `A_1 = (|3−2|, |5−3|, |11−5|, |13−11|, |17−13|, |19−17|) = (1, 2, 6, 2, 4, 2)`.
  Matches the claim's `A1=(1,2,6,2,4,2)`. Second entry `= 2 ∈ {0,2}` — row 1 OK.
- `A_2 = (|2−1|, |6−2|, |2−6|, |4−2|, |2−4|) = (1, 4, 4, 2, 2)`.
  **`A_2(1) = 4 ∉ {0,2}`** — second entry escapes at row 2.
- `A_3(0) = |1 − A_2(1)| = |1−4| = 3 ≠ 1`. **Left edge fails at row 3.**

**Delete-5** — `S = (2,3,7,11,13,17,19)`. Gaps `(1,4,4,2,4,2)`, max gap = 4.
- `A_1 = (1, 4, 4, 2, 4, 2)`. **`A_1(1) = 4 ∉ {0,2}`** — escapes immediately at
  row 1. (So delete-5 has gaps ≤ 4 *and* fails — sharpens Colonna's "g=4".)

**Delete-7** — `S = (2,3,5,11,13,17,19,23)`. Gaps `(1,2,6,2,4,2,4)`, max gap = 6.
- `A_1 = (1, 2, 6, 2, 4, 2, 4)`; `A_1(1)=2 ∈ {0,2}`. `A_2 = (1,4,4,2,2,2)`;
  **`A_2(1)=4 ∉ {0,2}`**, `A_3(0)=3`. Left edge fails at row 3.

All three deletions fail the left edge; delete-5 fails with max gap 4.

## What the constructor shows

`2` is the only even term, so these are genuine 2-then-odds sequences. The
escape `A_2(1)=4` is a local-event failure: a `{2,6}` adjacency (positions
1,2 of A₁) produces `|2−6|=4` at the next second entry. The gap-4/6 bound lets
such an adjacency persist into the block. So **no bounded-gap theorem with
`g ≥ 4` can hold**; only `g ≤ 3` (or a non-gap hypothesis) survives as a plain
general-class statement. This is the concrete companion to Eppstein's
asymptotic anti-Gilbreath construction.

```claim
id: colonna-deletion-left-edge-failure
statement: Removing one prime (5, 7, or 11) from the prime list gives a 2-then-odds sequence whose left edge fails: (2,3,5,11,13,17,19) (delete-11) has A_2(1)=4 and A_3(0)=3; (2,3,7,11,13,17,19) (delete-5, max gap 4) has A_1(1)=4; (2,3,5,11,13,17,19,23) (delete-7) has A_2(1)=4, A_3(0)=3. So no bounded-gap theorem with gap bound g>=4 holds on the 2-then-odds class.
hypotheses: 2-then-odds sequences obtained by deleting one prime from a finite prime prefix.
holds-here: yes -- the delete-5 example is gaps<=4 AND left-edge-failing, sharpening the plain bounded-gap class to g<=3.
status: checked (exact hand arithmetic on the nested absolute-difference triangle for all three explicit deletions, matching the claim's A1 for delete-11)
bearing: kills the plain bounded-gap general-class strategy at g>=4 (companion to Eppstein's asymptotic construction); the surviving general-class hopes are g<=3 or a non-gap (CHT two-separated non-concentration) hypothesis.
anchor: research/sources/colonna-proth-gilbreath-record.full.md (record-page footnote)
```

Cross-check: the delete-11 `A_1` reproduced here equals the claim's quoted
`(1,2,6,2,4,2)` exactly, and the subsequent failure is forced by the `{2,6}`
adjacency. This is a second route (direct triangle, not the footnote's index
table) agreeing with the source.
