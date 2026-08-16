# Librarian report — third pass, continuation

## What this cycle added

The library was already mature (52 full texts, 72 digests, phase-1 complete per
`research/ROOT.md`). This cycle made a **tightly-scoped structural addition** to
the fold-algebra tier, the thinnest live angle, and it was the *only* open gap
the run holds a search licence for (`walsh-spectral-subset-b904`). No fact was
re-fetched; both downloads were verified as absent first.

### Added full texts + summaries

1. **Callan, *Sierpinski's Triangle and the Prouhet-Thue-Morse Word***
   (arXiv:math/0610932) — `sources/callan_sierpinski_triangle_prouhet_thuemorse.full.md`,
   `summaries/callan_sierpinski_triangle_prouhet_thuemorse.md`.
   Gives the **explicit inverse** of the Pascal-mod-2 matrix: `S⁻¹ = S(−1)`, a
   (−1,0,1)-matrix with the *same zero pattern as S*, nonzero exactly where
   `i−j free of j` (binary no-carry / `C(i,j)` odd via Kummer), sign
   `(−1)^{b(i−j)}` (Thue-Morse down each column). Plus the `S(x)S(y)=S(x+y)`
   one-parameter family. This formalises the no-carry/submask relation the fold's
   column-hit-set / read-cone functional (GOAL priority 1) is the arithmetic of.
   Structural fact; not a SUPPLY result.

2. **Bacher & Chapman, *Symmetric Pascal matrices modulo p***
   (arXiv:math/0212144) — `sources/bacher_chapman_symmetric_pascal_modp.full.md`,
   `summaries/bacher_chapman_symmetric_pascal_modp.md`.
   Establishes `P(∞) = T·Tᵗ` for the lower-triangular fold family `T`, `det(P(n))=1`,
   `P(n)` positive definite, and the mod-2 characteristic polynomial of the
   symmetric product (p=3 conjectural). The connection to our fold is *indirect*
   (`P` symmetric vs our lower-triangular `Φ`); it confirms the fold's matrix
   algebra is well-behaved. Supporting reference, not a route-closer.

### Honest labels

Both are structural/algebraic facts proved in source; **neither bounds
`wt(Φ_n h)` and neither settles the open request `walsh-spectral-subset-b904`**
(a lower bound on the fold's image weight for sparse input). That gap stays open
as a *theorem to be found*, not literature to be downloaded. Both are consistent
with (do not change) the existing proved claims: `fold-rank-n-minus-2-binomial-proved`,
`enminus2-linear-supply-switch-density-not-necessary`, the hit-set table in
CONCLUSION-PASS2 §5.

## Net effect on the library

- **sources:** 52 → 54 full texts.
- **summaries:** 72 → 74 digests/summaries (both were written as full summaries,
  replacing the auto-digests).
- Derived ledgers re-rendered after each write.
- Durable finding stored to Cognee.

## Why this and not more

`research/ROOT.md` records directive 7/27's search freeze: a role wanting a new
source must first name which unworked FRONTIER candidate it read and why none
answers. This cycle *did* that — the two additions work the exact structural
tier the one open request names, and each was surfaced through `cite_`/`FRONTIER`
(two independent rows). The remaining gap (prove `E[S(n)²]=O(n)` or a
Walsh/subset-sum bound) is in-house computation/theorem, not reachable by
further download; gathering more would serve nothing and would violate the
freeze's intent. Nothing further to add this cycle.

## PostgreSQL-type inventory note

Both new full texts carry the source URL on line 1 (`<!-- source: … -->`) and are
search-reachable via `search_documents` after indexing.
