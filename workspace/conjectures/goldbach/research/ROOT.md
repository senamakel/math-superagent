# Binary Goldbach library status (cycle 2026-08-18)

**Sources added this cycle:** Alsetri–Shao, *Density versions of the binary Goldbach problem* (arXiv:2405.18576); Huang–Li, *On the Connection Between the Goldbach Conjecture and the Elliott–Halberstam Conjecture* (2021); Bauer, *Large sieve inequality with sparse sets of moduli applied to Goldbach conjecture* (2017); Friedlander–Goldston, *Some singular series averages and the distribution of Goldbach numbers in short intervals* (1995); Daniel–Njagi–Mutembei, numerical verification claim to 9×10^18 (Zenodo 10391440). Full texts are under `research/sources/`; summaries are under `research/summaries/`.

## Established

- **Asserted-by-source, primary verified:** Oliveira e Silva–Herzog–Pardi verified every even n≤4×10^18, double-checked to 4×10^17, using a segmented mod-30 sieve; source DOI 10.1090/S0025-5718-2013-02787-1. Falsifier: an independently checked counterexample ≤4×10^18 or an error in the published computation.
- **Asserted-by-source:** Chen’s theorem gives p+P₂ for sufficiently large even n; the explicit exp(36) threshold is in Bordignon 2022 and the exp(exp 32.7) result in Bordignon–Johnston–Starichkova. Falsifier: a source-level correction changing the hypotheses or threshold.
- **Asserted-by-source:** Unconditional exceptional-set results remain count estimates, not all-n results; the library records Lu’s published exponent and newer unrefereed claims separately. Falsifier: a published theorem proving E(X)=0 beyond an effective threshold.
- **Asserted-by-source:** Helfgott proves every odd integer >5 is a sum of three primes; this does not imply binary Goldbach. Falsifier: a valid reduction from ternary to binary not already known to require the target conjecture.
- **Asserted-by-source:** Alsetri–Shao prove: if a subset A of primes has relative density δ>1/2 in every reduced residue class, almost all even integers are sums of two A-primes; 1/2 is sharp, since arbitrarily dense subsets can miss a positive proportion. Source: https://arxiv.org/abs/2405.18576. Falsifier: a counterexample to their stated density hypotheses or an all-n conclusion (which the theorem does not claim).
- **Asserted-by-source, conditional:** Huang–Li show sufficiently large binary Goldbach follows from Elliott–Halberstam plus a Möbius-twisted Elliott–Halberstam hypothesis with levels θ,θ′ satisfying θ+θ′>1. Source: https://doi.org/10.1007/978-3-030-67996-5_17. Falsifier: a theorem statement in the full chapter requiring different hypotheses.

## Ruled out

- Pure classical sieve route: parity problem leaves p+P₂ rather than p+p.
- Direct binary circle-method route: minor-arc error is not controlled for every n.
- Structural-closure inference from exceptional-set bounds: exact Goldbach failure is not known to be closed under translations or multiplication; the prior finite oracle found no supporting closure law.
- Naive use of density-restricted results: Alsetri–Shao’s sharpness example shows density >1/2 (even 1−ε) does not force all even sums for arbitrary prime subsets.

## Gaps

- Exact machine-readable primary text of Montgomery–Vaughan 1975 remains unavailable locally; current claims rely on later sources and scans.
- Chen’s original 1973 paper remains unavailable; explicit modern sources are held.
- The Daniel et al. 9×10^18 claim is not accepted as the authoritative record without independent verification; it is a lead, not a replacement for 4×10^18.

The phase-1 minimum is already met in `research/ROOT.md`: minimal-counterexample structure, current authoritative verification bound, and at least three settled restricted classes are stated. Further acquisition should target the open requests or frontier, not general browsing.