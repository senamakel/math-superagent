# Scholar digest: reference library against H16.2 (2026-08-18)

`remember_memory` was unavailable during this digest (repeated health timeouts). The findings below are therefore durably written locally and should be retried through Cognee in a later run.

## Object and frame
The problem asks whether the supremum H(n) of isolated periodic orbits of real planar polynomial fields of degree <=n is finite. The displacement function is the return map minus identity. DRR/Roussarie reduce the quadratic question to finite cyclicity of a finite catalogue of compactified limit-periodic graphics. Rousseau–Zhu 2002 states the 121 count and the equivalence at the level of the quadratic normal-form family; no complete modern row-by-row ledger is held, and the library records a 121/125 catalogue discrepancy.

## What the main sources establish

- **DRR 1994** (UHasselt record, http://hdl.handle.net/1942/3763): systematic quadratic program; enumerate graphics/degenerate graphics and prove their finite cyclicity. Record is abstract-level, not the full paper. It establishes the programme and catalogue purpose, not a current complete status table.
- **Dumortier–El Morsalani–Rousseau 1996** (publisher abstract): several elementary quadratic graphics are finitely cyclic by normal forms, Khovanskii/fewnomial methods and center compensation; some regular side transitions are not tangent to identity. Thus a displacement composition must retain nontrivial regular-map jets.
- **DGR 2002** (UHasselt record, http://hdl.handle.net/1942/5292): seven elementary graphics are finitely cyclic: H^3_4,H^3_5,H^3_6,I^2_14a,I^2_15a,I^2_15b,I^2_27. The exact abstract does not supply all numerical bounds.
- **Rousseau–Zhu 2002** (JDE 178, 325–436, full held): all pp-graphics through multiplicity-3 nilpotent elliptic points not surrounding a center are finite; 15 DRR graphics are covered. It states the 121-list reduction. Normal forms, blow-up, first/second Dulac maps and derivation–division are the operative displacement theory.
- **Roussarie–Rousseau 2008** (full held): closes four pp center graphics H^1_7,F^1_7a,H^3_11,I^1_6a, generally cyclicity 2 except a discrete subset in two families. A regular transition has a finite nonzero derivative order, giving a bound through derivation–division.
- **Rousseau–Shan–Zhu 2015** (full held): closes I^1_12 and I^1_13 through a triple nilpotent saddle. Uses nilpotent normal forms, family blow-up, Dulac maps and displacement zero counting.
- **Roussarie–Rousseau 2015** (full held): fully closes I^1_14 through a triple nilpotent point surrounding a center. For I^1_6b, H^3_13 and DI_2b it closes only the boundary limit-periodic set after blow-up. Full cyclicity remains open because the displacement contains four second-type Dulac maps. This contradicts any recollection that all four were closed.
- **Dumortier–Rousseau 2009** (full held): gives 5-parameter normal forms and bounds DF1a <=3 and DF2a <=5; highlights an unresolved desingularization point P*. **Huzak 2018** record states DF2a is finite via slow-divergence/blow-up slow-fast analysis, but the held capture lacks full proof hypotheses and does not transfer to I^1_6b.
- **Mourtada 1991** (full held, DOI 10.5802/aif.1271): generic hyperbolic monodromic k-polycycles satisfying algebraic ratio conditions G(k) have cyclicity <=e(k) in every C-infinity family; an open dense set of degree<=n polynomial fields has a local bound. This is local/generic, not a uniform all-coefficient bound and excludes nonhyperbolic rows.
- **Ilyashenko–Yakovenko 2000; Kaloshin 2000** (full/record held): generic finite-parameter smooth families with elementary singularities/polycycles have uniform Hilbert–Arnold bounds; Kaloshin gives a 2^(25 k^2)-type bound. Elementary is the key hypothesis; nilpotent/degenerate graphics are not covered.
- **Marín–Villadelprat 2025** (JDE 2025, full held): quadratic hyperbolic hemicycles in Q3^R have exact cyclicity 2 (with stated exceptional case); simultaneous upper/lower hemicycles have exact cyclicity 3 or 2 by region. This is a settled hyperbolic DRR-adjacent row, not an open nilpotent graphic.
- **Buzzi–Gasull–Santana 2024** (full held): for a hyperbolic polycycle, cyclicity has lower bound Delta from stability flips; the construction is polynomial/smooth and gives a combinatorial displacement-map lower bound. It reinforces that the open DRR obstruction is nonhyperbolic.
- **Dukov 2023** (full held): in a typical n-parameter family, a hyperbolic n-saddle polycycle's born cycles have multiplicity <=n under an explicit resultant condition L_n !=0. This bounds multiplicity, not the whole count, and is hyperbolic-only.
- **Dumortier–Ilyashenko–Rousseau 2002** (full held): saddle-node normal forms and lips-ensemble results reduce several graphics to finite cyclicity controlled by a finite derivative order; analyticity outside the stable manifold supplies nonflat structure.
- **Panazzolo–Rousseau 2017** (full held): compactified polynomial limit-periodic sets are connected semialgebraic sphere subsets of dimension 0 or 1 up to homeomorphism, with a converse realization theorem. Structural support only; no cyclicity bound.

## Individual finiteness and contradictions

- **Écalle/Ilyashenko history and source** attribute pointwise finiteness of analytic polynomial fields to Écalle 1992/Ilyashenko 1991; Ilyashenko–Yakovenko explicitly state these proofs do not yield uniform H16. **Bamón 1986** independently gives finite cycles for each individual quadratic field, but the held paper is primarily a record/landing capture.
- **Yeung 2024 preprint / 2025 paper** does not claim the individual finiteness theorem false. It claims a gap in Ilyashenko's proof for semi-hyperbolic/nonhyperbolic polycycles: the asymptotic-ordering/leading-term step fails in a logarithmic differential-algebra class. Hyperbolic cases are not challenged; Écalle's route is not challenged. This is a live contradiction to unqualified memory that the Ilyashenko proof is fully settled, not a disproof of H16.

## Abelian/tangential sources

- **BNY 2010**, arXiv:0808.2952: explicit double-exponential bound for zeros of Abelian integrals over nonsingular ovals and first-order cycles in nonconservative Hamiltonian perturbations. It is a regular Gauss–Manin/Fuchsian connection result and does not bound full nonlinear displacement or H(n).
- **Binyamini–Dor 2011**, arXiv:1108.1846: explicit estimate N(n,m) <= exp_+^2(n^2)m + exp_+^5(n^2), linear in perturbation-form degree, for Abelian integrals. Same limitation.
- **BNY special quadratic Hamiltonian** (arXiv:0903.5056): for H=x^2 y(1-x-y) and polynomial form degree n, zeros on the specified oval interval are <=7n/4+9, and the corresponding smooth-cycle perturbation count <=(7n+43)/4. This is a named, sharp-ish special-family target only.
- **GGI 2009**: genus-one quadratic center classes r11/r18 have exact period-annulus cyclicity 2; a three-dimensional Abelian-integral derivative space is Chebyshev. Other listed class counts are conjectural. This is a good Lean-friendly validation target.
- **GMV 2008**: ECT criteria apply to specified first-order Abelian-integral families under separated-Hamiltonian and Chebyshev hypotheses. The held library explicitly finds these hypotheses absent for the complete I^1_6b four-Dulac displacement; no reduction to one Abelian family is established.
- **Luca et al. 2009**: alien cycles near a cubic Hamiltonian 2-saddle cycle can arise from higher transition-map derivatives despite Abelian-integral zero data. Therefore Abelian zeros do not by themselves control nonlinear polycycle displacement.
- **An–Dai–Hu 2025**: special hyperelliptic first-kind integral classes are claimed Chebyshev/at most one zero, but exact hypotheses were not fully extracted. It does not bear on general H16.
- **Yang 2025**: claims weak H16 solved for a restricted cubic isochronous Hamiltonian class with maximum n-1 cycles, attained. Restricted/tangential only.
- **Christopher–Li–Torregrosa 2024**: held only as TOC/catalogue; chapter titled “A Unified Proof of the Weak Hilbert’s 16th Problem for n=2”. It is a book-form anchor for weak H16, not a proof read in this run.

## Lower bounds and obstruction tests

- **Bautin 1952 primary**: M(2)=3, the maximum local small-amplitude quadratic focus/center cyclicity, with a realizing example. This is not H(2).
- **Galias–Tucker 2022**: interval arithmetic certifies exactly four cycles in Songling's quadratic system, at scales from ~4e-2 to ~7e-75. Thus H(2)>=4 has verified-computational support.
- **Prohens–Torregrosa 2019**: H(4)>=28,H(5)>=37,H(6)>=53,H(7)>=74,H(8)>=96,H(9)>=120,H(10)>=142 via reversible centers and simultaneous Hopf cycles; these are sourced lower bounds.
- **Torregrosa 2024**: explicit cubic families with twelve local cycles. Local lower-bound validation only; it does not establish H(3) optimality.
- **Llibre–Zhang 2017**: classical Lienard conjecture true for n<=4, false for n>=6 with at least n-2 cycles, n=5 open. Slow-divergence/canard mechanisms directly implement the slow-fast test.
- **Christopher–Lloyd / modern canard sources**: n^2 log n lower growth is recorded in the existing library; it rules out quadratic upper bounds. The Álvarez et al. 2020 local capture is broken and cannot be used as primary evidence; its claim is carried only at review-level.

## Suspect claimed resolutions

- **Pedregal 2021** claims a quartic-in-n upper bound and H(2)=4 through a variational global-minimizer argument, but is unrefereed and does not exhibit the analytic/quasianalytic return-map step required by the smooth test. Current community sources still treat H16.2 as open.
- **Buzzi–Novaes 2024** refute a different information-geometry quadratic formula using n^2 log n lower growth and discuss further defects. No global solution is accepted.
- **Lu 2026** claims local uniform finite cyclicity of H^3_14, exactly a formerly open semihyperbolic graphic. Only its finite algebraic core is independently checked in this workspace; analytic remainder/domain/root-unicity claims remain unverified and the preprint is unrefereed.

## Sources that do not help / evidence limitations

- DRR 1994 UHasselt record is abstract/metadata only: useful for programme/catalogue, not for exact row ledger.
- Ilyashenko 2002 AMS “primary” landing copy is a publisher page with no article mathematics; use the held PDF/full conversion instead.
- Kaloshin and Ilyashenko–Yakovenko duplicate abstract/landing files add provenance but no mathematical detail beyond the full sources.
- Binyamini–Dor IOP record is a CAPTCHA; use the arXiv/ar5iv/full source.
- Christopher–Lloyd 1995 Crossref digest is empty metadata; it does not support the n^2 log n bound by itself.
- Li–Liu–Yang 2009 landing/redirect is not mathematical; the H(3)>=13 claim remains anchored by other held survey/source material, not that file.
- Huzak 2018 held capture is only an abstract/record; do not use it for detailed parameter boxes or remainder estimates.
- Álvarez et al. 2020 held Elsevier capture is a redirect stub; only the MaRDI-level claim is available.
- `research/sources/llibre-zhang-lienard-conjecture-survey.full.md` is contaminated: unrelated German power-grid paper. Use the full UAB postprint instead.
- `research/sources/dulac` full primary 1923 text was not obtained; the historical smooth-test warning is supported by later sources.
- General encyclopedia/Wikipedia/MathWorld sources are orientation only, not primary evidence.

## Contradictions to flag

1. Any assertion that RR 2015 closed I^1_6b, H^3_13 and DI_2b fully is contradicted by the source: only boundary sets were closed.
2. Any assertion that H(2)<∞ or H(2)=4 is contradicted by the current status sources and the lack of a complete analytic proof.
3. Any assertion that Lu 2026 is established is contradicted by its evidence status: unrefereed, with only algebraic core independently verified.
4. Any unqualified assertion that Ilyashenko's pointwise proof is settled is contradicted by Yeung's live gap claim; the theorem itself is not refuted.
5. Any assertion that Abelian-integral zero bounds imply full H16.2 is contradicted by the alien-cycle source and by the distinction between smooth ovals and saddle/polycycle displacement.
6. Any claim that the 121 row inventory is complete/current is contradicted by the held 121/125 discrepancy and missing DRR primary catalogue.
