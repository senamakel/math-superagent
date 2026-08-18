# Scholar digest — Hilbert 16.2 investigation

The reference library was read against `problem.md` and `GOAL.md`. Durable-memory writes were attempted for each finding but the Cognee memory server timed out; this note is the fallback durable workspace record.

## Load-bearing sources and implications

- **DRR 1994; RSZ 2015; RR 2015; Zhu–Rousseau 2002/2004; Zhu 2005; DGR 2002; DIR 2002; Roussarie–Rousseau 2008; Dumortier–Rousseau 2009; Huzak 2018.** These establish the reduction of quadratic H(2) to finite cyclicity of the DRR graphics and prove finite cyclicity for restricted elementary, pp, nilpotent, saddle-node, center and some degenerate classes. RR 2015 fully closes `(I^1_14)` but only the boundary limit-periodic sets of `(I^1_6b)`, `(H^3_13)`, `(DI_2b)`; their full cyclicity remains open. There is no authoritative consolidated post-2020 121-row ledger; Shan's 125 count uses a different convention. Implication: target a named unresolved graphic, not H(2) globally.

- **Ilyashenko/Écalle; Kaloshin; Ilyashenko 2016; Yeung 2024/25.** Ilyashenko/Écalle sources state individual analytic/polynomial finiteness; Ilyashenko 2016 advertises a revised “superexact asymptotic series” proof. Yeung claims a gap in the non-hyperbolic polycycle ordering step, with an explicit obstruction. The theorem is not disproved, but proof completeness is contested. Bamón independently supports individual quadratic finiteness. Implication: never infer uniformity from pointwise finiteness; locate the analytic/quasianalytic displacement-map step explicitly.

- **Speissegger 2018; Kaiser–Rolin–Speissegger 2009.** If parametric transition-map relations are definable in an o-minimal structure, finite fibers imply a uniform bound. Full transition-map o-minimality is open; the non-resonant hyperbolic class is proved. This gives the correct uniformity mechanism and does not cover nilpotent/semi-hyperbolic DRR targets.

- **Novikov–Yakovenko 2002; Gavrilov 1999; Binyamini–Novikov–Yakovenko 2010; Binyamini–Dor 2012; GMV and GGI.** Under regular-at-infinity/nondegenerate-leading-part or Morse/nonsingular-oval hypotheses, Abelian integrals form finite-rank Picard–Fuchs/Petrov modules and have explicit zero bounds: BNY double exponential in degree, BD linear in `deg ω`. GGI gives exact cyclicity two for named genus-one quadratic centers. These are first-order/tangential results only and do not control nonlinear displacement near singular/polycycle levels.

- **Bautin 1952 and workspace exact algebra.** Bautin proves local quadratic focus/center cyclicity `M(2)=3`, not global `H(2)`. Exact workspace recurrence checks `8L4=AC+CD+2DF−EF`, `192L6+P30=0`, `L8 ∉ <L4,L6>`, and `L10,L12 ∈ <L4,L6,L8>`; Lean checks the finite certificates. This is useful finite algebra, not a proof of graphic finite cyclicity.

- **Lower bounds.** Galias–Tucker certify exactly four cycles in the Songling quadratic system, hence `H(2)≥4`. Held literature gives `H(3)≥13`, `H(4)≥28`, `M(3)≥12` (Torregrosa 2024), and asymptotic lower growth at least order `n^2 log n`; the latter rules out quadratic upper formulas. Constructions remain source-backed unless independently recertified.

- **Lu 2026.** The unrefereed preprint claims local uniform finite cyclicity of `(H^3_14)`, formerly the graphic with no partial result. The exact Bautin/Darboux core is independently computed and Lean-checked in this workspace, but root uniqueness, domain completeness, Hadamard divisibility and zero-theorem steps remain unchecked; the bound is existential. Treat the theorem as asserted-by-source, not established. The bundle scripts are held but not clean-room re-executed; stale memory saying they were not held is contradicted by the library.

- **Pedregal 2021 and Buzzi–Novaes 2024.** Pedregal's variational claim `H(n)` quartic and `H(2)=4` is unrefereed and does not analyze analytic return-map/displacement zeros, so it fails the smooth/analyticity test prima facie. Buzzi–Novaes reject the related closed formula and cite the `n^2 log n` lower growth. Do not use either as a solution.

## Sources that do not help directly

- Hilbert 1900 is only the canonical problem statement.
- BIRS 2007, Ilyashenko 2002, Han–Li–Li and the 2024 textbook are surveys/context, useful for framing but not new proof ingredients.
- Gasull–Santana's monomial-count variant addresses a different invariant, not degree-based H(n).
- Liénard surveys and canard/slow–fast papers provide restricted constructions/lower bounds, not a uniform degree-n upper bound.
- Galias–Tucker/Yu–Zeng lower-bound papers do not prove upper bounds; numerical phase portraits alone would not certify cycles, though Galias–Tucker's interval proof is useful oracle methodology.
- Landing pages, bibliographic records, paywalled abstracts, and the contaminated `llibre-zhang-lienard-conjecture-survey` file (actually an unrelated power-grid paper) cannot support mathematical claims. Dulac's full 1923 scan was not obtainable.

## Contradictions flagged

1. Individual finiteness “proved” by Écalle/Ilyashenko versus Yeung's published gap claim: theorem status is contested, not refuted.
2. DRR count 121 versus Shan's 125 convention.
3. RR 2015 closes one full center graphic, not four; earlier “all four closed” wording is wrong.
4. Lu bundle scripts are held, contrary to stale memory, but not independently verified.
5. `M(3)≥12` supersedes older `M(3)≥11`; `H(2)=4` remains a lower bound/conjecture, not equality.

## Partial-result conclusion

The defensible next attack is a displacement-function proof for one of `(I^1_6b)`, `(H^3_13)`, `(DI_2b)`, using RR's center-ideal/Bautin-trick and blow-up framework, with the missing analytic zero theorem isolated. The finite algebraic core can be carried in Lean; the analytic transition-map and uniformity steps cannot yet be claimed formalised. No source establishes H(2)<∞ or H(2)=4.