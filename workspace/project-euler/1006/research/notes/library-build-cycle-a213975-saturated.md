# Librarian cycle — OEIS A213975 catalogue record added; library confirmed saturated

## What was added

- **OEIS A213975 — "List of subwords of A003842 arranged in lexicographic order"**
  (`research/sources/oeis-A213975-fibonacci-subwords-lexicographic.full.md`,
  https://oeis.org/A213975). The canonical catalogue record of the *distinct
  Fibonacci subwords* — the exact object Ψ sums over — in the 1/2 alphabet
  (A003842, the digit-complement of the problem's S; the set is invariant under
  complement). It carries:
  - the "exactly n+1 factors of length n" Sturmian-complexity statement,
  - a recursive construction of the length-n factor set S(n),
  - the explicit length-1..8 factor lists,
  - cross-references to A003849 (which the library already holds as the factor
    corpus), A214216 (forbidden words), and to the Chuan–Ho 2005 "Locating
    factors of the infinite Fibonacci word" primary source.
  - `A213975/full.md` is the full text; a digest sits at
    `research/summaries/oeis-A213975-fibonacci-subwords-lexicographic.md`.
  Its 58 citations were added to derived/FRONTIER.md.

## What was checked and confirmed as already closed (no re-fetch)

- All four `requests` rows are answered by `answers:` lines in
  `research/summaries/claim-fibonacci-sturmian-complexity.md`,
  `research/summaries/claim-universal-euclidean-geometric-floor-sum.md`, and
  `research/summaries/requests-closed-recap.md`.
- A proposed request on factor-position structure was rejected by the
  guardrail as redundant: the library holds **eight** claims bearing on it,
  including the two position theorems (`sivasankar-rama-position-theorem`,
  `fibonacci-position-theorem-contiguous-windows`) that ground directive 9's
  window set.
- Paywalled primaries (Morse–Hedlund 1940 "Symbolic Dynamics II"; Berstel 1986
  "Fibonacci Words — A Survey", The Book of L; de Luca 1995 "A division
  property of the Fibonacci word"; Chuan–Ho 2005 "Locating factors of the
  infinite Fibonacci word") are all recorded as *not obtained* leads, each
  covered by a held full text or encyclopedic statement:
  - Morse–Hedlund 1940 → MathWorld Morse–Hedlund/Sturmian entries,
    Lothaire C2, Perrin–Restivo, Coven–Hedlund 1973 abstract, all on disk.
  - Berstel 1986 Book of L → the run's actual factor/subword citations are
    Lothaire C2, Perrin–Restivo, Berstel 1995/2007 (all held).
  - de Luca 1995 → Chuan 2003 (moments, held) + Wikipedia/moment sources.
  - Chuan–Ho 2005 → Sivasankar–Rama Thm 7 (held) + OEIS A003849 corpus.
- The MathWorld pages are already full-text on disk (summaries carry the
  `full.md` pointer).

## Assessment

The library is saturated on every load-bearing side: the Sturmian
factor-complexity foundation, the factor-position theorems, the
universal-Euclidean second-moment primitive, the three-gap/floor-sum side,
and the catalogue records. Adopted approach: mechanical/floor-sum via the
universal Euclidean second moment. No open request remains unanswerable; the
next cycle should spend on the solver's reduction (wiring mech_psi through
ueuclid to reproduce Psi(1..150), Psi(10), then anchors 34432237/20938836),
not on more sources.
