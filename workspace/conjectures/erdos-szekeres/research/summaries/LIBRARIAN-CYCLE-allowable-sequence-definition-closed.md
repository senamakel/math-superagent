# Librarian cycle report — allowable-sequence definition gap closed

## What this cycle added

**Closed the definitional foundation gap of the live `allowable-sequence` thread.**
The approach had been operating on the Goodman–Pollack allowable (circular) sequence
with its definition flagged `gp80-not-held-circular-sequence-unsourced` on disk — the
primary texts (GP80 JCTA, GP93 Springer survey, Abello–Eğecioğlu–Kumar 1995 DCG) all
paywalled, so the object itself had no citable definition in the library.

**Acquired:** Hagit Last, *Two Proofs for Sylvester's Problem Using an Allowable
Sequence*, MSRI Publications (Combinatorial and Computational Geometry) Vol. 52 (2005),
pp. 433–436. Free full text at
`research/sources/slmath-goodman-pollack-allowable-sequences-chapter22.full.md`
(source URL https://library.slmath.org/books/Book52/files/22last.pdf). It gives the
exact construction of A_{l,P}(S): label points by projection onto a line rotating 180°
about P; new permutation at each critical direction (orthogonal to a spanned line's
slope) by reversing the collinear points = *reversed substring*; runs 1..n to n..1;
each pair switches exactly once per half-period (C(n,2) events for a simple config);
each consecutive pair of permutations differs by reversing a single increasing
substring. Attributed to GP80, surveyed in GP93.

**Wrote claim** `gp-allowable-sequence-definition` (statement, hypotheses, bearing,
anchor) in `research/summaries/slmath-goodman-pollack-allowable-sequences-chapter22.md`.
This does **not** close `staircase-convexity-unsourced` (that flag stays: the literal
contiguous-block form is REFUTED by the thread's own machine check; the surviving
pointwise-extreme form is verified against the oracle but not sourced as a theorem).

## What this means for the run

- The thread's adjudication (already recorded in the approach file + allseq captures)
  stands: reversal-depth = ES block index is **refuted** (per-point reversal count is
  constant N−1 by the pair-reversal axiom), contiguous-block convexity is **false**,
  and convexity IS readable from the sequence as pointwise-extreme-in-projection.
- The definition is now on disk, so (a) the thread rests on a sourced primitive, and
  (b) no future pass needs to re-fetch GP80/93 for the definition. The escape from any
  new "the allowable sequence is unsourced" claim is the held MSRI chapter + Dumitrescu
  arXiv:2204.06101.
- Updated `research/allowable-sequence-extraction.md` (definition now quotable) and
  `research/threads/allowable-sequence.md` (next = adjudicated verdict; rests-on now
  names `gp-allowable-sequence-definition`).

## What I deliberately did NOT chase (and why)

- **Goodman–Pollack 1980** (DOI 10.1016/0097-3165(80)90011-4) and **GP93 survey**:
  paywalled at Elsevier/Springer; the definitional content is held via the MSRI chapter,
  so a fetch would be gold-plating. Recorded, not a live gap.
- **Abello–Eğecioğlu–Kumar 1995** (DOI 10.1007/bf02570710): paywalled; its content is
  about staircase-polygon *visibility graphs* and balanced tableaux, which the thread's
  refutation makes non-load-bearing. Not fetched.
- **SMQH inner-12 configurations**: already closed as a dead end (never published, not
  in the repo) by a prior cycle; re-searching is prohibited by that close.
- **Valtr "Open caps and cups" (2007) / Cerny simple proof**: adjacent
  open-cup/open-cap results on the cups-and-caps machinery. The Cerny PDF download
  failed (malformed). Not pursued: the class is adjacent, the run already covers
  cups-and-caps tightness via Morris–Soltan, and no stated gap asks for it.
- **ETV 1996 "Ramsey-remainder"**: `request_research` for it was correctly refused —
  the library already carries 5 claims bearing on it (Baek arXiv:2206.04260 is the held
  primary of the ETV reformulation; the equivalence `etv-equivalent-to-es` is on disk).

## State of the library

Mature and phase-1-complete. ROOT.md states the structure of a minimal counterexample,
the verification bound, and five+ settled restricted classes; every one of the three
standing request rows is answered by a held full text with an `answers:` claim block.
The only genuinely open item is the SMQH inner-12 *data* gap, which is unfillable from
public artifacts (would require re-running ~1 CPU-year SAT). Per the standing steering,
no further gathering until a stated gap opens.

## Durable finding

Attempted `remember_memory` twice; the memory server is not indexing this cycle, so the
eligible finding (the allowable-sequence definition is now sourced and the
depth=block/contiguous-staircase mechanisms are refuted) was recorded in the workspace
thread + approach + extraction notes instead. It should be promoted to Cognee once the
memory server is healthy.
