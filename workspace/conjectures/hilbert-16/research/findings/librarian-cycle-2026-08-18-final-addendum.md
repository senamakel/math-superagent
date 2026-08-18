# Library-building cycle run record — 2026-08-18

## Problem restatement and search
The object is H16.2: for polynomial planar fields X=(P,Q), P,Q∈R[x,y], max degree ≤n, H(n) is the supremum of isolated periodic orbits; the open question is whether H(n)<∞ for every n≥2. The displacement function is return map minus identity. Search covered canonical entries, DRR quadratic graphics, elementary-polycycle bounds, Abelian-integral bounds, and lower bounds. Citation graphs were run for Rousseau–Shan–Zhu 2015, Binyamini–Dor, and Christopher–Lloyd; similar-source searches were run for the first two.

## New/confirmed local holdings
- `research/sources/rousseau-rousseau-2015-center-graphics-arxiv.full.md`, URL https://arxiv.org/abs/1506.07104; summary updated at `research/summaries/rousseau-rousseau-2015-center-graphics-arxiv.md`. Primary abstract confirms finite cyclicity of I^1_14 and boundary limit-periodic sets in I^1_6b, H^3_13, DI_2b.
- `research/sources/binyamini-dor-petrov-khovanskii-2011-ar5iv.full.md`, URL https://ar5iv.labs.arxiv.org/html/1108.1846; summary updated at `research/summaries/binyamini-dor-petrov-khovanskii-2011-ar5iv.md`. Theorem 5 gives N(n,m)≤exp_+^2(n²)m+exp_+^5(n²) for Abelian-integral zeros under its stated Hamiltonian/oval hypotheses.
- `research/sources/sun-dai-hyperelliptic-zeros-2025-primary.html.full.md` and `research/sources/an-dai-hu-chebyshev-hyperelliptic-2025.html.full.md` were already held; a joint summary was added at `research/summaries/hyperelliptic-special-families-2025.md`. These are restricted special-family leads, not yet promoted beyond asserted-by-source because full theorem hypotheses require extraction.
- Canonical Wikipedia, MathWorld, and Encyclopedia of Mathematics records are already held locally and treated as orientation, not sole evidence.

## Formalisation
Added `code/lean/Lib/StatementLibraryCycle.lean`, a typed H16.2 blueprint. It explicitly represents polynomial fields and degree bounds, and exposes the missing flow/return-map/isolated-periodic-orbit interface rather than pretending Mathlib supplies it. It is a statement blueprint, not a proof; the existing Lean tree also contains the earlier fuller Statement and cited-result files.

## Status and limitations
`research/ROOT.md` already satisfies the phase-1 stopping criterion: minimal obstruction (infinite cyclicity of a compactified limit-periodic set/graphic), current verification boundary, and at least three settled restricted classes. The complete 121-graphic ledger remains unavailable; 121/125 catalogue conventions conflict. The full H(2) problem remains open. Cognee indexing was unavailable during this cycle, so durable findings are recorded in this workspace file and the source summaries instead.

## Complexity / oracle note
No full-size brute-force search was run. Existing local computations are exact symbolic Bautin certificates; they are evidence for finite algebraic claims, not a solver for H16.2. The naive oracle is retained under `code/naive_examples_oracle.py` and its capture. No larger run was needed: scaling would not resolve the stated library gaps; the next useful action is a source-backed DRR ledger or extraction of exact hypotheses for a special Abelian family.
