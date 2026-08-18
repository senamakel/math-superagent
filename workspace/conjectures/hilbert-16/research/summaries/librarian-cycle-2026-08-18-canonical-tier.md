# Librarian cycle: canonical and thin-angle verification (2026-08-18)

## Sources read and available locally
The canonical orientation tier is already on disk:
- `research/sources/han-li-li-scholarpedia-limit-cycles.full.md`, Scholarpedia 5(8):9648 (2010), URL http://www.scholarpedia.org/article/Limit_cycles_of_planar_polynomial_vector_fields.
- `research/sources/canonical-encyclopedia-limit-cycle.full.md`, Encyclopedia of Mathematics, URL http://encyclopediaofmath.org/wiki/Limit_cycle.
- `research/sources/canonical-mathworld-hilbert-problems.full.md`, Wolfram MathWorld, URL https://mathworld.wolfram.com/HilbertsProblems.html.
- `research/sources/ilyashenko-centennial-history-hilbert-16.full.md`, Ilyashenko, Bull. AMS 39 (2002), URL https://www.ams.org/journals/bull/2002-39-03/S0273-0979-02-00946-1/S0273-0979-02-00946-1.pdf.

Primary and survey sources already held for the main technical angles include BNY 2010, Binyamini–Dor 2011/2012, Kaloshin 2001, Kaleda–Shchurov 2011, RSZ 2015, RR 2015, Zhu–Rousseau 2002/2004/2005, Bautin 1952, and Gasull–Santana 2025; see `research/LIBRARY-STATUS.md` and `research/sources/`.

## Verified source-backed claim blocks

### Canonical object and status — asserted-by-source
The Encyclopedia of Mathematics defines a limit cycle as an isolated closed trajectory, i.e. a periodic nonconstant solution isolated among periodic trajectories. Its Hilbert-16 section states that each polynomial vector field has finitely many limit cycles, attributed to Écalle and Ilyashenko, while no coefficient-uniform bound is known even for degree 2. The page explicitly points to the Poincaré return map as the mechanism for stability and bifurcation.

**Falsifier:** a primary source proving a finite coefficient-uniform H(2), or disproving individual finiteness.

### Canonical historical statement — asserted-by-source
Ilyashenko's 2002 Bull. AMS survey states the polynomial/analytic individual finiteness theorem, distinguishes it from the uniform H(n) question, and describes the quadratic problem as unresolved. The source is a survey, not an independent proof in this run.

**Falsifier:** a verified primary proof of H(2)<∞ or a source overturning the finiteness theorem.

### Tangential H16 — asserted-by-source
BNY 2010 gives a constructive double-exponential bound for zeros of Abelian integrals arising from nonsingular compact ovals in polynomial Hamiltonian perturbations. Binyamini–Dor 2011/2012 give an explicit uniform improvement linear in deg(ω), with explicit dependence on deg(H). This is a first-order/tangential result and does not settle full H16.2; alien-cycle sources in the library warn that Abelian-integral zero counts alone do not control all higher-order cycles.

**Falsifier:** a source showing the hypotheses cover arbitrary polynomial vector fields, or a counterexample to the stated zero bound.

### Elementary polycycles — asserted-by-source
Kaloshin's Hilbert–Arnold notes and the Kaleda–Shchurov paper cover elementary singularities in generic finite-parameter families, with finite cyclicity and explicit bounds. The nonzero-eigenvalue/elementarity hypothesis is essential in the cited statements and does not cover nilpotent or degenerate DRR graphics.

**Falsifier:** a cited theorem with no elementarity/genericity assumption covering the degenerate classes.

### DRR status — asserted-by-source, incomplete ledger
Held sources establish the DRR reduction to 121 graphics; RSZ 2015 says its two closures bring the count to 88, and RR 2015 fully closes I^1_14 while proving only boundary-set cyclicity for I^1_6b, H^3_13, DI_2b. H^3_14 is named as the one triple-point-at-infinity graphic with no partial result in RR 2015. Shan's 2013 thesis uses a 125-graphic convention and reports 11 degenerate graphics open. Huzak 2018 closes DF_2a; Lu 2026 is an unrefereed claim for H^3_14 with only its finite algebraic core independently recomputed in this workspace. No consolidated post-2020 121-row ledger is held.

**Falsifier:** a primary complete 121-row catalogue or post-2020 status table disagreeing with these labels/counts.

## Search and triage record
Searches were run for: canonical H16/limit-cycle references; DRR 121-graphic status; elementary polycycles/Kaloshin; Abelian-integral bounds; and H(2), H(3), and asymptotic lower bounds. `citation_graph` was run on Ilyashenko 2002 and BNY 2010; their citation summaries are in `research/summaries/citations_w*.md` and frontier leads are in derived/FRONTIER.md. The sources searched in this cycle were already present locally, so duplicate downloads were correctly refused by the library validator. No source was cited without a local file.

## Coverage decision
`research/ROOT.md` already meets the minimal library threshold: it states the minimal obstruction structure, current verification boundary, and at least three settled restricted classes. This cycle therefore adds no invented URLs and records no unsupported expansion of the claims.
