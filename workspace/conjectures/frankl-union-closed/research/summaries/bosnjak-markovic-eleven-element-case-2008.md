# Bošnjak–Marković, "The 11-element case of Frankl's conjecture" — summary

**Source:** Ivica Bošnjak, Petar Marković. *Electronic Journal of Combinatorics* 15(1), #R88 (2008). DOI: https://doi.org/10.37236/812
**Full text on disk:** `research/sources/bosnjak-markovic-eleven-element-case-2008.full.pdf.full.md` (downloaded from the author's page: https://people.dmi.uns.ac.rs/~markovicp/papers/2008-Frankl11.pdf)
**Also present:** structural digest `research/sources/bosnjak-markovic-eleven-element-case-2008.full.pdf.md`, and the earlier abstract stub superseded by this note.

## What it establishes

**Theorem 3.1.** If a finite union-closed family `F ≠ {∅}` has ground set `|⋃F| ≤ 11`, then some element belongs to at least half the members of `F`. This is the n≤11 verification bound for Frankl's (union-closed sets) conjecture.

## Method — the weight-function framework

- **Lemma 2.1 (weight criterion):** `F` satisfies Frankl's conjecture iff there is a non-negative weight function `w` on `X = ⋃F` with `Σ_{A∈F} Σ_{x∈A} w(x) ≥ (1/2) Σ_{A∈F} Σ_{x∈X} w(x)` — i.e. a weighting under which the average abundance is ≥ 1/2. This is the averaging/weight formulation from earlier work (Marković's analysis of "Frankl's conjecture"), restated here as an iff.
- **Lemma 2.2:** a family containing a 1- or 2-element set satisfies the conjecture (re-proves the folklore Sarvate–Renaud observation).
- **Lemma 2.3:** an S-hypercube counting lemma bounding how many level-k subsets of a level-l set can lie in `F`, using only counts of what is/ isn't in `F` at one level; the engine of the case analysis.
- **Propositions 2.1–2.3, Theorem 2.1:** several local configurations of 3-sets already force Frankl's property (three 3-sets inside one 4-set; three 3-sets sharing a common 2-set; {a,b,c},{a,b,d},{c,d,e}; three 3-sets inside a 5-set).
- **Section 3 (the |X| = 11 case):** a chain of lemmas — if `F` contains two 3-sets with 2-element intersection, or three 4-sets in a 5-set, or three 4-sets sharing a common 3-set, or two 4-sets in a 5-set, or two intersecting 3-sets, or any two 3-sets, or a 4-set with one of its 3-subsets, or a disjoint 3-set and 4-set, or any 3-set at all, or a 5-set with a 4-subset, or any 4-set — then `F` is Frankl's. Since every nontrivial union-closed family on 11 elements contains one of these configurations, **Theorem 3.1** follows.

## Why it matters for this workspace

- Together with the Lo Faro / Roberts–Simpson bound (a counterexample on an m-element ground set has at least 4m−1 member sets), n≤11 settles every union-closed family with at most 40 member sets; ROOT.md states this line.
- The 12-element case (Vučković–Živković, in library) is computer-assisted; this paper is the largest *human-proof* ground-set verification and the structural, weight-based route to it (relevant to the oracle's LP / weight-certificate plans).
- Its Section 2 weight criterion is exactly the "averaging / FC-family" machinery the oracle can certify for small `n`.