# Koshelev & Koshka, "Combinatorial Geometry of Erdős–Szekeres Type Problems: SAT/ASP Modeling and Linear Subreduction" (2026)

> **Source:** V. Koshelev and A. Koshka, arXiv:2604.20120 (math.CO), submitted 22 Apr 2026. Preprint, not peer-reviewed as far as the library knows.
> Full text: `research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md`

**Role in this run:** methodology source for the SAT/ASP + realizability arm; reproduces the ES(6)=17 boundary with explicit integer coordinates the oracle can check. NOT an ES(7) attack (that would be adjacent drift).

## What it establishes

- **Linear subreduction (§5.2):** feed the *whole* logical formula (signotope axioms + geometric inequalities) to an SMT solver (Z3) with abscissae fixed (x_i = i, or exponential spacing), turning orientation determinants into linear-integer constraints. Authors' caveat: fixing x can in principle lose realizations; empirically, almost all SAT-confirmed signotopes realize with x_i = i.
- **Signotope axiom (§4.2):** per 4-tuple a<b<c<d exactly one sign change in (L_abc, L_abd, L_acd, L_bcd), 8 clauses — the same orientation-variable model the run's SAT arm must mirror.
- **ASP (clingo frumpy/crafty)** reproduces ES-boundary values in 70–190 min without manual decomposition.
- **Exact values:** h(6,≥2)=17, h(6,1)=18 — every 17-point set has a convex hexagon with ≤2 interior points, every 18-point set one with ≤1 interior point. Explicit 17-point integer-coordinate set with no empty/1-interior hexagon: a concrete oracle test case at the ES(6)=17 boundary.
- **Adjacent values** h_nc(4,0;4,0)=26 and R_EC(3,3)=21 (bicolored / geometric-Ramsey variants): NOT ES(7) progress — drift guard.

## Claims

```claim
id: kk-linear-subreduction
statement: A signotope satisfying a boolean geometric formula can be realized (given it is realizable) by feeding the full formula to an SMT solver with abscissae fixed (x_i=i or exponential), turning the orientation determinants into linear-integer constraints; empirically succeeds for almost all SAT-verified signotopes.
hypotheses: point set in general position; orientation of each triple encoded as a boolean; any realizable signotope has some realization (fixing x needs the set to admit those abscissae).
holds-here: true for the run's realizability arm, with the caveat the authors themselves state — fixing x can in principle exclude realizations, and the claim is empirical, not a theorem.
status: asserted-by-source (2026 preprint; not independently reproduced here).
bearing: gives the run's SAT/ASP + SMT arm a concrete realizability method for ES(5)/ES(6) reproduction and any ES(7) candidate realization, and an explicit integer-coordinate route.
anchor: research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md
```

```claim
id: kk-h61-h62
statement: h(6,1)=18 and h(6,≥2)=17, i.e. every 17-point set in general position contains a convex hexagon with ≤2 interior points, and every 18-point set contains one with ≤1 interior point; an explicit 17-point set with neither an empty nor a 1-interior hexagon is given by integer coordinates.
hypotheses: points in general position; hexagon interior-point counts as defined.
holds-here: true and relevant — refines/pins the ES(6)=17 boundary; explicit coordinates are an oracle checkpoint.
status: asserted-by-source (computer-assisted, clingo ASP; preprint; not re-derived here).
bearing: a concrete 17-point configuration to feed the oracle, and an upper bound consistent with ES(6)=17.
anchor: research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md
```

```claim
id: kk-adjacent-not-esz7
statement: The exact values h_nc(4,0;4,0)=26 and R_EC(3,3)=21 concern bicolored point sets and geometric Ramsey numbers respectively, NOT the planar Erdős–Szekeres ES(7)=33 conjecture.
hypotheses: none beyond the definitions of the bicolored/Ramsey variants.
holds-here: FALSE relevance — adjacent problems; do not cite as ES(7) progress.
status: asserted-by-source.
bearing: drift guard — keeps the run from mistaking these exact values for progress on ES(7).
anchor: research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md
```