# Librarian cycle — singular-words & circular-word primary sources; geometric-monoid request re-confirmed unfillable

## Deliverables this cycle (2 primary sources added)

1. **Wen & Wen, "Some properties of the singular words of the Fibonacci
   word"** (Eur. J. Combin. 15 (1994) 587–598; free preprint, Séminaire
   Lotharingien de Combinatoire).
   `research/sources/wen-wen-singular-words-fibonacci-word-1994.full.md`
   `research/summaries/wen-wen-singular-words-fibonacci-word-1994.md`

   This was a frontier top-row item (cited by 3 of the library's sources).
   Establishes the singular-word construction and the theorem that a factor of
   the Fibonacci word is a special (right-special) word iff it is a prefix of
   some finite Fibonacci word — a second primary anchor for the one-right-
   special-factor structure. Power bounds (u^4 never a factor) bear on the
   window-prefix length.

2. **Hegedüs & Nagy, "Representations of Circular Words"** (EPTCS 151 (2014)
   261–270; arXiv:1405.5607).
   `research/sources/hegedus-nagy-representations-circular-words-arxiv.full.md`
   `research/summaries/hegedus-nagy-representations-circular-words-arxiv.md`

   Open-access, independent second source for (a) the k+1 factor count and
   (b) Séébold's lemma (u^2 a factor ⇒ u conjugate of a finite Fibonacci
   word), plus the Fibonacci-number branching-gap structure. Also gives
   Cor 1 that the factor trees nest as subtrees (self-similarity).

   Note: the `.2014` file is the arXiv landing page only; the paper proper is
   the `.arxiv` file. The landing page is kept as provenance but the paper
   should be read from the `.arxiv` file.

## Claims added

`research/notes/wen-wen-and-circular-words-claims.md`: two blocks —
- `wen-wen-singular-words-structure`
- `hegedus-nagy-circular-words-fibonacci-trees`

Both affect the CLAIMS ledger as corroborating sources for the existing
`fibonacci-unique-special-factor-reverse`, `fibonacci-squares-conjugate-finite-word`
and the k+1 count (`governing-factor-complexity`).

## The geometric-monoid request — re-hunted, still unmatched in English

A `deep_research` run and two `find_similar_sources` / `exa_search` rounds
confirm once more: **no peer-reviewed English/French primary source states the
exact geometric-weight (x^i) floor-sum monoid recursion** the universal-
Euclidean primitive uses. Closest academic anchors — Babichev–Babichev
("#Counting all lattice rectangles", closed family of moment kernels under
Euclidean affine+reciprocal transforms), Patrício–Hartwig (geometric-sum
Euclid recursion, on disk), Brown (Dedekind-sum / floor-power reciprocity) —
are all **already on disk** and carry the *spirit*, not the exact x^i-weight
monoid-closure statement. Requests `citable-name-treatment-0c91`,
`citable-precise-statement-600d`, `citable-precise-statement-d2e7` map to
closed claims (`req-close-universal-euclidean`, `universal-euclidean-
geometric-floor-sum`, `geometric-sum-division-algorithm`) anchored to the
Chinese OI-wiki/fhq/LOJ/AtCoder primary sources. This cycle's searches produced
no new anchor; the request set is as filled as the literature allows. Recorded
so nobody re-hunts it.

## What was NOT obtained (recorded so nobody re-searches)

- Chuan, "A representation theorem of the suffixes of characteristic
  sequences", DAM 85 (1998) 47–57 — Elsevier paywall, no free full text. The
  library covers the suffix/factor-decomposition side via Fici (on disk) and
  the D-representation / Fibonacci factorization content is summarized in
  searches; not critical to the committed route.
- Chuan, "Unbordered factors of the characteristic sequences of irrational
  numbers", TCS 205 (1998) 337–344 — Elsevier paywall. The unbordered-factor
  account is already carried by Currie–Saari Cor 6 (on disk).
- de Luca, "A division property of the Fibonacci word", IPL 54 (1995)
  307–312 — Elsevier paywall; UNINA repository holds the record but no file.
  The division/factorization content is covered by Fici and Wen–Wen (on disk).

## Why these (and not more)

The library was previously at saturation on the word-combinatorics axis
(lothaire, Berstel surveys, Perrin–Restivo, three-gap tier, standard words,
universal-Euclidean primitive tier all present). The frontier's top rows were
the two papers added this cycle plus three Elsevier-paywalled items already
covered in substance by on-disk primary sources. This closes the last
obtainable top-row gaps without duplicating the source stock.

## Handoff / open items

- The run's critical path remains executable (tool_builder): wire mech_psi
  through ueuclid, reproduce anchors, run k=10^18. Library-side support is in
  place.
- `request_research`: geometric-monoid request set stays as-is; the falsifies
  column already captures what would settle it (a source showing the x^i
  recursion is not O(log) / not closed under the Euclidean reduction). No new
  request posted this cycle.